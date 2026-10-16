"""PTX unroll-and-batch: the load reorder that won on every CUDA kernel of the 13 Oct H100 run, as a compiler pass.

Hand reorders (FAISS k-select, Rodinia particle filter, llama.cpp rms_norm, PyTorch EmbeddingBag, Aerial cfo) all did
the same thing in the source: take a strided loop, group k consecutive iterations, issue every load of the group
first, then run the k bodies in their original order. ptxas never does this: it will not move a load above a store
of a pointer it cannot prove disjoint (two plain ``double*``), and it does not unroll loops with large or branching
bodies. This pass does it on the PTX, for any kernel (nvcc ``-ptx`` / NVRTC / Triton), with a proof per load:

  loop     a label L whose only incoming branch is the back-edge ``@%p bra L`` at the end of the body; every other
           branch in the body targets a label inside it (no break, no call, no ret, no bar.sync / membar / atomics);
  prefix   the body's straight-line start (up to its first branch or label): always executed, once per iteration;
  suffix   the body's straight-line end (from its last label to the back-edge): same;
  induction  registers the prefix's load addresses depend on that the body redefines: each must be defined exactly
           once, in the suffix, by a pure instruction (add / sub / mul / mad / shl / cvt / mov ...) of induction
           registers and loop invariants. Applying that update chain j times gives iteration j's addresses;
  load     an unpredicated, non-volatile ``ld.global`` in the prefix whose address is a pure slice of induction
           registers and invariants. It may cross a ``st.global`` of the body only when both addresses trace to
           single, different kernel parameters (``ptx_readonly``'s provenance); the launch guard then has to
           confirm those arguments do not overlap. Loads from parameters a store of unknown provenance may alias
           are refused; ``.shared`` / ``.local`` stores are not in the way.

Output for factor k (k = 1 only hoists the body's loads above its stores):

    L_main:  i_1 .. i_{k-1} := update chain applied 1 .. k-1 times (fresh registers)
             @!(iteration k-1 still inside the loop) bra L          ; fewer than k left: the original loop
             all loads of copies 0 .. k-1 (fresh destination registers, address slices rebuilt per copy)
             body copy 0 .. k-1 (loads replaced by ``mov`` from the fresh registers, labels renamed, the back-edge
             of copies 0 .. k-2 dropped; copy k-1 branches to L_main or to the exit)
    L:       the original loop, unchanged (the tail)
    L_exit:  the original fall-through

The values every body copy computes are exactly those of k consecutive iterations of the original (same
instructions, same order, same operands; only the load issue point moves), so outputs are bit-identical.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field

from .ptx_readonly import _INSTR, _REG, _split_functions, _PROPAGATE

_ANY_PARAM = re.compile(r"\.param\s+(?:\.align\s+\d+\s+)?\.\w+\s+(\w+)(?:\[\d+\])?\s*(?:,|\)|$)", re.M)
_LD_PARAM_OFF = re.compile(r"ld\.param\.(?:u64|b64|s64)\s+(%\w+)\s*,\s*\[\s*(\w+)\s*(?:\+\s*(\d+)\s*)?\]")


def _provenance(lines, start, end, params):
    """Fixed point: register -> frozenset of pointer sources, a source being "param" or "param+offset" (a pointer
    field of a struct parameter passed by value: different fields are different pointers)."""
    bases: dict[str, frozenset] = {}
    seeds, instrs = [], []
    for k in range(start, end + 1):
        line = lines[k]
        m = _LD_PARAM_OFF.search(line)
        if m and m.group(2) in params:
            seeds.append((m.group(1), m.group(2) + (f"+{m.group(3)}" if m.group(3) else "")))
            continue
        mi = _INSTR.match(line)
        if mi:
            instrs.append((mi.group(1), mi.group(2)))
    # pointer seeds: parameter fields that reach an address operand or cvta.to.global through pointer-preserving
    # ops only (mov / cvta / add / sub / selp / cvt). Integer fields (sizes, strides) go through mul / shl first
    # and are not pointer sources, even though they end up in an address.
    ptr_like = ("mov", "cvta", "add", "sub", "selp", "cvt")
    reach: dict[str, frozenset] = {dst: frozenset({src}) for dst, src in seeds}
    changed = True
    while changed:
        changed = False
        for op, rest in instrs:
            if not op.startswith(ptr_like):
                continue
            regs = _REG.findall(rest)
            if not regs:
                continue
            dst, srcs = regs[0], regs[1:]
            if op.startswith("selp"):
                srcs = srcs[:-1]
            acc = frozenset()
            for r in srcs:
                acc |= reach.get(r, frozenset())
            if acc and not acc <= reach.get(dst, frozenset()):
                reach[dst] = reach.get(dst, frozenset()) | acc
                changed = True
    pointer_sources = set()
    for op, rest in instrs:
        if op.startswith("cvta.to.global"):
            regs = _REG.findall(rest)
            if len(regs) >= 2:
                pointer_sources |= reach.get(regs[1], frozenset())
        m = re.search(r"\[\s*(%\w+)", rest)
        if m and (op.startswith("ld.") or op.startswith("st.") or op.startswith("atom") or op.startswith("red.")):
            pointer_sources |= reach.get(m.group(1), frozenset())
    for dst, src in seeds:
        if src in pointer_sources:
            bases[dst] = bases.get(dst, frozenset()) | {src}
    changed = True
    while changed:
        changed = False
        for op, rest in instrs:
            if not op.startswith(_PROPAGATE):
                continue
            regs = _REG.findall(rest)
            if not regs:
                continue
            dst, srcs = regs[0], regs[1:]
            if op.startswith("selp"):
                srcs = srcs[:-1]
            acc = frozenset()
            for r in srcs:
                acc |= bases.get(r, frozenset())
            if acc and not acc <= bases.get(dst, frozenset()):
                bases[dst] = bases.get(dst, frozenset()) | acc
                changed = True
    return bases

_LABEL = re.compile(r"^\s*(\$?[A-Za-z_][\w$]*)\s*:\s*(?://.*)?$")
_BRA = re.compile(r"^\s*(@!?%\w+\s+)?bra(?:\.uni)?\s+(\$?[\w$]+)\s*;")
_REG_DECL = re.compile(r"^\s*\.reg\s+\.(\w+)\s+(%[A-Za-z_]+)<(\d+)>\s*;")
_PRED = re.compile(r"^\s*@(!?)(%\w+)\s+")
_PURE = ("add", "sub", "mul", "mad", "shl", "shr", "cvt", "mov", "and", "or", "xor", "neg", "min", "max", "cvta",
         "mul.wide", "mul.lo", "mad.lo", "mad.wide", "not")
_BARRIER_OPS = ("bar.red", "bar.arrive", "membar", "fence", "atom", "red.", "call", "ret",
                "exit", "st.volatile", "ld.volatile", "cp.async", "st.async", "mbarrier", "wmma", "mma", "brx",
                "multimem", "trap")
# a block barrier inside the loop is allowed: it orders shared memory and the trip count is block-uniform whenever
# the original kernel is correct; only loads of buffers the kernel never writes may then be batched (they cross it)
_BLOCK_BARRIER = ("bar.sync", "barrier.sync", "bar.warp.sync")


@dataclass
class Report:
    kernel: str
    loops: list = field(default_factory=list)
    transformed: int = 0

    def line(self, s):
        self.loops.append(s)


class Ins:
    __slots__ = ("idx", "text", "label", "op", "rest", "pred", "pred_neg", "target", "dst", "dsts", "srcs", "is_ins")

    def __init__(self, idx, text):
        self.idx, self.text = idx, text
        self.label = self.op = self.rest = self.pred = self.target = None
        self.pred_neg = False
        self.dst, self.dsts, self.srcs, self.is_ins = None, [], [], False
        m = _LABEL.match(text)
        if m:
            self.label = m.group(1)
            return
        mi = _INSTR.match(text)
        if not mi:
            return
        self.is_ins = True
        self.op, self.rest = mi.group(1), mi.group(2)
        mp = _PRED.match(text)
        if mp:
            self.pred, self.pred_neg = mp.group(2), mp.group(1) == "!"
        mb = _BRA.match(text)
        if mb:
            self.target = mb.group(2)
        regs = _REG.findall(self.rest)
        if self.op.startswith(("st.", "bra", "vote", "bar", "red.")):
            self.dst, self.srcs = None, regs           # stores / branches / barriers: everything is a read
        elif self.op.startswith("ld.") and self.rest.lstrip().startswith("{"):
            vec = self.rest[:self.rest.index("}")]      # vector load: every register in the braces is written
            self.dsts = _REG.findall(vec)
            self.dst, self.srcs = (self.dsts[0] if self.dsts else None), regs[len(self.dsts):]
        elif regs:
            self.dst, self.srcs = regs[0], regs[1:]
        if self.dst and not self.dsts:
            self.dsts = [self.dst]


def _parse(lines):
    return [Ins(i, l) for i, l in enumerate(lines)]


def _pure(ins: Ins) -> bool:
    return ins.is_ins and ins.op.startswith(_PURE) and not ins.pred and not ins.op.startswith(("mov.pred",)) \
        and "%" in (ins.rest or "")


def _prefix(reg: str) -> str:
    m = re.match(r"(%[A-Za-z_]+)\d+", reg)
    return m.group(1) if m else reg


def _type_of(reg: str, classes: dict) -> str | None:
    return classes.get(_prefix(reg))


class Fresh:
    def __init__(self, classes):
        self.classes, self.n, self.decls = classes, 0, []

    def reg(self, like: str) -> str:
        t = _type_of(like, self.classes)
        if t is None:
            raise ValueError(f"unknown register class for {like}")
        self.n += 1
        name = f"{like}_tb{self.n}"
        self.decls.append(f"\t.reg .{t} \t{name};")
        return name


def _find_loops(ins, lo, hi):
    """(head label index, back-edge index) for every label whose single incoming branch is a later back-edge."""
    labels = {x.label: x.idx for x in ins[lo:hi] if x.label}
    incoming = {}
    for x in ins[lo:hi]:
        if x.target:
            incoming.setdefault(x.target, []).append(x.idx)
    out = []
    for name, at in labels.items():
        br = incoming.get(name, [])
        if len(br) == 1 and br[0] > at:
            out.append((at, br[0]))
    return sorted(out)


def _body_ok(ins, a, b, labels_in, all_labels):
    """None if the loop body is transformable. A branch to a label after the back-edge is a `break`: allowed (the
    batched loads of the copies after it are speculative reads of the loop's own index range, which has no effect
    for a buffer the loop does not write); a branch to a label before the loop is not."""
    for x in ins[a + 1:b]:
        if not x.is_ins:
            continue
        if x.op.startswith(_BARRIER_OPS) and not (x.op.startswith(("atom", "red.")) and ".shared" in x.op):
            return f"body has {x.op}"   # shared-memory atomics are not a hazard for global loads
        if x.target and x.target not in labels_in:
            if all_labels.get(x.target, -1) <= b:
                return f"branch out of the loop to {x.target}"
    return None


def _slice(ins, start, end, reg, defs_in_body, out, load_ok=None):
    """Backward slice of `reg` inside [start, end) through pure instructions and, when `load_ok(ins)` accepts
    them, loads (a gather's address comes from an index load: both are batched, the index load first). Indices
    appended to `out` in program order; returns the set of input registers (not defined in the slice), or None
    if a definition that is neither pure nor an acceptable load is hit."""
    need, inputs, chosen = [reg], set(), set()
    while need:
        r = need.pop()
        d = None
        for x in reversed(ins[start:end]):
            if x.is_ins and r in x.dsts:
                d = x
                break
        if d is None:
            inputs.add(r)
            continue
        if not _pure(d) and not (load_ok is not None and load_ok(d)):
            return None, None
        if d.idx not in chosen:
            chosen.add(d.idx)
            need += [s for s in d.srcs if s not in chosen]
    out += sorted(chosen)
    return inputs, chosen


def _rename_text(text, mapping):
    def sub(m):
        return mapping.get(m.group(0), m.group(0))
    return _REG.sub(sub, text)


def _emit_copy(y, mp, fresh):
    """`y` re-emitted with every destination renamed to a fresh register and every source renamed through `mp`
    (the sources are renamed with the values *before* this instruction: `add r, r, 1` reads the old r). Updates
    `mp` with the new destinations; returns the text."""
    text, pos, newmap = y.text, 0, {}
    for d in y.dsts:
        m = re.compile(re.escape(d) + r"(?![\w$])").search(text, pos)
        if m is None:
            raise ValueError(f"destination {d} not found in {y.text.strip()}")
        new = fresh.reg(d)
        text = text[:m.start()] + new + text[m.end():]
        pos = m.start() + len(new)
        newmap[d] = new
    text = text[:pos] + _rename_text(text[pos:], {s: mp[s] for s in y.srcs if s in mp})
    mp.update(newmap)
    return text


def transform_function(lines, start, end, k_max, report: Report, max_loads=16):
    """Rewrite the loops of one function body in place (lines list mutated); returns number of loops transformed."""
    classes = {}
    reg_end = None
    for i in range(start, end + 1):
        m = _REG_DECL.match(lines[i])
        if m:
            classes[m.group(2)] = m.group(1)
            reg_end = i
    if reg_end is None:
        return 0
    params = set(_ANY_PARAM.findall("\n".join(lines[start:end + 1])))
    ins = _parse(lines)
    bases = _provenance(lines, start, end, params)
    # pointer sources written anywhere in the kernel (store / atomic / reduction address, or an address of unknown
    # provenance: then every source may be written)
    written, unknown_write = set(), False
    for x in ins[start:end + 1]:
        if x.is_ins and x.op.startswith(("st.", "atom", "red.")) and ".shared" not in x.op and ".local" not in x.op \
                and ".param" not in x.op:
            m = re.search(r"\[\s*(%\w+)", x.rest)
            pb = bases.get(m.group(1), frozenset()) if m else frozenset()
            if not pb:
                unknown_write = True
            written |= pb
    def never_written(src):
        return not unknown_write and src not in written
    done = 0
    fresh = Fresh(classes)   # one counter per function: fresh names must not collide across its loops
    all_labels = {x.label: x.idx for x in ins[start:end + 1] if x.label}
    for a, b in reversed(_find_loops(ins, start, end + 1)):   # from the bottom so earlier indices stay valid
        L = ins[a].label
        labels_in = {x.label for x in ins[a + 1:b] if x.label}
        why = _body_ok(ins, a, b, labels_in, all_labels)
        if why:
            report.line(f"{L}: skipped ({why})")
            continue
        body = ins[a + 1:b + 1]
        has_barrier = any(x.is_ins and x.op.startswith(_BLOCK_BARRIER) for x in body)
        # prefix / suffix
        first_cf = next((x.idx for x in body if x.label or x.target), b)
        # suffix: the straight-line tail after the last label / branch before the back-edge; every path that reaches
        # the back-edge runs it exactly once
        last_cf = max([x.idx for x in ins[a + 1:b] if x.label or x.target], default=a)
        suffix_start = last_cf + 1
        defs_in_body = {}
        for x in body:
            if x.is_ins and x.dst:
                defs_in_body.setdefault(x.dst, []).append(x.idx)
        stores = [x for x in body if x.is_ins and x.op.startswith("st.global")]
        store_bases = []
        for s in stores:
            m = re.search(r"\[\s*(%\w+)", s.rest)
            pb = bases.get(m.group(1), frozenset()) if m else frozenset()
            store_bases.append(pb if len(pb) == 1 else None)
        # candidate loads in the prefix
        def addr_reg(x):
            m = re.search(r"\[\s*(%\w+)", x.rest)
            return m.group(1) if m else None

        def load_ok(x):
            """An unpredicated, non-volatile global load of a single-source address no store of the loop may alias."""
            if not (x.is_ins and x.op.startswith("ld.global") and ".volatile" not in x.op and not x.pred and a < x.idx < first_cf):
                return False
            r = addr_reg(x)
            lb = bases.get(r, frozenset()) if r else frozenset()
            if len(lb) != 1 or any(sb is None or sb == lb for sb in store_bases):
                return False
            return not has_barrier or never_written(next(iter(lb)))

        loads = []
        for x in ins[a + 1:first_cf]:
            if not (x.is_ins and x.op.startswith("ld.global") and ".volatile" not in x.op and not x.pred):
                continue
            r = addr_reg(x)
            if not r:
                continue
            lb = bases.get(r, frozenset())
            if len(lb) != 1:
                report.line(f"{L}: load {x.dst} skipped (address provenance {sorted(lb)})")
                continue
            if any(sb is None or sb == lb for sb in store_bases):
                report.line(f"{L}: load {x.dst} skipped (a store in the loop may alias it)")
                continue
            if has_barrier and not never_written(next(iter(lb))):
                report.line(f"{L}: load {x.dst} skipped (loop has a barrier and the kernel writes {next(iter(lb))[-24:]})")
                continue
            idxs = []
            inputs, chosen = _slice(ins, a + 1, x.idx, r, defs_in_body, idxs, load_ok)
            if inputs is None:
                report.line(f"{L}: load {x.dst} skipped (address slice not pure)")
                continue
            loads.append((x, idxs, inputs))
        if not loads:
            report.line(f"{L}: no batchable loads")
            continue
        # induction registers: slice inputs that the body defines, plus whatever the back-edge test reads (a loop
        # may count down on a register no address uses)
        induction = set()
        invariant = set()
        for _, _, inputs in loads:
            for r in inputs:
                (induction if r in defs_in_body else invariant).add(r)
        be = ins[b]
        setp = next((x for x in reversed(ins[suffix_start:b]) if x.is_ins and x.op.startswith("setp") and x.dst == be.pred), None)
        if setp is None:
            report.line(f"{L}: skipped (back-edge predicate is not set in the suffix)")
            continue
        for r in setp.srcs:
            if r in defs_in_body:
                induction.add(r)
        # update chain: definitions of induction regs must be single, pure, in the suffix; closure over their inputs
        chain, need, bad = [], list(induction), None
        seen = set()
        while need:
            r = need.pop()
            if r in seen:
                continue
            seen.add(r)
            d = defs_in_body.get(r)
            if d is None:
                continue  # invariant
            if len(d) != 1 or d[0] < suffix_start or not _pure(ins[d[0]]):
                bad = r
                break
            chain.append(d[0])
            need += ins[d[0]].srcs
        if bad:
            report.line(f"{L}: skipped (induction register {bad} not updated once, purely, in the suffix)")
            continue
        chain.sort()
        induction = {ins[i].dst for i in chain}
        if any(s in defs_in_body and s not in induction for s in setp.srcs):
            report.line(f"{L}: skipped (back-edge predicate reads a body register that is not an induction register)")
            continue
        # unroll factor from a load budget: k copies hold k x loads outstanding registers; past ~16 the register cost
        # (occupancy) outweighs the hidden latency (llama rms_norm: 32 batched loads lost, 8 won)
        k_req = k_max
        k = max(1, min(k_req, max_loads // max(1, len(loads))))
        out = []
        main = f"{L}_tbmain"
        exit_ = f"{L}_tbexit"
        out.append(f"{main}:")
        # induction values of copies 1..k-1
        cur = [{r: r for r in induction}]
        for j in range(1, k):
            mp = dict(cur[-1])
            for i in chain:
                out.append(_emit_copy(ins[i], mp, fresh))
            cur.append(mp)
        # copies 1..k-1 run only if the original would have continued into each of them: the back-edge test after
        # copy j-1 reads the induction values of copy j (a `!=` countdown is not monotone, so every test is emitted)
        for j in range(1, k):
            mp = dict(cur[j])
            out.append(_emit_copy(setp, mp, fresh))
            p = mp[setp.dst]
            out.append(f"\t@{'' if be.pred_neg else '!'}{p} bra \t{L};")
        # batched loads: per copy, every load's slice (dependency loads first) then the load, each definition
        # renamed to a fresh register (dst_map keeps the renames of the loads' destinations for the body copies)
        def emit_renamed(y, mp):
            out.append(_emit_copy(y, mp, fresh))

        dst_map = []  # per copy: {original register written by a batched load: fresh reg}
        for j in range(k):
            mp, dm = dict(cur[j]), {}
            emitted = set()
            for x, idxs, _ in loads:
                for i in idxs + [x.idx]:
                    if i in emitted:
                        continue
                    emitted.add(i)
                    emit_renamed(ins[i], mp)
                for d in x.dsts:
                    dm[d] = mp[d]
            dst_map.append(dm)
        # body copies
        load_idx = {x.idx: x for x, _, _ in loads}
        dep_idx = {i for _, idxs, _ in loads for i in idxs if ins[i].op.startswith("ld.")}
        for i in dep_idx:   # dependency loads: their destinations are in dst_map too (emitted in the slices)
            for j in range(k):
                for d in ins[i].dsts:
                    dst_map[j].setdefault(d, None)
        for j in range(k):
            lab = {l: f"{l}_tbu{j}" for l in labels_in}
            for x in body:
                if x.idx == b:  # back-edge
                    if j == k - 1:
                        out.append(f"\t@{'!' if be.pred_neg else ''}{be.pred} bra \t{main};")
                        out.append(f"\tbra.uni \t{exit_};")
                    continue
                if x.label:
                    out.append(f"{lab[x.label]}:")
                    continue
                if x.idx in load_idx or x.idx in dep_idx:
                    # a batched load (or a dependency load inside a batched slice): take the prefetched value
                    for d in x.dsts:
                        out.append(f"\tmov.{classes[_prefix(d)]} \t{d}, {dst_map[j][d]};")
                    continue
                text = x.text
                if x.target and x.target in lab:
                    text = text.replace(x.target, lab[x.target])
                out.append(text)
        # splice: main loop before L, exit label after the back-edge
        lines[b + 1:b + 1] = [f"{exit_}:"]
        lines[a:a] = out
        done += 1
        report.line(f"{L}: unrolled x{k} (requested {k_req}, budget {max_loads} loads), {len(loads)} load(s) batched per "
                    f"copy ({len(loads) * k} total), induction {sorted(induction)}, {len(stores)} store(s) crossed")
    # register declarations, once per function (the loops lie below reg_end, so the splice is safe)
    lines[reg_end + 1:reg_end + 1] = fresh.decls
    report.transformed = done
    return done


def unroll_batch(ptx: str, k: int = 8, kernels=None, max_loads=16):
    """Transform every .entry (or those whose name contains one of `kernels`); returns (ptx, [Report])."""
    lines = ptx.split("\n")
    reports = []
    # functions from the bottom so indices above stay valid
    funcs = list(_split_functions(lines))
    for start, end in reversed(funcs):
        name = lines[start].strip()
        if kernels and not any(k_ in name for k_ in kernels):
            continue
        rep = Report(name)
        try:
            transform_function(lines, start, end, k, rep, max_loads=max_loads)
        except Exception as e:  # never break compilation
            rep.line(f"error: {e!r}")
        reports.append(rep)
    return "\n".join(lines), reports


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="PTX unroll-and-batch load reorder")
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("-k", type=int, default=8, help="max copies per loop (the load budget may lower it)")
    ap.add_argument("--loads", type=int, default=16, help="batched-load budget per loop")
    ap.add_argument("--kernel", action="append", default=[])
    a = ap.parse_args(argv)
    ptx = open(a.inp, encoding="utf-8").read()
    new, reps = unroll_batch(ptx, a.k, a.kernel or None, max_loads=a.loads)
    open(a.out, "w", encoding="utf-8", newline="\n").write(new)
    for r in reps:
        print(f"== {r.kernel[:80]}: {r.transformed} loop(s) transformed")
        for l in r.loops:
            print("   ", l)


if __name__ == "__main__":
    main()

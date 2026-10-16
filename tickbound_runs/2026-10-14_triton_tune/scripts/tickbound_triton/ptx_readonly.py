"""Read-only load marking for Triton PTX (pass v1).

Triton emits every global load as plain ``ld.global``. ptxas must then assume that any earlier ``st.global`` may
write the loaded address, so it keeps each load behind the stores and barriers before it. When a kernel argument is
only ever read by the kernel, its loads can carry ``.nc`` (PTX: "non-coherent, read-only for the lifetime of the
kernel"), and ptxas is free to issue them early. On Kernl's rmsnorm (Triton 2.2, sm_80) that one change makes ptxas
batch the four pass-2 load waves into one, the schedule our hand-written ``ro``/``ro2`` reorders produced.

The pass is purely syntactic and conservative:

* every 64-bit register is traced back to the kernel pointer parameters it is derived from (``ld.param`` ->
  ``cvta``/``add``/``mad.wide``/``mov``/``selp``..., iterated to a fixed point so loop-carried pointers are covered);
* a parameter is *written* if any ``st``/``atom``/``red``/``cp.reduce``/``st.async``/``cp.async.bulk`` (global or
  generic) uses an address derived from it; an address derived from no parameter (a loaded pointer, an unknown
  generic address) makes the whole kernel ineligible;
* a load is rewritten only if its address derives from exactly one parameter and that parameter is never written,
  and the load is a plain weak load (no ``.volatile``/``.relaxed``/``.acquire``/``.cv``/``.lu``/``.mmio``).

Soundness also needs the read-only buffer not to overlap a buffer the kernel writes. Inside the kernel that is
guaranteed by the parameter analysis above only if distinct parameters point at disjoint memory; the launch guard in
``tickbound.triton`` checks that for the actual tensors and falls back to the unmodified kernel when they overlap.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_PARAM_DECL = re.compile(r"\.param\s+\.(?:u64|b64|s64)\b[^,)\n]*?\b(\w+)\s*(?:,|\)|$)", re.M)
_LD_PARAM = re.compile(r"ld\.param\.(?:u64|b64|s64)\s+(%\w+)\s*,\s*\[\s*(\w+)\s*(?:\+\s*\d+\s*)?\]")
_REG = re.compile(r"%[A-Za-z_][\w$]*")
_INSTR = re.compile(r"^\s*(?:@!?%\w+\s+)?([a-z][\w.:]*)\s*(.*?);\s*(?://.*)?$")
_ADDR = re.compile(r"\[\s*(%\w+)")
_FUNC_START = re.compile(r"^\s*\.(?:visible\s+|weak\s+)?\.?(entry|func)\b")

# opcodes whose 64-bit result carries the pointer bases of its 64-bit sources
_PROPAGATE = ("mov", "add", "sub", "mad", "cvta", "selp", "cvt", "and", "or", "xor", "shl", "shr", "mul", "min", "max")
_WRITE_PREFIXES = ("st.", "atom.", "red.", "cp.reduce", "st.async", "cp.async.bulk", "multimem.")
_BAD_LOAD_QUALS = (".volatile", ".relaxed", ".acquire", ".cv", ".lu", ".mmio", ".shared", ".local", ".const", ".param")


@dataclass
class KernelReport:
    name: str
    eligible: bool = True
    reason: str = ""
    params: list = field(default_factory=list)
    written: set = field(default_factory=set)
    readonly: set = field(default_factory=set)
    loads_total: int = 0
    loads_marked: int = 0
    loads_already_nc: int = 0
    lines_changed: list = field(default_factory=list)


def _split_functions(lines):
    """Yield (start, end) line ranges of each .entry/.func body (brace matched)."""
    i, n = 0, len(lines)
    while i < n:
        if _FUNC_START.match(lines[i]):
            depth, j, seen = 0, i, False
            while j < n:
                depth += lines[j].count("{") - lines[j].count("}")
                if "{" in lines[j]:
                    seen = True
                if seen and depth == 0:
                    break
                j += 1
            yield i, j
            i = j + 1
        else:
            i += 1


def _is_global_or_generic_mem(op: str) -> bool:
    return ".shared" not in op and ".local" not in op and ".param" not in op and ".const" not in op


def _bases_for_range(lines, start, end, params):
    """Fixed-point map register -> frozenset(param names) for one function body."""
    bases: dict[str, frozenset] = {}
    instrs = []
    for k in range(start, end + 1):
        line = lines[k]
        m = _LD_PARAM.search(line)
        if m and m.group(2) in params:
            instrs.append(("param", m.group(1), m.group(2), k))
            continue
        mi = _INSTR.match(line)
        if not mi:
            continue
        op, rest = mi.group(1), mi.group(2)
        instrs.append(("op", op, rest, k))
    changed = True
    while changed:
        changed = False
        for ins in instrs:
            if ins[0] == "param":
                _, dst, p, _ = ins
                if p not in bases.get(dst, ()):
                    bases[dst] = bases.get(dst, frozenset()) | {p}
                    changed = True
                continue
            _, op, rest, _ = ins
            if not op.startswith(_PROPAGATE):
                continue
            regs = _REG.findall(rest)
            if not regs:
                continue
            dst, srcs = regs[0], regs[1:]
            if op.startswith("selp"):
                srcs = srcs[:-1]  # selp: the last operand is the predicate
            acc = frozenset()
            for s in srcs:
                acc |= bases.get(s, frozenset())
            if acc and not acc <= bases.get(dst, frozenset()):
                bases[dst] = bases.get(dst, frozenset()) | acc
                changed = True
    return bases, instrs


def _mark_nc(op: str) -> str:
    """ld.global{.cop}{...}.type -> ld.global{.cop}.nc{...}.type"""
    m = re.match(r"(ld\.global(?:\.(?:ca|cg|cs))?)(.*)$", op)
    return m.group(1) + ".nc" + m.group(2)


def mark_readonly_loads(ptx: str):
    """Return (new_ptx, [KernelReport]). new_ptx == ptx when nothing was eligible."""
    lines = ptx.split("\n")
    reports = []
    for start, end in _split_functions(lines):
        head = lines[start]
        is_entry = ".entry" in head
        name_m = re.search(r"\.(?:entry|func)\s+(?:\([^)]*\)\s*)?(\w+)", " ".join(lines[start:start + 2]))
        rep = KernelReport(name=name_m.group(1) if name_m else "?")
        if not is_entry:
            continue
        # parameter declarations sit between the name and the opening brace
        params = []
        for k in range(start, end + 1):
            params += _PARAM_DECL.findall(lines[k])
            if "{" in lines[k]:
                break
        rep.params = params
        bases, instrs = _bases_for_range(lines, start, end, set(params))
        # calls into .func bodies that touch memory through pointers would escape this analysis
        loads = []
        for ins in instrs:
            if ins[0] != "op":
                continue
            _, op, rest, k = ins
            if op.startswith("call"):
                regs = _REG.findall(rest)
                if any(bases.get(r) for r in regs):
                    rep.eligible, rep.reason = False, f"pointer passed to a call (line {k + 1})"
            if op.startswith(_WRITE_PREFIXES) and _is_global_or_generic_mem(op):
                am = _ADDR.search(rest)
                b = bases.get(am.group(1), frozenset()) if am else frozenset()
                if not b:
                    rep.eligible, rep.reason = False, f"write through an address of unknown origin (line {k + 1}: {op})"
                rep.written |= set(b)
            elif op.startswith("ld.global") or (op.startswith("ld.") and _is_global_or_generic_mem(op)
                                                and not op.startswith("ld.param")):
                loads.append((op, rest, k))
        rep.readonly = set(params) - rep.written
        rep.loads_total = len(loads)
        if not rep.eligible:
            reports.append(rep)
            continue
        for op, rest, k in loads:
            if ".nc" in op:
                rep.loads_already_nc += 1
                continue
            if not op.startswith("ld.global") or any(q in op for q in _BAD_LOAD_QUALS):
                continue
            am = _ADDR.search(rest)
            b = bases.get(am.group(1), frozenset()) if am else frozenset()
            if len(b) != 1 or not b <= rep.readonly:
                continue
            new_op = _mark_nc(op)
            line = lines[k]
            idx = line.find(op)
            lines[k] = line[:idx] + new_op + line[idx + len(op):]
            rep.loads_marked += 1
            rep.lines_changed.append(k + 1)
        reports.append(rep)
    return "\n".join(lines), reports

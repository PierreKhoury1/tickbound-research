"""Loop prefetch for Triton kernels (pass v2): issue the next iteration's loads at the top of the current one.

Triton software-pipelines only loads that feed ``tl.dot``; a plain ``for`` loop (reductions, chunked softmax,
cross-entropy over the vocabulary, norm backward passes) waits one full memory round trip per iteration, even with
``tl.range(..., num_stages=N)`` (checked on Triton 3.2 and 3.8, sm_80 and sm_90: no ``cp.async``, plain
``ld.global``). This pass rewrites the kernel's AST before Triton lowers it:

    for i in range(a, b, s):                    _tb_n = a
        c = i + tl.arange(0, B)                 _tb_pf0 = tl.load(P(c(_tb_n)), mask=M(_tb_n) & (_tb_n < b), other=O)
        x = tl.load(P(c), mask=M(c), other=O)   for i in range(a, b, s):
        ...                                         _tb_cur0 = _tb_pf0
                                                    _tb_n = i + s
                                                    _tb_pf0 = tl.load(P(c(_tb_n)), mask=M(_tb_n) & (_tb_n < b), ...)
                                                    c = i + tl.arange(0, B)
                                                    x = _tb_cur0
                                                    ...

A load is moved only if (1) its pointer, mask and ``other`` depend only on the loop variable, loop invariants and
"pure" index definitions earlier in the body (re-evaluated for the next index); (2) its pointer derives from exactly
one pointer parameter that the kernel never stores to, atomically updates, or hands to another function; (3) the
loop step is a positive literal or a positive constexpr; (4) it uses no ``volatile``/``boundary_check``/block
pointers. The prefetch is masked with ``next < end``, so it never touches memory the original loop would not have
loaded. Values are identical: the loaded memory is read-only for the kernel, and the launch guard in
``tickbound.triton`` falls back to the unmodified kernel when tensor arguments share memory.
"""
from __future__ import annotations

import ast
import copy

_PURE_CALLS = {"arange", "full", "zeros", "multiple_of", "max_contiguous", "minimum", "maximum", "where", "cdiv",
               "broadcast_to", "reshape", "expand_dims", "to"}
_WRITE_CALLS = {"store", "atomic_add", "atomic_max", "atomic_min", "atomic_and", "atomic_or", "atomic_xor",
                "atomic_xchg", "atomic_cas"}
_LOAD_KW_OK = {"mask", "other", "cache_modifier", "eviction_policy"}


def _is_tl_call(node, names):
    """tl.<name>(...) or triton.language.<name>(...)."""
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in names
            and isinstance(node.func.value, (ast.Name, ast.Attribute)))


def _names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _assigned(stmts):
    out = set()
    for s in stmts:
        for n in ast.walk(s):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                out.add(n.id)
    return out


def _pure_expr(node, ok_names):
    for n in ast.walk(node):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id not in ok_names and n.id != "tl":
            return False
        if isinstance(n, ast.Call):
            f = n.func
            attr = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)
            if attr not in _PURE_CALLS and attr not in ("min", "max"):
                return False
        if isinstance(n, (ast.Await, ast.Yield, ast.Lambda, ast.NamedExpr)):
            return False
    return True


class _Rename(ast.NodeTransformer):
    def __init__(self, mapping):
        self.m = mapping

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id in self.m:
            return ast.copy_location(copy.deepcopy(self.m[node.id]), node)
        return node


class _Replace(ast.NodeTransformer):
    def __init__(self, targets):
        self.t = targets  # id(call node) -> name

    def visit_Call(self, node):
        if id(node) in self.t:
            return ast.copy_location(ast.Name(id=self.t[id(node)], ctx=ast.Load()), node)
        return self.generic_visit(node)


def _ptr_params(expr, pointer_params):
    return _names(expr) & pointer_params


def _written_pointers(fn_def, pointer_params, jit_names):
    """Pointer params stored to / atomically updated / passed to a non-tl call (conservative)."""
    w = set()
    for n in ast.walk(fn_def):
        if not isinstance(n, ast.Call):
            continue
        if _is_tl_call(n, _WRITE_CALLS) and n.args:
            w |= _ptr_params(n.args[0], pointer_params)
        elif not isinstance(n.func, ast.Attribute) or not isinstance(n.func.value, ast.Name) or n.func.value.id != "tl":
            # a call into another function (helper @jit, unknown): pointers handed over may be written there
            for a in list(n.args) + [k.value for k in n.keywords]:
                w |= _ptr_params(a, pointer_params)
    return w


def _step_positive(step, constexprs):
    if isinstance(step, ast.Constant) and isinstance(step.value, int):
        return step.value > 0
    if isinstance(step, ast.Name) and step.id in constexprs:
        v = constexprs[step.id]
        return isinstance(v, int) and not isinstance(v, bool) and v > 0
    return False


class _Counter:
    def __init__(self):
        self.k = 0

    def next(self):
        self.k += 1
        return self.k


def _transform_loop(loop, params, readonly, constexprs, ctr, report):
    it = loop.iter
    if not (isinstance(it, ast.Call) and isinstance(loop.target, ast.Name)):
        return None
    fname = it.func.attr if isinstance(it.func, ast.Attribute) else (it.func.id if isinstance(it.func, ast.Name) else "")
    if fname not in ("range",) or loop.orelse:
        return None  # static_range is unrolled at compile time; ptxas schedules it
    a = it.args
    if len(a) == 1:
        start, end, step = ast.Constant(0), a[0], ast.Constant(1)
    elif len(a) == 2:
        start, end, step = a[0], a[1], ast.Constant(1)
    elif len(a) == 3:
        start, end, step = a
    else:
        return None
    var = loop.target.id
    body = loop.body
    assigned = _assigned(body) | {var}
    if (_names(start) | _names(end)) & assigned or not _step_positive(step, constexprs):
        report.append(f"loop over {var}: start/end not invariant or step not provably positive")
        return None
    invariants_ok = lambda names: not (names & (assigned - {var}))
    pure_defs = {}   # name -> value expr (valid for the current var)
    pure_names = set()
    loads = []       # (call node, pure names it needs)
    redefined = set()
    for st in body:
        # loads at the top level of this statement (not inside nested loops/ifs)
        if isinstance(st, (ast.Assign, ast.AugAssign, ast.Expr, ast.AnnAssign)):
            for n in ast.walk(st):
                if _is_tl_call(n, {"load"}) and n.args:
                    kws = {k.arg for k in n.keywords}
                    if not kws <= _LOAD_KW_OK or len(n.args) > 1:
                        continue
                    if any(isinstance(k.value, ast.Constant) and k.value.value is True for k in n.keywords
                           if k.arg == "volatile"):
                        continue
                    exprs = [n.args[0]] + [k.value for k in n.keywords if k.arg in ("mask", "other")]
                    deps = set().union(*(_names(e) for e in exprs)) - {"tl"}
                    if not all(_pure_expr(e, (deps - assigned) | pure_names | {var}) for e in exprs):
                        continue
                    if deps & redefined:
                        continue
                    pp = _ptr_params(n.args[0], params)
                    if len(pp) != 1 or not pp <= readonly:
                        continue
                    loads.append((n, deps & pure_names))
        # track pure index definitions (single-name assignment of a pure expression)
        if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
            nm = st.targets[0].id
            deps = _names(st.value) - {"tl"}
            if nm in pure_names or nm in redefined:
                redefined.add(nm)
                pure_names.discard(nm)
                pure_defs.pop(nm, None)
            elif _pure_expr(st.value, (deps - assigned) | pure_names | {var}) and invariants_ok(deps - pure_names - {var}):
                pure_names.add(nm)
                pure_defs[nm] = st.value
            else:
                redefined.add(nm)
        else:
            for nm in _assigned([st]):
                redefined.add(nm)
                pure_names.discard(nm)
                pure_defs.pop(nm, None)
    # a load whose index definitions are reassigned later in the body cannot be re-evaluated at the loop top
    loads = [(n, need) for (n, need) in loads if not (need & redefined)]
    if not loads:
        return None

    def instantiate(expr, idx_expr, need):
        """expr with var -> idx_expr and pure names -> their definitions (recursively)."""
        mapping = {var: idx_expr}
        # resolve pure defs in definition order
        for nm, val in pure_defs.items():
            if nm in need or any(nm in _names(v) for v in pure_defs.values()):
                mapping[nm] = _Rename(dict(mapping)).visit(copy.deepcopy(val))
        return _Rename(mapping).visit(copy.deepcopy(expr))

    k0 = ctr.next()
    first_n, next_n = f"_tb_first{k0}", f"_tb_next{k0}"

    def make_load(call, need, idx_name):
        """tl.load of the iteration whose index is idx_name, masked to idx < end (never reads past the loop)."""
        idx = ast.Name(idx_name, ast.Load())
        ptr = instantiate(call.args[0], idx, need)
        kw = {k.arg: k.value for k in call.keywords}
        in_range = ast.Compare(left=ast.Name(idx_name, ast.Load()), ops=[ast.Lt()], comparators=[copy.deepcopy(end)])
        mask = ast.BinOp(instantiate(kw["mask"], idx, need), ast.BitAnd(), in_range) if "mask" in kw else in_range
        other = instantiate(kw["other"], idx, need) if "other" in kw else ast.Constant(0)
        kws = [ast.keyword("mask", mask), ast.keyword("other", other)]
        kws += [ast.keyword(k, copy.deepcopy(v)) for k, v in kw.items() if k not in ("mask", "other")]
        return ast.Call(func=copy.deepcopy(call.func), args=[ptr], keywords=kws)

    pre = [ast.Assign(targets=[ast.Name(first_n, ast.Store())], value=copy.deepcopy(start))]
    takes, issue, targets = [], [], {}
    for j, (call, need) in enumerate(loads):
        pf, cur = f"_tb_pf{k0}_{j}", f"_tb_cur{k0}_{j}"
        pre.append(ast.Assign(targets=[ast.Name(pf, ast.Store())], value=make_load(call, need, first_n)))
        takes.append(ast.Assign(targets=[ast.Name(cur, ast.Store())], value=ast.Name(pf, ast.Load())))
        issue.append(ast.Assign(targets=[ast.Name(pf, ast.Store())], value=make_load(call, need, next_n)))
        targets[id(call)] = cur
    nxt = ast.Assign(targets=[ast.Name(next_n, ast.Store())],
                     value=ast.BinOp(ast.Name(var, ast.Load()), ast.Add(), copy.deepcopy(step)))
    # loop top: take this iteration's values, compute the next index, issue the next iteration's loads
    loop.body = takes + [nxt] + issue + [_Replace(targets).visit(st) for st in body]
    report.append(f"loop over {var}: prefetching {len(loads)} load(s)")
    return pre


def _process_block(stmts, params, readonly, constexprs, ctr, report):
    out = []
    for st in stmts:
        # inner loops first
        for field in ("body", "orelse"):
            if hasattr(st, field) and isinstance(getattr(st, field), list) and not isinstance(st, ast.FunctionDef):
                setattr(st, field, _process_block(getattr(st, field), params, readonly, constexprs, ctr, report))
        if isinstance(st, ast.For):
            pre = _transform_loop(st, params, readonly, constexprs, ctr, report)
            if pre:
                out.extend(pre)
        out.append(st)
    return out


def prefetch_loops(tree: ast.Module, signature: dict, constexprs: dict):
    """Rewrite the kernel AST in place. signature: param name -> type string ("*fp16", "i32", "constexpr").
    Returns (tree, report lines)."""
    fn = tree.body[0]
    pointer_params = {k for k, v in signature.items() if isinstance(v, str) and v.startswith("*")}
    report = []
    if not pointer_params:
        return tree, ["no pointer parameters"]
    written = _written_pointers(fn, pointer_params, set())
    readonly = pointer_params - written
    report.append(f"read-only pointers: {sorted(readonly)}; written: {sorted(written)}")
    ctr = _Counter()
    fn.body = _process_block(fn.body, pointer_params, readonly, constexprs, ctr, report)
    ast.fix_missing_locations(tree)
    return tree, report

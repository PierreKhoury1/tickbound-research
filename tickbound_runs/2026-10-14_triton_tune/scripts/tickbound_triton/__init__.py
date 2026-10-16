"""tickbound.triton: compile-time load scheduling pass for Triton kernels (NVIDIA).

    import tickbound.triton
    tickbound.triton.enable()          # every Triton kernel compiled from now on goes through the pass

What it does (pass v1, ``ptx_readonly``): loads from kernel arguments that the kernel never writes are marked
``ld.global.nc``, which lets ptxas issue them ahead of earlier stores and barriers. Safety:

* compile time: a kernel whose stores use an address of unknown origin is left alone; ptxas failures on the
  rewritten PTX fall back to Triton's own PTX;
* launch time: if two tensor arguments share memory (in-place calls, views), the launch uses the unmodified kernel
  (a separately cached compile), because ``.nc`` is only valid when the read-only buffer is not written;
* occupancy (policy "occupancy", default): if the rewritten kernel fits fewer CTAs per SM than the original
  (more registers), the original is kept. Policy "always" keeps every rewrite.

Policy "tune" (see ``tune.py``) replaces the static rules with measurement: on the first launch of each kernel and
shape bucket it compiles candidates (original, read-only loads, + loop prefetch, then num_warps and num_stages
neighbours), keeps only those that leave memory byte-identical to the original, times them with CUDA events and
keeps a candidate only when it is faster with statistical confidence. It is never slower than the original by
construction (up to measurement error) and the decision is cached on disk.

Hooks: Triton >= 3.4 exposes ``knobs.runtime.add_stages_inspection_hook``; older versions get
``CUDABackend.add_stages`` / ``CUDABackend.hash`` patched. ``disable()`` restores everything.
Environment: TICKBOUND_TRITON=1 enables at import of this module; TICKBOUND_TRITON_POLICY=always|occupancy;
TICKBOUND_TRITON_LOG=path appends one JSON line per compiled kernel (what was changed and why).
"""
from __future__ import annotations

import copy
import json
import os
import struct
import threading
from collections import defaultdict

from .ptx_readonly import mark_readonly_loads
from .ast_prefetch import prefetch_loops
from . import tune as _tune

__all__ = ["enable", "disable", "enabled", "stats", "PASS_VERSION"]

PASS_VERSION = "tb-nc-1"
_state = threading.local()
_cfg = {"on": False, "policy": "occupancy", "log": None, "prefetch": False}
_saved = {}
_stats = defaultdict(int)
_orig_ptx_of = {}  # id-free map: rewritten PTX text -> Triton's PTX, for the ptxas fallback


def _off() -> bool:
    return getattr(_state, "off", False)


def _variant():
    """(read-only loads on, loop prefetch on) for the compile happening on this thread."""
    v = getattr(_state, "variant", None)
    if v is not None:
        return v
    if _off():
        return (False, False)
    return (True, _cfg["prefetch"])


def stats() -> dict:
    return dict(_stats)


def enabled() -> bool:
    return _cfg["on"]


# ------------------------------------------------------------------ cubin helpers
def _regs_from_cubin(cubin: bytes):
    """Register count of the kernel in a cubin: EIATTR_REGCOUNT (0x2f) in .nv.info, else .text.<name> sh_info >> 24."""
    try:
        if cubin[:4] != b"\x7fELF" or cubin[4] != 2:
            return None
        shoff, = struct.unpack_from("<Q", cubin, 0x28)
        shentsize, shnum, shstrndx = struct.unpack_from("<HHH", cubin, 0x3A)
        hdr = lambda i: struct.unpack_from("<IIQQQQIIQQ", cubin, shoff + i * shentsize)
        stroff = hdr(shstrndx)[4]
        regs_info = regs_text = None
        for i in range(shnum):
            name_off, _, _, _, off, size, _, info, _, _ = hdr(i)
            end_ = cubin.index(b"\0", stroff + name_off)
            name = cubin[stroff + name_off:end_]
            if name == b".nv.info":
                k = off
                while k + 4 <= off + size:
                    fmt, attr = cubin[k], cubin[k + 1]
                    if fmt == 0x04:  # EIFMT_SVAL: u16 size + payload
                        n, = struct.unpack_from("<H", cubin, k + 2)
                        if attr == 0x2F and n >= 8:
                            regs_info = struct.unpack_from("<I", cubin, k + 8)[0]
                        k += 4 + n
                    elif fmt == 0x03:  # EIFMT_HVAL: u16 value
                        k += 4
                    elif fmt == 0x02:  # EIFMT_BVAL
                        k += 4
                    else:  # EIFMT_NVAL
                        k += 4
            elif name.startswith(b".text.") and regs_text is None:
                regs_text = info >> 24
        return regs_info or regs_text or None
    except Exception:
        return None


def _ctas_per_sm(regs, num_warps, smem, capability):
    if not regs:
        return None
    max_warps = 48 if capability in (86, 89) else 64
    max_ctas = 16 if capability in (86, 89) else 32
    smem_per_sm = {80: 167936, 86: 101376, 89: 101376, 90: 232448}.get(capability, 101376)
    per_warp = -(-regs * 32 // 256) * 256
    warps_by_regs = (16384 // per_warp) * 4  # 64K registers per SM, allocated per scheduler (4 per SM)
    ctas = min(warps_by_regs // num_warps, max_warps // num_warps, max_ctas)
    if smem:
        ctas = min(ctas, smem_per_sm // (smem + 1024))
    return ctas


def _log(rec):
    path = _cfg["log"]
    if path:
        with open(path, "a") as f:
            f.write(json.dumps(rec) + "\n")


# ------------------------------------------------------------------ stage wrapping
def _wrap_stages(stages, options, capability):
    if not _variant()[0]:
        return
    make_ptx, make_cubin = stages.get("ptx"), stages.get("cubin")
    if make_ptx is None or make_cubin is None:
        return

    def ptx_stage(src, metadata):
        ptx = make_ptx(src, metadata)
        if not _variant()[0]:
            return ptx
        new, reports = mark_readonly_loads(ptx)
        rec = {"pass": PASS_VERSION, "kernel": metadata.get("name"), "capability": capability,
               "num_warps": getattr(options, "num_warps", None),
               "reports": [{"name": r.name, "eligible": r.eligible, "reason": r.reason, "readonly": sorted(r.readonly),
                            "written": sorted(r.written), "loads": r.loads_total, "marked": r.loads_marked}
                           for r in reports]}
        _state.last_rec = rec
        pending = getattr(_state, "pending", None)
        if new != ptx and pending is not None and _args_overlap(*pending):
            # first compile happens on a launch whose buffers overlap: keep Triton's PTX for this specialization
            _stats["skipped_alias_first_compile"] += 1
            rec.update(decision="skipped_alias_first_compile")
            _log(rec)
            return ptx
        if new != ptx:
            _state.applied = True
            _orig_ptx_of[new] = ptx
            _stats["kernels_rewritten"] += 1
        else:
            _stats["kernels_unchanged"] += 1
            _log(rec)
        return new

    def cubin_stage(src, metadata):
        orig = _orig_ptx_of.pop(src, None)
        if orig is None:
            return make_cubin(src, metadata)
        rec = getattr(_state, "last_rec", {}) or {}
        try:
            new_bin = make_cubin(src, metadata)
        except Exception as e:  # ptxas rejected the rewrite: Triton's own PTX
            _stats["ptxas_fallback"] += 1
            rec.update(decision="fallback_ptxas", error=str(e)[:300])
            _log(rec)
            return make_cubin(orig, metadata)
        if _cfg["policy"] == "occupancy":
            old_bin = make_cubin(orig, metadata)
            r_new, r_old = _regs_from_cubin(new_bin), _regs_from_cubin(old_bin)
            nw, sm = metadata.get("num_warps", getattr(options, "num_warps", 4)), metadata.get("shared", 0) or 0
            c_new, c_old = _ctas_per_sm(r_new, nw, sm, capability), _ctas_per_sm(r_old, nw, sm, capability)
            rec.update(regs_old=r_old, regs_new=r_new, ctas_old=c_old, ctas_new=c_new)
            if c_new is not None and c_old is not None and c_new < c_old:
                _stats["rejected_occupancy"] += 1
                rec.update(decision="rejected_occupancy")
                _log(rec)
                return old_bin
        _stats["applied"] += 1
        rec.update(decision="applied")
        _log(rec)
        return new_bin

    stages["ptx"] = ptx_stage
    stages["cubin"] = cubin_stage


def _cache_tag():
    nc, pf = _variant()
    return f"{PASS_VERSION}{'-pf1' if pf else ''}-{_cfg['policy']}-{'on' if nc else 'off'}"


class _InspectionHook:
    """Triton >= 3.4 protocol: hook() -> (key, hash); hook(backend, stages, options, language, capability)."""

    _tags = {}

    def __call__(self, *args):
        if not args:
            k = (_cfg["policy"], _variant())
            t = self._tags.get(k)
            if t is None:
                tag = _cache_tag()
                t = self._tags[k] = (tag, tag)
            return t
        backend, stages, options, language, capability = args
        _wrap_stages(stages, options, capability)


# ------------------------------------------------------------------ launch guard
_Tensor = None


def _args_overlap(args, kwargs):
    """True if two tensor arguments share a storage (views of one buffer, in-place calls).

    Storage base = data_ptr - storage_offset * element_size, three cheap C calls per tensor and no Python storage
    object. Distinct live storages from PyTorch's allocators never overlap, so "same base" is the overlap test
    (tensors built from raw pointers that alias with different bases are not detected; see module docstring)."""
    global _Tensor
    if _Tensor is None:
        import torch
        _Tensor = torch.Tensor
    T = _Tensor
    bases = []
    for a in (args if not kwargs else list(args) + list(kwargs.values())):
        if isinstance(a, T):
            bases.append(a.data_ptr() - a.storage_offset() * a.element_size())
        elif hasattr(a, "data_ptr"):
            b = _tune.backing(a)
            if b is None:  # pointer object we cannot see through: assume it may alias
                return True
            bases.append(b.data_ptr() - b.storage_offset() * b.element_size())
    return len(bases) > 1 and len(set(bases)) < len(bases)


def _plain_clone(fn):
    c = getattr(fn, "_tb_plain", None)
    if c is None:
        c = copy.copy(fn)
        if hasattr(c, "device_caches"):
            c.device_caches = defaultdict(c.create_binder)
        if hasattr(c, "cache"):
            c.cache = defaultdict(dict)
        if hasattr(c, "binder"):
            c.binder = None
        fn._tb_plain = c
    return c


def _variant_clone(fn, nc, pf):
    """A copy of ``fn`` with its own kernel caches, one per pass combination: older Tritons do not put the backend
    hash in the in-memory cache key, so each combination needs its own JITFunction."""
    clones = fn.__dict__.get("_tb_clones")
    if clones is None:
        clones = fn._tb_clones = {}
    c = clones.get((nc, pf))
    if c is None:
        c = copy.copy(fn)
        c.__dict__.pop("_tb_clones", None)
        if hasattr(c, "device_caches"):
            c.device_caches = defaultdict(c.create_binder)
        if hasattr(c, "cache"):
            c.cache = defaultdict(dict)
        if hasattr(c, "binder"):
            c.binder = None
        clones[(nc, pf)] = c
    return c


_SIMPLE = {int, float, bool, str, type(None)}


def _tune_run(self, orig_run, args, grid, kwargs):
    # fast path: exact launch signature (tensor dtype + shape, scalar values, kwargs) -> ready plan
    global _Tensor
    if _Tensor is None:
        import torch
        _Tensor = torch.Tensor
    T = _Tensor
    try:
        sig = tuple([(a.dtype, a.shape) if isinstance(a, T) else (a if type(a) in _SIMPLE else _tune.describe(a))
                     for a in args])
        if kwargs:
            sig = (sig, tuple((k, v if type(v) in _SIMPLE else _tune.describe(v)) for k, v in kwargs.items()))
        plans = self.__dict__.get("_tb_plans")
        plan = plans.get(sig) if plans is not None else None
    except TypeError:  # unhashable argument: no fast path
        sig, plan = None, None
    if plan is not None:
        clone, over, vstate = plan
        if not vstate[0] or not _args_overlap(args, kwargs):
            _state.variant = vstate
            try:
                # this call's own kwargs (they may hold tensors) + the plan's num_warps / num_stages overrides
                return orig_run(clone, *args, grid=grid, warmup=False, **({**kwargs, **over} if over else kwargs))
            finally:
                _state.variant = None
    return _tune_slow(self, orig_run, args, grid, kwargs, sig)


def _tune_slow(self, orig_run, args, grid, kwargs, sig):
    def launch(v):
        kw = dict(kwargs)
        if v.num_warps:
            kw["num_warps"] = v.num_warps
        if v.num_stages:
            kw["num_stages"] = v.num_stages
        prev = getattr(_state, "variant", None)
        _state.variant = (v.nc, v.pf)
        try:
            return orig_run(_variant_clone(self, v.nc, v.pf), *args, grid=grid, warmup=False, **kw)
        finally:
            _state.variant = prev

    if getattr(_state, "in_bench", False) or getattr(_state, "in_tune", False):
        # inside an autotuner's config benchmark, or a kernel launched by the tuner's own work: original kernel
        return launch(_tune.ORIG)
    bkey, ekey = _tune.keys(args, kwargs)
    v = _tune.lookup(self, bkey)
    overlap = None
    if v is None:
        import torch
        if torch.cuda.is_current_stream_capturing() or not _tune.budget_ok(self):
            return launch(_tune.ORIG)
        overlap = _args_overlap(args, kwargs)
        _stats["tuned"] += 1
        _state.in_tune = True
        try:
            v, snap = _tune.tune(self, launch, args, kwargs, bkey, _log, passes_ok=not overlap)
            if snap is not None:
                snap.restore()
        finally:
            _state.in_tune = False
        _stats[f"chosen_{v.name}"] += 1
    elif v.num_warps:
        import torch
        if not torch.cuda.is_current_stream_capturing():
            _state.in_tune = True
            try:
                v = _tune.verify_exact(self, launch, v, args, kwargs, ekey)
            finally:
                _state.in_tune = False
    if v.nc or v.pf:
        if overlap is None:
            overlap = _args_overlap(args, kwargs)
        if overlap:
            _stats["launches_alias_fallback"] += 1
            v = _tune.Variant(False, False, v.num_warps, v.num_stages)
            return launch(v)
    if sig is not None and (not v.num_warps or _tune.verified(self, ekey)):
        over = {}
        if v.num_warps:
            over["num_warps"] = v.num_warps
        if v.num_stages:
            over["num_stages"] = v.num_stages
        plans = self.__dict__.get("_tb_plans")
        if plans is None:
            plans = self._tb_plans = {}
        plans[sig] = (_variant_clone(self, v.nc, v.pf), over, (v.nc, v.pf))
    return launch(v)


def _patched_bench(orig_bench):
    """Autotuner config benchmarks run the original kernel: tuning every config would multiply the search; the
    config the autotuner picks is tuned on its first real launch."""
    def _bench(self, *args, **kwargs):
        prev = getattr(_state, "in_bench", False)
        _state.in_bench = True
        try:
            return orig_bench(self, *args, **kwargs)
        finally:
            _state.in_bench = prev
    return _bench


def _patched_run(orig_run, keyed_by_hook):
    def run(self, *args, grid, warmup, **kwargs):
        if not _cfg["on"]:
            return orig_run(self, *args, grid=grid, warmup=warmup, **kwargs)
        if _cfg["policy"] == "tune":
            if warmup:
                prev, _state.variant = getattr(_state, "variant", None), (False, False)
                try:
                    return orig_run(_variant_clone(self, False, False), *args, grid=grid, warmup=warmup, **kwargs)
                finally:
                    _state.variant = prev
            return _tune_run(self, orig_run, args, grid, kwargs)
        if not self.__dict__.get("_tb_rewritten"):
            # no rewritten specialization of this kernel yet: no per-launch check; a compile inside this launch
            # sees the arguments (pending) and refuses the rewrite if they overlap
            _state.pending, _state.applied = (args, kwargs), False
            try:
                return orig_run(self, *args, grid=grid, warmup=warmup, **kwargs)
            finally:
                _state.pending = None
                if _state.applied:
                    self._tb_rewritten = True
        if not _args_overlap(args, kwargs):
            return orig_run(self, *args, grid=grid, warmup=warmup, **kwargs)
        _stats["launches_alias_fallback"] += 1
        prev = _off()
        _state.off = True
        try:
            target = self if keyed_by_hook else _plain_clone(self)
            return orig_run(target, *args, grid=grid, warmup=warmup, **kwargs)
        finally:
            _state.off = prev
    return run


# ------------------------------------------------------------------ pass v2: loop prefetch at the AST level
def _ast_ctx_names(fn, src):
    sig = dict(getattr(src, "signature", {}) or {})
    consts = {}
    raw = getattr(src, "constants", None) or getattr(src, "constexprs", None) or {}
    names = list(getattr(fn, "arg_names", []))
    for key, v in raw.items():
        if isinstance(key, tuple):
            if len(key) == 1 and key[0] < len(names):
                consts[names[key[0]]] = v
        elif isinstance(key, int):
            if key < len(names):
                consts[names[key]] = v
        else:
            consts[key] = v
    # older Tritons key the signature by position
    sig = {(names[k] if isinstance(k, int) and k < len(names) else k): v for k, v in sig.items()}
    return sig, consts


def _wrap_ast_to_ttir(orig):
    def ast_to_ttir(fn, src, *a, **k):
        prev = getattr(_state, "ast_ctx", None)
        if _cfg["on"] and _variant()[1]:
            try:
                _state.ast_ctx = (fn,) + _ast_ctx_names(fn, src)
            except Exception:
                _state.ast_ctx = None
        try:
            return orig(fn, src, *a, **k)
        finally:
            _state.ast_ctx = prev
    ast_to_ttir._tb_orig = orig
    return ast_to_ttir


def _patched_parse(orig_parse):
    def parse(self):
        tree = orig_parse(self)
        ctx = getattr(_state, "ast_ctx", None)
        if ctx is None or ctx[0] is not self or not _variant()[1]:
            return tree
        try:
            tree, rep = prefetch_loops(tree, ctx[1], ctx[2])
            changed = any("prefetching" in r for r in rep)
            _stats["ast_kernels_prefetched" if changed else "ast_kernels_unchanged"] += 1
            _log({"pass": "prefetch", "kernel": getattr(self, "__name__", "?"), "report": rep, "changed": changed})
        except Exception as e:  # never break compilation: fall back to Triton's own AST
            _stats["ast_errors"] += 1
            _log({"pass": "prefetch", "kernel": getattr(self, "__name__", "?"), "error": repr(e)[:300]})
            tree = orig_parse(self)
        return tree
    return parse


# ------------------------------------------------------------------ enable / disable
def _backend_class(nvc):
    """The CUDABackend class Triton actually instantiates (older Tritons load backends as separate module objects)."""
    try:
        from triton.backends import backends
        return backends["nvidia"].compiler
    except Exception:
        return nvc.CUDABackend


def enable(policy: str | None = None, log: str | None = None, prefetch: bool | None = None):
    """policy: "occupancy" (default), "always", or "tune" (measured selection, see tune.py)."""
    import triton
    from triton.runtime.jit import JITFunction
    from triton.backends.nvidia import compiler as nvc

    if _cfg["on"]:
        return
    _cfg["policy"] = policy or os.environ.get("TICKBOUND_TRITON_POLICY", "occupancy")
    _cfg["log"] = log or os.environ.get("TICKBOUND_TRITON_LOG")
    _cfg["prefetch"] = bool(int(os.environ.get("TICKBOUND_TRITON_PREFETCH", "0"))) if prefetch is None else prefetch
    from triton.compiler import code_generator as _cg, compiler as _cc
    _saved["parse"] = JITFunction.parse
    JITFunction.parse = _patched_parse(JITFunction.parse)
    _saved["ast_to_ttir"] = _cg.ast_to_ttir
    _cg.ast_to_ttir = _wrap_ast_to_ttir(_cg.ast_to_ttir)
    if getattr(_cc, "ast_to_ttir", None) is _saved["ast_to_ttir"]:
        _cc.ast_to_ttir = _cg.ast_to_ttir
    knobs = getattr(triton, "knobs", None)
    use_hook = knobs is not None and hasattr(knobs.runtime, "add_stages_inspection_hook")
    if use_hook:
        _saved["hook"] = knobs.runtime.add_stages_inspection_hook
        knobs.runtime.add_stages_inspection_hook = _InspectionHook()
    else:
        B = _backend_class(nvc)
        _saved["add_stages"], _saved["hash"] = B.add_stages, B.__dict__.get("hash")
        orig_add, orig_hash = B.add_stages, B.hash

        def add_stages(self, stages, options, *rest):
            orig_add(self, stages, options, *rest)
            cap = self._parse_arch(options.arch) if hasattr(self, "_parse_arch") else getattr(self, "capability", 0)
            _wrap_stages(stages, options, cap)

        def hash_(self):
            base = orig_hash.__wrapped__(self) if hasattr(orig_hash, "__wrapped__") else orig_hash(self)
            return f"{base}-{_cache_tag()}"

        B.add_stages, B.hash = add_stages, hash_
    _saved["run"] = JITFunction.run
    JITFunction.run = _patched_run(JITFunction.run, keyed_by_hook=use_hook)
    try:
        from triton.runtime.autotuner import Autotuner
        if hasattr(Autotuner, "_bench"):
            _saved["bench"] = Autotuner._bench
            Autotuner._bench = _patched_bench(Autotuner._bench)
    except Exception:
        pass
    _cfg["on"] = True
    _cfg["mode"] = "inspection_hook" if use_hook else "patched_backend"


def disable():
    import triton
    from triton.runtime.jit import JITFunction
    from triton.backends.nvidia import compiler as nvc

    if not _cfg["on"]:
        return
    if "hook" in _saved:
        triton.knobs.runtime.add_stages_inspection_hook = _saved.pop("hook")
    if "add_stages" in _saved:
        B = _backend_class(nvc)
        B.add_stages = _saved.pop("add_stages")
        h = _saved.pop("hash")
        if h is not None:
            B.hash = h
    JITFunction.run = _saved.pop("run")
    JITFunction.parse = _saved.pop("parse")
    if "bench" in _saved:
        from triton.runtime.autotuner import Autotuner
        Autotuner._bench = _saved.pop("bench")
    from triton.compiler import code_generator as _cg, compiler as _cc
    if getattr(_cc, "ast_to_ttir", None) is _cg.ast_to_ttir:
        _cc.ast_to_ttir = _saved["ast_to_ttir"]
    _cg.ast_to_ttir = _saved.pop("ast_to_ttir")
    _cfg["on"] = False


if os.environ.get("TICKBOUND_TRITON") == "1":
    enable()

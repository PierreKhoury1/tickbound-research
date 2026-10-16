"""Measured variant selection for Triton kernels: generate by rule, select by CUDA-event timing.

On the first launch of a kernel for a shape bucket the tuner

1. snapshots every storage reachable from the tensor arguments (the launch has not happened yet);
2. runs the original kernel twice from the snapshot: its post-state is the reference, and two equal post-states
   mean the kernel is deterministic;
3. builds candidates in stages, each derived from the best so far:
     passes:   original, read-only loads (nc), nc + loop prefetch (pf)
     warps:    best with num_warps / 2 and * 2 (then one more step in the winning direction)
     stages:   best with num_stages - 1 and + 1
   a candidate whose cubin equals one already seen is dropped (the knob did nothing for this kernel), and so is
   any candidate that fails to compile or whose post-state differs from the reference by a single byte (warps
   variants change reduction order, so they are only tried on deterministic kernels);
4. times the survivors with CUDA events: rounds of shuffled launches, each preceded by a restore of the snapshot
   and a GPU sleep longer than the CPU launch cost, so the event pair brackets GPU work only. A candidate replaces
   the incumbent only if its median per-round ratio is >= 1 + min_gain and a sign test over the rounds gives
   p < 0.01;
5. restores the snapshot and performs the real launch with the winner, and records the decision (in memory and
   in a JSON file per GPU / Triton version, so later processes skip the search).

Launches during CUDA graph capture never tune (decision from the cache, else the original). Decisions are keyed by
kernel source hash + argument dtypes + power-of-two buckets of shapes and integer arguments. A decision that changes
num_warps is re-verified (one extra launch of each, byte compare) on the first launch of every new exact shape.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import random
import tempfile
import time
from typing import NamedTuple

_torch = None


def _t():
    global _torch
    if _torch is None:
        import torch
        _torch = torch
    return _torch


class Variant(NamedTuple):
    nc: bool = False
    pf: bool = False
    num_warps: int | None = None
    num_stages: int | None = None

    @property
    def name(self) -> str:
        s = "orig" if not (self.nc or self.pf) else ("nc+pf" if self.pf else "nc")
        if self.num_warps:
            s += f"@w{self.num_warps}"
        if self.num_stages:
            s += f"@s{self.num_stages}"
        return s

    @staticmethod
    def parse(s: str) -> "Variant":
        parts = s.split("@")
        nc, pf = parts[0] in ("nc", "nc+pf"), parts[0] == "nc+pf"
        w = st = None
        for p in parts[1:]:
            if p[0] == "w":
                w = int(p[1:])
            elif p[0] == "s":
                st = int(p[1:])
        return Variant(nc, pf, w, st)


ORIG = Variant()

cfg = {
    "min_gain": float(os.environ.get("TICKBOUND_TUNE_MIN_GAIN", "0.02")),
    "rounds": int(os.environ.get("TICKBOUND_TUNE_ROUNDS", "15")),
    "max_rounds": int(os.environ.get("TICKBOUND_TUNE_MAX_ROUNDS", "41")),
    "max_bytes": int(float(os.environ.get("TICKBOUND_TUNE_MAX_MB", "1024")) * 2**20),
    "search": os.environ.get("TICKBOUND_TUNE_SEARCH", "full"),  # full | passes
    "cache_path": os.environ.get("TICKBOUND_TUNE_CACHE"),
    "seed": 1234,
    "max_per_kernel": int(os.environ.get("TICKBOUND_TUNE_MAX_PER_KERNEL", "16")),
}

_mem = {}          # (kernel id, bucket key) -> Variant
_tuned_count = {}  # kernel id -> number of shape buckets searched in this process
_verified = set()  # (kernel id, exact key) for decisions that change num_warps
_disk = None
_sleep_cyc_per_us = None


# ------------------------------------------------------------------ argument helpers
def backing(a):
    """The torch.Tensor behind a pointer argument (the tensor itself, or wrappers such as FlagGems' StridedBuffer
    that keep it in ``_base`` / ``base``); None if it cannot be determined."""
    T = _t().Tensor
    if isinstance(a, T):
        return a
    for name in ("_base", "base"):
        b = getattr(a, name, None)
        if isinstance(b, T):
            return b
    return None


def describe(a):
    """Hashable, launch-independent description of a non-scalar argument."""
    if hasattr(a, "data_ptr"):
        return ("ptr", type(a).__name__, str(getattr(a, "dtype", "")), tuple(getattr(a, "shape", ()) or ()))
    try:
        hash(a)
        return a
    except TypeError:
        return type(a).__name__


def budget_ok(fn) -> bool:
    """At most max_per_kernel shape buckets are searched per kernel and process; later buckets run the original."""
    kid = kernel_id(fn)
    n = _tuned_count.get(kid, 0)
    if n >= cfg["max_per_kernel"]:
        return False
    _tuned_count[kid] = n + 1
    return True


# ------------------------------------------------------------------ keys
def _bucket(n: int) -> int:
    return n if n <= 16 else 1 << (n - 1).bit_length()


def keys(args, kwargs):
    """(bucket key, exact key) of a launch: tensor dtypes + shapes, scalar ints, constexpr / option kwargs."""
    T = _t().Tensor
    b, e = [], []
    for a in args:
        if isinstance(a, T):
            sh = tuple(a.shape)
            b.append((a.dtype, tuple(_bucket(x) for x in sh)))
            e.append(sh)
        elif isinstance(a, bool) or a is None or isinstance(a, str):
            b.append(a)
        elif isinstance(a, int):
            b.append(("i", _bucket(a)))
            e.append(a)
        elif isinstance(a, float):
            b.append("f")
        elif hasattr(a, "data_ptr") and hasattr(a, "shape"):
            sh = tuple(a.shape)
            b.append((str(getattr(a, "dtype", "")), tuple(_bucket(x) for x in sh)))
            e.append(sh)
        else:
            b.append(type(a).__name__)
    for k, v in kwargs.items():
        if isinstance(v, (int, float, bool, str)) or v is None:
            b.append((k, v))
        else:
            b.append((k, type(v).__name__))
    return tuple(b), tuple(e)


def kernel_id(fn) -> str:
    kid = fn.__dict__.get("_tb_kid")
    if kid is None:
        src = getattr(fn, "src", "") or ""
        kid = f"{fn.__module__}.{fn.__name__}:{hashlib.sha1(src.encode()).hexdigest()[:12]}"
        fn._tb_kid = kid
    return kid


# ------------------------------------------------------------------ disk cache
def _cache_file():
    if cfg["cache_path"]:
        return cfg["cache_path"]
    torch = _t()
    import triton
    from . import PASS_VERSION
    gpu = torch.cuda.get_device_name().replace(" ", "_").replace("/", "_")
    d = os.path.join(os.path.expanduser("~"), ".cache", "tickbound", "tune")
    return os.path.join(d, f"{gpu}-triton{triton.__version__}-{PASS_VERSION}.json")


def _disk_load():
    global _disk
    if _disk is None:
        try:
            with open(_cache_file()) as f:
                _disk = json.load(f)
        except Exception:
            _disk = {}
    return _disk


def _disk_store(kid, bkey, rec):
    d = _disk_load()
    d[f"{kid}|{bkey!r}"] = rec
    path = _cache_file()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
        with os.fdopen(fd, "w") as f:
            json.dump(d, f, indent=0)
        os.replace(tmp, path)
    except Exception:
        pass


def lookup(fn, bkey):
    kid = kernel_id(fn)
    v = _mem.get((kid, bkey))
    if v is None:
        rec = _disk_load().get(f"{kid}|{bkey!r}")
        if rec is not None:
            v = _mem[(kid, bkey)] = Variant.parse(rec["chosen"])
    return v


# ------------------------------------------------------------------ snapshots
def _storages(args, kwargs):
    """Distinct storages behind all pointer arguments; None if one of them cannot be resolved to a tensor."""
    seen = {}
    for a in list(args) + list(kwargs.values()):
        if not hasattr(a, "data_ptr"):
            continue
        b = backing(a)
        if b is None:
            return None
        if b.is_cuda:
            s = b.untyped_storage()
            seen.setdefault(s.data_ptr(), s)
    return list(seen.values())


_cu = None


def _cuda():
    """CUDA driver API via ctypes. Snapshots must not go through torch ops: libraries such as FlagGems replace
    aten::copy_ / clone / eq with their own Triton kernels, which would re-enter the tuner (and their locks)."""
    global _cu
    if _cu is None:
        import ctypes
        lib = ctypes.CDLL("nvcuda.dll" if os.name == "nt" else "libcuda.so.1")
        lib.cuMemcpyDtoDAsync_v2.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_void_p]
        lib.cuMemcpyDtoH_v2.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.c_size_t]
        _cu = lib
    return _cu


def _dtod(dst, src, n):
    r = _cuda().cuMemcpyDtoDAsync_v2(dst, src, n, _t().cuda.current_stream().cuda_stream)
    if r != 0:
        raise RuntimeError(f"cuMemcpyDtoDAsync failed: {r}")


class Snapshot:
    def __init__(self, storages):
        torch = _t()
        self.live = [(s.data_ptr(), s.nbytes()) for s in storages if s.nbytes()]
        self.saved = []
        for p, n in self.live:
            buf = torch.empty(n, dtype=torch.uint8, device="cuda")
            _dtod(buf.data_ptr(), p, n)
            self.saved.append(buf)

    def restore(self):
        for (p, n), buf in zip(self.live, self.saved):
            _dtod(p, buf.data_ptr(), n)

    def state(self):
        """Host copy of every live storage (bytes), after the work queued so far."""
        import numpy as np
        _t().cuda.current_stream().synchronize()
        out = []
        for p, n in self.live:
            h = np.empty(n, dtype=np.uint8)
            r = _cuda().cuMemcpyDtoH_v2(h.ctypes.data, p, n)
            if r != 0:
                raise RuntimeError(f"cuMemcpyDtoH failed: {r}")
            out.append(h)
        return out

    def same_as(self, ref):
        import numpy as np
        return all(np.array_equal(a, b) for a, b in zip(self.state(), ref))


# ------------------------------------------------------------------ timing
def _cyc_per_us():
    global _sleep_cyc_per_us
    if _sleep_cyc_per_us is None:
        torch = _t()
        a, b = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
        torch.cuda._sleep(1000)
        a.record()
        torch.cuda._sleep(2_000_000)
        b.record()
        b.synchronize()
        _sleep_cyc_per_us = 2_000_000 / max(a.elapsed_time(b) * 1000.0, 1.0)
    return _sleep_cyc_per_us


def _sign_p(wins, n):
    """One-sided sign test: P(X >= wins) for X ~ Bin(n, 1/2)."""
    return sum(math.comb(n, k) for k in range(wins, n + 1)) / 2 ** n


def _time(launch, variants, snap, rounds, sleep_us, rng):
    """Per-variant lists of GPU microseconds, one sample per round, interleaved and shuffled."""
    torch = _t()
    cyc = int(sleep_us * _cyc_per_us())
    evs = []
    for r in range(rounds):
        order = list(range(len(variants)))
        rng.shuffle(order)
        for i in order:
            snap.restore()
            torch.cuda._sleep(cyc)
            s, e = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
            s.record()
            launch(variants[i])
            e.record()
            evs.append((i, r, s, e))
    torch.cuda.synchronize()
    out = [[0.0] * rounds for _ in variants]
    for i, r, s, e in evs:
        out[i][r] = s.elapsed_time(e) * 1000.0
    return out


def _median(x):
    x = sorted(x)
    n = len(x)
    return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])


# ------------------------------------------------------------------ search
def tune(fn, launch, args, kwargs, bkey, log, passes_ok=True):
    """Pick a variant for this kernel / shape bucket; leaves memory as one original launch would (the caller then
    launches the returned variant for real after restore). Returns (variant, snapshot or None)."""
    torch = _t()
    kid = kernel_id(fn)
    rec = {"tune": kid, "kernel": fn.__name__, "key": repr(bkey)[:300]}
    storages = _storages(args, kwargs)
    if storages is None:
        rec.update(chosen=ORIG.name, reason="pointer argument not backed by a visible tensor")
        log(rec)
        _mem[(kid, bkey)] = ORIG
        return ORIG, None
    nbytes = sum(s.nbytes() for s in storages)
    if nbytes > cfg["max_bytes"]:
        rec.update(chosen=ORIG.name, reason=f"snapshot too large ({nbytes >> 20} MB)")
        log(rec)
        _mem[(kid, bkey)] = ORIG
        return ORIG, None
    t0 = time.perf_counter()
    try:
        snap = Snapshot(storages)
    except Exception as ex:
        rec.update(chosen=ORIG.name, reason=f"snapshot failed: {ex!r}"[:300])
        log(rec)
        _mem[(kid, bkey)] = ORIG
        return ORIG, None
    try:
        return _search(fn, launch, kwargs, kid, bkey, log, passes_ok, rec, snap, t0)
    except Exception as ex:  # never break the program: memory back to the pre-launch state, original kernel
        snap.restore()
        rec.update(chosen=ORIG.name, reason=f"tuner error: {ex!r}"[:300])
        log(rec)
        _mem[(kid, bkey)] = ORIG
        return ORIG, snap


def _search(fn, launch, kwargs, kid, bkey, log, passes_ok, rec, snap, t0):
    torch = _t()
    rng = random.Random(cfg["seed"])

    # reference post-state and determinism
    k0 = launch(ORIG)
    ref = snap.state()
    snap.restore()
    launch(ORIG)
    det = snap.same_as(ref)
    cubins = {_cubin_hash(k0): ORIG}
    base_w = kwargs.get("num_warps") or getattr(getattr(k0, "metadata", None), "num_warps", None) or 4
    base_s = kwargs.get("num_stages") or getattr(getattr(k0, "metadata", None), "num_stages", None) or 3
    tried = []

    def admit(v):
        """Compile + verify a candidate; True if it is a new, correct kernel."""
        snap.restore()
        try:
            k = launch(v)
            torch.cuda.synchronize()
        except Exception as ex:
            tried.append({"v": v.name, "verdict": "compile_or_launch_error", "err": repr(ex)[:200]})
            return False
        h = _cubin_hash(k)
        if h in cubins:
            tried.append({"v": v.name, "verdict": f"same_cubin_as_{cubins[h].name}"})
            return False
        cubins[h] = v
        if det and not snap.same_as(ref):
            tried.append({"v": v.name, "verdict": "output_differs"})
            return False
        if not det and v.num_warps not in (None, base_w):
            tried.append({"v": v.name, "verdict": "skipped_nondeterministic"})
            return False
        return True

    # CPU cost of one launch bounds how long the GPU must sleep before each timed launch
    c0 = time.perf_counter()
    launch(ORIG)
    sleep_us = max(50.0, 3e6 * (time.perf_counter() - c0) + 20.0)

    best = ORIG

    def race(cands):
        nonlocal best
        cands = [c for c in cands if admit(c)]
        if not cands:
            return False
        vs = [best] + cands
        samples = _time(launch, vs, snap, cfg["rounds"], sleep_us, rng)
        ratios = [[b / max(c, 1e-3) for b, c in zip(samples[0], samples[i])] for i in range(1, len(vs))]
        meds = [_median(r) for r in ratios]
        j = max(range(len(cands)), key=lambda i: meds[i])
        # borderline leader: more rounds for incumbent vs leader only
        if 1.0 < meds[j] < 1.0 + 2 * cfg["min_gain"] and cfg["max_rounds"] > cfg["rounds"]:
            extra = _time(launch, [best, cands[j]], snap, cfg["max_rounds"] - cfg["rounds"], sleep_us, rng)
            samples[0] += extra[0]
            samples[j + 1] += extra[1]
            ratios[j] = [b / max(c, 1e-3) for b, c in zip(samples[0], samples[j + 1])]
            meds[j] = _median(ratios[j])
        won = False
        for i, c in enumerate(cands):
            n, w = len(ratios[i]), sum(x > 1.0 for x in ratios[i])
            p = _sign_p(w, n)
            ok = meds[i] >= 1.0 + cfg["min_gain"] and p < 0.01
            tried.append({"v": c.name, "vs": best.name, "ratio_med": round(meds[i], 4), "wins": f"{w}/{n}",
                          "p": round(p, 5), "us_med": round(_median(samples[i + 1]), 3),
                          "verdict": "win" if ok and i == j else ("faster_not_best" if ok else "no_gain")})
        if meds[j] >= 1.0 + cfg["min_gain"] and _sign_p(sum(x > 1.0 for x in ratios[j]), len(ratios[j])) < 0.01:
            best, won = cands[j], True
        return won

    if passes_ok:  # arguments do not alias: read-only loads and prefetch are valid for this launch
        race([Variant(nc=True), Variant(nc=True, pf=True)])
    if cfg["search"] == "full":
        def at(v, w=None, s=None):
            return Variant(v.nc, v.pf, w if w is not None else v.num_warps, s if s is not None else v.num_stages)
        if det:
            ws = [w for w in (base_w // 2, base_w * 2) if 1 <= w <= 32]
            if race([at(best, w=w) for w in ws]) and best.num_warps:
                step = best.num_warps * 2 if best.num_warps > base_w else best.num_warps // 2
                if 1 <= step <= 32:
                    race([at(best, w=step)])
        ss = [s for s in (base_s - 1, base_s + 1) if 1 <= s <= 6]
        race([at(best, s=s) for s in ss])

    # final head-to-head for the record: original vs chosen, fresh rounds
    vs = [ORIG] if best == ORIG else [ORIG, best]
    fin = _time(launch, vs, snap, cfg["rounds"], sleep_us, rng)
    orig_us, best_us = _median(fin[0]), _median(fin[-1])
    _mem[(kid, bkey)] = best
    rec.update(chosen=best.name, deterministic=det, base_warps=base_w, base_stages=base_s,
               orig_us=round(orig_us, 3), best_us=round(best_us, 3), speedup=round(orig_us / max(best_us, 1e-3), 4),
               tune_ms=round(1000 * (time.perf_counter() - t0), 1), candidates=tried)
    _disk_store(kid, bkey, {"chosen": best.name, "orig_us": rec["orig_us"], "best_us": rec["best_us"],
                            "deterministic": det})
    log(rec)
    return best, snap


def verify_exact(fn, launch, chosen, args, kwargs, ekey):
    """For a decision that changes num_warps: on a new exact shape, check the chosen variant reproduces the original
    byte for byte; returns the variant to use (chosen, or the same passes at the original warps)."""
    kid = kernel_id(fn)
    if (kid, ekey) in _verified:
        return chosen
    storages = _storages(args, kwargs)
    if storages is None or sum(s.nbytes() for s in storages) > cfg["max_bytes"]:
        return Variant(chosen.nc, chosen.pf, None, chosen.num_stages)
    snap = Snapshot(storages)
    launch(ORIG)
    ref = snap.state()
    snap.restore()
    launch(chosen)
    ok = snap.same_as(ref)
    snap.restore()
    if ok:
        _verified.add((kid, ekey))
        return chosen
    return Variant(chosen.nc, chosen.pf, None, chosen.num_stages)


def verified(fn, ekey) -> bool:
    return (kernel_id(fn), ekey) in _verified


def _cubin_hash(k):
    try:
        b = k.asm["cubin"]
        return hashlib.sha1(b).hexdigest()
    except Exception:
        return id(k)

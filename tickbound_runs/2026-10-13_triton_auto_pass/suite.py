# suite.py - run real Triton kernels from real libraries (Liger-Kernel, FlagGems) through their public APIs, at
# LLM decode and prefill shapes, and record per case: which Triton kernels were compiled (TRITON_DUMP_DIR hashes),
# per-kernel GPU time (torch.profiler / CUPTI), and a SHA-256 of every output (and gradient) for bitwise checks.
#
#   python suite.py --lib liger|flaggems --out results.jsonl [--only NAME,...] [--reps 30]
#
# Crash-safe: writes {"case": .., "status": "start"} before each case; run.sh restarts the process after a crash and
# the case is recorded as crashed. Cases already in --out are skipped.
import argparse, hashlib, json, os, sys, time, traceback

import torch

p = argparse.ArgumentParser()
p.add_argument("--lib", required=True)
p.add_argument("--out", required=True)
p.add_argument("--only", default="")
p.add_argument("--reps", type=int, default=30)
p.add_argument("--tb", default="", help="'' = Triton as is; 'always' / 'occupancy' = tickbound.triton pass with that policy")
p.add_argument("--tblog", default="")
args = p.parse_args()
if args.tb:
    import tickbound.triton as tbt
    # "always" / "occupancy": pass v1 (read-only loads) with that policy; "pf": v1 + v2 (loop prefetch), always
    if args.tb == "pf":
        tbt.enable(policy="always", log=args.tblog or None, prefetch=True)
    else:
        tbt.enable(policy=args.tb, log=args.tblog or None, prefetch=False)
DEV = "cuda"
BF = torch.bfloat16


def seed(n=0):
    torch.manual_seed(1234 + n)


def rn(*s, dtype=BF, grad=False, scale=1.0):
    # inputs are generated on the CPU: GPU RNG kernels may be replaced by the library under test (FlagGems
    # registers its own randn), which made inputs differ between processes
    t = torch.randn(*s, dtype=torch.float32).mul_(scale).to(dtype).to(DEV)
    return t.requires_grad_(grad)


def ri(hi, s):
    return torch.randint(0, hi, s).to(DEV)


# ---------------------------------------------------------------- case lists: name -> (setup() -> fn, run_backward)
CASES = {}


def case(name, bwd=False):
    def deco(f):
        CASES[name] = (f, bwd)
        return f
    return deco


if args.lib == "liger":
    from liger_kernel.transformers import functional as LF

    for M in (16, 4096):
        H = 4096

        @case(f"rms_norm_M{M}", bwd=True)
        def _(M=M, H=H):
            x, w = rn(M, H, grad=True), rn(H, grad=True)
            return lambda: LF.liger_rms_norm(x, w, 1e-6, in_place=False), [x, w]

        @case(f"fused_add_rms_norm_M{M}")
        def _(M=M, H=H):
            x, r, w = rn(M, H), rn(M, H), rn(H)
            return lambda: LF.liger_fused_add_rms_norm(x.clone(), r.clone(), w, 1e-6, in_place=False), []

        @case(f"layer_norm_M{M}", bwd=True)
        def _(M=M, H=H):
            x, w, b = rn(M, H, grad=True), rn(H, grad=True), rn(H, grad=True)
            return lambda: LF.liger_layer_norm(x, w, b, 1e-6), [x, w, b]

        @case(f"poly_norm_M{M}")
        def _(M=M, H=H):
            x, w, b = rn(M, H), rn(3), rn(1)
            return lambda: LF.liger_poly_norm(x, w, b, 1e-6, in_place=False), []

        @case(f"dyt_M{M}", bwd=True)
        def _(M=M, H=H):
            x, a, g, b = rn(M, H, grad=True), rn(1, grad=True), rn(H, grad=True), rn(H, grad=True)
            return lambda: LF.liger_dyt(x, a, g, b), [x, a, g, b]

        @case(f"swiglu_M{M}", bwd=True)
        def _(M=M):
            a, b = rn(M, 11008, grad=True), rn(M, 11008, grad=True)
            return lambda: LF.liger_swiglu(a, b), [a, b]

        @case(f"geglu_M{M}", bwd=True)
        def _(M=M):
            a, b = rn(M, 11008, grad=True), rn(M, 11008, grad=True)
            return lambda: LF.liger_geglu(a, b), [a, b]

        @case(f"relu_squared_M{M}")
        def _(M=M):
            x = rn(M, 11008)
            return lambda: LF.liger_relu_squared(x), []

        @case(f"softmax_M{M}", bwd=True)
        def _(M=M):
            x = rn(M, 32000, grad=True)
            return lambda: LF.liger_softmax(x), [x]

        @case(f"sparsemax_M{M}")
        def _(M=M):
            x = rn(M, 1024, dtype=torch.float32)
            return lambda: LF.liger_sparsemax(x), []

        @case(f"cross_entropy_M{M}", bwd=True)
        def _(M=M):
            x = rn(M, 128256, grad=True)
            t = ri(128256, (M,))
            return lambda: LF.liger_cross_entropy(x, t), [x]

        @case(f"fused_linear_ce_M{M}", bwd=True)
        def _(M=M):
            x, w = rn(M, 4096, grad=True, scale=0.05), rn(32000, 4096, grad=True, scale=0.02)
            t = ri(32000, (M,))
            return lambda: LF.liger_fused_linear_cross_entropy(x, w, t), [x, w]

        @case(f"kl_div_M{M}", bwd=True)
        def _(M=M):
            x = torch.log_softmax(rn(M, 32000, dtype=torch.float32), -1).requires_grad_(True)
            y = torch.softmax(rn(M, 32000, dtype=torch.float32), -1)
            return lambda: LF.liger_kl_div(x, y), [x]

        @case(f"jsd_M{M}", bwd=True)
        def _(M=M):
            x = torch.log_softmax(rn(M, 32000, dtype=torch.float32), -1).requires_grad_(True)
            y = torch.log_softmax(rn(M, 32000, dtype=torch.float32), -1)
            return lambda: LF.liger_jsd(x, y), [x]

        @case(f"tvd_M{M}", bwd=True)
        def _(M=M):
            x = torch.softmax(rn(M, 32000, dtype=torch.float32), -1).requires_grad_(True)
            y = torch.softmax(rn(M, 32000, dtype=torch.float32), -1)
            return lambda: LF.liger_tvd(x, y), [x]

    for S in (16, 2048):
        @case(f"rope_S{S}", bwd=True)
        def _(S=S):
            q, k = rn(1, 32, S, 128, grad=True), rn(1, 8, S, 128, grad=True)
            cos, sin = rn(1, S, 128), rn(1, S, 128)
            return lambda: LF.liger_rope(q, k, cos, sin), [q, k]

    @case("group_norm_B8", bwd=True)
    def _():
        x, w, b = rn(8, 128, 1024, grad=True), rn(128, grad=True), rn(128, grad=True)
        return lambda: LF.liger_group_norm(x, w, b, 128, 32, 1e-6), [x, w, b]

elif args.lib == "flaggems":
    import flag_gems
    import torch.nn.functional as F

    flag_gems.enable()
    for M in (16, 4096):
        H = 4096
        ops = {
            "silu": lambda x: F.silu(x), "gelu": lambda x: F.gelu(x), "exp": torch.exp, "rsqrt": torch.rsqrt,
            "softmax": lambda x: torch.softmax(x, -1), "log_softmax": lambda x: torch.log_softmax(x, -1),
            "sum": lambda x: x.sum(-1), "mean": lambda x: x.mean(-1), "amax": lambda x: x.amax(-1),
            "argmax": lambda x: x.argmax(-1), "cumsum": lambda x: x.cumsum(-1), "var_mean": lambda x: torch.var_mean(x, -1),
            "vector_norm": lambda x: torch.linalg.vector_norm(x, dim=-1), "topk": lambda x: torch.topk(x, 50, -1),
            "sort": lambda x: torch.sort(x, -1), "layer_norm": lambda x: F.layer_norm(x, (H,)),
            "rms_norm": lambda x: F.rms_norm(x, (H,)), "masked_fill": lambda x: x.masked_fill(x > 0.5, 0.0),
            "where": lambda x: torch.where(x > 0, x, -x), "add": lambda x: x + x, "mul": lambda x: x * 1.5,
            "pow": lambda x: x.pow(2), "tanh": torch.tanh, "sigmoid": torch.sigmoid,
        }
        for nm, f in ops.items():
            @case(f"{nm}_M{M}")
            def _(M=M, H=H, f=f):
                x = rn(M, H)
                return lambda: f(x), []

        @case(f"mm_M{M}")
        def _(M=M, H=H):
            a, b = rn(M, H, scale=0.05), rn(H, H, scale=0.05)
            return lambda: torch.mm(a, b), []

        @case(f"addmm_M{M}")
        def _(M=M, H=H):
            c, a, b = rn(H), rn(M, H, scale=0.05), rn(H, H, scale=0.05)
            return lambda: torch.addmm(c, a, b), []

        @case(f"embedding_M{M}")
        def _(M=M, H=H):
            w, i = rn(32000, H), ri(32000, (M,))
            return lambda: F.embedding(i, w), []

        @case(f"index_select_M{M}")
        def _(M=M, H=H):
            w, i = rn(32000, H), ri(32000, (M,))
            return lambda: torch.index_select(w, 0, i), []

        @case(f"gather_M{M}")
        def _(M=M, H=H):
            x, i = rn(M, H), ri(H, (M, H))
            return lambda: torch.gather(x, 1, i), []

        @case(f"cross_entropy_M{M}")
        def _(M=M):
            x, t = rn(M, 32000), ri(32000, (M,))
            return lambda: F.cross_entropy(x, t), []

        @case(f"cat_M{M}")
        def _(M=M, H=H):
            a, b = rn(M, H), rn(M, H)
            return lambda: torch.cat([a, b], -1), []

    @case("bmm_B32")
    def _():
        a, b = rn(32, 16, 128, scale=0.1), rn(32, 128, 2048, scale=0.1)
        return lambda: torch.bmm(a, b), []
elif args.lib == "cuasmrl":
    # CuAsmRL's own benchmark kernels (cuasmrl_kernels.py, verbatim extraction), launched as their benchmarks /
    # Kernl launch them; fp16 like the originals
    import triton
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cuasmrl_kernels as CK
    H16 = torch.float16

    import kernl_port as KP
    for (B, M) in ((1, 16), (1, 4096)):
        @case(f"rmsnorm_kernl_port_M{M}")
        def _(B=B, M=M):
            x, w = rn(B, M, 4096, dtype=H16), rn(4096, dtype=H16, scale=0.2)
            out = torch.empty_like(x)
            def f():
                KP.rmsnorm_kernl_port[(B, M)](x, w, out, *x.stride(), w.stride(0), *out.stride(),
                                              N_SIZE=4096, eps=1e-6, BLOCK_N_SIZE=1024, num_warps=4, num_stages=2)
                return out
            return f, []

    for (B, M) in ((1, 16), (1, 4096)):
        @case(f"rmsnorm_kernl_M{M}")
        def _(B=B, M=M):
            x, w = rn(B, M, 4096, dtype=H16), rn(4096, dtype=H16, scale=0.2)
            out = torch.empty_like(x)
            def f():
                CK.rmsnorm_cuasmrl[(B, M)](x, w, out, *x.stride(), w.stride(0), *out.stride(),
                                           N_SIZE=4096, eps=1e-6, BLOCK_N_SIZE=1024, num_warps=4, num_stages=2)
                return out
            return f, []

    # (M, N, K, BM, BN, BK, warps, stages): CuAsmRL's shape + config, Kernl's decode config, LLaMA FFN prefill
    for (M, N, K, BM, BN, BK, W, S) in ((512, 512, 1024, 64, 32, 32, 2, 5), (16, 11008, 4096, 16, 16, 64, 4, 2),
                                        (16, 4096, 4096, 32, 64, 32, 2, 5), (4096, 11008, 4096, 64, 128, 32, 4, 4)):
        @case(f"fused_ff_M{M}_N{N}_K{K}_{BM}x{BN}x{BK}_w{W}s{S}")
        def _(M=M, N=N, K=K, BM=BM, BN=BN, BK=BK, W=W, S=S):
            a, w1, w3 = rn(M, K, dtype=H16), rn(K, N, dtype=H16, scale=0.02), rn(K, N, dtype=H16, scale=0.02)
            rw, out = rn(K, dtype=H16, scale=0.2), torch.empty(M, N, device=DEV, dtype=H16)
            grid = (triton.cdiv(M, BM) * triton.cdiv(N, BN),)
            def f():
                CK.tt_ff[grid](a, w1, w3, out, rw, M, N, K, *a.stride(), *w1.stride(), *w3.stride(), *out.stride(),
                               rw.stride(0), USE_FP8=False, EPS=1e-6, BLOCK_SIZE_M=BM, BLOCK_SIZE_N=BN,
                               BLOCK_SIZE_K=BK, GROUP_SIZE_M=8, num_warps=W, num_stages=S)
                return out
            return f, []

    for (R, C) in ((16, 4096), (4096, 4096), (4096, 32000)):
        @case(f"softmax_R{R}_C{C}")
        def _(R=R, C=C):
            x = rn(R, C, dtype=H16)
            y = torch.empty_like(x)
            BS = triton.next_power_of_2(C)
            nw = 4 if BS < 2048 else (8 if BS < 4096 else 16)
            def f():
                CK.softmax[(R,)](y, x, x.stride(0), y.stride(0), R, C, BLOCK_SIZE=BS, num_warps=nw)
                return y
            return f, []

    for (M, N, K) in ((16, 4096, 4096), (4096, 4096, 4096)):
        @case(f"matmul_leaky_M{M}")
        def _(M=M, N=N, K=K):
            a, b = rn(M, K, dtype=H16, scale=0.05), rn(K, N, dtype=H16, scale=0.05)
            c = torch.empty(M, N, device=DEV, dtype=H16)
            BM, BN, BK = (16, 64, 64) if M <= 64 else (128, 128, 32)
            grid = (triton.cdiv(M, BM) * triton.cdiv(N, BN),)
            def f():
                CK.matmul_leaky[grid](a, b, c, M, N, K, *a.stride(), *b.stride(), *c.stride(), BLOCK_SIZE_M=BM,
                                      BLOCK_SIZE_N=BN, BLOCK_SIZE_K=BK, GROUP_SIZE_M=8, ACTIVATION="leaky_relu",
                                      num_warps=4, num_stages=4)
                return c
            return f, []
else:
    sys.exit(f"unknown lib {args.lib}")


# ---------------------------------------------------------------- helpers
def tensors(o):
    if isinstance(o, torch.Tensor):
        yield o
    elif isinstance(o, (list, tuple)):
        for x in o:
            yield from tensors(x)
    elif hasattr(o, "_fields") or hasattr(o, "__dict__"):
        for x in (o if hasattr(o, "_fields") else vars(o).values()):
            yield from tensors(x)


def digest(ts):
    h = hashlib.sha256()
    for t in ts:
        if t is None:
            continue
        t = t.detach().contiguous()
        h.update(str((t.dtype, tuple(t.shape))).encode())
        h.update(t.reshape(-1).view(torch.uint8).cpu().numpy().tobytes() if t.numel() else b"")
    return h.hexdigest()


def first_tensor(o):
    for t in tensors(o):
        return t


def dump_hashes():
    d = os.environ.get("TRITON_DUMP_DIR")
    return set(os.listdir(d)) if d and os.path.isdir(d) else set()


def step(fn, inputs, bwd):
    for t in inputs:
        t.grad = None
    o = fn()
    if bwd:
        t = first_tensor(o)
        g = torch.ones_like(t) if t.dim() else torch.ones((), device=DEV, dtype=t.dtype)
        t.backward(g)
    return o


done = set()
if os.path.exists(args.out):
    for line in open(args.out):
        try:
            done.add(json.loads(line)["case"])
        except Exception:
            pass
only = set(filter(None, args.only.split(",")))
outf = open(args.out, "a")


def emit(rec):
    outf.write(json.dumps(rec) + "\n")
    outf.flush()


from torch.profiler import ProfilerActivity, profile

for i, (name, (setup, bwd)) in enumerate(CASES.items()):
    if name in done or (only and name not in only):
        continue
    emit({"case": name, "status": "start"})
    rec = {"case": name, "lib": args.lib, "bwd": bwd, "status": "ok"}
    try:
        seed(i)
        before = dump_hashes()
        fn, inputs = setup()
        o = step(fn, inputs, bwd)
        torch.cuda.synchronize()
        rec["new_dump_hashes"] = sorted(dump_hashes() - before)
        rec["out_sha256"] = digest(list(tensors(o)) + [t.grad for t in inputs])
        # determinism: second run must give the same bytes (else bitwise checks are meaningless for this case)
        o2 = step(fn, inputs, bwd)
        torch.cuda.synchronize()
        rec["deterministic"] = digest(list(tensors(o2)) + [t.grad for t in inputs]) == rec["out_sha256"]
        for _ in range(5):
            step(fn, inputs, bwd)
        torch.cuda.synchronize()
        with profile(activities=[ProfilerActivity.CUDA]) as prof:
            for _ in range(args.reps):
                step(fn, inputs, bwd)
            torch.cuda.synchronize()
        ks = {}
        for e in prof.events():
            if e.device_type.name != "CUDA":
                continue
            d = ks.setdefault(e.name, [])
            d.append(e.device_time if hasattr(e, "device_time") else e.cuda_time)
        rec["kernels"] = {k: {"n": len(v), "per_call_n": len(v) / args.reps, "us_sum": sum(v),
                              "us_med": sorted(v)[len(v) // 2], "us_min": min(v)} for k, v in ks.items()}
        t0 = torch.cuda.Event(enable_timing=True); t1 = torch.cuda.Event(enable_timing=True)
        t0.record()
        for _ in range(args.reps):
            step(fn, inputs, bwd)
        t1.record(); torch.cuda.synchronize()
        rec["wall_us_per_step"] = t0.elapsed_time(t1) * 1000 / args.reps
        if args.tb:
            rec["tb_stats"] = tbt.stats()
    except Exception as e:
        rec["status"] = "error"
        rec["error"] = f"{type(e).__name__}: {e}"[:600]
        rec["trace"] = traceback.format_exc()[-1500:]
    emit(rec)
    print(f"[{args.lib}] {name:28s} {rec['status']:5s} "
          + (f"{rec.get('wall_us_per_step', 0):9.1f} us  kernels {len(rec.get('kernels', {}))}  new {len(rec.get('new_dump_hashes', []))}"
             f"  det {rec.get('deterministic')}" if rec["status"] == "ok" else rec["error"][:150]), flush=True)
print("SUITE DONE", flush=True)

# t_tune.py: correctness of tickbound.triton policy "tune" on a real GPU. Each check compares against plain Triton
# (same kernels, tickbound disabled) byte for byte. Usage: python t_tune.py LOG CACHE [phase]  (phase 2 = cache hit run)
import json, os, sys, hashlib
import torch, triton, triton.language as tl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tickbound.triton as tbt

log, cache = sys.argv[1], sys.argv[2]
phase = int(sys.argv[3]) if len(sys.argv) > 3 else 1
os.environ["TICKBOUND_TUNE_CACHE"] = cache
tbt._tune.cfg["cache_path"] = cache
dev = "cuda"


@triton.jit
def add_inplace(x_ptr, y_ptr, n, BLOCK: tl.constexpr):
    o = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = o < n
    tl.store(x_ptr + o, tl.load(x_ptr + o, mask=m) + tl.load(y_ptr + o, mask=m), mask=m)


@triton.jit
def count_atomic(idx_ptr, cnt_ptr, n, BLOCK: tl.constexpr):
    o = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = o < n
    tl.atomic_add(cnt_ptr + tl.load(idx_ptr + o, mask=m), 1, mask=m)


@triton.jit
def rowsum(x_ptr, out_ptr, N, BLOCK: tl.constexpr):
    r = tl.program_id(0)
    acc = tl.zeros([BLOCK], dtype=tl.float32)
    for off in range(0, N, BLOCK):
        c = off + tl.arange(0, BLOCK)
        acc += tl.load(x_ptr + r * N + c, mask=c < N, other=0.).to(tl.float32)
    tl.store(out_ptr + r, tl.sum(acc, 0))


@triton.jit
def rms(x_ptr, w_ptr, out_ptr, N, eps, BLOCK: tl.constexpr):
    row = tl.program_id(0)
    acc = tl.zeros([BLOCK], dtype=tl.float32)
    for off in range(0, N, BLOCK):
        c = off + tl.arange(0, BLOCK)
        x = tl.load(x_ptr + row * N + c, mask=c < N, other=0.).to(tl.float32)
        acc += x * x
    r = 1.0 / tl.sqrt(tl.sum(acc, 0) / N + eps)
    for off in range(0, N, BLOCK):
        c = off + tl.arange(0, BLOCK)
        x = tl.load(x_ptr + row * N + c, mask=c < N, other=0.).to(tl.float32)
        w = tl.load(w_ptr + c, mask=c < N, other=0.).to(tl.float32)
        tl.store(out_ptr + row * N + c, (x * r * w).to(tl.float16), mask=c < N)


def h(*ts):
    m = hashlib.sha256()
    for t in ts:
        m.update(t.detach().contiguous().view(torch.uint8).cpu().numpy().tobytes())
    return m.hexdigest()[:16]


g = torch.Generator().manual_seed(0)
X = torch.randn(1 << 20, generator=g).to(dev)
Y = torch.randn(1 << 20, generator=g).to(dev)
IDX = torch.randint(0, 1000, (1 << 20,), generator=g).to(dev, torch.int32)
XR = torch.randn(16, 8192, generator=g).to(dev, torch.float16)
W = torch.randn(8192, generator=g).to(dev, torch.float16)


def run_all():
    out = {}
    x = X.clone(); add_inplace[(x.numel() // 1024,)](x, Y, x.numel(), BLOCK=1024)
    add_inplace[(x.numel() // 1024,)](x, Y, x.numel(), BLOCK=1024)  # twice: second launch uses the decision
    out["inplace_x2"] = h(x)
    a = X.clone(); add_inplace[(a.numel() // 1024,)](a, a, a.numel(), BLOCK=1024)  # aliased args
    out["aliased"] = h(a)
    # tensors passed as keyword arguments, different buffers on each call (fast path must use this call's tensors)
    k1, k2 = X.clone(), (X * 2).contiguous()
    for t in (k1, k2, k1):
        add_inplace[(t.numel() // 1024,)](x_ptr=t, y_ptr=Y, n=t.numel(), BLOCK=1024)
    out["kwargs_k1"] = h(k1)
    out["kwargs_k2"] = h(k2)
    out["aliased"] = h(a)
    cnt = torch.zeros(1000, dtype=torch.int32, device=dev)
    count_atomic[(IDX.numel() // 1024,)](IDX, cnt, IDX.numel(), BLOCK=1024)
    out["atomic_counts"] = h(cnt)
    out["atomic_total"] = int(cnt.sum())
    o = torch.empty(16, device=dev); rowsum[(16,)](XR, o, 8192, BLOCK=1024); out["rowsum"] = h(o)
    o = torch.empty_like(XR); rms[(16,)](XR, W, o, 8192, 1e-6, BLOCK=1024); out["rms_M16"] = h(o)
    o2 = torch.empty_like(XR[:8]); rms[(8,)](XR[:8].contiguous(), W, o2, 8192, 1e-6, BLOCK=1024); out["rms_M8"] = h(o2)
    # graph capture of an untuned shape: must not tune, must replay correctly
    xs = XR[:4].contiguous(); og = torch.empty_like(xs)
    s = torch.cuda.Stream(); s.wait_stream(torch.cuda.current_stream())
    gr = torch.cuda.CUDAGraph()
    with torch.cuda.stream(s):
        rms[(4,)](xs, W, og, 8192, 1e-6, BLOCK=1024)  # warm compile outside capture is done by triton on first call
        torch.cuda.synchronize()
        with torch.cuda.graph(gr, stream=s):
            rms[(4,)](xs, W, og, 8192, 1e-6, BLOCK=1024)
    og.zero_(); gr.replay(); torch.cuda.synchronize(); out["graph_rms_M4"] = h(og)
    torch.cuda.synchronize()
    return out


ref = run_all()
tbt.enable(policy="tune", log=log)
got = run_all()
tbt.disable()
bad = [k for k in ref if ref[k] != got[k]]
print("phase", phase, "triton", triton.__version__, "stats", tbt.stats())
for k in ref:
    print(f"  {k:16s} ref {ref[k]}  tune {got[k]}  {'OK' if ref[k] == got[k] else 'MISMATCH'}")
for l in (open(log) if os.path.exists(log) else []):
    r = json.loads(l)
    if "tune" in r:
        print(f"  TUNE {r['kernel']:12s} chosen {r.get('chosen'):14s} speedup {r.get('speedup')} det {r.get('deterministic')} "
              f"{r.get('tune_ms')} ms  {r.get('reason', '')}")
        for c in r.get("candidates", []):
            print("        ", c)
print("RESULT", "PASS" if not bad else f"FAIL {bad}")

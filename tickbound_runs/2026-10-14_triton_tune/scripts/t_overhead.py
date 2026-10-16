# t_overhead.py: CPU cost per launch (us) of a tiny Triton kernel: plain Triton vs tickbound policies.
# Launch-bound loop (kernel ~2-5 us GPU), so per-launch wall time ~ CPU launch cost. One process per mode.
import sys, time, os, json
import torch, triton, triton.language as tl
mode = sys.argv[1]

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

@triton.jit
def add(x_ptr, y_ptr, o_ptr, n, BLOCK: tl.constexpr):
    o = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = o < n
    tl.store(o_ptr + o, tl.load(x_ptr + o, mask=m) + tl.load(y_ptr + o, mask=m), mask=m)

if mode != "plain":
    sys.path.insert(0, "/root/b/tbsrc")
    import tickbound.triton as tbt
    tbt.enable(policy=mode)
x = torch.randn(16, 4096, device="cuda", dtype=torch.float16); w = torch.randn(4096, device="cuda", dtype=torch.float16)
o = torch.empty_like(x)
a = torch.randn(4096, device="cuda"); b = torch.randn(4096, device="cuda"); c = torch.empty_like(a)
res = {"mode": mode, "triton": triton.__version__}
for name, f in (("rms_M16", lambda: rms[(16,)](x, w, o, 4096, 1e-6, BLOCK=1024)),
                ("add_4096", lambda: add[(4,)](a, b, c, 4096, BLOCK=1024))):
    for _ in range(50): f()
    torch.cuda.synchronize()
    best = 1e9
    for rep in range(5):
        t0 = time.perf_counter()
        for _ in range(2000): f()
        t1 = time.perf_counter()
        torch.cuda.synchronize()
        best = min(best, (t1 - t0) / 2000 * 1e6)
    res[name + "_cpu_us"] = round(best, 2)
print(json.dumps(res))

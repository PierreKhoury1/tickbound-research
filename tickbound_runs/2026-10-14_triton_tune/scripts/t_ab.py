# t_ab.py: same process A/B for one kernel: plain Triton vs tickbound tune (cached decision), alternating phases.
# Prints per-phase profiler kernel median, and whether the compiled kernels launched are byte-identical.
import sys, json, hashlib, os
sys.path.insert(0, "/root/b3"); sys.path.insert(0, "/root/b3/tbsrc")
import torch, triton
import cuasmrl_kernels as CK
import tickbound.triton as tbt
from torch.profiler import profile, ProfilerActivity
R, C = 16, 4096
g = torch.Generator().manual_seed(0)
x = torch.randn(R, C, generator=g).to("cuda", torch.float16); y = torch.empty_like(x)
BS = triton.next_power_of_2(C); nw = 16
def f():
    return CK.softmax[(R,)](y, x, x.stride(0), y.stride(0), R, C, BLOCK_SIZE=BS, num_warps=nw)
def phase(name):
    k = f(); torch.cuda.synchronize()
    for _ in range(20): f()
    torch.cuda.synchronize()
    with profile(activities=[ProfilerActivity.CUDA]) as prof:
        for _ in range(200): f()
        torch.cuda.synchronize()
    ts = sorted(e.device_time if hasattr(e, "device_time") else e.cuda_time for e in prof.events() if e.device_type.name == "CUDA")
    h = hashlib.sha1(k.asm["cubin"]).hexdigest()[:12]
    print(json.dumps({"phase": name, "n": len(ts), "us_med": ts[len(ts) // 2], "us_min": ts[0], "cubin": h,
                      "num_warps": getattr(k.metadata, "num_warps", None), "regs": getattr(k, "n_regs", None),
                      "shared": getattr(k.metadata, "shared", None)}))
phase("plain_1")
tbt.enable(policy="tune", log="/root/ab_log.jsonl")
phase("tune_1")
tbt.disable()
phase("plain_2")
tbt.enable(policy="tune", log="/root/ab_log.jsonl")
phase("tune_2")
print("stats", tbt.stats())

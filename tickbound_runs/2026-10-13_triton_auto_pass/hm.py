import json, os, statistics as st, sys
import numpy as np
R = "res"
def L(p):
    p = os.path.join(R, p)
    if not os.path.exists(p): return {}
    return {r["case"]: r for r in map(json.loads, open(p)) if r.get("status") != "start"}
def changed(p):
    p = os.path.join(R, p); s = set()
    if not os.path.exists(p): return s
    for r in map(json.loads, open(p)):
        if r.get("decision") == "applied" or (r.get("pass") == "prefetch" and r.get("changed")): s.add(r["kernel"])
    return s
ENVS = [("tt32", "Triton 3.2"), ("tt35", "Triton 3.5"), ("tt38", "Triton 3.8")]
COLS = []
for e, _ in ENVS:
    COLS += [(e, "noise"), (e, "v1"), (e, "v1+v2")]
data = {}  # (lib, case, kernel) -> {col: ratio}
for e, _ in ENVS:
    for lib in ("cuasmrl", "liger", "flaggems"):
        b, b2 = L(f"r2_{e}_{lib}_base.jsonl"), L(f"r2_{e}_{lib}_base2.jsonl")
        v1, pf = L(f"r2_{e}_{lib}_tb_always.jsonl"), L(f"r3_{e}_{lib}_pf.jsonl")
        ch1 = changed(f"tblog_r2_{e}_{lib}_tb_always.jsonl"); ch2 = changed(f"tblog_r3_{e}_{lib}_pf.jsonl") | ch1
        for c, rb in b.items():
            if rb.get("status") != "ok": continue
            for k, v in rb["kernels"].items():
                if k not in ch1 and k not in ch2: continue
                g = lambda d: d.get(c, {}).get("kernels", {}).get(k, {}).get("us_med") if d.get(c, {}).get("status") == "ok" else None
                d = data.setdefault((lib, c, k), {})
                for col, src, ok in (("noise", b2, True), ("v1", v1, k in ch1), ("v1+v2", pf, k in ch2)):
                    t = g(src)
                    if t and ok: d[(e, col)] = v["us_med"] / t
                    elif t and not ok: d[(e, col)] = None  # not rewritten -> grey
                d[(e, "base_us")] = v["us_med"]
print(len(data), "rows")
json.dump([[list(k), {f"{a}|{b}": x for (a, b), x in d.items()}] for k, d in data.items()], open("hm.json", "w"))

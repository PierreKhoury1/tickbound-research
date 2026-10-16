# compare_tune.py BASE BASE2 TUNE TUNE2 TUNELOG: per Triton kernel (every kernel the tuner saw), time ratio
# base / tune (>1 = faster with tickbound tune), base / base2 = run-to-run noise; tune2 = second process (disk cache).
import json, statistics as st, sys, math
def load(p):
    d = {}
    try:
        for l in open(p):
            r = json.loads(l)
            if r.get("status") != "start":
                d[r["case"]] = r
    except FileNotFoundError:
        pass
    return d
base, base2, tune, tune2 = (load(p) for p in sys.argv[1:5])
names, chosen = set(), {}
for l in open(sys.argv[5]):
    r = json.loads(l)
    if "tune" in r:
        names.add(r["kernel"])
        chosen.setdefault(r["kernel"], []).append((r.get("chosen"), r.get("speedup")))
rows, R, N, R2, W, IDENT = [], [], [], [], [], [0, 0, 0]
for c, b in base.items():
    t, t2, b2 = tune.get(c, {}), tune2.get(c, {}), base2.get(c, {})
    if b.get("status") != "ok" or t.get("status") != "ok":
        rows.append(f"{c:30s} base {b.get('status')} tune {t.get('status')} {t.get('error', '')[:100]}")
        continue
    same = b["out_sha256"] == t["out_sha256"]
    IDENT[0 if same else (1 if b.get("deterministic") else 2)] += 1
    g = lambda d, k: d.get("kernels", {}).get(k, {}).get("us_med") if d.get("status") == "ok" else None
    ks = []
    for k, v in b["kernels"].items():
        if k not in names or not g(t, k):
            continue
        r = v["us_med"] / g(t, k); R.append(r)
        nz = v["us_med"] / g(b2, k) if g(b2, k) else None
        if nz: N.append(nz)
        r2 = v["us_med"] / g(t2, k) if g(t2, k) else None
        if r2: R2.append(r2)
        ks.append(f"{k[:30]} x{r:5.3f} (noise {nz and round(nz, 3)}, cached x{r2 and round(r2, 3)})")
    W.append(b["wall_us_per_step"] / t["wall_us_per_step"])
    rows.append(f"{c:30s} out {'IDENT' if same else ('DIFF' if b.get('deterministic') else 'nondet')}  step x{W[-1]:5.3f}  " + "  ".join(ks))
print("\n".join(rows))
gm = lambda x: math.exp(sum(map(math.log, x)) / len(x)) if x else float("nan")
summ = lambda nm, x: (f"{nm}: n {len(x)}, faster(>1.03) {sum(v > 1.03 for v in x)}, slower(<0.97) {sum(v < 0.97 for v in x)}, "
                      f"median {st.median(x):.3f}, geomean {gm(x):.3f}, min {min(x):.3f}, max {max(x):.3f}") if x else f"{nm}: none"
print()
print(summ("tune kernel ratio", R)); print(summ("tune (cached, 2nd process) kernel ratio", R2)); print(summ("noise base/base2", N))
print(summ("whole-step ratio", W))
print(f"outputs: identical {IDENT[0]}, DIFF {IDENT[1]}, nondeterministic case {IDENT[2]}")
from collections import Counter
print("decisions:", dict(Counter(v for xs in chosen.values() for v, _ in xs)))

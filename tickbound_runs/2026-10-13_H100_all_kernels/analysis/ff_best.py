# Best-of-everything comparison for kernl_fused_ff: per (M,N,K,l2) shape, fastest Triton build (any version, any
# config, any of Triton's own knobs) vs fastest build carrying our reorder. Ratio > 1 = ours faster.
import csv, json, sys, statistics as st
from collections import defaultdict
OURS = {"ro", "ro_clamp", "ro_tt32", "ro_full_tt32"}
TRITON = {"orig", "ctl_s2", "ctl_s5", "kernl", "tt32", "tt38", "ctl_r64"}
rows = list(csv.DictReader(open(sys.argv[1])))
best = defaultdict(lambda: {"ours": (1e18, ""), "triton": (1e18, ""), "tt38": (1e18, ""), "orig": (1e18, "")})
for r in rows:
    p = json.loads(r["params_json"]); v = r["variant"]; t = float(r["mean_us_median"])
    key = (p["M"], p["N"], p["K"], p["l2"]); tag = f'{v}@{p["cfg"]}'
    b = best[key]
    if v in OURS and t < b["ours"][0]: b["ours"] = (t, tag)
    if v in TRITON and t < b["triton"][0]: b["triton"] = (t, tag)
    if v == "tt38" and t < b["tt38"][0]: b["tt38"] = (t, tag)
    if v == "orig" and t < b["orig"][0]: b["orig"] = (t, tag)
win = 0; rs = []; r38 = []; r22 = []
print(f'{"shape":28s} {"best Triton":>11s} {"ours":>9s} ratio  vs3.8  vs2.2  (winner builds)')
for k in sorted(best):
    b = best[k]; r = b["triton"][0] / b["ours"][0]; rs.append(r); win += r > 1
    a38 = b["tt38"][0] / b["ours"][0]; r38.append(a38); a22 = b["orig"][0] / b["ours"][0]; r22.append(a22)
    print(f'M{k[0]} N{k[1]} K{k[2]} {k[3]:5s}'.ljust(28), f'{b["triton"][0]:11.2f} {b["ours"][0]:9.2f} {r:5.3f} {a38:5.3f} {a22:5.3f}  T={b["triton"][1]} O={b["ours"][1]}')
print(f"\nshapes {len(rs)}: ours faster than BEST Triton in {win}; median ratio {st.median(rs):.3f} (min {min(rs):.3f} max {max(rs):.3f})")
print(f"vs best Triton 3.8 only: faster in {sum(x>1 for x in r38)}/{len(r38)}, median {st.median(r38):.3f}")
print(f"vs best Triton 2.2 only: faster in {sum(x>1 for x in r22)}/{len(r22)}, median {st.median(r22):.3f}")

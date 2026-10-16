# Per kernel, per case: time(orig) / time(variant) for every reorder variant, from the 17-column result CSVs.
# Reports the pre-registered primary variant "ro" and the best variant per case (best-of picks favour us: flagged).
import csv, sys, glob, statistics as st
from collections import defaultdict
files = sys.argv[1:]
for f in files:
    rows = [r for r in csv.DictReader(open(f)) if r.get("mean_us_median")]
    if not rows: print(f"{f}: NO ROWS"); continue
    by = defaultdict(dict); beq = defaultdict(int); n = 0
    for r in rows:
        by[r["case_id"]][r["variant"]] = float(r["mean_us_median"])
        if r["variant"] != "orig": n += 1; beq[r["bitwise_equal"].lower()] += 1
    variants = sorted({v for c in by.values() for v in c} - {"orig"})
    k = rows[0]["kernel"]; print(f"\n== {k}  ({len(by)} cases, GPU {rows[0]['gpu']}, non-orig rows bitwise_equal: {dict(beq)})")
    for v in variants:
        rs = [c["orig"] / c[v] for c in by.values() if v in c and "orig" in c]
        if rs: print(f"   {v:14s} faster {sum(x>1 for x in rs):3d}/{len(rs):3d}  median {st.median(rs):.3f}  min {min(rs):.3f}  max {max(rs):.3f}")
    best = [max(c["orig"] / c[v] for v in c if v != "orig") for c in by.values() if "orig" in c and len(c) > 1]
    print(f"   {'best-of-ours':14s} faster {sum(x>1 for x in best):3d}/{len(best):3d}  median {st.median(best):.3f}  min {min(best):.3f}  max {max(best):.3f}")

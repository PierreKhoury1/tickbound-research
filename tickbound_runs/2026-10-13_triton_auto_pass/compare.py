# compare.py BASE.jsonl TB.jsonl TBLOG.jsonl [BASE2.jsonl] - per case: outputs bit-identical?, per rewritten kernel
# time ratio (base / tb, >1 = faster with the pass), whole-step ratio; base vs base2 gives the run-to-run noise.
import json, statistics as st, sys
from collections import defaultdict
def load(p):
    d = {}
    for l in open(p):
        r = json.loads(l)
        if r.get("status") != "start":
            d[r["case"]] = r
    return d
base, tb = load(sys.argv[1]), load(sys.argv[2])
applied = defaultdict(set)
for l in open(sys.argv[3]):
    r = json.loads(l)
    applied[r.get("decision", "unchanged")].add(r.get("kernel"))
base2 = load(sys.argv[4]) if len(sys.argv) > 4 else {}
rows, kr, wr, nz = [], [], [], []
for c, b in base.items():
    t = tb.get(c)
    if not t or b.get("status") != "ok" or t.get("status") != "ok":
        rows.append(f"{c:30s} base {b.get('status')} tb {t.get('status') if t else 'missing'} {(t or {}).get('error', '')[:80]}")
        continue
    same = b["out_sha256"] == t["out_sha256"]
    det = b.get("deterministic")
    ks = []
    for k, v in b["kernels"].items():
        if k in applied["applied"] and k in t["kernels"]:
            r = v["us_med"] / t["kernels"][k]["us_med"]
            ks.append((k, r)); kr.append(r)
    w = b["wall_us_per_step"] / t["wall_us_per_step"]; wr.append(w)
    if c in base2 and base2[c].get("status") == "ok":
        nz.append(b["wall_us_per_step"] / base2[c]["wall_us_per_step"])
    rows.append(f"{c:30s} step x{w:5.3f}  out {'IDENT' if same else ('DIFF' if det else 'nondet')}  "
                + "  ".join(f"{k[:28]} x{r:5.3f}" for k, r in ks))
print("\n".join(rows))
print(f"\nkernels applied {len(applied['applied'])}, rejected_occupancy {len(applied['rejected_occupancy'])}, "
      f"ptxas fallback {len(applied['fallback_ptxas'])}, unchanged {len(applied['unchanged'])}")
if kr: print(f"rewritten-kernel time ratio: n {len(kr)}, faster {sum(x > 1.02 for x in kr)}, slower {sum(x < 0.98 for x in kr)}, median {st.median(kr):.3f}, min {min(kr):.3f}, max {max(kr):.3f}")
if wr: print(f"whole-step ratio: median {st.median(wr):.3f}, min {min(wr):.3f}, max {max(wr):.3f}")
if nz: print(f"noise (base/base2 whole step): median {st.median(nz):.3f}, min {min(nz):.3f}, max {max(nz):.3f}")

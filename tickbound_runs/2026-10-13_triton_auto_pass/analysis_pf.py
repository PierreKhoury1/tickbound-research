import json, glob, os, statistics as st
R = r"C:\Users\pierr\tb-triton\proof\res_P\res"
def L(p):
    if not os.path.exists(p): return {}
    return {json.loads(l)["case"]: json.loads(l) for l in open(p) if '"start"' not in l}
rows = []
for env in ("tt32", "tt35", "tt38"):
    for lib in ("cuasmrl", "liger", "flaggems"):
        tbl = os.path.join(R, f"tblog_r3_{env}_{lib}_pf.jsonl")
        if not os.path.exists(tbl): continue
        pf_k = {json.loads(l)["kernel"] for l in open(tbl) if json.loads(l).get("pass") == "prefetch" and json.loads(l).get("changed")}
        b, b2 = L(os.path.join(R, f"r2_{env}_{lib}_base.jsonl")), L(os.path.join(R, f"r2_{env}_{lib}_base2.jsonl"))
        v1, pf = L(os.path.join(R, f"r2_{env}_{lib}_tb_always.jsonl")), L(os.path.join(R, f"r3_{env}_{lib}_pf.jsonl"))
        for c, rb in b.items():
            if rb.get("status") != "ok": continue
            for k, v in rb["kernels"].items():
                if k not in pf_k: continue
                g = lambda d: d.get(c, {}).get("kernels", {}).get(k, {}).get("us_med")
                t0, tn, t1, tp = v["us_med"], g(b2), g(v1), g(pf)
                if not (tn and t1 and tp): continue
                same = pf.get(c, {}).get("out_sha256") == rb.get("out_sha256")
                rows.append((env, lib, c, k, t0, t0 / tn, t0 / t1, t0 / tp, same, rb.get("deterministic")))
print(f"{'env':5s} {'case':26s} {'kernel':30s} {'base us':>9s} noise  v1    v1+v2  out")
for r in rows:
    print(f"{r[0]:5s} {r[2][:26]:26s} {r[3][:30]:30s} {r[4]:9.2f} {r[5]:5.3f} {r[6]:5.3f} {r[7]:5.3f}  {'IDENT' if r[8] else ('nondet' if not r[9] else 'DIFF')}")
pfr = [r[7] for r in rows]; nz = [r[5] for r in rows]
print(f"\nprefetched kernel-cases: {len(rows)}; v1+v2 faster(>1.03) {sum(x>1.03 for x in pfr)}, slower(<0.97) {sum(x<0.97 for x in pfr)}, median {st.median(pfr):.3f}; noise median {st.median(nz):.3f} range {min(nz):.3f}-{max(nz):.3f}")

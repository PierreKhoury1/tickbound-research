# compare_builds.py ORIG_RESULTS_DIR AUTO_RESULTS_DIR [OUT.json]
# Every harness writes results/<kernel>_<gpu>_<stamp>.csv with the same columns (kernel, variant, case_id,
# mean_us_median, bitwise_equal, ...). ORIG = harness built with the real ptxas, AUTO = the same harness built with
# tb_ptxas (only the original kernels transformed). Per case: orig_us (ORIG build, variant orig), auto_us (AUTO build,
# variant orig), ratio = orig/auto; hand = best hand variant in the ORIG build; the AUTO build's `bitwise_equal` of
# its hand variants against its (automatic) orig = automatic vs true original byte-equality (the hand variants are
# untouched and were bit-identical to the original in the ORIG build).
import csv, glob, json, os, statistics as st, sys

O, A = sys.argv[1], sys.argv[2]
OUT = sys.argv[3] if len(sys.argv) > 3 else None


def load(d):
    rows = {}
    for f in glob.glob(os.path.join(d, "**", "*.csv"), recursive=True):
        if "_extra" in f or "/quick/" in f.replace("\\", "/"):
            continue
        with open(f, newline="") as fh:
            for r in csv.DictReader(fh):
                if "mean_us_median" not in r:
                    continue
                rows[(r["kernel"], r["variant"], r["case_id"])] = r
    return rows


def f(x):
    try:
        return float(x)
    except Exception:
        return None


o, a = load(O), load(A)
by_kernel = {}
for (k, v, c), r in o.items():
    if v != "orig":
        continue
    ra = a.get((k, "orig", c))
    if not ra:
        continue
    ou, au = f(r["mean_us_median"]), f(ra["mean_us_median"])
    if not ou or not au:
        continue
    hands = [(f(o[(k, vv, cc)]["mean_us_median"]), vv) for (kk, vv, cc) in o if kk == k and cc == c and vv != "orig"
             and f(o[(k, vv, cc)]["mean_us_median"])]
    hand = min(hands) if hands else (None, None)
    eq = [a[(kk, vv, cc)].get("bitwise_equal") for (kk, vv, cc) in a if kk == k and cc == c and vv != "orig"]
    rec = {"case": c, "orig_us": ou, "auto_us": au, "ratio": round(ou / au, 4),
           "hand_best_us": hand[0], "hand_variant": hand[1], "hand_ratio": round(ou / hand[0], 4) if hand[0] else None,
           "auto_equals_hand_outputs": eq}
    by_kernel.setdefault(k, []).append(rec)
summary = {}
for k, recs in by_kernel.items():
    rs = [r["ratio"] for r in recs]
    hs = [r["hand_ratio"] for r in recs if r["hand_ratio"]]
    bad = [r["case"] for r in recs if any(x not in ("1", "true", "True") for x in r["auto_equals_hand_outputs"])]
    summary[k] = {"cases": len(rs), "auto_median": round(st.median(rs), 3), "auto_min": round(min(rs), 3),
                  "auto_max": round(max(rs), 3), "auto_faster": sum(x > 1.03 for x in rs), "auto_slower": sum(x < 0.97 for x in rs),
                  "hand_median": round(st.median(hs), 3) if hs else None, "output_mismatch_cases": bad}
    print(f"{k:24s} n {len(rs):3d}  auto median {st.median(rs):.3f} (min {min(rs):.3f} max {max(rs):.3f}) faster {sum(x > 1.03 for x in rs)} "
          f"slower {sum(x < 0.97 for x in rs)} | hand median {st.median(hs) if hs else float('nan'):.3f} | output mismatches {len(bad)}")
if OUT:
    json.dump({"summary": summary, "cases": by_kernel}, open(OUT, "w"), indent=1)

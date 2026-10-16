# plot_tune.py RESDIR OUTDIR: heatmap of tickbound "tune" per Triton kernel x shape on each Triton version.
# Columns per version: noise (base/base2), tune (first process, decisions made on first launch), cached (second
# process, decisions from disk); cell text = speedup, row label also shows the chosen variant.
import json, os, sys, math, statistics as st
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
R, OUT = sys.argv[1], sys.argv[2]
ENVS = [("tt32", "3.2"), ("tt35", "3.5"), ("tt38", "3.8")]
SUB = ["noise", "tune", "cached"]
def L(p):
    p = os.path.join(R, p)
    if not os.path.exists(p): return {}
    return {r["case"]: r for r in map(json.loads, open(p)) if r.get("status") != "start"}
rows = {}
for e, _ in ENVS:
    for lib in ("cuasmrl", "liger", "flaggems"):
        tl = os.path.join(R, f"tblog_{e}_{lib}_tune.jsonl")
        if not os.path.exists(tl): continue
        dec = {}
        for r in map(json.loads, open(tl)):
            if "tune" in r: dec.setdefault(r["kernel"], set()).add(r["chosen"])
        b, b2, t = (L(f"{e}_{lib}_{x}.jsonl") for x in ("base", "base2", "tune")); t2 = L(f"s4_{e}_{lib}_tune4.jsonl")
        for c, rb in b.items():
            if rb.get("status") != "ok": continue
            for k, v in rb["kernels"].items():
                if k not in dec: continue
                g = lambda d: d.get(c, {}).get("kernels", {}).get(k, {}).get("us_med") if d.get(c, {}).get("status") == "ok" else None
                d = rows.setdefault((lib, c, k), {})
                for col, src in (("noise", b2), ("tune", t), ("cached", t2)):
                    if g(src): d[(e, col)] = v["us_med"] / g(src)
                d[(e, "chosen")] = "/".join(sorted(dec[k]))
                d[(e, "same")] = t.get(c, {}).get("out_sha256") == rb.get("out_sha256")
COLS = [(e, s) for e, _ in ENVS for s in SUB]
def cell(d, e, s):
    nz = d.get((e, "noise"))
    if s != "noise" and nz is not None and abs(nz - 1) > 0.08: return "bad"
    return d.get((e, s))
def score(d):
    v = [x for e, _ in ENVS for x in [cell(d, e, "cached")] if isinstance(x, float)]
    return max(v, key=lambda x: abs(x - 1)) if v else 1.0
items = sorted(rows.items(), key=lambda kv: -score(kv[1]))
def short(k): k = k.replace("void ", ""); return k if len(k) <= 30 else k[:29] + "…"
def plot(sel, fn, title, annot):
    M = np.full((len(sel), len(COLS)), np.nan); B = np.zeros_like(M, bool)
    for i, (_, d) in enumerate(sel):
        for j, (e, s) in enumerate(COLS):
            x = cell(d, e, s)
            if x == "bad": B[i, j] = True
            elif isinstance(x, float): M[i, j] = x
    fig, ax = plt.subplots(figsize=(15, max(4, 0.24 * len(sel) + 2.4)))
    cm = plt.get_cmap("RdYlGn").copy(); cm.set_bad("white")
    im = ax.imshow(np.clip(M, 0.6, 1.5), cmap=cm, norm=TwoSlopeNorm(vmin=0.6, vcenter=1.0, vmax=1.5), aspect="auto", interpolation="nearest")
    for i, j in zip(*np.where(B)):
        ax.add_patch(plt.Rectangle((j - .5, i - .5), 1, 1, facecolor="#e0e0e0", hatch="///", edgecolor="#aaa", lw=0))
    if annot:
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if not np.isnan(M[i, j]):
                    ax.text(j, i, f"{M[i,j]:.2f}", ha="center", va="center", fontsize=7, color="black" if 0.75 < M[i, j] < 1.3 else "white")
    ax.xaxis.tick_top(); ax.set_xticks(range(len(COLS))); ax.set_xticklabels([s for e, s in COLS], fontsize=8)
    for k, (e, lab) in enumerate(ENVS):
        ax.annotate(f"Triton {lab}", xy=(3 * k + 1, 1), xycoords=("data", "axes fraction"), xytext=(0, 22), textcoords="offset points", ha="center", fontsize=10, weight="bold")
        if k: ax.axvline(3 * k - .5, color="black", lw=1.8)
    lab = []
    for (l, c, k), d in sel:
        ch = sorted({d.get((e, "chosen")) for e, _ in ENVS} - {None})
        lab.append(f"{l} · {c} · {short(k)}  [{','.join(ch)[:28]}]")
    ax.set_yticks(range(len(sel))); ax.set_yticklabels(lab, fontsize=7)
    fig.colorbar(im, ax=ax, fraction=0.03, pad=0.01).set_label("speedup vs original Triton (>1 = faster)")
    ax.set_title(title, fontsize=11, pad=44)
    fig.text(0.01, 0.004, "noise = original vs original rerun. tune = tickbound policy 'tune' (first process: measures on first launch). cached = new process with fixed fast path "
             "using saved decisions. [..] = variant chosen. hatched = baseline unreliable (>8% rerun spread). per-kernel median (torch.profiler).", fontsize=7, color="#444")
    fig.tight_layout(rect=(0, 0.02, 1, 1)); fig.savefig(os.path.join(OUT, fn), dpi=150); plt.close(fig)
plot(items, "heatmap_tune_all.png", f"tickbound.triton tune — all {len(items)} Triton kernel×shape cases", False)
mv = [r for r in items if any(isinstance(cell(r[1], e, s), float) and abs(cell(r[1], e, s) - 1) > 0.05 for e, _ in ENVS for s in ("tune", "cached"))]
plot(mv, "heatmap_tune_movers.png", f"tune: cases moved >5% ({len(mv)} of {len(items)})", True)
gm = lambda x: math.exp(sum(map(math.log, x)) / len(x)) if x else float("nan")
for s in ("noise", "tune", "cached"):
    v = [cell(d, e, s) for _, d in items for e, _ in ENVS]
    v = [x for x in v if isinstance(x, float)]
    if v: print(f"{s:7s} n {len(v)} median {st.median(v):.3f} geomean {gm(v):.3f} >1.05 {sum(x>1.05 for x in v)} <0.95 {sum(x<0.95 for x in v)} min {min(v):.3f} max {max(v):.3f}")
same = [d.get((e, "same")) for _, d in items for e, _ in ENVS if (e, "same") in d]
print("rows", len(items), "outputs identical (per kernel-env, case-level):", sum(1 for x in same if x), "/", len(same))

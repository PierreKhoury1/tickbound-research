import json, numpy as np, statistics as st, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
rows = json.load(open("hm.json"))
ENVS = [("tt32", "3.2"), ("tt35", "3.5"), ("tt38", "3.8")]
SUB = ["noise", "v1", "v1+v2", "pick"]
COLS = [(e, s) for e, _ in ENVS for s in SUB]
def short(k):
    k = k.replace("void ", ""); return k if len(k) <= 34 else k[:33] + "…"
def cells(d):
    out = {}
    for e, _ in ENVS:
        nz = d.get(f"{e}|noise")
        bad = isinstance(nz, float) and abs(nz - 1) > 0.08
        for s in ("noise", "v1", "v1+v2"):
            x = d.get(f"{e}|{s}", "missing")
            out[(e, s)] = "bad" if (bad and s != "noise" and isinstance(x, float)) else x
        vs = [out[(e, s)] for s in ("v1", "v1+v2") if isinstance(out[(e, s)], float)]
        out[(e, "pick")] = max([1.0] + vs) if vs else ("bad" if bad else "missing")
    return out
C = [(k, cells(d)) for k, d in rows]
def score(c):
    v = [x for (e, s), x in c.items() if s in ("v1", "v1+v2") and isinstance(x, float)]
    if not v: return 0
    return max(v) if max(v) - 1 > 1 - min(v) else min(v)
C.sort(key=lambda r: -score(r[1]))
def plot(sel, fn, title, annot):
    M = np.full((len(sel), len(COLS)), np.nan); B = np.zeros_like(M, bool)
    for i, (_, c) in enumerate(sel):
        for j, col in enumerate(COLS):
            x = c[col]
            if x == "bad": B[i, j] = True
            elif isinstance(x, float): M[i, j] = x
    fig, ax = plt.subplots(figsize=(14, max(4, 0.24 * len(sel) + 2.2)))
    cm = plt.get_cmap("RdYlGn").copy(); cm.set_bad("white")
    im = ax.imshow(np.clip(M, 0.6, 1.5), cmap=cm, norm=TwoSlopeNorm(vmin=0.6, vcenter=1.0, vmax=1.5), aspect="auto", interpolation="nearest")
    for i, j in zip(*np.where(B)):
        ax.add_patch(plt.Rectangle((j - .5, i - .5), 1, 1, facecolor="#e0e0e0", hatch="///", edgecolor="#aaa", lw=0))
    if annot:
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if not np.isnan(M[i, j]):
                    ax.text(j, i, f"{M[i,j]:.2f}", ha="center", va="center", fontsize=7,
                            weight="bold" if COLS[j][1] == "pick" else None,
                            color="black" if 0.75 < M[i, j] < 1.3 else "white")
    ax.xaxis.tick_top(); ax.set_xticks(range(len(COLS))); ax.set_xticklabels([s for e, s in COLS], fontsize=8)
    for k, (e, lab) in enumerate(ENVS):
        ax.annotate(f"Triton {lab}", xy=(4 * k + 1.5, 1), xycoords=("data", "axes fraction"), xytext=(0, 22),
                    textcoords="offset points", ha="center", fontsize=10, weight="bold")
        if k: ax.axvline(4 * k - .5, color="black", lw=1.8)
        ax.axvline(4 * k + 2.5, color="black", lw=0.6, ls=":")
    ax.set_yticks(range(len(sel))); ax.set_yticklabels([f"{l} · {c} · {short(k)}" for (l, c, k), _ in sel], fontsize=7)
    fig.colorbar(im, ax=ax, fraction=0.03, pad=0.01).set_label("speedup vs original Triton (>1 = faster)")
    ax.set_title(title, fontsize=11, pad=44)
    fig.text(0.01, 0.004, "noise = original vs original rerun. v1 = read-only .nc loads. v1+v2 = + loop prefetch. pick = keep fastest of original/v1/v1+v2 "
             "(measure-then-pick, never <1). hatched = baseline unreliable (rerun spread >8%), white = not run. H100, per-kernel median, outputs bit-identical.",
             fontsize=7, color="#444", wrap=True)
    fig.tight_layout(rect=(0, 0.02, 1, 1)); fig.savefig(fn, dpi=150); plt.close(fig)
plot(C, "heatmap_all.png", f"tickbound.triton automatic pass — all {len(C)} rewritten kernel×shape cases (H100)", False)
mv = [r for r in C if any(isinstance(x, float) and abs(x - 1) > 0.05 for (e, s), x in r[1].items() if s in ("v1", "v1+v2"))]
plot(mv, "heatmap_movers.png", f"Cases where the pass moved kernel time >5% ({len(mv)} of {len(C)}; noisy baselines hatched)", True)
for s in ("v1", "v1+v2", "pick"):
    v = [c[(e, s)] for _, c in C for e, _ in ENVS if isinstance(c[(e, s)], float)]
    print(f"{s:6s} n {len(v)} median {st.median(v):.3f} geomean {np.exp(np.mean(np.log(v))):.3f} >1.05 {sum(x>1.05 for x in v)} <0.95 {sum(x<0.95 for x in v)}")

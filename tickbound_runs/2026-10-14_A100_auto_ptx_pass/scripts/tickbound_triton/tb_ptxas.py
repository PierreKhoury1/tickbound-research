#!/usr/bin/env python3
"""tickbound ptxas wrapper: the unroll-and-batch load reorder (ptx_unroll) applied to every PTX that goes through
ptxas, then the real ptxas. Drop-in for any build: nvcc calls ptxas from its own bin directory, Triton from
TRITON_PTXAS_PATH, so

    mv /usr/local/cuda/bin/ptxas /usr/local/cuda/bin/ptxas.real
    install -m 755 tb_ptxas.py /usr/local/cuda/bin/ptxas          # TB_REAL_PTXAS defaults to <this dir>/ptxas.real

makes every kernel compiled on the machine go through the pass, with no source change. Environment:
  TB_PTX_K         unroll factor (default 4; 1 = hoist loads above stores only)
  TB_PTX_KERNELS   comma-separated substrings; only entries whose name contains one are transformed (default all)
  TB_PTX_LOG       append one JSON line per PTX file (what was transformed and why not)
  TB_PTX_OFF=1     pass-through (no transform)
  TB_REAL_PTXAS    the real ptxas (default: ptxas.real next to this script, else `ptxas` on PATH other than self)
A PTX the pass cannot handle, or that the real ptxas rejects after the transform, is assembled unchanged (logged)."""
import json
import os
import subprocess
import sys
import tempfile
import time


def real_ptxas():
    env = os.environ.get("TB_REAL_PTXAS")
    if env:
        return env
    here = os.path.dirname(os.path.abspath(__file__))
    cand = os.path.join(here, "ptxas.real")
    if os.path.exists(cand):
        return cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        p = os.path.join(d, "ptxas")
        if os.path.exists(p) and os.path.abspath(p) != os.path.abspath(__file__):
            return p
    raise SystemExit("tb_ptxas: no real ptxas found (set TB_REAL_PTXAS)")


def log(rec):
    p = os.environ.get("TB_PTX_LOG")
    if p:
        with open(p, "a") as f:
            f.write(json.dumps(rec) + "\n")


def main():
    args = sys.argv[1:]
    rp = real_ptxas()
    if os.environ.get("TB_PTX_OFF") == "1":
        os.execv(rp, [rp] + args)
    inputs = [i for i, a in enumerate(args) if a.endswith(".ptx") and os.path.exists(a)]
    if len(inputs) != 1:
        log({"ptx": None, "note": f"{len(inputs)} ptx inputs, pass-through", "args": args[:6]})
        os.execv(rp, [rp] + args)
    i = inputs[0]
    src = args[i]
    rec = {"ptx": src, "k": int(os.environ.get("TB_PTX_K", "8")), "loads": int(os.environ.get("TB_PTX_LOADS", "16"))}
    try:
        src_dir = os.environ.get("TB_SRC") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, src_dir)   # TB_SRC = the tickbound `src` directory when this file is installed elsewhere
        from tickbound.triton.ptx_unroll import unroll_batch
        kernels = [k for k in os.environ.get("TB_PTX_KERNELS", "").split(",") if k]
        t0 = time.time()
        text = open(src, encoding="utf-8", errors="replace").read()
        new, reps = unroll_batch(text, rec["k"], kernels or None, max_loads=rec["loads"])
        rec["pass_s"] = round(time.time() - t0, 2)
        rec["kernels"] = [{"name": r.kernel[:120], "transformed": r.transformed, "notes": r.loops[:40]} for r in reps]
        rec["loops_transformed"] = sum(r.transformed for r in reps)
    except Exception as e:
        rec["error"] = repr(e)[:300]
        log(rec)
        os.execv(rp, [rp] + args)
    if rec["loops_transformed"] == 0:
        rec["note"] = "nothing transformed"
        log(rec)
        os.execv(rp, [rp] + args)
    fd, tmp = tempfile.mkstemp(suffix=".tb.ptx", dir=os.path.dirname(os.path.abspath(src)) or None)
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
    new_args = list(args)
    new_args[i] = tmp
    r = subprocess.run([rp] + new_args, capture_output=True, text=True)
    if r.returncode == 0:
        rec["result"] = "transformed"
        log(rec)
        try:
            os.remove(tmp)
        except OSError:
            pass
        sys.stdout.write(r.stdout)
        sys.stderr.write(r.stderr)
        sys.exit(0)
    rec["result"] = "ptxas rejected the transformed PTX, original assembled"
    rec["ptxas_error"] = (r.stderr or r.stdout)[-600:]
    log(rec)
    os.execv(rp, [rp] + args)


if __name__ == "__main__":
    main()

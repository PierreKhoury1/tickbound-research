#!/usr/bin/env bash
# rerun.sh: second pass on the same box with CPU-generated inputs + cheap launch guard + Kernl port; reuses venvs.
set -u
LOG=/root/res/rerun.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
export UV_CACHE_DIR=/root/uvcache PYTHONPATH=/root/b/tbsrc
uv pip install -q -p /root/v_tt32/bin/python setuptools >> $LOG 2>&1
for name in tt32 tt35 tt38; do
  V=/root/v_$name
  log "$name env: $($V/bin/python -c 'import torch,triton;print(torch.__version__,triton.__version__)' 2>&1 | tail -1)"
  for lib in cuasmrl liger flaggems; do
    [ $name = tt38 ] && [ $lib = flaggems ] && continue   # flag-gems 5.0.2 does not compile on Triton 3.8
    for run in base tb_always base2 tb_occ; do
      t0=$(date +%s); tag=r2_${name}_${lib}_$run
      extra=(); case $run in tb_always) extra=(--tb always --tblog /root/res/tblog_$tag.jsonl);; tb_occ) extra=(--tb occupancy --tblog /root/res/tblog_$tag.jsonl);; esac
      dumpenv=(); [ $run = base ] && dumpenv=(TRITON_KERNEL_DUMP=1 TRITON_DUMP_DIR=/root/res/dump_r2_${name}_$lib)
      env "${dumpenv[@]}" TRITON_CACHE_DIR=/root/cache_$tag bash /root/b/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl "${extra[@]}" > /root/res/log_$tag.txt 2>&1
      log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err $(grep -c crashed /root/res/$tag.jsonl) crash ($(( $(date +%s)-t0 )) s)"
    done
    p=/root/res/r2_${name}_${lib}
    $V/bin/python /root/b/compare.py ${p}_base.jsonl ${p}_tb_always.jsonl /root/res/tblog_r2_${name}_${lib}_tb_always.jsonl ${p}_base2.jsonl > /root/res/cmp_r2_${name}_${lib}_always.txt 2>&1
    $V/bin/python /root/b/compare.py ${p}_base.jsonl ${p}_tb_occ.jsonl /root/res/tblog_r2_${name}_${lib}_tb_occ.jsonl ${p}_base2.jsonl > /root/res/cmp_r2_${name}_${lib}_occ.txt 2>&1
    log "$name $lib always: $(grep -E 'rewritten-kernel' /root/res/cmp_r2_${name}_${lib}_always.txt)"
  done
done
log "RERUN END"; cd /root && tar -czf /root/res.tgz res

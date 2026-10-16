#!/usr/bin/env bash
# pf.sh: after rerun.sh, run every lib with tickbound.triton pass v1+v2 (loop prefetch); baselines = r2 base/base2.
set -u
LOG=/root/res/pf.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
while ! grep -q "RERUN END" /root/res/rerun.log 2>/dev/null; do sleep 10; done
export PYTHONPATH=/root/b/tbsrc
for name in tt32 tt35 tt38; do
  V=/root/v_$name
  for lib in cuasmrl liger flaggems; do
    [ $name = tt38 ] && [ $lib = flaggems ] && continue
    t0=$(date +%s); tag=r3_${name}_${lib}_pf
    TRITON_CACHE_DIR=/root/cache_$tag bash /root/b/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl --tb pf --tblog /root/res/tblog_$tag.jsonl > /root/res/log_$tag.txt 2>&1
    p=/root/res/r2_${name}_${lib}
    $V/bin/python /root/b/compare.py ${p}_base.jsonl /root/res/$tag.jsonl /root/res/tblog_$tag.jsonl ${p}_base2.jsonl > /root/res/cmp_r3_${name}_${lib}_pf.txt 2>&1
    log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err ($(( $(date +%s)-t0 )) s) | prefetched $(grep -c '"changed": true' /root/res/tblog_$tag.jsonl) | $(grep -E 'rewritten-kernel' /root/res/cmp_r3_${name}_${lib}_pf.txt)"
  done
done
log "PF END"; cd /root && tar -czf /root/res.tgz res

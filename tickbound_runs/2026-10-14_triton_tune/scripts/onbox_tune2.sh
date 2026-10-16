#!/usr/bin/env bash
# onbox_tune2.sh: second stage with fixed tune code in /root/b3 (autotuner benchmarks not tuned, wrapper pointer args,
# budget per kernel, exact-signature fast path). Runs what the first stage missed (tt35 flaggems, all of tt32), then
# followup.sh (overhead + cached-decision rerun of every lib). Writes /root/res.tgz + /root/DONE3.
set -u
LOG=/root/res/onbox.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
export UV_CACHE_DIR=/root/uvcache PYTHONPATH=/root/b3/tbsrc
log "stage2 start (b3 code)"
rm -f /root/res/tt35_flaggems_tune.jsonl /root/res/tblog_tt35_flaggems_tune.jsonl /root/res/tunecache_tt35_flaggems.json
mv /root/res/log_tt35_flaggems_tune.txt /root/res/log_tt35_flaggems_tune_hung_stage1.txt 2>/dev/null
run_lib() {  # name lib runs...
  local name=$1 lib=$2; shift 2; local V=/root/v_$name
  for run in "$@"; do
    t0=$(date +%s); tag=${name}_${lib}_$run
    extra=(); case $run in tune|tune2) extra=(--tb tune --tblog /root/res/tblog_$tag.jsonl);; esac
    TICKBOUND_TUNE_CACHE=/root/res/tunecache_${name}_$lib.json TRITON_CACHE_DIR=/root/cache_$tag \
      bash /root/b3/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl "${extra[@]}" > /root/res/log_$tag.txt 2>&1
    log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err $(grep -c crashed /root/res/$tag.jsonl) crash ($(( $(date +%s)-t0 )) s)"
  done
  p=/root/res/${name}_${lib}
  $V/bin/python /root/b3/compare_tune.py ${p}_base.jsonl ${p}_base2.jsonl ${p}_tune.jsonl ${p}_tune2.jsonl /root/res/tblog_${name}_${lib}_tune.jsonl > /root/res/cmp_${name}_${lib}.txt 2>&1
  log "$name $lib: $(grep -E '^tune kernel ratio|^outputs|^decisions' /root/res/cmp_${name}_${lib}.txt | tr '\n' ' ' | cut -c1-500)"
}
run_lib tt35 flaggems tune base2 tune2
for ph in 1 2; do
  TRITON_CACHE_DIR=/root/cache_t_tt32 /root/v_tt32/bin/python /root/b3/t_tune.py /root/res/tunelog_t_tt32_$ph.jsonl /root/res/tunecache_t_tt32.json $ph > /root/res/t_tune_tt32_$ph.txt 2>&1
  log "tt32 t_tune phase $ph: $(grep -E '^RESULT|stats' /root/res/t_tune_tt32_$ph.txt | tr '\n' ' ' | cut -c1-400)"
done
for lib in cuasmrl liger flaggems; do run_lib tt32 $lib base tune base2 tune2; done
log "stage2 END"
bash /root/b3/followup.sh > /root/followup.out 2>&1
cd /root && tar -czf /root/res.tgz res && touch /root/DONE3

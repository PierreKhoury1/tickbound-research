#!/usr/bin/env bash
# followup.sh: after onbox_tune.sh. New tbsrc (exact-signature fast path) in /root/b3. Per env: CPU overhead per launch
# (plain / occupancy / tune), correctness test again, and each lib re-run with the decisions saved by the first run
# (tune3 = cached decisions + fast path) to measure whole-step cost. Results in /root/res/fu_*.
set -u
export PYTHONPATH=/root/b3/tbsrc
LOG=/root/res/followup.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
for name in tt38 tt35 tt32; do
  V=/root/v_$name
  for m in plain occupancy tune plain tune; do
    TRITON_CACHE_DIR=/root/cache_ov_$name TICKBOUND_TUNE_CACHE=/root/res/fu_ovcache_$name.json $V/bin/python /root/b3/t_overhead.py $m >> /root/res/fu_overhead_$name.txt 2>&1
  done
  log "$name overhead: $(tail -5 /root/res/fu_overhead_$name.txt | tr '\n' ' ')"
  for ph in 1 2; do
    TRITON_CACHE_DIR=/root/cache_fu_$name $V/bin/python /root/b3/t_tune.py /root/res/fu_tunelog_t_${name}_$ph.jsonl /root/res/fu_tunecache_t_$name.json $ph > /root/res/fu_t_tune_${name}_$ph.txt 2>&1
    log "$name t_tune phase $ph: $(grep -E '^RESULT' /root/res/fu_t_tune_${name}_$ph.txt)"
  done
  for lib in cuasmrl liger flaggems; do
    [ $name = tt38 ] && [ $lib = flaggems ] && continue
    tag=${name}_${lib}_tune3
    TICKBOUND_TUNE_CACHE=/root/res/tunecache_${name}_$lib.json TRITON_CACHE_DIR=/root/cache_${name}_${lib}_tune \
      bash /root/b3/run_suite.sh $V/bin/python $lib /root/res/fu_$tag.jsonl --tb tune --tblog /root/res/fu_tblog_$tag.jsonl > /root/res/fu_log_$tag.txt 2>&1
    p=/root/res/${name}_${lib}
    $V/bin/python /root/b3/compare_tune.py ${p}_base.jsonl ${p}_base2.jsonl /root/res/fu_$tag.jsonl ${p}_tune2.jsonl /root/res/tblog_${name}_${lib}_tune.jsonl > /root/res/fu_cmp_${name}_${lib}.txt 2>&1
    log "$name $lib tune3: $(grep -E '^tune kernel ratio|^whole-step|^outputs' /root/res/fu_cmp_${name}_${lib}.txt | tr '\n' ' ' | cut -c1-500)"
  done
done
log "FOLLOWUP END"

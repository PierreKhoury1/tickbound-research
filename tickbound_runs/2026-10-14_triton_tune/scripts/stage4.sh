#!/usr/bin/env bash
# stage4.sh: after stage3 (DONE4): fixed fast path (per-call kwargs). Correctness test + cached-decision rerun (tune4)
# of every lib on tt38 / tt35 / tt32. Writes /root/res.tgz + /root/DONE5.
set -u
while [ ! -f /root/DONE4 ]; do sleep 15; done
LOG=/root/res/onbox.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
export PYTHONPATH=/root/b3/tbsrc
for name in tt38 tt35 tt32; do
  V=/root/v_$name
  for ph in 1 2; do
    TRITON_CACHE_DIR=/root/cache_s4_$name $V/bin/python /root/b3/t_tune.py /root/res/s4_tunelog_t_${name}_$ph.jsonl /root/res/s4_tunecache_t_$name.json $ph > /root/res/s4_t_tune_${name}_$ph.txt 2>&1
    log "$name s4 t_tune phase $ph: $(grep -E '^RESULT' /root/res/s4_t_tune_${name}_$ph.txt)"
  done
  for lib in cuasmrl liger flaggems; do
    [ $name = tt38 ] && [ $lib = flaggems ] && continue
    tag=${name}_${lib}_tune4
    TICKBOUND_TUNE_CACHE=/root/res/tunecache_${name}_$lib.json TRITON_CACHE_DIR=/root/cache_${name}_${lib}_tune \
      bash /root/b3/run_suite.sh $V/bin/python $lib /root/res/s4_$tag.jsonl --tb tune --tblog /root/res/s4_tblog_$tag.jsonl > /root/res/s4_log_$tag.txt 2>&1
    p=/root/res/${name}_${lib}
    $V/bin/python /root/b3/compare_tune.py ${p}_base.jsonl ${p}_base2.jsonl /root/res/s4_$tag.jsonl ${p}_tune2.jsonl /root/res/tblog_${name}_${lib}_tune.jsonl > /root/res/s4_cmp_${name}_${lib}.txt 2>&1
    log "$name $lib tune4: $(grep -E '^tune kernel ratio|^whole-step|^outputs' /root/res/s4_cmp_${name}_${lib}.txt | tr '\n' ' ' | cut -c1-500)"
  done
done
log "STAGE4 END"
cd /root && tar -czf /root/res.tgz res && touch /root/DONE5

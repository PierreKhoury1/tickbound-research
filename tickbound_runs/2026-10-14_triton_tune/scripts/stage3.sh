#!/usr/bin/env bash
# stage3.sh: Triton 3.2 env (missed by stage 1), then correctness test, all libs (base/tune/base2/tune2), overhead,
# and the cached-decision rerun (tune3) for tt32. Starts after /root/DONE3. Writes /root/res.tgz + /root/DONE4.
set -u
while [ ! -f /root/DONE3 ]; do sleep 15; done
LOG=/root/res/onbox.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
export UV_CACHE_DIR=/root/uvcache PYTHONPATH=/root/b3/tbsrc
name=tt32; V=/root/v_tt32; t0=$(date +%s)
uv venv -q -p 3.11 $V >> "$LOG" 2>&1
uv pip install -q -p $V/bin/python "torch==2.6.0" --index-url https://download.pytorch.org/whl/cu124 --extra-index-url https://pypi.org/simple >> /root/res/pip_tt32.log 2>&1
uv pip install -q -p $V/bin/python "triton==3.2.0" numpy pyyaml sqlalchemy packaging setuptools >> /root/res/pip_tt32.log 2>&1
uv pip install -q -p $V/bin/python --no-deps liger-kernel flag-gems >> /root/res/pip_tt32.log 2>&1
log "tt32 env: $($V/bin/python -c 'import torch,triton;print(torch.__version__,triton.__version__,torch.cuda.is_available())' 2>&1 | tail -1) ($(( $(date +%s)-t0 )) s)"
for ph in 1 2; do
  TRITON_CACHE_DIR=/root/cache_t_tt32 $V/bin/python /root/b3/t_tune.py /root/res/tunelog_t_tt32_$ph.jsonl /root/res/tunecache_t_tt32.json $ph > /root/res/t_tune_tt32_$ph.txt 2>&1
  log "tt32 t_tune phase $ph: $(grep -E '^RESULT|stats' /root/res/t_tune_tt32_$ph.txt | tr '\n' ' ' | cut -c1-400)"
done
for lib in cuasmrl liger flaggems; do
  for run in base tune base2 tune2; do
    t0=$(date +%s); tag=tt32_${lib}_$run
    extra=(); case $run in tune|tune2) extra=(--tb tune --tblog /root/res/tblog_$tag.jsonl);; esac
    TICKBOUND_TUNE_CACHE=/root/res/tunecache_tt32_$lib.json TRITON_CACHE_DIR=/root/cache_$tag \
      bash /root/b3/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl "${extra[@]}" > /root/res/log_$tag.txt 2>&1
    log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err $(grep -c crashed /root/res/$tag.jsonl) crash ($(( $(date +%s)-t0 )) s)"
  done
  p=/root/res/tt32_${lib}
  $V/bin/python /root/b3/compare_tune.py ${p}_base.jsonl ${p}_base2.jsonl ${p}_tune.jsonl ${p}_tune2.jsonl /root/res/tblog_tt32_${lib}_tune.jsonl > /root/res/cmp_tt32_${lib}.txt 2>&1
  log "tt32 $lib: $(grep -E '^tune kernel ratio|^outputs|^decisions|^whole' /root/res/cmp_tt32_${lib}.txt | tr '\n' ' ' | cut -c1-600)"
done
rm -f /root/res/fu_overhead_tt32.txt
for m in plain occupancy tune plain tune; do
  TRITON_CACHE_DIR=/root/cache_ov_tt32 TICKBOUND_TUNE_CACHE=/root/res/fu_ovcache_tt32.json $V/bin/python /root/b3/t_overhead.py $m >> /root/res/fu_overhead_tt32.txt 2>&1
done
log "tt32 overhead: $(tail -5 /root/res/fu_overhead_tt32.txt | tr '\n' ' ')"
log "STAGE3 END"
cd /root && tar -czf /root/res.tgz res && touch /root/DONE4

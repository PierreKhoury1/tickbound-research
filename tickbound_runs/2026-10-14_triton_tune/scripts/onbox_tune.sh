#!/usr/bin/env bash
# onbox_tune.sh (13 Oct 2026): tickbound.triton policy "tune" (measured selection) on Triton 3.2 / 3.5 / 3.8.
# Per env: correctness test (t_tune.py, two processes: tune, then disk-cache hit); per lib: base, tune, base2, tune2
# (tune2 = new process reusing the tune decision cache). Writes /root/res.tgz + /root/DONE. No secrets read.
set -u
mkdir -p /root/res; LOG=/root/res/onbox.log
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
finish() { log "finish"; cd /root && tar -czf /root/res.tgz res; touch /root/DONE; }
trap finish EXIT
log "start"; nvidia-smi -L | tee -a "$LOG"
(apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3 python3-pip python3-venv >/dev/null) >> "$LOG" 2>&1
pip3 install -q uv >> "$LOG" 2>&1
mkdir -p /root/b && tar -xzf /root/tickbound.tgz -C /root/b
export UV_CACHE_DIR=/root/uvcache PYTHONPATH=/root/b/tbsrc
ENVS="${ENVS:-tt38:torch==2.14.1:https://download.pytorch.org/whl/cu128:triton==3.8.0
tt35:torch==2.9.1:https://download.pytorch.org/whl/cu128:triton==3.5.1
tt32:torch==2.6.0:https://download.pytorch.org/whl/cu124:triton==3.2.0}"
echo "$ENVS" | while IFS=: read -r name tspec idx1 idx2 tri; do
  idx="$idx1:$idx2"; V=/root/v_$name; t0=$(date +%s)
  uv venv -q -p 3.11 $V >> "$LOG" 2>&1
  uv pip install -q -p $V/bin/python "$tspec" --index-url "$idx" --extra-index-url https://pypi.org/simple >> /root/res/pip_$name.log 2>&1 \
    || uv pip install -q -p $V/bin/python "$tspec" >> /root/res/pip_$name.log 2>&1
  uv pip install -q -p $V/bin/python "$tri" numpy pyyaml sqlalchemy packaging setuptools >> /root/res/pip_$name.log 2>&1
  uv pip install -q -p $V/bin/python --no-deps liger-kernel flag-gems >> /root/res/pip_$name.log 2>&1
  log "$name env: $($V/bin/python -c 'import torch,triton;print(torch.__version__,triton.__version__,torch.cuda.is_available())' 2>&1 | tail -1) ($(( $(date +%s)-t0 )) s)"
  for ph in 1 2; do
    TRITON_CACHE_DIR=/root/cache_t_$name $V/bin/python /root/b/t_tune.py /root/res/tunelog_t_${name}_$ph.jsonl /root/res/tunecache_t_$name.json $ph > /root/res/t_tune_${name}_$ph.txt 2>&1
    log "$name t_tune phase $ph: $(grep -E '^RESULT|stats' /root/res/t_tune_${name}_$ph.txt | tr '\n' ' ' | cut -c1-400)"
  done
  for lib in cuasmrl liger flaggems; do
    [ $name = tt38 ] && [ $lib = flaggems ] && continue   # flag-gems 5.0.2 does not compile on Triton 3.8
    for run in base tune base2 tune2; do
      t0=$(date +%s); tag=${name}_${lib}_$run
      extra=(); case $run in tune|tune2) extra=(--tb tune --tblog /root/res/tblog_$tag.jsonl);; esac
      TICKBOUND_TUNE_CACHE=/root/res/tunecache_${name}_$lib.json TRITON_CACHE_DIR=/root/cache_$tag \
        bash /root/b/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl "${extra[@]}" > /root/res/log_$tag.txt 2>&1
      log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err $(grep -c crashed /root/res/$tag.jsonl) crash ($(( $(date +%s)-t0 )) s)"
    done
    p=/root/res/${name}_${lib}
    $V/bin/python /root/b/compare_tune.py ${p}_base.jsonl ${p}_base2.jsonl ${p}_tune.jsonl ${p}_tune2.jsonl /root/res/tblog_${name}_${lib}_tune.jsonl > /root/res/cmp_${name}_${lib}.txt 2>&1
    log "$name $lib: $(grep -E '^tune kernel ratio|^outputs|^decisions' /root/res/cmp_${name}_${lib}.txt | tr '\n' ' ' | cut -c1-500)"
  done
done
log "end"

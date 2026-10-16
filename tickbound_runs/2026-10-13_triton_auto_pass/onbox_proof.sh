#!/usr/bin/env bash
# onbox_proof.sh (13 Oct 2026): does tickbound.triton (automatic pass, no hand edits) speed up real Triton kernels?
# Per env (torch+triton pair) and lib (cuasmrl, liger, flaggems): base run, pass run (policy always), base2 (noise),
# pass run (policy occupancy). Same box, same process layout. Writes /root/res.tgz + /root/DONE. No secrets read.
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
LIBS="${LIBS:-cuasmrl liger flaggems}"
echo "$ENVS" | while IFS=: read -r name tspec idx1 idx2 tri; do
  idx="$idx1:$idx2"; V=/root/v_$name; t0=$(date +%s)
  uv venv -q -p 3.11 $V >> "$LOG" 2>&1
  uv pip install -q -p $V/bin/python "$tspec" --index-url "$idx" --extra-index-url https://pypi.org/simple >> /root/res/pip_$name.log 2>&1 \
    || uv pip install -q -p $V/bin/python "$tspec" >> /root/res/pip_$name.log 2>&1
  uv pip install -q -p $V/bin/python "$tri" numpy pyyaml sqlalchemy packaging >> /root/res/pip_$name.log 2>&1
  uv pip install -q -p $V/bin/python --no-deps liger-kernel flag-gems >> /root/res/pip_$name.log 2>&1
  log "$name env: $($V/bin/python -c 'import torch,triton;print(torch.__version__,triton.__version__,torch.cuda.is_available())' 2>&1 | tail -1) ($(( $(date +%s)-t0 )) s)"
  for lib in $LIBS; do
    for run in base tb_always base2 tb_occ; do
      t0=$(date +%s); tag=${name}_${lib}_$run
      extra=(); case $run in tb_always) extra=(--tb always --tblog /root/res/tblog_$tag.jsonl);; tb_occ) extra=(--tb occupancy --tblog /root/res/tblog_$tag.jsonl);; esac
      dumpenv=(); [ $run = base ] && dumpenv=(TRITON_KERNEL_DUMP=1 TRITON_DUMP_DIR=/root/res/dump_${name}_$lib)
      env "${dumpenv[@]}" TRITON_CACHE_DIR=/root/cache_$tag bash /root/b/run_suite.sh $V/bin/python $lib /root/res/$tag.jsonl "${extra[@]}" > /root/res/log_$tag.txt 2>&1
      log "$tag: $(grep -c '"status": "ok"' /root/res/$tag.jsonl) ok $(grep -c '"status": "error"' /root/res/$tag.jsonl) err $(grep -c crashed /root/res/$tag.jsonl) crash ($(( $(date +%s)-t0 )) s)"
    done
    $V/bin/python /root/b/compare.py /root/res/${name}_${lib}_base.jsonl /root/res/${name}_${lib}_tb_always.jsonl /root/res/tblog_${name}_${lib}_tb_always.jsonl /root/res/${name}_${lib}_base2.jsonl > /root/res/cmp_${name}_${lib}_always.txt 2>&1
    $V/bin/python /root/b/compare.py /root/res/${name}_${lib}_base.jsonl /root/res/${name}_${lib}_tb_occ.jsonl /root/res/tblog_${name}_${lib}_tb_occ.jsonl > /root/res/cmp_${name}_${lib}_occ.txt 2>&1
    log "$name $lib always: $(grep -E 'rewritten-kernel' /root/res/cmp_${name}_${lib}_always.txt)"
  done
done
log "end"

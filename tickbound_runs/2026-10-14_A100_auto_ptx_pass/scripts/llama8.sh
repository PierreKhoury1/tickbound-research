#!/usr/bin/env bash
# llama8.sh: after run 3 (DONE): llama_rmsnorm AUTO again with a batched-load budget of 8 per loop (= the hand RO1 width).
until [ -f /root/DONE ]; do sleep 10; done
LOG=/root/res/onbox.log; log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
rm -rf /root/bl; mkdir -p /root/bl; tar -xzf /root/tickbound.tgz -C /root/bl llama_rmsnorm common 2>/dev/null || tar -xzf /root/tickbound.tgz -C /root/bl
export TB_REAL_PTXAS=/root/ptxas.real TB_SRC=/root/tb/src TB_PTX_K=8 TB_PTX_LOADS=8 TB_PTX_KERNELS="_Z12rms_norm_f32ILi1024" TB_PTX_LOG=/root/res/auto/llama_l8.ptxlog.jsonl
rm -f /root/res/auto/llama_l8.ptxlog.jsonl
( cd /root/bl/llama_rmsnorm && timeout 900 bash ./run.sh A100 ) > /root/res/llama_l8_run.log 2>&1
log "llama_l8 run rc=$?"
mkdir -p /root/res/auto_l8/llama_rmsnorm && cp -r /root/bl/llama_rmsnorm/results /root/res/auto_l8/llama_rmsnorm/
python3 /root/compare_builds.py /root/res/orig/llama_rmsnorm /root/res/auto_l8/llama_rmsnorm /root/res/compare_llama_l8.json > /root/res/compare_llama_l8.txt 2>&1
log "llama_rmsnorm LOADS=8 COMPARE: $(cat /root/res/compare_llama_l8.txt | tr '\n' ' ' | cut -c1-300)"
cd /root && tar -czf /root/res.tgz res && touch /root/DONE_L8

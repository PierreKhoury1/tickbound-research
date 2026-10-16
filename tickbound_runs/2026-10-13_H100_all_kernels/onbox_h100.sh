#!/usr/bin/env bash
# onbox_h100.sh (13 Oct 2026): every real-kernel reorder harness on one H100, image nvidia/cuda:12.6.3-devel-ubuntu22.04.
# Extracts /root/tickbound.tgz, runs build + run of each harness (each isolated, own timeout), copies results,
# packs /root/res.tgz and writes /root/DONE, also after a failure. Rents nothing, reads no secret.
set -u
mkdir -p /root/res; LOG=/root/res/onbox.log
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
finish() { log "finish"; cd /root && tar -czf /root/res.tgz res; touch /root/DONE; }
trap finish EXIT
log "start"; nvidia-smi -L | tee -a "$LOG"; nvidia-smi --query-gpu=name,clocks.sm,clocks.max.sm,driver_version --format=csv | tee -a "$LOG"
(apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3 python3-pip >/dev/null) >> "$LOG" 2>&1
log "apt rc=$?"
mkdir -p /root/b && tar -xzf /root/tickbound.tgz -C /root/b && log "bundle ok"
step() {  # name timeout cmd...
  local name=$1 to=$2; shift 2
  local t0=$(date +%s)
  ( cd /root/b/$name && timeout "$to" "$@" ) >> /root/res/$name.log 2>&1
  local rc=$?; log "$name: $* rc=$rc ($(( $(date +%s) - t0 )) s)"
}
save() { mkdir -p /root/res/$1; ( cd /root/b/$1 && cp -r results traces sass sass_box /root/res/$1/ 2>/dev/null ); true; }
# Triton kernels first (CuAsmRL / Triton comparison), then the CUDA library kernels.
step kernl_fused_ff 900 env ARCHS=90 bash ./build.sh; step kernl_fused_ff 1500 bash ./run.sh; save kernl_fused_ff
step kernl_rmsnorm 1200 bash ./run.sh H100; save kernl_rmsnorm
step llama_rmsnorm 900 bash ./run.sh H100; save llama_rmsnorm
step faiss_kselect 600 bash ./build.sh 90; step faiss_kselect 900 bash ./run.sh H100; save faiss_kselect
step pt_embbag 600 bash ./build.sh 90; step pt_embbag 900 bash ./run.sh H100; save pt_embbag
step rodinia_pf 600 bash ./build.sh; step rodinia_pf 900 bash ./run.sh H100; save rodinia_pf
step aerial_rssi 600 bash ./build.sh; step aerial_rssi 900 bash ./run.sh H100; save aerial_rssi
log "end"

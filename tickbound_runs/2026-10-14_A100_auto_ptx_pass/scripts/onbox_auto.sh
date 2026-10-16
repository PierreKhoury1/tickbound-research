#!/usr/bin/env bash
# onbox_auto.sh (14 Oct 2026): the automatic PTX unroll-and-batch pass (tickbound tb_ptxas wrapper) on the five
# CUDA reorder harnesses, one A100/H100, image nvidia/cuda:12.6.3-devel-ubuntu22.04.
#   ORIG build: real ptxas (TB_PTX_OFF=1).  AUTO build: /usr/local/cuda/bin/ptxas = tb_ptxas.py, transforming only
#   the harness's original kernels (TB_PTX_KERNELS), so each harness's own hand variants stay untouched and its
#   bitwise check of hand-vs-orig inside the AUTO run compares the automatic kernel with the true original's output.
# Writes /root/res/{orig,auto}/<harness>/results, ptx logs, compare JSON, /root/res.tgz + /root/DONE. No secrets read.
set -u
mkdir -p /root/res/orig /root/res/auto; LOG=/root/res/onbox.log
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
finish() { log "finish"; cd /root && tar -czf /root/res.tgz res; touch /root/DONE; }
trap finish EXIT
log "start"; nvidia-smi -L | tee -a "$LOG"; nvidia-smi --query-gpu=name,clocks.sm,clocks.max.sm,driver_version --format=csv | tee -a "$LOG"
(apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3 python3-pip >/dev/null) >> "$LOG" 2>&1
MODES=${MODES:-orig auto}
rm -rf /root/tb; mkdir -p /root/b /root/ba /root/tb
tar -xzf /root/tb_src.tgz -C /root/tb
case " $MODES " in *" orig "*) rm -rf /root/b; mkdir -p /root/b; tar -xzf /root/tickbound.tgz -C /root/b;; esac
case " $MODES " in *" auto "*) rm -rf /root/ba; mkdir -p /root/ba; tar -xzf /root/tickbound.tgz -C /root/ba;; esac
log "bundles ok (modes: $MODES)"
GPU=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1); case "$GPU" in *A100*) G=A100; SM=80;; *H100*) G=H100; SM=90;; *) G=A100; SM=80;; esac
log "gpu $G sm_$SM"
# the wrapper as ptxas (idempotent: the real one is kept at /root/ptxas.real)
[ -f /root/ptxas.real ] || cp /usr/local/cuda/bin/ptxas /root/ptxas.real
install -m 755 /root/tb/src/tickbound/triton/tb_ptxas.py /usr/local/cuda/bin/ptxas
export TB_REAL_PTXAS=/root/ptxas.real TB_SRC=/root/tb/src TB_PTX_K=${TB_PTX_K:-4}
log "ptxas wrapper: $(TB_PTX_OFF=1 ptxas --version | tail -1)"
step() {  # name timeout cmd...
  local name=$1 to=$2; shift 2
  local t0=$(date +%s)
  ( timeout "$to" "$@" ) >> /root/res/$name.log 2>&1
  local rc=$?; log "$name: $* rc=$rc ($(( $(date +%s) - t0 )) s)"
}
declare -A FILTER=(
  [rodinia_pf]="pf_time24normalize_weights_kernelE,pf_time17find_index_kernelE"
  [faiss_kselect]="12l2SelectMin1If,12l2SelectMinKIif"
  [pt_embbag]="eb_time4orig"
  [llama_rmsnorm]="_Z12rms_norm_f32ILi1024"
  [aerial_rssi]="cfo_orig_time"
)
declare -A BUILD=( [rodinia_pf]="bash ./build.sh" [faiss_kselect]="bash ./build.sh $SM" [pt_embbag]="bash ./build.sh $SM" [llama_rmsnorm]="" [aerial_rssi]="bash ./build.sh" )
declare -A RUN=( [rodinia_pf]="bash ./run.sh $G" [faiss_kselect]="bash ./run.sh $G" [pt_embbag]="bash ./run.sh $G" [llama_rmsnorm]="bash ./run.sh $G" [aerial_rssi]="bash ./run.sh $G" )
for H in rodinia_pf faiss_kselect pt_embbag llama_rmsnorm aerial_rssi; do
  for mode in $MODES; do
    rm -rf /root/res/$mode/$H /root/res/$mode/$H.ptxlog.jsonl
    if [ $mode = orig ]; then D=/root/b/$H; export TB_PTX_OFF=1; unset TB_PTX_KERNELS TB_PTX_LOG
    else D=/root/ba/$H; unset TB_PTX_OFF; export TB_PTX_KERNELS="${FILTER[$H]}" TB_PTX_LOG=/root/res/auto/$H.ptxlog.jsonl; fi
    if [ -n "${BUILD[$H]}" ]; then ( cd $D && step ${H}_${mode}_build 1200 ${BUILD[$H]} ); fi
    ( cd $D && step ${H}_${mode}_run 1500 ${RUN[$H]} )
    mkdir -p /root/res/$mode/$H && ( cd $D && cp -r results traces sass build/*.log build/*.sass /root/res/$mode/$H/ 2>/dev/null ); true
    if [ $mode = auto ] && [ -f /root/res/auto/$H.ptxlog.jsonl ]; then
      log "$H auto pass: $(python3 -c "
import json,sys
n=t=0
for l in open('/root/res/auto/$H.ptxlog.jsonl'):
    r=json.loads(l); n+=1; t+=r.get('loops_transformed',0) or 0
print(n,'ptx files,',t,'loops transformed')")"
    fi
  done
  python3 /root/compare_builds.py /root/res/orig/$H /root/res/auto/$H /root/res/compare_$H.json > /root/res/compare_$H.txt 2>&1
  log "$H COMPARE: $(cat /root/res/compare_$H.txt | tr '\n' ' ' | cut -c1-400)"
done
unset TB_PTX_OFF TB_PTX_KERNELS
log "end"

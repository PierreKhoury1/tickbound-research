# kernl_rmsnorm: load reordering in Kernl's Triton RMSNorm (A100 sm_80, H100 sm_90)

## The kernel and who uses it
`rmsnorm_triton`: standalone Triton RMSNorm from Kernl's experimental LLaMA-2 port (ELS-RD, Apache-2.0,
`experimental/llama-v2/kernel/fused_kernel_proj_qkv.py:12-55` @ 0347bec7). Kernl's model forward does not call it: it
fuses RMSNorm into the QKV and FF matmul kernels (`llama/model.py:171-176, 245-248, 286-300`). Its only call site is
that file's import-time test and benchmark (x [1, 16, 4096], lines 357-361, `out = torch.empty_like(x)`). CuAsmRL
(He and Yoneki, CGO 2025) benchmarks the same body (`benchmarks/rmsnorm.py` and `benchmarks/cutlass/torch_rmsnorm.py`,
kernel `_cuasmrl`, also `out = torch.empty_like(x)`). The PTX here is Triton 2.2.0 output for CuAsmRL's verbatim copy
(the sweep's `rmsnorm_cuasmrl` in `../../cuasmrl/kernels/cuasmrl_kernels.py`), hence the symbol `rmsnorm_cuasmrl_*`;
apart from the name it is the same code (checked line by line against Kernl's source). Each CTA handles one row:
* pass 1 loads x in chunks of BLOCK_N_SIZE and sums x^2;
* the sum is reduced by warp shuffles, shared memory and 2 `bar.sync`, then `rstd = rsqrt(sum / N + eps)`;
* pass 2 reloads x and rms_w chunk by chunk and stores `x * rstd * rms_w` (fp16).

Launch (Kernl's `rmsnorm_triton_wrapper`): x [1, M, N] fp16 contiguous, `out = torch.empty_like(x)`, grid (1, M),
`BLOCK_N_SIZE=1024`, `num_warps=4` (128 threads), `eps=1e-6`, 16 B of shared memory. N = 4096 / 5120 / 8192 are the
LLaMA-2 7B / 13B / 70B hidden sizes (the Kernl call site uses 4096). M = rows (tokens): the Kernl call site uses
M = 16; M = 1..256 covers decode-sized row counts, and M = 1024 / 4096 are prefill-sized controls.

**orig** is Triton 2.2.0's PTX, verbatim (`src/ptx/orig_n{N}.sm{80,90}.ptx`). It was regenerated without a GPU by
`tools/gen_ptx.py`, which calls the sweep's `compile_tt.py` with pip triton 2.2.0 (in WSL). The PTX for N=4096 is
byte-identical to the sweep's `rmsnorm_kernl_bn1024`. The PTX does not depend on M. N_SIZE is a constexpr, so there is
one PTX per N, and they differ only in loop bounds and the 1/N constant. `build.sh` assembles every PTX exactly as
Triton 2.2's `compile_ptx_to_cubin` does: `ptxas -lineinfo -v --gpu-name=sm_80 | sm_90a`, with the default -O3.
Here ptxas is 12.6.85, the version in the box image nvidia/cuda:12.6.3. The harness loads the cubin with the driver
API, as Triton's launcher does, so the box needs neither Triton nor PyTorch.

## What ptxas does (`sass/`, `sass/LOADS.md`)
ptxas unrolls both loops completely, so the kernel is one straight-line block of 368 to 672 SASS instructions.
* **Pass 1 is fine.** All x loads are issued together.
* **Pass 2 is serialised.** Each chunk does `LDG.E.128 x; LDG.E.128 rms_w; ~40 ALU; STG.E.128 out`, and the loads of
  chunk c+1 are issued only after the STG of chunk c. ptxas cannot prove that `out` does not alias x or rms_w: Triton
  emits no `noalias`, and PTX has no restrict.
* **The cost.** N/1024 memory round trips are serialised: 4 / 5 / 8 L2 (or DRAM) round trips for rms_w. Each CTA has
  only 4 warps, and M <= 256 rows put at most 3 CTAs on an SM, so nothing hides them.

From `sass/LOADS.md` (pass-2 load "waves" = serialised round trips):

| variant | pass-2 LDGs placed | waves sm_80 N=4096 / 8192 | waves sm_90 N=4096 / 8192 | regs sm_80 / sm_90 (N=4096) |
|---|---|---|---|---|
| orig | after each previous chunk's STG | 2+2+2+2 / 8 x 2 | 2+2+2+2 / 8 x 2 | 32 / 32 |
| ro | all above the first STG (the task's reorder) | 4+4 / 10+6 | 4+1+1+2 / 12+4 | 38 / 44 |
| ro2 | all between the two BAR.SYNC | 8 / 16 | 8 / 16 | 48 / 56 |
| ro3 | ro2, rms_w loads at kernel entry in the PTX | 8 / 16 | 1+7 / 16 | 48 / 56 |

ptxas does not keep ro3's rms_w loads at entry; where it puts them is described under ro3 below and in
`sass/LOADS.md`.

## The reorders (`tools/make_variants.py`)
Every variant keeps every non-load instruction of pass 2 unchanged and in its original order. Per element, that is
the same `cvt.f32.f16 / mul.f32 (x * rstd) / mul.f32 (* rms_w) / cvt.rn.f16.f32` chain and the same address
arithmetic. Only where the 2T `ld.global.v4` of pass 2 are issued changes; their data go to per-chunk virtual
registers. Pass 2 is written out per chunk, as ptxas unrolls it anyway.
* **ro** is the task's definition. The pass-2 loads of chunks 2..T are moved above the first `st.global.v4`, at the
  top of pass 2. ptxas still sinks some of them toward their use, but it can no longer put any after a store.
* **ro2** puts all pass-2 loads between the two `bar.sync`. ptxas does not move loads across `bar.sync`, so they are
  all in flight while the block reduction runs.
* **ro3** is ro2 with the rms_w loads at kernel entry. ptxas keeps them before the first BAR.SYNC but sinks most of
  them to the end of pass 1 and into the warp reduction:
  * sm_80 N=4096 / 8192 and sm_90 N=8192 issue all T in the last stretch of pass 1 and in the warp reduction (sm_80
    N=4096: 0x0780-0x0a70, BAR.SYNC at 0x0ab0, x loads at 0x00c0-0x00f0), each on a scoreboard that no pending
    pass-1 load uses. Their latency overlaps the end of pass 1 and both reductions.
  * sm_90 N=4096 / 5120 and sm_80 N=5120 issue one rms_w load right after the pass-1 x loads, on the same scoreboard
    as a pass-1 x load (ro3_n4096.sm_90: w[0] at 0x0170 on SB4 with x1[2] at 0x0110, waited on at 0x0550). Pass 1
    therefore waits for it, and in decode its DRAM latency is exposed in pass 1. The other T-1 issue at the end of
    pass 1 and in the warp reduction, just before BAR 1 (0x09d0-0x0b10): the '1+k' waves in `sass/LOADS.md`.
  The model reads the real SASS, so the predictions include both placements.

**Legality.** The kernel reads only x and rms_w and writes only out. At both real call sites (Kernl's test and
benchmark, CuAsmRL's benchmark), `out = torch.empty_like(x)` is a fresh allocation, disjoint from x and rms_w, and
nothing else writes x or rms_w during the kernel. A load
therefore returns the same value whether it is issued before or after any store of this kernel. `bar.sync` orders
only this CTA's own accesses, and no CTA writes x or rms_w. x is re-read in pass 2 exactly as in the original: an L1
hit, never forwarded from pass 1. The arithmetic and the operand order are identical, so out is bit-identical. The
harness checks that with memcmp in every case.

**Registers.** The live data cost registers: up to 84 on sm_80 for N=8192. At decode-sized M this costs no
occupancy. At M=4096 it cuts resident CTAs per SM from 16 to 10 (ro2, N=4096). That is one of the cases where the
model predicts no gain.

## Trace build: stamps inserted into ptxas's SASS (`tools/instrument.py`, `check_trace_sass.py`)
**Why not PTX stamps.** In a straight-line kernel, ptxas schedules and register-allocates the whole block at once, so
time stamps written in PTX change pass 2 too. An earlier attempt tried 160 PTX stamp placements: 0 kept pass 2
identical, 28 kept it "timing-equivalent" (`local/exp/res4.txt`).

**What the trace build is instead.** `*.tbase.ptx` is the timing PTX plus one u64 kernel parameter (the trace
buffer). ptxas gives it the same `.text`, word for word, which `instrument.py` checks. `instrument.py` then inserts
stamp code into that cubin, only at five points:
* **entry**: a 13-instruction prologue. It records %globaltimer and %clock64 first, then writes the warp's record
  {smid, ctaid.y, warp, magic, entry stamp}.
* **p1_end**: before the first SHFL.
* **bar1**: before the first BAR.SYNC.
* **bar2**: right after the second BAR.SYNC.
* **exit**: before EXIT.

How the inserted code is made and kept apart from the kernel:
* **Encodings.** The instruction words are ptxas 12.6's own, taken from a donor kernel (`local/donor/`), with
  registers renumbered.
* **Registers.** Only R[K..K+27] (K = the kernel's register count rounded up to 4) and the kernel's own
  memory-descriptor UR, which is loaded once and never rewritten.
* **Scoreboards.** Only the prologue uses them, and it drains them before the kernel's first instruction. Mid-kernel
  stamps are fixed-latency CS2R reads plus a store, with no scoreboard.
* **Metadata.** The ELF metadata is patched: section and program header offsets, EIATTR_EXIT/COOP_GROUP instruction
  offsets, and the register count.

`check_trace_sass.py build/sm_80 build/sm_90` verifies on the cuobjdump listings:
1. With the inserted words removed, the trace build is the timing build: every instruction is equal in all 128 bits,
   including control codes, and in the same order.
2. No stamp sits between two instructions of the reduction region or of the hot region. The hot region is pass 2,
   from the second BAR.SYNC to the last store.
3. The inserted code uses only the reserved registers and scoreboards.
4. cuobjdump disassembles every inserted word as the intended instruction.
5. Every instruction-offset list in .nv.info (EXIT, SHFL), mapped through the insertion, matches, and the register
   count covers the stamp registers.

Locally all 24 trace builds pass (`sass/check_trace_sass_sm_80.txt`, `_sm_90.txt`), and `build.sh` re-checks them on
the box. Instrumentation cost: 25 instructions, about 150 cycles per warp. The harness also times the trace builds
(`trace_build_mean_us` in the extra CSV). Trace phases:

| segment | what it covers |
|---|---|
| entry -> p1_end | pass 1: x loads and sum of x^2 |
| p1_end -> bar1 | warp reduction |
| bar1 -> bar2 | block reduction (ro2 issues all its pass-2 loads here, ro3 its x re-loads) |
| bar2 -> exit | pass 2 |

## Test matrix: 37 cases x 4 variants per GPU (`src/harness.cpp`)
| L2 state | how | N | M (rows = CTAs) |
|---|---|---|---|
| warm | the same x and rms_w every launch, so both are L2-resident | 4096, 5120, 8192 | 1, 4, 16, 64, 256 (+1024, 4096 for N=4096) |
| decode | before each launch, an L2 flush (memset of 2.5 x L2) and then a rewrite of x. x is L2-resident, as just written by the previous op; rms_w comes from DRAM, as in LLM decode | 4096, 5120, 8192 | 1, 4, 16, 64, 256 |
| cold | before each launch, an L2 flush, so both come from DRAM | 4096 | 1, 16, 256, 1024, 4096 |

M <= 64 is one CTA per SM (4 warps per SM, 1 per scheduler). M=256 is 2-3 CTAs per SM. M=1024 and 4096 run up to
full occupancy and are DRAM / issue bound. Those are the controls where the model predicts about x1.0.

**Timing.**
* Warm: a CUDA graph of B back-to-back launches, B set so that a batch takes about 2 ms (20-400 launches), with
  events around the graph. Mean per launch = elapsed / B. Before each batch, a one-thread kernel spins for 20 us
  while the host enqueues the start event and the graph, so the host's submit latency is outside the events.
* Decode and cold: per launch, the flush (and the x rewrite) and then events around the single launch. The flush and
  the rewrite sit outside the events. B = 30.
* Batches are repeated 31 times (warm) or 21 times (flushed). The variant order is rotated every repetition, and the
  CSV reports median, p10 and p90 of the batch means.
* An empty kernel with the same grid is timed the same way. It measures the per-launch overhead E that no
  reordering can remove (extra CSV).

**Span.** The trace build is launched 21 times per variant in the same L2 state. Each recorded launch follows a
warm-up launch of the same trace build (its records are then cleared), so it does not pay first-touch instruction
fetches that the graph-timed launches never pay; in flushed cases the flush then follows, as in the timing loop.
Device span = first warp entry to last warp exit. Each SM's %clock64 is placed on the %globaltimer axis by
intersecting the windows each stamp gives: gt <= t < gt + tick. The tick is measured: about 1 us on A100, 32 ns on
H100. The SM clock f that converts cycles to ns is measured per case (2 ms of %globaltimer, right after the timing
runs, so in steady state); it is the `sm_clock_ghz` of the extra CSV and of each trace JSON. The CSV reports the
median span. The span is given only when every CTA is resident at once in both builds (M <= 256). The trace JSON of
the median-span launch is written for M <= 256.

Checks on the placement and the occupancy (extra CSV, and per launch in each trace JSON):
* `placement_window_min_ns` is the narrowest SM window over the launches. An empty window (negative width, beyond a
  2-cycle tolerance for the integer %clock64) means the stamps contradict f, for example a clock change during the
  launch. `placement_inconsistent_sms` counts such SMs, summed over the launches; any such launch also counts in
  `trace_bad_launches`. Before this check, an empty window showed up as a 0-ns (perfect-looking) window.
* `observed_max_ctas_per_sm_median` / `observed_sms_median` are the CTAs that ran on the busiest SM and the SMs used,
  read from the records (`smid`). They check the "1 CTA per SM at M <= 64" premise of every prediction. For M > 256
  they count CTAs over the whole launch, not CTAs resident at once.

**Correctness.**
* Every variant's output, from the timing and the trace build, is memcmp'ed against orig: bitwise_equal and
  max_abs_diff. All timing builds run first, then the trace builds, whose records are checked as well.
* orig is run twice to check that it is deterministic (no atomics).
* orig is checked against a CPU reference within a tolerance. It cannot be bitwise: fp16 output, approximate rsqrt.

**Also recorded.**
* The SM clock (from %clock64 over 4 ms of %globaltimer) and the timer tick at the start and the end of the run
  (`*_env.json`), and per case before its trace launches (extra CSV).
* The driver's own PTX JIT of each variant (registers and warm time, N4096_M16) in `*_env.json`, as a cross-check
  against ptxas 12.6.
* `results/box_build_*/`: the box's own SASS, ptxas version and nvidia-smi output.

## Predictions (`predictions.json`, written before any run; sha256 in `predictions.json.sha256`)
There are 222 entries: 37 cases x 3 variants x 2 GPUs. Each has `pred_lo` / `pred_hi` for the measured speed-up
(orig mean_us_median / variant mean_us_median), plus `pred_span_lo` / `pred_span_hi` for the device span.

**Model** (`tools/predict.py` on `tools/sassmodel.py`):
1. One warp's latency chain on each variant's real SASS: the stall counts and scoreboard waits, load latency classes
   per L2 state, and the SM's L2 and L1 fill ports shared by its warps.
2. The issue bound for the warps per scheduler.
3. Resident CTAs and waves from the register counts.
4. The aggregate DRAM / L2 bandwidth.
5. The measured time is that body time plus a per-launch overhead E.

**Latency classes and priors** (cycles):

| GPU | L2 | DRAM | L1 | E, CUDA graph | E, single launch after a flush |
|---|---|---|---|---|---|
| A100 | 220 / 374 | 493 / 645 | 39 | 0.8-2.6 us | 1.5-4.5 us |
| H100 | 280 / 472 | 572 / 774 | 35 | 0.6-2.2 us | 1.3-4.0 us |

**Ranges.** Each range spans latency low / high, E, the SM clock, and model-error factors: x0.9-1.3 on the part the
reorder does not change and x0.75-1.1 on the part it saves. E dominates the width; the predicted kernel-body and span
ratios are much tighter.

| GPU | L2 | N | M | ro | ro2 | ro3 | ro2 device span |
|---|---|---|---|---|---|---|---|
| A100 | warm | 4096 | 1-64 | 1.07-1.33 | 1.13-1.60 | 1.14-1.80 | 1.47-1.86 |
| A100 | warm | 4096 | 256 | 1.07-1.26 | 1.11-1.45 | 1.15-1.63 | 1.29-1.58 |
| A100 | warm | 8192 | 1-64 | 1.20-1.89 | 1.22-2.06 | 1.23-2.08 | 1.68-2.31 |
| A100 | decode | 4096 | 1-64 | 1.09-1.37 | 1.15-1.66 | 1.18-1.80 | 1.81-2.17 |
| A100 | decode | 8192 | 1-64 | 1.26-2.00 | 1.30-2.26 | 1.31-2.28 | 2.30-2.89 |
| A100 | warm / cold | 4096 | 1024, 4096 | 0.95-1.14 | 0.95-1.19 | 0.95-1.22 | (no span: multi-CTA) |
| H100 | warm | 4096 | 1-64 | 1.08-1.40 | 1.13-1.69 | 1.15-1.86 | 1.47-1.89 |
| H100 | warm | 8192 | 1-64 | 1.30-2.39 | 1.32-2.58 | 1.35-2.73 | 2.04-2.85 |
| H100 | decode | 4096 | 1-64 | 1.09-1.41 | 1.15-1.71 | 1.15-1.73 | 1.80-2.20 |
| H100 | decode | 8192 | 1-64 | 1.31-2.35 | 1.36-2.63 | 1.38-2.74 | 2.65-3.42 |
| H100 | warm / cold | 4096 | 1024, 4096 | 0.95-1.22 | 0.95-1.23 | 0.95-1.26 | |

**Changes after the freeze.** `predictions.json` is unchanged (its sha256 still matches). After the review, the
measurement changed in three ways, each removing a bias that is the same for every variant:
* the 20-us spin before each graph batch (host submit latency);
* the trace warm-up with the trace build itself (instruction fetch);
* the per-case SM clock (span and phase conversion).

The stricter smoke test and the shorter timeouts do not change any number.

In words:
* **Ordering.** The model expects ro < ro2 <= ro3 for every latency-bound case.
* **Size.** Gains grow with N (more serialised round trips) and with latency (decode/cold > warm).
* **Controls.** The large-M controls predict about x1.0, possibly a little lower for ro2/ro3 because of fewer
  resident CTAs.

## Files
* `src/ptx/`: orig (verbatim Triton PTX) and ro/ro2/ro3 PTX for N=4096/5120/8192, sm80 and sm90. `*.tbase.ptx` are
  the same with the trace parameter.
* `src/harness.cpp` is the host benchmark (runtime and driver API, C++17, host code only). `src/util.ptx.in` holds the
  clock-calibration and empty kernels.
* `build.sh`: ptxas for every variant (timing, trace base), cuobjdump SASS, the instrumenter, the trace check and the
  nvcc host build.
* `run.sh [A100|H100]`: builds if needed, then runs a smoke test under a 2-minute timeout. The smoke test fails if
  the harness crashes or hangs, or exits 3 because a trace build ran but wrote bad records or an output that differs
  from orig. If it fails, the full run goes without the trace builds. The full run has an 8-minute timeout. It prints
  DONE.
* `predictions.json` (+ `.sha256`), `check_trace_sass.py`.
* `sass/`: annotated SASS of every variant with the hot region marked, `LOADS.md`, and the local trace-check
  reports.
* `tools/`: `make_variants.py` (the reorders), `instrument.py` + `cubin_elf.py` (trace build), `sassmodel.py` +
  `predict.py` (model), `mark_sass.py`, `gen_ptx.py` (regenerate the orig PTX).
* `local/`: local toolchain (ptxas 12.6.85 / CUDA 12.6 headers from NVIDIA's pip wheels), the Triton build
  artefacts, the donor kernel, host unit tests (`local/hosttest`) and scratch. It is not needed on the box.

## On the box (about 2-3 minutes per GPU)
Copy this directory **without `local/` and `build/`** (2.6 MB), then run `bash run.sh` (or `bash run.sh A100` /
`bash run.sh H100`).
It builds with the image's CUDA 12.6: about 1 minute of ptxas and nvcc, plus `apt-get install python3` if Python is
missing (used by the instrumenter). Then the smoke test takes about 15 s and the full run about 1 minute. Worst case,
with timeouts: about 2 minutes of build, 2 minutes of smoke test and 8 minutes of full run.

Outputs:
* `results/kernl_rmsnorm_<GPU>_<stamp>.csv`: the 17 shared columns, one row per variant x case.
* `_extra.csv`: empty-kernel overhead, trace-build time and bitwise, phases, span p10/p90, CPU-reference error, the
  per-case SM clock, the placement checks and the observed CTAs per SM.
* `_env.json` and `_run.log`.
* `results/box_build_<GPU>_<stamp>/`.
* `traces/kernl_rmsnorm__<GPU>__<case>__<variant>.json` (about 130 files, up to about 300 KB each).

## Uncertain
* **The overhead E** sets most of each predicted range. The empty-kernel rows measure it, so the body-level claim can
  be checked against the span and the extra CSV.
* **A100 span resolution.** %globaltimer ticks every ~1 us on the A100, so per-launch A100 spans rely on the window
  placement. On 50 synthetic launches (`local/hosttest`) the error was a median of 68 ns and at most 280 ns, against
  0.4 / 2.6 ns with H100's 32 ns tick. The CSV reports the median over 21 launches.
* **The trace build is hand-encoded SASS.** It is checked by disassembly but has never run on hardware. If it faults
  or hangs (the smoke test runs under a 2-minute timeout), writes bad records or a different output (the smoke test
  exits 3), or reports fewer than K+28 registers, it is disabled, and the timing results do not depend on it. In the
  correctness step the trace builds run after all timing builds, so a trace build that wrote outside its record could
  not show up as a timing-build mismatch.
* **Code eviction in flushed cases.** Decode/cold flushes also evict the kernel's code from L2, so each flushed
  launch may fetch its 6-11 KB of instructions from DRAM. The memset does not flush the SM-level instruction caches,
  so part of the code may still hit there, and the size of the effect is unknown. This cost is the same for every
  variant, is not in the model, and the empty kernel does not measure it; it lowers the measured decode/cold ratios.
* **Prologue cost.** The stamp prologue delays every warp's first kernel instruction by about 60-80 cycles (S2R
  latency), the same for every variant. The span therefore includes it, and the predicted span ratios add 150
  cycles to both builds.
* **Register counts.** ro/ro2/ro3 use more registers. They are irrelevant at M <= 256, but they matter at M=4096,
  where ro2/ro3 may come out slightly slower: the predicted range goes down to 0.95.
* **Kernl's own benchmark** (`triton.testing.do_bench`) flushes L2, so its numbers correspond to our "cold" or
  "decode" rows, not "warm".

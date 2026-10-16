# Full-kernel GPU profiling with hardware timers

MSc Advanced Computing research, King's College London · Pierre Khoury · status 16 October 2026

This repository holds the research behind **tickbound**, a profiler that timestamps work *inside* GPU kernels with
the GPU's own hardware counters. It puts every checkpoint, from every SM of every GPU in a machine, on one host clock
with a stated error bound. The bound is hard under assumptions this README names; H100 placement across SMs is
empirical. With its own probe kernels we measured NVIDIA A100 and H100 GPUs (single GPUs, and eight A100s in one
host), and tested which instruction reorderings are legal and which save time. We then applied one reordering, issuing
a loop's loads a group ahead, to eight production kernels, by hand and by an automatic compiler pass, and traced per
instruction where the saved cycles came from.

The full tables, data paths and limits are in **[FINDINGS.md](FINDINGS.md)**. All GPU measurements ran on rented
vast.ai machines between 8 and 16 October 2026 (about $15 in total).

**This version was revised on 10 October 2026 after an AI-assisted audit**, which recomputed the results from the raw
data; FINDINGS section 8 lists every correction. **It was extended on 16 October** with the real-kernel reordering
results (FINDINGS section 9).

## Summary

1. **Host time is not kernel time.** On the A100, 17.3 µs pass from the launch call to `cudaStreamSynchronize`
   returning, around 3.5 µs of warp execution. This was measured on our instrumented probe kernel; no uninstrumented
   control was run yet.
2. **We can place every part of a kernel on one clock, with stated bounds.**
   - **One SM.** Inside one SM, timing is exact to the cycle.
   - **Host clock.** It is ±0.55–1.03 µs for kernel timing: ±0.55–0.90 µs where the syncs are at most 0.26 s apart,
     and ±0.79–1.03 µs in the 8-GPU run (syncs 16 s apart, events within 0.17 s of a sync). It is hard if the
     GPU/host clock rate is constant between the syncs; at the drift we observed, a change would add at most ~50 ns
     in these runs.
   - **Across SMs.** ±29–285 ns on A100 (median per run). On H100, ±12–23 ns, but empirical, not proven.
   - **Eight GPUs.** Eight GPUs share one host clock with ±0.85–1.2 µs per GPU. Their start order can be proved only
     when they are more than ~1.7–2.3 µs apart.
3. **Reordering: one transform, proven on a microkernel and on eight production kernels.** Issuing the next loop
   iterations' loads before the current work, a move ptxas does not make across a loop branch, ran 1.24–1.46× faster
   than the compiler's own unrolled schedule on an A100 microkernel, within ~20 cycles per iteration of the prediction
   (section 5.1). On real kernels (section 5.2; A100 and H100; outputs bit-identical) it beats the compiler on all
   eight, warm and cold: FAISS k-select 2.1–2.7×, Rodinia particlefilter 2.5–3.6×, PyTorch EmbeddingBag 1.1–1.5×,
   Kernl RMSNorm 1.2–1.3×, llama.cpp rms_norm 1.2×, NVIDIA Aerial cfo 1.2×, Kernl fused FF 1.2× over its Triton 2.2
   schedule. An **automatic** PTX pass (a ptxas drop-in, no source edits) reproduces the search, scan and gather wins
   (1.1–3.3×). Against **Triton 3.8** it wins only where Triton's own pipeline is too shallow (DRAM-bound decode, 1.9×)
   and loses elsewhere (fused FF median 0.99 on H100); on Triton 3.x library kernels the pass finds no loop to
   transform (median 1.00). In **CuAsmRL**'s action space the sound gain is ≤ 2.2%. The rest of what we know:
   - **Latency hiding works.** For each load, hiding work under the load's latency follows the textbook model to
     within 1.5 FFMA.
   - **The compiler already did it.** In our test kernel the compiler had already put the load first.
   - **Fences.** A fence stalls its warp for a fixed time that the work around it does not hide.
   - **The checker.** Our legality checker refused every deliberate violation it was given and approved only edits
     that ran correctly. But this was on small test kernels only.
4. **Where the cycles go, per instruction.** A sliding probe (one cycle-counter read after instruction k, one build
   per k) shows the original Kernl RMSNorm waiting 192–226 cycles at exactly the four instructions that first consume
   a loaded vector; the reorder removes them, and the per-instruction sum matches the stopwatch within 1%. The same
   probe inside Kernl fused FF's K loop shows where Triton 3.8 waits (its `DEPBAR`, ~730 cycles per iteration at the
   decode shape) and where it does not (issue-bound at 64×32×32).
5. **What looks new** (section 6): a stated bound on every in-kernel checkpoint, mapped to the host clock across
   several GPUs (hard under the named assumptions; H100 placement across SMs and widened fits are empirical); a
   fence's cost does not shrink when its store has time to drain; with CUDA 12.6's barrier, register-only work runs
   free while the warp waits; and the per-instruction attribution of a reordering's gain on production kernels.
   Per-warp in-kernel tracing itself already exists in other tools.

## 1. Why we are doing this

GPUs now run work with deadlines and work spread over many GPUs at once:

- **GPU-based 5G/6G base stations.** NVIDIA Aerial runs the radio physical layer on GPUs, and each slot's
  processing must finish on time.
- **Multi-GPU training and inference.** Every collective step waits for the slowest GPU.
- **Distributed tracing across GPU clusters** (for example TempoTrace). It needs GPU timestamps it can trust in order
  to put events in the right order.

To find out why something is late, you have to see when each part of the work actually ran: on which GPU, on which
SM, in which part of the kernel, and how certain that time is. Today's tools each see part of that:

| Tool | What it sees | What it does not give |
|---|---|---|
| Nsight Systems / CUPTI | kernel start and end on a timeline; sampled counters and PC samples inside kernels | per-warp events inside a kernel |
| Nsight Compute | per-kernel metrics, sampled stall reasons, sampled metric timelines | when each warp did what |
| Ervin Tasnadi's nanobenchmarking | exact cycle cost of one instruction in an isolated snippet | other SMs, other GPUs, the host clock |
| Intra-kernel tracers (Neutrino, Triton Proton / KPerfIR, NVIDIA IKET, TVM CudaProfiler, Xtrace) | per-warp events of every SM on `%globaltimer` | a stated error bound; mapping to the host clock; alignment across GPUs |
| TempoTrace (arXiv:2609.23301) | cluster-wide event order from PTP-disciplined NIC timestamps | inside kernels; its GPU-side precision is a design target, not yet measured |

The idea of this project is **full-kernel profiling with hardware timers, with an error bound on every point**. Every
warp of every SM of every GPU stamps its own progress with the GPU's counters. The stamps then land on one host clock,
each with a stated worst-case error.

The second question builds on the first: with timing that exact, can we learn the rules of instruction reordering?
And can moving arithmetic into the time a memory load takes make a kernel faster than the compiler makes it?

## 2. Starting point: Ervin Tasnadi's nanobenchmarking

Ervin Tasnadi's post "Nanobenchmarking: cycle accurate benchmarking of CUDA kernels" (Core Velocity Lab,
3 December 2025) times single instructions to the cycle:

- He reads the SM cycle counter (`CS2R Rx, SR_CLOCKLO`) before and after a small code snippet.
- He then edits the compiled SASS with CuAssembler so that the closing read waits until the measured instruction
  has finished.

This gives exact cycle counts for an isolated snippet on one SM. Each SM's counter starts at its own value, so the
method cannot compare times between SMs.

tickbound keeps the exact cycle counter and adds the layers his method does not have:

| | Tasnadi | tickbound |
|---|---|---|
| Inside one SM | exact to the cycle | exact to the cycle. Shared-memory load: 23 cycles on A100 and H100 (his post: 22–23 on Turing) |
| Across SMs | not comparable | Each checkpoint reads timer · cycle · timer, and each block's cycle counter is fitted onto the GPU-wide timer. Result: A100 ±29–285 ns (median per run); H100 ±12–23 ns, empirical |
| GPU to host | – | Clock sync before and after every run: ±0.55–1.03 µs for kernel timing, hard under a constant clock rate between the syncs |
| Several GPUs | – | 8 A100s on one host clock, ±0.85–1.2 µs per GPU |
| What is timed | one snippet, with the SASS edited by hand | every warp of a whole kernel. A SASS check confirms that each timed step in the binary that ran holds only the instructions its name says |
| Reordering | – | Experiments E1–E7 compile the same instructions in different orders. 30 SASS edits made with CuAssembler are judged by a legality checker and then run on the GPU |

## 3. How it works

- **Three clocks.**
  - `clock64` counts cycles exactly on each SM, but each SM's count starts from a different value.
  - `%globaltimer` is one nanosecond timer per GPU that moves in steps: 1,024 ns on A100 (default rate) and 32 ns on
    H100.
  - The host clock, `CLOCK_MONOTONIC_RAW`, is where the CPU stamps launches, polls and syncs.
- **Every checkpoint is a bracket.** It reads the timer, then the cycle counter, then the timer again, so the cycle
  value is known to lie inside a window of the timer. Each timed phase ends with an instruction that uses the phase's
  result. This makes the closing read wait for the work, as in Tasnadi's method, but done from source code.
- **One line per block.** A block's checkpoints give many timer windows on one SM counter, and a straight
  cycle-to-time line is fitted through them.
  - **A100.** The timer steps only every 1,024 ns. The windows fall at different points between steps, like the marks
    on a vernier scale, so the line is placed far more finely than one step.
  - **H100.** The step is 32 ns and the fitted band is about one step wide, so the fit adds no resolution. At that
    step the straight-line model also fails for most multi-block launches, so H100 placement across SMs is empirical.
- **Host sync.**
  - Before and after each run, a GPU thread and a host thread exchange timestamps through shared host memory. The
    exchanges are timed around the moments the GPU timer steps to its next value.
  - The **strict bound** is the worst case over every clock offset and drift rate that agrees with both syncs.
  - It is hard if the rate is constant in between. The fit cannot detect a rate change inside the gap.
- **SASS gate.** The binary that measured is disassembled. Each timed step is checked to contain exactly what its
  name says, for example 1 FADD + N FFMA and nothing else. Builds that fail are dropped. This caught CUDA 12.2
  inserting extra waits into timed steps.
- **Built-in checks.** On every kernel-timing run (32 runs), three things are checked against the placed times, per
  GPU: barrier releases, the order of a grid-wide atomic ticket, and when the CPU saw the done-flag. There were 0
  violations. The ticket check confirms the one-timer assumption across SMs only above ~0.2–0.5 µs. Nothing yet checks
  alignment between GPUs.

## 4. What we found

### 4.1 Host time is not kernel time

![Where the time goes between CPU and GPU](figures_2026-10-08/where_time_goes.png)

These are medians of 4–5 warm launches of our instrumented probe kernel, one host per GPU type (8 Oct):

| | A100 | H100 |
|---|---|---|
| Launch call to `cudaStreamSynchronize` returning | 17.3 µs | 12.6 µs |
| of which warps ran | 3.5 µs | 2.3 µs |
| system fence after the done-flag store (inside the kernel time) | 2.85 µs | 1.74 µs |
| Launch to first warp, warm | 5.1–6.8 µs | 4.6–5.6 µs |
| Launch to first warp, after 50 ms of host sleep | 9.8 µs | 24–32 µs |
| First launch of the kernel in a process | 24–39 µs | 40–60 µs |

- **Where the extra time goes.**
  - The idle penalty and most of the first-launch cost are spent inside the host's launch API call. The GPU does not
    start later once the call returns.
  - Host sleep and GPU idle were not separated.
  - The first-launch values are one sample per process.
- **Polling the done-flag.**
  - The last block stores its done-flag *before* its system fence. A CPU polling that flag sees it 6.5 µs (A100) or
    4.4 µs (H100) before `cudaStreamSynchronize` returns, but the kernel has not finished at that point.
  - With the fence placed before the flag, the lead would be about 3.7 / 2.7 µs. That is an estimate, not a
    measurement.
- **Confounds.** A100 and H100 differ in host CPU, driver and SM clock. Each split point carries the run's clock bound
  (±0.8–0.9 µs on A100, ±0.7 µs on H100).

### 4.2 Inside a kernel

![Where a warp's cycles go](figures_2026-10-08/corrected_2026-10-09/kernel_phases.png)

**Phase costs.** These are cycles per warp, with one block of 256 threads per SM (CUDA 12.6). Every phase except the
atomic ticket is checked in SASS.

| Phase | A100 | H100 |
|---|---|---|
| 256 dependent FFMA | ~1,030 | ~1,030 |
| store + GPU-scope fence | 628 | 1,534 |
| system-scope fence after the done-flag store | 3,056 | 3,374 |

On the 9 Oct H100 host the system fence cost 2,156 cycles, and on the 8× A100-PCIe host 2,405–2,583 cycles (about
3.0–3.6 µs at its 0.72–0.76 GHz SM clock). Fence costs depend on the host, the driver and the store target.

**Latency per instruction**, in cycles (8 Oct dependent chains):

| Instruction | A100 | H100 |
|---|---|---|
| FFMA, FADD, IMAD | 4 | 4 |
| shared-memory load | 23 | 23 |
| warp shuffle | 26 | 26 |
| L1 hit | 39 | 39 |
| L2 load (1 MB set) | 282 | 283 |
| DRAM load, misses only (128 MB set) | ~541 | ~683 |

Load latency per line is bimodal on the 9 Oct machines:

| | L2, near / far | DRAM, near / far |
|---|---|---|
| A100 | 220 / 374 | 493 / 645 |
| H100 | 280 / 472 | 572 / 774 |

**Crowding.**
- **Residency.** At most 3 blocks of 256 threads were resident per SM. This limit comes from the probe's own 80
  registers per thread, not from the hardware.
- **A100 FP32 pipe.** With 3 resident blocks, A100 blocks take turns on the FP32 pipe: the first, second and third
  block on each SM run at 4, 8 and 12 cycles per FFMA. This matches the A100's 16 FP32 lanes per scheduler. On H100,
  86–90% of warps stay at 4.
- **Code size.** Warm straight-line code up to 64 KB runs at full speed with one block per SM. Its first execution
  costs a few hundred cycles more.

### 4.3 Eight GPUs on one host clock

![8 GPUs on one host clock](figures_2026-10-09/multi_gpu_instruction_timeline.png)

**Setup.**
- Eight A100s in one host, one process per GPU, each with its own clock sync.
- All processes launched the same kernel (108 blocks × 256 threads) on a shared 2 ms grid of the host clock.
- The figure draws every block's warp 0 phase by phase on one host axis, each GPU with its bound.
- The SM clock ran at about 0.76 GHz in this run.

**Results, over 40 shared launch instants.**
- **Launch calls.** The eight launch calls were made within **30 ns** of each other (median).
- **Start spread.** The estimated kernel starts spread by **0.78 µs** (median). At any single instant this is smaller
  than the error bars, so the size of the spread is not resolved. But for every GPU pair the start offset changed
  between instants by more than the stamp errors allow, so the starts were not simultaneous.
- **Per-GPU bound.** Each GPU's position on the host axis is known to ±0.85–1.2 µs.
- **Provable order.** The start order of two GPUs at one instant is provable only for gaps above **~1.7–2.3 µs**
  (about 1.66 µs with exact intervals). That held for 11 of 1,120 pairs.

**What this means.**
- **What compares exactly.** Phase durations, and positions relative to each GPU's own kernel start, compare exactly
  across GPUs.
- **What does not compare yet.** Absolute positions on two GPUs can be ordered only when they are more than ~1.7–2.3 µs
  apart. That is longer than every phase (0.05–1.35 µs in this run), so a phase-by-phase cross-GPU comparison is not
  yet possible.
- **Where the threshold comes from.** It comes from this sync method on this host (the syncs were 16 s apart), not
  from the host clock itself.
- **Not checked.** The checks are per GPU. Alignment between GPUs, and one host clock across the two CPU sockets, are
  not tested.

### 4.4 Instruction reordering: the rules, tested on hardware

GPU machine code (SASS) carries its own timing. The compiler writes a stall count and scoreboard waits in front of
every instruction, and the hardware does not re-check dependencies. Moving an instruction without updating these
codes silently gives wrong results. We encoded five rules in a legality checker, and timed or violated them on the GPU.

**Rule 1: a load stalls only at its first use.**
- What the hardware does: independent work placed between a load and its use runs while the load is in flight.
- Measured (A100 / H100, CUDA 12.6), for each load:
  - Time follows max(L, 4N + d). The break-even is within 1.5 FFMA of (L − d)/4 for each latency class.
  - Hoisting a DRAM load ahead of enough work saves about its latency minus d: about 460–615 cycles on A100 and
    540–745 on H100.
  - In hand-edited SASS, the time stays flat while the load is hidden, then rises 4 cycles per slot.
- Correction: the first version's group-median numbers were line-mix artefacts.

**Rule 2: a store reads its registers late.**
- What the hardware does: overwriting a register that a store has not read yet makes the next instruction wait.
- Measured: at 1 warp, 0–11 cycles, measured to about ±6. The 32-warp numbers are confounded by other differences
  between the variants.

**Rule 3: results need their stall cycles.**
- What the hardware does: a dependent instruction issued too early reads the old register value.
- Measured:
  - Below the minimum stall, every link read a stale register in every launch.
  - FFMA results were wrong in 200 of 200 runs.
  - IADD3 results were right in 192 of 200 runs only because the register still held the value the same kernel had
    left there, with the same input.

**Rule 4: a barrier blocks memory, not arithmetic.**
- What the hardware does: after `BAR.SYNC.DEFER_BLOCKING` (CUDA 12.6), a warp keeps issuing instructions until its
  first memory instruction.
- Measured:
  - Register-only arithmetic after the barrier costs nothing while the warp would otherwise wait. Work that touches
    shared memory costs its full length.
  - With CUDA 12.2's plain `BAR.SYNC`, register-only work costs its full length too.
  - Moving the slowest warp's arithmetic past the barrier does **not** make the block finish sooner.

**Rule 5: fences and memory order.**
- What the hardware does: no instruction moves across a fence, and async copies keep their order.
- Measured, in one thread with one 4-byte store:
  - A fence stalls its warp for a fixed 410 / 682 cycles (GPU scope) and 2,277 / 1,252 (system scope).
  - Up to 1,024 FFMA of drain time before the fence change this by at most 8 cycles.
  - Hiding by other warps was not tested.

**Checker against hardware.** Thirty edits to real A100 SASS were each run 200 times.
- **Agreement.** The checker's verdict matched the hardware on 26 of 30.
- **Violations.** It refused all 13 deliberate violations. Nine broke the output. Four ran correctly, so there the
  checker was stricter than needed.
- **Approvals.** It approved 17 slides of one load, and all of them ran correctly.
- **Scope.** Five small test kernels, one A100, one fixed input. The approvals have not been tested on edits close to
  a hazard.
- **Testing lesson.** Every broken edit that sometimes passed failed on its first, cold launch. A test that warms up
  and repeats one input would miss them. A cold launch, a register scrub, or a fresh input on each launch catches them.

**Throughput limit (E5).** Cycles per FFMA follow max(4 / ILP, p × warps per scheduler), with p = 2 on A100 and
p = 1 on H100. With dependent chains, the FP32 pipe fills at 2 warps per scheduler on A100 and 4 on H100.

## 5. Did we learn how to make kernels faster by reordering?

**The rules, in part. A faster kernel: yes, on one microkernel as predicted (5.1) and on eight production kernels
(5.2), by one transform that is now automatic for CUDA code.**

What the data show:

1. **The rules hold where we tested them.** On five small test kernels, the checker refused every violation we tried
   and approved only edits that ran correctly. Several rules were never violated: fences, branches, real memory
   aliasing, and the store-register hazard.
2. **Latency hiding follows the model for each load:** free until the independent work covers the load's latency,
   then 4 cycles per FFMA.
3. **Where hiding cannot help.**
   - A fence stalls its own warp for a fixed time that the work around it does not hide.
   - Once a few warps compete, the FP32 pipe is full: at 2 warps per scheduler on A100 and 4 on H100.
4. **One free slot.** Register-only work placed after a CUDA 12.6 barrier runs while the warp waits.

What the earlier experiments (E1–E7 and Tier B) do not show is **any kernel made faster than the compiler made it**
(section 5.1 shows one, on a microkernel):

- **Tier B could not show a gain, by design.** It only slid one load later, in a kernel that already issues the load
  first.
- **E1's big savings** are measured against an order we forced to be bad.
- **The barrier move** made the block slightly slower.
- **A fresh register** saved nothing measurable at 1 warp.
- **CuAsmRL** reports speed-ups from reordering ptxas's SASS for some kernels. We have not reproduced that.

So the earlier experiments alone did not support "we found how to optimise kernels by hiding execution under load
time". The proof experiment below does, for one microkernel.

### 5.1 Proof: a reordering that beats the compiler (10 Oct, A100)

Each loop iteration loads one value per thread (L2) and runs a chain of N dependent FFMA that starts from it.

| Cycles per iteration, A100-PCIe, 1 warp per SM | compiler, `#pragma unroll 4` | ours: next group's loads hoisted | speedup (kernel time) | predicted saving | measured saving |
|---|---|---|---|---|---|
| N = 16 | 149.1 | 120.9 | 1.24× | 32 | 28 |
| N = 64 | 248.0 | 170.7 | 1.46× | 97 | 77 |
| N = 128 | 397.8 | 297.5 | 1.34× | 97 | 100 |
| N = 128, 16 warps per SM | 1,071.2 | 1,059.2 | 1.02× | ~0 | 12 |

- **What the SASS shows.** The compiler issues the 4 loads of a group back to back, but the next instruction already
  needs the first one, so the warp stalls about 390 cycles per group. It did not move any load across the loop branch.
  Ours issues the next group's loads before this group's 4 chains, so the wait runs under them.
- **Prediction** from measured costs: saving per iteration = min(L, 8N) / 4, with L ≈ 390 cycles (this loop's own
  load wait, measured at N = 0 in the first run: 377–392 cycles) and 8N = 4 chains × N FFMA × 2 cycles of A100 issue.
  With 16 warps per SM, other warps already hide L, so with L2-resident data the gain vanishes, as predicted. With
  DRAM-resident data (512 MB set) short chains still gained: 1.29× at N = 16, 1.10× at N = 64, 1.03× at N = 128.
- **Checks.** Outputs are bit-identical in all 96 configurations. Medians of 7 launches. The speed-up column is the
  ratio of kernel times; the cycle counts give the same ratios to within about 0.01.
- **Limits.** One microkernel, one A100, CUDA 12.6, L2-resident data. The move was written in source (it crosses the
  loop branch, which our basic-block checker cannot judge), so correctness rests on output comparison.
- Code, results and SASS: `tickbound_runs/2026-10-10_reorder_proof/`.

### 5.2 The same transform on eight production kernels (12–16 Oct, A100 and H100)

FINDINGS section 9 has the full tables. Ratio = original kernel time / reordered kernel time; every reordered output
was byte-identical to the original's.

| kernel | type | hand reorder vs compiler (median, wins) | automatic pass (median, wins) |
|---|---|---|---|
| FAISS `l2SelectMinK` / `Min1` | search | 2.14 H100 (70/70), 2.66 A100 (70/70) | 2.51 (70/70) |
| Rodinia particlefilter normalize / find_index | scan / search | 3.58 / 2.51 H100, 3.00 / 2.65 A100 (all) | 2.99 / 1.21 (all) |
| PyTorch `EmbeddingBag` | gather | 1.11 H100, 1.46 A100 (31/31) | 1.12 (24/31) |
| Kernl RMSNorm (Triton 2.2 PTX) | normalisation | 1.23 H100 (35/37), 1.31 A100 | 1.23 (5/5) |
| llama.cpp `rms_norm_f32` | normalisation | 1.16 H100 (75/80), 1.22 A100 | 1.07 (7/9) |
| NVIDIA Aerial `cfoTaEst` | 5G PHY | 1.19 H100 (20/22), 1.18 A100 (22/22) | 1.00 (predicated loads not handled) |
| Kernl fused FF (= CuAsmRL `tt_ff`) | matmul + activation | 1.22 vs Triton 2.2 best config (45–48/48) | none by design |

- **Against Triton.** Triton pipelines only `tl.dot` loads. Versus Triton 3.8's best config on fused FF: A100 1.06
  (34/48), **H100 0.99 (23/48)**: we win warm cases and the DRAM-bound decode shape (1.9×, and the probe shows why), and
  lose cold small-M cases to its `cp.async` pipeline. The automatic pass on Triton 3.x libraries (Liger, FlagGems,
  ~100 kernels) transforms no loop and gives median 1.00; only `.nc` marking acts (12 of 97 cases, 1.03–1.17×).
- **Against CuAsmRL.** In its action space (memory moves inside a basic block), with byte-compared outputs and
  CUDA-graph timing, the best gain on its six kernels is 1.022×. Its own timing method reports 1.08–1.33× for unchanged
  kernels, so its 2–26% claims lie inside its noise. A head-to-head with its trained cubins was not run.
- **Where hand still beats automatic.** Tricks that are not reorders (a bit mask in find_index), hoists across a loop
  and a barrier (llama.cpp), predicated in-loop loads (Aerial), and the unroll width, which must be measured per loop:
  `tickbound reorder-tune` now builds eight candidates, bit-checks and times each, and picks per case.

What is supported:
- **A measurement method.** We can measure what a reordering does, with stated error bars, down to the instruction.
- **The rules.** We know the rules that keep a reordering correct, tested on small kernels and by output comparison
  on real ones.
- **The costs.** We measured what each kind of move costs.
- **A transform that pays.** Loads issued a group ahead beat ptxas on every real kernel tried, and the pass does it
  automatically for CUDA code. Modern Triton already does it for `tl.dot` loops, and there we do not add to it.

## 6. What is new, and what confirms known results

**Not found in the work we checked.** We checked NVIDIA's documentation and forums, Tasnadi, CuAssembler, CuAsmRL,
maxas, the microbenchmark papers on Volta, Turing, Ampere and Hopper, the intra-kernel tracers above, and TempoTrace.
A full literature review is still to do.

1. **A stated error bound on every in-kernel checkpoint, across GPUs** (hard under the named assumptions; H100
   placement across SMs and widened fits are empirical).
   - Each event comes from timer · cycle · timer brackets and is mapped onto the host clock with a strict bound, for
     several GPUs on one host clock.
   - Other intra-kernel tracers place per-warp events on `%globaltimer` without a stated bound. NVIDIA IKET states
     that multi-GPU traces are not aligned.
   - The bound is hard for kernel timing under the named assumptions.
2. **A fence's cost does not shrink when the store before it has time to drain.** It changed by at most 8 cycles with
   up to 1,024 FFMA in between, in one thread with one store.
3. **On the barrier.**
   - With `BAR.SYNC.DEFER_BLOCKING`, register-only work after `__syncthreads()` costs nothing while the warp waits.
     With CUDA 12.2's plain `BAR.SYNC`, it costs its full length.
   - NVIDIA does not document these semantics.
   - Moving such work across the barrier is correct on hardware (200 of 200 runs, one kernel).

**Confirms known results:**
- **The H100 timer.** `%globaltimer` steps every 32 ns (Fusco et al. 2024; NVIDIA IKET documentation). Our data
  confirm it. The first version of this README misread our sync loop's 64/96/128 ns gaps as timer steps.
- **Latency hiding** with independent work (Volkov, GTC 2010).
- **The control-code rules:**
  - stall counts and scoreboards (maxas; Jia et al. 2018; CuAssembler; CuAsmRL);
  - stall violations fail non-deterministically (maxas);
  - IMAD.WIDE takes extra issue cycles (NVIDIA forum, 2023).
- **The FP32 pipe width:** 16 lanes per scheduler on A100, 32 on H100.
- **Launch and completion overhead** of several µs per kernel.
- **Cross-GPU ordering.** With our host-clock sync on 8×A100-PCIe, two GPUs could be ordered only when more than
  ~1.7–2.3 µs apart (each ±0.85–1.2 µs). Like for like, that is about half TempoTrace's pair threshold for its
  software fallback (2 × 2.1 µs = 4.2 µs) and 4–5× its 0.44 µs pair threshold with hardware (GTE) timestamps.

## 7. Limits

- **Clocks.** Each run uses one host and its host clock, not TAI, with no external reference clock. All checks are
  internal and per GPU.
- **The rate assumption.** Bounds are hard if the GPU/host rate is constant between the two syncs. That holds in
  practice for syncs up to 0.26 s apart. In the 8-GPU run (syncs 16 s apart) the events sit within 0.17 s of a sync,
  so a rate change would add at most ~50 ns. It is not established for the 8 Oct instruction / co-tenant / MPS runs,
  whose syncs were 7–32 s apart.
- **Across SMs.** Placement across SMs assumes all SMs read one `%globaltimer`, which is checked only above
  ~0.2–0.5 µs. H100 placement across SMs is empirical.
- **Kernels and machines.**
  - Sections 4 and 5.1 use our own probes and microbenchmarks. Section 5.2 uses eight production kernels, each on one
    GPU per run; the automatic pass ran on A100 only.
  - The kernel-timing probe carries its own instrumentation, and there is no uninstrumented control.
  - The 8 Oct samples are small.
  - The machines are rented containers, and A100 and H100 ran on different hosts and drivers.
- **Reordering.**
  - The fused FF comparison against Triton 3.8 is a loss over all shapes (median 0.99 on H100); the win is confined
    to the DRAM-bound decode shape.
  - The automatic pass does not match Triton 3.x loop shapes, predicated in-loop loads or cross-loop hoists.
  - The Aerial `rssi` harness crashed and has no data.
  - CuAsmRL was not run head-to-head.
- **Open items.**
  - Re-analyse H100 placement across SMs at the 32 ns step.
  - Redo E1 with both orders on the same lines.
  - Repeat the Tier B runs with cold and warm launches and fresh inputs.

## 8. Next steps

1. **Extend the pass** to Triton 3.x loop shapes and predicated loads, and run it on H100; then the Aerial `rssi`
   harness fix and a CuAsmRL head-to-head (~$8) if the comparison is wanted.
2. **Cheap reruns, under $2 in total.**
   - E1 with both orders on the same lines.
   - Tier B with per-launch records, a register scrub, fresh inputs, and cold and warm launches.
   - A run of the same kernel without our timing code, as a control.
   - A direct SM-to-SM timer-skew test.
   - Clock syncs placed next to the launch burst.
3. **Re-analysis, no GPU.** Use the H100's 32 ns step, compute bounds at the event times, and give exact per-pair
   verdicts across GPUs.
4. **Stamps anywhere, automatically.** Insert timer · cycle · timer reads into any compiled kernel, using NVBit for
   closed-source binaries. Position this against Xtrace and NVIDIA IKET.
5. **A common reference clock across hosts** (PTP hardware timestamps, as TempoTrace proposes), to order events below
   ~2 µs and across machines.

## 9. Repository

| Path | Contents |
|---|---|
| [FINDINGS.md](FINDINGS.md) | full results, all tables, limits and the list of corrections |
| `figures_2026-10-08/` | 8 Oct figures (A100, H100). `corrected_2026-10-09/` holds the corrected versions |
| `figures_2026-10-09/` | the 8-GPU timeline (PNG, SVG and its data), per-instant results and the ordering rules |
| `tickbound_data/` | per run: metadata, analysis, log and SASS check results; reports and gzipped SASS per run set. Also strict bounds and the summary for all runs |
| `tickbound_runs/2026-10-09/` | the scripts that ran on the rented machines and locally, and two patches |
| `tickbound_runs/2026-10-10_reorder_proof/` | the reorder proof (section 5.1): source, on-box script, log, results and gzipped SASS |
| `tickbound_runs/2026-10-12_*` … `2026-10-16_*` | the real-kernel runs (section 5.2 / FINDINGS 9): one `SUMMARY.txt` per run, results CSV / JSON, scripts, figures, the 16 Oct `report.html` and `picks.csv`, and the 15 Oct claims page as PDF |
| `code/`, `data/`, `demo/`, `gpu_run/`, `storyboard/`, `GPU_Clock_Findings.pptx` | earlier feasibility work (September 2026), from before tickbound |

The raw traces, probe dumps, cubins and SASS listings are kept out of git because of their size. tickbound's source
code, the eight kernel harnesses (`bench_real/`), the automatic pass and the probe tools are in a separate repository
that is not yet published, so the run scripts cannot yet be run from this repository alone. The 10 Oct reorder proof
needs only the CUDA toolkit.

## 10. References

- E. Tasnadi, "Nanobenchmarking: cycle accurate benchmarking of CUDA kernels", Core Velocity Lab, 3 Dec 2025:
  https://corevelocitylab.com/posts/nanobenchmarking-cycle-accurate-benchmarking-of-cuda-kernels/
- TempoTrace, Elbakoury and Sharma, arXiv:2609.23301 (unreviewed white paper; its GPU timestamp figures are design
  targets): https://arxiv.org/abs/2609.23301
- L. Fusco et al., "Understanding Data Movement in Tightly Coupled Heterogeneous Systems: A Case Study with the Grace
  Hopper Superchip", 2024, arXiv:2408.11556 (H100 `%globaltimer` resolution 32 ns): https://arxiv.org/abs/2408.11556
- Intra-kernel tracers: Neutrino (OSDI 2025); Triton Proton intra-kernel profiling (2025) and KPerfIR (OSDI 2025,
  arXiv:2505.21661); NVIDIA IKET (CUTLASS documentation); TVM CudaProfiler; Xtrace (arXiv:2609.28769, 2026)
- CuAssembler: https://github.com/cloudcores/CuAssembler
- G. He and E. Yoneki, "CuAsmRL: Optimizing GPU SASS Schedules via Deep Reinforcement Learning", CGO 2025,
  arXiv:2501.08071: https://arxiv.org/abs/2501.08071
- Z. Jia, M. Maggioni, B. Staiger, D. P. Scarpazza, "Dissecting the NVIDIA Volta GPU Architecture via
  Microbenchmarking", arXiv:1804.06826: https://arxiv.org/abs/1804.06826
- V. Volkov, "Better Performance at Lower Occupancy", GTC 2010.
- NVIDIA PTX ISA, special registers `%globaltimer` and `%clock64`: https://docs.nvidia.com/cuda/parallel-thread-execution/
- NVIDIA Aerial CUDA-Accelerated RAN: https://github.com/NVIDIA/aerial-cuda-accelerated-ran

# kernl_fused_ff: does load reordering beat Triton's own schedule?

Kernel: Kernl's LLaMA-2 fused RMSNorm + SwiGLU up-projection, `out = silu(rmsnorm(x) @ W1^T) * (rmsnorm(x) @ W3^T)`
(ELS-RD/kernl `experimental/llama-v2/kernel/fused_kernel_ff.py`, Apache-2.0), in the form CuAsmRL (He & Yoneki,
CGO'25) benchmarked and optimised it as `tt_ff` and reported x1.155 on. Question asked: does our reordering apply to
Triton, and is Triton better than it?

## Honest framing

* Triton is a compiler, and it already does what we do for the loads it understands: `num_stages` software-pipelines
  every load whose only use is a `tl.dot` operand (W1 and W3 here) into `cp.async` (LDGSTS) a few iterations ahead.
* Triton 2.2 (CuAsmRL's) does not pipeline loads that feed elementwise code before the dot. In this kernel the x tile
  (`a = tl.load`, squared for the RMS sum and multiplied by `rms_w`) and the RMSNorm weight `rms_w` are such loads:
  they are register loads (LDG.E.128) at the top of the K loop, and the first consumer (`HMUL2`, a * rms_w) waits for
  them 12-27 issue cycles later in the sweep's tiles (43-87 in the 128-row tiles and the sm_90 HGMMA builds), i.e. a
  full L2 round trip per iteration with 1 warp per scheduler at CuAsmRL's shape. Triton 3.2 (PyTorch 2.6's)
  pipelines the x tile too, except in its sm_90 HGMMA builds (64x128, 128x32, 128x64 tiles), but still leaves `rms_w`
  as an in-loop LDG; its in-loop LDGs are consumed 5-77 cycles later.
* **Triton 3.8.0 (the current release, Aug 2026; compiled here without a GPU like the others) pipelines both**: no LDG
  is left in any hot loop of any config on either architecture; the x tile and `rms_w` go through cp.async like W1 and
  W3 (one more LDGSTS per iteration than 3.2, three more in the HGMMA builds where 3.2 kept the x tile in registers). So
  "Triton leaves these loads exposed" is true for Triton <= 3.2, not for the current release. Triton 3.8's schedule is
  timed as variant `tt38`: it is Triton's own, deeper (num_stages, shared memory) answer to the problem our reorder
  solves by hand (1 iteration, registers). A register prefetch of `rms_w` on top of 3.8 (`ff_ro_rms`) was compiled and
  dropped: it puts an LDG back into the loop.
* Our reorder targets exactly the exposed loads: one-iteration software pipelining written in the Triton source
  (`ff_ro`), same arithmetic and accumulation order, so the output must be bit-identical.
* CuAsmRL got x1.155 on this kernel with single-slot swaps of memory instructions inside a basic block. The loads sit
  at the top of the loop body, so no in-block move can hide them; only a cross-iteration move can.
* So the comparison is not "Triton vs us": `orig` is Triton 2.2's schedule, `ctl_s2` / `ctl_s5` / `tt32` / `tt38`
  show what Triton's own knobs and newer Tritons buy, `ro` / `ro_clamp` / `ro_tt32` / `ro_full_tt32` show what our
  reorder adds, and the baseline entries (`ro_vs_tt32`, `ro_vs_tt38`, best-of-configs) score "is Triton better than
  our reorder?" directly (below).

## The answer the measurement will check (predicted before any GPU run)

At CuAsmRL's shape (M=N=512, K=1024), 7 configs per GPU, `predictions.json`:
* Our reorder vs Triton 2.2 (`ro`): predicted faster for 3 of 7 configs warm on each GPU and 5 / 7 of 7 cold
  (A100 / H100); x1.20-1.69 for the two 64x32 tiles (both GPUs, warm and cold), 1.40-1.69 A100 warm for
  CuAsmRL's likely winner 64x32x32_w2_s5.
* Our reorder on 2.2 vs Triton 3.2's own schedule (`ro_vs_tt32`): faster for 3 / 6 of 7 warm, 6 / 7 of 7 cold.
  Triton 3.2 does not fix the problem: `tt32` vs orig is 0.53-1.21, below 1 for 4 of 7 configs on H100.
* Current Triton 3.8 vs our reorder (`ro_vs_tt38`): ours is predicted SLOWER for 6 of 7 configs on A100 and 4 of 7 on
  H100 (warm), never faster on A100; Triton 3.8 pipelines the same loads itself, num_stages deep and without the
  register cost. Autotuned against autotuned (`ro_bestcfg_vs_tt38`): 0.72-0.84 (A100 warm), 0.60-1.19 (H100 warm).
So the expected answer to "does it apply to Triton, and is Triton better?": it applies to Triton <= 3.2, which leaves
these loads exposed and which our reorder beats; the current Triton already does it, and is predicted to be better.
The bench measures all three, so the answer will not rest on the model.

## Variants (one row each per case in the results CSV)

| variant | what | built from | output must equal |
|---|---|---|---|
| `orig` | Kernl's kernel as CuAsmRL benchmarked it (`tt_ff`, verbatim from cuasmrl@fed7fb14 `benchmarks/fused_feedforward.py` 140-228), at the case's config | Triton 2.2.0 | - |
| `ro` | `ff_ro`: x tile and `rms_w` of iteration k+1 loaded at the top of iteration k into fresh variables (masked off on the last iteration), rotated at the end | Triton 2.2.0 | orig (bitwise) |
| `ro_clamp` | `ff_ro_clamp`: the same prefetch without a mask (offset 0 on the last iteration re-reads the current tile), issued after the current tile's last use | Triton 2.2.0 | orig (bitwise) |
| `ctl_s2`, `ctl_s5` | `orig` compiled with num_stages 2 / 5: Triton's own pipeliner, shallow and deep (= orig when the case's config already has that stage count: an A/A null test) | Triton 2.2.0 | orig (bitwise) |
| `ctl_r64` | `orig` 16x16x64_w4_s2 with `.maxnreg 64` in its PTX: the register drop `ro` gets on sm_90 (67 -> 64, 7 -> 8 CTAs/SM) without any reorder (occupancy control) | Triton 2.2.0 | orig (bitwise) |
| `kernl` | Kernl's text verbatim (`ff_llama`: ungrouped program order, `tl.math.pow(a, 2)`) | Triton 2.2.0 | informational: pow gives mul + add where `a * a + a_sum` contracts to FMA, so not expected bit-identical |
| `tt32` | `tt_ff` compiled by Triton 3.2.0 (pipelines the x tile except in sm_90 HGMMA builds) | Triton 3.2.0 | informational (other compiler) |
| `ro_tt32` | `ff_ro_rms`: Triton 3.2 + our prefetch of `rms_w` only | Triton 3.2.0 | tt32 (bitwise) |
| `ro_full_tt32` | `ff_ro` (x tile + `rms_w`) compiled by Triton 3.2, for the tiles whose sm_90 HGMMA build leaves the x tile exposed (64x128, 128x32, 128x64) | Triton 3.2.0 | tt32 (bitwise) |
| `tt38` | `tt_ff` compiled by Triton 3.8.0 (pipelines the x tile and `rms_w`; PTX ISA 8.5 so that ptxas 12.6 takes it; two hidden scratch-pointer parameters, size 0, passed as null) | Triton 3.8.0 | informational (other compiler) |

All in `src/fused_ff_kernels.py`; lines that differ from `tt_ff` are marked `ro:`. Legality: the kernel only reads
x, rms_w, W1, W3 and writes `out` (a fresh buffer), so issuing a read one iteration earlier cannot change its value.
Every bitwise pair has the same PTX arithmetic (mma.sync / wgmma shapes and counts, fma, f16x2 mul, ex2, rcp...):
only loads, address math and unpack moves differ (checked for all 50 pairs, including the new configs).

## Configs and cases

Tile configs (`BLOCK_M x BLOCK_N x BLOCK_K, warps, stages`), all from CuAsmRL's 10-config autotune list:
* all variants: the 2-warp configs of the sweep `64x32x32_w2_s5`, `32x64x32_w2_s5`, `64x32x32_w2_s2`; the 4-warp
  `64x128x32_w4_s4`, `128x32x32_w4_s4`, `128x64x32_w4_s4` (about 64 and 128 accumulator registers per thread: plausible
  autotune winners); Kernl's own decode config `16x16x64_w4_s2` (CuAsmRL's "origin"). Controls: num_stages 2 and 5 of
  the first five tiles (3 and 2 extra builds).
* `orig` only: `128x256x64_w8_s3`, `64x256x32_w4_s4`, `128x128x32_w4_s4`. Their two fp32 accumulators need ~256
  registers per thread; with ptxas 12.6 they spill 1.1-13 KB per thread (sm_80 128x256 / 64x256 fall to 32 registers
  and spill nearly everything). They are measured so that "Triton's autotuned best" covers all 10 configs.
* **Every build compiled**: 72 Triton 2.2 + 34 Triton 3.2 + 14 Triton 3.8 PTX (120 builds), sm_80 and sm_90a, all
  through ptxas 12.6.77; spills only in the three orig-only configs, `tt38` 128x64 (8 / 12 B) and `ctl_r64` sm_90
  (4 B) (`sass/sass_report.md`).

Cases (`src/cases.tsv`, 280), each in L2 states `warm` and `cold`:
* the first five tiles: 24 shapes = CuAsmRL's M=N=512 with K=1024 (script default) and K=2048 (paper table),
  M in {16, 64, 128, 256, 1024} x N in {1024, 4096} x K in {1024, 4096}, and LLaMA-2-7B's real up-projection
  N=11008, K=4096 at decode M=16 (Kernl's own launch) and prefill M=512 (240 cases);
* 128x32, 128x64 and the three orig-only tiles: CuAsmRL's two shapes and the two LLaMA shapes (40 cases), so that at
  those four shapes all 10 autotune configs are measured (best-of-configs below).
The grid goes from 1 to 22,016 CTAs, so residency, waves and DRAM / L2 traffic vary. L2 `warm` = back-to-back
launches; `cold` = L2 flushed before every launch, as `triton.testing.do_bench`, CuAsmRL's timer, does. Inputs: fp16,
fixed seeds, CuAsmRL's benchmark magnitudes (x = randn, rms_w = randn x 0.2, W1, W3 = randn x 0.2; W stored [N, K] as
nn.Linear and read transposed, as Kernl does; masters 1024 x 4096 and 11008 x 4096, each case a top-left block). M, N,
K are multiples of 16 everywhere, which is the specialisation every PTX was compiled for (`divisibility 16`, unit
strides folded).

## How the PTX was made (no GPU)

`tools/gen_ptx.py` (in WSL): pip `triton==2.2.0` in `cuasmrl/tools/venv_tt22` with a 10-line `torch` stand-in
(`cuasmrl/tools/stubs/torch`) so Triton imports without PyTorch or a GPU; the compile stages are called one by one
(AST -> TTIR -> TTGIR (`optimize_ttgir(num_stages, num_warps)`) -> LLIR -> PTX ISA 8.2), skipping the launcher stub
that needs libcuda, with the specialisation `JITFunction._get_config` computes for the real launch arguments (the
sweep's `compile_tt.py`). Triton 3.2.0 (`venv_tt32`) runs `triton.compile(ASTSource, GPUTarget)` directly. Triton
3.8.0 (`venv_tt38`, `--tt38`) does the same with the specialisation `JITFunction.run` computes (`native_specialize_impl`
per argument) and `ptx_version=85`. Kernel parameters left at run time: the 5 pointers, M, N, K, stride_am,
stride_w1n, stride_w3n, stride_outm (+ 2 scratch pointers for 3.8) (`src/ptx/*.json`). `tools/make_trace.py` copies
them to `src/ptx/`, writes the trace builds and `src/manifest.tsv`; `tools/sass.sh` compiles every PTX with ptxas
12.6.77 (Triton's flags: `-lineinfo -v --gpu-name=sm_80 | sm_90a`) into `sass/` and `local/cubin/`. `local/gen.sh`
reruns all of it (without `venv_tt38` it reuses the 3.8 PTX in `local/triton_build_tt38`). Note: pip Triton itself
would run its bundled ptxas (12.3 for 2.2, 12.4 for 3.2, 12.9 for 3.8); here every variant goes through the same CUDA
12.6 ptxas, so the A/B is fair, but absolute times can differ from a pip-Triton run.

## On the box (CUDA 12.x toolkit for nvcc + cuobjdump; the box needs no Triton or PyTorch)

Upload the whole directory **including `local/cubin/`** (34 MB: the ptxas 12.6.77 cubins, used only if the box cannot
get that ptxas), but not `local/triton_build*` / `local/exp`.
```
./build.sh          # nvcc -O2 -std=c++17 src/harness/ff_bench.cpp -lcuda (driver API, host code only) + selftest;
                    # ptxas PINNED to 12.6.77 (toolkit's, else pip wheel nvidia-cuda-nvcc-cu12==12.6.77 into
                    # build/pin, else local/cubin, else exit 4) -> build/cubin/*.cubin for this GPU's arch;
                    # SASS -> build/sass/; check_trace_sass.py; any hot loop that differs from sass/ (the SASS the
                    # predictions were computed from) stops the build (exit 4)
QUICK=1 ./run.sh    # smoke subset (CuAsmRL's shapes for all 10 configs + one large case, 7 reps), < 1 min;
                    # writes results/quick, traces/quick (summarize.py never reads them)
./run.sh            # all 280 cases on this GPU (A100 / H100 from nvidia-smi); model estimate of the measuring time
                    # (harness loops replayed on the predicted kernel times): A100 ~2.5 min, H100 ~2.2 min
```
The harness loads the cubins built on the box (Triton loads cubins too; `--allow-jit` would load the PTX instead and
is off). `run.sh` refuses to start unless `predictions.json` matches `predictions.json.sha256` (frozen before any GPU
run, QUICK=1 included), and records the SHA-256 in the env JSON.

Measurement rules (`src/harness/ff_bench.cpp`):
* correctness first: `out` of every variant (plain and trace build) is poisoned (0xFFFF) before its check launch,
  must be fully overwritten, and is `memcmp`ed against its reference (table above) and against orig; the trace build's
  output must equal the plain build's (else it counts as a mismatch and its span never reaches the shared CSV); orig
  is also checked against a float64 CPU reference at 34 points (rel. err <= 2e-2); the shared CSV's `bitwise_equal`
  and `max_abs_diff` are both against the row's own reference (the extra CSV also has the max difference vs orig);
* warm timing: one CUDA graph of B back-to-back launches per variant (B so that a graph runs >= 2 ms, 3 <= B <= 200),
  events around the graph, 21 batches, each in its own Fisher-Yates-shuffled variant order (seed hashed from
  `--order-seed` and the batch, recorded in the env JSON): cancels clock drift, position and predecessor effects;
  `mean_us` = graph time / B; median, p10, p90 over the batches;
* cold timing: L2 flush (memset of 2 x L2 size) before every launch, outside the events; 5 launches per batch,
  21 batches, shuffled orders;
* trace build: two stamps per warp (%globaltimer + %clock64 at kernel entry and before `ret`), nothing in or next to
  the K loop; 11 runs per variant (shuffled); device span = first warp entry to last warp exit with each SM's clock64
  placed on the globaltimer axis; the median-span run goes to `traces/` for CuAsmRL's shapes and the largest decode
  shape; the trace build is also timed (extra CSV `trace_vs_timing`);
* the GPU must be the modelled one: A100-PCIE-40GB (108 SMs) and H100 80GB HBM3 (SXM5, 132 SMs). Another part (H100
  PCIe 114 SMs, A100 SXM) is measured but flagged (`model_sms_match` / `model_name_match: false` in the env JSON and a
  warning): the 16x16 wave-quantisation predictions and the DRAM floors do not hold there;
* builds whose shared memory exceeds the GPU's opt-in limit are skipped with a note (none on A100 / H100);
* outputs: `results/kernl_fused_ff_<GPU>_<stamp>.csv` with the 17 shared columns
  (`kernel,variant,gpu,case_id,params_json,grid,block,regs,warps_per_sm,batch_launches,reps,mean_us_median,
  mean_us_p10,mean_us_p90,span_us_median,bitwise_equal,max_abs_diff`), `_extra.csv` (bitwise vs ref and vs orig,
  poison left in plain and trace output, CPU-reference error, trace mode / loop verdict / time, span spread, clocks,
  speed-up, max abs diff vs orig and vs ref), `_env.json`, `.log`, `_nvsmi.txt`, and `traces/*.json` in the shared
  trace format. `bench/common/summarize.py` reads them.

## Trace builds and the SASS check

ptxas reacts to any change of a kernel: inline stamps (even only at entry and exit) changed the hot loop of every build.
The stamps therefore live in a non-inlined PTX `.func` called at the first instruction and before `ret`, in two call
forms (`.trace.ptx`: the trace pointer as an extra kernel parameter appended last; `.traceg.ptx`: no arguments, pointer
in a module variable set with `cuModuleGetGlobal`). `check_trace_sass.py` compares each with the plain build's hot loop
and writes `trace_choice.tsv` (the form the harness loads): with ptxas 12.6.77, **80 identical, 3 identical up to
register renaming, 9 near (<= 8 instructions differ, same stall sum +-2), 28 different, of 120**. The different ones: 24
sm_90 and 4 sm_80 builds; by variant 8 orig, 6 ro, 5 tt38, 4 ro_tt32, 3 tt32, 1 kernl, 1 ro_clamp. For those the shared
CSV gets `span_us_median = nan` unless the trace build's measured run time is within 2 % of the plain build's (and its
output equals the plain build's); the extra CSV always has the span. Among them is `ro` on sm_90 for every 2-warp
config, 64x128 and 128x32 (and 32x64 on sm_80), so few H100 `ro` spans will reach the shared CSV; the speed-ups come from the timed plain
builds, not from spans. `build.sh` reruns the check on the box's own SASS and compares every hot loop with `sass/`: a
DIFFERENT one stops the build (exit 4), since the box would then measure binaries other than the predicted ones.

Also checked per build (`sass/sass_report.md`, decoded loops in `sass/loops/`): registers, spills, residency, and
every LDG in the hot loop with its first waiter. Prefetch placement passes when every PREFETCHING LDG is first waited
on in the next iteration or >= 128 issue cycles later. Prefetching LDGs are the predicated ones (`@!P LDG`, the masked
next-iteration load) for `ro`, `ro_tt32` and `ro_full_tt32`, whose unpredicated LDGs are current-iteration loads the
compiler still issues (the x tile of Triton 3.2's HGMMA builds), and every LDG for `ro_clamp` (unmasked prefetch).

## SASS evidence (ptxas 12.6.77)

LDGs in the hot loop, issue cycles from each (prefetching) LDG to its first waiter; registers.

| config | arch | orig | ro | ro_clamp | tt32 | ro_tt32 | ro_full_tt32 | tt38 |
|---|---|---|---|---|---|---|---|---|
| 64x32x32_w2_s5 | sm_80 | 5 LDG, 14-25; 168 | 5 LDG, 297-416; 238 | 5 LDG, 346-383; 239 | 1 LDG, 23; 168 | 1 LDG, 169; 168 | - | 0 LDG (9 LDGSTS); 216 |
| 64x32x32_w2_s5 | sm_90 | 5 LDG, 14-25; 168 | 5 LDG, 296-373; 233 | 5 LDG, 354-380; 239 | 1 LDG, 66; 168 | 1 LDG, 395; 168 | - | 0 LDG (9 LDGSTS); 215 |
| 32x64x32_w2_s5 | sm_80 | 3 LDG, 18-22; 165 | 3 LDG, 167-169; 166 | 3 LDG, 397-409; 164 | 1 LDG, 23; 168 | 1 LDG, 273; 164 | - | 0 LDG (11 LDGSTS); 168 |
| 32x64x32_w2_s5 | sm_90 | 3 LDG, 23-27; 166 | 3 LDG, 275-314; 166 | 3 LDG, 337-345; 168 | 1 LDG, 25; 168 | 1 LDG, 306; 162 | - | 0 LDG (11 LDGSTS); 168 |
| 64x32x32_w2_s2 | sm_80 | 5 LDG, 14-25; 168 | 5 LDG, 297-397; 234 | 5 LDG, 297-374; 238 | 1 LDG, 5; 168 | 1 LDG, 158; 168 | - | 0 LDG (9 LDGSTS); 212 |
| 64x32x32_w2_s2 | sm_90 | 5 LDG, 14-25; 168 | 5 LDG, 311-366; 234 | 5 LDG, 328-354; 238 | 1 LDG, 11; 168 | 1 LDG, 328; 168 | - | 0 LDG (9 LDGSTS); 213 |
| 64x128x32_w4_s4 | sm_80 | 3 LDG, 23-27; 241 | 3 LDG, 383-599; 255 | 3 LDG, 340-596; 253 | 1 LDG, 25; 243 | 1 LDG, 417; 242 | 3 LDG, 341-361; 245 | 0 LDG (11 LDGSTS); 255 |
| 64x128x32_w4_s4 | sm_90 (HGMMA) | 3 LDG, 60-64; 244 | 3 LDG, 139-159; 243 | 3 LDG, 168-221; 244 | 3 LDG, 44-48; 255 | **3 LDG, 103: FAIL**; 255 | 3 LDG, 161-217; 255 | 0 LDG (11 LDGSTS); 255 |
| 16x16x64_w4_s2 | sm_80 | 2 LDG, 12; 64 | 2 LDG, 167-175; 68 | 2 LDG, 184-189; 80 | 1 LDG, 22; 68 | 1 LDG, 160; 63 | - | 0 LDG (4 LDGSTS); 90 |
| 16x16x64_w4_s2 | sm_90 | 2 LDG, 12; 67 | **2 LDG, 82-151: FAIL**; 64 | **2 LDG, 79-127: FAIL**; 75 | 1 LDG, 23; 68 | **1 LDG, 71: FAIL**; 64 | - | 0 LDG (4 LDGSTS); 90 |
| 128x32x32_w4_s4 | sm_80 | 5 LDG, 47-54; 168 | 5 LDG, 295-414; 233 | 5 LDG, 288-368; 235 | 1 LDG, 48; 168 | 1 LDG, 389; 176 | 5 LDG, 269-286; 207 | 0 LDG (7 LDGSTS); 211 |
| 128x32x32_w4_s4 | sm_90 (HGMMA) | 5 LDG, 75-87; 164 | 5 LDG, 213-249; 191 | 5 LDG, 221-259; 190 | 5 LDG, 61-73; 160 | 5 LDG, 155; 157 | 5 LDG, 280-324; 167 | 0 LDG (7 LDGSTS); 219 |
| 128x64x32_w4_s4 | sm_80 | 5 LDG, 43-55; 255 | 5 LDG, 173-185; 254 | 5 LDG, 140-638; 252 | 1 LDG, 25; 255 | 1 LDG, 381; 255 | 5 LDG, 251-274; 254 | 0 LDG (9 LDGSTS); 255 |
| 128x64x32_w4_s4 | sm_90 (HGMMA) | 5 LDG, 68-80; 252 | 5 LDG, 195-251; 250 | 5 LDG, 238-262; 254 | 5 LDG, 19-77; 228 | 5 LDG, 240; 226 | 5 LDG, 195-274; 231 | 0 LDG (9 LDGSTS); 255 |

What the reorder does in SASS: the LDGs of iteration k+1 issue at the top of iteration k and the HMUL2 of iteration
k+1 reads registers that were filled an iteration earlier. The first waiter of each prefetching LDG is NOT in the next
iteration, though: Triton carries a loop-carried fp16 tensor as unpacked 16-bit values, so ptxas inserts a `SEL`
(merge of the masked-off value, `ro`) or `SHF.R.U32.HI` (high halves, `ro_clamp`) late in the same iteration. The
load still gets 139-638 issue cycles (builds that pass) instead of 5-87. Cost: +30 to +88 loop instructions (`ro`;
+24 to +47 for `ro_clamp`), +65 to +71 registers for the 64x32 tiles (168 -> 233-239: 6 -> 4 CTAs per SM) and +26 to
+67 for 128x32 (3 -> 2 CTAs per SM), which matters only once the grid fills the GPU. Four builds fail the
placement gate (ptxas put the waiter 71-103 cycles after the prefetch: `ro`, `ro_clamp`, `ro_tt32` 16x16 sm_90 and
`ro_tt32` 64x128 sm_90); they are measured anyway. Triton 3.8 (`tt38`) has no LDG in any loop but needs more
registers for the 64x32 tiles (168 -> 212-216: 6 -> 4 CTAs/SM, like `ro`), more shared memory for 32x64 (A100: 4 -> 3
CTAs/SM) and 90 registers for 16x16 (8 -> 5 CTAs/SM).

## Frozen predictions (`predictions.json`, written before any GPU run)

`tools/model_ff.py` (method in its docstring, per-build numbers in `model_report.md`): a one-warp in-order simulation
of each build's hot loop AS COMPILED (scoreboards and stall counts from the SASS, LDG latency = L2 hit when warm and
DRAM when cold, cp.async groups, LDSM / HMMA latencies, HGMMA groups on sm_90), then per case residency from registers
and shared memory, waves on the busiest scheduler, DRAM and L2 bandwidth floors, and a fixed launch + prologue cost.
Speed-up = T(base) / T(variant) at four corners (LDG latency A100 220 / 374 warm, 493 / 645 cold; H100 280 / 472
warm, 572 / 774 cold; non-load work as modelled or x2.2, the sweep's calibration caveat; low / high bandwidths);
range = corners -+0.03. In cold cases every x-tile and `rms_w` LDG is a fresh DRAM read (each K step touches a new
64 B per row, plain LDG.E.128, no L2 prefetch hint), so cold is no longer a copy of warm. GPUs as on the earlier
runs: A100-PCIE-40GB (108 SMs) and H100 80GB HBM3 (SXM, 132 SMs). 6,082 entries over 280 cases x 2 GPUs; SHA-256
of the frozen file starts `a9c4407e3d9e2632` (full hash in `predictions.json.sha256`). Kinds:
* per case, variant vs orig (`ro` is the primary and carries no `"variant"` key; the others do);
* per case, `"baseline"` entries, T(baseline) / T(target), > 1 = ours faster: `ro_vs_tt32`, `ro_tt32_vs_tt32`,
  `ro_full_tt32_vs_tt32` (is Triton 3.2's own schedule better than our reorder, on 2.2 and on 3.2?), `ro_vs_tt38` (is
  the current Triton better than our reorder?), `ro_vs_ctl_r64` (what is left of `ro` at 16x16 once its occupancy
  change is controlled for);
* best-of-configs (`"baseline_cases"` / `"target_cases"`): min over configs of T(baseline) / min over configs of
  T(target) at CuAsmRL's two shapes and the two LLaMA shapes: `ro_bestcfg` (Triton 2.2 autotuned over all 10 configs
  vs our reorder autotuned over its 7), `ro_bestcfg_vs_tt32`, `ro_bestcfg_vs_tt38` (Triton 3.2 / 3.8 autotuned over
  the 7 configs built with them). The model's minimum skips builds that spill (it does not model local memory); the
  measured minimum takes every config;
* `ro_sweep`: the cuasmrl sweep's committed ranges, scored on the same measured T(orig) / T(ro) (see Scoring);
* every per-case entry carries both builds' CTAs per SM and `occupancy_changed` (the CTAs co-resident on the busiest
  SM differ): such a speed-up is partly an occupancy effect, not the reorder, and `summarize.py` reports those cases
  in separate `[occupancy changed]` / `[occupancy unchanged]` rows (856 of the 6016 per-case entries).

At CuAsmRL's script shape (M=N=512, K=1024; the K=2048 and LLaMA tables are in `model_report.md`); (o) = occupancy
changed:

| config | ro A100 warm / cold | ro H100 warm / cold | ro_clamp A100 / H100 | ctl_s2 A100 / H100 | ctl_s5 A100 / H100 |
|---|---|---|---|---|---|
| 64x32x32_w2_s5 | **1.40-1.69** / 1.44-1.68 | **1.27-1.50** / 1.31-1.57 | 1.44-1.93 / 1.31-1.67 | 0.73-0.88 / 0.69-0.83 | 0.97-1.03 / 0.97-1.03 |
| 32x64x32_w2_s5 | **0.78-1.09** / 0.98-1.07 | **0.88-1.23** / 1.11-1.19 | 0.66-1.10 / 0.89-1.36 | 0.67-0.80 / 0.63-0.74 | 0.97-1.03 / 0.97-1.03 |
| 64x32x32_w2_s2 | **1.37-1.51** / 1.29-1.53 | **1.22-1.36** / 1.20-1.41 | 1.39-1.64 / 1.26-1.57 | 0.97-1.03 / 0.97-1.03 | 1.15-1.34 / 1.22-1.42 |
| 64x128x32_w4_s4 | **0.94-1.34** / 1.10-1.28 | **0.95-1.08** / 1.00-1.10 | 1.02-1.38 / 1.12-1.22 | 0.72-0.86 / 0.91-1.03 | 0.97-1.03 / 0.97-1.03 |
| 16x16x64_w4_s2 | **0.98-1.33 (o)** / 1.24-1.59 (o) | **1.24-2.13 (o)** / 1.72-2.39 (o) | 0.98-1.40 (o) / 1.06-1.17 (o) | 0.97-1.03 / 0.97-1.03 | 0.98-1.23 / 1.24-2.34 (o) |
| 128x32x32_w4_s4 | **1.08-1.45** / 1.27-1.36 | **0.97-1.12** / 1.03-1.16 | 1.15-1.51 / 0.97-1.28 | - / - | - / - |
| 128x64x32_w4_s4 | **0.72-0.92** / 0.83-0.94 | **0.97-1.15** / 1.06-1.17 | 0.71-0.90 / 0.97-1.31 | - / - | - / - |

(ro_clamp, ctl_s2, ctl_s5 warm; a control whose stage count equals the config's is an A/A null test: 0.97-1.03.)

Is Triton better than our reorder? (same shape; > 1 = our reorder is faster than that Triton's own schedule)

| config | tt32 vs orig A100 / H100 | ro_vs_tt32 A100 w; c / H100 w; c | ro_tt32_vs_tt32 A100 / H100 | ro_full_tt32_vs_tt32 A100 / H100 | tt38 vs orig A100 / H100 | ro_vs_tt38 A100 w; c / H100 w; c |
|---|---|---|---|---|---|---|
| 64x32x32_w2_s5 | 1.09-1.21 / 0.94-1.01 | 1.18-1.51; 1.31-1.46 / 1.31-1.53; 1.33-1.61 | 0.88-1.13 / 0.93-1.40 | - / - | 1.74-2.27 / 1.51-2.15 | 0.71-0.84; 0.50-0.84 / 0.66-0.88; 0.47-0.88 |
| 32x64x32_w2_s5 | 0.88-0.98 / 0.88-0.98 | 0.86-1.15; 1.06-1.12 / 0.97-1.29; 1.16-1.29 | 1.15-1.50 / 1.15-1.47 | - / - | 1.00-1.57 / 1.04-1.77 | 0.66-0.82; 0.48-0.82 / 0.66-0.88; 0.46-0.88 |
| 64x32x32_w2_s2 | 1.08-1.21 / 0.99-1.07 | 1.15-1.37; 1.19-1.35 / 1.17-1.33; 1.18-1.36 | 0.86-1.09 / 1.00-1.35 | - / - | 1.59-1.79 / 1.38-1.67 | 0.81-0.89; 0.68-0.91 / 0.78-0.92; 0.66-0.93 |
| 64x128x32_w4_s4 | 0.96-1.02 / 0.59-0.79 | 0.95-1.35; 1.12-1.29 / 1.35-1.61; 1.24-1.60 | 1.09-1.52 / 0.79-1.00 | 1.10-1.51 / 1.15-1.52 | 1.00-1.41 / 1.03-1.82 | 0.92-0.98; 0.70-0.98 / 0.56-0.96; 0.40-0.81 |
| 16x16x64_w4_s2 | 0.97-1.04 (o) / 0.94-1.01 | 0.97-1.33; 1.23-1.59 / 1.26-2.19 (o); 1.74-2.44 (o) | 0.97-1.24 (o) / 1.26-2.07 (o) | - / - | 0.98-1.50 (o) / 1.15-1.51 (o) | 0.86-1.03 (o); 0.91-1.03 (o) / 0.97-1.81 (o); 1.03-1.80 (o) |
| 128x32x32_w4_s4 | 0.79-0.91 / 0.55-0.68 | 1.32-1.65; 1.41-1.60 / 1.63-1.75; 1.46-2.02 | 0.97-1.36 / 0.93-1.03 | 1.64-1.84 / 1.02-1.43 | 1.33-1.90 / 0.97-1.47 | 0.73-0.85; 0.51-0.85 / 0.72-1.03; 0.52-1.05 |
| 128x64x32_w4_s4 | 1.02-1.10 / 0.53-0.67 | 0.67-0.87; 0.78-0.90 / 1.72-1.83; 1.51-2.07 | 1.08-1.48 / 1.00-1.08 | 0.90-1.20 / 1.10-1.52 | 1.17-1.57 / 0.84-1.32 | 0.55-0.66; 0.45-0.66 / 0.84-1.18; 0.60-1.18 |

(warm unless marked; w = warm, c = cold. tt32 / tt38 vs orig > 1 = that Triton's own schedule beats Triton 2.2's.)

Best of configs (autotuned Triton vs autotuned reorder; > 1 = ours faster):

| shape | entry | A100 warm | A100 cold | H100 warm | H100 cold |
|---|---|---|---|---|---|
| 512x512x1024 | ro_bestcfg | 0.86-1.26 | 1.08-1.19 | 0.95-1.26 | 1.06-1.40 |
| 512x512x1024 | ro_bestcfg_vs_tt32 | 0.94-1.33 | 1.16-1.24 | 1.17-1.54 | 1.16-1.63 |
| 512x512x1024 | ro_bestcfg_vs_tt38 | 0.72-0.84 | 0.50-0.84 | 0.60-1.19 | 0.42-1.02 |
| 512x512x2048 | ro_bestcfg | 0.85-1.27 | 1.08-1.20 | 0.95-1.28 | 1.07-1.42 |
| 512x512x2048 | ro_bestcfg_vs_tt32 | 0.94-1.35 | 1.17-1.25 | 1.18-1.57 | 1.17-1.67 |
| 512x512x2048 | ro_bestcfg_vs_tt38 | 0.70-0.83 | 0.48-0.83 | 0.57-1.21 | 0.39-1.02 |
| 16x11008x4096 | ro_bestcfg | 0.97-1.03 | 0.97-1.03 | 0.97-1.03 | 0.97-1.20 |
| 16x11008x4096 | ro_bestcfg_vs_tt32 | 0.97-1.03 | 0.97-1.03 | 0.97-1.03 | 0.97-1.23 |
| 16x11008x4096 | ro_bestcfg_vs_tt38 | 0.97-1.03 | 0.97-1.03 | 0.97-1.03 | 0.97-1.03 |
| 512x11008x4096 | ro_bestcfg | 0.86-1.10 | 0.98-1.26 | 0.97-1.03 | 0.97-1.12 |
| 512x11008x4096 | ro_bestcfg_vs_tt32 | 0.81-1.10 | 0.98-1.27 | 1.07-1.62 | 1.22-1.65 |
| 512x11008x4096 | ro_bestcfg_vs_tt38 | 0.92-1.03 | 0.88-1.03 | 0.97-1.28 | 0.82-1.28 |

Over all shapes (`ro` vs orig, per GPU and L2 state; "grid-filling" = M >= 256 with N >= 4096, or M = 1024):

| config | A100 warm | A100 cold | H100 warm | H100 cold |
|---|---|---|---|---|
| 64x32x32_w2_s5 | faster 16, slower 0 of 24; grid-filling 0.70-1.20 | faster 16, slower 4 of 24; grid-filling 0.73-1.39 | faster 16, slower 0 of 24; grid-filling 0.86-1.35 | faster 17, slower 0 of 24; grid-filling 0.89-1.60 |
| 32x64x32_w2_s5 | faster 0, slower 0 of 24; grid-filling 0.77-1.10 | faster 0, slower 0 of 24; grid-filling 0.97-1.08 | faster 0, slower 0 of 24; grid-filling 0.92-1.03 | faster 17, slower 0 of 24; grid-filling 0.97-1.21 |
| 64x32x32_w2_s2 | faster 16, slower 4 of 24; grid-filling 0.68-1.25 | faster 19, slower 4 of 24; grid-filling 0.64-1.25 | faster 21, slower 0 of 24; grid-filling 0.82-1.38 | faster 21, slower 1 of 24; grid-filling 0.80-1.43 |
| 64x128x32_w4_s4 | faster 0, slower 0 of 24; grid-filling 0.94-1.12 | faster 20, slower 0 of 24; grid-filling 0.98-1.27 | faster 0, slower 0 of 24; grid-filling 0.95-1.08 | faster 20, slower 0 of 24; grid-filling 0.97-1.11 |
| 16x16x64_w4_s2 | faster 5, slower 0 of 24; grid-filling 0.91-1.05 | faster 16, slower 0 of 24; grid-filling 0.97-1.43 | faster 14, slower 0 of 24; grid-filling 0.97-1.45 | faster 20, slower 0 of 24; grid-filling 0.99-1.61 |
| 128x32x32_w4_s4 | faster 3, slower 0 of 4; grid-filling 0.77-1.09 | faster 3, slower 0 of 4; grid-filling 0.92-1.03 | faster 0, slower 2 of 4; grid-filling 0.82-0.99 | faster 2, slower 2 of 4; grid-filling 0.85-0.96 |
| 128x64x32_w4_s4 | faster 0, slower 3 of 4; grid-filling 0.71-0.91 | faster 0, slower 3 of 4; grid-filling 0.82-0.93 | faster 0, slower 0 of 4; grid-filling 0.97-1.03 | faster 3, slower 0 of 4; grid-filling 0.97-1.18 |

(faster = predicted lower bound > 1, slower = upper bound < 1; the rest straddle 1.0.)

So: the 64x32 tiles are predicted faster at 16-21 of 24 shapes, and range from a clear loss to a clear gain where the
grid fills the GPU (`ro`'s 6 -> 4 CTAs/SM against the hidden latency; on A100 64x32_s2 is predicted slower at 4 shapes
warm and cold, 64x32_s5 at 4 shapes cold). 32x64 and 64x128 straddle 1.0 warm and are predicted faster cold (64x128 on
both GPUs, 32x64 on H100): their `ro` prefetch is consumed 139-169 cycles later on one GPU, and with the LDG wait gone
the LDSM -> HMMA latencies are the exposed ones, so the gain needs the longer DRAM latency to show. 128x64 `ro` is
predicted slower on A100 (3 of 4 shapes), 128x32 on H100 (2 of 4). The large 16x16x64 H100 numbers are a
wave-quantisation effect (orig 67 registers -> 7 CTAs/SM, `ro` 64 -> 8 CTAs/SM, 1,024 CTAs on 132 SMs), not the reorder:
`ctl_r64` (no reorder, same registers) is predicted to give the same 1.24-2.13, and `ro_vs_ctl_r64` 0.97-1.04 warm; they
would not hold on a 114-SM H100 PCIe.

## Scoring

`summarize.py`: hit = `pred_lo <= measured <= pred_hi` for every entry, primary and extra, per case and for the
baseline / best-of entries. Two commitments are scored on the same measured T(orig) / T(ro):

| case (M, N, K, config) | GPU | the sweep's range (`ro_sweep`; ideal transform: prefetch consumed in the next iteration, no extra instructions) | this bench's range (`ro`; as compiled), warm / cold |
|---|---|---|---|
| 512, 512, 1024, 64x32x32_w2_s5 | A100 | 1.15-1.60 | 1.40-1.69 / 1.44-1.68 |
| 512, 512, 1024, 64x32x32_w2_s5 | H100 | 1.20-1.80 | 1.27-1.50 / 1.31-1.57 |
| 512, 512, 1024, 64x32x32_w2_s2 | A100 | 1.15-1.60 | 1.37-1.51 / 1.29-1.53 |
| 512, 512, 1024, 64x32x32_w2_s2 | H100 | 1.20-1.80 | 1.22-1.36 / 1.20-1.41 |
| 512, 512, 1024, 32x64x32_w2_s5 | A100 | 1.15-1.60 | 0.78-1.09 / 0.98-1.07 |
| 512, 512, 1024, 32x64x32_w2_s5 | H100 | 1.20-2.00 | 0.88-1.23 / 1.11-1.19 |
| 16, 11008, 4096, 16x16x64_w4_s2 | A100 | 0.95-1.05 | 0.97-1.03 / 0.97-1.03 |
| 16, 11008, 4096, 16x16x64_w4_s2 | H100 | 0.95-1.05 | 0.97-1.03 / 0.97-1.20 |
| 512, 11008, 4096, 64x32x32_w2_s5 | A100 | 1.15-1.35 | 0.97-1.09 (o) / 0.97-1.24 (o) |

The sweep's "up to x2.0 for 32x64 on H100" is kept as its own scored range, not silently replaced: the bench's
as-compiled range for that config is lower because ptxas consumes the prefetch inside the iteration (167-169 issue
cycles after the load on sm_80) and the 32x64 `ro` loop grows from 147 to 194-200 instructions (327-369 to 430-436
issue cycles).

## Risks

* ptxas: the SASS (and so the gain) depends on the ptxas version (with ptxas 12.2 the `ro` 64x32 loop is 588 instead
  of 511 issue cycles). `build.sh` pins 12.6.77 and stops when a box hot loop differs from `sass/`.
* The prefetch is consumed inside the iteration (SEL / SHF), so the gain depends on how much other work ptxas puts
  between load and unpack; on sm_90 for 16x16 and for Triton 3.2's 64x128 HGMMA build it is too little (placement
  FAIL).
* Register growth (168 -> 233-239 for 64x32, 168 -> 233 for 128x32 sm_80) can make `ro` slower than orig at large
  grids; the same holds for `tt38` (212-216 registers for 64x32).
* Model uncertainty: L2 / DRAM latency and bandwidth, the x2.2 calibration, HGMMA timing (rough), wave quantisation at
  small grids, no model of spills (orig-only configs). The L2 state is binary: warm cases whose data do not fit in L2
  (N=11008, M=1024 x N=4096 x K=4096) still use the L2-hit LDG latency (their DRAM floor is modelled), and in cold
  multi-wave grids later waves can find x / rms_w in L2 while the model charges DRAM latency. Ranges are wide on
  purpose.
* 28 of 120 trace builds change the hot loop despite the callee stamps; their spans reach the shared CSV only when the
  trace build runs within 2 % of the plain build.
* `kernl`, `tt32` and `tt38` are not expected to be bit-identical to orig; every other variant is to its reference
  (a mismatch, or a trace build whose output differs from its plain build, makes `ff_bench` exit 1 and is listed in
  the extra CSV).
* Clocks are not locked (no root needed); `run.sh` records nvidia-smi clocks before and after, the harness measures
  the SM clock at start and end, and the shuffled orders spread drift over all variants.
* CuAsmRL measured on an A100-80GB-PCIe with ptxas 12.2; the boxes here are A100-PCIE-40GB and H100 SXM with 12.6.
  The current Triton (3.8) is compiled with PTX ISA 8.5 for ptxas 12.6 instead of its own 8.8 / ptxas 12.9.

## Files

```
src/fused_ff_kernels.py      Triton sources: tt_ff (orig, tt32, tt38), ff_ro (ro, ro_full_tt32), ff_ro_clamp,
                             ff_ro_rms (ro_tt32), ff_llama (kernl)
src/ptx/                     <variant>__<cfg>.sm<cc>.{ptx,trace.ptx,traceg.ptx,json} (120 builds)
src/manifest.tsv             builds the harness loads;  src/cases.tsv: the 280 cases
src/harness/ff_bench.cpp     the driver-API harness (C++, -lcuda)
build.sh, run.sh             box steps
predictions.json(.sha256)    frozen predictions + their hash
model_report.md              the model's per-build and per-case numbers
check_trace_sass.py          SASS checks (placement, spills, residency, trace loops, box vs local SASS)
sass/                        ptxas 12.6.77 SASS + ptxas -v logs of every build, sass_report.md, loops/, trace_choice.tsv
local/cubin/                 the ptxas 12.6.77 cubins (build.sh's fallback when the box cannot get that ptxas)
tools/gen_ptx.py, make_trace.py, sass.sh, model_ff.py    generation and model;  local/gen.sh reruns them (WSL)
tools/fake_cuda/             a CPU stand-in for libcuda + smoke.sh (+ smoke_preds.py, fake predictions of every kind):
                             runs the harness and summarize.py end to end without a GPU
```
`results/` and `traces/` are filled on the box.

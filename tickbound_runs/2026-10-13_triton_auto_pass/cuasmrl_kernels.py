# Triton kernels that CuAsmRL (He & Yoneki, CGO 2025) optimised, extracted verbatim (bodies unchanged) from
#   https://github.com/hgl71964/cuasmrl  branch `reproduce`, commit fed7fb14ad51e8398e0edc90270f5207a26671ec
#   (= Zenodo 10.5281/zenodo.14058861, cuasmrl-reproduce.zip). Repo licence: Triton MIT (+ CuAsmRL Apache-2.0 per paper).
# Only the decorators differ: CuAsmRL's `@jit` (cuasmrl.jit) is replaced by `@triton.jit`; the fork's jit uses
# Triton's own specialisation (JITFunction._get_config), so the compiled code is the same.
#
#   rmsnorm_cuasmrl  benchmarks/cutlass/torch_rmsnorm.py `_cuasmrl` (also benchmarks/rmsnorm.py) - the kernel the
#                    RL agent optimised; N_SIZE is tl.constexpr here
#   rmsnorm_tt       benchmarks/cutlass/torch_rmsnorm.py `rmsnorm_tt` - the "Triton" baseline of the paper's Fig.;
#                    N_SIZE is a RUNTIME argument here (the only source difference)
#   softmax          benchmarks/02-fused-softmax.py `cuasmrl_kernel` == `tt_kernel` (identical source)
#   matmul_leaky     benchmarks/cutlass/cutlass_mm_leakyrelu.py `cuasmrl_kernel` (+ `leaky_relu`)
# Kernl origin of rmsnorm: https://github.com/ELS-RD/kernl (Apache-2.0). Softmax / matmul: Triton tutorials (MIT).
import triton
import triton.language as tl


@triton.jit
def rmsnorm_cuasmrl(x_ptr, rms_w_ptr, output_ptr,
                    stride_x_batch, stride_x_m, stride_x_k,
                    stride_rms_w,
                    stride_out_batch, stride_out_m, stride_out_k,
                    N_SIZE: tl.constexpr, eps: tl.constexpr, BLOCK_N_SIZE: tl.constexpr):
    pid_batch = tl.program_id(0)
    pid_m = tl.program_id(1)

    offs_m = pid_batch * stride_x_batch + pid_m * stride_x_m
    block_N = tl.arange(0, BLOCK_N_SIZE)
    var = tl.zeros((BLOCK_N_SIZE,), tl.float32)
    for block_n_start_idx in range(0, N_SIZE, BLOCK_N_SIZE):
        offs_n = block_n_start_idx + block_N
        x_ptr_mask = offs_n < N_SIZE
        x = tl.load(x_ptr + offs_m + offs_n * stride_x_k, mask=x_ptr_mask, other=0.0)
        var += tl.math.pow(x.to(tl.float32), 2)

    var = tl.sum(var, axis=0) / N_SIZE
    rstd = tl.math.rsqrt(var + eps)

    # multiply by weight and add bias
    for block_n_start_idx in range(0, N_SIZE, BLOCK_N_SIZE):
        offs_n = block_n_start_idx + block_N
        x_ptr_mask = offs_n < N_SIZE
        rms_w = tl.load(rms_w_ptr + offs_n * stride_rms_w, mask=x_ptr_mask)

        x = tl.load(x_ptr + offs_m + offs_n * stride_x_k, mask=x_ptr_mask, other=0.0).to(tl.float32)
        x_hat = x * rstd
        out = x_hat * rms_w
        out_off = pid_batch * stride_out_batch + pid_m * stride_out_m + offs_n * stride_out_k
        tl.store(output_ptr + out_off, out, mask=x_ptr_mask)


@triton.jit
def rmsnorm_tt(x_ptr, rms_w_ptr, output_ptr,
                   stride_x_batch, stride_x_m, stride_x_k,
                   stride_rms_w,
                   stride_out_batch, stride_out_m, stride_out_k,
                   N_SIZE, eps: tl.constexpr, BLOCK_N_SIZE: tl.constexpr):
    pid_batch = tl.program_id(0)
    pid_m = tl.program_id(1)

    offs_m = pid_batch * stride_x_batch + pid_m * stride_x_m
    block_N = tl.arange(0, BLOCK_N_SIZE)
    var = tl.zeros((BLOCK_N_SIZE,), tl.float32)
    for block_n_start_idx in range(0, N_SIZE, BLOCK_N_SIZE):
        offs_n = block_n_start_idx + block_N
        x_ptr_mask = offs_n < N_SIZE
        x = tl.load(x_ptr + offs_m + offs_n * stride_x_k, mask=x_ptr_mask, other=0.0)
        var += tl.math.pow(x.to(tl.float32), 2)

    var = tl.sum(var, axis=0) / N_SIZE
    rstd = tl.math.rsqrt(var + eps)

    # multiply by weight and add bias
    for block_n_start_idx in range(0, N_SIZE, BLOCK_N_SIZE):
        offs_n = block_n_start_idx + block_N
        x_ptr_mask = offs_n < N_SIZE
        rms_w = tl.load(rms_w_ptr + offs_n * stride_rms_w, mask=x_ptr_mask)

        x = tl.load(x_ptr + offs_m + offs_n * stride_x_k, mask=x_ptr_mask, other=0.0).to(tl.float32)
        x_hat = x * rstd
        out = x_hat * rms_w
        out_off = pid_batch * stride_out_batch + pid_m * stride_out_m + offs_n * stride_out_k
        tl.store(output_ptr + out_off, out, mask=x_ptr_mask)


@triton.jit
def softmax(output_ptr, input_ptr,
                input_row_stride, output_row_stride,
                n_rows, n_cols,
                BLOCK_SIZE: tl.constexpr,
    ):
    # The rows of the softmax are independent, so we parallelize across those
    row_idx = tl.program_id(0)
    # The stride represents how much we need to increase the pointer to advance 1 row
    row_start_ptr = input_ptr + row_idx * input_row_stride
    # The block size is the next power of two greater than n_cols, so we can fit each
    # row in a single block
    col_offsets = tl.arange(0, BLOCK_SIZE)
    input_ptrs = row_start_ptr + col_offsets
    # Load the row into SRAM, using a mask since BLOCK_SIZE may be > than n_cols
    row = tl.load(input_ptrs, mask=col_offsets < n_cols, other=-float('inf'))
    # Subtract maximum for numerical stability
    row_minus_max = row - tl.max(row, axis=0)
    # Note that exponentiation in Triton is fast but approximate (i.e., think __expf in CUDA)
    numerator = tl.exp(row_minus_max)
    denominator = tl.sum(numerator, axis=0)
    softmax_output = numerator / denominator
    # Write back output to DRAM
    output_row_start_ptr = output_ptr + row_idx * output_row_stride
    output_ptrs = output_row_start_ptr + col_offsets
    tl.store(output_ptrs, softmax_output, mask=col_offsets < n_cols)


@triton.jit
def leaky_relu(x):
    x = x + 1
    return tl.where(x >= 0, x, 0.01 * x)


@triton.jit
def matmul_leaky(
        # Pointers to matrices
        a_ptr, b_ptr, c_ptr,
        # Matrix dimensions
        M, N, K,
        # The stride variables represent how much to increase the ptr by when moving by 1
        # element in a particular dimension. E.g. `stride_am` is how much to increase `a_ptr`
        # by to get the element one row down (A has M rows).
        stride_am, stride_ak,  #
        stride_bk, stride_bn,  #
        stride_cm, stride_cn,
        # Meta-parameters
        BLOCK_SIZE_M: tl.constexpr, BLOCK_SIZE_N: tl.constexpr, BLOCK_SIZE_K: tl.constexpr,  #
        GROUP_SIZE_M: tl.constexpr,  #
        ACTIVATION: tl.constexpr  #
):
    # -----------------------------------------------------------
    pid = tl.program_id(axis=0)
    num_pid_m = tl.cdiv(M, BLOCK_SIZE_M)
    num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
    num_pid_in_group = GROUP_SIZE_M * num_pid_n
    group_id = pid // num_pid_in_group
    first_pid_m = group_id * GROUP_SIZE_M
    group_size_m = min(num_pid_m - first_pid_m, GROUP_SIZE_M)
    pid_m = first_pid_m + (pid % group_size_m)
    pid_n = (pid % num_pid_in_group) // group_size_m

    # ----------------------------------------------------------
    offs_am = (pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)) % M
    offs_bn = (pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)) % N
    offs_k = tl.arange(0, BLOCK_SIZE_K)
    a_ptrs = a_ptr + (offs_am[:, None] * stride_am + offs_k[None, :] * stride_ak)
    b_ptrs = b_ptr + (offs_k[:, None] * stride_bk + offs_bn[None, :] * stride_bn)

    # -----------------------------------------------------------
    accumulator = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=tl.float32)
    for k in range(0, tl.cdiv(K, BLOCK_SIZE_K)):
        # Load the next block of A and B, generate a mask by checking the K dimension.
        # If it is out of bounds, set it to 0.
        a = tl.load(a_ptrs, mask=offs_k[None, :] < K - k * BLOCK_SIZE_K, other=0.0)
        b = tl.load(b_ptrs, mask=offs_k[:, None] < K - k * BLOCK_SIZE_K, other=0.0)
        # We accumulate along the K dimension.
        accumulator += tl.dot(a, b)
        # Advance the ptrs to the next K block.
        a_ptrs += BLOCK_SIZE_K * stride_ak
        b_ptrs += BLOCK_SIZE_K * stride_bk
    # You can fuse arbitrary activation functions here
    # while the accumulator is still in FP32!
    if ACTIVATION == "leaky_relu":
        accumulator = leaky_relu(accumulator)
    c = accumulator.to(tl.float16)

    # -----------------------------------------------------------
    # Write back the block of the output matrix C with masks.
    offs_cm = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)
    offs_cn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    c_ptrs = c_ptr + stride_cm * offs_cm[:, None] + stride_cn * offs_cn[None, :]
    c_mask = (offs_cm[:, None] < M) & (offs_cn[None, :] < N)
    tl.store(c_ptrs, c, mask=c_mask)


# fused_ff: benchmarks/fused_feedforward.py `tt_ff` (lines 140-228; `cuasmrl_kernel` has the same body)
@triton.jit
def tt_ff(
    a_ptr, w1_ptr, w3_ptr, out_ptr, rms_w_ptr,
    M, N, K,
    stride_am, stride_ak,
    stride_w1k, stride_w1n,
    stride_w3k, stride_w3n,
    stride_outm, stride_outn,
    stride_rms_w,
    USE_FP8: tl.constexpr,
    EPS: tl.constexpr,
    BLOCK_SIZE_M: tl.constexpr, BLOCK_SIZE_N: tl.constexpr, BLOCK_SIZE_K: tl.constexpr,
    GROUP_SIZE_M: tl.constexpr,
):
    """
    w1 and w3 are weights (linear layers)
    F.silu(w1(x)) * w3(x)
    """
    # native
    # pid = tl.program_id(axis=0)
    # pid_m = pid // tl.cdiv(N, BLOCK_SIZE_N)
    # pid_n = pid % tl.cdiv(N, BLOCK_SIZE_N)

    # L2
    pid = tl.program_id(axis=0)
    num_pid_m = tl.cdiv(M, BLOCK_SIZE_M)
    num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
    num_pid_in_group = GROUP_SIZE_M * num_pid_n
    group_id = pid // num_pid_in_group
    first_pid_m = group_id * GROUP_SIZE_M
    group_size_m = min(num_pid_m - first_pid_m, GROUP_SIZE_M)
    pid_m = first_pid_m + ((pid % num_pid_in_group) % group_size_m)
    pid_n = (pid % num_pid_in_group) // group_size_m

    ##################

    offs_am = (pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)) % M
    offs_bn = (pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)) % N
    offs_k = tl.arange(0, BLOCK_SIZE_K)
    a_ptrs = a_ptr + (offs_am[:, None] * stride_am + offs_k[None, :] * stride_ak)
    w1_ptrs = w1_ptr + (offs_k[:, None] * stride_w1k + offs_bn[None, :] * stride_w1n)
    w3_ptrs = w3_ptr + (offs_k[:, None] * stride_w3k + offs_bn[None, :] * stride_w3n)
    acc1 = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=tl.float32)
    acc2 = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=tl.float32)

    rms_w_ptrs = rms_w_ptr + tl.arange(0, BLOCK_SIZE_K)[None, :] * stride_rms_w
    a_sum = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_K), dtype=tl.float32)
    for _ in range(0, tl.cdiv(K, BLOCK_SIZE_K)):
        a = tl.load(a_ptrs)

        # a_sum += tl.math.pow(a.to(tl.float32), 2)
        a_float32 = a.to(tl.float32)
        a_sum += a_float32 * a_float32

        rms_w = tl.load(rms_w_ptrs)
        if USE_FP8:
            rms_w = rms_w.to(tl.float8e5, bitcast=True)
            rms_w = rms_w.to(tl.float16)
        a = a * rms_w
        b = tl.load(w1_ptrs)
        if USE_FP8:
            b = b.to(tl.float8e5, bitcast=True)
            b = b.to(tl.float32)
            b = b.to(tl.float16)
        acc1 += tl.dot(a, b)
        c = tl.load(w3_ptrs)
        if USE_FP8:
            c = c.to(tl.float8e5, bitcast=True)
            c = c.to(tl.float32)
            c = c.to(tl.float16)
        acc2 += tl.dot(a, c)

        a_ptrs += BLOCK_SIZE_K * stride_ak
        w1_ptrs += BLOCK_SIZE_K * stride_w1k
        w3_ptrs += BLOCK_SIZE_K * stride_w3k

        rms_w_ptrs += BLOCK_SIZE_K * stride_rms_w

    a_mean = tl.sum(a_sum, axis=1) / K + EPS
    a_norm = tl.math.rsqrt(a_mean)
    acc1 = acc1 * a_norm[:, None]
    acc2 = acc2 * a_norm[:, None]
    accumulator = (acc1 * tl.sigmoid(acc1)) * acc2

    offs_outm = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)
    offs_outn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    out_ptrs = out_ptr + (stride_outm * offs_outm[:, None] + stride_outn * offs_outn[None, :])
    out_mask = (offs_outm[:, None] < M) & (offs_outn[None, :] < N)
    tl.store(out_ptrs, accumulator, mask=out_mask)

| kernl_fused_ff | A100 | ro | 256 | 1.12x | 0.96-1.39x | 1.13x | 0.74-1.65x | 206/256 | 256/256 | 160/256 (43 above, 53 below) | 1.13x |
| kernl_fused_ff | A100 | ctl_r64 (extra) | 48 | 1.00x | 0.99-1.00x | 1.00x | 0.98-1.01x | 1/48 | 48/48 | 48/48 | 1.00x |
| kernl_fused_ff | A100 | ctl_s2 (extra) | 240 | 0.91x | 0.74-1.00x | 0.89x | 0.63-1.27x | 13/240 | 240/240 | 198/240 (32 above, 10 below) | 0.98x |
| kernl_fused_ff | A100 | ctl_s2 [occupancy changed] (extra) | 14 | 1.18x | 0.90-1.25x | 1.09x | 0.88-1.27x | 8/14 | 14/14 | 12/14 (0 above, 2 below) | 1.26x |
| kernl_fused_ff | A100 | ctl_s2 [occupancy unchanged] (extra) | 226 | 0.88x | 0.74-1.00x | 0.88x | 0.63-1.03x | 5/226 | 226/226 | 186/226 (32 above, 8 below) | 0.97x |
| kernl_fused_ff | A100 | ctl_s5 (extra) | 240 | 1.00x | 1.00-1.26x | 1.06x | 0.83-1.39x | 78/240 | 240/240 | 209/240 (4 above, 27 below) | 1.00x |
| kernl_fused_ff | A100 | kernl (extra) | 256 | 0.96x | 0.91-1.02x | 0.96x | 0.46-1.19x | 29/256 | 256/256 | 181/256 (39 above, 36 below) | 0.96x |
| kernl_fused_ff | A100 | ro [occupancy changed] (extra) | 62 | 1.04x | 0.80-1.20x | 1.01x | 0.74-1.29x | 28/62 | 62/62 | 50/62 (6 above, 6 below) | 1.01x |
| kernl_fused_ff | A100 | ro [occupancy unchanged] (extra) | 194 | 1.15x | 1.02-1.40x | 1.17x | 0.84-1.65x | 178/194 | 194/194 | 110/194 (37 above, 47 below) | 1.18x |
| kernl_fused_ff | A100 | ro_bestcfg (extra) | 8 | 1.14x | 1.03-1.18x | 1.12x | 1.01-1.19x | 7/8 | 8/8 | 6/8 (2 above, 0 below) | 1.15x |
| kernl_fused_ff | A100 | ro_bestcfg_vs_tt32 (extra) | 8 | 1.08x | 1.02-1.13x | 1.08x | 1.01-1.17x | 7/8 | 8/8 | 7/8 (0 above, 1 below) | 1.06x |
| kernl_fused_ff | A100 | ro_bestcfg_vs_tt38 (extra) | 8 | 1.14x | 0.92-1.25x | 1.11x | 0.92-1.25x | 6/8 | 8/8 | 0/8 (8 above, 0 below) | 1.19x |
| kernl_fused_ff | A100 | ro_clamp (extra) | 256 | 1.14x | 0.94-1.39x | 1.13x | 0.70-1.76x | 194/256 | 256/256 | 148/256 (26 above, 82 below) | 1.12x |
| kernl_fused_ff | A100 | ro_clamp [occupancy changed] (extra) | 64 | 0.98x | 0.77-1.15x | 0.97x | 0.70-1.22x | 22/64 | 64/64 | 49/64 (1 above, 14 below) | 0.96x |
| kernl_fused_ff | A100 | ro_clamp [occupancy unchanged] (extra) | 192 | 1.17x | 1.01-1.43x | 1.19x | 0.87-1.76x | 172/192 | 192/192 | 99/192 (25 above, 68 below) | 1.18x |
| kernl_fused_ff | A100 | ro_full_tt32 (extra) | 64 | 1.19x | 1.07-1.25x | 1.17x | 0.98-1.35x | 62/64 | 64/64 | 26/64 (6 above, 32 below) | 1.18x |
| kernl_fused_ff | A100 | ro_full_tt32 [occupancy changed] (extra) | 4 | 1.12x | 0.98-1.27x | 1.11x | 0.98-1.27x | 2/4 | 4/4 | 3/4 (0 above, 1 below) | 1.12x |
| kernl_fused_ff | A100 | ro_full_tt32 [occupancy unchanged] (extra) | 60 | 1.19x | 1.08-1.25x | 1.17x | 1.02-1.35x | 60/60 | 60/60 | 23/60 (6 above, 31 below) | 1.18x |
| kernl_fused_ff | A100 | ro_full_tt32_vs_tt32 (extra) | 64 | 1.14x | 1.08-1.29x | 1.17x | 0.95-1.44x | 62/64 | 64/64 | 27/64 (4 above, 33 below) | 1.13x |
| kernl_fused_ff | A100 | ro_full_tt32_vs_tt32 [occupancy changed] (extra) | 4 | 1.04x | 0.95-1.18x | 1.05x | 0.95-1.20x | 2/4 | 4/4 | 0/4 (0 above, 4 below) | 1.05x |
| kernl_fused_ff | A100 | ro_full_tt32_vs_tt32 [occupancy unchanged] (extra) | 60 | 1.14x | 1.09-1.29x | 1.17x | 1.03-1.44x | 60/60 | 60/60 | 27/60 (4 above, 29 below) | 1.13x |
| kernl_fused_ff | A100 | ro_sweep (extra) | 10 | 1.08x | 1.04-1.34x | 1.13x | 1.01-1.34x | 9/10 | 10/10 | 5/10 (0 above, 5 below) | 1.09x |
| kernl_fused_ff | A100 | ro_tt32 (extra) | 256 | 1.16x | 1.01-1.31x | 1.14x | 0.66-1.53x | 221/256 | 256/256 | 181/256 (34 above, 41 below) | 1.17x |
| kernl_fused_ff | A100 | ro_tt32 [occupancy changed] (extra) | 32 | 1.06x | 0.71-1.28x | 1.01x | 0.66-1.32x | 19/32 | 32/32 | 21/32 (11 above, 0 below) | 1.07x |
| kernl_fused_ff | A100 | ro_tt32 [occupancy unchanged] (extra) | 224 | 1.17x | 1.03-1.32x | 1.17x | 0.91-1.53x | 202/224 | 224/224 | 160/224 (23 above, 41 below) | 1.18x |
| kernl_fused_ff | A100 | ro_tt32_vs_tt32 (extra) | 256 | 1.11x | 1.00-1.29x | 1.12x | 0.92-1.85x | 210/256 | 256/256 | 174/256 (32 above, 50 below) | 1.11x |
| kernl_fused_ff | A100 | ro_tt32_vs_tt32 [occupancy changed] (extra) | 34 | 1.08x | 1.00-1.24x | 1.10x | 0.95-1.32x | 25/34 | 34/34 | 32/34 (0 above, 2 below) | 1.05x |
| kernl_fused_ff | A100 | ro_tt32_vs_tt32 [occupancy unchanged] (extra) | 222 | 1.11x | 1.00-1.31x | 1.13x | 0.92-1.85x | 185/222 | 222/222 | 142/222 (32 above, 48 below) | 1.11x |
| kernl_fused_ff | A100 | ro_vs_ctl_r64 (extra) | 48 | 1.11x | 1.00-1.27x | 1.11x | 0.95-1.39x | 32/48 | 48/48 | 35/48 (4 above, 9 below) | 1.11x |
| kernl_fused_ff | A100 | ro_vs_ctl_r64 [occupancy changed] (extra) | 30 | 1.07x | 0.99-1.17x | 1.08x | 0.95-1.29x | 15/30 | 30/30 | 23/30 (2 above, 5 below) | 1.06x |
| kernl_fused_ff | A100 | ro_vs_ctl_r64 [occupancy unchanged] (extra) | 18 | 1.13x | 1.07-1.33x | 1.16x | 1.01-1.39x | 17/18 | 18/18 | 12/18 (2 above, 4 below) | 1.15x |
| kernl_fused_ff | A100 | ro_vs_tt32 (extra) | 256 | 1.12x | 0.91-1.29x | 1.11x | 0.76-1.60x | 197/256 | 256/256 | 158/256 (15 above, 83 below) | 1.12x |
| kernl_fused_ff | A100 | ro_vs_tt32 [occupancy changed] (extra) | 32 | 0.90x | 0.80-1.00x | 0.89x | 0.76-1.15x | 2/32 | 32/32 | 15/32 (5 above, 12 below) | 0.86x |
| kernl_fused_ff | A100 | ro_vs_tt32 [occupancy unchanged] (extra) | 224 | 1.14x | 1.02-1.29x | 1.14x | 0.85-1.60x | 195/224 | 224/224 | 143/224 (10 above, 71 below) | 1.14x |
| kernl_fused_ff | A100 | ro_vs_tt38 (extra) | 256 | 1.11x | 0.86-2.45x | 1.19x | 0.53-2.91x | 180/256 | 256/256 | 39/256 (214 above, 3 below) | 1.11x |
| kernl_fused_ff | A100 | ro_vs_tt38 [occupancy changed] (extra) | 46 | 2.47x | 1.03-2.77x | 1.94x | 0.88-2.91x | 42/46 | 46/46 | 5/46 (41 above, 0 below) | 2.12x |
| kernl_fused_ff | A100 | ro_vs_tt38 [occupancy unchanged] (extra) | 210 | 1.07x | 0.83-1.38x | 1.07x | 0.53-2.64x | 138/210 | 210/210 | 34/210 (173 above, 3 below) | 1.08x |
| kernl_fused_ff | A100 | tt32 (extra) | 256 | 1.01x | 0.93-1.16x | 1.02x | 0.65-1.33x | 121/256 | 256/256 | 119/256 (84 above, 53 below) | 1.01x |
| kernl_fused_ff | A100 | tt32 [occupancy changed] (extra) | 58 | 0.98x | 0.71-1.21x | 0.98x | 0.65-1.33x | 22/58 | 58/58 | 23/58 (27 above, 8 below) | 0.97x |
| kernl_fused_ff | A100 | tt32 [occupancy unchanged] (extra) | 198 | 1.02x | 0.95-1.14x | 1.03x | 0.68-1.30x | 99/198 | 198/198 | 96/198 (57 above, 45 below) | 1.02x |
| kernl_fused_ff | A100 | tt38 (extra) | 256 | 1.02x | 0.46-1.45x | 0.95x | 0.36-2.36x | 131/256 | 32/256 (224 differ) | 60/256 (4 above, 192 below) | 1.00x |
| kernl_fused_ff | A100 | tt38 [occupancy changed] (extra) | 78 | 0.69x | 0.37-0.98x | 0.64x | 0.36-1.20x | 7/78 | 2/78 (76 differ) | 6/78 (0 above, 72 below) | 0.66x |
| kernl_fused_ff | A100 | tt38 [occupancy unchanged] (extra) | 178 | 1.17x | 0.79-1.51x | 1.12x | 0.42-2.36x | 124/178 | 30/178 (148 differ) | 54/178 (4 above, 120 below) | 1.11x |
| kernl_rmsnorm | A100 | ro | 37 | 1.19x | 1.06-1.35x | 1.20x | 1.02-1.46x | 37/37 | 37/37 | 32/37 (0 above, 5 below) | - |
| kernl_rmsnorm | A100 | ro2 (extra) | 37 | 1.24x | 1.08-1.41x | 1.24x | 1.03-1.44x | 37/37 | 37/37 | 29/37 (2 above, 6 below) | - |
| kernl_rmsnorm | A100 | ro3 (extra) | 37 | 1.25x | 1.09-1.43x | 1.26x | 1.03-1.47x | 37/37 | 37/37 | 27/37 (2 above, 8 below) | - |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro | 27.159 | 19.712 | 1.378x | 1.069-1.772x | 1.371x | 1.40-1.69x | NO | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ctl_s2 | 27.159 | 31.930 | 0.851x | 0.660-1.095x | 0.852x | 0.73-0.88x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ctl_s5 | 27.159 | 27.136 | 1.001x | 0.777-1.287x | 0.998x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | kernl | 27.159 | 28.276 | 0.960x | 0.746-1.235x | 0.961x | 0.89-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro_clamp | 27.159 | 18.735 | 1.450x | 1.125-1.867x | 1.449x | 1.44-1.93x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32 | 27.159 | 22.831 | 1.190x | 0.925-1.533x | 1.190x | 1.04-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 24.343 | 22.831 | 1.066x | 0.828-1.372x | 1.054x | 0.88-1.13x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 24.343 | 19.712 | 1.235x | 0.956-1.586x | 1.214x | 1.18-1.51x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 18.665 | 19.712 | 0.947x | 0.733-1.216x | 0.936x | 0.71-0.84x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | tt32 | 27.159 | 24.343 | 1.116x | 0.868-1.439x | 1.129x | 1.09-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_warm | tt38 | 27.159 | 18.665 | 1.455x | 1.132-1.876x | 1.464x | 1.74-2.27x | NO | yes | 0 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro | 44.032 | 33.178 | 1.327x | 1.313-1.342x | 1.363x | 1.44-1.68x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ctl_s2 | 44.032 | 58.982 | 0.747x | 0.740-0.755x | 0.928x | 0.68-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ctl_s5 | 44.032 | 44.032 | 1.000x | 0.991-1.014x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | kernl | 44.032 | 45.466 | 0.968x | 0.960-0.982x | 0.961x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro_clamp | 44.032 | 29.286 | 1.503x | 1.476-1.521x | 1.582x | 1.59-1.73x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32 | 44.032 | 38.093 | 1.156x | 1.138-1.168x | 1.166x | 1.15-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 42.394 | 38.093 | 1.113x | 1.096-1.130x | 1.130x | 1.04-1.11x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 42.394 | 33.178 | 1.278x | 1.264-1.298x | 1.322x | 1.31-1.46x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 23.962 | 33.178 | 0.722x | 0.712-0.733x | 0.673x | 0.50-0.84x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | tt32 | 44.032 | 42.394 | 1.039x | 1.024-1.049x | 1.031x | 1.07-1.18x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s5_cold | tt38 | 44.032 | 23.962 | 1.838x | 1.814-1.862x | 2.025x | 2.01-2.82x | NO | yes | 0 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro | 20.046 | 18.339 | 1.093x | 1.092-1.094x | - | 0.78-1.09x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ctl_s2 | 20.046 | 25.848 | 0.776x | 0.774-0.776x | 0.771x | 0.67-0.80x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ctl_s5 | 20.046 | 20.046 | 1.000x | 0.999-1.001x | 0.994x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | kernl | 20.046 | 20.899 | 0.959x | 0.958-0.960x | 0.952x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro_clamp | 20.046 | 22.730 | 0.882x | 0.881-0.883x | 0.873x | 0.66-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32 | 20.046 | 16.337 | 1.227x | 1.225-1.227x | 1.213x | 1.04-1.42x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 20.294 | 16.337 | 1.242x | 1.240-1.243x | 1.228x | 1.15-1.50x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 20.294 | 18.339 | 1.107x | 1.106-1.108x | - | 0.86-1.15x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 18.091 | 18.339 | 0.986x | 0.986-0.988x | - | 0.66-0.82x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | tt32 | 20.046 | 20.294 | 0.988x | 0.986-0.989x | 0.988x | 0.88-0.98x | NO | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_warm | tt38 | 20.046 | 18.091 | 1.108x | 1.106-1.108x | 1.128x | 1.00-1.57x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro | 38.912 | 36.659 | 1.061x | 1.044-1.073x | - | 0.98-1.07x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ctl_s2 | 38.912 | 54.272 | 0.717x | 0.707-0.726x | 0.690x | 0.62-0.74x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ctl_s5 | 38.912 | 38.912 | 1.000x | 0.984-1.016x | 0.997x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | kernl | 38.912 | 39.526 | 0.984x | 0.969-1.000x | 0.977x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro_clamp | 38.912 | 29.901 | 1.301x | 1.270-1.317x | 1.346x | 0.83-1.34x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32 | 38.912 | 32.768 | 1.188x | 1.168-1.209x | 1.220x | 1.24-1.37x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 39.322 | 32.768 | 1.200x | 1.186-1.228x | 1.251x | 1.29-1.47x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 39.322 | 36.659 | 1.073x | 1.061-1.090x | - | 1.06-1.12x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 23.142 | 36.659 | 0.631x | 0.622-0.646x | - | 0.48-0.82x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | tt32 | 38.912 | 39.322 | 0.990x | 0.969-1.000x | 0.975x | 0.90-0.99x | NO | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_32x64x32_w2_s5_cold | tt38 | 38.912 | 23.142 | 1.681x | 1.635-1.705x | - | 1.25-2.08x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro | 31.803 | 22.823 | 1.393x | 1.392-1.394x | 1.392x | 1.37-1.51x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ctl_s2 | 31.803 | 31.823 | 0.999x | 0.999-1.001x | 1.002x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ctl_s5 | 31.803 | 27.077 | 1.175x | 1.175-1.176x | 1.177x | 1.15-1.34x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | kernl | 31.803 | 34.206 | 0.930x | 0.930-0.931x | 0.934x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro_clamp | 31.803 | 23.020 | 1.382x | 1.380-1.382x | 1.385x | 1.39-1.64x | NO | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32 | 31.803 | 27.412 | 1.160x | 1.159-1.161x | 1.171x | 1.02-1.20x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 28.199 | 27.412 | 1.029x | 1.027-1.029x | 1.032x | 0.86-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 28.199 | 22.823 | 1.236x | 1.234-1.236x | 1.227x | 1.15-1.37x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 23.119 | 22.823 | 1.013x | 1.012-1.013x | 0.996x | 0.81-0.89x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | tt32 | 31.803 | 28.199 | 1.128x | 1.128-1.129x | 1.134x | 1.08-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_warm | tt38 | 31.803 | 23.119 | 1.376x | 1.376-1.376x | 1.398x | 1.59-1.79x | NO | yes | 0 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro | 58.778 | 42.803 | 1.373x | 1.360-1.389x | 1.100x | 1.29-1.53x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ctl_s2 | 58.778 | 58.778 | 1.000x | 0.993-1.010x | 0.995x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ctl_s5 | 58.778 | 44.032 | 1.335x | 1.329-1.350x | 1.068x | 1.23-1.44x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | kernl | 58.778 | 61.235 | 0.960x | 0.960-0.973x | 0.954x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro_clamp | 58.778 | 42.803 | 1.373x | 1.360-1.389x | 1.095x | 1.50-1.75x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32 | 58.778 | 49.152 | 1.196x | 1.186-1.209x | 0.945x | 1.09-1.20x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 51.405 | 49.152 | 1.046x | 1.029-1.063x | 1.053x | 0.99-1.07x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 51.405 | 42.803 | 1.201x | 1.180-1.221x | 1.225x | 1.19-1.35x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 43.008 | 42.803 | 1.005x | 0.986-1.014x | 0.998x | 0.68-0.91x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | tt32 | 58.778 | 51.405 | 1.143x | 1.130-1.161x | 0.897x | 1.05-1.17x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x32x32_w2_s2_cold | tt38 | 58.778 | 43.008 | 1.367x | 1.360-1.389x | 1.102x | 1.68-1.89x | NO | yes | 0 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro | 30.379 | 30.741 | 0.988x | 0.987-0.989x | 0.988x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ctl_s2 | 30.379 | 34.859 | 0.871x | 0.870-0.873x | 0.869x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ctl_s5 | 30.379 | 30.549 | 0.994x | 0.994-0.996x | 0.995x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | kernl | 30.379 | 32.619 | 0.931x | 0.931-0.932x | 0.932x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_clamp | 30.379 | 28.416 | 1.069x | 1.068-1.070x | 1.059x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 30.379 | 28.139 | 1.080x | 1.078-1.081x | 1.073x | 1.09-1.49x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 30.848 | 28.139 | 1.096x | 1.095-1.098x | 1.086x | 1.10-1.51x | NO | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32 | 30.379 | 27.371 | 1.110x | 1.107-1.111x | 1.110x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 30.848 | 27.371 | 1.127x | 1.125-1.128x | 1.124x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 30.848 | 30.741 | 1.003x | 1.002-1.004x | 1.000x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.056 | 30.741 | 1.205x | 1.204-1.205x | 1.199x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | tt32 | 30.379 | 30.848 | 0.985x | 0.983-0.986x | 0.988x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_warm | tt38 | 30.379 | 37.056 | 0.820x | 0.819-0.821x | 0.824x | 1.00-1.41x | NO | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro | 50.381 | 41.779 | 1.206x | 1.189-1.228x | 1.240x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ctl_s2 | 50.381 | 65.126 | 0.774x | 0.768-0.782x | 0.978x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ctl_s5 | 50.381 | 50.176 | 1.004x | 0.996-1.016x | 1.010x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | kernl | 50.381 | 51.610 | 0.976x | 0.968-0.988x | 0.977x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_clamp | 50.381 | 41.370 | 1.218x | 1.207-1.234x | 1.256x | 1.19-1.29x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 50.381 | 40.960 | 1.230x | 1.219-1.253x | 1.269x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 50.790 | 40.960 | 1.240x | 1.229-1.258x | 1.270x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32 | 50.381 | 38.298 | 1.316x | 1.303-1.333x | 1.371x | 1.26-1.45x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 50.790 | 38.298 | 1.326x | 1.314-1.339x | 1.371x | 1.27-1.46x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 50.790 | 41.779 | 1.216x | 1.199-1.233x | 1.240x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 42.598 | 41.779 | 1.020x | 1.005-1.040x | 1.020x | 0.70-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | tt32 | 50.381 | 50.790 | 0.992x | 0.984-1.004x | 1.000x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_64x128x32_w4_s4_cold | tt38 | 50.381 | 42.598 | 1.183x | 1.167-1.198x | 1.215x | 1.17-1.76x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro | 14.267 | 11.989 | 1.190x | 1.189-1.192x | 1.208x | 1.08-1.39x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ctl_r64 | 14.267 | 14.255 | 1.001x | 1.000-1.002x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ctl_s2 | 14.267 | 14.278 | 0.999x | 0.999-1.001x | 1.005x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ctl_s5 | 14.267 | 12.012 | 1.188x | 1.187-1.190x | 1.199x | 1.14-1.34x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | kernl | 14.267 | 14.739 | 0.968x | 0.968-0.970x | 0.969x | 0.90-0.99x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_clamp | 14.267 | 12.127 | 1.176x | 1.175-1.179x | 1.180x | 1.05-1.37x | yes | yes | 0 | 4, 4 | 64, 80 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32 | 14.267 | 12.058 | 1.183x | 1.183-1.184x | 1.191x | 1.06-1.38x | yes | yes | 0 | 4, 4 | 64, 63 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 13.887 | 12.058 | 1.152x | 1.152-1.153x | 1.160x | 1.05-1.37x | yes | yes | 0 | 4, 4 | 68, 63 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 14.255 | 11.989 | 1.189x | 1.187-1.191x | 1.203x | 1.08-1.39x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 13.887 | 11.989 | 1.158x | 1.157-1.160x | 1.176x | 1.07-1.39x | yes | yes | 0 | 4, 4 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 16.913 | 11.989 | 1.411x | 1.409-1.413x | 1.446x | 0.91-0.99x | NO | yes | 0 | 4, 4 | 90, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | tt32 | 14.267 | 13.887 | 1.027x | 1.026-1.028x | 1.027x | 0.97-1.04x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_warm | tt38 | 14.267 | 16.913 | 0.844x | 0.843-0.844x | 0.835x | 1.15-1.45x | NO | NO | 1.53e-05 | 4, 4 | 64, 90 | warm |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro | 30.720 | 24.576 | 1.250x | 1.231-1.269x | 1.304x | 1.23-1.55x | yes | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ctl_r64 | 30.720 | 30.925 | 0.993x | 0.987-1.007x | 0.995x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ctl_s2 | 30.720 | 30.720 | 1.000x | 0.980-1.007x | 0.996x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ctl_s5 | 30.720 | 23.552 | 1.304x | 1.284-1.325x | - | 1.25-1.46x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | kernl | 30.720 | 31.334 | 0.980x | 0.961-0.993x | 0.976x | 0.92-1.00x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_clamp | 30.720 | 24.781 | 1.240x | 1.221-1.258x | 1.252x | 1.20-1.53x | yes | yes | 0 | 4, 4 | 64, 80 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32 | 30.720 | 24.371 | 1.261x | 1.242-1.280x | - | 1.21-1.54x | yes | yes | 0 | 4, 4 | 64, 63 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 28.058 | 24.371 | 1.151x | 1.142-1.178x | - | 1.21-1.54x | NO | yes | 0 | 4, 4 | 68, 63 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 30.925 | 24.576 | 1.258x | 1.240-1.269x | 1.311x | 1.23-1.55x | yes | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 28.058 | 24.576 | 1.142x | 1.132-1.168x | 1.175x | 1.22-1.55x | NO | yes | 0 | 4, 4 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 29.286 | 24.576 | 1.192x | 1.174-1.210x | 1.225x | 0.91-0.99x | NO | yes | 0 | 4, 4 | 90, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | tt32 | 30.720 | 28.058 | 1.095x | 1.072-1.102x | 1.110x | 0.97-1.04x | NO | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k1024_16x16x64_w4_s2_cold | tt38 | 30.720 | 29.286 | 1.049x | 1.035-1.063x | 1.064x | 1.30-1.61x | NO | NO | 1.53e-05 | 4, 4 | 64, 90 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro | 99.870 | 70.174 | 1.423x | 1.423-1.429x | 1.422x | 1.42-1.76x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ctl_s2 | 99.870 | 119.928 | 0.833x | 0.831-0.836x | 0.836x | 0.72-0.88x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ctl_s5 | 99.870 | 99.870 | 1.000x | 0.999-1.003x | 1.000x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | kernl | 99.870 | 104.749 | 0.953x | 0.953-0.956x | 0.951x | 0.89-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro_clamp | 99.870 | 66.138 | 1.510x | 1.509-1.515x | 1.510x | 1.47-2.04x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32 | 99.870 | 82.462 | 1.211x | 1.211-1.216x | 1.214x | 1.04-1.29x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 88.184 | 82.462 | 1.069x | 1.069-1.071x | 1.074x | 0.88-1.14x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 88.184 | 70.174 | 1.257x | 1.257-1.259x | 1.259x | 1.19-1.56x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 65.837 | 70.174 | 0.938x | 0.938-0.940x | 0.932x | 0.68-0.83x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | tt32 | 99.870 | 88.184 | 1.133x | 1.132-1.136x | 1.130x | 1.10-1.22x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_warm | tt38 | 99.870 | 65.837 | 1.517x | 1.516-1.522x | 1.526x | 1.79-2.46x | NO | yes | 0 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro | 153.805 | 112.026 | 1.373x | 1.364-1.383x | 1.386x | 1.48-1.72x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ctl_s2 | 153.805 | 213.402 | 0.721x | 0.718-0.725x | 0.713x | 0.67-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ctl_s5 | 153.805 | 154.010 | 0.999x | 0.993-1.005x | 0.994x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | kernl | 153.805 | 160.358 | 0.959x | 0.954-0.967x | 0.957x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro_clamp | 153.805 | 95.232 | 1.615x | 1.600-1.629x | 1.644x | 1.64-1.77x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32 | 153.805 | 131.686 | 1.168x | 1.159-1.174x | 1.174x | 1.16-1.28x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 149.299 | 131.686 | 1.134x | 1.125-1.139x | 1.138x | 1.05-1.11x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 149.299 | 112.026 | 1.333x | 1.324-1.341x | 1.344x | 1.34-1.49x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 71.270 | 112.026 | 0.636x | 0.632-0.640x | 0.621x | 0.46-0.83x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | tt32 | 153.805 | 149.299 | 1.030x | 1.025-1.037x | 1.031x | 1.07-1.19x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s5_cold | tt38 | 153.805 | 71.270 | 2.158x | 2.146-2.173x | 2.233x | 2.09-3.09x | yes | yes | 0 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro | 70.997 | 63.878 | 1.111x | 1.111-1.112x | 1.111x | 0.77-1.10x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ctl_s2 | 70.997 | 95.720 | 0.742x | 0.738-0.745x | 0.743x | 0.65-0.79x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ctl_s5 | 70.997 | 70.997 | 1.000x | 0.999-1.001x | 0.998x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | kernl | 70.997 | 74.703 | 0.950x | 0.950-0.951x | 0.945x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro_clamp | 70.997 | 81.432 | 0.872x | 0.871-0.872x | 0.873x | 0.65-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32 | 70.997 | 57.051 | 1.244x | 1.243-1.246x | 1.237x | 1.05-1.47x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 72.850 | 57.051 | 1.277x | 1.275-1.279x | 1.274x | 1.16-1.56x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 72.850 | 63.878 | 1.140x | 1.140-1.141x | 1.144x | 0.85-1.16x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 63.732 | 63.878 | 0.998x | 0.998-0.998x | 0.984x | 0.63-0.81x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | tt32 | 70.997 | 72.850 | 0.975x | 0.974-0.976x | 0.971x | 0.88-0.97x | NO | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_warm | tt38 | 70.997 | 63.732 | 1.114x | 1.113-1.115x | 1.129x | 1.00-1.65x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro | 135.782 | 129.024 | 1.052x | 1.047-1.057x | - | 0.98-1.08x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ctl_s2 | 135.782 | 196.198 | 0.692x | 0.689-0.696x | 0.687x | 0.61-0.73x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ctl_s5 | 135.782 | 135.782 | 1.000x | 0.995-1.006x | 0.998x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | kernl | 135.782 | 138.854 | 0.978x | 0.975-0.982x | 0.974x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro_clamp | 135.782 | 97.690 | 1.390x | 1.385-1.400x | 1.406x | 0.83-1.37x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32 | 135.782 | 114.074 | 1.190x | 1.184-1.200x | 1.202x | 1.26-1.40x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 140.902 | 114.074 | 1.235x | 1.227-1.244x | 1.251x | 1.32-1.50x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 140.902 | 129.024 | 1.092x | 1.085-1.095x | - | 1.06-1.13x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 68.198 | 129.024 | 0.529x | 0.524-0.531x | - | 0.45-0.81x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | tt32 | 135.782 | 140.902 | 0.964x | 0.961-0.969x | 0.961x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_32x64x32_w2_s5_cold | tt38 | 135.782 | 68.198 | 1.991x | 1.982-2.009x | - | 1.27-2.23x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro | 119.552 | 82.752 | 1.445x | 1.443-1.445x | 1.449x | 1.39-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ctl_s2 | 119.552 | 119.552 | 1.000x | 0.999-1.001x | 1.000x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ctl_s5 | 119.552 | 99.968 | 1.196x | 1.194-1.197x | 1.195x | 1.15-1.36x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | kernl | 119.552 | 129.408 | 0.924x | 0.923-0.924x | 0.922x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro_clamp | 119.552 | 83.904 | 1.425x | 1.423-1.427x | 1.421x | 1.41-1.68x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32 | 119.552 | 101.696 | 1.176x | 1.173-1.176x | 1.176x | 1.02-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 105.536 | 101.696 | 1.038x | 1.035-1.039x | 1.035x | 0.85-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 105.536 | 82.752 | 1.275x | 1.274-1.277x | 1.275x | 1.16-1.39x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 84.736 | 82.752 | 1.024x | 1.022-1.026x | 1.026x | 0.80-0.88x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | tt32 | 119.552 | 105.536 | 1.133x | 1.131-1.134x | 1.136x | 1.09-1.22x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_warm | tt38 | 119.552 | 84.736 | 1.411x | 1.407-1.413x | 1.412x | 1.63-1.86x | NO | yes | 0 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro | 213.606 | 150.528 | 1.419x | 1.409-1.426x | 1.439x | 1.31-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ctl_s2 | 213.606 | 213.197 | 1.002x | 0.996-1.006x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ctl_s5 | 213.606 | 153.805 | 1.389x | 1.382-1.395x | 1.398x | 1.24-1.46x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | kernl | 213.606 | 223.232 | 0.957x | 0.953-0.961x | 0.956x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro_clamp | 213.606 | 149.709 | 1.427x | 1.416-1.433x | 1.440x | 1.52-1.80x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32 | 213.606 | 182.886 | 1.168x | 1.157-1.182x | 1.181x | 1.10-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 197.632 | 182.886 | 1.081x | 1.064-1.095x | 1.092x | 1.00-1.07x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 197.632 | 150.528 | 1.313x | 1.296-1.321x | 1.332x | 1.20-1.36x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 149.914 | 150.528 | 0.996x | 0.991-1.000x | 0.999x | 0.67-0.90x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | tt32 | 213.606 | 197.632 | 1.081x | 1.075-1.091x | 1.081x | 1.05-1.18x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x32x32_w2_s2_cold | tt38 | 213.606 | 149.914 | 1.425x | 1.420-1.428x | 1.440x | 1.71-1.94x | NO | yes | 0 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro | 108.398 | 109.787 | 0.987x | 0.985-0.989x | 0.988x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ctl_s2 | 108.398 | 126.683 | 0.856x | 0.854-0.858x | 0.860x | 0.71-0.86x | yes | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ctl_s5 | 108.398 | 108.325 | 1.001x | 0.999-1.003x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | kernl | 108.398 | 117.833 | 0.920x | 0.919-0.922x | 0.922x | 0.95-1.01x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_clamp | 108.398 | 99.840 | 1.086x | 1.083-1.089x | 1.088x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 108.398 | 102.693 | 1.056x | 1.053-1.058x | 1.060x | 1.10-1.54x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 112.859 | 102.693 | 1.099x | 1.096-1.100x | 1.100x | 1.11-1.55x | NO | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32 | 108.398 | 99.621 | 1.088x | 1.080-1.101x | 1.092x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 112.859 | 99.621 | 1.133x | 1.125-1.145x | 1.133x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 112.859 | 109.787 | 1.028x | 1.026-1.029x | 1.025x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 139.995 | 109.787 | 1.275x | 1.248-1.301x | 1.295x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | tt32 | 108.398 | 112.859 | 0.960x | 0.959-0.963x | 0.964x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_warm | tt38 | 108.398 | 139.995 | 0.774x | 0.759-0.791x | 0.763x | 1.00-1.44x | NO | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro | 177.152 | 141.107 | 1.255x | 1.247-1.263x | 1.263x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ctl_s2 | 177.152 | 235.315 | 0.753x | 0.751-0.757x | 0.746x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ctl_s5 | 177.152 | 176.742 | 1.002x | 0.995-1.008x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | kernl | 177.152 | 183.091 | 0.968x | 0.962-0.972x | 0.966x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_clamp | 177.152 | 140.698 | 1.259x | 1.253-1.269x | 1.277x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 177.152 | 141.312 | 1.254x | 1.244-1.262x | 1.275x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 182.067 | 141.312 | 1.288x | 1.278-1.295x | 1.308x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32 | 177.152 | 131.072 | 1.352x | 1.344-1.361x | 1.370x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 182.067 | 131.072 | 1.389x | 1.382-1.397x | 1.406x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 182.067 | 141.107 | 1.290x | 1.282-1.297x | 1.295x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 144.589 | 141.107 | 1.025x | 1.019-1.029x | 1.025x | 0.68-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | tt32 | 177.152 | 182.067 | 0.973x | 0.969-0.979x | 0.975x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_64x128x32_w4_s4_cold | tt38 | 177.152 | 144.589 | 1.225x | 1.221-1.231x | 1.232x | 1.18-1.82x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro | 50.738 | 41.356 | 1.227x | 1.225-1.229x | 1.236x | 1.09-1.45x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ctl_r64 | 50.738 | 50.738 | 1.000x | 0.999-1.001x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ctl_s2 | 50.738 | 50.738 | 1.000x | 0.999-1.001x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ctl_s5 | 50.738 | 41.489 | 1.223x | 1.222-1.225x | 1.234x | 1.16-1.39x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | kernl | 50.738 | 52.885 | 0.959x | 0.958-0.961x | 1.233x | 0.89-0.99x | yes | yes | 0 | 4, 4 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_clamp | 50.738 | 42.116 | 1.205x | 1.203-1.205x | 1.199x | 1.05-1.42x | yes | yes | 0 | 4, 4 | 64, 80 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32 | 50.738 | 41.720 | 1.216x | 1.214-1.218x | 1.216x | 1.07-1.44x | yes | yes | 0 | 4, 4 | 64, 63 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 49.218 | 41.720 | 1.180x | 1.178-1.181x | 1.181x | 1.06-1.43x | yes | yes | 0 | 4, 4 | 68, 63 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 50.738 | 41.356 | 1.227x | 1.225-1.228x | 1.237x | 1.09-1.45x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 49.218 | 41.356 | 1.190x | 1.188-1.191x | 1.201x | 1.08-1.44x | yes | yes | 0 | 4, 4 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 61.539 | 41.356 | 1.488x | 1.486-1.489x | 1.170x | 0.90-0.98x | NO | yes | 0 | 4, 4 | 90, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | tt32 | 50.738 | 49.218 | 1.031x | 1.030-1.032x | 1.030x | 0.97-1.04x | yes | yes | 0 | 4, 4 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_warm | tt38 | 50.738 | 61.539 | 0.824x | 0.824-0.825x | 1.057x | 1.17-1.53x | NO | yes | 0 | 4, 4 | 64, 90 | warm |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro | 102.810 | 77.619 | 1.325x | 1.312-1.334x | 1.337x | 1.25-1.62x | yes | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ctl_r64 | 102.810 | 102.810 | 1.000x | 0.992-1.006x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ctl_s2 | 102.810 | 103.014 | 0.998x | 0.992-1.004x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ctl_s5 | 102.810 | 75.776 | 1.357x | 1.344-1.363x | - | 1.27-1.50x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | kernl | 102.810 | 105.062 | 0.979x | 0.971-0.984x | 0.979x | 0.91-1.00x | yes | yes | 0 | 4, 4 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_clamp | 102.810 | 78.438 | 1.311x | 1.299-1.317x | 1.317x | 1.22-1.59x | yes | yes | 0 | 4, 4 | 64, 80 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32 | 102.810 | 77.824 | 1.321x | 1.312-1.327x | - | 1.24-1.61x | yes | yes | 0 | 4, 4 | 64, 63 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 91.341 | 77.824 | 1.174x | 1.168-1.182x | - | 1.23-1.60x | NO | yes | 0 | 4, 4 | 68, 63 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 102.810 | 77.619 | 1.325x | 1.312-1.337x | 1.337x | 1.25-1.62x | yes | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 91.341 | 77.619 | 1.177x | 1.168-1.188x | 1.184x | 1.24-1.61x | NO | yes | 0 | 4, 4 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 96.461 | 77.619 | 1.243x | 1.234-1.255x | 1.254x | 0.91-0.99x | NO | yes | 0 | 4, 4 | 90, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | tt32 | 102.810 | 91.341 | 1.126x | 1.116-1.130x | 1.130x | 0.97-1.04x | NO | yes | 0 | 4, 4 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n1024_k4096_16x16x64_w4_s2_cold | tt38 | 102.810 | 96.461 | 1.066x | 1.057-1.070x | 1.066x | 1.33-1.69x | NO | yes | 0 | 4, 4 | 64, 90 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro | 28.034 | 27.300 | 1.027x | 1.025-1.030x | 1.041x | 1.40-1.69x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ctl_s2 | 28.034 | 32.787 | 0.855x | 0.853-0.859x | 0.850x | 0.73-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ctl_s5 | 28.034 | 28.015 | 1.001x | 0.997-1.003x | 0.993x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | kernl | 28.034 | 29.909 | 0.937x | 0.934-0.941x | 0.929x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro_clamp | 28.034 | 26.643 | 1.052x | 1.051-1.056x | 1.069x | 1.44-1.93x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32 | 28.034 | 28.730 | 0.976x | 0.974-0.978x | 0.981x | 1.04-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 31.937 | 28.730 | 1.112x | 1.110-1.114x | 1.117x | 0.88-1.13x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 31.937 | 27.300 | 1.170x | 1.169-1.172x | 1.184x | 1.18-1.51x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 31.841 | 27.300 | 1.166x | 1.165-1.167x | 1.170x | 0.71-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | tt32 | 28.034 | 31.937 | 0.878x | 0.876-0.880x | 0.879x | 1.09-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_warm | tt38 | 28.034 | 31.841 | 0.880x | 0.879-0.883x | 0.889x | 1.74-2.27x | NO | NO | 0.000977 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro | 54.067 | 44.646 | 1.211x | 1.186-1.226x | 1.240x | 1.44-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ctl_s2 | 54.067 | 70.861 | 0.763x | 0.753-0.776x | 0.956x | 0.68-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ctl_s5 | 54.067 | 54.067 | 1.000x | 0.985-1.011x | 1.003x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | kernl | 54.067 | 55.706 | 0.971x | 0.956-0.982x | 0.968x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro_clamp | 54.067 | 45.670 | 1.184x | 1.164-1.204x | 1.223x | 1.59-1.73x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32 | 54.067 | 49.971 | 1.082x | 1.065-1.095x | 1.116x | 1.15-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 57.549 | 49.971 | 1.152x | 1.138-1.165x | 0.939x | 1.04-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 57.549 | 44.646 | 1.289x | 1.267-1.304x | 1.043x | 1.31-1.46x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 39.731 | 44.646 | 0.890x | 0.869-0.908x | 0.862x | 0.59-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | tt32 | 54.067 | 57.549 | 0.940x | 0.926-0.950x | 1.189x | 1.07-1.18x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s5_cold | tt38 | 54.067 | 39.731 | 1.361x | 1.330-1.385x | 1.438x | 2.01-2.41x | NO | NO | 0.000977 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro | 20.418 | 18.541 | 1.101x | 1.099-1.102x | - | 0.78-1.09x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ctl_s2 | 20.418 | 27.400 | 0.745x | 0.744-0.747x | 0.759x | 0.67-0.80x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ctl_s5 | 20.418 | 20.418 | 1.000x | 0.998-1.002x | 1.007x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | kernl | 20.418 | 21.240 | 0.961x | 0.960-0.963x | 0.959x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro_clamp | 20.418 | 22.869 | 0.893x | 0.892-0.893x | 0.889x | 0.66-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32 | 20.418 | 16.524 | 1.236x | 1.234-1.238x | 1.232x | 1.04-1.42x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 21.333 | 16.524 | 1.291x | 1.289-1.297x | 1.275x | 1.15-1.50x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 21.333 | 18.541 | 1.151x | 1.149-1.155x | - | 0.86-1.15x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 18.386 | 18.541 | 0.992x | 0.990-0.992x | - | 0.66-0.82x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | tt32 | 20.418 | 21.333 | 0.957x | 0.953-0.959x | 0.966x | 0.88-0.98x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_warm | tt38 | 20.418 | 18.386 | 1.111x | 1.110-1.112x | 1.120x | 1.00-1.57x | yes | NO | 0.000977 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro | 47.309 | 46.080 | 1.027x | 1.018-1.045x | - | 0.98-1.07x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ctl_s2 | 47.309 | 66.355 | 0.713x | 0.703-0.724x | 0.883x | 0.62-0.74x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ctl_s5 | 47.309 | 47.514 | 0.996x | 0.991-1.013x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | kernl | 47.309 | 47.923 | 0.987x | 0.979-1.004x | 0.981x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro_clamp | 47.309 | 42.803 | 1.105x | 1.095-1.126x | 1.113x | 0.83-1.34x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32 | 47.309 | 43.827 | 1.079x | 1.070-1.099x | 1.103x | 1.24-1.37x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 48.742 | 43.827 | 1.112x | 1.098-1.127x | 1.139x | 1.29-1.47x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 48.742 | 46.080 | 1.058x | 1.044-1.072x | - | 1.06-1.12x | NO | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 32.358 | 46.080 | 0.702x | 0.690-0.713x | - | 0.53-0.82x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | tt32 | 47.309 | 48.742 | 0.971x | 0.962-0.987x | 0.968x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_32x64x32_w2_s5_cold | tt38 | 47.309 | 32.358 | 1.462x | 1.447-1.494x | - | 1.25-1.89x | yes | NO | 0.000977 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro | 32.748 | 28.090 | 1.166x | 1.163-1.171x | 1.181x | 1.37-1.51x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ctl_s2 | 32.748 | 32.748 | 1.000x | 0.997-1.003x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ctl_s5 | 32.748 | 28.070 | 1.167x | 1.162-1.170x | 1.169x | 1.15-1.34x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | kernl | 32.748 | 35.258 | 0.929x | 0.926-0.932x | 0.925x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro_clamp | 32.748 | 28.291 | 1.158x | 1.152-1.162x | 1.181x | 1.39-1.64x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32 | 32.748 | 30.218 | 1.084x | 1.081-1.087x | 1.073x | 1.02-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 30.780 | 30.218 | 1.019x | 1.015-1.021x | 1.008x | 0.86-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 30.780 | 28.090 | 1.096x | 1.091-1.100x | 1.109x | 1.15-1.37x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 31.804 | 28.090 | 1.132x | 1.128-1.138x | 1.130x | 0.81-0.89x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | tt32 | 32.748 | 30.780 | 1.064x | 1.061-1.069x | 1.065x | 1.08-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_warm | tt38 | 32.748 | 31.804 | 1.030x | 1.026-1.034x | 1.045x | 1.59-1.79x | NO | NO | 0.000977 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro | 70.861 | 52.224 | 1.357x | 1.344-1.370x | 1.093x | 1.29-1.53x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ctl_s2 | 70.861 | 70.656 | 1.003x | 0.986-1.012x | 0.998x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ctl_s5 | 70.861 | 54.067 | 1.311x | 1.279-1.323x | 1.056x | 1.23-1.44x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | kernl | 70.861 | 72.909 | 0.972x | 0.956-0.983x | 0.984x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro_clamp | 70.861 | 53.453 | 1.326x | 1.308-1.344x | 1.077x | 1.50-1.75x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32 | 70.861 | 58.573 | 1.210x | 1.190-1.225x | 1.235x | 1.09-1.20x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 60.006 | 58.573 | 1.024x | 1.003-1.049x | 1.027x | 0.99-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 60.006 | 52.224 | 1.149x | 1.133-1.173x | 0.909x | 1.19-1.35x | NO | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 54.682 | 52.224 | 1.047x | 1.035-1.063x | 1.051x | 0.68-0.91x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | tt32 | 70.861 | 60.006 | 1.181x | 1.154-1.200x | 1.202x | 1.05-1.17x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x32x32_w2_s2_cold | tt38 | 70.861 | 54.682 | 1.296x | 1.274-1.313x | 1.039x | 1.68-1.89x | NO | NO | 0.000977 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro | 31.417 | 31.156 | 1.008x | 1.008-1.009x | 1.003x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ctl_s2 | 31.417 | 36.036 | 0.872x | 0.872-0.872x | 0.871x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ctl_s5 | 31.417 | 31.504 | 0.997x | 0.997-0.997x | 0.993x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | kernl | 31.417 | 33.356 | 0.942x | 0.941-0.942x | 0.939x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_clamp | 31.417 | 28.628 | 1.097x | 1.097-1.097x | 1.089x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 31.417 | 28.345 | 1.108x | 1.108-1.109x | 1.106x | 1.09-1.49x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 31.744 | 28.345 | 1.120x | 1.119-1.123x | 1.123x | 1.10-1.51x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32 | 31.417 | 27.626 | 1.137x | 1.122-1.138x | 1.122x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 31.744 | 27.626 | 1.149x | 1.134-1.152x | 1.139x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 31.744 | 31.156 | 1.019x | 1.019-1.022x | 1.019x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.387 | 31.156 | 1.200x | 1.199-1.209x | 1.200x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | tt32 | 31.417 | 31.744 | 0.990x | 0.988-0.990x | 0.985x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_warm | tt38 | 31.417 | 37.387 | 0.840x | 0.834-0.841x | 0.836x | 1.00-1.41x | NO | NO | 0.000977 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro | 57.549 | 50.381 | 1.142x | 1.134-1.155x | 0.905x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ctl_s2 | 57.549 | 75.776 | 0.759x | 0.753-0.765x | 0.741x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ctl_s5 | 57.549 | 57.139 | 1.007x | 0.996-1.018x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | kernl | 57.549 | 58.778 | 0.979x | 0.966-0.990x | 0.970x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_clamp | 57.549 | 49.971 | 1.152x | 1.138-1.169x | 0.915x | 1.19-1.29x | NO | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 57.549 | 49.357 | 1.166x | 1.157-1.184x | 0.921x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 58.163 | 49.357 | 1.178x | 1.165-1.192x | 0.936x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32 | 57.549 | 47.514 | 1.211x | 1.202-1.225x | 0.965x | 1.26-1.45x | NO | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 58.163 | 47.514 | 1.224x | 1.210-1.234x | 0.982x | 1.27-1.46x | NO | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 58.163 | 50.381 | 1.154x | 1.142-1.163x | 0.920x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 44.646 | 50.381 | 0.886x | 0.874-0.894x | 0.875x | 0.70-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | tt32 | 57.549 | 58.163 | 0.989x | 0.982-1.004x | 0.983x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_64x128x32_w4_s4_cold | tt38 | 57.549 | 44.646 | 1.289x | 1.279-1.310x | 1.034x | 1.17-1.76x | yes | NO | 0.000977 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro | 18.244 | 16.468 | 1.108x | 1.105-1.109x | 1.114x | 1.08-1.39x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ctl_r64 | 18.244 | 18.223 | 1.001x | 0.999-1.001x | 0.997x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ctl_s2 | 18.244 | 18.244 | 1.000x | 0.998-1.001x | 0.996x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ctl_s5 | 18.244 | 17.554 | 1.039x | 1.037-1.041x | 1.043x | 1.14-1.34x | NO | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | kernl | 18.244 | 18.578 | 0.982x | 0.980-0.982x | 0.976x | 0.90-0.99x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_clamp | 18.244 | 16.886 | 1.080x | 1.078-1.082x | 1.070x | 1.05-1.37x | yes | yes | 0 | 12, 12 | 64, 80 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32 | 18.244 | 16.342 | 1.116x | 1.112-1.118x | - | 1.06-1.38x | yes | yes | 0 | 12, 12 | 64, 63 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 19.122 | 16.342 | 1.170x | 1.166-1.172x | - | 1.05-1.37x | yes | yes | 0 | 12, 12 | 68, 63 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 18.223 | 16.468 | 1.107x | 1.105-1.109x | 1.118x | 1.08-1.39x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 19.122 | 16.468 | 1.161x | 1.158-1.163x | 1.173x | 1.07-1.39x | yes | yes | 0 | 12, 12 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 35.318 | 16.468 | 2.145x | 2.142-2.149x | 2.213x | 0.91-0.99x | NO | yes | 0 | 12, 12 | 90, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | tt32 | 18.244 | 19.122 | 0.954x | 0.953-0.955x | 0.950x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_warm | tt38 | 18.244 | 35.318 | 0.517x | 0.516-0.517x | 0.503x | 1.15-1.45x | NO | NO | 0.000122 | 12, 12 | 64, 90 | warm |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro | 41.984 | 34.202 | 1.228x | 1.214-1.255x | 1.286x | 1.23-1.55x | yes | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ctl_r64 | 41.984 | 41.984 | 1.000x | 0.990-1.020x | 1.008x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ctl_s2 | 41.984 | 41.984 | 1.000x | 0.986-1.015x | 0.999x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ctl_s5 | 41.984 | 35.635 | 1.178x | 1.159-1.197x | - | 1.25-1.46x | NO | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | kernl | 41.984 | 41.984 | 1.000x | 0.981-1.020x | 0.983x | 0.92-1.00x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_clamp | 41.984 | 34.611 | 1.213x | 1.193-1.232x | 1.222x | 1.20-1.53x | yes | yes | 0 | 12, 12 | 64, 80 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32 | 41.984 | 33.997 | 1.235x | 1.214-1.262x | - | 1.21-1.54x | yes | yes | 0 | 12, 12 | 64, 63 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 36.864 | 33.997 | 1.084x | 1.065-1.110x | - | 1.21-1.54x | NO | yes | 0 | 12, 12 | 68, 63 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 41.984 | 34.202 | 1.228x | 1.208-1.248x | 1.277x | 1.23-1.55x | yes | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 36.864 | 34.202 | 1.078x | 1.065-1.103x | 1.114x | 1.22-1.55x | NO | yes | 0 | 12, 12 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 49.971 | 34.202 | 1.461x | 1.446-1.485x | 1.567x | 0.91-1.03x | NO | yes | 0 | 12, 12 | 90, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | tt32 | 41.984 | 36.864 | 1.139x | 1.121-1.156x | 1.155x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k1024_16x16x64_w4_s2_cold | tt38 | 41.984 | 49.971 | 0.840x | 0.833-0.852x | 0.821x | 1.30-1.56x | NO | NO | 0.000122 | 12, 12 | 64, 90 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro | 161.280 | 118.170 | 1.365x | 1.358-1.369x | 1.369x | 1.42-1.76x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ctl_s2 | 161.280 | 212.582 | 0.759x | 0.756-0.760x | 0.756x | 0.72-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ctl_s5 | 161.280 | 161.178 | 1.001x | 0.997-1.002x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | kernl | 161.280 | 168.755 | 0.956x | 0.953-0.957x | 0.958x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro_clamp | 161.280 | 118.886 | 1.357x | 1.348-1.361x | 1.360x | 1.47-2.04x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32 | 161.280 | 140.493 | 1.148x | 1.144-1.150x | 1.156x | 1.04-1.29x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 174.080 | 140.493 | 1.239x | 1.236-1.242x | 1.243x | 0.88-1.14x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 174.080 | 118.170 | 1.473x | 1.466-1.479x | 1.472x | 1.19-1.56x | yes | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 117.555 | 118.170 | 0.995x | 0.988-0.998x | 0.994x | 0.77-1.00x | yes | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | tt32 | 161.280 | 174.080 | 0.926x | 0.924-0.928x | 0.930x | 1.10-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_warm | tt38 | 161.280 | 117.555 | 1.372x | 1.368-1.378x | 1.377x | 1.75-2.07x | NO | NO | 0.00391 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro | 177.562 | 137.830 | 1.288x | 1.280-1.295x | 1.310x | 1.48-1.72x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ctl_s2 | 177.562 | 235.110 | 0.755x | 0.747-0.760x | 0.745x | 0.67-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ctl_s5 | 177.562 | 177.357 | 1.001x | 0.995-1.006x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | kernl | 177.562 | 184.730 | 0.961x | 0.956-0.966x | 0.959x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro_clamp | 177.562 | 139.878 | 1.269x | 1.259-1.278x | 1.278x | 1.64-1.77x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32 | 177.562 | 157.901 | 1.125x | 1.116-1.129x | 1.127x | 1.16-1.28x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 190.259 | 157.901 | 1.205x | 1.198-1.209x | 1.211x | 1.05-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 190.259 | 137.830 | 1.380x | 1.373-1.387x | 1.407x | 1.34-1.49x | yes | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 124.928 | 137.830 | 0.906x | 0.899-0.912x | 0.914x | 0.56-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | tt32 | 177.562 | 190.259 | 0.933x | 0.928-0.937x | 0.931x | 1.07-1.19x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s5_cold | tt38 | 177.562 | 124.928 | 1.421x | 1.412-1.432x | 1.433x | 2.09-2.60x | NO | NO | 0.00391 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro | 131.072 | 126.157 | 1.039x | 1.036-1.041x | 1.032x | 0.77-1.10x | yes | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ctl_s2 | 131.072 | 209.203 | 0.627x | 0.625-0.628x | 0.624x | 0.65-0.79x | NO | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ctl_s5 | 131.072 | 130.970 | 1.001x | 0.998-1.004x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | kernl | 131.072 | 134.451 | 0.975x | 0.973-0.979x | 0.975x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro_clamp | 131.072 | 109.056 | 1.202x | 1.199-1.211x | 1.210x | 0.65-1.10x | NO | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32 | 131.072 | 112.128 | 1.169x | 1.167-1.174x | 1.175x | 1.05-1.47x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 137.216 | 112.128 | 1.224x | 1.221-1.228x | 1.229x | 1.16-1.56x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 137.216 | 126.157 | 1.088x | 1.084-1.089x | 1.080x | 0.85-1.16x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 69.837 | 126.157 | 0.554x | 0.551-0.556x | 0.543x | 0.70-0.87x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | tt32 | 131.072 | 137.216 | 0.955x | 0.954-0.958x | 0.956x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_warm | tt38 | 131.072 | 69.837 | 1.877x | 1.867-1.885x | 1.899x | 1.00-1.49x | NO | NO | 0.00391 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro | 149.914 | 143.974 | 1.041x | 1.035-1.047x | - | 0.98-1.08x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ctl_s2 | 149.914 | 226.918 | 0.661x | 0.657-0.664x | 0.650x | 0.61-0.73x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ctl_s5 | 149.914 | 149.914 | 1.000x | 0.995-1.005x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | kernl | 149.914 | 152.781 | 0.981x | 0.977-0.987x | 0.984x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro_clamp | 149.914 | 127.590 | 1.175x | 1.164-1.184x | 1.188x | 0.83-1.37x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32 | 149.914 | 132.506 | 1.131x | 1.125-1.138x | 1.136x | 1.26-1.40x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 155.034 | 132.506 | 1.170x | 1.163-1.177x | 1.177x | 1.32-1.50x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 155.034 | 143.974 | 1.077x | 1.071-1.083x | - | 1.06-1.13x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 87.450 | 143.974 | 0.607x | 0.600-0.613x | - | 0.50-0.81x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | tt32 | 149.914 | 155.034 | 0.967x | 0.962-0.972x | 0.965x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_32x64x32_w2_s5_cold | tt38 | 149.914 | 87.450 | 1.714x | 1.698-1.735x | - | 1.27-2.01x | yes | NO | 0.00391 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro | 212.878 | 150.642 | 1.413x | 1.407-1.419x | 1.414x | 1.39-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ctl_s2 | 212.878 | 213.106 | 0.999x | 0.996-1.002x | 0.998x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ctl_s5 | 212.878 | 161.451 | 1.319x | 1.315-1.323x | 1.321x | 1.15-1.36x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | kernl | 212.878 | 220.956 | 0.963x | 0.961-0.966x | 0.963x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro_clamp | 212.878 | 158.037 | 1.347x | 1.342-1.353x | 1.354x | 1.41-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32 | 212.878 | 179.086 | 1.189x | 1.183-1.195x | 1.192x | 1.02-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 194.674 | 179.086 | 1.087x | 1.082-1.093x | 1.088x | 0.85-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 194.674 | 150.642 | 1.292x | 1.287-1.298x | 1.291x | 1.16-1.39x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 165.205 | 150.642 | 1.097x | 1.088-1.105x | 1.099x | 0.80-0.88x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | tt32 | 212.878 | 194.674 | 1.094x | 1.090-1.097x | 1.096x | 1.09-1.22x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_warm | tt38 | 212.878 | 165.205 | 1.289x | 1.280-1.297x | 1.287x | 1.63-1.86x | NO | NO | 0.00391 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro | 235.315 | 167.731 | 1.403x | 1.389-1.413x | 1.419x | 1.31-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ctl_s2 | 235.315 | 235.110 | 1.001x | 0.993-1.011x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ctl_s5 | 235.315 | 177.357 | 1.327x | 1.314-1.333x | 1.340x | 1.24-1.46x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | kernl | 235.315 | 242.688 | 0.970x | 0.961-0.975x | 0.970x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro_clamp | 235.315 | 172.646 | 1.363x | 1.353-1.374x | 1.386x | 1.52-1.80x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32 | 235.315 | 197.018 | 1.194x | 1.183-1.205x | 1.204x | 1.10-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 208.486 | 197.018 | 1.058x | 1.048-1.071x | 1.064x | 1.00-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 208.486 | 167.731 | 1.243x | 1.230-1.256x | 1.254x | 1.20-1.36x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 177.766 | 167.731 | 1.060x | 1.047-1.067x | 1.059x | 0.67-0.90x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | tt32 | 235.315 | 208.486 | 1.129x | 1.115-1.139x | 1.132x | 1.05-1.18x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x32x32_w2_s2_cold | tt38 | 235.315 | 177.766 | 1.324x | 1.312-1.338x | 1.340x | 1.71-1.94x | NO | NO | 0.00391 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro | 173.952 | 139.648 | 1.246x | 1.242-1.252x | 1.246x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ctl_s2 | 173.952 | 251.264 | 0.692x | 0.691-0.694x | 0.690x | 0.71-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ctl_s5 | 173.952 | 172.928 | 1.006x | 1.003-1.010x | 1.010x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | kernl | 173.952 | 180.736 | 0.962x | 0.960-0.967x | 0.960x | 0.95-1.01x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_clamp | 173.952 | 139.008 | 1.251x | 1.245-1.258x | 1.251x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 173.952 | 139.264 | 1.249x | 1.243-1.253x | 1.253x | 1.10-1.54x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 179.840 | 139.264 | 1.291x | 1.282-1.295x | 1.297x | 1.11-1.55x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32 | 173.952 | 129.024 | 1.348x | 1.342-1.354x | 1.350x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 179.840 | 129.024 | 1.394x | 1.385-1.400x | 1.398x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 179.840 | 139.648 | 1.288x | 1.281-1.294x | 1.290x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 146.432 | 139.648 | 1.049x | 1.012-1.052x | 1.047x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | tt32 | 173.952 | 179.840 | 0.967x | 0.964-0.973x | 0.966x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_warm | tt38 | 173.952 | 146.432 | 1.188x | 1.185-1.231x | 1.191x | 1.00-1.44x | yes | NO | 0.00391 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro | 188.621 | 156.262 | 1.207x | 1.201-1.214x | 1.209x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ctl_s2 | 188.621 | 265.830 | 0.710x | 0.707-0.713x | 0.702x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ctl_s5 | 188.621 | 188.211 | 1.002x | 0.997-1.009x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | kernl | 188.621 | 194.355 | 0.970x | 0.965-0.977x | 0.967x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_clamp | 188.621 | 155.853 | 1.210x | 1.203-1.217x | 1.211x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 188.621 | 155.853 | 1.210x | 1.204-1.216x | 1.212x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 193.331 | 155.853 | 1.240x | 1.235-1.245x | 1.246x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32 | 188.621 | 146.842 | 1.285x | 1.278-1.291x | 1.295x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 193.331 | 146.842 | 1.317x | 1.310-1.321x | 1.331x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 193.331 | 156.262 | 1.237x | 1.231-1.243x | 1.243x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 146.432 | 156.262 | 0.937x | 0.933-0.941x | 0.933x | 0.68-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | tt32 | 188.621 | 193.331 | 0.976x | 0.971-0.981x | 0.973x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_64x128x32_w4_s4_cold | tt38 | 188.621 | 146.432 | 1.288x | 1.284-1.294x | 1.296x | 1.18-1.82x | yes | NO | 0.00391 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro | 115.712 | 83.023 | 1.394x | 1.387-1.400x | 1.389x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ctl_r64 | 115.712 | 115.633 | 1.001x | 0.998-1.003x | 1.003x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ctl_s2 | 115.712 | 115.948 | 0.998x | 0.995-1.002x | 0.997x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ctl_s5 | 115.712 | 85.780 | 1.349x | 1.338-1.353x | 1.356x | 0.97-1.22x | NO | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | kernl | 115.712 | 118.154 | 0.979x | 0.976-0.983x | 0.977x | 0.89-1.01x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_clamp | 115.712 | 86.095 | 1.344x | 1.338-1.348x | 1.332x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 64, 80 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32 | 115.712 | 81.684 | 1.417x | 1.407-1.421x | 1.416x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 64, 63 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 98.225 | 81.684 | 1.203x | 1.193-1.213x | 1.194x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 68, 63 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 115.633 | 83.023 | 1.393x | 1.387-1.398x | 1.385x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 98.225 | 83.023 | 1.183x | 1.176-1.194x | 1.172x | 0.97-1.15x | NO | yes | 0 | 12, 12 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 158.090 | 83.023 | 1.904x | 1.897-1.910x | 1.906x | 0.90-1.03x | NO | yes | 0 | 12, 12 | 90, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | tt32 | 115.712 | 98.225 | 1.178x | 1.168-1.183x | 1.185x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_warm | tt38 | 115.712 | 158.090 | 0.732x | 0.730-0.734x | 0.729x | 0.97-1.23x | NO | yes | 0 | 12, 12 | 64, 90 | warm |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro | 133.325 | 99.328 | 1.342x | 1.333-1.352x | 1.366x | 1.25-1.62x | yes | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ctl_r64 | 133.325 | 133.120 | 1.002x | 0.991-1.011x | 1.002x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ctl_s2 | 133.325 | 133.325 | 1.000x | 0.992-1.009x | 1.002x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ctl_s5 | 133.325 | 101.171 | 1.318x | 1.304-1.333x | - | 1.27-1.50x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | kernl | 133.325 | 134.554 | 0.991x | 0.982-0.998x | 0.992x | 0.91-1.00x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_clamp | 133.325 | 101.786 | 1.310x | 1.296-1.319x | 1.317x | 1.22-1.59x | yes | yes | 0 | 12, 12 | 64, 80 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32 | 133.325 | 98.509 | 1.353x | 1.342-1.363x | - | 1.24-1.61x | yes | yes | 0 | 12, 12 | 64, 63 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 114.483 | 98.509 | 1.162x | 1.147-1.173x | - | 1.23-1.60x | NO | yes | 0 | 12, 12 | 68, 63 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 133.120 | 99.328 | 1.340x | 1.329-1.354x | 1.364x | 1.25-1.62x | yes | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 114.483 | 99.328 | 1.153x | 1.140-1.164x | 1.171x | 1.24-1.61x | NO | yes | 0 | 12, 12 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 167.936 | 99.328 | 1.691x | 1.685-1.700x | 1.732x | 0.91-1.03x | NO | yes | 0 | 12, 12 | 90, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | tt32 | 133.325 | 114.483 | 1.165x | 1.153-1.179x | 1.167x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n4096_k4096_16x16x64_w4_s2_cold | tt38 | 133.325 | 167.936 | 0.794x | 0.789-0.797x | 0.789x | 1.33-1.63x | NO | yes | 0 | 12, 12 | 64, 90 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro | 244.864 | 212.864 | 1.150x | 1.137-1.158x | 1.159x | 0.97-1.28x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ctl_s2 | 244.864 | 262.016 | 0.935x | 0.921-0.953x | 0.963x | 0.82-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ctl_s5 | 244.864 | 244.352 | 1.002x | 0.995-1.007x | 1.000x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | kernl | 244.864 | 256.256 | 0.956x | 0.949-0.963x | 0.947x | 0.89-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro_clamp | 244.864 | 210.048 | 1.166x | 1.157-1.173x | 1.161x | 0.97-1.28x | yes | yes | 0 | 8, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro_tt32 | 244.864 | 234.880 | 1.043x | 1.031-1.052x | 1.037x | 0.97-1.10x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 224.640 | 234.880 | 0.956x | 0.939-0.969x | 0.938x | 0.88-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 224.640 | 212.864 | 1.055x | 1.035-1.067x | 1.048x | 0.97-1.09x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 236.544 | 212.864 | 1.111x | 1.100-1.118x | 1.123x | 0.97-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | tt32 | 244.864 | 224.640 | 1.090x | 1.077-1.106x | 1.105x | 0.97-1.22x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_warm | tt38 | 244.864 | 236.544 | 1.035x | 1.028-1.041x | 1.032x | 0.97-1.28x | yes | NO | 0.00391 | 8, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro | 262.963 | 231.629 | 1.135x | 1.121-1.152x | 1.141x | 0.97-1.49x | yes | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ctl_s2 | 262.963 | 281.805 | 0.933x | 0.913-0.956x | 0.928x | 0.68-0.85x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ctl_s5 | 262.963 | 262.963 | 1.000x | 0.994-1.009x | 1.003x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | kernl | 262.963 | 274.842 | 0.957x | 0.950-0.966x | 0.964x | 0.90-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro_clamp | 262.963 | 228.762 | 1.150x | 1.140-1.160x | 1.164x | 0.97-1.49x | yes | yes | 0 | 8, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro_tt32 | 262.963 | 254.362 | 1.034x | 1.024-1.051x | 1.033x | 0.97-1.28x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 234.906 | 254.362 | 0.924x | 0.909-0.941x | 0.910x | 0.97-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 234.906 | 231.629 | 1.014x | 0.995-1.030x | 1.005x | 0.97-1.29x | yes | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 253.747 | 231.629 | 1.095x | 1.081-1.111x | 1.096x | 0.97-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | tt32 | 262.963 | 234.906 | 1.119x | 1.108-1.136x | 1.135x | 0.97-1.19x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s5_cold | tt38 | 262.963 | 253.747 | 1.036x | 1.028-1.045x | 1.041x | 0.97-1.49x | yes | NO | 0.00391 | 8, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro | 225.664 | 220.416 | 1.024x | 1.018-1.029x | 1.010x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ctl_s2 | 225.664 | 273.408 | 0.825x | 0.823-0.830x | 0.818x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ctl_s5 | 225.664 | 225.920 | 0.999x | 0.994-1.005x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | kernl | 225.664 | 222.720 | 1.013x | 1.009-1.018x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro_clamp | 225.664 | 207.488 | 1.088x | 1.082-1.093x | 1.086x | 0.86-1.03x | NO | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro_tt32 | 225.664 | 216.832 | 1.041x | 1.035-1.047x | 1.035x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 213.760 | 216.832 | 0.986x | 0.981-0.992x | 0.992x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 213.760 | 220.416 | 0.970x | 0.965-0.975x | 0.968x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 191.104 | 220.416 | 0.867x | 0.860-0.874x | 0.858x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | tt32 | 225.664 | 213.760 | 1.056x | 1.050-1.061x | 1.044x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_warm | tt38 | 225.664 | 191.104 | 1.181x | 1.171-1.190x | 1.177x | 0.97-1.03x | NO | NO | 0.00391 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro | 248.218 | 241.869 | 1.026x | 1.014-1.032x | - | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ctl_s2 | 248.218 | 291.840 | 0.851x | 0.842-0.857x | 0.842x | 0.70-1.00x | yes | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ctl_s5 | 248.218 | 248.013 | 1.001x | 0.986-1.007x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | kernl | 248.218 | 245.350 | 1.012x | 1.001-1.019x | 1.011x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro_clamp | 248.218 | 227.942 | 1.089x | 1.081-1.095x | 1.091x | 0.86-1.03x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro_tt32 | 248.218 | 238.387 | 1.041x | 1.034-1.051x | 1.044x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 234.291 | 238.387 | 0.983x | 0.978-0.995x | 0.988x | 0.97-1.07x | yes | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 234.291 | 241.869 | 0.969x | 0.959-0.977x | - | 0.97-1.07x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 211.968 | 241.869 | 0.876x | 0.864-0.885x | - | 0.97-1.03x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | tt32 | 248.218 | 234.291 | 1.059x | 1.050-1.065x | 1.056x | 0.93-1.03x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_32x64x32_w2_s5_cold | tt38 | 248.218 | 211.968 | 1.171x | 1.158-1.182x | - | 0.97-1.03x | NO | NO | 0.00391 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro | 264.046 | 227.913 | 1.159x | 1.133-1.180x | 1.211x | 0.97-1.45x | yes | yes | 0 | 8, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ctl_s2 | 264.046 | 268.727 | 0.983x | 0.944-1.019x | 1.022x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ctl_s5 | 264.046 | 242.834 | 1.087x | 1.060-1.110x | 1.139x | 0.97-1.21x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | kernl | 264.046 | 256.439 | 1.030x | 0.999-1.049x | 1.069x | 0.88-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro_clamp | 264.046 | 231.570 | 1.140x | 1.115-1.160x | 1.196x | 0.97-1.47x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro_tt32 | 264.046 | 243.712 | 1.083x | 1.058-1.104x | 1.139x | 0.97-1.08x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 249.271 | 243.712 | 1.023x | 1.014-1.059x | 1.040x | 0.85-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 249.271 | 227.913 | 1.094x | 1.086-1.132x | 1.106x | 0.97-1.22x | yes | yes | 0 | 8, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 249.856 | 227.913 | 1.096x | 1.088-1.108x | 1.093x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | tt32 | 264.046 | 249.271 | 1.059x | 1.009-1.078x | 1.095x | 0.97-1.22x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_warm | tt38 | 264.046 | 249.856 | 1.057x | 1.031-1.076x | 1.109x | 0.97-1.51x | yes | NO | 0.00391 | 8, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro | 280.781 | 246.989 | 1.137x | 1.111-1.162x | 1.148x | 1.19-1.55x | NO | yes | 0 | 8, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ctl_s2 | 280.781 | 281.805 | 0.996x | 0.945-1.036x | 1.028x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ctl_s5 | 280.781 | 263.168 | 1.067x | 1.043-1.091x | 1.074x | 1.19-1.44x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | kernl | 280.781 | 276.890 | 1.014x | 0.982-1.044x | 0.991x | 0.90-0.98x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro_clamp | 280.781 | 252.314 | 1.113x | 1.085-1.136x | 1.122x | 1.19-1.58x | NO | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro_tt32 | 280.781 | 263.987 | 1.064x | 1.039-1.094x | 1.080x | 1.10-1.21x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 268.083 | 263.987 | 1.016x | 1.005-1.030x | 1.020x | 1.00-1.07x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 268.083 | 246.989 | 1.085x | 1.075-1.094x | 1.084x | 1.10-1.36x | NO | yes | 0 | 8, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 267.878 | 246.989 | 1.085x | 1.073-1.095x | 1.097x | 0.84-1.03x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | tt32 | 280.781 | 268.083 | 1.047x | 1.024-1.071x | 1.059x | 1.05-1.18x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x32x32_w2_s2_cold | tt38 | 280.781 | 267.878 | 1.048x | 1.024-1.073x | 1.047x | 1.19-1.77x | NO | NO | 0.00391 | 8, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro | 226.158 | 220.891 | 1.024x | 1.018-1.029x | 1.033x | 0.94-1.03x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ctl_s2 | 226.158 | 318.171 | 0.711x | 0.707-0.715x | 0.711x | 0.80-1.03x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ctl_s5 | 226.158 | 226.889 | 0.997x | 0.992-1.003x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | kernl | 226.158 | 227.913 | 0.992x | 0.985-0.997x | 0.990x | 0.95-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_clamp | 226.158 | 220.014 | 1.028x | 1.023-1.033x | 1.033x | 0.97-1.08x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 226.158 | 220.453 | 1.026x | 1.020-1.032x | 1.032x | 0.97-1.16x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 226.743 | 220.453 | 1.029x | 1.024-1.035x | 1.036x | 0.97-1.17x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_tt32 | 226.158 | 219.867 | 1.029x | 1.023-1.036x | 1.034x | 0.97-1.14x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 226.743 | 219.867 | 1.031x | 1.027-1.039x | 1.038x | 0.97-1.16x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 226.743 | 220.891 | 1.026x | 1.022-1.032x | 1.037x | 0.95-1.03x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 219.429 | 220.891 | 0.993x | 0.987-1.001x | 0.991x | 0.92-1.03x | yes | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | tt32 | 226.158 | 226.743 | 0.997x | 0.992-1.002x | 0.996x | 0.96-1.03x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_warm | tt38 | 226.158 | 219.429 | 1.031x | 1.022-1.037x | 1.042x | 0.97-1.06x | yes | NO | 0.00391 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro | 246.989 | 241.664 | 1.022x | 1.015-1.028x | 1.018x | 0.97-1.17x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ctl_s2 | 246.989 | 336.896 | 0.733x | 0.727-0.737x | 0.726x | 0.70-0.87x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ctl_s5 | 246.989 | 247.603 | 0.998x | 0.991-1.004x | 0.995x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | kernl | 246.989 | 247.603 | 0.998x | 0.992-1.002x | 0.994x | 0.95-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_clamp | 246.989 | 241.664 | 1.022x | 1.016-1.027x | 1.018x | 0.97-1.26x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 246.989 | 240.845 | 1.026x | 1.019-1.034x | 1.023x | 0.97-1.35x | yes | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 247.603 | 240.845 | 1.028x | 1.022-1.036x | 1.027x | 0.97-1.37x | yes | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_tt32 | 246.989 | 240.845 | 1.026x | 1.018-1.033x | 1.026x | 0.97-1.33x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 247.603 | 240.845 | 1.028x | 1.021-1.035x | 1.030x | 0.97-1.35x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 247.603 | 241.664 | 1.025x | 1.019-1.030x | 1.022x | 0.97-1.18x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 235.930 | 241.664 | 0.976x | 0.970-0.984x | 0.976x | 0.92-1.03x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | tt32 | 246.989 | 247.603 | 0.998x | 0.992-1.003x | 0.996x | 0.96-1.03x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_64x128x32_w4_s4_cold | tt38 | 246.989 | 235.930 | 1.047x | 1.038-1.054x | 1.042x | 0.97-1.24x | yes | NO | 0.00391 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro | 161.178 | 155.238 | 1.038x | 1.021-1.057x | 1.031x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ctl_r64 | 161.178 | 161.792 | 0.996x | 0.979-1.026x | 0.993x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ctl_s2 | 161.178 | 161.587 | 0.997x | 0.976-1.023x | 0.999x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ctl_s5 | 161.178 | 154.010 | 1.047x | 1.022-1.067x | 1.032x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | kernl | 161.178 | 159.334 | 1.012x | 0.994-1.028x | 1.009x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_clamp | 161.178 | 210.739 | 0.765x | 0.744-0.779x | 0.741x | 0.97-1.03x | NO | yes | 0 | 28, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_sweep | 161.178 | 155.238 | 1.038x | 1.021-1.057x | 1.031x | 0.95-1.05x | yes | yes | 0 | 28, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_tt32 | 161.178 | 152.166 | 1.059x | 1.040-1.077x | 1.045x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 63 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 158.720 | 152.166 | 1.043x | 1.025-1.060x | 1.047x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 68, 63 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 161.792 | 155.238 | 1.042x | 1.017-1.057x | 1.038x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 158.720 | 155.238 | 1.022x | 1.007-1.040x | 1.033x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 451.379 | 155.238 | 2.908x | 2.888-2.993x | 2.893x | 0.97-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | tt32 | 161.178 | 158.720 | 1.015x | 0.995-1.037x | 0.998x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_warm | tt38 | 161.178 | 451.379 | 0.357x | 0.346-0.361x | 0.356x | 0.97-1.03x | NO | yes | 0 | 28, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro | 176.947 | 174.694 | 1.013x | 0.995-1.024x | 1.016x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ctl_r64 | 176.947 | 176.947 | 1.000x | 0.986-1.012x | 0.995x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ctl_s2 | 176.947 | 176.947 | 1.000x | 0.987-1.014x | 0.995x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ctl_s5 | 176.947 | 170.189 | 1.040x | 1.023-1.055x | - | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | kernl | 176.947 | 176.333 | 1.003x | 0.993-1.016x | 0.992x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 64 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_clamp | 176.947 | 226.099 | 0.783x | 0.768-0.799x | 0.769x | 0.85-1.03x | NO | yes | 0 | 28, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_sweep | 176.947 | 174.694 | 1.013x | 0.995-1.024x | 1.016x | 0.95-1.05x | yes | yes | 0 | 28, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_tt32 | 176.947 | 172.237 | 1.027x | 1.011-1.039x | - | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 63 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 175.718 | 172.237 | 1.020x | 1.006-1.035x | - | 0.97-1.03x | yes | yes | 0 | 28, 28 | 68, 63 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 176.947 | 174.694 | 1.013x | 0.997-1.025x | 1.021x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 175.718 | 174.694 | 1.006x | 0.991-1.019x | 1.007x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 432.333 | 174.694 | 2.475x | 2.405-2.490x | 2.588x | 0.97-1.07x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | tt32 | 176.947 | 175.718 | 1.007x | 0.992-1.018x | 1.009x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_16x16x64_w4_s2_cold | tt38 | 176.947 | 432.333 | 0.409x | 0.406-0.419x | 0.393x | 0.93-1.03x | NO | yes | 0 | 28, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro | 348.501 | 286.720 | 1.215x | 1.209-1.245x | 1.216x | 1.09-1.32x | yes | yes | 0 | 12, 8 | 168, 233 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | kernl | 348.501 | 372.224 | 0.936x | 0.915-0.962x | 0.941x | 0.81-0.91x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_clamp | 348.501 | 285.525 | 1.221x | 1.204-1.251x | 1.206x | 1.09-1.32x | yes | yes | 0 | 12, 8 | 168, 235 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_full_tt32 | 348.501 | 273.408 | 1.275x | 1.266-1.299x | 1.266x | 1.09-1.44x | yes | yes | 0 | 12, 8 | 168, 207 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 328.363 | 273.408 | 1.201x | 1.166-1.241x | 1.176x | 1.26-1.76x | NO | yes | 0 | 12, 8 | 168, 207 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_tt32 | 348.501 | 277.845 | 1.254x | 1.232-1.306x | 1.261x | 0.78-1.22x | NO | yes | 0 | 12, 8 | 168, 176 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_tt32_vs_tt32 | 328.363 | 277.845 | 1.182x | 1.135-1.248x | 1.172x | 0.97-1.40x | yes | yes | 0 | 12, 8 | 168, 176 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_vs_tt32 | 328.363 | 286.720 | 1.145x | 1.114-1.190x | 1.130x | 1.26-1.52x | NO | yes | 0 | 12, 8 | 168, 233 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | ro_vs_tt38 | 324.949 | 286.720 | 1.133x | 1.095-1.152x | 1.126x | 0.78-1.03x | NO | yes | 0 | 8, 8 | 211, 233 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | tt32 | 348.501 | 328.363 | 1.061x | 1.024-1.109x | 1.077x | 0.79-0.90x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_warm | tt38 | 348.501 | 324.949 | 1.072x | 1.058-1.128x | 1.080x | 1.09-1.42x | NO | NO | 0.00391 | 12, 8 | 168, 211 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro | 363.315 | 299.213 | 1.214x | 1.201-1.238x | 1.219x | 1.29-1.38x | NO | yes | 0 | 12, 8 | 168, 233 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | kernl | 363.315 | 379.904 | 0.956x | 0.947-0.979x | 0.964x | 0.83-0.94x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_clamp | 363.315 | 304.128 | 1.195x | 1.182-1.218x | 1.200x | 1.34-1.47x | NO | yes | 0 | 12, 8 | 168, 235 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_full_tt32 | 363.315 | 290.611 | 1.250x | 1.238-1.269x | 1.251x | 1.41-1.74x | NO | yes | 0 | 12, 8 | 168, 207 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 329.728 | 290.611 | 1.135x | 1.125-1.169x | 1.133x | 1.58-2.06x | NO | yes | 0 | 12, 8 | 168, 207 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_tt32 | 363.315 | 283.238 | 1.283x | 1.265-1.309x | 1.293x | 0.95-1.45x | yes | yes | 0 | 12, 8 | 168, 176 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_tt32_vs_tt32 | 329.728 | 283.238 | 1.164x | 1.150-1.206x | 1.171x | 1.14-1.61x | yes | yes | 0 | 12, 8 | 168, 176 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_vs_tt32 | 329.728 | 299.213 | 1.102x | 1.091-1.140x | 1.104x | 1.45-1.64x | NO | yes | 0 | 12, 8 | 168, 233 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | ro_vs_tt38 | 319.283 | 299.213 | 1.067x | 1.056-1.083x | 1.062x | 0.75-0.93x | NO | yes | 0 | 8, 8 | 211, 233 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | tt32 | 363.315 | 329.728 | 1.102x | 1.067-1.120x | 1.104x | 0.81-0.93x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x32x32_w4_s4_cold | tt38 | 363.315 | 319.283 | 1.138x | 1.123-1.158x | 1.148x | 1.44-1.72x | NO | NO | 0.00391 | 12, 8 | 168, 211 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro | 261.504 | 247.168 | 1.058x | 1.055-1.062x | 1.097x | 0.71-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | kernl | 261.504 | 251.776 | 1.039x | 1.034-1.044x | 1.077x | 0.86-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_clamp | 261.504 | 238.336 | 1.097x | 1.093-1.105x | 1.126x | 0.70-1.03x | NO | yes | 0 | 8, 8 | 255, 252 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_full_tt32 | 261.504 | 227.328 | 1.150x | 1.146-1.156x | 1.180x | 0.97-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 268.800 | 227.328 | 1.182x | 1.178-1.187x | 1.171x | 0.90-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_tt32 | 261.504 | 224.256 | 1.166x | 1.158-1.174x | 1.197x | 0.97-1.23x | yes | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_tt32_vs_tt32 | 268.800 | 224.256 | 1.199x | 1.190-1.207x | 1.189x | 0.97-1.14x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_vs_tt32 | 268.800 | 247.168 | 1.088x | 1.084-1.091x | 1.089x | 0.66-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | ro_vs_tt38 | 248.192 | 247.168 | 1.004x | 1.001-1.007x | 1.014x | 0.58-1.03x | yes | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | tt32 | 261.504 | 268.800 | 0.973x | 0.970-0.977x | 1.007x | 0.97-1.11x | yes | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_warm | tt38 | 261.504 | 248.192 | 1.054x | 1.051-1.058x | 1.082x | 0.97-1.24x | yes | NO | 0.00391 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro | 267.674 | 257.024 | 1.041x | 1.034-1.052x | 1.083x | 0.82-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | kernl | 267.674 | 255.590 | 1.047x | 1.036-1.058x | 1.088x | 0.88-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_clamp | 267.674 | 256.205 | 1.045x | 1.036-1.057x | 1.081x | 0.81-1.02x | NO | yes | 0 | 8, 8 | 255, 252 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_full_tt32 | 267.674 | 245.350 | 1.091x | 1.080-1.100x | 1.132x | 0.97-1.18x | yes | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 279.142 | 245.350 | 1.138x | 1.125-1.145x | 1.140x | 0.97-1.11x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_tt32 | 267.674 | 242.074 | 1.106x | 1.101-1.118x | 1.147x | 0.97-1.40x | yes | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_tt32_vs_tt32 | 279.142 | 242.074 | 1.153x | 1.147-1.164x | 1.155x | 0.97-1.32x | yes | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_vs_tt32 | 279.142 | 257.024 | 1.086x | 1.078-1.095x | 1.090x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | ro_vs_tt38 | 260.506 | 257.024 | 1.014x | 1.004-1.022x | 1.017x | 0.58-1.03x | yes | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | tt32 | 267.674 | 279.142 | 0.959x | 0.952-0.968x | 0.993x | 0.97-1.09x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_128x64x32_w4_s4_cold | tt38 | 267.674 | 260.506 | 1.028x | 1.020-1.039x | 1.065x | 0.97-1.42x | yes | NO | 0.00391 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro | 27.425 | 19.698 | 1.392x | 1.391-1.395x | 1.383x | 1.40-1.69x | NO | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ctl_s2 | 27.425 | 32.321 | 0.849x | 0.848-0.851x | 0.848x | 0.73-0.88x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ctl_s5 | 27.425 | 27.425 | 1.000x | 0.998-1.003x | 0.995x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | kernl | 27.425 | 28.635 | 0.958x | 0.957-0.960x | 0.960x | 0.89-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro_clamp | 27.425 | 18.693 | 1.467x | 1.463-1.472x | 1.465x | 1.44-1.93x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32 | 27.425 | 22.863 | 1.200x | 1.198-1.203x | 1.206x | 1.04-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 24.353 | 22.863 | 1.065x | 1.063-1.068x | 1.058x | 0.88-1.13x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 24.353 | 19.698 | 1.236x | 1.234-1.239x | 1.214x | 1.18-1.51x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 18.655 | 19.698 | 0.947x | 0.946-0.951x | 0.934x | 0.71-0.84x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | tt32 | 27.425 | 24.353 | 1.126x | 1.124-1.129x | 1.139x | 1.09-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_warm | tt38 | 27.425 | 18.655 | 1.470x | 1.464-1.473x | 1.481x | 1.74-2.27x | NO | yes | 0 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro | 45.875 | 33.382 | 1.374x | 1.354-1.395x | 1.435x | 1.44-1.68x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ctl_s2 | 45.875 | 60.211 | 0.762x | 0.750-0.771x | 0.942x | 0.68-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ctl_s5 | 45.875 | 45.875 | 1.000x | 0.982-1.023x | 1.005x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | kernl | 45.875 | 46.899 | 0.978x | 0.965-0.996x | 0.983x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro_clamp | 45.875 | 31.130 | 1.474x | 1.451-1.507x | 1.553x | 1.59-1.73x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32 | 45.875 | 38.093 | 1.204x | 1.187-1.222x | 1.228x | 1.15-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 42.189 | 38.093 | 1.108x | 1.096-1.124x | 1.127x | 1.04-1.11x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 42.189 | 33.382 | 1.264x | 1.250-1.284x | 1.318x | 1.31-1.46x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 23.757 | 33.382 | 0.712x | 0.707-0.728x | 0.675x | 0.50-0.84x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | tt32 | 45.875 | 42.189 | 1.087x | 1.067-1.102x | 1.089x | 1.07-1.18x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s5_cold | tt38 | 45.875 | 23.757 | 1.931x | 1.881-1.948x | 2.125x | 2.01-2.82x | NO | yes | 0 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro | 20.343 | 18.477 | 1.101x | 1.097-1.106x | - | 0.78-1.09x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ctl_s2 | 20.343 | 26.123 | 0.779x | 0.777-0.783x | 0.784x | 0.67-0.80x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ctl_s5 | 20.343 | 20.343 | 1.000x | 0.996-1.003x | 1.002x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | kernl | 20.343 | 21.185 | 0.960x | 0.956-0.963x | 0.970x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro_clamp | 20.343 | 22.801 | 0.892x | 0.889-0.896x | 0.893x | 0.66-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32 | 20.343 | 16.452 | 1.237x | 1.232-1.242x | 1.240x | 1.04-1.42x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 20.821 | 16.452 | 1.266x | 1.261-1.270x | 1.254x | 1.15-1.50x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 20.821 | 18.477 | 1.127x | 1.123-1.131x | - | 0.86-1.15x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 18.296 | 18.477 | 0.990x | 0.988-0.994x | - | 0.66-0.82x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | tt32 | 20.343 | 20.821 | 0.977x | 0.974-0.981x | 0.988x | 0.88-0.98x | NO | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_warm | tt38 | 20.343 | 18.296 | 1.112x | 1.108-1.116x | 1.133x | 1.00-1.57x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro | 38.707 | 36.454 | 1.062x | 1.050-1.073x | - | 0.98-1.07x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ctl_s2 | 38.707 | 53.043 | 0.730x | 0.720-0.739x | 0.705x | 0.62-0.74x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ctl_s5 | 38.707 | 38.707 | 1.000x | 0.989-1.016x | 0.998x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | kernl | 38.707 | 39.117 | 0.990x | 0.979-1.000x | 0.992x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro_clamp | 38.707 | 30.515 | 1.268x | 1.253-1.284x | 1.315x | 0.83-1.34x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32 | 38.707 | 32.563 | 1.189x | 1.175-1.210x | 1.224x | 1.24-1.37x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 39.322 | 32.563 | 1.208x | 1.194-1.223x | 1.250x | 1.29-1.47x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 39.322 | 36.454 | 1.079x | 1.067-1.085x | - | 1.06-1.12x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 23.347 | 36.454 | 0.640x | 0.626-0.650x | - | 0.48-0.82x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | tt32 | 38.707 | 39.322 | 0.984x | 0.979-0.995x | 0.979x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_32x64x32_w2_s5_cold | tt38 | 38.707 | 23.347 | 1.658x | 1.635-1.696x | - | 1.25-2.08x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro | 32.177 | 22.902 | 1.405x | 1.402-1.407x | 1.404x | 1.37-1.51x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ctl_s2 | 32.177 | 32.177 | 1.000x | 0.998-1.001x | 1.000x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ctl_s5 | 32.177 | 27.431 | 1.173x | 1.171-1.175x | 1.182x | 1.15-1.34x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | kernl | 32.177 | 34.580 | 0.931x | 0.928-0.932x | 0.928x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro_clamp | 32.177 | 23.139 | 1.391x | 1.388-1.393x | 1.393x | 1.39-1.64x | NO | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32 | 32.177 | 27.687 | 1.162x | 1.160-1.165x | 1.168x | 1.02-1.20x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 28.633 | 27.687 | 1.034x | 1.033-1.038x | 1.033x | 0.86-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 28.633 | 22.902 | 1.250x | 1.248-1.254x | 1.243x | 1.15-1.37x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 23.198 | 22.902 | 1.013x | 1.011-1.014x | 1.001x | 0.81-0.89x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | tt32 | 32.177 | 28.633 | 1.124x | 1.120-1.125x | 1.130x | 1.08-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_warm | tt38 | 32.177 | 23.198 | 1.387x | 1.385-1.389x | 1.402x | 1.59-1.79x | NO | yes | 0 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro | 60.211 | 43.213 | 1.393x | 1.384-1.411x | 1.117x | 1.29-1.53x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ctl_s2 | 60.211 | 60.211 | 1.000x | 0.990-1.010x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ctl_s5 | 60.211 | 45.670 | 1.318x | 1.292-1.329x | 1.050x | 1.23-1.44x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | kernl | 60.211 | 62.464 | 0.964x | 0.954-0.970x | 0.955x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro_clamp | 60.211 | 43.418 | 1.387x | 1.371-1.405x | 1.112x | 1.50-1.75x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32 | 60.211 | 49.357 | 1.220x | 1.202-1.229x | 0.970x | 1.09-1.20x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 51.610 | 49.357 | 1.046x | 1.033-1.058x | 1.057x | 0.99-1.07x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 51.610 | 43.213 | 1.194x | 1.190-1.215x | 1.218x | 1.19-1.35x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 42.803 | 43.213 | 0.991x | 0.981-1.010x | 0.992x | 0.68-0.91x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | tt32 | 60.211 | 51.610 | 1.167x | 1.150-1.175x | 0.917x | 1.05-1.17x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x32x32_w2_s2_cold | tt38 | 60.211 | 42.803 | 1.407x | 1.384-1.425x | 1.127x | 1.68-1.89x | NO | yes | 0 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro | 30.657 | 30.887 | 0.993x | 0.992-0.993x | 0.995x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ctl_s2 | 30.657 | 35.192 | 0.871x | 0.870-0.872x | 0.872x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ctl_s5 | 30.657 | 30.741 | 0.997x | 0.997-0.999x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | kernl | 30.657 | 32.998 | 0.929x | 0.928-0.930x | 0.934x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_clamp | 30.657 | 28.338 | 1.082x | 1.081-1.083x | 1.081x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 30.657 | 28.567 | 1.073x | 1.072-1.075x | 1.074x | 1.09-1.49x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 31.096 | 28.567 | 1.089x | 1.087-1.090x | 1.082x | 1.10-1.51x | NO | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32 | 30.657 | 27.648 | 1.109x | 1.104-1.110x | 1.110x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 31.096 | 27.648 | 1.125x | 1.119-1.126x | 1.118x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 31.096 | 30.887 | 1.007x | 1.005-1.007x | 1.002x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.407 | 30.887 | 1.211x | 1.206-1.225x | 1.218x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | tt32 | 30.657 | 31.096 | 0.986x | 0.985-0.987x | 0.993x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_warm | tt38 | 30.657 | 37.407 | 0.820x | 0.810-0.823x | 0.817x | 1.00-1.41x | NO | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro | 50.790 | 41.779 | 1.216x | 1.205-1.233x | 1.240x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ctl_s2 | 50.790 | 66.560 | 0.763x | 0.758-0.769x | 0.962x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ctl_s5 | 50.790 | 50.381 | 1.008x | 1.000-1.020x | 1.005x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | kernl | 50.790 | 52.019 | 0.976x | 0.965-0.984x | 0.966x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_clamp | 50.790 | 41.370 | 1.228x | 1.217-1.239x | 1.250x | 1.19-1.29x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 50.790 | 40.960 | 1.240x | 1.223-1.258x | 1.268x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 50.790 | 40.960 | 1.240x | 1.223-1.263x | 1.276x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32 | 50.790 | 38.502 | 1.319x | 1.300-1.332x | 1.360x | 1.26-1.45x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 50.790 | 38.502 | 1.319x | 1.300-1.337x | 1.368x | 1.27-1.46x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 50.790 | 41.779 | 1.216x | 1.205-1.238x | 1.248x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 43.008 | 41.779 | 1.029x | 1.015-1.045x | 1.024x | 0.70-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | tt32 | 50.790 | 50.790 | 1.000x | 0.988-1.008x | 0.994x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_64x128x32_w4_s4_cold | tt38 | 50.790 | 43.008 | 1.181x | 1.171-1.197x | 1.211x | 1.17-1.76x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro | 18.251 | 16.505 | 1.106x | 1.103-1.107x | 1.107x | 1.08-1.39x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ctl_r64 | 18.251 | 18.291 | 0.998x | 0.996-0.998x | 1.004x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ctl_s2 | 18.251 | 18.311 | 0.997x | 0.995-0.997x | 1.000x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ctl_s5 | 18.251 | 17.769 | 1.027x | 1.026-1.029x | 1.045x | 1.14-1.34x | NO | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | kernl | 18.251 | 18.814 | 0.970x | 0.968-0.970x | 0.977x | 0.90-0.99x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_clamp | 18.251 | 17.087 | 1.068x | 1.064-1.069x | 1.066x | 1.05-1.37x | yes | yes | 0 | 12, 12 | 64, 80 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32 | 18.251 | 16.384 | 1.114x | 1.111-1.115x | 1.121x | 1.06-1.38x | yes | yes | 0 | 12, 12 | 64, 63 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 19.014 | 16.384 | 1.161x | 1.159-1.163x | 1.173x | 1.05-1.37x | yes | yes | 0 | 12, 12 | 68, 63 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 18.291 | 16.505 | 1.108x | 1.107-1.111x | 1.103x | 1.08-1.39x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 19.014 | 16.505 | 1.152x | 1.151-1.155x | 1.159x | 1.07-1.39x | yes | yes | 0 | 12, 12 | 68, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 35.278 | 16.505 | 2.137x | 2.134-2.140x | 2.189x | 0.91-0.99x | NO | yes | 0 | 12, 12 | 90, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | tt32 | 18.251 | 19.014 | 0.960x | 0.958-0.960x | 0.955x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_warm | tt38 | 18.251 | 35.278 | 0.517x | 0.517-0.518x | 0.506x | 1.15-1.45x | NO | NO | 0.000488 | 12, 12 | 64, 90 | warm |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro | 31.744 | 28.467 | 1.115x | 1.100-1.130x | 1.160x | 1.23-1.55x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ctl_r64 | 31.744 | 31.949 | 0.994x | 0.987-1.006x | 0.997x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ctl_s2 | 31.744 | 31.949 | 0.994x | 0.981-1.006x | 1.002x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ctl_s5 | 31.744 | 27.443 | 1.157x | 1.141-1.191x | - | 1.25-1.46x | NO | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | kernl | 31.744 | 32.973 | 0.963x | 0.951-0.975x | 0.970x | 0.92-1.00x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_clamp | 31.744 | 28.672 | 1.107x | 1.092-1.130x | 1.085x | 1.20-1.53x | NO | yes | 0 | 12, 12 | 64, 80 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32 | 31.744 | 28.058 | 1.131x | 1.116-1.156x | - | 1.21-1.54x | NO | yes | 0 | 12, 12 | 64, 63 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 30.310 | 28.058 | 1.080x | 1.065-1.104x | - | 1.21-1.54x | NO | yes | 0 | 12, 12 | 68, 63 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 31.949 | 28.467 | 1.122x | 1.107-1.130x | 1.163x | 1.23-1.55x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 30.310 | 28.467 | 1.065x | 1.050-1.080x | 1.099x | 1.22-1.55x | NO | yes | 0 | 12, 12 | 68, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 45.670 | 28.467 | 1.604x | 1.586-1.623x | 1.765x | 0.91-0.99x | NO | yes | 0 | 12, 12 | 90, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | tt32 | 31.744 | 30.310 | 1.047x | 1.034-1.061x | 1.056x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k1024_16x16x64_w4_s2_cold | tt38 | 31.744 | 45.670 | 0.695x | 0.688-0.703x | 0.657x | 1.30-1.61x | NO | NO | 0.000488 | 12, 12 | 64, 90 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro | 100.533 | 70.114 | 1.434x | 1.432-1.436x | 1.432x | 1.42-1.76x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ctl_s2 | 100.533 | 120.049 | 0.837x | 0.832-0.838x | 0.837x | 0.72-0.88x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ctl_s5 | 100.533 | 100.533 | 1.000x | 0.999-1.001x | 1.000x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | kernl | 100.533 | 105.593 | 0.952x | 0.950-0.953x | 0.953x | 0.89-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro_clamp | 100.533 | 66.138 | 1.520x | 1.518-1.522x | 1.521x | 1.47-2.04x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32 | 100.533 | 82.583 | 1.217x | 1.214-1.219x | 1.220x | 1.04-1.29x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 88.425 | 82.583 | 1.071x | 1.067-1.076x | 1.076x | 0.88-1.14x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 88.425 | 70.114 | 1.261x | 1.258-1.267x | 1.264x | 1.19-1.56x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 65.958 | 70.114 | 0.941x | 0.939-0.943x | 0.944x | 0.68-0.83x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | tt32 | 100.533 | 88.425 | 1.137x | 1.132-1.139x | 1.133x | 1.10-1.22x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_warm | tt38 | 100.533 | 65.958 | 1.524x | 1.521-1.527x | 1.516x | 1.79-2.46x | NO | NO | 0.0156 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro | 166.707 | 114.893 | 1.451x | 1.436-1.462x | 1.478x | 1.48-1.72x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ctl_s2 | 166.707 | 222.618 | 0.749x | 0.744-0.753x | 0.744x | 0.67-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ctl_s5 | 166.707 | 166.298 | 1.002x | 0.994-1.010x | 1.004x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | kernl | 166.707 | 169.984 | 0.981x | 0.971-0.987x | 0.979x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro_clamp | 166.707 | 105.677 | 1.578x | 1.561-1.584x | 1.608x | 1.64-1.77x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32 | 166.707 | 131.482 | 1.268x | 1.256-1.275x | 1.279x | 1.16-1.28x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 148.890 | 131.482 | 1.132x | 1.124-1.139x | 1.139x | 1.05-1.11x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 148.890 | 114.893 | 1.296x | 1.285-1.306x | 1.316x | 1.34-1.49x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 70.656 | 114.893 | 0.615x | 0.610-0.620x | 0.603x | 0.46-0.83x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | tt32 | 166.707 | 148.890 | 1.120x | 1.111-1.126x | 1.123x | 1.07-1.19x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s5_cold | tt38 | 166.707 | 70.656 | 2.359x | 2.341-2.372x | 2.451x | 2.09-3.09x | yes | NO | 0.0156 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro | 72.038 | 64.666 | 1.114x | 1.107-1.123x | 1.120x | 0.77-1.10x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ctl_s2 | 72.038 | 97.126 | 0.742x | 0.738-0.749x | 0.760x | 0.65-0.79x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ctl_s5 | 72.038 | 73.421 | 0.981x | 0.972-0.987x | 1.011x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | kernl | 72.038 | 76.339 | 0.944x | 0.937-0.957x | 0.886x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro_clamp | 72.038 | 81.562 | 0.883x | 0.879-0.888x | 0.889x | 0.65-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32 | 72.038 | 56.986 | 1.264x | 1.259-1.272x | 1.266x | 1.05-1.47x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 73.984 | 56.986 | 1.298x | 1.293-1.315x | 1.286x | 1.16-1.56x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 73.984 | 64.666 | 1.144x | 1.137-1.161x | 1.138x | 0.85-1.16x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 64.102 | 64.666 | 0.991x | 0.987-0.997x | 0.979x | 0.63-0.81x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | tt32 | 72.038 | 73.984 | 0.974x | 0.960-0.981x | 0.984x | 0.88-0.97x | NO | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_warm | tt38 | 72.038 | 64.102 | 1.124x | 1.119-1.130x | 1.144x | 1.00-1.65x | yes | NO | 0.0156 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro | 137.421 | 129.638 | 1.060x | 1.054-1.068x | - | 0.98-1.08x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ctl_s2 | 137.421 | 193.331 | 0.711x | 0.707-0.717x | 0.708x | 0.61-0.73x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ctl_s5 | 137.421 | 137.626 | 0.999x | 0.993-1.009x | 1.000x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | kernl | 137.421 | 139.878 | 0.982x | 0.977-0.991x | 0.984x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro_clamp | 137.421 | 101.990 | 1.347x | 1.335-1.361x | 1.364x | 0.83-1.37x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32 | 137.421 | 115.302 | 1.192x | 1.186-1.203x | 1.200x | 1.26-1.40x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 142.336 | 115.302 | 1.234x | 1.229-1.241x | 1.241x | 1.32-1.50x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 142.336 | 129.638 | 1.098x | 1.091-1.101x | - | 1.06-1.13x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 68.403 | 129.638 | 0.528x | 0.524-0.530x | - | 0.45-0.81x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | tt32 | 137.421 | 142.336 | 0.965x | 0.961-0.974x | 0.967x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_32x64x32_w2_s5_cold | tt38 | 137.421 | 68.403 | 2.009x | 1.997-2.027x | - | 1.27-2.23x | yes | NO | 0.0156 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro | 120.695 | 82.944 | 1.455x | 1.431-1.459x | 1.456x | 1.39-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ctl_s2 | 120.695 | 120.695 | 1.000x | 0.997-1.003x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ctl_s5 | 120.695 | 101.035 | 1.195x | 1.191-1.199x | 1.193x | 1.15-1.36x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | kernl | 120.695 | 130.526 | 0.925x | 0.923-0.928x | 0.922x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro_clamp | 120.695 | 84.514 | 1.428x | 1.408-1.436x | 1.432x | 1.41-1.68x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32 | 120.695 | 101.922 | 1.184x | 1.177-1.188x | 1.183x | 1.02-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 105.950 | 101.922 | 1.040x | 1.034-1.044x | 1.040x | 0.85-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 105.950 | 82.944 | 1.277x | 1.257-1.282x | 1.280x | 1.16-1.39x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 85.265 | 82.944 | 1.028x | 1.007-1.043x | 1.022x | 0.80-0.88x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | tt32 | 120.695 | 105.950 | 1.139x | 1.135-1.142x | 1.138x | 1.09-1.22x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_warm | tt38 | 120.695 | 85.265 | 1.416x | 1.395-1.425x | 1.425x | 1.63-1.86x | NO | NO | 0.0156 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro | 222.208 | 149.709 | 1.484x | 1.475-1.491x | 1.502x | 1.31-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ctl_s2 | 222.208 | 222.208 | 1.000x | 0.995-1.003x | 0.999x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ctl_s5 | 222.208 | 166.502 | 1.335x | 1.325-1.340x | 1.350x | 1.24-1.46x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | kernl | 222.208 | 231.834 | 0.958x | 0.956-0.962x | 0.957x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro_clamp | 222.208 | 150.323 | 1.478x | 1.473-1.483x | 1.492x | 1.52-1.80x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32 | 222.208 | 179.200 | 1.240x | 1.233-1.245x | 1.244x | 1.10-1.21x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 188.416 | 179.200 | 1.051x | 1.043-1.056x | 1.052x | 1.00-1.07x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 188.416 | 149.709 | 1.259x | 1.248-1.265x | 1.270x | 1.20-1.36x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 150.118 | 149.709 | 1.003x | 0.996-1.008x | 1.006x | 0.67-0.90x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | tt32 | 222.208 | 188.416 | 1.179x | 1.176-1.185x | 1.183x | 1.05-1.18x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x32x32_w2_s2_cold | tt38 | 222.208 | 150.118 | 1.480x | 1.475-1.485x | 1.492x | 1.71-1.94x | NO | NO | 0.0156 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro | 108.885 | 109.568 | 0.994x | 0.992-0.995x | 0.993x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ctl_s2 | 108.885 | 127.659 | 0.853x | 0.851-0.855x | 0.855x | 0.71-0.86x | yes | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ctl_s5 | 108.885 | 109.022 | 0.999x | 0.996-1.000x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | kernl | 108.885 | 118.306 | 0.920x | 0.919-0.921x | 0.920x | 0.95-1.01x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_clamp | 108.885 | 99.055 | 1.099x | 1.097-1.101x | 1.094x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 108.885 | 102.332 | 1.064x | 1.062-1.066x | 1.066x | 1.10-1.54x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 113.186 | 102.332 | 1.106x | 1.103-1.109x | 1.106x | 1.11-1.55x | NO | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32 | 108.885 | 99.465 | 1.095x | 1.089-1.099x | 1.096x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 113.186 | 99.465 | 1.138x | 1.131-1.143x | 1.137x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 113.186 | 109.568 | 1.033x | 1.030-1.035x | 1.031x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 137.626 | 109.568 | 1.256x | 1.252-1.259x | 1.254x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | tt32 | 108.885 | 113.186 | 0.962x | 0.960-0.965x | 0.964x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_warm | tt38 | 108.885 | 137.626 | 0.791x | 0.789-0.794x | 0.792x | 1.00-1.44x | NO | NO | 0.0156 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro | 177.562 | 141.107 | 1.258x | 1.250-1.265x | 1.264x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ctl_s2 | 177.562 | 244.736 | 0.726x | 0.722-0.729x | 0.721x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ctl_s5 | 177.562 | 177.152 | 1.002x | 0.997-1.007x | 1.006x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | kernl | 177.562 | 184.525 | 0.962x | 0.956-0.967x | 0.965x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_clamp | 177.562 | 140.698 | 1.262x | 1.254-1.267x | 1.274x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 177.562 | 141.107 | 1.258x | 1.249-1.263x | 1.273x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 182.682 | 141.107 | 1.295x | 1.282-1.299x | 1.302x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32 | 177.562 | 130.867 | 1.357x | 1.348-1.362x | 1.378x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 182.682 | 130.867 | 1.396x | 1.384-1.401x | 1.409x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 182.682 | 141.107 | 1.295x | 1.284-1.301x | 1.293x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 144.998 | 141.107 | 1.028x | 1.023-1.032x | 1.021x | 0.68-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | tt32 | 177.562 | 182.682 | 0.972x | 0.966-0.980x | 0.978x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_64x128x32_w4_s4_cold | tt38 | 177.562 | 144.998 | 1.225x | 1.219-1.229x | 1.238x | 1.18-1.82x | yes | NO | 0.0156 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro | 64.307 | 56.456 | 1.139x | 1.133-1.147x | 1.052x | 1.09-1.45x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ctl_r64 | 64.307 | 63.556 | 1.012x | 1.008-1.017x | 0.998x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ctl_s2 | 64.307 | 63.693 | 1.010x | 1.003-1.016x | 1.003x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ctl_s5 | 64.307 | 59.255 | 1.085x | 1.079-1.094x | 1.083x | 1.16-1.39x | NO | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | kernl | 64.307 | 66.424 | 0.968x | 0.962-0.977x | 0.966x | 0.89-0.99x | yes | yes | 0 | 12, 12 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_clamp | 64.307 | 58.231 | 1.104x | 1.098-1.112x | 1.091x | 1.05-1.42x | yes | yes | 0 | 12, 12 | 64, 80 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32 | 64.307 | 55.979 | 1.149x | 1.140-1.158x | 1.145x | 1.07-1.44x | yes | yes | 0 | 12, 12 | 64, 63 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 66.833 | 55.979 | 1.194x | 1.186-1.200x | 1.224x | 1.06-1.43x | yes | yes | 0 | 12, 12 | 68, 63 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 63.556 | 56.456 | 1.126x | 1.122-1.130x | 1.053x | 1.09-1.45x | yes | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 66.833 | 56.456 | 1.184x | 1.179-1.188x | 1.124x | 1.08-1.44x | yes | yes | 0 | 12, 12 | 68, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 131.686 | 56.456 | 2.333x | 2.324-2.342x | 2.185x | 0.90-0.98x | NO | yes | 0 | 12, 12 | 90, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | tt32 | 64.307 | 66.833 | 0.962x | 0.958-0.968x | 0.936x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_warm | tt38 | 64.307 | 131.686 | 0.488x | 0.486-0.491x | 0.481x | 1.17-1.53x | NO | yes | 0 | 12, 12 | 64, 90 | warm |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro | 107.110 | 93.184 | 1.149x | 1.143-1.161x | 1.157x | 1.25-1.62x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ctl_r64 | 107.110 | 107.110 | 1.000x | 0.992-1.010x | 0.996x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ctl_s2 | 107.110 | 106.906 | 1.002x | 0.994-1.012x | 0.999x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ctl_s5 | 107.110 | 90.317 | 1.186x | 1.173-1.198x | - | 1.27-1.50x | NO | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | kernl | 107.110 | 114.278 | 0.937x | 0.934-0.946x | 0.930x | 0.91-1.00x | yes | yes | 0 | 12, 12 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_clamp | 107.110 | 93.798 | 1.142x | 1.133-1.154x | 1.101x | 1.22-1.59x | NO | yes | 0 | 12, 12 | 64, 80 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32 | 107.110 | 92.160 | 1.162x | 1.150-1.177x | - | 1.24-1.61x | NO | yes | 0 | 12, 12 | 64, 63 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 102.810 | 92.160 | 1.116x | 1.104-1.132x | - | 1.23-1.60x | NO | yes | 0 | 12, 12 | 68, 63 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 107.110 | 93.184 | 1.149x | 1.143-1.159x | 1.161x | 1.25-1.62x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 102.810 | 93.184 | 1.103x | 1.096-1.117x | 1.117x | 1.24-1.61x | NO | yes | 0 | 12, 12 | 68, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 161.997 | 93.184 | 1.738x | 1.730-1.751x | 1.792x | 0.91-0.99x | NO | yes | 0 | 12, 12 | 90, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | tt32 | 107.110 | 102.810 | 1.042x | 1.030-1.052x | 1.036x | 0.97-1.04x | NO | yes | 0 | 12, 12 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n1024_k4096_16x16x64_w4_s2_cold | tt38 | 107.110 | 161.997 | 0.661x | 0.657-0.667x | 0.646x | 1.33-1.69x | NO | yes | 0 | 12, 12 | 64, 90 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro | 28.869 | 27.333 | 1.056x | 1.052-1.061x | 1.067x | 1.40-1.69x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ctl_s2 | 28.869 | 33.260 | 0.868x | 0.863-0.875x | 0.853x | 0.73-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ctl_s5 | 28.869 | 28.948 | 0.997x | 0.990-1.005x | 0.998x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | kernl | 28.869 | 30.188 | 0.956x | 0.951-0.965x | 0.946x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro_clamp | 28.869 | 26.801 | 1.077x | 1.072-1.082x | 1.091x | 1.44-1.93x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32 | 28.869 | 28.711 | 1.005x | 0.999-1.010x | 1.016x | 1.04-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 32.138 | 28.711 | 1.119x | 1.115-1.124x | 1.123x | 0.88-1.13x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 32.138 | 27.333 | 1.176x | 1.174-1.180x | 1.179x | 1.18-1.51x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 31.567 | 27.333 | 1.155x | 1.153-1.158x | 1.158x | 0.71-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | tt32 | 28.869 | 32.138 | 0.898x | 0.892-0.903x | 0.905x | 1.09-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_warm | tt38 | 28.869 | 31.567 | 0.915x | 0.910-0.919x | 0.922x | 1.74-2.27x | NO | NO | 0.000977 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro | 56.115 | 48.128 | 1.166x | 1.143-1.194x | 1.164x | 1.44-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ctl_s2 | 56.115 | 72.909 | 0.770x | 0.757-0.782x | 0.938x | 0.68-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ctl_s5 | 56.115 | 56.320 | 0.996x | 0.975-1.018x | 1.181x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | kernl | 56.115 | 56.934 | 0.986x | 0.964-1.000x | 1.186x | 0.90-0.98x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro_clamp | 56.115 | 49.357 | 1.137x | 1.120-1.159x | 1.127x | 1.59-1.73x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32 | 56.115 | 50.176 | 1.118x | 1.097-1.135x | 1.120x | 1.15-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 57.754 | 50.176 | 1.151x | 1.138-1.164x | 0.926x | 1.04-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 57.754 | 48.128 | 1.200x | 1.186-1.224x | 0.963x | 1.31-1.46x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 39.526 | 48.128 | 0.821x | 0.806-0.845x | 0.796x | 0.60-0.84x | yes | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | tt32 | 56.115 | 57.754 | 0.972x | 0.954-0.986x | 1.209x | 1.07-1.18x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s5_cold | tt38 | 56.115 | 39.526 | 1.420x | 1.383-1.450x | 1.462x | 2.01-2.35x | NO | NO | 0.000977 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro | 28.884 | 25.971 | 1.112x | 1.110-1.115x | - | 0.78-1.09x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ctl_s2 | 28.884 | 28.813 | 1.002x | 0.999-1.006x | 1.012x | 0.67-0.80x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ctl_s5 | 28.884 | 28.884 | 1.000x | 0.996-1.003x | 0.992x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | kernl | 28.884 | 26.324 | 1.097x | 1.088-1.105x | 1.113x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro_clamp | 28.884 | 28.849 | 1.001x | 0.999-1.005x | 1.018x | 0.66-1.10x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32 | 28.884 | 24.382 | 1.185x | 1.181-1.188x | 1.205x | 1.04-1.42x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 26.854 | 24.382 | 1.101x | 1.097-1.104x | 1.102x | 1.15-1.50x | NO | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 26.854 | 25.971 | 1.034x | 1.031-1.037x | - | 0.86-1.15x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 28.831 | 25.971 | 1.110x | 1.108-1.114x | - | 0.66-0.82x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | tt32 | 28.884 | 26.854 | 1.076x | 1.072-1.080x | 1.093x | 0.88-0.98x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_warm | tt38 | 28.884 | 28.831 | 1.002x | 0.998-1.005x | - | 1.00-1.57x | yes | NO | 0.000977 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro | 54.477 | 49.971 | 1.090x | 1.073-1.116x | - | 0.98-1.07x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ctl_s2 | 54.477 | 67.789 | 0.804x | 0.790-0.821x | 1.004x | 0.62-0.74x | NO | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ctl_s5 | 54.477 | 54.272 | 1.004x | 0.981-1.027x | 0.983x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | kernl | 54.477 | 49.971 | 1.090x | 1.065-1.111x | 1.094x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro_clamp | 54.477 | 46.694 | 1.167x | 1.148-1.195x | 1.191x | 0.83-1.34x | yes | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32 | 54.477 | 47.309 | 1.152x | 1.134-1.174x | 1.173x | 1.24-1.37x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 49.766 | 47.309 | 1.052x | 1.039-1.061x | 1.058x | 1.29-1.47x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 49.766 | 49.971 | 0.996x | 0.984-1.008x | - | 1.06-1.12x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 40.141 | 49.971 | 0.803x | 0.792-0.818x | - | 0.55-0.82x | yes | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | tt32 | 54.477 | 49.766 | 1.095x | 1.078-1.120x | 1.108x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_32x64x32_w2_s5_cold | tt38 | 54.477 | 40.141 | 1.357x | 1.328-1.392x | - | 1.25-1.84x | yes | NO | 0.000977 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro | 33.040 | 28.797 | 1.147x | 1.144-1.155x | 1.175x | 1.37-1.51x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ctl_s2 | 33.040 | 33.040 | 1.000x | 0.996-1.004x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ctl_s5 | 33.040 | 28.818 | 1.146x | 1.142-1.153x | 1.158x | 1.15-1.34x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | kernl | 33.040 | 35.464 | 0.932x | 0.929-0.936x | 0.931x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro_clamp | 33.040 | 28.985 | 1.140x | 1.135-1.150x | 1.171x | 1.39-1.64x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32 | 33.040 | 30.845 | 1.071x | 1.067-1.079x | 1.059x | 1.02-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 31.556 | 30.845 | 1.023x | 1.017-1.030x | 1.000x | 0.86-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 31.556 | 28.797 | 1.096x | 1.091-1.103x | 1.110x | 1.15-1.37x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 32.016 | 28.797 | 1.112x | 1.107-1.122x | 1.116x | 0.81-0.89x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | tt32 | 33.040 | 31.556 | 1.047x | 1.043-1.054x | 1.058x | 1.08-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_warm | tt38 | 33.040 | 32.016 | 1.032x | 1.025-1.039x | 1.053x | 1.59-1.79x | NO | NO | 0.000977 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro | 73.114 | 52.838 | 1.384x | 1.375-1.397x | 1.112x | 1.29-1.53x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ctl_s2 | 73.114 | 73.114 | 1.000x | 0.994-1.011x | 0.990x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ctl_s5 | 73.114 | 56.525 | 1.293x | 1.276-1.315x | 1.296x | 1.23-1.44x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | kernl | 73.114 | 75.366 | 0.970x | 0.965-0.984x | 0.968x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro_clamp | 73.114 | 54.067 | 1.352x | 1.338-1.375x | 1.081x | 1.50-1.75x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32 | 73.114 | 58.368 | 1.253x | 1.236-1.273x | 1.280x | 1.09-1.20x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 61.235 | 58.368 | 1.049x | 1.028-1.078x | 1.036x | 0.99-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 61.235 | 52.838 | 1.159x | 1.143-1.183x | 0.900x | 1.19-1.35x | NO | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 54.886 | 52.838 | 1.039x | 1.027-1.051x | 1.027x | 0.68-0.91x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | tt32 | 73.114 | 61.235 | 1.194x | 1.171-1.213x | 1.236x | 1.05-1.17x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x32x32_w2_s2_cold | tt38 | 73.114 | 54.886 | 1.332x | 1.319-1.350x | 1.083x | 1.68-1.89x | NO | NO | 0.000977 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro | 31.972 | 31.152 | 1.026x | 1.021-1.028x | 1.017x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ctl_s2 | 31.972 | 36.432 | 0.878x | 0.875-0.880x | 0.873x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ctl_s5 | 31.972 | 31.972 | 1.000x | 0.996-1.002x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | kernl | 31.972 | 33.678 | 0.949x | 0.944-0.951x | 0.940x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_clamp | 31.972 | 28.376 | 1.127x | 1.122-1.128x | 1.120x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 31.972 | 28.627 | 1.117x | 1.112-1.120x | 1.123x | 1.09-1.49x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 32.449 | 28.627 | 1.134x | 1.129-1.139x | 1.138x | 1.10-1.51x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32 | 31.972 | 28.831 | 1.109x | 1.104-1.114x | 1.107x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 32.449 | 28.831 | 1.125x | 1.121-1.132x | 1.122x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 32.449 | 31.152 | 1.042x | 1.037-1.045x | 1.031x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 39.299 | 31.152 | 1.262x | 1.256-1.263x | 1.245x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | tt32 | 31.972 | 32.449 | 0.985x | 0.980-0.988x | 0.987x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_warm | tt38 | 31.972 | 39.299 | 0.814x | 0.811-0.816x | 0.817x | 1.00-1.41x | NO | NO | 0.000977 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro | 58.368 | 51.200 | 1.140x | 1.119-1.158x | 0.900x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ctl_s2 | 58.368 | 77.619 | 0.752x | 0.740-0.757x | 0.728x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ctl_s5 | 58.368 | 57.754 | 1.011x | 0.989-1.021x | 1.011x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | kernl | 58.368 | 61.235 | 0.953x | 0.931-0.969x | 0.947x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_clamp | 58.368 | 50.790 | 1.149x | 1.128-1.158x | 0.906x | 1.19-1.29x | NO | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 58.368 | 50.381 | 1.159x | 1.142-1.172x | 0.917x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 58.163 | 50.381 | 1.154x | 1.146-1.172x | 0.914x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32 | 58.368 | 47.309 | 1.234x | 1.210-1.243x | 0.977x | 1.26-1.45x | NO | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 58.163 | 47.309 | 1.229x | 1.215-1.243x | 0.974x | 1.27-1.46x | NO | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 58.163 | 51.200 | 1.136x | 1.123-1.158x | 0.897x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 44.646 | 51.200 | 0.872x | 0.861-0.891x | 0.867x | 0.70-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | tt32 | 58.368 | 58.163 | 1.004x | 0.986-1.011x | 1.004x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_64x128x32_w4_s4_cold | tt38 | 58.368 | 44.646 | 1.307x | 1.282-1.318x | 1.038x | 1.17-1.76x | yes | NO | 0.000977 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro | 51.257 | 44.430 | 1.154x | 1.136-1.178x | 1.196x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ctl_r64 | 51.257 | 51.257 | 1.000x | 0.985-1.015x | 1.007x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ctl_s2 | 51.257 | 51.371 | 0.998x | 0.980-1.017x | 1.002x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ctl_s5 | 51.257 | 50.916 | 1.007x | 0.992-1.020x | 1.031x | 0.98-1.23x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | kernl | 51.257 | 50.460 | 1.016x | 1.002-1.031x | 1.039x | 0.90-0.99x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_clamp | 51.257 | 45.909 | 1.116x | 1.100-1.127x | 1.120x | 0.98-1.40x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32 | 51.257 | 45.113 | 1.136x | 1.121-1.152x | 1.162x | 0.98-1.25x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 52.508 | 45.113 | 1.164x | 1.151-1.180x | 1.164x | 0.97-1.24x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 51.257 | 44.430 | 1.154x | 1.140-1.175x | 1.188x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 52.508 | 44.430 | 1.182x | 1.167-1.206x | 1.198x | 0.97-1.33x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 109.340 | 44.430 | 2.461x | 2.449-2.503x | 1.998x | 0.86-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | tt32 | 51.257 | 52.508 | 0.976x | 0.959-0.991x | 0.998x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_warm | tt38 | 51.257 | 109.340 | 0.469x | 0.462-0.472x | 0.599x | 0.98-1.50x | NO | NO | 0.000977 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro | 72.704 | 60.416 | 1.203x | 1.174-1.226x | 1.236x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ctl_r64 | 72.704 | 72.704 | 1.000x | 0.978-1.023x | 1.006x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ctl_s2 | 72.704 | 72.499 | 1.003x | 0.978-1.017x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ctl_s5 | 72.704 | 61.440 | 1.183x | 1.155-1.205x | - | 1.27-1.49x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | kernl | 72.704 | 69.837 | 1.041x | 1.012-1.069x | 1.062x | 0.91-1.00x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_clamp | 72.704 | 62.874 | 1.156x | 1.133-1.174x | 1.159x | 1.21-1.57x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32 | 72.704 | 57.549 | 1.263x | 1.228-1.283x | - | 1.23-1.57x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 70.451 | 57.549 | 1.224x | 1.204-1.244x | - | 1.22-1.57x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 72.704 | 60.416 | 1.203x | 1.174-1.226x | 1.229x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 70.451 | 60.416 | 1.166x | 1.151-1.188x | 1.181x | 1.23-1.59x | NO | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 117.965 | 60.416 | 1.953x | 1.930-1.993x | 1.610x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | tt32 | 72.704 | 70.451 | 1.032x | 1.009-1.044x | 1.047x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k1024_16x16x64_w4_s2_cold | tt38 | 72.704 | 117.965 | 0.616x | 0.601-0.623x | 0.768x | 1.32-1.66x | NO | NO | 0.000977 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro | 165.319 | 131.868 | 1.254x | 1.245-1.266x | 1.255x | 1.42-1.76x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ctl_s2 | 165.319 | 220.388 | 0.750x | 0.746-0.756x | 0.744x | 0.72-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ctl_s5 | 165.319 | 165.547 | 0.999x | 0.989-1.008x | 1.003x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | kernl | 165.319 | 170.325 | 0.971x | 0.963-0.979x | 0.967x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro_clamp | 165.319 | 129.024 | 1.281x | 1.274-1.293x | 1.262x | 1.47-2.04x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32 | 165.319 | 141.995 | 1.164x | 1.158-1.173x | 1.161x | 1.04-1.29x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 174.990 | 141.995 | 1.232x | 1.228-1.236x | 1.233x | 0.88-1.14x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 174.990 | 131.868 | 1.327x | 1.320-1.333x | 1.332x | 1.19-1.56x | yes | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 117.077 | 131.868 | 0.888x | 0.885-0.893x | 0.892x | 0.77-1.01x | yes | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | tt32 | 165.319 | 174.990 | 0.945x | 0.940-0.952x | 0.942x | 1.10-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_warm | tt38 | 165.319 | 117.077 | 1.412x | 1.404-1.421x | 1.407x | 1.73-2.05x | NO | NO | 0.0156 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro | 180.429 | 146.022 | 1.236x | 1.222-1.257x | 1.250x | 1.48-1.72x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ctl_s2 | 180.429 | 241.254 | 0.748x | 0.742-0.758x | 0.739x | 0.67-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ctl_s5 | 180.429 | 180.019 | 1.002x | 0.990-1.017x | 0.995x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | kernl | 180.429 | 185.139 | 0.975x | 0.966-0.987x | 0.972x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro_clamp | 180.429 | 147.456 | 1.224x | 1.212-1.243x | 1.228x | 1.64-1.77x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32 | 180.429 | 157.901 | 1.143x | 1.133-1.159x | 1.147x | 1.16-1.28x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 190.054 | 157.901 | 1.204x | 1.198-1.212x | 1.209x | 1.05-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 190.054 | 146.022 | 1.302x | 1.291-1.315x | 1.318x | 1.34-1.49x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 123.904 | 146.022 | 0.849x | 0.840-0.857x | 0.846x | 0.56-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | tt32 | 180.429 | 190.054 | 0.949x | 0.941-0.961x | 0.949x | 1.07-1.19x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s5_cold | tt38 | 180.429 | 123.904 | 1.456x | 1.443-1.478x | 1.478x | 2.09-2.57x | NO | NO | 0.0156 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro | 160.666 | 137.933 | 1.165x | 1.158-1.170x | 1.161x | 0.77-1.10x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ctl_s2 | 160.666 | 196.403 | 0.818x | 0.815-0.821x | 0.815x | 0.65-0.79x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ctl_s5 | 160.666 | 160.563 | 1.001x | 0.996-1.003x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | kernl | 160.666 | 134.861 | 1.191x | 1.184-1.194x | 1.195x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro_clamp | 160.666 | 107.008 | 1.501x | 1.492-1.506x | 1.499x | 0.65-1.10x | NO | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32 | 160.666 | 124.314 | 1.292x | 1.286-1.297x | 1.294x | 1.05-1.47x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 137.318 | 124.314 | 1.105x | 1.102-1.109x | 1.105x | 1.16-1.56x | NO | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 137.318 | 137.933 | 0.996x | 0.992-1.000x | 0.992x | 0.85-1.16x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 107.315 | 137.933 | 0.778x | 0.774-0.783x | - | 0.71-0.88x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | tt32 | 160.666 | 137.318 | 1.170x | 1.165-1.172x | 1.171x | 0.88-0.97x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_warm | tt38 | 160.666 | 107.315 | 1.497x | 1.487-1.502x | - | 1.00-1.47x | NO | NO | 0.0156 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro | 173.261 | 153.600 | 1.128x | 1.107-1.139x | - | 0.98-1.08x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ctl_s2 | 173.261 | 216.474 | 0.800x | 0.788-0.807x | 0.790x | 0.61-0.73x | NO | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ctl_s5 | 173.261 | 173.670 | 0.998x | 0.979-1.017x | 0.990x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | kernl | 173.261 | 151.552 | 1.143x | 1.124-1.152x | 1.142x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro_clamp | 173.261 | 127.795 | 1.356x | 1.334-1.369x | 1.363x | 0.83-1.37x | yes | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32 | 173.261 | 142.746 | 1.214x | 1.193-1.227x | 1.220x | 1.26-1.40x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 153.600 | 142.746 | 1.076x | 1.067-1.094x | 1.081x | 1.32-1.50x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 153.600 | 153.600 | 1.000x | 0.991-1.016x | - | 1.06-1.13x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 119.808 | 153.600 | 0.780x | 0.773-0.788x | - | 0.51-0.81x | yes | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | tt32 | 173.261 | 153.600 | 1.128x | 1.102-1.138x | 1.128x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_32x64x32_w2_s5_cold | tt38 | 173.261 | 119.808 | 1.446x | 1.420-1.458x | - | 1.27-1.99x | yes | NO | 0.0156 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro | 220.160 | 152.348 | 1.445x | 1.436-1.451x | 1.455x | 1.39-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ctl_s2 | 220.160 | 220.274 | 0.999x | 0.997-1.002x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ctl_s5 | 220.160 | 171.463 | 1.284x | 1.277-1.292x | 1.295x | 1.15-1.36x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | kernl | 220.160 | 229.831 | 0.958x | 0.956-0.961x | 0.955x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro_clamp | 220.160 | 159.175 | 1.383x | 1.375-1.392x | 1.400x | 1.41-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32 | 220.160 | 173.284 | 1.271x | 1.266-1.276x | 1.284x | 1.02-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 187.847 | 173.284 | 1.084x | 1.077-1.090x | 1.088x | 0.85-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 187.847 | 152.348 | 1.233x | 1.222-1.240x | 1.233x | 1.16-1.39x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 164.636 | 152.348 | 1.081x | 1.070-1.088x | 1.087x | 0.80-0.88x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | tt32 | 220.160 | 187.847 | 1.172x | 1.167-1.178x | 1.180x | 1.09-1.22x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_warm | tt38 | 220.160 | 164.636 | 1.337x | 1.330-1.346x | 1.339x | 1.63-1.86x | NO | NO | 0.0156 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro | 241.050 | 167.731 | 1.437x | 1.423-1.444x | 1.445x | 1.31-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ctl_s2 | 241.050 | 241.254 | 0.999x | 0.995-1.005x | 0.993x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ctl_s5 | 241.050 | 180.429 | 1.336x | 1.321-1.349x | 1.338x | 1.24-1.46x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | kernl | 241.050 | 249.651 | 0.966x | 0.960-0.970x | 0.960x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro_clamp | 241.050 | 173.261 | 1.391x | 1.381-1.400x | 1.403x | 1.52-1.80x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32 | 241.050 | 191.898 | 1.256x | 1.246-1.267x | 1.257x | 1.10-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 202.752 | 191.898 | 1.057x | 1.045-1.069x | 1.057x | 1.00-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 202.752 | 167.731 | 1.209x | 1.193-1.218x | 1.216x | 1.20-1.36x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 177.766 | 167.731 | 1.060x | 1.046-1.067x | 1.057x | 0.67-0.90x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | tt32 | 241.050 | 202.752 | 1.189x | 1.180-1.199x | 1.189x | 1.05-1.18x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x32x32_w2_s2_cold | tt38 | 241.050 | 177.766 | 1.356x | 1.346-1.367x | 1.367x | 1.71-1.94x | NO | NO | 0.0156 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro | 174.336 | 140.160 | 1.244x | 1.240-1.247x | 1.240x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ctl_s2 | 174.336 | 252.416 | 0.691x | 0.689-0.692x | 0.690x | 0.71-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ctl_s5 | 174.336 | 173.696 | 1.004x | 1.001-1.007x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | kernl | 174.336 | 181.504 | 0.961x | 0.958-0.965x | 0.958x | 0.95-1.01x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_clamp | 174.336 | 139.648 | 1.248x | 1.245-1.251x | 1.256x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 174.336 | 140.032 | 1.245x | 1.240-1.249x | 1.248x | 1.10-1.54x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 179.968 | 140.032 | 1.285x | 1.279-1.295x | 1.287x | 1.11-1.55x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32 | 174.336 | 129.664 | 1.345x | 1.340-1.349x | 1.342x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 179.968 | 129.664 | 1.388x | 1.382-1.399x | 1.384x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 179.968 | 140.160 | 1.284x | 1.279-1.293x | 1.279x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 145.024 | 140.160 | 1.035x | 1.011-1.048x | 1.029x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | tt32 | 174.336 | 179.968 | 0.969x | 0.963-0.972x | 0.970x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_warm | tt38 | 174.336 | 145.024 | 1.202x | 1.187-1.229x | 1.205x | 1.00-1.44x | yes | NO | 0.0156 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro | 189.030 | 156.672 | 1.207x | 1.196-1.214x | 1.205x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ctl_s2 | 189.030 | 270.541 | 0.699x | 0.696-0.702x | 0.692x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ctl_s5 | 189.030 | 188.416 | 1.003x | 0.998-1.008x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | kernl | 189.030 | 194.765 | 0.971x | 0.965-0.975x | 0.970x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_clamp | 189.030 | 156.467 | 1.208x | 1.202-1.217x | 1.212x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 189.030 | 156.672 | 1.207x | 1.202-1.214x | 1.211x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 193.331 | 156.672 | 1.234x | 1.231-1.240x | 1.238x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32 | 189.030 | 146.842 | 1.287x | 1.281-1.295x | 1.290x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 193.331 | 146.842 | 1.317x | 1.312-1.323x | 1.319x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 193.331 | 156.672 | 1.234x | 1.225-1.240x | 1.233x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 146.637 | 156.672 | 0.936x | 0.929-0.940x | 0.930x | 0.68-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | tt32 | 189.030 | 193.331 | 0.978x | 0.974-0.982x | 0.978x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_64x128x32_w4_s4_cold | tt38 | 189.030 | 146.637 | 1.289x | 1.285-1.295x | 1.296x | 1.18-1.82x | yes | NO | 0.0156 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro | 245.760 | 191.693 | 1.282x | 1.273-1.300x | 1.288x | 0.98-1.36x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ctl_r64 | 245.760 | 246.170 | 0.998x | 0.984-1.014x | 1.009x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ctl_s2 | 245.760 | 246.784 | 0.996x | 0.984-1.007x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ctl_s5 | 245.760 | 208.896 | 1.176x | 1.164-1.197x | 1.183x | 0.98-1.24x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | kernl | 245.760 | 260.506 | 0.943x | 0.927-0.960x | 0.948x | 0.89-0.98x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_clamp | 245.760 | 208.077 | 1.181x | 1.164-1.201x | 1.172x | 0.98-1.43x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32 | 245.760 | 194.765 | 1.262x | 1.246-1.281x | 1.268x | 0.98-1.26x | NO | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 242.074 | 194.765 | 1.243x | 1.229-1.260x | 1.244x | 0.97-1.25x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 246.170 | 191.693 | 1.284x | 1.269-1.306x | 1.277x | 0.98-1.36x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 242.074 | 191.693 | 1.263x | 1.256-1.278x | 1.264x | 0.97-1.35x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 437.043 | 191.693 | 2.280x | 2.271-2.296x | 2.276x | 0.85-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | tt32 | 245.760 | 242.074 | 1.015x | 1.005-1.025x | 1.019x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_warm | tt38 | 245.760 | 437.043 | 0.562x | 0.560-0.567x | 0.566x | 0.98-1.54x | NO | NO | 0.00195 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro | 254.771 | 198.246 | 1.285x | 1.256-1.304x | 1.277x | 1.25-1.63x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ctl_r64 | 254.771 | 255.386 | 0.998x | 0.981-1.020x | 0.998x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ctl_s2 | 254.771 | 254.362 | 1.002x | 0.977-1.024x | 1.013x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ctl_s5 | 254.771 | 211.558 | 1.204x | 1.170-1.230x | - | 1.28-1.51x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | kernl | 254.771 | 268.698 | 0.948x | 0.921-0.964x | 0.950x | 0.91-1.00x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_clamp | 254.771 | 214.426 | 1.188x | 1.166-1.203x | 1.179x | 1.22-1.60x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32 | 254.771 | 198.656 | 1.282x | 1.257-1.314x | - | 1.24-1.61x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 246.989 | 198.656 | 1.243x | 1.225-1.269x | - | 1.23-1.60x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 255.386 | 198.246 | 1.288x | 1.255-1.304x | 1.279x | 1.25-1.63x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 246.989 | 198.246 | 1.246x | 1.224-1.259x | 1.233x | 1.24-1.62x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 439.501 | 198.246 | 2.217x | 2.176-2.241x | 2.220x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | tt32 | 254.771 | 246.989 | 1.032x | 1.016-1.046x | 1.035x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m64_n4096_k4096_16x16x64_w4_s2_cold | tt38 | 254.771 | 439.501 | 0.580x | 0.571-0.588x | 0.575x | 1.34-1.70x | NO | NO | 0.00195 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro | 28.479 | 19.862 | 1.434x | 1.431-1.436x | 1.398x | 1.40-1.69x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ctl_s2 | 28.479 | 32.691 | 0.871x | 0.868-0.872x | 0.857x | 0.73-0.88x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ctl_s5 | 28.479 | 28.479 | 1.000x | 0.997-1.001x | 1.001x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | kernl | 28.479 | 30.024 | 0.949x | 0.941-0.951x | 0.933x | 0.89-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro_clamp | 28.479 | 18.896 | 1.507x | 1.504-1.514x | 1.483x | 1.44-1.93x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32 | 28.479 | 22.992 | 1.239x | 1.237-1.241x | 1.212x | 1.04-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 24.460 | 22.992 | 1.064x | 1.061-1.065x | 1.061x | 0.88-1.13x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 24.460 | 19.862 | 1.232x | 1.227-1.233x | 1.224x | 1.18-1.51x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 18.838 | 19.862 | 0.948x | 0.945-0.949x | 0.936x | 0.71-0.84x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | tt32 | 28.479 | 24.460 | 1.164x | 1.163-1.168x | 1.142x | 1.09-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_warm | tt38 | 28.479 | 18.838 | 1.512x | 1.510-1.517x | 1.493x | 1.74-2.27x | NO | NO | 0.000244 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro | 46.080 | 33.382 | 1.380x | 1.343-1.395x | 1.436x | 1.44-1.68x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ctl_s2 | 46.080 | 58.982 | 0.781x | 0.774-0.790x | 0.977x | 0.68-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ctl_s5 | 46.080 | 46.080 | 1.000x | 0.982-1.009x | 1.003x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | kernl | 46.080 | 47.309 | 0.974x | 0.961-0.987x | 0.970x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro_clamp | 46.080 | 31.744 | 1.452x | 1.429-1.468x | 1.536x | 1.59-1.73x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32 | 46.080 | 38.298 | 1.203x | 1.186-1.215x | 1.242x | 1.15-1.27x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 42.394 | 38.298 | 1.107x | 1.096-1.118x | 1.121x | 1.04-1.11x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 42.394 | 33.382 | 1.270x | 1.241-1.284x | 1.296x | 1.31-1.46x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 24.371 | 33.382 | 0.730x | 0.705-0.741x | 0.667x | 0.50-0.84x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | tt32 | 46.080 | 42.394 | 1.087x | 1.072-1.097x | 1.108x | 1.07-1.18x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s5_cold | tt38 | 46.080 | 24.371 | 1.891x | 1.858-1.932x | 2.154x | 2.01-2.82x | NO | NO | 0.000244 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro | 20.728 | 18.812 | 1.102x | 1.100-1.102x | - | 0.78-1.09x | NO | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ctl_s2 | 20.728 | 27.400 | 0.756x | 0.756-0.757x | 0.754x | 0.67-0.80x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ctl_s5 | 20.728 | 20.728 | 1.000x | 0.999-1.001x | 1.001x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | kernl | 20.728 | 21.355 | 0.971x | 0.969-0.971x | 0.972x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro_clamp | 20.728 | 22.941 | 0.904x | 0.903-0.904x | 0.894x | 0.66-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32 | 20.728 | 16.599 | 1.249x | 1.247-1.249x | 1.250x | 1.04-1.42x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 21.520 | 16.599 | 1.297x | 1.293-1.297x | 1.293x | 1.15-1.50x | yes | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 21.520 | 18.812 | 1.144x | 1.141-1.144x | - | 0.86-1.15x | yes | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 18.465 | 18.812 | 0.982x | 0.980-0.982x | - | 0.66-0.82x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | tt32 | 20.728 | 21.520 | 0.963x | 0.962-0.965x | 0.966x | 0.88-0.98x | yes | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_warm | tt38 | 20.728 | 18.465 | 1.123x | 1.122-1.124x | 1.151x | 1.00-1.57x | yes | NO | 0.000244 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro | 38.707 | 36.454 | 1.062x | 1.056-1.079x | - | 0.98-1.07x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ctl_s2 | 38.707 | 52.224 | 0.741x | 0.732-0.752x | 0.711x | 0.62-0.74x | NO | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ctl_s5 | 38.707 | 38.707 | 1.000x | 0.989-1.016x | 1.002x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | kernl | 38.707 | 39.526 | 0.979x | 0.964-0.995x | 0.972x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro_clamp | 38.707 | 31.130 | 1.243x | 1.221-1.265x | 1.287x | 0.83-1.34x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32 | 38.707 | 32.154 | 1.204x | 1.190-1.232x | 1.250x | 1.24-1.37x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 39.117 | 32.154 | 1.217x | 1.196-1.239x | 1.263x | 1.29-1.47x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 39.117 | 36.454 | 1.073x | 1.062-1.085x | - | 1.06-1.12x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 23.962 | 36.454 | 0.657x | 0.646-0.667x | - | 0.48-0.82x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | tt32 | 38.707 | 39.117 | 0.990x | 0.979-1.011x | 0.989x | 0.90-0.99x | NO | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_32x64x32_w2_s5_cold | tt38 | 38.707 | 23.962 | 1.615x | 1.593-1.661x | - | 1.25-2.08x | yes | NO | 0.000244 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro | 32.551 | 23.020 | 1.414x | 1.413-1.417x | 1.432x | 1.37-1.51x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ctl_s2 | 32.551 | 32.532 | 1.001x | 0.999-1.002x | 1.011x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ctl_s5 | 32.551 | 27.569 | 1.181x | 1.179-1.182x | 1.183x | 1.15-1.34x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | kernl | 32.551 | 34.954 | 0.931x | 0.930-0.933x | 0.939x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro_clamp | 32.551 | 23.335 | 1.395x | 1.393-1.398x | 1.417x | 1.39-1.64x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32 | 32.551 | 28.928 | 1.125x | 1.123-1.127x | 1.147x | 1.02-1.20x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 28.928 | 28.928 | 1.000x | 0.998-1.002x | 1.004x | 0.86-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 28.928 | 23.020 | 1.257x | 1.256-1.260x | 1.254x | 1.15-1.37x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 23.335 | 23.020 | 1.014x | 1.014-1.015x | 1.004x | 0.81-0.89x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | tt32 | 32.551 | 28.928 | 1.125x | 1.122-1.127x | 1.142x | 1.08-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_warm | tt38 | 32.551 | 23.335 | 1.395x | 1.393-1.397x | 1.426x | 1.59-1.79x | NO | NO | 0.000244 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro | 58.982 | 43.213 | 1.365x | 1.343-1.388x | 1.112x | 1.29-1.53x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ctl_s2 | 58.982 | 58.982 | 1.000x | 0.986-1.014x | 0.996x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ctl_s5 | 58.982 | 46.285 | 1.274x | 1.260-1.289x | 1.022x | 1.23-1.44x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | kernl | 58.982 | 61.440 | 0.960x | 0.947-0.970x | 0.956x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro_clamp | 58.982 | 43.622 | 1.352x | 1.336-1.374x | 1.093x | 1.50-1.75x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32 | 58.982 | 49.562 | 1.190x | 1.172-1.203x | 0.944x | 1.09-1.20x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 52.019 | 49.562 | 1.050x | 1.033-1.062x | 1.056x | 0.99-1.07x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 52.019 | 43.213 | 1.204x | 1.183-1.225x | 1.244x | 1.19-1.35x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 43.008 | 43.213 | 0.995x | 0.981-1.014x | 1.005x | 0.68-0.91x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | tt32 | 58.982 | 52.019 | 1.134x | 1.117-1.151x | 0.894x | 1.05-1.17x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x32x32_w2_s2_cold | tt38 | 58.982 | 43.008 | 1.371x | 1.349-1.388x | 1.106x | 1.68-1.89x | NO | NO | 0.000244 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro | 31.147 | 30.997 | 1.005x | 1.004-1.006x | 1.004x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ctl_s2 | 31.147 | 35.776 | 0.871x | 0.869-0.872x | 0.871x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ctl_s5 | 31.147 | 31.211 | 0.998x | 0.997-0.999x | 0.995x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | kernl | 31.147 | 33.387 | 0.933x | 0.931-0.934x | 0.929x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_clamp | 31.147 | 28.373 | 1.098x | 1.096-1.098x | 1.092x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 31.147 | 28.565 | 1.090x | 1.089-1.091x | 1.091x | 1.09-1.49x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 31.488 | 28.565 | 1.102x | 1.101-1.104x | 1.100x | 1.10-1.51x | NO | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32 | 31.147 | 27.819 | 1.120x | 1.107-1.120x | 1.116x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 31.488 | 27.819 | 1.132x | 1.119-1.134x | 1.125x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 31.488 | 30.997 | 1.016x | 1.015-1.017x | 1.013x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.483 | 30.997 | 1.209x | 1.208-1.226x | 1.209x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | tt32 | 31.147 | 31.488 | 0.989x | 0.988-0.990x | 0.992x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_warm | tt38 | 31.147 | 37.483 | 0.831x | 0.820-0.832x | 0.831x | 1.00-1.41x | NO | NO | 0.000244 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro | 50.176 | 41.370 | 1.213x | 1.202-1.224x | 1.248x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ctl_s2 | 50.176 | 64.922 | 0.773x | 0.767-0.778x | 0.977x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ctl_s5 | 50.176 | 49.971 | 1.004x | 0.996-1.012x | 1.005x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | kernl | 50.176 | 52.019 | 0.965x | 0.957-0.976x | 0.960x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_clamp | 50.176 | 41.165 | 1.219x | 1.208-1.230x | 1.248x | 1.19-1.29x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 50.176 | 40.550 | 1.237x | 1.214-1.255x | 1.273x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 50.790 | 40.550 | 1.253x | 1.229-1.270x | 1.281x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32 | 50.176 | 38.298 | 1.310x | 1.298-1.323x | 1.361x | 1.26-1.45x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 50.790 | 38.298 | 1.326x | 1.314-1.339x | 1.370x | 1.27-1.46x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 50.790 | 41.370 | 1.228x | 1.217-1.239x | 1.256x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 43.008 | 41.370 | 1.040x | 1.025-1.050x | 1.041x | 0.70-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | tt32 | 50.176 | 50.790 | 0.988x | 0.980-0.996x | 0.994x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_64x128x32_w4_s4_cold | tt38 | 50.176 | 43.008 | 1.167x | 1.156-1.183x | 1.199x | 1.17-1.76x | NO | NO | 0.000244 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro | 24.877 | 22.919 | 1.085x | 1.070-1.106x | 1.106x | 0.98-1.39x | yes | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ctl_r64 | 24.877 | 24.847 | 1.001x | 0.986-1.011x | 0.995x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ctl_s2 | 24.877 | 24.817 | 1.002x | 0.987-1.020x | 1.008x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ctl_s5 | 24.877 | 24.154 | 1.030x | 1.006-1.049x | 1.040x | 0.98-1.34x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | kernl | 24.877 | 24.245 | 1.026x | 1.007-1.046x | 1.033x | 0.90-0.99x | NO | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_clamp | 24.877 | 23.130 | 1.076x | 1.061-1.089x | 1.082x | 0.98-1.37x | yes | yes | 0 | 20, 20 | 64, 80 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32 | 24.877 | 23.462 | 1.060x | 1.043-1.078x | 1.074x | 0.98-1.38x | yes | yes | 0 | 20, 20 | 64, 63 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 26.895 | 23.462 | 1.146x | 1.124-1.177x | 1.150x | 0.97-1.37x | yes | yes | 0 | 20, 20 | 68, 63 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 24.847 | 22.919 | 1.084x | 1.073-1.108x | 1.111x | 0.98-1.39x | yes | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 26.895 | 22.919 | 1.173x | 1.154-1.209x | 1.184x | 0.97-1.39x | yes | yes | 0 | 20, 20 | 68, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 55.868 | 22.919 | 2.438x | 2.414-2.505x | 1.997x | 0.91-1.03x | NO | yes | 0 | 20, 20 | 90, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | tt32 | 24.877 | 26.895 | 0.925x | 0.903-0.940x | 0.934x | 0.97-1.04x | NO | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_warm | tt38 | 24.877 | 55.868 | 0.445x | 0.436-0.449x | 0.554x | 0.98-1.45x | NO | NO | 0.000488 | 20, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro | 36.250 | 33.178 | 1.093x | 1.074-1.126x | 1.129x | 1.23-1.55x | NO | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ctl_r64 | 36.250 | 36.250 | 1.000x | 0.978-1.017x | 0.994x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ctl_s2 | 36.250 | 36.250 | 1.000x | 0.972-1.029x | 1.007x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ctl_s5 | 36.250 | 31.130 | 1.164x | 1.129-1.193x | - | 1.25-1.46x | NO | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | kernl | 36.250 | 36.250 | 1.000x | 0.978-1.017x | 0.995x | 0.92-1.00x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_clamp | 36.250 | 33.997 | 1.066x | 1.042-1.091x | 1.047x | 1.20-1.53x | NO | yes | 0 | 20, 20 | 64, 80 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32 | 36.250 | 32.563 | 1.113x | 1.087-1.140x | - | 1.21-1.54x | NO | yes | 0 | 20, 20 | 64, 63 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 36.454 | 32.563 | 1.119x | 1.087-1.146x | - | 1.21-1.54x | NO | yes | 0 | 20, 20 | 68, 63 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 36.250 | 33.178 | 1.093x | 1.080-1.126x | 1.135x | 1.23-1.55x | NO | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 36.454 | 33.178 | 1.099x | 1.074-1.132x | 1.133x | 1.22-1.55x | NO | yes | 0 | 20, 20 | 68, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 61.645 | 33.178 | 1.858x | 1.840-1.925x | 1.627x | 0.91-1.03x | NO | yes | 0 | 20, 20 | 90, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | tt32 | 36.250 | 36.454 | 0.994x | 0.972-1.023x | 0.996x | 0.97-1.04x | yes | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k1024_16x16x64_w4_s2_cold | tt38 | 36.250 | 61.645 | 0.588x | 0.572-0.597x | 0.694x | 1.30-1.61x | NO | NO | 0.000488 | 20, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro | 116.288 | 70.272 | 1.655x | 1.649-1.661x | 1.450x | 1.42-1.76x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ctl_s2 | 116.288 | 123.264 | 0.943x | 0.937-0.954x | 0.835x | 0.72-0.88x | NO | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ctl_s5 | 116.288 | 105.728 | 1.100x | 1.091-1.106x | 0.986x | 0.97-1.03x | NO | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | kernl | 116.288 | 110.272 | 1.055x | 1.049-1.062x | 0.939x | 0.89-0.97x | NO | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro_clamp | 116.288 | 66.240 | 1.756x | 1.744-1.761x | 1.543x | 1.47-2.04x | yes | yes | 0 | 2, 2 | 168, 239 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32 | 116.288 | 83.008 | 1.401x | 1.393-1.407x | 1.230x | 1.04-1.29x | NO | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 89.408 | 83.008 | 1.077x | 1.066-1.087x | 1.070x | 0.88-1.14x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 89.408 | 70.272 | 1.272x | 1.262-1.284x | 1.261x | 1.19-1.56x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 66.176 | 70.272 | 0.942x | 0.939-0.944x | 0.933x | 0.68-0.83x | NO | yes | 0 | 2, 2 | 216, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | tt32 | 116.288 | 89.408 | 1.301x | 1.288-1.313x | 1.150x | 1.10-1.22x | NO | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_warm | tt38 | 116.288 | 66.176 | 1.757x | 1.751-1.765x | 1.554x | 1.79-2.46x | NO | NO | 0.0156 | 2, 2 | 168, 216 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro | 166.502 | 117.146 | 1.421x | 1.409-1.432x | 1.433x | 1.48-1.72x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ctl_s2 | 166.502 | 218.112 | 0.763x | 0.758-0.768x | 0.754x | 0.67-0.82x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ctl_s5 | 166.502 | 166.298 | 1.001x | 0.991-1.009x | 0.996x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | kernl | 166.502 | 171.622 | 0.970x | 0.962-0.977x | 0.961x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro_clamp | 166.502 | 107.110 | 1.554x | 1.538-1.560x | 1.570x | 1.64-1.77x | NO | yes | 0 | 2, 2 | 168, 239 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32 | 166.502 | 132.710 | 1.255x | 1.247-1.261x | 1.260x | 1.16-1.28x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 149.914 | 132.710 | 1.130x | 1.125-1.133x | 1.135x | 1.05-1.11x | NO | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 149.914 | 117.146 | 1.280x | 1.272-1.286x | 1.291x | 1.34-1.49x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 72.090 | 117.146 | 0.615x | 0.610-0.619x | 0.595x | 0.46-0.83x | yes | yes | 0 | 2, 2 | 216, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | tt32 | 166.502 | 149.914 | 1.111x | 1.104-1.118x | 1.110x | 1.07-1.19x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s5_cold | tt38 | 166.502 | 72.090 | 2.310x | 2.292-2.331x | 2.408x | 2.09-3.09x | yes | NO | 0.0156 | 2, 2 | 168, 216 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro | 74.638 | 68.210 | 1.094x | 1.088-1.118x | - | 0.77-1.10x | yes | yes | 0 | 2, 2 | 165, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ctl_s2 | 74.638 | 99.783 | 0.748x | 0.744-0.751x | 0.828x | 0.65-0.79x | yes | yes | 0 | 2, 2 | 165, 162 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ctl_s5 | 74.638 | 80.327 | 0.929x | 0.924-0.934x | 1.042x | 0.97-1.03x | NO | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | kernl | 74.638 | 78.962 | 0.945x | 0.936-0.964x | 1.280x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro_clamp | 74.638 | 81.863 | 0.912x | 0.908-0.915x | 1.274x | 0.65-1.10x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32 | 74.638 | 58.937 | 1.266x | 1.252-1.274x | 1.760x | 1.05-1.47x | yes | yes | 0 | 2, 2 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 109.227 | 58.937 | 1.853x | 1.817-1.862x | 1.846x | 1.16-1.56x | NO | yes | 0 | 2, 2 | 168, 164 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 109.227 | 68.210 | 1.601x | 1.580-1.634x | - | 0.85-1.16x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 64.455 | 68.210 | 0.945x | 0.942-0.963x | - | 0.63-0.81x | NO | yes | 0 | 2, 2 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | tt32 | 74.638 | 109.227 | 0.683x | 0.680-0.693x | 0.954x | 0.88-0.97x | NO | yes | 0 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_warm | tt38 | 74.638 | 64.455 | 1.158x | 1.153-1.163x | 1.633x | 1.00-1.65x | yes | NO | 0.0156 | 2, 2 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro | 135.168 | 127.795 | 1.058x | 1.051-1.063x | - | 0.98-1.08x | yes | yes | 0 | 2, 2 | 165, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ctl_s2 | 135.168 | 191.078 | 0.707x | 0.704-0.712x | 0.698x | 0.61-0.73x | yes | yes | 0 | 2, 2 | 165, 162 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ctl_s5 | 135.168 | 135.168 | 1.000x | 0.994-1.005x | 1.003x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | kernl | 135.168 | 139.264 | 0.971x | 0.962-0.976x | 0.968x | 0.94-1.01x | yes | yes | 0 | 2, 2 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro_clamp | 135.168 | 102.810 | 1.315x | 1.308-1.327x | 1.331x | 0.83-1.37x | yes | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32 | 135.168 | 113.050 | 1.196x | 1.190-1.204x | 1.205x | 1.26-1.40x | NO | yes | 0 | 2, 2 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 139.674 | 113.050 | 1.236x | 1.231-1.245x | 1.250x | 1.32-1.50x | NO | yes | 0 | 2, 2 | 168, 164 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 139.674 | 127.795 | 1.093x | 1.088-1.100x | - | 1.06-1.13x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 69.427 | 127.795 | 0.543x | 0.540-0.547x | - | 0.45-0.81x | yes | yes | 0 | 2, 2 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | tt32 | 135.168 | 139.674 | 0.968x | 0.961-0.972x | 0.964x | 0.90-0.99x | yes | yes | 0 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_32x64x32_w2_s5_cold | tt38 | 135.168 | 69.427 | 1.947x | 1.930-1.959x | - | 1.27-2.23x | yes | NO | 0.0156 | 2, 2 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro | 122.953 | 84.553 | 1.454x | 1.431-1.485x | 1.464x | 1.39-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ctl_s2 | 122.953 | 121.490 | 1.012x | 0.999-1.020x | 1.014x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ctl_s5 | 122.953 | 105.984 | 1.160x | 1.143-1.176x | 1.182x | 1.15-1.36x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | kernl | 122.953 | 133.998 | 0.918x | 0.908-0.935x | 0.927x | 0.88-0.97x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro_clamp | 122.953 | 86.821 | 1.416x | 1.398-1.448x | 1.448x | 1.41-1.68x | yes | yes | 0 | 2, 2 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32 | 122.953 | 110.153 | 1.116x | 1.106-1.127x | 1.119x | 1.02-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 111.835 | 110.153 | 1.015x | 1.005-1.031x | 1.273x | 0.85-1.09x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 111.835 | 84.553 | 1.323x | 1.299-1.357x | 1.665x | 1.16-1.39x | yes | yes | 0 | 2, 2 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 87.186 | 84.553 | 1.031x | 1.003-1.051x | 1.025x | 0.80-0.88x | NO | yes | 0 | 2, 2 | 212, 234 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | tt32 | 122.953 | 111.835 | 1.099x | 1.082-1.113x | 0.879x | 1.09-1.22x | yes | yes | 0 | 2, 2 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_warm | tt38 | 122.953 | 87.186 | 1.410x | 1.398-1.442x | 1.428x | 1.63-1.86x | NO | NO | 0.0156 | 2, 2 | 168, 212 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro | 218.112 | 149.914 | 1.455x | 1.448-1.462x | 1.470x | 1.31-1.55x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ctl_s2 | 218.112 | 218.112 | 1.000x | 0.996-1.004x | 0.996x | 0.97-1.03x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ctl_s5 | 218.112 | 166.093 | 1.313x | 1.303-1.321x | 1.320x | 1.24-1.46x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | kernl | 218.112 | 227.942 | 0.957x | 0.953-0.960x | 0.955x | 0.90-0.98x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro_clamp | 218.112 | 151.552 | 1.439x | 1.433-1.446x | 1.457x | 1.52-1.80x | NO | yes | 0 | 2, 2 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32 | 218.112 | 180.838 | 1.206x | 1.200-1.210x | 1.211x | 1.10-1.21x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 190.259 | 180.838 | 1.052x | 1.047-1.056x | 1.055x | 1.00-1.07x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 190.259 | 149.914 | 1.269x | 1.264-1.275x | 1.281x | 1.20-1.36x | yes | yes | 0 | 2, 2 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 151.142 | 149.914 | 1.008x | 1.004-1.014x | 1.007x | 0.67-0.90x | NO | yes | 0 | 2, 2 | 212, 234 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | tt32 | 218.112 | 190.259 | 1.146x | 1.142-1.150x | 1.147x | 1.05-1.18x | yes | yes | 0 | 2, 2 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x32x32_w2_s2_cold | tt38 | 218.112 | 151.142 | 1.443x | 1.436-1.448x | 1.459x | 1.71-1.94x | NO | NO | 0.0156 | 2, 2 | 168, 212 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro | 110.319 | 109.909 | 1.004x | 1.002-1.010x | 1.017x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ctl_s2 | 110.319 | 130.662 | 0.844x | 0.837-0.850x | 0.859x | 0.71-0.86x | yes | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ctl_s5 | 110.319 | 112.367 | 0.982x | 0.973-0.988x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | kernl | 110.319 | 121.242 | 0.910x | 0.906-0.918x | 0.938x | 0.95-1.01x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_clamp | 110.319 | 99.260 | 1.111x | 1.109-1.118x | 1.122x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 110.319 | 102.400 | 1.077x | 1.075-1.084x | 1.089x | 1.10-1.54x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 114.415 | 102.400 | 1.117x | 1.114-1.135x | 1.118x | 1.11-1.55x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32 | 110.319 | 100.011 | 1.103x | 1.096-1.114x | 1.120x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 114.415 | 100.011 | 1.144x | 1.135-1.167x | 1.149x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 114.415 | 109.909 | 1.041x | 1.038-1.058x | 1.045x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 137.967 | 109.909 | 1.255x | 1.253-1.257x | 1.253x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | tt32 | 110.319 | 114.415 | 0.964x | 0.948-0.972x | 0.974x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_warm | tt38 | 110.319 | 137.967 | 0.800x | 0.798-0.805x | 0.812x | 1.00-1.44x | NO | NO | 0.0156 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro | 179.200 | 143.770 | 1.246x | 1.238-1.255x | 1.249x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ctl_s2 | 179.200 | 240.845 | 0.744x | 0.740-0.750x | 0.733x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ctl_s5 | 179.200 | 178.790 | 1.002x | 0.998-1.010x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | kernl | 179.200 | 185.754 | 0.965x | 0.960-0.972x | 0.957x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_clamp | 179.200 | 143.360 | 1.250x | 1.245-1.261x | 1.255x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 179.200 | 143.770 | 1.246x | 1.238-1.257x | 1.258x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 184.525 | 143.770 | 1.283x | 1.275-1.293x | 1.302x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32 | 179.200 | 133.530 | 1.342x | 1.333-1.356x | 1.355x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 184.525 | 133.530 | 1.382x | 1.373-1.394x | 1.402x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 184.525 | 143.770 | 1.283x | 1.275-1.291x | 1.292x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 144.998 | 143.770 | 1.009x | 1.003-1.011x | 1.007x | 0.68-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | tt32 | 179.200 | 184.525 | 0.971x | 0.965-0.979x | 0.967x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_64x128x32_w4_s4_cold | tt38 | 179.200 | 144.998 | 1.236x | 1.231-1.245x | 1.240x | 1.18-1.82x | yes | NO | 0.0156 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro | 89.998 | 81.465 | 1.105x | 1.080-1.130x | 1.123x | 0.98-1.45x | yes | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ctl_r64 | 89.998 | 92.046 | 0.978x | 0.954-1.001x | 1.033x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ctl_s2 | 89.998 | 90.226 | 0.997x | 0.973-1.019x | 1.029x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ctl_s5 | 89.998 | 81.465 | 1.105x | 1.079-1.129x | - | 0.98-1.39x | yes | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | kernl | 89.998 | 83.968 | 1.072x | 1.046-1.093x | 1.118x | 0.89-0.99x | NO | yes | 0 | 20, 20 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_clamp | 89.998 | 82.830 | 1.087x | 1.057-1.118x | 1.138x | 0.98-1.42x | yes | yes | 0 | 20, 20 | 64, 80 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32 | 89.998 | 84.082 | 1.070x | 1.044-1.092x | - | 0.98-1.44x | yes | yes | 0 | 20, 20 | 64, 63 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 104.789 | 84.082 | 1.246x | 1.218-1.278x | - | 0.97-1.43x | yes | yes | 0 | 20, 20 | 68, 63 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 92.046 | 81.465 | 1.130x | 1.104-1.159x | 1.088x | 0.98-1.45x | yes | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 104.789 | 81.465 | 1.286x | 1.260-1.323x | 1.256x | 0.97-1.44x | yes | yes | 0 | 20, 20 | 68, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 215.381 | 81.465 | 2.644x | 2.618-2.711x | 2.601x | 0.90-1.03x | NO | yes | 0 | 20, 20 | 90, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | tt32 | 89.998 | 104.789 | 0.859x | 0.835-0.877x | 0.894x | 0.97-1.04x | NO | yes | 0 | 20, 20 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_warm | tt38 | 89.998 | 215.381 | 0.418x | 0.408-0.422x | 0.432x | 0.98-1.53x | NO | NO | 0.000488 | 20, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro | 117.965 | 107.725 | 1.095x | 1.083-1.107x | 1.096x | 1.25-1.62x | NO | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ctl_r64 | 117.965 | 117.965 | 1.000x | 0.993-1.009x | 0.999x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ctl_s2 | 117.965 | 117.965 | 1.000x | 0.991-1.010x | 0.998x | 0.97-1.03x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ctl_s5 | 117.965 | 97.485 | 1.210x | 1.193-1.231x | - | 1.27-1.50x | NO | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | kernl | 117.965 | 122.061 | 0.966x | 0.958-0.975x | 0.968x | 0.91-1.00x | yes | yes | 0 | 20, 20 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_clamp | 117.965 | 112.435 | 1.049x | 1.038-1.060x | 1.032x | 1.22-1.59x | NO | yes | 0 | 20, 20 | 64, 80 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32 | 117.965 | 107.930 | 1.093x | 1.083-1.111x | - | 1.24-1.61x | NO | yes | 0 | 20, 20 | 64, 63 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 123.085 | 107.930 | 1.140x | 1.123-1.159x | - | 1.23-1.60x | NO | yes | 0 | 20, 20 | 68, 63 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 117.965 | 107.725 | 1.095x | 1.085-1.103x | 1.097x | 1.25-1.62x | NO | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 123.085 | 107.725 | 1.143x | 1.123-1.155x | 1.145x | 1.24-1.61x | NO | yes | 0 | 20, 20 | 68, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 222.413 | 107.725 | 2.065x | 2.045-2.090x | 2.114x | 0.91-1.03x | NO | yes | 0 | 20, 20 | 90, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | tt32 | 117.965 | 123.085 | 0.958x | 0.949-0.975x | 0.957x | 0.97-1.04x | NO | yes | 0 | 20, 20 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n1024_k4096_16x16x64_w4_s2_cold | tt38 | 117.965 | 222.413 | 0.530x | 0.524-0.535x | 0.519x | 1.33-1.69x | NO | NO | 0.000488 | 20, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro | 34.315 | 30.197 | 1.136x | 1.119-1.153x | 1.191x | 1.33-1.69x | NO | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ctl_s2 | 34.315 | 37.779 | 0.908x | 0.897-0.922x | 0.943x | 0.73-0.88x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ctl_s5 | 34.315 | 34.467 | 0.996x | 0.979-1.010x | 1.021x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | kernl | 34.315 | 36.428 | 0.942x | 0.933-0.958x | 0.970x | 0.89-0.97x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro_clamp | 34.315 | 31.090 | 1.104x | 1.088-1.121x | 1.170x | 1.33-1.90x | NO | yes | 0 | 6, 6 | 168, 239 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32 | 34.315 | 31.809 | 1.079x | 1.063-1.095x | 1.138x | 1.04-1.27x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 34.271 | 31.809 | 1.077x | 1.058-1.091x | 1.064x | 0.88-1.13x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 34.271 | 30.197 | 1.135x | 1.113-1.149x | 1.113x | 1.18-1.51x | NO | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 35.927 | 30.197 | 1.190x | 1.172-1.207x | 1.184x | 0.78-1.03x | NO | yes | 0 | 6, 6 | 216, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | tt32 | 34.315 | 34.271 | 1.001x | 0.989-1.020x | 1.069x | 1.09-1.21x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_warm | tt38 | 34.315 | 35.927 | 0.955x | 0.941-0.969x | 1.005x | 1.33-1.90x | NO | NO | 0.000977 | 6, 6 | 168, 216 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro | 57.344 | 49.152 | 1.167x | 1.149-1.195x | 1.186x | 1.44-1.68x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ctl_s2 | 57.344 | 74.342 | 0.771x | 0.759-0.781x | 0.940x | 0.68-0.82x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ctl_s5 | 57.344 | 57.344 | 1.000x | 0.982-1.014x | 1.233x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | kernl | 57.344 | 56.934 | 1.007x | 0.993-1.018x | 1.002x | 0.90-0.98x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro_clamp | 57.344 | 49.971 | 1.148x | 1.126-1.165x | 1.147x | 1.59-1.73x | NO | yes | 0 | 6, 6 | 168, 239 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32 | 57.344 | 51.610 | 1.111x | 1.095-1.128x | 1.107x | 1.15-1.27x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 56.730 | 51.610 | 1.099x | 1.087-1.120x | 1.108x | 1.04-1.11x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 56.730 | 49.152 | 1.154x | 1.141-1.186x | 1.188x | 1.31-1.46x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 44.646 | 49.152 | 0.908x | 0.896-0.932x | 0.902x | 0.62-0.90x | NO | yes | 0 | 6, 6 | 216, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | tt32 | 57.344 | 56.730 | 1.011x | 0.989-1.025x | 0.999x | 1.07-1.18x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s5_cold | tt38 | 57.344 | 44.646 | 1.284x | 1.259-1.306x | 1.315x | 1.65-2.28x | NO | NO | 0.000977 | 6, 6 | 168, 216 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro | 35.477 | 30.059 | 1.180x | 1.175-1.185x | - | 0.78-1.09x | NO | yes | 0 | 6, 6 | 165, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ctl_s2 | 35.477 | 35.840 | 0.990x | 0.986-0.995x | 0.953x | 0.67-0.89x | NO | yes | 0 | 6, 6 | 165, 162 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ctl_s5 | 35.477 | 35.456 | 1.001x | 0.996-1.005x | 1.010x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | kernl | 35.477 | 33.835 | 1.049x | 1.043-1.058x | 1.055x | 0.94-1.03x | NO | yes | 0 | 6, 6 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro_clamp | 35.477 | 31.467 | 1.127x | 1.123-1.133x | 1.143x | 0.66-1.10x | NO | yes | 0 | 6, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32 | 35.477 | 28.672 | 1.237x | 1.231-1.252x | 1.261x | 0.97-1.28x | yes | yes | 0 | 6, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 31.680 | 28.672 | 1.105x | 1.095-1.118x | 1.091x | 0.97-1.35x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 31.680 | 30.059 | 1.054x | 1.045-1.058x | - | 0.86-1.15x | yes | yes | 0 | 6, 6 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 35.349 | 30.059 | 1.176x | 1.171-1.183x | - | 0.76-1.03x | NO | yes | 0 | 6, 6 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | tt32 | 35.477 | 31.680 | 1.120x | 1.115-1.129x | 1.156x | 0.88-1.03x | NO | yes | 0 | 6, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_warm | tt38 | 35.477 | 35.349 | 1.004x | 0.998-1.008x | 1.013x | 0.97-1.28x | yes | NO | 0.000977 | 6, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro | 54.682 | 50.995 | 1.072x | 1.052-1.089x | - | 0.98-1.07x | yes | yes | 0 | 6, 6 | 165, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ctl_s2 | 54.682 | 68.608 | 0.797x | 0.786-0.811x | 0.987x | 0.62-0.74x | NO | yes | 0 | 6, 6 | 165, 162 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ctl_s5 | 54.682 | 55.091 | 0.993x | 0.971-1.019x | 1.009x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | kernl | 54.682 | 53.453 | 1.023x | 1.008-1.042x | 1.020x | 0.94-1.01x | NO | yes | 0 | 6, 6 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro_clamp | 54.682 | 48.742 | 1.122x | 1.109-1.144x | 1.130x | 0.83-1.34x | yes | yes | 0 | 6, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32 | 54.682 | 48.538 | 1.127x | 1.113-1.149x | 1.145x | 1.05-1.37x | yes | yes | 0 | 6, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 47.923 | 48.538 | 0.987x | 0.958-1.017x | 0.952x | 1.09-1.47x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 47.923 | 50.995 | 0.940x | 0.905-0.964x | - | 1.06-1.12x | NO | yes | 0 | 6, 6 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 46.694 | 50.995 | 0.916x | 0.893-0.927x | - | 0.60-1.00x | yes | yes | 0 | 6, 6 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | tt32 | 54.682 | 47.923 | 1.141x | 1.109-1.184x | 1.203x | 0.90-0.99x | NO | yes | 0 | 6, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_32x64x32_w2_s5_cold | tt38 | 54.682 | 46.694 | 1.171x | 1.152-1.200x | - | 1.05-1.69x | yes | NO | 0.000977 | 6, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro | 37.678 | 32.209 | 1.170x | 1.159-1.177x | 1.291x | 1.37-1.51x | NO | yes | 0 | 6, 6 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ctl_s2 | 37.678 | 37.283 | 1.011x | 1.006-1.016x | 1.012x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ctl_s5 | 37.678 | 34.420 | 1.095x | 1.088-1.103x | 1.197x | 1.15-1.34x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | kernl | 37.678 | 41.100 | 0.917x | 0.911-0.924x | 0.998x | 0.88-0.97x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro_clamp | 37.678 | 35.235 | 1.069x | 1.060-1.079x | 0.952x | 1.39-1.64x | NO | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32 | 37.678 | 36.119 | 1.043x | 1.037-1.052x | 1.158x | 1.02-1.20x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 36.562 | 36.119 | 1.012x | 1.006-1.024x | 1.028x | 0.86-1.09x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 36.562 | 32.209 | 1.135x | 1.125-1.145x | 1.146x | 1.15-1.37x | NO | yes | 0 | 6, 6 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 38.959 | 32.209 | 1.210x | 1.197-1.220x | 1.295x | 0.81-0.89x | NO | yes | 0 | 6, 6 | 212, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | tt32 | 37.678 | 36.562 | 1.031x | 1.022-1.036x | 1.126x | 1.08-1.21x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_warm | tt38 | 37.678 | 38.959 | 0.967x | 0.960-0.974x | 0.997x | 1.59-1.79x | NO | NO | 0.000977 | 6, 6 | 168, 212 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro | 74.752 | 56.525 | 1.322x | 1.302-1.336x | 1.061x | 1.29-1.53x | yes | yes | 0 | 6, 6 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ctl_s2 | 74.752 | 74.547 | 1.003x | 0.992-1.011x | 1.008x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ctl_s5 | 74.752 | 57.344 | 1.304x | 1.279-1.312x | 1.319x | 1.23-1.44x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | kernl | 74.752 | 78.438 | 0.953x | 0.938-0.963x | 0.949x | 0.90-0.98x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro_clamp | 74.752 | 61.030 | 1.225x | 1.211-1.232x | 1.249x | 1.50-1.75x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32 | 74.752 | 59.597 | 1.254x | 1.240-1.266x | 1.286x | 1.09-1.20x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 61.645 | 59.597 | 1.034x | 1.024-1.062x | 1.025x | 0.99-1.07x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 61.645 | 56.525 | 1.091x | 1.076-1.120x | 0.845x | 1.19-1.35x | NO | yes | 0 | 6, 6 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 62.669 | 56.525 | 1.109x | 1.090-1.120x | 0.872x | 0.68-0.91x | NO | yes | 0 | 6, 6 | 212, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | tt32 | 74.752 | 61.645 | 1.213x | 1.179-1.224x | 1.255x | 1.05-1.17x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x32x32_w2_s2_cold | tt38 | 74.752 | 62.669 | 1.193x | 1.179-1.208x | 1.217x | 1.68-1.89x | NO | NO | 0.000977 | 6, 6 | 168, 212 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro | 33.559 | 31.348 | 1.071x | 1.067-1.077x | 1.103x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ctl_s2 | 33.559 | 38.447 | 0.873x | 0.870-0.878x | 0.868x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ctl_s5 | 33.559 | 33.583 | 0.999x | 0.996-1.004x | 1.049x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | kernl | 33.559 | 35.165 | 0.954x | 0.952-0.959x | 1.005x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_clamp | 33.559 | 28.253 | 1.188x | 1.180-1.194x | 1.189x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 33.559 | 28.532 | 1.176x | 1.168-1.181x | 1.219x | 1.09-1.49x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 33.769 | 28.532 | 1.184x | 1.174-1.190x | 1.163x | 1.10-1.51x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32 | 33.559 | 28.974 | 1.158x | 1.155-1.164x | 1.204x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 33.769 | 28.974 | 1.165x | 1.160-1.172x | 1.148x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 33.769 | 31.348 | 1.077x | 1.072-1.084x | 1.052x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 39.401 | 31.348 | 1.257x | 1.253-1.263x | 1.246x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | tt32 | 33.559 | 33.769 | 0.994x | 0.989-0.999x | 1.048x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_warm | tt38 | 33.559 | 39.401 | 0.852x | 0.849-0.855x | 0.885x | 1.00-1.41x | NO | NO | 0.000977 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro | 58.573 | 51.814 | 1.130x | 1.122-1.143x | 0.901x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ctl_s2 | 58.573 | 79.462 | 0.737x | 0.733-0.744x | 0.723x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ctl_s5 | 58.573 | 58.368 | 1.004x | 0.997-1.014x | 1.003x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | kernl | 58.573 | 60.826 | 0.963x | 0.938-0.973x | 0.963x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_clamp | 58.573 | 51.405 | 1.139x | 1.131-1.148x | 0.905x | 1.19-1.29x | NO | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 58.573 | 51.405 | 1.139x | 1.126-1.148x | 0.907x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 58.368 | 51.405 | 1.135x | 1.119-1.144x | 0.906x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32 | 58.573 | 48.538 | 1.207x | 1.192-1.216x | 0.970x | 1.26-1.45x | NO | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 58.368 | 48.538 | 1.203x | 1.184-1.212x | 0.968x | 1.27-1.46x | NO | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 58.368 | 51.814 | 1.126x | 1.114-1.139x | 0.899x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 45.261 | 51.814 | 0.874x | 0.862-0.880x | 0.863x | 0.70-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | tt32 | 58.573 | 58.368 | 1.004x | 0.997-1.014x | 1.002x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_64x128x32_w4_s4_cold | tt38 | 58.573 | 45.261 | 1.294x | 1.290-1.311x | 1.044x | 1.17-1.76x | yes | NO | 0.000977 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro | 84.992 | 81.613 | 1.041x | 1.022-1.072x | 1.035x | 0.97-1.24x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ctl_r64 | 84.992 | 84.890 | 1.001x | 0.979-1.017x | 0.995x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ctl_s2 | 84.992 | 85.094 | 0.999x | 0.979-1.018x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ctl_s5 | 84.992 | 85.504 | 0.994x | 0.977-1.018x | 1.012x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | kernl | 84.992 | 86.118 | 0.987x | 0.966-0.999x | 0.994x | 0.90-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_clamp | 84.992 | 87.552 | 0.971x | 0.952-0.991x | 0.944x | 0.79-1.08x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32 | 84.992 | 82.637 | 1.029x | 1.006-1.046x | 1.011x | 0.97-1.20x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 86.221 | 82.637 | 1.043x | 1.021-1.062x | 1.024x | 0.97-1.20x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 84.890 | 81.613 | 1.040x | 1.026-1.073x | 1.040x | 0.97-1.24x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 86.221 | 81.613 | 1.056x | 1.037-1.088x | 1.048x | 0.97-1.24x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 211.354 | 81.613 | 2.590x | 2.564-2.666x | 2.027x | 0.97-1.25x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | tt32 | 84.992 | 86.221 | 0.986x | 0.965-1.006x | 0.987x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_warm | tt38 | 84.992 | 211.354 | 0.402x | 0.394-0.407x | 0.510x | 0.88-1.17x | NO | NO | 0.000977 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro | 102.810 | 88.883 | 1.157x | 1.130-1.179x | 1.163x | 1.06-1.61x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ctl_r64 | 102.810 | 102.400 | 1.004x | 0.976-1.024x | 1.012x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ctl_s2 | 102.810 | 102.810 | 1.000x | 0.976-1.022x | 1.012x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ctl_s5 | 102.810 | 92.365 | 1.113x | 1.081-1.139x | - | 1.06-1.50x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | kernl | 102.810 | 100.147 | 1.027x | 1.004-1.045x | 1.030x | 0.91-1.00x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_clamp | 102.810 | 103.629 | 0.992x | 0.969-1.014x | 0.984x | 0.91-1.21x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32 | 102.810 | 89.088 | 1.154x | 1.130-1.176x | - | 1.06-1.58x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 98.509 | 89.088 | 1.106x | 1.087-1.118x | - | 1.05-1.58x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 102.400 | 88.883 | 1.152x | 1.133-1.177x | 1.149x | 1.06-1.61x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 98.509 | 88.883 | 1.108x | 1.087-1.121x | 1.103x | 1.05-1.60x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 219.955 | 88.883 | 2.475x | 2.435-2.530x | 2.026x | 0.97-1.29x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | tt32 | 102.810 | 98.509 | 1.044x | 1.025-1.067x | 1.055x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k1024_16x16x64_w4_s2_cold | tt38 | 102.810 | 219.955 | 0.467x | 0.454-0.477x | 0.574x | 1.00-1.28x | NO | NO | 0.000977 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro | 175.104 | 125.235 | 1.398x | 1.384-1.408x | 1.402x | 1.36-1.76x | yes | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ctl_s2 | 175.104 | 219.546 | 0.798x | 0.787-0.804x | 0.796x | 0.72-0.88x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ctl_s5 | 175.104 | 175.206 | 0.999x | 0.991-1.012x | 1.003x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | kernl | 175.104 | 171.110 | 1.023x | 1.015-1.034x | 1.022x | 0.89-0.97x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro_clamp | 175.104 | 120.525 | 1.453x | 1.438-1.470x | 1.461x | 1.36-2.01x | yes | yes | 0 | 6, 6 | 168, 239 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32 | 175.104 | 151.347 | 1.157x | 1.146-1.172x | 1.159x | 1.04-1.29x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 173.568 | 151.347 | 1.147x | 1.125-1.165x | 1.140x | 0.88-1.14x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 173.568 | 125.235 | 1.386x | 1.359-1.399x | 1.379x | 1.19-1.56x | yes | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 132.403 | 125.235 | 1.057x | 1.043-1.065x | 1.054x | 0.77-1.03x | NO | yes | 0 | 6, 6 | 216, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | tt32 | 175.104 | 173.568 | 1.009x | 0.998-1.028x | 1.017x | 1.10-1.22x | NO | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_warm | tt38 | 175.104 | 132.403 | 1.323x | 1.311-1.339x | 1.330x | 1.36-2.01x | NO | NO | 0.0156 | 6, 6 | 168, 216 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro | 184.934 | 138.240 | 1.338x | 1.321-1.353x | 1.346x | 1.48-1.72x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ctl_s2 | 184.934 | 233.882 | 0.791x | 0.782-0.802x | 0.781x | 0.67-0.82x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ctl_s5 | 184.934 | 185.139 | 0.999x | 0.989-1.012x | 0.999x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | kernl | 184.934 | 181.248 | 1.020x | 1.009-1.033x | 1.017x | 0.90-0.98x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro_clamp | 184.934 | 138.650 | 1.334x | 1.317-1.355x | 1.351x | 1.64-1.77x | NO | yes | 0 | 6, 6 | 168, 239 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32 | 184.934 | 161.792 | 1.143x | 1.130-1.154x | 1.145x | 1.16-1.28x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 183.296 | 161.792 | 1.133x | 1.121-1.141x | 1.137x | 1.05-1.11x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 183.296 | 138.240 | 1.326x | 1.310-1.338x | 1.336x | 1.34-1.49x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 137.626 | 138.240 | 0.996x | 0.985-1.007x | 0.995x | 0.58-0.89x | NO | yes | 0 | 6, 6 | 216, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | tt32 | 184.934 | 183.296 | 1.009x | 0.999-1.020x | 1.008x | 1.07-1.19x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s5_cold | tt38 | 184.934 | 137.626 | 1.344x | 1.326-1.357x | 1.353x | 1.71-2.52x | NO | NO | 0.0156 | 6, 6 | 168, 216 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro | 160.861 | 139.264 | 1.155x | 1.135-1.165x | 1.170x | 0.77-1.10x | NO | yes | 0 | 6, 6 | 165, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ctl_s2 | 160.861 | 194.188 | 0.828x | 0.817-0.838x | 0.845x | 0.65-0.89x | yes | yes | 0 | 6, 6 | 165, 162 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ctl_s5 | 160.861 | 160.582 | 1.002x | 0.986-1.013x | 1.006x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | kernl | 160.861 | 150.621 | 1.068x | 1.052-1.081x | 1.096x | 0.94-1.03x | NO | yes | 0 | 6, 6 | 165, 165 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro_clamp | 160.861 | 116.643 | 1.379x | 1.361-1.400x | 1.404x | 0.65-1.10x | NO | yes | 0 | 6, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32 | 160.861 | 126.976 | 1.267x | 1.248-1.282x | 1.292x | 0.97-1.30x | yes | yes | 0 | 6, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 135.168 | 126.976 | 1.065x | 1.047-1.089x | 1.047x | 0.97-1.38x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 135.168 | 139.264 | 0.971x | 0.952-0.990x | 0.948x | 0.85-1.16x | yes | yes | 0 | 6, 6 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 132.468 | 139.264 | 0.951x | 0.935-0.956x | 0.930x | 0.75-1.03x | yes | yes | 0 | 6, 6 | 168, 166 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | tt32 | 160.861 | 135.168 | 1.190x | 1.156-1.213x | 1.234x | 0.88-1.03x | NO | yes | 0 | 6, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_warm | tt38 | 160.861 | 132.468 | 1.214x | 1.198-1.235x | 1.259x | 0.97-1.30x | yes | NO | 0.0156 | 6, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro | 173.670 | 149.914 | 1.158x | 1.122-1.193x | - | 0.98-1.08x | NO | yes | 0 | 6, 6 | 165, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ctl_s2 | 173.670 | 208.282 | 0.834x | 0.812-0.855x | 0.861x | 0.61-0.73x | NO | yes | 0 | 6, 6 | 165, 162 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ctl_s5 | 173.670 | 174.694 | 0.994x | 0.965-1.037x | 1.000x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | kernl | 173.670 | 159.539 | 1.089x | 1.053-1.118x | 1.123x | 0.94-1.01x | NO | yes | 0 | 6, 6 | 165, 165 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro_clamp | 173.670 | 129.843 | 1.338x | 1.305-1.373x | 1.400x | 0.83-1.37x | yes | yes | 0 | 6, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32 | 173.670 | 138.854 | 1.251x | 1.219-1.280x | 1.313x | 1.05-1.40x | yes | yes | 0 | 6, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 145.613 | 138.854 | 1.049x | 1.004-1.080x | 1.058x | 1.10-1.50x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 145.613 | 149.914 | 0.971x | 0.924-1.007x | - | 1.06-1.13x | NO | yes | 0 | 6, 6 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 138.650 | 149.914 | 0.925x | 0.909-0.941x | - | 0.57-1.00x | yes | yes | 0 | 6, 6 | 168, 166 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | tt32 | 173.670 | 145.613 | 1.193x | 1.137-1.265x | 1.241x | 0.90-0.99x | NO | yes | 0 | 6, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_32x64x32_w2_s5_cold | tt38 | 173.670 | 138.650 | 1.253x | 1.217-1.285x | - | 1.05-1.76x | yes | NO | 0.0156 | 6, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro | 212.537 | 164.864 | 1.289x | 1.286-1.295x | 1.285x | 1.39-1.55x | NO | yes | 0 | 6, 6 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ctl_s2 | 212.537 | 212.537 | 1.000x | 0.998-1.003x | 1.002x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ctl_s5 | 212.537 | 170.780 | 1.245x | 1.240-1.249x | 1.250x | 1.15-1.36x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | kernl | 212.537 | 227.214 | 0.935x | 0.933-0.937x | 0.944x | 0.88-0.97x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro_clamp | 212.537 | 185.116 | 1.148x | 1.145-1.151x | 1.158x | 1.41-1.68x | NO | yes | 0 | 6, 6 | 168, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32 | 212.537 | 175.787 | 1.209x | 1.206-1.213x | 1.220x | 1.02-1.21x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 187.278 | 175.787 | 1.065x | 1.062-1.070x | 1.067x | 0.85-1.09x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 187.278 | 164.864 | 1.136x | 1.132-1.142x | 1.124x | 1.16-1.39x | NO | yes | 0 | 6, 6 | 168, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 193.308 | 164.864 | 1.173x | 1.169-1.179x | 1.164x | 0.80-0.88x | NO | yes | 0 | 6, 6 | 212, 234 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | tt32 | 212.537 | 187.278 | 1.135x | 1.132-1.138x | 1.144x | 1.09-1.22x | yes | yes | 0 | 6, 6 | 168, 168 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_warm | tt38 | 212.537 | 193.308 | 1.099x | 1.096-1.103x | 1.105x | 1.63-1.86x | NO | NO | 0.0156 | 6, 6 | 168, 212 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro | 233.472 | 180.019 | 1.297x | 1.289-1.308x | 1.298x | 1.31-1.55x | NO | yes | 0 | 6, 6 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ctl_s2 | 233.472 | 233.882 | 0.998x | 0.994-1.008x | 0.996x | 0.97-1.03x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ctl_s5 | 233.472 | 185.139 | 1.261x | 1.253-1.272x | 1.272x | 1.24-1.46x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | kernl | 233.472 | 242.893 | 0.961x | 0.956-0.970x | 0.959x | 0.90-0.98x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro_clamp | 233.472 | 199.680 | 1.169x | 1.165-1.179x | 1.174x | 1.52-1.80x | NO | yes | 0 | 6, 6 | 168, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32 | 233.472 | 191.693 | 1.218x | 1.212-1.230x | 1.221x | 1.10-1.21x | NO | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 201.114 | 191.693 | 1.049x | 1.042-1.060x | 1.048x | 1.00-1.07x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 201.114 | 180.019 | 1.117x | 1.108-1.128x | 1.113x | 1.20-1.36x | NO | yes | 0 | 6, 6 | 168, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 208.282 | 180.019 | 1.157x | 1.147-1.168x | 1.155x | 0.67-0.90x | NO | yes | 0 | 6, 6 | 212, 234 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | tt32 | 233.472 | 201.114 | 1.161x | 1.152-1.172x | 1.166x | 1.05-1.18x | yes | yes | 0 | 6, 6 | 168, 168 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x32x32_w2_s2_cold | tt38 | 233.472 | 208.282 | 1.121x | 1.112-1.131x | 1.124x | 1.71-1.94x | NO | NO | 0.0156 | 6, 6 | 168, 212 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro | 173.824 | 139.648 | 1.245x | 1.239-1.247x | 1.252x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ctl_s2 | 173.824 | 251.392 | 0.691x | 0.690-0.693x | 0.688x | 0.71-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ctl_s5 | 173.824 | 173.568 | 1.001x | 0.997-1.004x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | kernl | 173.824 | 182.656 | 0.952x | 0.948-0.956x | 0.953x | 0.95-1.01x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_clamp | 173.824 | 138.752 | 1.253x | 1.249-1.256x | 1.259x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 173.824 | 139.392 | 1.247x | 1.243-1.251x | 1.252x | 1.10-1.54x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 179.456 | 139.392 | 1.287x | 1.282-1.297x | 1.288x | 1.11-1.55x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32 | 173.824 | 130.432 | 1.333x | 1.326-1.336x | 1.338x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 179.456 | 130.432 | 1.376x | 1.368-1.384x | 1.377x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 179.456 | 139.648 | 1.285x | 1.279-1.292x | 1.288x | 0.95-1.38x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 144.640 | 139.648 | 1.036x | 1.014-1.049x | 1.036x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | tt32 | 173.824 | 179.456 | 0.969x | 0.963-0.971x | 0.972x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_warm | tt38 | 173.824 | 144.640 | 1.202x | 1.186-1.225x | 1.208x | 1.00-1.44x | yes | NO | 0.0156 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro | 186.982 | 154.419 | 1.211x | 1.203-1.217x | 1.220x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ctl_s2 | 186.982 | 268.493 | 0.696x | 0.694-0.700x | 0.690x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ctl_s5 | 186.982 | 186.573 | 1.002x | 0.998-1.007x | 0.996x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | kernl | 186.982 | 193.741 | 0.965x | 0.959-0.971x | 0.967x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_clamp | 186.982 | 154.010 | 1.214x | 1.207-1.218x | 1.227x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 186.982 | 154.214 | 1.212x | 1.207-1.217x | 1.214x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 191.693 | 154.214 | 1.243x | 1.237-1.246x | 1.241x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32 | 186.982 | 145.613 | 1.284x | 1.278-1.289x | 1.292x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 191.693 | 145.613 | 1.316x | 1.310-1.320x | 1.320x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 191.693 | 154.419 | 1.241x | 1.234-1.246x | 1.246x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 147.046 | 154.419 | 0.952x | 0.947-0.956x | 0.952x | 0.68-0.98x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | tt32 | 186.982 | 191.693 | 0.975x | 0.972-0.980x | 0.979x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_64x128x32_w4_s4_cold | tt38 | 186.982 | 147.046 | 1.272x | 1.267-1.276x | 1.281x | 1.18-1.82x | yes | NO | 0.0156 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro | 360.448 | 321.536 | 1.121x | 1.092-1.167x | 1.138x | 0.97-1.25x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ctl_r64 | 360.448 | 360.789 | 0.999x | 0.960-1.027x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ctl_s2 | 360.448 | 361.472 | 0.997x | 0.966-1.033x | 0.989x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ctl_s5 | 360.448 | 328.021 | 1.099x | 1.067-1.142x | 1.120x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | kernl | 360.448 | 412.331 | 0.874x | 0.851-0.904x | 0.874x | 0.89-1.03x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_clamp | 360.448 | 377.173 | 0.956x | 0.925-0.994x | 0.940x | 0.79-1.09x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32 | 360.448 | 331.776 | 1.086x | 1.053-1.127x | 1.102x | 0.97-1.21x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 361.472 | 331.776 | 1.090x | 1.062-1.125x | 1.095x | 0.97-1.20x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 360.789 | 321.536 | 1.122x | 1.104-1.170x | 1.138x | 0.97-1.25x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 361.472 | 321.536 | 1.124x | 1.101-1.165x | 1.130x | 0.97-1.25x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 879.957 | 321.536 | 2.737x | 2.661-2.868x | 2.727x | 0.97-1.26x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | tt32 | 360.448 | 361.472 | 0.997x | 0.965-1.030x | 1.007x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_warm | tt38 | 360.448 | 879.957 | 0.410x | 0.392-0.426x | 0.417x | 0.88-1.17x | NO | NO | 0.00781 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro | 374.784 | 321.126 | 1.167x | 1.130-1.214x | 1.172x | 1.06-1.64x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ctl_r64 | 374.784 | 374.374 | 1.001x | 0.969-1.033x | 0.996x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ctl_s2 | 374.784 | 375.194 | 0.999x | 0.971-1.029x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ctl_s5 | 374.784 | 326.861 | 1.147x | 1.121-1.200x | - | 1.06-1.52x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | kernl | 374.784 | 416.563 | 0.900x | 0.877-0.931x | 0.903x | 0.91-1.00x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_clamp | 374.784 | 381.747 | 0.982x | 0.952-1.029x | 0.981x | 0.91-1.22x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32 | 374.784 | 332.186 | 1.128x | 1.098-1.172x | - | 1.06-1.61x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 367.002 | 332.186 | 1.105x | 1.073-1.147x | - | 1.06-1.60x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 374.374 | 321.126 | 1.166x | 1.130-1.212x | 1.178x | 1.06-1.64x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 367.002 | 321.126 | 1.143x | 1.103-1.188x | 1.131x | 1.06-1.63x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 888.832 | 321.126 | 2.768x | 2.643-2.880x | 2.799x | 0.97-1.30x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | tt32 | 374.784 | 367.002 | 1.021x | 0.988-1.059x | 1.036x | 0.97-1.04x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m128_n4096_k4096_16x16x64_w4_s2_cold | tt38 | 374.784 | 888.832 | 0.422x | 0.408-0.442x | 0.419x | 1.00-1.29x | NO | NO | 0.00781 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro | 29.519 | 27.412 | 1.077x | 1.076-1.083x | 1.100x | 1.40-1.69x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ctl_s2 | 29.519 | 33.536 | 0.880x | 0.879-0.885x | 0.875x | 0.73-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ctl_s5 | 29.519 | 29.519 | 1.000x | 0.994-1.007x | 1.002x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | kernl | 29.519 | 30.897 | 0.955x | 0.952-0.962x | 0.959x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro_clamp | 29.519 | 26.860 | 1.099x | 1.097-1.106x | 1.121x | 1.44-1.93x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32 | 29.519 | 28.573 | 1.033x | 1.032-1.039x | 1.045x | 1.04-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 32.039 | 28.573 | 1.121x | 1.120-1.123x | 1.126x | 0.88-1.13x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 32.039 | 27.412 | 1.169x | 1.168-1.170x | 1.185x | 1.18-1.51x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 31.567 | 27.412 | 1.152x | 1.152-1.153x | 1.161x | 0.71-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | tt32 | 29.519 | 32.039 | 0.921x | 0.920-0.927x | 0.929x | 1.09-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_warm | tt38 | 29.519 | 31.567 | 0.935x | 0.934-0.940x | 0.947x | 1.74-2.27x | NO | NO | 0.000244 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro | 46.490 | 35.635 | 1.305x | 1.278-1.326x | 1.385x | 1.44-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ctl_s2 | 46.490 | 58.778 | 0.791x | 0.781-0.800x | 0.983x | 0.68-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ctl_s5 | 46.490 | 46.490 | 1.000x | 0.987-1.009x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | kernl | 46.490 | 48.128 | 0.966x | 0.949-0.983x | 0.969x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro_clamp | 46.490 | 33.792 | 1.376x | 1.364-1.399x | 1.489x | 1.59-1.73x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32 | 46.490 | 40.960 | 1.135x | 1.114-1.146x | 1.176x | 1.15-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 46.694 | 40.960 | 1.140x | 1.114-1.176x | 1.161x | 1.04-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 46.694 | 35.635 | 1.310x | 1.278-1.360x | 1.368x | 1.31-1.46x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 37.274 | 35.635 | 1.046x | 1.028-1.064x | 1.050x | 0.50-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | tt32 | 46.490 | 46.694 | 0.996x | 0.962-1.013x | 1.012x | 1.07-1.18x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s5_cold | tt38 | 46.490 | 37.274 | 1.247x | 1.230-1.260x | 1.319x | 2.01-2.82x | NO | NO | 0.000244 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro | 28.566 | 25.706 | 1.111x | 1.106-1.117x | - | 0.78-1.09x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ctl_s2 | 28.566 | 27.842 | 1.026x | 1.022-1.030x | 1.031x | 0.67-0.80x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ctl_s5 | 28.566 | 28.584 | 0.999x | 0.994-1.004x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | kernl | 28.566 | 25.971 | 1.100x | 1.093-1.107x | 1.104x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro_clamp | 28.566 | 28.442 | 1.004x | 1.000-1.009x | 1.001x | 0.66-1.10x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32 | 28.566 | 24.329 | 1.174x | 1.169-1.180x | 1.196x | 1.04-1.42x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 26.801 | 24.329 | 1.102x | 1.097-1.106x | 1.105x | 1.15-1.50x | NO | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 26.801 | 25.706 | 1.043x | 1.038-1.048x | - | 0.86-1.15x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 28.601 | 25.706 | 1.113x | 1.109-1.119x | - | 0.66-0.82x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | tt32 | 28.566 | 26.801 | 1.066x | 1.061-1.071x | 1.082x | 0.88-0.98x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_warm | tt38 | 28.566 | 28.601 | 0.999x | 0.993-1.003x | - | 1.00-1.57x | yes | NO | 0.000244 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro | 42.394 | 38.093 | 1.113x | 1.096-1.141x | - | 0.98-1.07x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ctl_s2 | 42.394 | 52.224 | 0.812x | 0.798-0.824x | 0.777x | 0.62-0.74x | NO | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ctl_s5 | 42.394 | 42.394 | 1.000x | 0.986-1.029x | 1.011x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | kernl | 42.394 | 41.165 | 1.030x | 1.015-1.061x | 1.040x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro_clamp | 42.394 | 34.406 | 1.232x | 1.206-1.257x | 1.283x | 0.83-1.34x | yes | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32 | 42.394 | 35.635 | 1.190x | 1.165-1.221x | 1.215x | 1.24-1.37x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 39.322 | 35.635 | 1.103x | 1.085-1.128x | 1.109x | 1.29-1.47x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 39.322 | 38.093 | 1.032x | 1.021-1.054x | - | 1.06-1.12x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 35.021 | 38.093 | 0.919x | 0.909-0.935x | - | 0.48-0.82x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | tt32 | 42.394 | 39.322 | 1.078x | 1.057-1.099x | 1.096x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_32x64x32_w2_s5_cold | tt38 | 42.394 | 35.021 | 1.211x | 1.192-1.235x | - | 1.25-2.08x | NO | NO | 0.000244 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro | 33.625 | 28.526 | 1.179x | 1.176-1.182x | 1.197x | 1.37-1.51x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ctl_s2 | 33.625 | 33.667 | 0.999x | 0.998-1.002x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ctl_s5 | 33.625 | 29.738 | 1.131x | 1.129-1.135x | 1.143x | 1.15-1.34x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | kernl | 33.625 | 36.195 | 0.929x | 0.926-0.932x | 0.933x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro_clamp | 33.625 | 28.965 | 1.161x | 1.160-1.164x | 1.173x | 1.39-1.64x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32 | 33.625 | 30.992 | 1.085x | 1.084-1.089x | 1.071x | 1.02-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 31.263 | 30.992 | 1.009x | 1.007-1.012x | 0.988x | 0.86-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 31.263 | 28.526 | 1.096x | 1.093-1.098x | 1.104x | 1.15-1.37x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 31.953 | 28.526 | 1.120x | 1.117-1.122x | 1.119x | 0.81-0.89x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | tt32 | 33.625 | 31.263 | 1.076x | 1.073-1.079x | 1.084x | 1.08-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_warm | tt38 | 33.625 | 31.953 | 1.052x | 1.051-1.056x | 1.070x | 1.59-1.79x | NO | NO | 0.000244 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro | 58.778 | 43.622 | 1.347x | 1.336-1.358x | 1.095x | 1.29-1.53x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ctl_s2 | 58.778 | 58.573 | 1.003x | 0.993-1.011x | 1.003x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ctl_s5 | 58.778 | 46.490 | 1.264x | 1.249-1.274x | 1.008x | 1.23-1.44x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | kernl | 58.778 | 61.030 | 0.963x | 0.950-0.970x | 0.950x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro_clamp | 58.778 | 44.851 | 1.311x | 1.288-1.321x | 1.059x | 1.50-1.75x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32 | 58.778 | 50.176 | 1.171x | 1.163-1.180x | 0.935x | 1.09-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 53.043 | 50.176 | 1.057x | 1.049-1.066x | 1.059x | 0.99-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 53.043 | 43.622 | 1.216x | 1.206-1.226x | 1.241x | 1.19-1.35x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 46.899 | 43.622 | 1.075x | 1.056-1.090x | 1.096x | 0.68-0.91x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | tt32 | 58.778 | 53.043 | 1.108x | 1.100-1.116x | 0.882x | 1.05-1.17x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x32x32_w2_s2_cold | tt38 | 58.778 | 46.899 | 1.253x | 1.238-1.274x | 1.000x | 1.68-1.89x | NO | NO | 0.000244 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro | 31.878 | 31.098 | 1.025x | 1.024-1.027x | 1.026x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ctl_s2 | 31.878 | 36.441 | 0.875x | 0.874-0.876x | 0.880x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ctl_s5 | 31.878 | 31.944 | 0.998x | 0.997-0.999x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | kernl | 31.878 | 33.703 | 0.946x | 0.945-0.946x | 0.940x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_clamp | 31.878 | 28.405 | 1.122x | 1.121-1.124x | 1.116x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 31.878 | 28.583 | 1.115x | 1.114-1.118x | 1.118x | 1.09-1.49x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 32.078 | 28.583 | 1.122x | 1.121-1.125x | 1.117x | 1.10-1.51x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32 | 31.878 | 27.937 | 1.141x | 1.126-1.143x | 1.136x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 32.078 | 27.937 | 1.148x | 1.134-1.150x | 1.135x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 32.078 | 31.098 | 1.031x | 1.031-1.033x | 1.026x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.754 | 31.098 | 1.214x | 1.211-1.218x | 1.223x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | tt32 | 31.878 | 32.078 | 0.994x | 0.992-0.994x | 1.001x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_warm | tt38 | 31.878 | 37.754 | 0.844x | 0.841-0.847x | 0.840x | 1.00-1.41x | NO | NO | 0.000244 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro | 49.766 | 41.165 | 1.209x | 1.193-1.220x | 1.247x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ctl_s2 | 49.766 | 62.874 | 0.792x | 0.782-0.797x | 0.992x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ctl_s5 | 49.766 | 49.562 | 1.004x | 0.992-1.012x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | kernl | 49.766 | 51.814 | 0.960x | 0.949-0.968x | 0.953x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_clamp | 49.766 | 40.550 | 1.227x | 1.211-1.239x | 1.258x | 1.19-1.29x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 49.766 | 40.346 | 1.234x | 1.217-1.245x | 1.277x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 50.995 | 40.346 | 1.264x | 1.247-1.276x | 1.293x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32 | 49.766 | 37.683 | 1.321x | 1.303-1.333x | 1.369x | 1.26-1.45x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 50.995 | 37.683 | 1.353x | 1.335-1.366x | 1.386x | 1.27-1.46x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 50.995 | 41.165 | 1.239x | 1.223-1.250x | 1.262x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 43.008 | 41.165 | 1.045x | 1.035-1.055x | 1.051x | 0.70-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | tt32 | 49.766 | 50.995 | 0.976x | 0.964-0.988x | 0.988x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_64x128x32_w4_s4_cold | tt38 | 49.766 | 43.008 | 1.157x | 1.142-1.167x | 1.186x | 1.17-1.76x | NO | NO | 0.000244 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro | 50.972 | 44.715 | 1.140x | 1.123-1.158x | 1.148x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ctl_r64 | 50.972 | 50.916 | 1.001x | 0.986-1.016x | 0.993x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ctl_s2 | 50.972 | 50.916 | 1.001x | 0.987-1.015x | 1.005x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ctl_s5 | 50.972 | 51.428 | 0.991x | 0.976-1.009x | 0.985x | 0.98-1.23x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | kernl | 50.972 | 51.086 | 0.998x | 0.982-1.012x | 0.996x | 0.90-0.99x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_clamp | 50.972 | 46.592 | 1.094x | 1.078-1.111x | 1.080x | 0.98-1.40x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32 | 50.972 | 45.454 | 1.121x | 1.106-1.136x | 1.117x | 0.98-1.25x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 52.850 | 45.454 | 1.163x | 1.142-1.185x | 1.231x | 0.97-1.24x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 50.916 | 44.715 | 1.139x | 1.123-1.157x | 1.157x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 52.850 | 44.715 | 1.182x | 1.159-1.208x | 1.266x | 0.97-1.33x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 110.421 | 44.715 | 2.469x | 2.437-2.500x | 2.028x | 0.86-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | tt32 | 50.972 | 52.850 | 0.964x | 0.944-0.984x | 0.907x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_warm | tt38 | 50.972 | 110.421 | 0.462x | 0.456-0.468x | 0.566x | 0.98-1.50x | NO | NO | 0.000488 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro | 58.982 | 55.091 | 1.071x | 1.040-1.082x | 1.100x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ctl_r64 | 58.982 | 58.982 | 1.000x | 0.963-1.018x | 1.001x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ctl_s2 | 58.982 | 58.778 | 1.003x | 0.983-1.014x | 1.027x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ctl_s5 | 58.982 | 57.958 | 1.018x | 0.986-1.043x | - | 1.27-1.49x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | kernl | 58.982 | 57.549 | 1.025x | 1.004-1.036x | 1.028x | 0.91-1.00x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_clamp | 58.982 | 56.730 | 1.040x | 1.018-1.047x | 1.022x | 1.21-1.57x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32 | 58.982 | 52.224 | 1.129x | 1.084-1.138x | - | 1.23-1.57x | NO | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 69.018 | 52.224 | 1.322x | 1.266-1.343x | - | 1.22-1.57x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 58.982 | 55.091 | 1.071x | 1.036-1.109x | 1.099x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 69.018 | 55.091 | 1.253x | 1.215-1.277x | 1.278x | 1.23-1.59x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 115.917 | 55.091 | 2.104x | 2.044-2.127x | 1.752x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | tt32 | 58.982 | 69.018 | 0.855x | 0.836-0.868x | 0.861x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k1024_16x16x64_w4_s2_cold | tt38 | 58.982 | 115.917 | 0.509x | 0.502-0.516x | 0.628x | 1.32-1.66x | NO | NO | 0.000488 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro | 115.931 | 97.134 | 1.194x | 1.189-1.197x | 1.290x | 1.42-1.76x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ctl_s2 | 115.931 | 141.312 | 0.820x | 0.812-0.824x | 0.858x | 0.72-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ctl_s5 | 115.931 | 138.021 | 0.840x | 0.834-0.844x | 0.904x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | kernl | 115.931 | 117.102 | 0.990x | 0.981-0.997x | 1.060x | 0.89-0.97x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro_clamp | 115.931 | 94.866 | 1.222x | 1.217-1.227x | 1.324x | 1.47-2.04x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32 | 115.931 | 112.421 | 1.031x | 1.023-1.037x | 1.116x | 1.04-1.29x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 147.968 | 112.421 | 1.316x | 1.306-1.325x | 1.210x | 0.88-1.14x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 147.968 | 97.134 | 1.523x | 1.517-1.529x | 1.398x | 1.19-1.56x | yes | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 114.395 | 97.134 | 1.178x | 1.177-1.178x | 1.180x | 0.68-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | tt32 | 115.931 | 147.968 | 0.783x | 0.778-0.789x | 0.923x | 1.10-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_warm | tt38 | 115.931 | 114.395 | 1.013x | 1.010-1.017x | 1.093x | 1.79-2.46x | NO | NO | 0.0156 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro | 167.731 | 119.603 | 1.402x | 1.392-1.411x | 1.421x | 1.48-1.72x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ctl_s2 | 167.731 | 215.859 | 0.777x | 0.773-0.780x | 0.770x | 0.67-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ctl_s5 | 167.731 | 167.731 | 1.000x | 0.993-1.006x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | kernl | 167.731 | 174.490 | 0.961x | 0.956-0.970x | 0.958x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro_clamp | 167.731 | 109.363 | 1.534x | 1.522-1.549x | 1.557x | 1.64-1.77x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32 | 167.731 | 141.722 | 1.184x | 1.174-1.192x | 1.194x | 1.16-1.28x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 164.659 | 141.722 | 1.162x | 1.138-1.203x | 1.155x | 1.05-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 164.659 | 119.603 | 1.377x | 1.350-1.424x | 1.373x | 1.34-1.49x | yes | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 119.603 | 119.603 | 1.000x | 0.995-1.009x | 1.001x | 0.46-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | tt32 | 167.731 | 164.659 | 1.019x | 0.984-1.038x | 1.035x | 1.07-1.19x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s5_cold | tt38 | 167.731 | 119.603 | 1.402x | 1.390-1.408x | 1.419x | 2.09-3.09x | NO | NO | 0.0156 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro | 103.744 | 91.264 | 1.137x | 1.120-1.145x | - | 0.77-1.10x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ctl_s2 | 103.744 | 113.280 | 0.916x | 0.908-0.921x | 0.842x | 0.65-0.79x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ctl_s5 | 103.744 | 123.776 | 0.838x | 0.828-0.846x | 0.848x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | kernl | 103.744 | 92.544 | 1.121x | 1.110-1.132x | 1.118x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro_clamp | 103.744 | 101.376 | 1.023x | 1.016-1.030x | 1.045x | 0.65-1.10x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32 | 103.744 | 88.640 | 1.170x | 1.157-1.180x | 1.234x | 1.05-1.47x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 112.384 | 88.640 | 1.268x | 1.254-1.280x | 1.289x | 1.16-1.56x | yes | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 112.384 | 91.264 | 1.231x | 1.214-1.243x | - | 0.85-1.16x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 102.272 | 91.264 | 1.121x | 1.103-1.125x | - | 0.63-0.81x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | tt32 | 103.744 | 112.384 | 0.923x | 0.913-0.931x | 0.957x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_warm | tt38 | 103.744 | 102.272 | 1.014x | 1.008-1.025x | - | 1.00-1.65x | yes | NO | 0.0156 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro | 148.480 | 132.506 | 1.121x | 1.104-1.132x | - | 0.98-1.08x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ctl_s2 | 148.480 | 191.898 | 0.774x | 0.766-0.780x | 0.763x | 0.61-0.73x | NO | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ctl_s5 | 148.480 | 148.070 | 1.003x | 0.993-1.013x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | kernl | 148.480 | 140.493 | 1.057x | 1.045-1.067x | 1.065x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro_clamp | 148.480 | 106.906 | 1.389x | 1.379-1.399x | 1.401x | 0.83-1.37x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32 | 148.480 | 123.904 | 1.198x | 1.190-1.211x | 1.202x | 1.26-1.40x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 139.878 | 123.904 | 1.129x | 1.124-1.138x | 1.135x | 1.32-1.50x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 139.878 | 132.506 | 1.056x | 1.043-1.064x | - | 1.06-1.13x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 110.592 | 132.506 | 0.835x | 0.825-0.843x | - | 0.45-0.81x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | tt32 | 148.480 | 139.878 | 1.061x | 1.053-1.070x | 1.059x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_32x64x32_w2_s5_cold | tt38 | 148.480 | 110.592 | 1.343x | 1.328-1.353x | - | 1.27-2.23x | yes | NO | 0.0156 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro | 132.974 | 112.567 | 1.181x | 1.172-1.188x | 1.329x | 1.39-1.55x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ctl_s2 | 132.974 | 140.800 | 0.944x | 0.934-0.953x | 0.996x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ctl_s5 | 132.974 | 139.118 | 0.956x | 0.946-0.962x | 1.105x | 1.15-1.36x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | kernl | 132.974 | 143.360 | 0.928x | 0.919-0.937x | 1.117x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro_clamp | 132.974 | 129.755 | 1.025x | 1.017-1.030x | 1.183x | 1.41-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32 | 132.974 | 145.408 | 0.914x | 0.907-0.923x | 1.067x | 1.02-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 147.237 | 145.408 | 1.013x | 1.007-1.020x | 1.021x | 0.85-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 147.237 | 112.567 | 1.308x | 1.301-1.313x | 1.272x | 1.16-1.39x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 137.655 | 112.567 | 1.223x | 1.215-1.232x | 1.176x | 0.80-0.88x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | tt32 | 132.974 | 147.237 | 0.903x | 0.896-0.909x | 1.045x | 1.09-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_warm | tt38 | 132.974 | 137.655 | 0.966x | 0.955-0.974x | 1.130x | 1.63-1.86x | NO | NO | 0.0156 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro | 215.859 | 151.552 | 1.424x | 1.412-1.432x | 1.448x | 1.31-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ctl_s2 | 215.859 | 215.859 | 1.000x | 0.996-1.005x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ctl_s5 | 215.859 | 167.731 | 1.287x | 1.278-1.295x | 1.293x | 1.24-1.46x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | kernl | 215.859 | 226.509 | 0.953x | 0.947-0.957x | 0.952x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro_clamp | 215.859 | 156.262 | 1.381x | 1.368-1.391x | 1.394x | 1.52-1.80x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32 | 215.859 | 182.477 | 1.183x | 1.177-1.189x | 1.192x | 1.10-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 192.717 | 182.477 | 1.056x | 1.051-1.061x | 1.056x | 1.00-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 192.717 | 151.552 | 1.272x | 1.262-1.278x | 1.283x | 1.20-1.36x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 165.069 | 151.552 | 1.089x | 1.077-1.100x | 1.090x | 0.67-0.90x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | tt32 | 215.859 | 192.717 | 1.120x | 1.116-1.124x | 1.129x | 1.05-1.18x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x32x32_w2_s2_cold | tt38 | 215.859 | 165.069 | 1.308x | 1.296-1.318x | 1.328x | 1.71-1.94x | NO | NO | 0.0156 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro | 126.740 | 109.804 | 1.154x | 1.148-1.161x | 1.247x | 0.94-1.37x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ctl_s2 | 126.740 | 150.449 | 0.842x | 0.838-0.848x | 0.838x | 0.71-0.86x | yes | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ctl_s5 | 126.740 | 152.261 | 0.832x | 0.828-0.838x | 0.889x | 0.97-1.03x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | kernl | 126.740 | 131.466 | 0.964x | 0.954-0.979x | 1.010x | 0.95-1.01x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_clamp | 126.740 | 110.828 | 1.144x | 1.137-1.152x | 1.221x | 1.02-1.41x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 126.740 | 108.859 | 1.164x | 1.157-1.174x | 1.247x | 1.10-1.54x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 156.672 | 108.859 | 1.439x | 1.433-1.448x | 1.432x | 1.11-1.55x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32 | 126.740 | 102.479 | 1.237x | 1.228-1.247x | 1.331x | 1.08-1.56x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 156.672 | 102.479 | 1.529x | 1.522-1.538x | 1.528x | 1.10-1.57x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 156.672 | 109.804 | 1.427x | 1.423-1.432x | 1.432x | 0.95-1.38x | NO | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 138.634 | 109.804 | 1.263x | 1.259-1.263x | 1.269x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | tt32 | 126.740 | 156.672 | 0.809x | 0.803-0.815x | 0.871x | 0.96-1.02x | NO | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_warm | tt38 | 126.740 | 138.634 | 0.914x | 0.910-0.921x | 0.983x | 1.00-1.44x | NO | NO | 0.0156 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro | 176.947 | 141.312 | 1.252x | 1.244-1.261x | 1.262x | 1.11-1.30x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ctl_s2 | 176.947 | 236.954 | 0.747x | 0.744-0.750x | 0.739x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ctl_s5 | 176.947 | 176.947 | 1.000x | 0.994-1.005x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | kernl | 176.947 | 185.549 | 0.954x | 0.948-0.959x | 0.954x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_clamp | 176.947 | 140.698 | 1.258x | 1.248-1.264x | 1.270x | 1.20-1.31x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 176.947 | 141.312 | 1.252x | 1.242-1.261x | 1.263x | 1.29-1.39x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 183.091 | 141.312 | 1.296x | 1.287-1.307x | 1.303x | 1.31-1.40x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32 | 176.947 | 130.458 | 1.356x | 1.347-1.364x | 1.366x | 1.27-1.48x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 183.091 | 130.458 | 1.403x | 1.396-1.414x | 1.410x | 1.29-1.50x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 183.091 | 141.312 | 1.296x | 1.289-1.307x | 1.302x | 1.12-1.31x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 144.384 | 141.312 | 1.022x | 1.017-1.028x | 1.023x | 0.68-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | tt32 | 176.947 | 183.091 | 0.966x | 0.959-0.971x | 0.969x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_64x128x32_w4_s4_cold | tt38 | 176.947 | 144.384 | 1.226x | 1.220-1.230x | 1.233x | 1.18-1.82x | yes | NO | 0.0156 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro | 191.488 | 164.659 | 1.163x | 1.135-1.193x | 1.163x | 0.98-1.36x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ctl_r64 | 191.488 | 192.717 | 0.994x | 0.961-1.019x | 1.010x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ctl_s2 | 191.488 | 192.512 | 0.995x | 0.972-1.025x | 1.004x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ctl_s5 | 191.488 | 186.778 | 1.025x | 0.998-1.057x | 1.026x | 0.98-1.24x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | kernl | 191.488 | 189.645 | 1.010x | 0.991-1.026x | 1.015x | 0.89-0.98x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_clamp | 191.488 | 183.091 | 1.046x | 1.024-1.076x | 1.080x | 0.98-1.43x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32 | 191.488 | 173.670 | 1.103x | 1.079-1.129x | 1.121x | 0.98-1.26x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 210.125 | 173.670 | 1.210x | 1.194-1.241x | 1.196x | 0.97-1.25x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 192.717 | 164.659 | 1.170x | 1.141-1.210x | 1.152x | 0.98-1.36x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 210.125 | 164.659 | 1.276x | 1.256-1.311x | 1.241x | 0.97-1.35x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 430.080 | 164.659 | 2.612x | 2.579-2.674x | 2.530x | 0.85-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | tt32 | 191.488 | 210.125 | 0.911x | 0.888-0.927x | 0.938x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_warm | tt38 | 191.488 | 430.080 | 0.445x | 0.435-0.451x | 0.460x | 0.98-1.54x | NO | NO | 0.000977 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro | 223.437 | 198.861 | 1.124x | 1.074-1.149x | 1.108x | 1.25-1.63x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ctl_r64 | 223.437 | 222.413 | 1.005x | 0.936-1.042x | 0.955x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ctl_s2 | 223.437 | 220.570 | 1.013x | 0.950-1.052x | 1.006x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ctl_s5 | 223.437 | 199.066 | 1.122x | 1.065-1.155x | - | 1.28-1.51x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | kernl | 223.437 | 199.680 | 1.119x | 1.072-1.147x | 1.078x | 0.91-1.00x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_clamp | 223.437 | 194.970 | 1.146x | 1.098-1.176x | 1.126x | 1.22-1.60x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32 | 223.437 | 191.488 | 1.167x | 1.115-1.197x | - | 1.24-1.61x | NO | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 239.002 | 191.488 | 1.248x | 1.225-1.274x | - | 1.23-1.60x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 222.413 | 198.861 | 1.118x | 1.084-1.166x | 1.160x | 1.25-1.63x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 239.002 | 198.861 | 1.202x | 1.180-1.222x | 1.203x | 1.24-1.62x | NO | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 434.790 | 198.861 | 2.186x | 2.137-2.216x | 2.200x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | tt32 | 223.437 | 239.002 | 0.935x | 0.893-0.958x | 0.921x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n1024_k4096_16x16x64_w4_s2_cold | tt38 | 223.437 | 434.790 | 0.514x | 0.493-0.529x | 0.504x | 1.34-1.70x | NO | NO | 0.000977 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro | 49.380 | 59.999 | 0.823x | 0.814-0.836x | 0.836x | 0.71-1.03x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ctl_s2 | 49.380 | 51.503 | 0.959x | 0.947-0.969x | 1.100x | 0.73-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ctl_s5 | 49.380 | 49.493 | 0.998x | 0.986-1.009x | 1.002x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | kernl | 49.380 | 50.745 | 0.973x | 0.963-0.984x | 1.000x | 0.89-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro_clamp | 49.380 | 60.757 | 0.813x | 0.805-0.825x | 0.847x | 0.73-1.05x | yes | yes | 0 | 10, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32 | 49.380 | 69.897 | 0.706x | 0.698-0.714x | 0.714x | 0.52-0.94x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 73.045 | 69.897 | 1.045x | 1.033-1.056x | 1.033x | 0.88-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 73.045 | 59.999 | 1.217x | 1.206-1.236x | 1.210x | 1.19-1.54x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 66.560 | 59.999 | 1.109x | 1.097-1.127x | 1.099x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | tt32 | 49.380 | 73.045 | 0.676x | 0.668-0.683x | 0.691x | 0.56-0.85x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_warm | tt38 | 49.380 | 66.560 | 0.742x | 0.733-0.750x | 0.761x | 0.90-1.14x | NO | NO | 0.00195 | 10, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro | 61.030 | 75.366 | 0.810x | 0.803-0.824x | 0.623x | 0.74-0.90x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ctl_s2 | 61.030 | 75.571 | 0.808x | 0.796-0.822x | 0.792x | 0.68-0.83x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ctl_s5 | 61.030 | 61.235 | 0.997x | 0.983-1.010x | 1.000x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | kernl | 61.030 | 62.669 | 0.974x | 0.967-0.990x | 0.971x | 0.90-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro_clamp | 61.030 | 73.114 | 0.835x | 0.818-0.852x | 0.666x | 0.82-0.99x | yes | yes | 0 | 10, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32 | 61.030 | 78.848 | 0.774x | 0.760-0.796x | 0.588x | 0.58-0.72x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 79.872 | 78.848 | 1.013x | 0.992-1.040x | 0.997x | 1.05-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 79.872 | 75.366 | 1.060x | 1.049-1.077x | 1.056x | 1.33-1.48x | NO | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 70.246 | 75.366 | 0.932x | 0.924-0.945x | 0.928x | 0.53-0.90x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | tt32 | 61.030 | 79.872 | 0.764x | 0.758-0.773x | 0.590x | 0.54-0.67x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s5_cold | tt38 | 61.030 | 70.246 | 0.869x | 0.863-0.877x | 0.672x | 0.97-1.41x | NO | NO | 0.00195 | 10, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro | 65.218 | 62.393 | 1.045x | 1.030-1.065x | - | 0.77-1.09x | yes | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ctl_s2 | 65.218 | 51.483 | 1.267x | 1.247-1.286x | 1.559x | 0.97-1.50x | yes | yes | 0 | 8, 10 | 165, 162 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ctl_s5 | 65.218 | 65.430 | 0.997x | 0.984-1.012x | 0.999x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | kernl | 65.218 | 66.207 | 0.985x | 0.970-0.998x | 0.999x | 0.94-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro_clamp | 65.218 | 65.324 | 0.998x | 0.983-1.017x | 1.009x | 0.65-1.10x | yes | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32 | 65.218 | 55.367 | 1.178x | 1.158-1.192x | 1.224x | 0.97-1.29x | yes | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 55.826 | 55.367 | 1.008x | 0.993-1.019x | 1.018x | 0.97-1.37x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 55.826 | 62.393 | 0.895x | 0.883-0.910x | - | 0.85-1.16x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 66.701 | 62.393 | 1.069x | 1.057-1.087x | - | 0.75-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | tt32 | 65.218 | 55.826 | 1.168x | 1.152-1.184x | 1.202x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_warm | tt38 | 65.218 | 66.701 | 0.978x | 0.965-0.990x | 1.007x | 0.97-1.29x | yes | NO | 0.00195 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro | 84.173 | 79.872 | 1.054x | 1.043-1.064x | - | 0.98-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ctl_s2 | 84.173 | 70.246 | 1.198x | 1.179-1.211x | 1.547x | 1.05-1.41x | yes | yes | 0 | 8, 10 | 165, 162 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ctl_s5 | 84.173 | 83.968 | 1.002x | 0.993-1.015x | 1.005x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | kernl | 84.173 | 85.606 | 0.983x | 0.969-0.993x | 0.973x | 0.94-1.01x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro_clamp | 84.173 | 77.210 | 1.090x | 1.082-1.110x | 1.101x | 0.83-1.36x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32 | 84.173 | 64.717 | 1.301x | 1.282-1.311x | 1.331x | 1.05-1.39x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 64.717 | 64.717 | 1.000x | 0.981-1.019x | 0.999x | 1.10-1.49x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 64.717 | 79.872 | 0.810x | 0.798-0.827x | - | 1.06-1.12x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 70.246 | 79.872 | 0.879x | 0.870-0.894x | - | 0.58-1.00x | yes | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | tt32 | 84.173 | 64.717 | 1.301x | 1.274-1.319x | 1.332x | 0.90-0.99x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_32x64x32_w2_s5_cold | tt38 | 84.173 | 70.246 | 1.198x | 1.179-1.211x | - | 1.05-1.74x | yes | NO | 0.00195 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro | 51.334 | 66.337 | 0.774x | 0.756-0.787x | 0.623x | 0.69-0.86x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ctl_s2 | 51.334 | 52.090 | 0.985x | 0.966-0.999x | 0.976x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ctl_s5 | 51.334 | 49.286 | 1.042x | 1.023-1.058x | 0.894x | 0.97-1.34x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | kernl | 51.334 | 54.539 | 0.941x | 0.924-0.955x | 0.933x | 0.88-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro_clamp | 51.334 | 71.769 | 0.715x | 0.701-0.726x | 0.582x | 0.70-0.93x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32 | 51.334 | 50.710 | 1.012x | 0.995-1.030x | 0.879x | 0.97-1.20x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 54.094 | 50.710 | 1.067x | 1.051-1.089x | 0.893x | 0.86-1.09x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 54.094 | 66.337 | 0.815x | 0.799-0.831x | 0.633x | 0.58-0.86x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 84.369 | 66.337 | 1.272x | 1.244-1.311x | 1.268x | 0.80-0.89x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | tt32 | 51.334 | 54.094 | 0.949x | 0.930-0.963x | 0.984x | 0.97-1.21x | NO | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_warm | tt38 | 51.334 | 84.369 | 0.608x | 0.590-0.619x | 0.491x | 0.81-1.02x | NO | NO | 0.00195 | 10, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro | 75.571 | 93.184 | 0.811x | 0.792-0.830x | 0.789x | 0.65-0.80x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ctl_s2 | 75.571 | 75.981 | 0.995x | 0.973-1.027x | 0.996x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ctl_s5 | 75.571 | 61.030 | 1.238x | 1.213-1.267x | 1.257x | 1.22-1.44x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | kernl | 75.571 | 82.944 | 0.911x | 0.890-0.938x | 0.893x | 0.90-0.98x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro_clamp | 75.571 | 96.666 | 0.782x | 0.754-0.808x | 0.785x | 0.75-0.93x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32 | 75.571 | 66.560 | 1.135x | 1.113-1.161x | 1.144x | 1.09-1.20x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 71.066 | 66.560 | 1.068x | 1.049-1.087x | 1.072x | 0.99-1.07x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 71.066 | 93.184 | 0.763x | 0.746-0.777x | 0.739x | 0.60-0.70x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 108.339 | 93.184 | 1.163x | 1.137-1.175x | 1.175x | 0.67-0.91x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | tt32 | 75.571 | 71.066 | 1.063x | 1.040-1.090x | 1.068x | 1.05-1.17x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x32x32_w2_s2_cold | tt38 | 75.571 | 108.339 | 0.698x | 0.687-0.716x | 0.671x | 0.85-1.00x | NO | NO | 0.00195 | 10, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro | 47.470 | 50.871 | 0.933x | 0.923-0.948x | 0.968x | 0.94-1.03x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ctl_s2 | 47.470 | 51.054 | 0.930x | 0.919-0.942x | 1.181x | 0.75-0.86x | NO | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ctl_s5 | 47.470 | 47.945 | 0.990x | 0.977-1.003x | 0.992x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | kernl | 47.470 | 47.909 | 0.991x | 0.980-1.007x | 1.021x | 0.95-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_clamp | 47.470 | 46.373 | 1.024x | 1.011-1.037x | 1.062x | 0.97-1.08x | yes | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 47.470 | 42.386 | 1.120x | 1.108-1.138x | 1.163x | 0.97-1.15x | yes | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 48.128 | 42.386 | 1.135x | 1.121-1.158x | 1.144x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32 | 47.470 | 43.849 | 1.083x | 1.069-1.099x | 1.132x | 0.97-1.14x | yes | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 48.128 | 43.849 | 1.098x | 1.082-1.118x | 1.114x | 0.97-1.15x | yes | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 48.128 | 50.871 | 0.946x | 0.934-0.964x | 0.952x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 69.376 | 50.871 | 1.364x | 1.346-1.384x | 1.074x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | tt32 | 47.470 | 48.128 | 0.986x | 0.971-1.000x | 1.016x | 0.96-1.03x | yes | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_warm | tt38 | 47.470 | 69.376 | 0.684x | 0.676-0.694x | 0.901x | 0.97-1.06x | NO | NO | 0.00195 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro | 61.645 | 56.115 | 1.099x | 1.079-1.118x | 0.881x | 1.10-1.24x | NO | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ctl_s2 | 61.645 | 78.848 | 0.782x | 0.775-0.792x | 0.769x | 0.67-0.81x | yes | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ctl_s5 | 61.645 | 61.850 | 0.997x | 0.984-1.017x | 0.993x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | kernl | 61.645 | 62.874 | 0.980x | 0.968-0.993x | 0.976x | 0.95-1.02x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_clamp | 61.645 | 57.344 | 1.075x | 1.060-1.097x | 1.078x | 1.18-1.25x | NO | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 61.645 | 56.730 | 1.087x | 1.076-1.105x | 1.088x | 1.18-1.34x | NO | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 60.416 | 56.730 | 1.065x | 1.050-1.080x | 1.063x | 1.18-1.35x | NO | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32 | 61.645 | 51.610 | 1.194x | 1.182-1.216x | 0.959x | 1.18-1.32x | yes | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 60.416 | 51.610 | 1.171x | 1.154-1.188x | 0.937x | 1.18-1.33x | NO | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 60.416 | 56.115 | 1.077x | 1.054-1.092x | 0.860x | 1.12-1.24x | NO | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 69.632 | 56.115 | 1.241x | 1.227-1.257x | 0.997x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | tt32 | 61.645 | 60.416 | 1.020x | 1.007-1.041x | 1.023x | 0.96-1.02x | yes | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_64x128x32_w4_s4_cold | tt38 | 61.645 | 69.632 | 0.885x | 0.874-0.894x | 0.884x | 1.17-1.24x | NO | NO | 0.00195 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro | 159.539 | 160.154 | 0.996x | 0.980-1.015x | 0.987x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ctl_r64 | 159.539 | 160.768 | 0.992x | 0.982-1.015x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ctl_s2 | 159.539 | 160.768 | 0.992x | 0.984-1.017x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ctl_s5 | 159.539 | 161.997 | 0.985x | 0.972-1.010x | 0.996x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | kernl | 159.539 | 159.744 | 0.999x | 0.981-1.015x | 1.000x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_clamp | 159.539 | 165.478 | 0.964x | 0.946-0.979x | 0.943x | 0.75-1.04x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32 | 159.539 | 162.406 | 0.982x | 0.964-0.997x | 0.985x | 0.97-1.13x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 165.888 | 162.406 | 1.021x | 1.002-1.037x | 1.034x | 0.97-1.34x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 160.768 | 160.154 | 1.004x | 0.981-1.017x | 0.987x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 165.888 | 160.154 | 1.036x | 1.019-1.055x | 1.036x | 0.97-1.24x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 431.514 | 160.154 | 2.694x | 2.632-2.718x | 2.088x | 0.97-1.26x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | tt32 | 159.539 | 165.888 | 0.962x | 0.946-0.978x | 0.953x | 0.81-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_warm | tt38 | 159.539 | 431.514 | 0.370x | 0.367-0.378x | 0.473x | 0.73-1.03x | NO | NO | 0.00195 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro | 170.394 | 166.093 | 1.026x | 0.965-1.091x | 1.020x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ctl_r64 | 170.394 | 170.394 | 1.000x | 0.940-1.060x | 0.997x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ctl_s2 | 170.394 | 169.984 | 1.002x | 0.942-1.062x | 1.003x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ctl_s5 | 170.394 | 165.888 | 1.027x | 0.967-1.092x | - | 0.97-1.49x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | kernl | 170.394 | 168.755 | 1.010x | 0.952-1.074x | 1.008x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_clamp | 170.394 | 176.947 | 0.963x | 0.906-1.024x | 0.947x | 0.87-1.16x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32 | 170.394 | 164.659 | 1.035x | 0.977-1.105x | - | 0.97-1.49x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 174.694 | 164.659 | 1.061x | 1.002-1.138x | - | 1.05-1.77x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 170.394 | 166.093 | 1.026x | 0.966-1.093x | 1.023x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 174.694 | 166.093 | 1.052x | 0.990-1.123x | 1.052x | 1.05-1.62x | NO | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 429.056 | 166.093 | 2.583x | 2.413-2.743x | 2.065x | 0.97-1.30x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | tt32 | 170.394 | 174.694 | 0.975x | 0.915-1.034x | 0.970x | 0.81-0.95x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k1024_16x16x64_w4_s2_cold | tt38 | 170.394 | 429.056 | 0.397x | 0.375-0.424x | 0.494x | 0.83-1.08x | NO | NO | 0.00195 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro | 200.576 | 253.696 | 0.791x | 0.781-0.802x | 0.790x | 0.70-1.03x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ctl_s2 | 200.576 | 248.576 | 0.807x | 0.798-0.818x | 0.811x | 0.72-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ctl_s5 | 200.576 | 200.704 | 0.999x | 0.985-1.013x | 1.006x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | kernl | 200.576 | 200.320 | 1.001x | 0.990-1.013x | 1.006x | 0.89-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro_clamp | 200.576 | 212.096 | 0.946x | 0.936-0.959x | 0.942x | 0.73-1.05x | yes | yes | 0 | 10, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32 | 200.576 | 286.080 | 0.701x | 0.693-0.715x | 0.697x | 0.51-0.93x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 294.400 | 286.080 | 1.029x | 1.017-1.050x | 1.025x | 0.87-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 294.400 | 253.696 | 1.160x | 1.146-1.177x | 1.162x | 1.20-1.57x | NO | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 256.896 | 253.696 | 1.013x | 1.003-1.026x | 1.006x | 0.76-1.03x | yes | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | tt32 | 200.576 | 294.400 | 0.681x | 0.671-0.691x | 0.680x | 0.54-0.84x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_warm | tt38 | 200.576 | 256.896 | 0.781x | 0.770-0.790x | 0.785x | 0.89-1.15x | NO | NO | 0.0156 | 10, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro | 202.342 | 257.638 | 0.785x | 0.749-0.816x | 0.786x | 0.73-0.89x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ctl_s2 | 202.342 | 254.976 | 0.794x | 0.756-0.822x | 0.793x | 0.67-0.82x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ctl_s5 | 202.342 | 202.752 | 0.998x | 0.952-1.041x | 1.014x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | kernl | 202.342 | 204.390 | 0.990x | 0.940-1.028x | 0.991x | 0.90-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro_clamp | 202.342 | 225.485 | 0.897x | 0.849-0.918x | 0.876x | 0.81-0.99x | yes | yes | 0 | 10, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32 | 202.342 | 284.262 | 0.712x | 0.675-0.741x | 0.700x | 0.57-0.71x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 288.973 | 284.262 | 1.017x | 0.968-1.058x | 0.999x | 1.05-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 288.973 | 257.638 | 1.122x | 1.074-1.164x | 1.123x | 1.34-1.49x | NO | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 252.723 | 257.638 | 0.981x | 0.935-1.019x | 0.976x | 0.51-0.89x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | tt32 | 202.342 | 288.973 | 0.700x | 0.669-0.730x | 0.700x | 0.53-0.66x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s5_cold | tt38 | 202.342 | 252.723 | 0.801x | 0.764-0.839x | 0.805x | 0.97-1.43x | NO | NO | 0.0156 | 10, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro | 282.331 | 265.655 | 1.063x | 1.049-1.084x | 1.044x | 0.77-1.10x | yes | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ctl_s2 | 282.331 | 226.597 | 1.246x | 1.228-1.267x | 1.253x | 0.97-1.53x | yes | yes | 0 | 8, 10 | 165, 162 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ctl_s5 | 282.331 | 283.209 | 0.997x | 0.983-1.019x | 0.998x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | kernl | 282.331 | 317.733 | 0.889x | 0.873-0.911x | 0.884x | 0.93-1.03x | NO | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro_clamp | 282.331 | 259.072 | 1.090x | 1.073-1.108x | 1.085x | 0.65-1.10x | yes | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32 | 282.331 | 213.138 | 1.325x | 1.303-1.344x | 1.345x | 0.97-1.31x | NO | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 213.723 | 213.138 | 1.003x | 0.989-1.016x | 1.003x | 0.97-1.39x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 213.723 | 265.655 | 0.805x | 0.796-0.820x | 0.779x | 0.85-1.17x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 248.832 | 265.655 | 0.937x | 0.927-0.955x | 0.908x | 0.75-1.03x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | tt32 | 282.331 | 213.723 | 1.321x | 1.299-1.342x | 1.341x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_warm | tt38 | 282.331 | 248.832 | 1.135x | 1.116-1.153x | 1.150x | 0.97-1.31x | yes | NO | 0.0156 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro | 289.792 | 270.746 | 1.070x | 1.032-1.108x | - | 0.98-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ctl_s2 | 289.792 | 231.834 | 1.250x | 1.216-1.296x | 1.270x | 1.05-1.42x | yes | yes | 0 | 8, 10 | 165, 162 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ctl_s5 | 289.792 | 289.997 | 0.999x | 0.964-1.025x | 0.998x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | kernl | 289.792 | 321.536 | 0.901x | 0.868-0.922x | 0.896x | 0.94-1.01x | NO | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro_clamp | 289.792 | 262.963 | 1.102x | 1.069-1.144x | 1.100x | 0.83-1.38x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32 | 289.792 | 220.570 | 1.314x | 1.279-1.372x | 1.330x | 1.05-1.40x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 218.317 | 220.570 | 0.990x | 0.948-1.030x | 0.988x | 1.10-1.51x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 218.317 | 270.746 | 0.806x | 0.765-0.832x | - | 1.06-1.13x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 245.965 | 270.746 | 0.908x | 0.860-0.938x | - | 0.57-1.00x | yes | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | tt32 | 289.792 | 218.317 | 1.327x | 1.294-1.389x | 1.345x | 0.90-0.99x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_32x64x32_w2_s5_cold | tt38 | 289.792 | 245.965 | 1.178x | 1.148-1.235x | - | 1.05-1.78x | yes | NO | 0.0156 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro | 241.323 | 323.925 | 0.745x | 0.724-0.760x | 0.737x | 0.68-0.85x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ctl_s2 | 241.323 | 241.152 | 1.001x | 0.982-1.019x | 0.999x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ctl_s5 | 241.323 | 193.365 | 1.248x | 1.225-1.272x | 1.249x | 0.97-1.36x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | kernl | 241.323 | 252.757 | 0.955x | 0.939-0.964x | 0.949x | 0.88-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro_clamp | 241.323 | 346.453 | 0.697x | 0.672-0.716x | 0.677x | 0.70-0.93x | NO | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32 | 241.323 | 218.624 | 1.104x | 1.087-1.119x | 1.101x | 0.97-1.21x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 246.101 | 218.624 | 1.126x | 1.114-1.143x | 1.134x | 0.85-1.09x | NO | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 246.101 | 323.925 | 0.760x | 0.742-0.777x | 0.759x | 0.57-0.85x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 384.171 | 323.925 | 1.186x | 1.148-1.236x | 1.210x | 0.80-0.88x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | tt32 | 241.323 | 246.101 | 0.981x | 0.961-0.994x | 0.971x | 0.97-1.22x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_warm | tt38 | 241.323 | 384.171 | 0.628x | 0.604-0.642x | 0.610x | 0.81-1.02x | NO | NO | 0.0156 | 10, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro | 249.037 | 326.246 | 0.763x | 0.745-0.779x | 0.763x | 0.64-0.80x | yes | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ctl_s2 | 249.037 | 249.037 | 1.000x | 0.981-1.018x | 1.003x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ctl_s5 | 249.037 | 197.837 | 1.259x | 1.240-1.290x | 1.276x | 1.23-1.46x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | kernl | 249.037 | 262.349 | 0.949x | 0.933-0.970x | 0.953x | 0.90-0.98x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro_clamp | 249.037 | 347.546 | 0.717x | 0.698-0.730x | 0.714x | 0.75-0.92x | NO | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32 | 249.037 | 223.642 | 1.114x | 1.098-1.138x | 1.124x | 1.10-1.21x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 249.037 | 223.642 | 1.114x | 1.090-1.139x | 1.125x | 1.00-1.07x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 249.037 | 326.246 | 0.763x | 0.740-0.779x | 0.764x | 0.59-0.70x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 387.277 | 326.246 | 1.187x | 1.142-1.224x | 1.186x | 0.67-0.90x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | tt32 | 249.037 | 249.037 | 1.000x | 0.984-1.023x | 0.999x | 1.05-1.18x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x32x32_w2_s2_cold | tt38 | 249.037 | 387.277 | 0.643x | 0.627-0.663x | 0.643x | 0.85-1.00x | NO | NO | 0.0156 | 10, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro | 202.866 | 176.469 | 1.150x | 1.139-1.169x | 1.145x | 0.94-1.03x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ctl_s2 | 202.866 | 253.838 | 0.799x | 0.791-0.812x | 0.797x | 0.74-0.86x | yes | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ctl_s5 | 202.866 | 202.980 | 0.999x | 0.991-1.016x | 1.001x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | kernl | 202.866 | 192.740 | 1.053x | 1.042-1.068x | 1.054x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_clamp | 202.866 | 167.367 | 1.212x | 1.201-1.227x | 1.210x | 0.97-1.08x | NO | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 202.866 | 163.726 | 1.239x | 1.228-1.255x | 1.247x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 197.632 | 163.726 | 1.207x | 1.197-1.231x | 1.208x | 0.97-1.17x | NO | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32 | 202.866 | 165.205 | 1.228x | 1.209-1.286x | 1.236x | 0.97-1.14x | NO | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 197.632 | 165.205 | 1.196x | 1.178-1.261x | 1.197x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 197.632 | 176.469 | 1.120x | 1.110-1.146x | 1.109x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 268.402 | 176.469 | 1.521x | 1.454-1.553x | 1.505x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | tt32 | 202.866 | 197.632 | 1.026x | 1.006-1.040x | 1.032x | 0.96-1.03x | yes | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_warm | tt38 | 202.866 | 268.402 | 0.756x | 0.742-0.794x | 0.761x | 0.97-1.06x | NO | NO | 0.0156 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro | 203.162 | 177.766 | 1.143x | 1.106-1.179x | 1.147x | 1.11-1.25x | yes | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ctl_s2 | 203.162 | 264.806 | 0.767x | 0.744-0.792x | 0.762x | 0.66-0.80x | yes | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ctl_s5 | 203.162 | 202.547 | 1.003x | 0.969-1.030x | 1.001x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | kernl | 203.162 | 198.656 | 1.023x | 0.989-1.051x | 1.021x | 0.95-1.02x | NO | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_clamp | 203.162 | 173.466 | 1.171x | 1.135-1.197x | 1.181x | 1.19-1.26x | NO | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 203.162 | 171.213 | 1.187x | 1.149-1.219x | 1.187x | 1.19-1.35x | NO | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 203.162 | 171.213 | 1.187x | 1.156-1.231x | 1.180x | 1.20-1.37x | NO | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32 | 203.162 | 162.611 | 1.249x | 1.210-1.287x | 1.263x | 1.19-1.33x | yes | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 203.162 | 162.611 | 1.249x | 1.217-1.300x | 1.256x | 1.20-1.35x | yes | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 203.162 | 177.766 | 1.143x | 1.112-1.191x | 1.140x | 1.12-1.26x | yes | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 245.146 | 177.766 | 1.379x | 1.328-1.421x | 1.383x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | tt32 | 203.162 | 203.162 | 1.000x | 0.958-1.027x | 1.006x | 0.96-1.02x | yes | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_64x128x32_w4_s4_cold | tt38 | 203.162 | 245.146 | 0.829x | 0.803-0.860x | 0.829x | 1.18-1.25x | NO | NO | 0.0156 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro | 660.821 | 648.533 | 1.019x | 0.983-1.056x | 1.021x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ctl_r64 | 660.821 | 661.845 | 0.998x | 0.964-1.035x | 0.995x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ctl_s2 | 660.821 | 661.504 | 0.999x | 0.963-1.042x | 0.995x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ctl_s5 | 660.821 | 629.419 | 1.050x | 1.012-1.094x | 1.052x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | kernl | 660.821 | 707.584 | 0.934x | 0.907-0.960x | 0.929x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_clamp | 660.821 | 715.435 | 0.924x | 0.892-0.959x | 0.913x | 0.75-1.04x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32 | 660.821 | 649.557 | 1.017x | 0.973-1.049x | 1.017x | 0.97-1.14x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 695.296 | 649.557 | 1.070x | 1.028-1.104x | 1.064x | 0.97-1.34x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 661.845 | 648.533 | 1.021x | 0.988-1.053x | 1.026x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 695.296 | 648.533 | 1.072x | 1.039-1.111x | 1.069x | 0.97-1.25x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 1792.341 | 648.533 | 2.764x | 2.698-2.888x | 2.741x | 0.97-1.26x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | tt32 | 660.821 | 695.296 | 0.950x | 0.913-0.984x | 0.956x | 0.81-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_warm | tt38 | 660.821 | 1792.341 | 0.369x | 0.351-0.379x | 0.373x | 0.73-1.03x | NO | NO | 0.00781 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro | 667.648 | 647.373 | 1.031x | 0.995-1.067x | 1.028x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ctl_r64 | 667.648 | 664.781 | 1.004x | 0.974-1.050x | 1.001x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ctl_s2 | 667.648 | 665.600 | 1.003x | 0.967-1.059x | 1.005x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ctl_s5 | 667.648 | 627.917 | 1.063x | 1.026-1.099x | - | 0.97-1.50x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | kernl | 667.648 | 708.608 | 0.942x | 0.908-0.977x | 0.935x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_clamp | 667.648 | 715.776 | 0.933x | 0.892-0.981x | 0.931x | 0.87-1.16x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32 | 667.648 | 644.710 | 1.036x | 0.990-1.068x | - | 0.97-1.50x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 695.501 | 644.710 | 1.079x | 1.045-1.118x | - | 1.06-1.79x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 664.781 | 647.373 | 1.027x | 0.980-1.060x | 1.027x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 695.501 | 647.373 | 1.074x | 1.050-1.117x | 1.068x | 1.06-1.63x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 1779.917 | 647.373 | 2.749x | 2.677-2.864x | 2.712x | 0.97-1.30x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | tt32 | 667.648 | 695.501 | 0.960x | 0.924-0.980x | 0.962x | 0.81-0.95x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m256_n4096_k4096_16x16x64_w4_s2_cold | tt38 | 667.648 | 1779.917 | 0.375x | 0.360-0.384x | 0.379x | 0.83-1.08x | NO | NO | 0.00781 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro | 29.794 | 28.101 | 1.060x | 1.057-1.065x | 1.089x | 1.40-1.69x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ctl_s2 | 29.794 | 33.851 | 0.880x | 0.878-0.885x | 0.883x | 0.73-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ctl_s5 | 29.794 | 29.794 | 1.000x | 0.994-1.005x | 1.015x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | kernl | 29.794 | 31.153 | 0.956x | 0.951-0.963x | 0.969x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_clamp | 29.794 | 27.747 | 1.074x | 1.068-1.080x | 1.092x | 1.44-1.93x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_sweep | 29.794 | 28.101 | 1.060x | 1.057-1.065x | 1.089x | 1.15-1.60x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_tt32 | 29.794 | 28.633 | 1.041x | 1.038-1.045x | 1.064x | 1.04-1.27x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 31.980 | 28.633 | 1.117x | 1.116-1.118x | 1.122x | 0.88-1.13x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 31.980 | 28.101 | 1.138x | 1.137-1.140x | 1.148x | 1.18-1.51x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 31.567 | 28.101 | 1.123x | 1.123-1.125x | 1.138x | 0.71-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | tt32 | 29.794 | 31.980 | 0.932x | 0.929-0.935x | 0.949x | 1.09-1.21x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_warm | tt38 | 29.794 | 31.567 | 0.944x | 0.941-0.948x | 0.957x | 1.74-2.27x | NO | NO | 0.000244 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro | 45.670 | 33.997 | 1.343x | 1.315-1.366x | 1.425x | 1.44-1.68x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ctl_s2 | 45.670 | 56.934 | 0.802x | 0.789-0.812x | 0.990x | 0.68-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ctl_s5 | 45.670 | 45.466 | 1.005x | 0.987-1.014x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | kernl | 45.670 | 46.899 | 0.974x | 0.961-0.987x | 0.967x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_clamp | 45.670 | 32.358 | 1.411x | 1.390-1.427x | 1.499x | 1.59-1.73x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_sweep | 45.670 | 33.997 | 1.343x | 1.315-1.366x | 1.425x | 1.15-1.60x | yes | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_tt32 | 45.670 | 38.912 | 1.174x | 1.151-1.185x | 1.221x | 1.15-1.27x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 43.622 | 38.912 | 1.121x | 1.099-1.143x | 1.143x | 1.04-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 43.622 | 33.997 | 1.283x | 1.256-1.317x | 1.334x | 1.31-1.46x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 36.659 | 33.997 | 1.078x | 1.054-1.104x | 1.099x | 0.50-0.84x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | tt32 | 45.670 | 43.622 | 1.047x | 1.023-1.062x | 1.068x | 1.07-1.18x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s5_cold | tt38 | 45.670 | 36.659 | 1.246x | 1.221-1.266x | 1.297x | 2.01-2.82x | NO | NO | 0.000244 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro | 28.849 | 25.706 | 1.122x | 1.121-1.124x | 1.129x | 0.78-1.09x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ctl_s2 | 28.849 | 28.036 | 1.029x | 1.027-1.030x | 1.024x | 0.67-0.80x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ctl_s5 | 28.849 | 28.849 | 1.000x | 0.998-1.001x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | kernl | 28.849 | 26.377 | 1.094x | 1.086-1.098x | 1.136x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_clamp | 28.849 | 28.548 | 1.011x | 1.009-1.012x | 1.008x | 0.66-1.10x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_sweep | 28.849 | 25.706 | 1.122x | 1.121-1.124x | 1.129x | 1.15-1.60x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_tt32 | 28.849 | 24.311 | 1.187x | 1.184-1.187x | 1.203x | 1.04-1.42x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 27.083 | 24.311 | 1.114x | 1.112-1.115x | 1.111x | 1.15-1.50x | NO | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 27.083 | 25.706 | 1.054x | 1.052-1.056x | 1.042x | 0.86-1.15x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 28.637 | 25.706 | 1.114x | 1.113-1.116x | - | 0.66-0.82x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | tt32 | 28.849 | 27.083 | 1.065x | 1.063-1.067x | 1.083x | 0.88-0.98x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_warm | tt38 | 28.849 | 28.637 | 1.007x | 1.005-1.009x | - | 1.00-1.57x | yes | NO | 0.000244 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro | 39.322 | 36.864 | 1.067x | 1.049-1.090x | - | 0.98-1.07x | yes | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ctl_s2 | 39.322 | 51.405 | 0.765x | 0.758-0.776x | 0.729x | 0.62-0.74x | NO | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ctl_s5 | 39.322 | 39.322 | 1.000x | 0.985-1.016x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | kernl | 39.322 | 40.755 | 0.965x | 0.941-0.980x | 0.955x | 0.94-1.01x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_clamp | 39.322 | 33.997 | 1.157x | 1.137-1.176x | 1.190x | 0.83-1.34x | yes | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_sweep | 39.322 | 36.864 | 1.067x | 1.049-1.090x | - | 1.15-1.60x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_tt32 | 39.322 | 32.358 | 1.215x | 1.201-1.244x | 1.274x | 1.24-1.37x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 37.888 | 32.358 | 1.171x | 1.157-1.199x | 1.217x | 1.29-1.47x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 37.888 | 36.864 | 1.028x | 1.011-1.051x | - | 1.06-1.12x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 34.816 | 36.864 | 0.944x | 0.929-0.961x | - | 0.48-0.82x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | tt32 | 39.322 | 37.888 | 1.038x | 1.021-1.054x | 1.047x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_32x64x32_w2_s5_cold | tt38 | 39.322 | 34.816 | 1.129x | 1.117-1.148x | - | 1.25-2.08x | NO | NO | 0.000244 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro | 33.515 | 28.736 | 1.166x | 1.165-1.169x | 1.181x | 1.37-1.51x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ctl_s2 | 33.515 | 33.536 | 0.999x | 0.997-1.003x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ctl_s5 | 33.515 | 29.568 | 1.133x | 1.131-1.138x | 1.159x | 1.15-1.34x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | kernl | 33.515 | 35.968 | 0.932x | 0.930-0.935x | 0.930x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_clamp | 33.515 | 29.184 | 1.148x | 1.148-1.153x | 1.168x | 1.39-1.64x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_sweep | 33.515 | 28.736 | 1.166x | 1.165-1.169x | 1.181x | 1.15-1.60x | yes | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_tt32 | 33.515 | 30.336 | 1.105x | 1.103-1.109x | 1.108x | 1.02-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 30.699 | 30.336 | 1.012x | 1.009-1.018x | 1.003x | 0.86-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 30.699 | 28.736 | 1.068x | 1.066-1.073x | 1.069x | 1.15-1.37x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 31.893 | 28.736 | 1.110x | 1.108-1.111x | 1.105x | 0.81-0.89x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | tt32 | 33.515 | 30.699 | 1.092x | 1.087-1.096x | 1.105x | 1.08-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_warm | tt38 | 33.515 | 31.893 | 1.051x | 1.049-1.055x | 1.069x | 1.59-1.79x | NO | NO | 0.000244 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro | 56.934 | 42.394 | 1.343x | 1.325-1.366x | 1.107x | 1.29-1.53x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ctl_s2 | 56.934 | 56.934 | 1.000x | 0.993-1.011x | 1.000x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ctl_s5 | 56.934 | 45.466 | 1.252x | 1.242-1.267x | 1.009x | 1.23-1.44x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | kernl | 56.934 | 59.392 | 0.959x | 0.949-0.969x | 0.963x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_clamp | 56.934 | 42.803 | 1.330x | 1.307-1.353x | 1.090x | 1.50-1.75x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_sweep | 56.934 | 42.394 | 1.343x | 1.325-1.366x | 1.107x | 1.15-1.60x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_tt32 | 56.934 | 49.152 | 1.158x | 1.149-1.172x | 0.926x | 1.09-1.20x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 52.019 | 49.152 | 1.058x | 1.046-1.067x | 1.055x | 0.99-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 52.019 | 42.394 | 1.227x | 1.206-1.244x | 1.261x | 1.19-1.35x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 44.851 | 42.394 | 1.058x | 1.038-1.083x | 1.066x | 0.68-0.91x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | tt32 | 56.934 | 52.019 | 1.094x | 1.086-1.111x | 0.877x | 1.05-1.17x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x32x32_w2_s2_cold | tt38 | 56.934 | 44.851 | 1.269x | 1.248-1.290x | 1.038x | 1.68-1.89x | NO | NO | 0.000244 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro | 31.831 | 31.090 | 1.024x | 1.023-1.025x | 1.024x | 0.94-1.34x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ctl_s2 | 31.831 | 36.341 | 0.876x | 0.875-0.876x | 0.879x | 0.72-0.86x | NO | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ctl_s5 | 31.831 | 31.896 | 0.998x | 0.997-0.999x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | kernl | 31.831 | 33.618 | 0.947x | 0.946-0.948x | 0.947x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_clamp | 31.831 | 28.367 | 1.122x | 1.120-1.123x | 1.120x | 1.02-1.38x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 31.831 | 28.563 | 1.114x | 1.114-1.116x | 1.118x | 1.09-1.49x | yes | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 32.071 | 28.563 | 1.123x | 1.121-1.124x | 1.118x | 1.10-1.51x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_tt32 | 31.831 | 27.931 | 1.140x | 1.126-1.141x | 1.140x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 32.071 | 27.931 | 1.148x | 1.134-1.150x | 1.140x | 1.09-1.52x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 32.071 | 31.090 | 1.032x | 1.030-1.032x | 1.024x | 0.95-1.35x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 37.714 | 31.090 | 1.213x | 1.211-1.214x | 1.205x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | tt32 | 31.831 | 32.071 | 0.993x | 0.992-0.994x | 1.000x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_warm | tt38 | 31.831 | 37.714 | 0.844x | 0.844-0.846x | 0.849x | 1.00-1.41x | NO | NO | 0.000244 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro | 49.357 | 39.936 | 1.236x | 1.219-1.254x | 1.272x | 1.10-1.28x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ctl_s2 | 49.357 | 62.259 | 0.793x | 0.784-0.801x | 1.000x | 0.67-0.81x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ctl_s5 | 49.357 | 49.152 | 1.004x | 0.992-1.013x | 1.005x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | kernl | 49.357 | 51.405 | 0.960x | 0.948-0.968x | 0.956x | 0.95-1.02x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_clamp | 49.357 | 39.322 | 1.255x | 1.238-1.267x | 1.286x | 1.19-1.29x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 49.357 | 39.526 | 1.249x | 1.226-1.260x | 1.305x | 1.28-1.37x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 49.152 | 39.526 | 1.244x | 1.226-1.260x | 1.296x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_tt32 | 49.357 | 35.840 | 1.377x | 1.350-1.383x | 1.430x | 1.26-1.45x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 49.152 | 35.840 | 1.371x | 1.350-1.383x | 1.420x | 1.27-1.46x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 49.152 | 39.936 | 1.231x | 1.219-1.254x | 1.263x | 1.12-1.29x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 42.394 | 39.936 | 1.062x | 1.056-1.083x | 1.069x | 0.70-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | tt32 | 49.357 | 49.152 | 1.004x | 0.988-1.013x | 1.007x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_64x128x32_w4_s4_cold | tt38 | 49.357 | 42.394 | 1.164x | 1.144-1.169x | 1.190x | 1.17-1.76x | NO | NO | 0.000244 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro | 50.176 | 45.113 | 1.112x | 1.082-1.139x | 1.120x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ctl_r64 | 50.176 | 50.233 | 0.999x | 0.973-1.024x | 0.992x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ctl_s2 | 50.176 | 50.119 | 1.001x | 0.975-1.029x | 0.997x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ctl_s5 | 50.176 | 51.940 | 0.966x | 0.943-0.991x | 0.963x | 0.98-1.23x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | kernl | 50.176 | 51.655 | 0.971x | 0.945-0.997x | 0.967x | 0.90-0.99x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_clamp | 50.176 | 46.933 | 1.069x | 1.039-1.089x | 1.043x | 0.98-1.40x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_tt32 | 50.176 | 45.625 | 1.100x | 1.065-1.119x | - | 0.98-1.25x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 53.589 | 45.625 | 1.175x | 1.134-1.197x | - | 0.97-1.24x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 50.233 | 45.113 | 1.113x | 1.082-1.143x | 1.129x | 0.98-1.33x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 53.589 | 45.113 | 1.188x | 1.153-1.218x | 1.206x | 0.97-1.33x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 111.900 | 45.113 | 2.480x | 2.408-2.536x | 2.026x | 0.86-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | tt32 | 50.176 | 53.589 | 0.936x | 0.913-0.961x | 0.928x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_warm | tt38 | 50.176 | 111.900 | 0.448x | 0.439-0.460x | 0.553x | 0.98-1.50x | NO | NO | 0.000488 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro | 54.477 | 57.139 | 0.953x | 0.936-0.982x | 0.962x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ctl_r64 | 54.477 | 54.272 | 1.004x | 0.989-1.030x | 1.036x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ctl_s2 | 54.477 | 54.272 | 1.004x | 0.989-1.034x | 0.998x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ctl_s5 | 54.477 | 55.296 | 0.985x | 0.974-1.015x | - | 1.27-1.49x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | kernl | 54.477 | 56.115 | 0.971x | 0.964-0.993x | 0.978x | 0.91-1.00x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_clamp | 54.477 | 56.320 | 0.967x | 0.957-0.996x | 0.962x | 1.21-1.57x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_tt32 | 54.477 | 55.091 | 0.989x | 0.981-1.019x | - | 1.23-1.57x | NO | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 67.174 | 55.091 | 1.219x | 1.193-1.244x | - | 1.22-1.57x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 54.272 | 57.139 | 0.950x | 0.929-0.971x | 0.929x | 1.24-1.59x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 67.174 | 57.139 | 1.176x | 1.138-1.199x | 1.182x | 1.23-1.59x | NO | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 114.688 | 57.139 | 2.007x | 1.979-2.036x | 1.653x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | tt32 | 54.477 | 67.174 | 0.811x | 0.801-0.842x | 0.814x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_16x16x64_w4_s2_cold | tt38 | 54.477 | 114.688 | 0.475x | 0.472-0.484x | 0.582x | 1.32-1.66x | NO | NO | 0.000488 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro | 27.246 | 24.229 | 1.125x | 1.123-1.125x | 1.103x | 1.08-1.45x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | kernl | 27.246 | 30.373 | 0.897x | 0.896-0.898x | 0.900x | 0.81-0.92x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_clamp | 27.246 | 24.283 | 1.122x | 1.121-1.124x | 1.136x | 1.15-1.51x | NO | yes | 0 | 4, 4 | 168, 235 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_full_tt32 | 27.246 | 22.345 | 1.219x | 1.218-1.221x | 1.236x | 1.35-1.61x | NO | yes | 0 | 4, 4 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 28.800 | 22.345 | 1.289x | 1.288-1.291x | 1.305x | 1.64-1.84x | NO | yes | 0 | 4, 4 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_tt32 | 27.246 | 26.149 | 1.042x | 1.028-1.043x | 1.032x | 0.79-1.20x | yes | yes | 0 | 4, 4 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_tt32_vs_tt32 | 28.800 | 26.149 | 1.101x | 1.086-1.103x | 1.089x | 0.97-1.36x | yes | yes | 0 | 4, 4 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_vs_tt32 | 28.800 | 24.229 | 1.189x | 1.187-1.189x | 1.165x | 1.32-1.65x | NO | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | ro_vs_tt38 | 25.655 | 24.229 | 1.059x | 1.057-1.072x | 1.045x | 0.73-0.85x | NO | yes | 0 | 4, 4 | 211, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | tt32 | 27.246 | 28.800 | 0.946x | 0.945-0.947x | 0.947x | 0.79-0.91x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_warm | tt38 | 27.246 | 25.655 | 1.062x | 1.049-1.063x | 1.056x | 1.33-1.90x | NO | NO | 0.000244 | 4, 4 | 168, 211 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro | 44.851 | 35.021 | 1.281x | 1.275-1.294x | 1.329x | 1.27-1.36x | yes | yes | 0 | 4, 4 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | kernl | 44.851 | 47.923 | 0.936x | 0.924-0.944x | 0.928x | 0.84-0.94x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_clamp | 44.851 | 33.587 | 1.335x | 1.321-1.350x | 1.396x | 1.31-1.44x | yes | yes | 0 | 4, 4 | 168, 235 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_full_tt32 | 44.851 | 33.997 | 1.319x | 1.305-1.333x | 1.395x | 1.37-1.68x | NO | yes | 0 | 4, 4 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 44.851 | 33.997 | 1.319x | 1.305-1.333x | 1.396x | 1.53-1.98x | NO | yes | 0 | 4, 4 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_tt32 | 44.851 | 31.334 | 1.431x | 1.406-1.447x | 1.521x | 0.95-1.41x | NO | yes | 0 | 4, 4 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_tt32_vs_tt32 | 44.851 | 31.334 | 1.431x | 1.406-1.447x | 1.522x | 1.13-1.56x | yes | yes | 0 | 4, 4 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_vs_tt32 | 44.851 | 35.021 | 1.281x | 1.275-1.294x | 1.330x | 1.41-1.60x | NO | yes | 0 | 4, 4 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | ro_vs_tt38 | 31.539 | 35.021 | 0.901x | 0.895-0.912x | 0.880x | 0.51-0.85x | NO | yes | 0 | 4, 4 | 211, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | tt32 | 44.851 | 44.851 | 1.000x | 0.991-1.009x | 0.999x | 0.82-0.93x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x32x32_w4_s4_cold | tt38 | 44.851 | 31.539 | 1.422x | 1.406-1.438x | 1.510x | 1.60-2.43x | NO | NO | 0.000244 | 4, 4 | 168, 211 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro | 35.709 | 37.561 | 0.951x | 0.951-0.952x | 0.958x | 0.72-0.92x | NO | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | kernl | 35.709 | 37.322 | 0.957x | 0.957-0.958x | 0.962x | 0.87-0.95x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_clamp | 35.709 | 37.736 | 0.946x | 0.946-0.947x | 0.949x | 0.71-0.90x | NO | yes | 0 | 4, 4 | 255, 252 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_full_tt32 | 35.709 | 28.955 | 1.233x | 1.232-1.234x | 1.242x | 0.97-1.26x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 31.984 | 28.955 | 1.105x | 1.103-1.105x | 1.104x | 0.90-1.20x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_tt32 | 35.709 | 28.520 | 1.252x | 1.252-1.254x | 1.252x | 1.16-1.56x | yes | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_tt32_vs_tt32 | 31.984 | 28.520 | 1.121x | 1.121-1.122x | 1.113x | 1.08-1.48x | yes | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_vs_tt32 | 31.984 | 37.561 | 0.852x | 0.851-0.852x | 0.852x | 0.67-0.87x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | ro_vs_tt38 | 32.267 | 37.561 | 0.859x | 0.859-0.860x | 0.856x | 0.55-0.66x | NO | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | tt32 | 35.709 | 31.984 | 1.116x | 1.116-1.118x | 1.125x | 1.02-1.10x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_warm | tt38 | 35.709 | 32.267 | 1.107x | 1.106-1.107x | 1.120x | 1.17-1.57x | NO | NO | 0.000244 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro | 53.658 | 54.682 | 0.981x | 0.970-0.992x | 0.990x | 0.83-0.94x | NO | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | kernl | 53.658 | 55.706 | 0.963x | 0.953-0.974x | 1.229x | 0.88-0.96x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_clamp | 53.658 | 53.248 | 1.008x | 1.000-1.023x | 1.018x | 0.81-0.92x | NO | yes | 0 | 4, 4 | 255, 252 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_full_tt32 | 53.658 | 44.646 | 1.202x | 1.197-1.222x | 1.249x | 1.11-1.21x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 48.947 | 44.646 | 1.096x | 1.092-1.116x | 1.125x | 1.05-1.17x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_tt32 | 53.658 | 36.454 | 1.472x | 1.450-1.500x | 1.560x | 1.33-1.47x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_tt32_vs_tt32 | 48.947 | 36.454 | 1.343x | 1.322-1.369x | 1.405x | 1.25-1.42x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_vs_tt32 | 48.947 | 54.682 | 0.895x | 0.885-0.906x | 0.891x | 0.78-0.90x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | ro_vs_tt38 | 38.298 | 54.682 | 0.700x | 0.691-0.707x | 0.669x | 0.45-0.66x | NO | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | tt32 | 53.658 | 48.947 | 1.096x | 1.083-1.109x | 1.110x | 1.01-1.09x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_128x64x32_w4_s4_cold | tt38 | 53.658 | 38.298 | 1.401x | 1.388-1.419x | 1.479x | 1.34-1.93x | yes | NO | 0.000244 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro | 56.002 | 52.118 | 1.075x | 1.072-1.082x | 0.838x | 1.41-1.74x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ctl_s2 | 56.002 | 63.912 | 0.876x | 0.874-0.883x | 0.863x | 0.73-0.88x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ctl_s5 | 56.002 | 55.967 | 1.001x | 0.994-1.008x | 1.005x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | kernl | 56.002 | 58.439 | 0.958x | 0.952-0.965x | 0.954x | 0.89-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro_clamp | 56.002 | 51.165 | 1.095x | 1.087-1.105x | 0.858x | 1.46-2.00x | NO | yes | 0 | 4, 4 | 168, 239 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro_tt32 | 56.002 | 52.824 | 1.060x | 1.057-1.069x | 1.041x | 1.04-1.28x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 59.463 | 52.824 | 1.126x | 1.123-1.129x | 1.119x | 0.88-1.14x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro_vs_tt32 | 59.463 | 52.118 | 1.141x | 1.139-1.142x | 0.901x | 1.19-1.54x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | ro_vs_tt38 | 59.109 | 52.118 | 1.134x | 1.132-1.135x | 0.893x | 0.69-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | tt32 | 56.002 | 59.463 | 0.942x | 0.940-0.948x | 0.930x | 1.10-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_warm | tt38 | 56.002 | 59.109 | 0.947x | 0.946-0.954x | 0.939x | 1.78-2.39x | NO | NO | 0.000488 | 4, 4 | 168, 216 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro | 83.968 | 59.802 | 1.404x | 1.392-1.417x | 1.457x | 1.46-1.70x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ctl_s2 | 83.968 | 107.315 | 0.782x | 0.776-0.786x | 0.773x | 0.67-0.82x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ctl_s5 | 83.968 | 83.968 | 1.000x | 0.988-1.007x | 1.004x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | kernl | 83.968 | 86.630 | 0.969x | 0.960-0.976x | 0.967x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro_clamp | 83.968 | 57.344 | 1.464x | 1.452-1.478x | 1.210x | 1.62-1.76x | NO | yes | 0 | 4, 4 | 168, 239 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro_tt32 | 83.968 | 69.837 | 1.202x | 1.190-1.212x | 1.218x | 1.16-1.27x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 79.258 | 69.837 | 1.135x | 1.125-1.156x | 1.135x | 1.05-1.11x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro_vs_tt32 | 79.258 | 59.802 | 1.325x | 1.317-1.352x | 1.358x | 1.33-1.48x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | ro_vs_tt38 | 64.307 | 59.802 | 1.075x | 1.068-1.090x | 1.084x | 0.47-0.83x | NO | yes | 0 | 4, 4 | 216, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | tt32 | 83.968 | 79.258 | 1.059x | 1.041-1.065x | 1.073x | 1.07-1.19x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s5_cold | tt38 | 83.968 | 64.307 | 1.306x | 1.291-1.313x | 1.344x | 2.06-2.99x | NO | NO | 0.000488 | 4, 4 | 168, 216 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro | 53.124 | 46.980 | 1.131x | 1.129-1.133x | 0.903x | 0.77-1.09x | NO | yes | 0 | 4, 4 | 165, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ctl_s2 | 53.124 | 52.814 | 1.006x | 1.004-1.008x | 1.013x | 0.66-0.79x | NO | yes | 0 | 4, 4 | 165, 162 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ctl_s5 | 53.124 | 53.155 | 0.999x | 0.997-1.001x | 1.001x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | kernl | 53.124 | 46.794 | 1.135x | 1.130-1.139x | 0.913x | 0.94-1.01x | NO | yes | 0 | 4, 4 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro_clamp | 53.124 | 52.658 | 1.009x | 1.006-1.011x | 1.012x | 0.65-1.10x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro_tt32 | 53.124 | 44.342 | 1.198x | 1.195-1.201x | 0.959x | 1.05-1.46x | yes | yes | 0 | 4, 4 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 48.966 | 44.342 | 1.104x | 1.103-1.108x | 1.103x | 1.15-1.54x | NO | yes | 0 | 4, 4 | 168, 164 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro_vs_tt32 | 48.966 | 46.980 | 1.042x | 1.042-1.045x | 1.038x | 0.85-1.16x | yes | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | ro_vs_tt38 | 53.341 | 46.980 | 1.135x | 1.132-1.138x | - | 0.64-0.81x | NO | yes | 0 | 4, 4 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | tt32 | 53.124 | 48.966 | 1.085x | 1.082-1.086x | 0.870x | 0.88-0.97x | NO | yes | 0 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_warm | tt38 | 53.124 | 53.341 | 0.996x | 0.993-0.999x | - | 1.00-1.62x | NO | NO | 0.000488 | 4, 4 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro | 70.246 | 65.126 | 1.079x | 1.066-1.082x | - | 0.98-1.08x | NO | yes | 0 | 4, 4 | 165, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ctl_s2 | 70.246 | 96.461 | 0.728x | 0.722-0.735x | 0.711x | 0.61-0.73x | yes | yes | 0 | 4, 4 | 165, 162 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ctl_s5 | 70.246 | 70.246 | 1.000x | 0.988-1.006x | 0.998x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | kernl | 70.246 | 72.909 | 0.963x | 0.950-0.972x | 0.951x | 0.94-1.01x | yes | yes | 0 | 4, 4 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro_clamp | 70.246 | 58.368 | 1.204x | 1.188-1.216x | 1.221x | 0.83-1.36x | yes | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro_tt32 | 70.246 | 57.344 | 1.225x | 1.214-1.237x | 1.247x | 1.25-1.39x | NO | yes | 0 | 4, 4 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 70.246 | 57.344 | 1.225x | 1.214-1.237x | 1.240x | 1.31-1.49x | NO | yes | 0 | 4, 4 | 168, 164 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro_vs_tt32 | 70.246 | 65.126 | 1.079x | 1.066-1.082x | - | 1.06-1.12x | yes | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | ro_vs_tt38 | 60.006 | 65.126 | 0.921x | 0.912-0.928x | - | 0.46-0.81x | NO | yes | 0 | 4, 4 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | tt32 | 70.246 | 70.246 | 1.000x | 0.991-1.009x | 1.006x | 0.90-0.99x | NO | yes | 0 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_32x64x32_w2_s5_cold | tt38 | 70.246 | 60.006 | 1.171x | 1.156-1.178x | - | 1.27-2.18x | NO | NO | 0.000488 | 4, 4 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro | 63.829 | 53.400 | 1.195x | 1.192-1.199x | 1.196x | 1.38-1.54x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ctl_s2 | 63.829 | 63.829 | 1.000x | 0.995-1.005x | 0.991x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ctl_s5 | 63.829 | 55.751 | 1.145x | 1.141-1.151x | 1.155x | 1.15-1.35x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | kernl | 63.829 | 69.101 | 0.924x | 0.918-0.929x | 0.926x | 0.88-0.97x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro_clamp | 63.829 | 54.689 | 1.167x | 1.164-1.172x | 1.171x | 1.41-1.67x | NO | yes | 0 | 4, 4 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro_tt32 | 63.829 | 58.747 | 1.087x | 1.081-1.090x | 1.073x | 1.02-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 59.316 | 58.747 | 1.010x | 1.005-1.012x | 0.999x | 0.86-1.09x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro_vs_tt32 | 59.316 | 53.400 | 1.111x | 1.108-1.113x | 1.113x | 1.16-1.38x | NO | yes | 0 | 4, 4 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | ro_vs_tt38 | 60.454 | 53.400 | 1.132x | 1.130-1.138x | 1.137x | 0.80-0.89x | NO | yes | 0 | 4, 4 | 212, 234 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | tt32 | 63.829 | 59.316 | 1.076x | 1.072-1.081x | 1.074x | 1.08-1.22x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_warm | tt38 | 63.829 | 60.454 | 1.056x | 1.049-1.060x | 1.052x | 1.62-1.84x | NO | NO | 0.000488 | 4, 4 | 168, 212 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro | 107.520 | 76.800 | 1.400x | 1.386-1.417x | 1.446x | 1.30-1.55x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ctl_s2 | 107.520 | 107.315 | 1.002x | 0.994-1.010x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ctl_s5 | 107.520 | 84.173 | 1.277x | 1.269-1.289x | 1.300x | 1.24-1.45x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | kernl | 107.520 | 112.230 | 0.958x | 0.953-0.963x | 0.956x | 0.90-0.98x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro_clamp | 107.520 | 78.029 | 1.378x | 1.358-1.398x | 1.409x | 1.51-1.78x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro_tt32 | 107.520 | 91.341 | 1.177x | 1.172-1.187x | 1.189x | 1.10-1.21x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 96.666 | 91.341 | 1.058x | 1.051-1.068x | 1.063x | 1.00-1.07x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro_vs_tt32 | 96.666 | 76.800 | 1.259x | 1.243-1.274x | 1.293x | 1.20-1.35x | yes | yes | 0 | 4, 4 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | ro_vs_tt38 | 82.330 | 76.800 | 1.072x | 1.050-1.097x | 1.082x | 0.67-0.91x | NO | yes | 0 | 4, 4 | 212, 234 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | tt32 | 107.520 | 96.666 | 1.112x | 1.105-1.121x | 1.118x | 1.05-1.18x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x32x32_w2_s2_cold | tt38 | 107.520 | 82.330 | 1.306x | 1.284-1.327x | 1.336x | 1.70-1.92x | NO | NO | 0.000488 | 4, 4 | 168, 212 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro | 58.368 | 57.382 | 1.017x | 1.017-1.019x | 1.014x | 0.94-1.36x | yes | yes | 0 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ctl_s2 | 58.368 | 67.925 | 0.859x | 0.859-0.860x | 0.852x | 0.71-0.86x | yes | yes | 0 | 4, 4 | 241, 238 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ctl_s5 | 58.368 | 58.671 | 0.995x | 0.994-0.996x | 0.997x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | kernl | 58.368 | 62.502 | 0.934x | 0.934-0.935x | 0.933x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_clamp | 58.368 | 52.224 | 1.118x | 1.118-1.119x | 1.107x | 1.02-1.40x | yes | yes | 0 | 4, 4 | 241, 253 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_full_tt32 | 58.368 | 53.362 | 1.094x | 1.093-1.095x | 1.088x | 1.09-1.52x | NO | yes | 0 | 4, 4 | 241, 245 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 59.961 | 53.362 | 1.124x | 1.123-1.127x | 1.119x | 1.11-1.54x | yes | yes | 0 | 4, 4 | 243, 245 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_tt32 | 58.368 | 51.845 | 1.126x | 1.117-1.127x | 1.122x | 1.08-1.54x | yes | yes | 0 | 4, 4 | 241, 242 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 59.961 | 51.845 | 1.157x | 1.147-1.160x | 1.153x | 1.09-1.55x | yes | yes | 0 | 4, 4 | 243, 242 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_vs_tt32 | 59.961 | 57.382 | 1.045x | 1.045-1.048x | 1.042x | 0.95-1.37x | yes | yes | 0 | 4, 4 | 243, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | ro_vs_tt38 | 71.377 | 57.382 | 1.244x | 1.243-1.247x | 1.236x | 0.92-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | tt32 | 58.368 | 59.961 | 0.973x | 0.972-0.974x | 0.973x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_warm | tt38 | 58.368 | 71.377 | 0.818x | 0.816-0.819x | 0.820x | 1.00-1.43x | NO | NO | 0.000488 | 4, 4 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro | 90.522 | 71.885 | 1.259x | 1.246-1.269x | 1.280x | 1.11-1.29x | yes | yes | 0 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ctl_s2 | 90.522 | 119.808 | 0.756x | 0.751-0.762x | 0.747x | 0.66-0.80x | yes | yes | 0 | 4, 4 | 241, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ctl_s5 | 90.522 | 90.317 | 1.002x | 0.995-1.009x | 0.999x | 0.97-1.03x | yes | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | kernl | 90.522 | 95.027 | 0.953x | 0.944-0.961x | 0.948x | 0.95-1.02x | NO | yes | 0 | 4, 4 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_clamp | 90.522 | 71.066 | 1.274x | 1.261-1.280x | 1.294x | 1.20-1.30x | yes | yes | 0 | 4, 4 | 241, 253 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_full_tt32 | 90.522 | 71.680 | 1.263x | 1.254-1.272x | 1.296x | 1.29-1.38x | NO | yes | 0 | 4, 4 | 241, 245 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 92.365 | 71.680 | 1.289x | 1.285-1.298x | 1.318x | 1.30-1.39x | NO | yes | 0 | 4, 4 | 243, 245 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_tt32 | 90.522 | 65.126 | 1.390x | 1.379-1.405x | 1.414x | 1.27-1.47x | yes | yes | 0 | 4, 4 | 241, 242 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 92.365 | 65.126 | 1.418x | 1.414-1.434x | 1.439x | 1.28-1.48x | yes | yes | 0 | 4, 4 | 243, 242 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_vs_tt32 | 92.365 | 71.885 | 1.285x | 1.278-1.294x | 1.302x | 1.12-1.30x | yes | yes | 0 | 4, 4 | 243, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | ro_vs_tt38 | 76.390 | 71.885 | 1.063x | 1.054-1.069x | 1.068x | 0.68-0.98x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | tt32 | 90.522 | 92.365 | 0.980x | 0.971-0.984x | 0.983x | 0.96-1.02x | yes | yes | 0 | 4, 4 | 241, 243 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_64x128x32_w4_s4_cold | tt38 | 90.522 | 76.390 | 1.185x | 1.176-1.194x | 1.199x | 1.17-1.80x | yes | NO | 0.000488 | 4, 4 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro | 96.154 | 83.763 | 1.148x | 1.132-1.161x | 1.155x | 0.98-1.35x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ctl_r64 | 96.154 | 96.358 | 0.998x | 0.983-1.012x | 1.002x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ctl_s2 | 96.154 | 96.358 | 0.998x | 0.986-1.012x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ctl_s5 | 96.154 | 95.744 | 1.004x | 0.994-1.015x | 1.009x | 0.98-1.24x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | kernl | 96.154 | 98.202 | 0.979x | 0.970-0.992x | 0.984x | 0.89-0.99x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_clamp | 96.154 | 87.962 | 1.093x | 1.080-1.110x | 0.873x | 0.98-1.42x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_tt32 | 96.154 | 87.245 | 1.102x | 1.093-1.114x | 1.110x | 0.98-1.26x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 102.707 | 87.245 | 1.177x | 1.159-1.194x | 1.218x | 0.97-1.25x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 96.358 | 83.763 | 1.150x | 1.136-1.163x | 1.153x | 0.98-1.35x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_vs_tt32 | 102.707 | 83.763 | 1.226x | 1.202-1.244x | 1.268x | 0.97-1.34x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | ro_vs_tt38 | 219.034 | 83.763 | 2.615x | 2.597-2.626x | 2.608x | 0.85-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | tt32 | 96.154 | 102.707 | 0.936x | 0.919-0.957x | 0.911x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_warm | tt38 | 96.154 | 219.034 | 0.439x | 0.436-0.443x | 0.443x | 0.98-1.53x | NO | NO | 0.00195 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro | 99.738 | 104.858 | 0.951x | 0.931-0.978x | 0.947x | 1.25-1.62x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ctl_r64 | 99.738 | 99.738 | 1.000x | 0.986-1.017x | 1.001x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ctl_s2 | 99.738 | 99.738 | 1.000x | 0.986-1.023x | 0.998x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ctl_s5 | 99.738 | 98.509 | 1.012x | 0.996-1.029x | - | 1.27-1.50x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | kernl | 99.738 | 102.195 | 0.976x | 0.968-0.988x | 0.966x | 0.91-1.00x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_clamp | 99.738 | 100.966 | 0.988x | 0.974-0.998x | 0.978x | 1.22-1.59x | NO | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_tt32 | 99.738 | 100.147 | 0.996x | 0.978-1.008x | - | 1.24-1.59x | NO | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 122.470 | 100.147 | 1.223x | 1.198-1.238x | - | 1.23-1.59x | NO | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 99.738 | 104.858 | 0.951x | 0.929-0.978x | 0.947x | 1.25-1.62x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_vs_tt32 | 122.470 | 104.858 | 1.168x | 1.140-1.201x | 1.175x | 1.24-1.61x | NO | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | ro_vs_tt38 | 219.341 | 104.858 | 2.092x | 2.056-2.141x | 2.137x | 0.91-1.03x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | tt32 | 99.738 | 122.470 | 0.814x | 0.803-0.828x | 0.806x | 0.97-1.04x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_16x16x64_w4_s2_cold | tt38 | 99.738 | 219.341 | 0.455x | 0.450-0.459x | 0.443x | 1.33-1.69x | NO | NO | 0.00195 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro | 51.040 | 45.216 | 1.129x | 1.127-1.134x | 1.124x | 1.08-1.48x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | kernl | 51.040 | 57.408 | 0.889x | 0.886-0.894x | 1.130x | 0.81-0.92x | yes | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_clamp | 51.040 | 45.344 | 1.126x | 1.119-1.131x | 1.134x | 1.16-1.55x | NO | yes | 0 | 4, 4 | 168, 235 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_full_tt32 | 51.040 | 41.472 | 1.231x | 1.229-1.238x | 1.234x | 1.36-1.66x | NO | yes | 0 | 4, 4 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 54.336 | 41.472 | 1.310x | 1.308-1.313x | 1.023x | 1.67-1.90x | NO | yes | 0 | 4, 4 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_tt32 | 51.040 | 49.408 | 1.033x | 1.022-1.046x | 1.022x | 0.79-1.21x | yes | yes | 0 | 4, 4 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_tt32_vs_tt32 | 54.336 | 49.408 | 1.100x | 1.088-1.110x | 0.847x | 0.97-1.38x | yes | yes | 0 | 4, 4 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_vs_tt32 | 54.336 | 45.216 | 1.202x | 1.200-1.203x | 0.932x | 1.33-1.69x | NO | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | ro_vs_tt38 | 48.480 | 45.216 | 1.072x | 1.063-1.079x | 1.071x | 0.71-0.84x | NO | yes | 0 | 4, 4 | 211, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | tt32 | 51.040 | 54.336 | 0.939x | 0.938-0.945x | 1.206x | 0.79-0.90x | NO | yes | 0 | 4, 4 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_warm | tt38 | 51.040 | 48.480 | 1.053x | 1.046-1.067x | 1.050x | 1.35-1.98x | NO | NO | 0.000488 | 4, 4 | 168, 211 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro | 84.173 | 64.102 | 1.313x | 1.303-1.328x | 1.341x | 1.28-1.37x | yes | yes | 0 | 4, 4 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | kernl | 84.173 | 90.522 | 0.930x | 0.923-0.937x | 0.926x | 0.83-0.94x | yes | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_clamp | 84.173 | 60.621 | 1.389x | 1.372-1.400x | 1.417x | 1.33-1.46x | yes | yes | 0 | 4, 4 | 168, 235 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_full_tt32 | 84.173 | 62.464 | 1.348x | 1.337-1.359x | 1.380x | 1.39-1.71x | NO | yes | 0 | 4, 4 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 83.149 | 62.464 | 1.331x | 1.324-1.342x | 1.369x | 1.56-2.02x | NO | yes | 0 | 4, 4 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_tt32 | 84.173 | 54.886 | 1.534x | 1.520-1.553x | 1.245x | 0.95-1.43x | NO | yes | 0 | 4, 4 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_tt32_vs_tt32 | 83.149 | 54.886 | 1.515x | 1.506-1.534x | 1.235x | 1.13-1.59x | yes | yes | 0 | 4, 4 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_vs_tt32 | 83.149 | 64.102 | 1.297x | 1.290-1.312x | 1.330x | 1.43-1.62x | NO | yes | 0 | 4, 4 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | ro_vs_tt38 | 54.886 | 64.102 | 0.856x | 0.847-0.865x | 1.087x | 0.49-0.84x | NO | yes | 0 | 4, 4 | 211, 233 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | tt32 | 84.173 | 83.149 | 1.012x | 1.002-1.020x | 1.008x | 0.81-0.93x | NO | yes | 0 | 4, 4 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x32x32_w4_s4_cold | tt38 | 84.173 | 54.886 | 1.534x | 1.520-1.553x | 1.233x | 1.63-2.56x | NO | NO | 0.000488 | 4, 4 | 168, 211 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro | 66.484 | 70.163 | 0.948x | 0.948-0.949x | 0.957x | 0.72-0.91x | NO | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | kernl | 66.484 | 69.973 | 0.950x | 0.950-0.951x | 0.954x | 0.86-0.95x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_clamp | 66.484 | 70.466 | 0.943x | 0.943-0.944x | 0.942x | 0.70-0.90x | NO | yes | 0 | 4, 4 | 255, 252 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_full_tt32 | 66.484 | 54.196 | 1.227x | 1.227-1.228x | 1.222x | 0.97-1.27x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 59.809 | 54.196 | 1.104x | 1.104-1.104x | 1.091x | 0.90-1.21x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_tt32 | 66.484 | 53.020 | 1.254x | 1.253-1.256x | 1.255x | 1.16-1.59x | yes | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_tt32_vs_tt32 | 59.809 | 53.020 | 1.128x | 1.127-1.129x | 1.120x | 1.08-1.51x | yes | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_vs_tt32 | 59.809 | 70.163 | 0.852x | 0.852-0.853x | 0.854x | 0.66-0.87x | yes | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | ro_vs_tt38 | 60.378 | 70.163 | 0.861x | 0.860-0.861x | 0.855x | 0.53-0.65x | NO | yes | 0 | 4, 4 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | tt32 | 66.484 | 59.809 | 1.112x | 1.112-1.112x | 1.120x | 1.02-1.10x | NO | yes | 0 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_warm | tt38 | 66.484 | 60.378 | 1.101x | 1.101-1.102x | 1.119x | 1.18-1.61x | NO | NO | 0.000488 | 4, 4 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro | 99.942 | 101.581 | 0.984x | 0.978-0.990x | 0.980x | 0.82-0.93x | NO | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | kernl | 99.942 | 103.629 | 0.964x | 0.961-0.972x | 0.968x | 0.88-0.96x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_clamp | 99.942 | 97.280 | 1.027x | 1.023-1.036x | 1.032x | 0.81-0.92x | NO | yes | 0 | 4, 4 | 255, 252 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_full_tt32 | 99.942 | 82.534 | 1.211x | 1.202-1.219x | 1.235x | 1.12-1.22x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 90.931 | 82.534 | 1.102x | 1.094-1.109x | 1.116x | 1.05-1.17x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_tt32 | 99.942 | 65.536 | 1.525x | 1.517-1.536x | 1.576x | 1.34-1.49x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_tt32_vs_tt32 | 90.931 | 65.536 | 1.387x | 1.380-1.398x | 1.424x | 1.25-1.43x | yes | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_vs_tt32 | 90.931 | 101.581 | 0.895x | 0.890-0.901x | 0.886x | 0.77-0.90x | yes | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | ro_vs_tt38 | 67.584 | 101.581 | 0.665x | 0.661-0.669x | 0.643x | 0.43-0.65x | NO | yes | 0 | 4, 4 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | tt32 | 99.942 | 90.931 | 1.099x | 1.092-1.106x | 1.107x | 1.01-1.09x | NO | yes | 0 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_128x64x32_w4_s4_cold | tt38 | 99.942 | 67.584 | 1.479x | 1.471-1.489x | 1.525x | 1.35-1.98x | yes | NO | 0.000488 | 4, 4 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro | 998.059 | 925.013 | 1.079x | 1.049-1.102x | 1.070x | 0.97-1.09x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ctl_s2 | 998.059 | 1261.568 | 0.791x | 0.776-0.807x | 0.775x | 0.72-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ctl_s5 | 998.059 | 996.352 | 1.002x | 0.972-1.024x | 1.005x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | kernl | 998.059 | 1298.773 | 0.768x | 0.745-0.789x | 0.739x | 0.89-1.03x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_clamp | 998.059 | 898.731 | 1.111x | 1.081-1.134x | 1.117x | 0.97-1.11x | NO | yes | 0 | 12, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_sweep | 998.059 | 925.013 | 1.079x | 1.049-1.102x | 1.070x | 1.15-1.35x | NO | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_tt32 | 998.059 | 1064.960 | 0.937x | 0.915-0.958x | 0.953x | 0.74-1.03x | yes | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 1057.109 | 1064.960 | 0.993x | 0.971-1.016x | 1.001x | 0.87-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 1057.109 | 925.013 | 1.143x | 1.113-1.169x | 1.124x | 0.97-1.33x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 1155.413 | 925.013 | 1.249x | 1.217-1.281x | 1.220x | 0.76-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | tt32 | 998.059 | 1057.109 | 0.944x | 0.921-0.965x | 0.952x | 0.78-1.03x | yes | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_warm | tt38 | 998.059 | 1155.413 | 0.864x | 0.840-0.882x | 0.877x | 0.97-1.35x | NO | NO | 0.0156 | 12, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro | 996.352 | 927.130 | 1.075x | 1.058-1.086x | 1.045x | 0.97-1.24x | yes | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ctl_s2 | 996.352 | 1268.941 | 0.785x | 0.775-0.801x | 0.763x | 0.67-0.88x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ctl_s5 | 996.352 | 1003.930 | 0.992x | 0.982-1.013x | 0.993x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | kernl | 996.352 | 1292.698 | 0.771x | 0.758-0.782x | 0.714x | 0.90-1.03x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_clamp | 996.352 | 889.856 | 1.120x | 1.105-1.143x | 1.102x | 0.97-1.28x | yes | yes | 0 | 12, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_sweep | 996.352 | 927.130 | 1.075x | 1.058-1.086x | 1.045x | 1.15-1.35x | NO | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_tt32 | 996.352 | 1068.851 | 0.932x | 0.921-0.953x | 0.952x | 0.83-1.03x | yes | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 1060.659 | 1068.851 | 0.992x | 0.972-1.007x | 0.999x | 1.01-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 1060.659 | 927.130 | 1.144x | 1.117-1.148x | 1.097x | 1.01-1.49x | yes | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 1125.581 | 927.130 | 1.214x | 1.179-1.235x | 1.159x | 0.76-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | tt32 | 996.352 | 1060.659 | 0.939x | 0.934-0.960x | 0.953x | 0.76-0.99x | yes | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s5_cold | tt38 | 996.352 | 1125.581 | 0.885x | 0.868-0.909x | 0.902x | 0.97-1.56x | NO | NO | 0.0156 | 12, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro | 1122.304 | 1049.600 | 1.069x | 1.046-1.093x | 1.064x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ctl_s2 | 1122.304 | 1183.061 | 0.949x | 0.925-0.969x | 0.946x | 0.97-1.08x | NO | yes | 0 | 8, 12 | 165, 162 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ctl_s5 | 1122.304 | 1120.597 | 1.002x | 0.980-1.025x | 0.999x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | kernl | 1122.304 | 2424.149 | 0.463x | 0.448-0.479x | 0.447x | 0.93-1.03x | NO | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro_clamp | 1122.304 | 963.243 | 1.165x | 1.138-1.206x | 1.179x | 0.64-1.03x | NO | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro_tt32 | 1122.304 | 945.493 | 1.187x | 1.161-1.222x | 1.202x | 0.97-1.11x | NO | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 918.528 | 945.493 | 0.971x | 0.949-1.002x | 0.969x | 0.97-1.22x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 918.528 | 1049.600 | 0.875x | 0.855-0.897x | 0.858x | 0.85-1.03x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 1202.176 | 1049.600 | 1.145x | 1.120-1.171x | 1.105x | 0.74-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | tt32 | 1122.304 | 918.528 | 1.222x | 1.191-1.253x | 1.241x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_warm | tt38 | 1122.304 | 1202.176 | 0.934x | 0.911-0.957x | 0.963x | 0.97-1.06x | NO | NO | 0.0156 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro | 1121.075 | 1049.395 | 1.068x | 1.039-1.094x | - | 0.97-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ctl_s2 | 1121.075 | 1183.334 | 0.947x | 0.927-0.970x | 0.943x | 0.86-1.03x | yes | yes | 0 | 8, 12 | 165, 162 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ctl_s5 | 1121.075 | 1121.075 | 1.000x | 0.979-1.024x | 0.990x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | kernl | 1121.075 | 2429.747 | 0.461x | 0.449-0.478x | 0.419x | 0.94-1.03x | NO | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro_clamp | 1121.075 | 960.512 | 1.167x | 1.143-1.210x | 1.174x | 0.83-1.18x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro_tt32 | 1121.075 | 933.683 | 1.201x | 1.172-1.233x | 1.225x | 0.97-1.40x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 908.288 | 933.683 | 0.973x | 0.948-1.002x | 0.987x | 0.97-1.51x | yes | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 908.288 | 1049.395 | 0.866x | 0.841-0.889x | - | 0.97-1.13x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 1185.792 | 1049.395 | 1.130x | 1.096-1.157x | - | 0.74-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | tt32 | 1121.075 | 908.288 | 1.234x | 1.203-1.264x | 1.241x | 0.90-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_32x64x32_w2_s5_cold | tt38 | 1121.075 | 1185.792 | 0.945x | 0.924-0.970x | - | 0.97-1.34x | NO | NO | 0.0156 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro | 1226.411 | 1108.992 | 1.106x | 1.092-1.115x | 1.100x | 0.97-1.12x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ctl_s2 | 1226.411 | 1227.093 | 0.999x | 0.991-1.005x | 0.996x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ctl_s5 | 1226.411 | 957.099 | 1.281x | 1.265-1.289x | 1.284x | 0.97-1.36x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | kernl | 1226.411 | 1501.867 | 0.817x | 0.800-0.825x | 0.806x | 0.88-1.03x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro_clamp | 1226.411 | 1196.373 | 1.025x | 1.017-1.036x | 1.030x | 0.97-1.22x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro_tt32 | 1226.411 | 1033.899 | 1.186x | 1.173-1.196x | 1.205x | 0.97-1.22x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 1000.448 | 1033.899 | 0.968x | 0.958-0.980x | 0.975x | 0.85-1.09x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 1000.448 | 1108.992 | 0.902x | 0.892-0.914x | 0.890x | 0.82-1.03x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 1406.976 | 1108.992 | 1.269x | 1.252-1.284x | 1.247x | 0.80-1.03x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | tt32 | 1226.411 | 1000.448 | 1.226x | 1.212-1.232x | 1.236x | 0.97-1.22x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_warm | tt38 | 1226.411 | 1406.976 | 0.872x | 0.862-0.878x | 0.882x | 0.97-1.35x | NO | NO | 0.0156 | 12, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro | 1232.282 | 1117.389 | 1.103x | 1.091-1.116x | 1.110x | 0.93-1.12x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ctl_s2 | 1232.282 | 1231.872 | 1.000x | 0.991-1.009x | 1.003x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ctl_s5 | 1232.282 | 960.102 | 1.283x | 1.272-1.300x | 1.307x | 1.15-1.47x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | kernl | 1232.282 | 1523.098 | 0.809x | 0.794-0.824x | 0.803x | 0.90-0.98x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro_clamp | 1232.282 | 1195.622 | 1.031x | 1.016-1.044x | 1.040x | 1.08-1.30x | NO | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro_tt32 | 1232.282 | 1028.710 | 1.198x | 1.177-1.204x | 1.216x | 1.10-1.21x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 1000.653 | 1028.710 | 0.973x | 0.959-0.984x | 0.980x | 1.00-1.07x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 1000.653 | 1117.389 | 0.896x | 0.889-0.912x | 0.894x | 0.85-0.98x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 1411.277 | 1117.389 | 1.263x | 1.250-1.285x | 1.259x | 0.66-0.90x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | tt32 | 1232.282 | 1000.653 | 1.231x | 1.213-1.238x | 1.241x | 1.05-1.18x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x32x32_w2_s2_cold | tt38 | 1232.282 | 1411.277 | 0.873x | 0.861-0.881x | 0.882x | 1.15-1.41x | NO | NO | 0.0156 | 12, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro | 804.864 | 683.349 | 1.178x | 1.148-1.201x | 1.180x | 0.94-1.10x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ctl_s2 | 804.864 | 1061.888 | 0.758x | 0.738-0.772x | 0.759x | 0.73-0.96x | yes | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ctl_s5 | 804.864 | 803.840 | 1.001x | 0.973-1.018x | 1.000x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | kernl | 804.864 | 956.075 | 0.842x | 0.822-0.856x | 0.836x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_clamp | 804.864 | 655.019 | 1.229x | 1.196-1.253x | 1.240x | 0.97-1.10x | NO | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 804.864 | 673.109 | 1.196x | 1.153-1.223x | 1.189x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 727.723 | 673.109 | 1.081x | 1.014-1.110x | 1.074x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_tt32 | 804.864 | 625.323 | 1.287x | 1.247-1.321x | 1.295x | 0.97-1.14x | NO | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 727.723 | 625.323 | 1.164x | 1.097-1.199x | 1.169x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 727.723 | 683.349 | 1.065x | 1.009-1.090x | 1.065x | 0.95-1.10x | yes | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 981.333 | 683.349 | 1.436x | 1.407-1.468x | 1.419x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | tt32 | 804.864 | 727.723 | 1.106x | 1.074-1.167x | 1.108x | 0.96-1.03x | NO | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_warm | tt38 | 804.864 | 981.333 | 0.820x | 0.797-0.837x | 0.831x | 0.97-1.11x | NO | NO | 0.0156 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro | 808.141 | 678.093 | 1.192x | 1.147-1.234x | 1.180x | 0.98-1.26x | yes | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ctl_s2 | 808.141 | 1075.405 | 0.751x | 0.731-0.770x | 0.746x | 0.66-0.80x | yes | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ctl_s5 | 808.141 | 805.478 | 1.003x | 0.972-1.036x | 0.991x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | kernl | 808.141 | 963.174 | 0.839x | 0.817-0.859x | 0.823x | 0.95-1.02x | NO | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_clamp | 808.141 | 658.022 | 1.228x | 1.190-1.268x | 1.210x | 0.98-1.27x | yes | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 808.141 | 666.829 | 1.212x | 1.170-1.250x | 1.172x | 0.98-1.36x | yes | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 731.341 | 666.829 | 1.097x | 1.054-1.137x | 1.061x | 0.98-1.37x | yes | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_tt32 | 808.141 | 620.544 | 1.302x | 1.265-1.349x | 1.293x | 0.98-1.34x | yes | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 731.341 | 620.544 | 1.179x | 1.139-1.228x | 1.171x | 0.98-1.35x | yes | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 731.341 | 678.093 | 1.079x | 1.033-1.123x | 1.068x | 0.98-1.27x | yes | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 954.163 | 678.093 | 1.407x | 1.361-1.472x | 1.384x | 0.90-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | tt32 | 808.141 | 731.341 | 1.105x | 1.069-1.141x | 1.105x | 0.96-1.02x | NO | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_64x128x32_w4_s4_cold | tt38 | 808.141 | 954.163 | 0.847x | 0.816-0.867x | 0.853x | 0.98-1.36x | NO | NO | 0.0156 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro | 3768.661 | 3472.725 | 1.085x | 0.960-1.206x | 1.074x | 0.94-1.03x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ctl_r64 | 3768.661 | 3775.829 | 0.998x | 0.885-1.118x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ctl_s2 | 3768.661 | 3771.733 | 0.999x | 0.891-1.099x | 0.998x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ctl_s5 | 3768.661 | 3408.213 | 1.106x | 0.972-1.193x | 1.087x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | kernl | 3768.661 | 4432.213 | 0.850x | 0.761-0.877x | 0.739x | 0.89-1.03x | NO | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_clamp | 3768.661 | 3768.661 | 1.000x | 0.888-1.094x | 0.998x | 0.80-1.03x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_tt32 | 3768.661 | 3595.605 | 1.048x | 0.927-1.161x | 1.052x | 0.97-1.14x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 3582.635 | 3595.605 | 0.996x | 0.917-1.119x | 1.017x | 0.97-1.29x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 3775.829 | 3472.725 | 1.087x | 0.970-1.207x | 1.074x | 0.94-1.03x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 3582.635 | 3472.725 | 1.032x | 0.950-1.162x | 1.039x | 0.97-1.17x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 9687.040 | 3472.725 | 2.789x | 2.561-3.085x | 2.800x | 0.97-1.29x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | tt32 | 3768.661 | 3582.635 | 1.052x | 0.919-1.141x | 1.034x | 0.84-1.03x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_warm | tt38 | 3768.661 | 9687.040 | 0.389x | 0.346-0.423x | 0.384x | 0.74-1.03x | NO | NO | 0.0156 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro | 3727.974 | 3494.912 | 1.067x | 0.967-1.236x | 1.073x | 0.97-1.43x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ctl_r64 | 3727.974 | 3770.163 | 0.989x | 0.876-1.070x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ctl_s2 | 3727.974 | 3754.189 | 0.993x | 0.895-1.135x | 1.002x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ctl_s5 | 3727.974 | 3411.763 | 1.093x | 0.986-1.265x | - | 0.97-1.46x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | kernl | 3727.974 | 4465.254 | 0.835x | 0.765-0.887x | 0.736x | 0.91-1.03x | NO | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_clamp | 3727.974 | 3754.394 | 0.993x | 0.898-1.131x | 0.995x | 0.93-1.24x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_tt32 | 3727.974 | 3599.360 | 1.036x | 0.922-1.189x | - | 0.97-1.46x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 3621.479 | 3599.360 | 1.006x | 0.880-1.133x | - | 0.98-1.67x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 3770.163 | 3494.912 | 1.079x | 1.027-1.242x | 1.072x | 0.97-1.43x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 3621.479 | 3494.912 | 1.036x | 0.922-1.177x | 1.039x | 0.98-1.64x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 9554.944 | 3494.912 | 2.734x | 2.632-3.087x | 2.799x | 0.97-1.34x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | tt32 | 3727.974 | 3621.479 | 1.029x | 0.924-1.191x | 1.032x | 0.84-1.02x | NO | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_16x16x64_w4_s2_cold | tt38 | 3727.974 | 9554.944 | 0.390x | 0.352-0.417x | 0.383x | 0.84-1.10x | NO | NO | 0.0156 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro | 945.493 | 1020.245 | 0.927x | 0.908-0.941x | 0.920x | 0.77-1.09x | yes | yes | 0 | 12, 8 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | kernl | 945.493 | 1181.013 | 0.801x | 0.786-0.814x | 0.785x | 0.81-1.03x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_clamp | 945.493 | 931.157 | 1.015x | 0.995-1.031x | 1.008x | 0.82-1.14x | yes | yes | 0 | 12, 8 | 168, 235 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_full_tt32 | 945.493 | 961.536 | 0.983x | 0.966-1.003x | 0.973x | 0.97-1.20x | yes | yes | 0 | 12, 8 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 915.115 | 961.536 | 0.952x | 0.940-0.976x | 0.967x | 0.97-1.38x | NO | yes | 0 | 12, 8 | 168, 207 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_tt32 | 945.493 | 961.536 | 0.983x | 0.963-0.999x | 0.976x | 0.55-1.03x | yes | yes | 0 | 12, 8 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_tt32_vs_tt32 | 915.115 | 961.536 | 0.952x | 0.937-0.973x | 0.970x | 0.68-1.03x | yes | yes | 0 | 12, 8 | 168, 176 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_vs_tt32 | 915.115 | 1020.245 | 0.897x | 0.884-0.917x | 0.914x | 0.95-1.25x | NO | yes | 0 | 12, 8 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | ro_vs_tt38 | 1122.987 | 1020.245 | 1.101x | 1.084-1.132x | 1.096x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 211, 233 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | tt32 | 945.493 | 915.115 | 1.033x | 1.005-1.050x | 1.006x | 0.78-1.03x | NO | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_warm | tt38 | 945.493 | 1122.987 | 0.842x | 0.813-0.856x | 0.839x | 0.97-1.20x | NO | NO | 0.0156 | 12, 8 | 168, 211 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro | 937.370 | 1010.074 | 0.928x | 0.911-0.942x | 0.930x | 0.92-1.03x | yes | yes | 0 | 12, 8 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | kernl | 937.370 | 1183.334 | 0.792x | 0.780-0.805x | 0.780x | 0.83-0.99x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_clamp | 937.370 | 920.781 | 1.018x | 0.998-1.032x | 1.029x | 0.95-1.06x | yes | yes | 0 | 12, 8 | 168, 235 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_full_tt32 | 937.370 | 954.163 | 0.982x | 0.969-1.004x | 0.979x | 0.97-1.25x | yes | yes | 0 | 12, 8 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 909.517 | 954.163 | 0.953x | 0.942-0.974x | 0.957x | 1.03-1.49x | NO | yes | 0 | 12, 8 | 168, 207 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_tt32 | 937.370 | 950.682 | 0.986x | 0.967-1.000x | 0.997x | 0.67-1.05x | yes | yes | 0 | 12, 8 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_tt32_vs_tt32 | 909.517 | 950.682 | 0.957x | 0.940-0.970x | 0.974x | 0.81-1.17x | yes | yes | 0 | 12, 8 | 168, 176 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_vs_tt32 | 909.517 | 1010.074 | 0.900x | 0.885-0.914x | 0.909x | 1.03-1.18x | NO | yes | 0 | 12, 8 | 168, 233 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | ro_vs_tt38 | 1114.112 | 1010.074 | 1.103x | 1.079-1.117x | 1.105x | 0.59-1.03x | NO | yes | 0 | 8, 8 | 211, 233 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | tt32 | 937.370 | 909.517 | 1.031x | 1.010-1.050x | 1.023x | 0.81-0.97x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x32x32_w4_s4_cold | tt38 | 937.370 | 1114.112 | 0.841x | 0.827-0.861x | 0.841x | 0.97-1.57x | NO | NO | 0.0156 | 12, 8 | 168, 211 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro | 875.179 | 907.947 | 0.964x | 0.945-0.983x | 0.966x | 0.71-0.91x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | kernl | 875.179 | 1054.379 | 0.830x | 0.817-0.847x | 0.833x | 0.86-0.95x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_clamp | 875.179 | 862.891 | 1.014x | 0.994-1.035x | 1.017x | 0.70-0.89x | NO | yes | 0 | 8, 8 | 255, 252 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_full_tt32 | 875.179 | 735.232 | 1.190x | 1.166-1.216x | 1.202x | 0.97-1.15x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 831.488 | 735.232 | 1.131x | 1.109-1.152x | 1.131x | 0.90-1.09x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_tt32 | 875.179 | 643.413 | 1.360x | 1.333-1.389x | 1.378x | 1.08-1.23x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_tt32_vs_tt32 | 831.488 | 643.413 | 1.292x | 1.267-1.315x | 1.296x | 1.02-1.14x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_vs_tt32 | 831.488 | 907.947 | 0.916x | 0.898-0.930x | 0.908x | 0.66-0.86x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | ro_vs_tt38 | 856.747 | 907.947 | 0.944x | 0.925-0.964x | 0.926x | 0.58-0.82x | NO | yes | 0 | 8, 8 | 255, 254 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | tt32 | 875.179 | 831.488 | 1.053x | 1.032-1.076x | 1.063x | 1.03-1.11x | yes | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_warm | tt38 | 875.179 | 856.747 | 1.022x | 0.996-1.045x | 1.044x | 1.08-1.24x | NO | NO | 0.0156 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro | 875.520 | 911.974 | 0.960x | 0.943-0.980x | 0.955x | 0.82-0.93x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | kernl | 875.520 | 1057.792 | 0.828x | 0.813-0.844x | 0.819x | 0.88-0.96x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_clamp | 875.520 | 870.195 | 1.006x | 0.988-1.025x | 1.004x | 0.81-0.92x | NO | yes | 0 | 8, 8 | 255, 252 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_full_tt32 | 875.520 | 742.400 | 1.179x | 1.163-1.203x | 1.174x | 1.12-1.23x | yes | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 833.536 | 742.400 | 1.123x | 1.105-1.146x | 1.116x | 1.05-1.18x | yes | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_tt32 | 875.520 | 645.325 | 1.357x | 1.334-1.388x | 1.365x | 1.34-1.41x | yes | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_tt32_vs_tt32 | 833.536 | 645.325 | 1.292x | 1.267-1.323x | 1.297x | 1.26-1.34x | yes | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_vs_tt32 | 833.536 | 911.974 | 0.914x | 0.896-0.934x | 0.907x | 0.77-0.89x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | ro_vs_tt38 | 847.258 | 911.974 | 0.929x | 0.911-0.951x | 0.918x | 0.58-0.68x | NO | yes | 0 | 8, 8 | 255, 254 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | tt32 | 875.520 | 833.536 | 1.050x | 1.030-1.072x | 1.052x | 1.01-1.10x | yes | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_128x64x32_w4_s4_cold | tt38 | 875.520 | 847.258 | 1.033x | 1.011-1.056x | 1.040x | 1.35-1.49x | NO | NO | 0.0156 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro | 50.290 | 63.336 | 0.794x | 0.779-0.810x | 0.784x | 0.71-1.03x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ctl_s2 | 50.290 | 52.338 | 0.961x | 0.943-0.980x | 0.972x | 0.73-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ctl_s5 | 50.290 | 50.366 | 0.998x | 0.983-1.018x | 0.998x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | kernl | 50.290 | 51.845 | 0.970x | 0.954-0.987x | 0.971x | 0.89-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro_clamp | 50.290 | 62.464 | 0.805x | 0.791-0.819x | 0.805x | 0.73-1.05x | yes | yes | 0 | 10, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32 | 50.290 | 71.794 | 0.700x | 0.691-0.716x | 0.692x | 0.52-0.94x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 74.107 | 71.794 | 1.032x | 1.016-1.051x | 1.029x | 0.88-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 74.107 | 63.336 | 1.170x | 1.145-1.189x | 1.165x | 1.19-1.54x | NO | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 68.418 | 63.336 | 1.080x | 1.059-1.098x | 1.070x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | tt32 | 50.290 | 74.107 | 0.679x | 0.669-0.693x | 0.672x | 0.56-0.85x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_warm | tt38 | 50.290 | 68.418 | 0.735x | 0.724-0.749x | 0.732x | 0.90-1.14x | NO | NO | 0.00391 | 10, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro | 55.706 | 59.392 | 0.938x | 0.894-0.958x | 0.843x | 0.74-0.90x | NO | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ctl_s2 | 55.706 | 66.150 | 0.842x | 0.825-0.854x | 1.038x | 0.68-0.83x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ctl_s5 | 55.706 | 55.706 | 1.000x | 0.982-1.015x | 1.003x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | kernl | 55.706 | 57.958 | 0.961x | 0.941-0.975x | 1.188x | 0.90-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro_clamp | 55.706 | 58.163 | 0.958x | 0.906-0.982x | 0.869x | 0.82-0.99x | yes | yes | 0 | 10, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32 | 55.706 | 76.800 | 0.725x | 0.701-0.747x | 0.680x | 0.58-0.72x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 77.619 | 76.800 | 1.011x | 0.977-1.038x | 0.989x | 1.05-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 77.619 | 59.392 | 1.307x | 1.246-1.332x | 1.227x | 1.33-1.48x | NO | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 70.246 | 59.392 | 1.183x | 1.133-1.210x | 1.090x | 0.53-0.90x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | tt32 | 55.706 | 77.619 | 0.718x | 0.706-0.731x | 0.688x | 0.54-0.67x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s5_cold | tt38 | 55.706 | 70.246 | 0.793x | 0.777-0.804x | 0.774x | 0.97-1.41x | NO | NO | 0.00391 | 10, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro | 65.331 | 64.471 | 1.013x | 1.004-1.024x | - | 0.77-1.09x | yes | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ctl_s2 | 65.331 | 52.224 | 1.251x | 1.243-1.262x | 1.510x | 0.97-1.50x | yes | yes | 0 | 8, 10 | 165, 162 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ctl_s5 | 65.331 | 65.372 | 0.999x | 0.989-1.009x | 1.006x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | kernl | 65.331 | 66.888 | 0.977x | 0.971-0.983x | 0.997x | 0.94-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro_clamp | 65.331 | 65.208 | 1.002x | 0.987-1.013x | 0.991x | 0.65-1.10x | yes | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32 | 65.331 | 56.320 | 1.160x | 1.154-1.168x | 1.190x | 0.97-1.29x | yes | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 56.279 | 56.320 | 0.999x | 0.993-1.004x | 1.006x | 0.97-1.37x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 56.279 | 64.471 | 0.873x | 0.865-0.881x | - | 0.85-1.16x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 67.625 | 64.471 | 1.049x | 1.041-1.057x | - | 0.75-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | tt32 | 65.331 | 56.279 | 1.161x | 1.154-1.171x | 1.184x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_warm | tt38 | 65.331 | 67.625 | 0.966x | 0.961-0.973x | 0.979x | 0.97-1.29x | NO | NO | 0.00391 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro | 70.042 | 66.150 | 1.059x | 1.040-1.082x | - | 0.98-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ctl_s2 | 70.042 | 60.211 | 1.163x | 1.149-1.177x | 1.502x | 1.05-1.41x | yes | yes | 0 | 8, 10 | 165, 162 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ctl_s5 | 70.042 | 70.042 | 1.000x | 0.969-1.021x | 1.021x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | kernl | 70.042 | 79.258 | 0.884x | 0.871-0.896x | 0.874x | 0.94-1.01x | NO | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro_clamp | 70.042 | 69.222 | 1.012x | 0.991-1.036x | 1.039x | 0.83-1.36x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32 | 70.042 | 62.464 | 1.121x | 1.104-1.135x | 1.145x | 1.05-1.39x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 62.464 | 62.464 | 1.000x | 0.990-1.010x | 0.997x | 1.10-1.49x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 62.464 | 66.150 | 0.944x | 0.933-0.962x | - | 1.06-1.12x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 70.451 | 66.150 | 1.065x | 1.052-1.085x | - | 0.58-1.00x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | tt32 | 70.042 | 62.464 | 1.121x | 1.104-1.135x | 1.149x | 0.90-0.99x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_32x64x32_w2_s5_cold | tt38 | 70.042 | 70.451 | 0.994x | 0.980-1.006x | - | 1.05-1.74x | NO | NO | 0.00391 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro | 52.306 | 66.396 | 0.788x | 0.783-0.792x | 0.780x | 0.69-0.86x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ctl_s2 | 52.306 | 52.388 | 0.998x | 0.992-1.009x | 0.998x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ctl_s5 | 52.306 | 50.381 | 1.038x | 1.031-1.046x | 1.040x | 0.97-1.34x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | kernl | 52.306 | 55.132 | 0.949x | 0.941-0.955x | 1.116x | 0.88-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro_clamp | 52.306 | 71.926 | 0.727x | 0.721-0.731x | 0.717x | 0.70-0.93x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32 | 52.306 | 50.545 | 1.035x | 1.027-1.044x | 1.035x | 0.97-1.20x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 54.518 | 50.545 | 1.079x | 1.066-1.087x | 0.899x | 0.86-1.09x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 54.518 | 66.396 | 0.821x | 0.812-0.825x | 0.678x | 0.58-0.86x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 79.913 | 66.396 | 1.204x | 1.182-1.230x | 1.331x | 0.80-0.89x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | tt32 | 52.306 | 54.518 | 0.959x | 0.954-0.970x | 1.152x | 0.97-1.21x | NO | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_warm | tt38 | 52.306 | 79.913 | 0.655x | 0.640-0.667x | 0.586x | 0.81-1.02x | NO | NO | 0.00391 | 10, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro | 66.150 | 75.776 | 0.873x | 0.861-0.895x | 0.676x | 0.65-0.80x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ctl_s2 | 66.150 | 65.946 | 1.003x | 0.994-1.016x | 1.007x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ctl_s5 | 66.150 | 55.501 | 1.192x | 1.184-1.204x | 0.972x | 1.22-1.44x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | kernl | 66.150 | 69.222 | 0.956x | 0.950-0.967x | 0.951x | 0.90-0.98x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro_clamp | 66.150 | 81.920 | 0.807x | 0.799-0.821x | 0.782x | 0.75-0.93x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32 | 66.150 | 58.163 | 1.137x | 1.130-1.148x | 1.165x | 1.09-1.20x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 68.403 | 58.163 | 1.176x | 1.165-1.191x | 1.201x | 0.99-1.07x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 68.403 | 75.776 | 0.903x | 0.888-0.928x | 0.697x | 0.60-0.70x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 95.642 | 75.776 | 1.262x | 1.235-1.298x | 1.024x | 0.67-0.91x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | tt32 | 66.150 | 68.403 | 0.967x | 0.955-0.979x | 0.970x | 1.05-1.17x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x32x32_w2_s2_cold | tt38 | 66.150 | 95.642 | 0.692x | 0.684-0.703x | 0.661x | 0.85-1.00x | NO | NO | 0.00391 | 10, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro | 44.155 | 52.429 | 0.842x | 0.836-0.847x | 1.040x | 0.94-1.03x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ctl_s2 | 44.155 | 49.398 | 0.894x | 0.887-0.906x | 0.901x | 0.75-0.86x | NO | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ctl_s5 | 44.155 | 44.523 | 0.992x | 0.984-1.007x | 1.009x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | kernl | 44.155 | 49.152 | 0.898x | 0.891-0.903x | 0.910x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_clamp | 44.155 | 47.555 | 0.929x | 0.922-0.934x | 0.944x | 0.97-1.08x | NO | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 44.155 | 43.295 | 1.020x | 1.011-1.026x | 1.038x | 0.97-1.15x | yes | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 47.636 | 43.295 | 1.100x | 1.085-1.108x | 1.101x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32 | 44.155 | 44.032 | 1.003x | 0.991-1.017x | 1.026x | 0.97-1.14x | yes | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 47.636 | 44.032 | 1.082x | 1.063-1.099x | 1.087x | 0.97-1.15x | yes | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 47.636 | 52.429 | 0.909x | 0.896-0.915x | 1.102x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 70.124 | 52.429 | 1.337x | 1.305-1.352x | 1.338x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | tt32 | 44.155 | 47.636 | 0.927x | 0.917-0.941x | 0.943x | 0.96-1.03x | NO | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_warm | tt38 | 44.155 | 70.124 | 0.630x | 0.621-0.646x | 0.777x | 0.97-1.06x | NO | NO | 0.00391 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro | 53.862 | 52.838 | 1.019x | 1.004-1.031x | 1.030x | 1.10-1.24x | NO | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ctl_s2 | 53.862 | 66.765 | 0.807x | 0.796-0.812x | 1.003x | 0.67-0.81x | NO | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ctl_s5 | 53.862 | 53.862 | 1.000x | 0.989-1.011x | 1.001x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | kernl | 53.862 | 57.344 | 0.939x | 0.926-0.953x | 1.196x | 0.95-1.02x | NO | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_clamp | 53.862 | 49.357 | 1.091x | 1.079-1.100x | 1.104x | 1.18-1.25x | NO | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 53.862 | 46.899 | 1.148x | 1.140-1.163x | 1.179x | 1.18-1.34x | NO | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 53.453 | 46.899 | 1.140x | 1.135-1.159x | 1.170x | 1.18-1.35x | NO | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32 | 53.862 | 46.899 | 1.148x | 1.135-1.158x | 1.177x | 1.18-1.32x | NO | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 53.453 | 46.899 | 1.140x | 1.130-1.154x | 1.168x | 1.18-1.33x | NO | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 53.453 | 52.838 | 1.012x | 1.000-1.027x | 1.022x | 1.12-1.24x | NO | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 68.608 | 52.838 | 1.298x | 1.281-1.316x | 1.044x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | tt32 | 53.862 | 53.453 | 1.008x | 0.992-1.015x | 1.008x | 0.96-1.02x | yes | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_64x128x32_w4_s4_cold | tt38 | 53.862 | 68.608 | 0.785x | 0.774-0.793x | 0.987x | 1.17-1.24x | NO | NO | 0.00391 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro | 162.645 | 162.475 | 1.001x | 0.977-1.019x | 1.002x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ctl_r64 | 162.645 | 162.816 | 0.999x | 0.976-1.023x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ctl_s2 | 162.645 | 163.157 | 0.997x | 0.977-1.017x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ctl_s5 | 162.645 | 163.840 | 0.993x | 0.967-1.012x | 0.997x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | kernl | 162.645 | 163.328 | 0.996x | 0.973-1.014x | 0.997x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_clamp | 162.645 | 168.619 | 0.965x | 0.944-0.981x | 0.958x | 0.75-1.04x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32 | 162.645 | 165.717 | 0.981x | 0.960-1.006x | 0.984x | 0.97-1.13x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 168.789 | 165.717 | 1.019x | 1.003-1.042x | 1.023x | 0.97-1.34x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 162.816 | 162.475 | 1.002x | 0.978-1.019x | 1.002x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 168.789 | 162.475 | 1.039x | 1.021-1.055x | 1.042x | 0.97-1.24x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 436.565 | 162.475 | 2.687x | 2.616-2.729x | 2.123x | 0.97-1.26x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | tt32 | 162.645 | 168.789 | 0.964x | 0.943-0.981x | 0.962x | 0.81-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_warm | tt38 | 162.645 | 436.565 | 0.373x | 0.364-0.383x | 0.472x | 0.73-1.03x | NO | NO | 0.00195 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro | 167.322 | 165.478 | 1.011x | 0.943-1.077x | 1.007x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ctl_r64 | 167.322 | 166.912 | 1.002x | 0.938-1.069x | 1.001x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ctl_s2 | 167.322 | 166.912 | 1.002x | 0.938-1.069x | 0.997x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ctl_s5 | 167.322 | 167.731 | 0.998x | 0.933-1.066x | - | 0.97-1.49x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | kernl | 167.322 | 165.478 | 1.011x | 0.945-1.075x | 1.006x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_clamp | 167.322 | 172.851 | 0.968x | 0.902-1.033x | 0.953x | 0.87-1.16x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32 | 167.322 | 166.093 | 1.007x | 0.939-1.076x | - | 0.97-1.49x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 176.742 | 166.093 | 1.064x | 0.999-1.138x | - | 1.05-1.77x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 166.912 | 165.478 | 1.009x | 0.943-1.075x | 1.007x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 176.742 | 165.478 | 1.068x | 1.004-1.139x | 1.064x | 1.05-1.62x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 430.285 | 165.478 | 2.600x | 2.421-2.789x | 2.098x | 0.97-1.30x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | tt32 | 167.322 | 176.742 | 0.947x | 0.885-1.005x | 0.946x | 0.81-0.95x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k1024_16x16x64_w4_s2_cold | tt38 | 167.322 | 430.285 | 0.389x | 0.361-0.417x | 0.480x | 0.83-1.08x | NO | NO | 0.00195 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro | 188.928 | 224.384 | 0.842x | 0.805-0.863x | 0.853x | 0.70-1.03x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ctl_s2 | 188.928 | 234.752 | 0.805x | 0.792-0.811x | 0.796x | 0.72-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ctl_s5 | 188.928 | 189.184 | 0.999x | 0.989-1.013x | 0.999x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | kernl | 188.928 | 201.088 | 0.940x | 0.930-0.948x | 0.930x | 0.89-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro_clamp | 188.928 | 209.152 | 0.903x | 0.872-0.916x | 0.917x | 0.73-1.05x | yes | yes | 0 | 10, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32 | 188.928 | 286.336 | 0.660x | 0.649-0.675x | 0.647x | 0.51-0.93x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 291.968 | 286.336 | 1.020x | 0.996-1.041x | 1.005x | 0.87-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 291.968 | 224.384 | 1.301x | 1.237-1.333x | 1.326x | 1.20-1.57x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 258.944 | 224.384 | 1.154x | 1.097-1.182x | 1.175x | 0.76-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | tt32 | 188.928 | 291.968 | 0.647x | 0.642-0.657x | 0.643x | 0.54-0.84x | yes | yes | 0 | 10, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_warm | tt38 | 188.928 | 258.944 | 0.730x | 0.724-0.741x | 0.726x | 0.89-1.15x | NO | NO | 0.0156 | 10, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro | 196.403 | 223.437 | 0.879x | 0.821-0.915x | 0.871x | 0.73-0.89x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ctl_s2 | 196.403 | 243.917 | 0.805x | 0.762-0.849x | 0.798x | 0.67-0.82x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ctl_s5 | 196.403 | 196.403 | 1.000x | 0.944-1.057x | 0.998x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | kernl | 196.403 | 207.462 | 0.947x | 0.890-0.998x | 0.945x | 0.90-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro_clamp | 196.403 | 211.763 | 0.927x | 0.866-0.958x | 0.876x | 0.81-0.99x | yes | yes | 0 | 10, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32 | 196.403 | 274.637 | 0.715x | 0.661-0.754x | 0.663x | 0.57-0.71x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 285.491 | 274.637 | 1.040x | 0.959-1.104x | 0.990x | 1.05-1.11x | NO | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 285.491 | 223.437 | 1.278x | 1.191-1.339x | 1.301x | 1.34-1.49x | NO | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 254.566 | 223.437 | 1.139x | 1.060-1.188x | 1.141x | 0.51-0.89x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | tt32 | 196.403 | 285.491 | 0.688x | 0.646-0.729x | 0.670x | 0.53-0.66x | NO | yes | 0 | 10, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s5_cold | tt38 | 196.403 | 254.566 | 0.772x | 0.728-0.819x | 0.763x | 0.97-1.43x | NO | NO | 0.0156 | 10, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro | 258.688 | 245.888 | 1.052x | 1.039-1.062x | 1.035x | 0.77-1.10x | yes | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ctl_s2 | 258.688 | 206.080 | 1.255x | 1.246-1.264x | 1.260x | 0.97-1.53x | yes | yes | 0 | 8, 10 | 165, 162 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ctl_s5 | 258.688 | 259.200 | 0.998x | 0.989-1.006x | 0.991x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | kernl | 258.688 | 275.328 | 0.940x | 0.931-0.946x | 0.934x | 0.93-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro_clamp | 258.688 | 255.488 | 1.013x | 1.000-1.030x | 1.005x | 0.65-1.10x | yes | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32 | 258.688 | 208.512 | 1.241x | 1.229-1.250x | 1.245x | 0.97-1.31x | yes | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 214.144 | 208.512 | 1.027x | 1.022-1.031x | 1.025x | 0.97-1.39x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 214.144 | 245.888 | 0.871x | 0.863-0.876x | 0.852x | 0.85-1.17x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 249.984 | 245.888 | 1.017x | 1.008-1.022x | 0.991x | 0.75-1.03x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | tt32 | 258.688 | 214.144 | 1.208x | 1.198-1.217x | 1.215x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_warm | tt38 | 258.688 | 249.984 | 1.035x | 1.027-1.043x | 1.045x | 0.97-1.31x | yes | NO | 0.0156 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro | 269.926 | 252.109 | 1.071x | 1.023-1.120x | - | 0.98-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ctl_s2 | 269.926 | 217.498 | 1.241x | 1.189-1.302x | 1.269x | 1.05-1.42x | yes | yes | 0 | 8, 10 | 165, 162 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ctl_s5 | 269.926 | 270.336 | 0.998x | 0.955-1.022x | 1.006x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | kernl | 269.926 | 287.130 | 0.940x | 0.900-0.962x | 0.944x | 0.94-1.01x | NO | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro_clamp | 269.926 | 241.664 | 1.117x | 1.063-1.158x | 1.119x | 0.83-1.38x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32 | 269.926 | 222.413 | 1.214x | 1.161-1.278x | 1.237x | 1.05-1.40x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 219.750 | 222.413 | 0.988x | 0.941-1.036x | 1.003x | 1.10-1.51x | NO | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 219.750 | 252.109 | 0.872x | 0.829-0.907x | - | 1.06-1.13x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 249.242 | 252.109 | 0.989x | 0.935-1.029x | - | 0.57-1.00x | yes | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | tt32 | 269.926 | 219.750 | 1.228x | 1.175-1.295x | 1.233x | 0.90-0.99x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_32x64x32_w2_s5_cold | tt38 | 269.926 | 249.242 | 1.083x | 1.036-1.150x | - | 1.05-1.78x | yes | NO | 0.0156 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro | 230.059 | 284.672 | 0.808x | 0.793-0.821x | 0.802x | 0.68-0.85x | yes | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ctl_s2 | 230.059 | 229.888 | 1.001x | 0.985-1.018x | 0.998x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ctl_s5 | 230.059 | 186.197 | 1.236x | 1.215-1.251x | 1.250x | 0.97-1.36x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | kernl | 230.059 | 240.981 | 0.955x | 0.939-0.971x | 0.954x | 0.88-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro_clamp | 230.059 | 310.101 | 0.742x | 0.721-0.762x | 0.749x | 0.70-0.93x | yes | yes | 0 | 10, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32 | 230.059 | 195.925 | 1.174x | 1.155-1.194x | 1.179x | 0.97-1.21x | yes | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 245.760 | 195.925 | 1.254x | 1.221-1.272x | 1.270x | 0.85-1.09x | NO | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 245.760 | 284.672 | 0.863x | 0.839-0.874x | 0.864x | 0.57-0.85x | NO | yes | 0 | 10, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 357.888 | 284.672 | 1.257x | 1.194-1.295x | 1.195x | 0.80-0.88x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | tt32 | 230.059 | 245.760 | 0.936x | 0.924-0.961x | 0.928x | 0.97-1.22x | NO | yes | 0 | 10, 10 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_warm | tt38 | 230.059 | 357.888 | 0.643x | 0.624-0.675x | 0.671x | 0.81-1.02x | NO | NO | 0.0156 | 10, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro | 240.230 | 289.997 | 0.828x | 0.798-0.851x | 0.821x | 0.64-0.80x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ctl_s2 | 240.230 | 240.026 | 1.001x | 0.968-1.037x | 0.995x | 0.97-1.03x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ctl_s5 | 240.230 | 193.126 | 1.244x | 1.204-1.279x | 1.249x | 1.23-1.46x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | kernl | 240.230 | 252.518 | 0.951x | 0.923-0.982x | 0.953x | 0.90-0.98x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro_clamp | 240.230 | 319.078 | 0.753x | 0.720-0.779x | 0.746x | 0.75-0.92x | yes | yes | 0 | 10, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32 | 240.230 | 208.691 | 1.151x | 1.113-1.185x | 1.157x | 1.10-1.21x | yes | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 252.314 | 208.691 | 1.209x | 1.176-1.237x | 1.211x | 1.00-1.07x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 252.314 | 289.997 | 0.870x | 0.843-0.889x | 0.859x | 0.59-0.70x | NO | yes | 0 | 10, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 365.773 | 289.997 | 1.261x | 1.218-1.321x | 1.245x | 0.67-0.90x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | tt32 | 240.230 | 252.314 | 0.952x | 0.926-0.979x | 0.955x | 1.05-1.18x | NO | yes | 0 | 10, 10 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x32x32_w2_s2_cold | tt38 | 240.230 | 365.773 | 0.657x | 0.623-0.678x | 0.659x | 0.85-1.00x | NO | NO | 0.0156 | 10, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro | 173.056 | 191.374 | 0.904x | 0.893-0.918x | 0.888x | 0.94-1.03x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ctl_s2 | 173.056 | 236.544 | 0.732x | 0.724-0.740x | 0.725x | 0.74-0.86x | NO | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ctl_s5 | 173.056 | 173.739 | 0.996x | 0.988-1.007x | 0.994x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | kernl | 173.056 | 197.291 | 0.877x | 0.869-0.888x | 0.877x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_clamp | 173.056 | 171.691 | 1.008x | 0.997-1.026x | 1.002x | 0.97-1.08x | yes | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 173.056 | 158.151 | 1.094x | 1.080-1.110x | 1.085x | 0.97-1.16x | yes | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 180.224 | 158.151 | 1.140x | 1.116-1.155x | 1.135x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32 | 173.056 | 160.654 | 1.077x | 1.058-1.097x | 1.074x | 0.97-1.14x | yes | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 180.224 | 160.654 | 1.122x | 1.093-1.142x | 1.123x | 0.97-1.16x | yes | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 180.224 | 191.374 | 0.942x | 0.923-0.955x | 0.928x | 0.95-1.03x | NO | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 263.168 | 191.374 | 1.375x | 1.326-1.430x | 1.354x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | tt32 | 173.056 | 180.224 | 0.960x | 0.951-0.978x | 0.957x | 0.96-1.03x | yes | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_warm | tt38 | 173.056 | 263.168 | 0.658x | 0.636-0.680x | 0.656x | 0.97-1.06x | NO | NO | 0.0156 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro | 182.886 | 177.766 | 1.029x | 0.997-1.074x | 1.027x | 1.11-1.25x | NO | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ctl_s2 | 182.886 | 246.170 | 0.743x | 0.721-0.770x | 0.740x | 0.66-0.80x | yes | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ctl_s5 | 182.886 | 184.934 | 0.989x | 0.959-1.023x | 0.989x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | kernl | 182.886 | 200.090 | 0.914x | 0.884-0.946x | 0.914x | 0.95-1.02x | NO | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_clamp | 182.886 | 163.021 | 1.122x | 1.087-1.169x | 1.129x | 1.19-1.26x | NO | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 182.886 | 156.672 | 1.167x | 1.134-1.221x | 1.173x | 1.19-1.35x | NO | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 186.368 | 156.672 | 1.190x | 1.158-1.251x | 1.206x | 1.20-1.37x | NO | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32 | 182.886 | 157.901 | 1.158x | 1.122-1.213x | 1.164x | 1.19-1.33x | NO | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 186.368 | 157.901 | 1.180x | 1.146-1.243x | 1.197x | 1.20-1.35x | NO | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 186.368 | 177.766 | 1.048x | 1.017-1.100x | 1.056x | 1.12-1.26x | NO | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 244.122 | 177.766 | 1.373x | 1.320-1.438x | 1.386x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | tt32 | 182.886 | 186.368 | 0.981x | 0.946-1.011x | 0.973x | 0.96-1.02x | yes | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_64x128x32_w4_s4_cold | tt38 | 182.886 | 244.122 | 0.749x | 0.723-0.779x | 0.741x | 1.18-1.25x | NO | NO | 0.0156 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro | 633.173 | 643.413 | 0.984x | 0.955-1.030x | 0.988x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ctl_r64 | 633.173 | 635.563 | 0.996x | 0.956-1.038x | 1.001x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ctl_s2 | 633.173 | 631.808 | 1.002x | 0.959-1.046x | 0.997x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ctl_s5 | 633.173 | 614.741 | 1.030x | 0.987-1.078x | 1.029x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | kernl | 633.173 | 630.101 | 1.005x | 0.971-1.053x | 1.012x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_clamp | 633.173 | 674.475 | 0.939x | 0.901-0.981x | 0.931x | 0.75-1.04x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32 | 633.173 | 647.509 | 0.978x | 0.942-1.012x | 0.985x | 0.97-1.14x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 669.696 | 647.509 | 1.034x | 1.004-1.063x | 1.038x | 0.97-1.34x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 635.563 | 643.413 | 0.988x | 0.964-1.030x | 0.987x | 0.91-1.05x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 669.696 | 643.413 | 1.041x | 1.018-1.083x | 1.041x | 0.97-1.25x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 1781.760 | 643.413 | 2.769x | 2.689-2.873x | 2.709x | 0.97-1.26x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | tt32 | 633.173 | 669.696 | 0.945x | 0.909-0.982x | 0.949x | 0.81-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_warm | tt38 | 633.173 | 1781.760 | 0.355x | 0.343-0.372x | 0.365x | 0.73-1.03x | NO | NO | 0.0156 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro | 645.734 | 635.290 | 1.016x | 0.966-1.042x | 1.009x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ctl_r64 | 645.734 | 638.771 | 1.011x | 0.969-1.044x | 1.002x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ctl_s2 | 645.734 | 644.710 | 1.002x | 0.961-1.047x | 1.004x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ctl_s5 | 645.734 | 615.014 | 1.050x | 1.006-1.099x | - | 0.97-1.50x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | kernl | 645.734 | 634.880 | 1.017x | 0.975-1.049x | 1.014x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_clamp | 645.734 | 682.803 | 0.946x | 0.901-0.982x | 0.941x | 0.87-1.16x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32 | 645.734 | 645.939 | 1.000x | 0.951-1.035x | - | 0.97-1.50x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 681.779 | 645.939 | 1.055x | 1.001-1.095x | - | 1.06-1.79x | NO | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 638.771 | 635.290 | 1.005x | 0.964-1.033x | 1.006x | 0.97-1.37x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 681.779 | 635.290 | 1.073x | 1.018-1.103x | 1.060x | 1.06-1.63x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 1772.544 | 635.290 | 2.790x | 2.679-2.863x | 2.716x | 0.97-1.30x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | tt32 | 645.734 | 681.779 | 0.947x | 0.908-0.989x | 0.951x | 0.81-0.95x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n1024_k4096_16x16x64_w4_s2_cold | tt38 | 645.734 | 1772.544 | 0.364x | 0.350-0.376x | 0.371x | 0.83-1.08x | NO | NO | 0.0156 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro | 206.438 | 178.176 | 1.159x | 1.156-1.165x | 0.993x | 0.97-1.20x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ctl_s2 | 206.438 | 236.442 | 0.873x | 0.869-0.879x | 0.888x | 0.72-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ctl_s5 | 206.438 | 206.438 | 1.000x | 0.995-1.004x | 1.010x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | kernl | 206.438 | 206.848 | 0.998x | 0.993-1.003x | 1.012x | 0.89-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro_clamp | 206.438 | 180.838 | 1.142x | 1.137-1.148x | 0.990x | 0.97-1.24x | yes | yes | 0 | 12, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32 | 206.438 | 198.656 | 1.039x | 1.036-1.044x | 0.900x | 0.83-1.04x | yes | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 199.373 | 198.656 | 1.004x | 0.999-1.009x | 1.006x | 0.88-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt32 | 199.373 | 178.176 | 1.119x | 1.115-1.127x | 1.111x | 0.97-1.28x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | ro_vs_tt38 | 229.478 | 178.176 | 1.288x | 1.286-1.293x | 1.272x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | tt32 | 206.438 | 199.373 | 1.035x | 1.029-1.041x | 0.894x | 0.88-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_warm | tt38 | 206.438 | 229.478 | 0.900x | 0.897-0.903x | 0.781x | 0.97-1.50x | NO | NO | 0.00391 | 12, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro | 206.643 | 183.091 | 1.129x | 1.072-1.185x | 0.992x | 0.97-1.39x | yes | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ctl_s2 | 206.643 | 243.507 | 0.849x | 0.808-0.889x | 0.855x | 0.67-0.82x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ctl_s5 | 206.643 | 206.643 | 1.000x | 0.951-1.052x | 1.001x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | kernl | 206.643 | 210.739 | 0.981x | 0.934-1.062x | 0.983x | 0.90-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro_clamp | 206.643 | 179.610 | 1.151x | 1.091-1.209x | 1.007x | 0.97-1.43x | yes | yes | 0 | 12, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32 | 206.643 | 196.813 | 1.050x | 0.996-1.104x | 0.919x | 0.93-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 194.970 | 196.813 | 0.991x | 0.908-1.041x | 0.992x | 0.97-1.11x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt32 | 194.970 | 183.091 | 1.065x | 0.978-1.118x | 1.070x | 0.97-1.49x | yes | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | ro_vs_tt38 | 223.437 | 183.091 | 1.220x | 1.107-1.287x | 1.225x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | tt32 | 206.643 | 194.970 | 1.060x | 1.008-1.153x | 0.927x | 0.85-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s5_cold | tt38 | 206.643 | 223.437 | 0.925x | 0.876-1.018x | 0.809x | 0.97-1.73x | NO | NO | 0.00391 | 12, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro | 201.421 | 189.850 | 1.061x | 1.047-1.074x | 1.056x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ctl_s2 | 201.421 | 210.534 | 0.957x | 0.950-0.973x | 1.132x | 0.91-1.03x | yes | yes | 0 | 8, 12 | 165, 162 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ctl_s5 | 201.421 | 201.523 | 0.999x | 0.987-1.012x | 1.001x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | kernl | 201.421 | 206.131 | 0.977x | 0.967-0.989x | 0.979x | 0.94-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro_clamp | 201.421 | 185.344 | 1.087x | 1.081-1.099x | 1.097x | 0.65-1.03x | NO | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32 | 201.421 | 187.802 | 1.073x | 1.069-1.086x | 1.081x | 0.97-1.11x | yes | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 185.344 | 187.802 | 0.987x | 0.984-0.991x | 0.987x | 0.97-1.22x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt32 | 185.344 | 189.850 | 0.976x | 0.964-0.980x | 0.964x | 0.85-1.03x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | ro_vs_tt38 | 236.339 | 189.850 | 1.245x | 1.229-1.263x | 1.228x | 0.75-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | tt32 | 201.421 | 185.344 | 1.087x | 1.083-1.100x | 1.095x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_warm | tt38 | 201.421 | 236.339 | 0.852x | 0.841-0.862x | 0.860x | 0.97-1.06x | NO | NO | 0.00391 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro | 207.667 | 196.198 | 1.058x | 0.976-1.140x | - | 0.97-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ctl_s2 | 207.667 | 225.280 | 0.922x | 0.847-0.988x | 1.089x | 0.76-1.03x | yes | yes | 0 | 8, 12 | 165, 162 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ctl_s5 | 207.667 | 207.872 | 0.999x | 0.921-1.066x | 0.999x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | kernl | 207.667 | 212.787 | 0.976x | 0.902-1.053x | 1.100x | 0.94-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro_clamp | 207.667 | 186.573 | 1.113x | 1.022-1.180x | 1.118x | 0.83-1.13x | yes | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32 | 207.667 | 188.416 | 1.102x | 1.009-1.195x | 1.112x | 0.97-1.40x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 185.549 | 188.416 | 0.985x | 0.907-1.069x | 0.984x | 0.97-1.51x | yes | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt32 | 185.549 | 196.198 | 0.946x | 0.877-1.020x | - | 0.97-1.13x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | ro_vs_tt38 | 228.966 | 196.198 | 1.167x | 1.055-1.256x | - | 0.75-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | tt32 | 207.667 | 185.549 | 1.119x | 1.032-1.205x | 1.131x | 0.90-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_32x64x32_w2_s5_cold | tt38 | 207.667 | 228.966 | 0.907x | 0.838-1.002x | - | 0.97-1.33x | NO | NO | 0.00391 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro | 227.442 | 211.285 | 1.076x | 1.061-1.094x | 0.872x | 0.97-1.25x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ctl_s2 | 227.442 | 227.101 | 1.002x | 0.987-1.017x | 0.994x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ctl_s5 | 227.442 | 197.860 | 1.150x | 1.134-1.168x | 1.095x | 0.97-1.36x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | kernl | 227.442 | 234.610 | 0.969x | 0.953-0.987x | 0.965x | 0.88-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro_clamp | 227.442 | 228.238 | 0.997x | 0.977-1.015x | 0.968x | 0.97-1.36x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32 | 227.442 | 208.441 | 1.091x | 1.076-1.108x | 1.076x | 0.97-1.21x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 203.435 | 208.441 | 0.976x | 0.963-0.985x | 0.977x | 0.85-1.09x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt32 | 203.435 | 211.285 | 0.963x | 0.949-0.972x | 0.792x | 0.92-1.12x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | ro_vs_tt38 | 262.030 | 211.285 | 1.240x | 1.223-1.255x | 1.014x | 0.80-1.03x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | tt32 | 227.442 | 203.435 | 1.118x | 1.105-1.138x | 1.101x | 0.97-1.22x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_warm | tt38 | 227.442 | 262.030 | 0.868x | 0.856-0.883x | 0.860x | 0.97-1.50x | NO | NO | 0.00391 | 12, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro | 238.182 | 219.546 | 1.085x | 1.031-1.122x | 0.876x | 1.04-1.25x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ctl_s2 | 238.182 | 238.387 | 0.999x | 0.948-1.055x | 0.995x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ctl_s5 | 238.182 | 201.523 | 1.182x | 1.122-1.224x | 1.164x | 1.23-1.46x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | kernl | 238.182 | 250.675 | 0.950x | 0.900-1.007x | 0.939x | 0.90-0.98x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro_clamp | 238.182 | 228.557 | 1.042x | 0.988-1.083x | 0.998x | 1.21-1.45x | NO | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32 | 238.182 | 213.197 | 1.117x | 1.063-1.182x | 1.108x | 1.10-1.21x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 211.354 | 213.197 | 0.991x | 0.939-1.051x | 0.991x | 1.00-1.07x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt32 | 211.354 | 219.546 | 0.963x | 0.910-0.997x | 0.783x | 0.96-1.10x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | ro_vs_tt38 | 263.578 | 219.546 | 1.201x | 1.126-1.243x | 0.980x | 0.67-0.90x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | tt32 | 238.182 | 211.354 | 1.127x | 1.071-1.189x | 1.118x | 1.05-1.18x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x32x32_w2_s2_cold | tt38 | 238.182 | 263.578 | 0.904x | 0.859-0.961x | 0.894x | 1.23-1.57x | NO | NO | 0.00391 | 12, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro | 160.597 | 136.704 | 1.175x | 1.164-1.198x | 1.167x | 0.94-1.12x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ctl_s2 | 160.597 | 185.003 | 0.868x | 0.857-0.883x | 0.876x | 0.73-0.95x | yes | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ctl_s5 | 160.597 | 160.683 | 0.999x | 0.991-1.016x | 0.985x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | kernl | 160.597 | 164.693 | 0.975x | 0.967-0.993x | 0.957x | 0.95-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_clamp | 160.597 | 129.792 | 1.237x | 1.229-1.253x | 1.183x | 0.97-1.13x | NO | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32 | 160.597 | 129.451 | 1.241x | 1.219-1.258x | 1.098x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 149.504 | 129.451 | 1.155x | 1.123-1.171x | 1.034x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32 | 160.597 | 125.440 | 1.280x | 1.267-1.311x | 1.120x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 149.504 | 125.440 | 1.192x | 1.167-1.221x | 1.054x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt32 | 149.504 | 136.704 | 1.094x | 1.072-1.115x | 1.099x | 0.95-1.12x | yes | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | ro_vs_tt38 | 188.928 | 136.704 | 1.382x | 1.364-1.408x | 1.359x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | tt32 | 160.597 | 149.504 | 1.074x | 1.063-1.097x | 1.062x | 0.96-1.03x | NO | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_warm | tt38 | 160.597 | 188.928 | 0.850x | 0.842-0.862x | 0.858x | 0.97-1.13x | NO | NO | 0.00391 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro | 166.093 | 136.602 | 1.216x | 1.139-1.289x | 1.193x | 0.99-1.26x | yes | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ctl_s2 | 166.093 | 199.885 | 0.831x | 0.777-0.886x | 0.829x | 0.66-0.80x | NO | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ctl_s5 | 166.093 | 166.093 | 1.000x | 0.934-1.071x | 0.980x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | kernl | 166.093 | 167.936 | 0.989x | 0.925-1.049x | 0.985x | 0.95-1.02x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_clamp | 166.093 | 135.782 | 1.223x | 1.147-1.291x | 1.197x | 0.99-1.26x | yes | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32 | 166.093 | 133.939 | 1.240x | 1.152-1.306x | 0.978x | 0.99-1.35x | yes | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 150.118 | 133.939 | 1.121x | 1.039-1.181x | 0.882x | 0.99-1.36x | yes | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32 | 166.093 | 124.928 | 1.330x | 1.248-1.407x | 1.118x | 0.99-1.33x | yes | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 150.118 | 124.928 | 1.202x | 1.126-1.272x | 1.009x | 0.99-1.35x | yes | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt32 | 150.118 | 136.602 | 1.099x | 1.027-1.166x | 1.077x | 0.99-1.27x | yes | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | ro_vs_tt38 | 177.152 | 136.602 | 1.297x | 1.200-1.382x | 1.269x | 0.88-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | tt32 | 166.093 | 150.118 | 1.106x | 1.035-1.184x | 1.108x | 0.96-1.02x | NO | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_64x128x32_w4_s4_cold | tt38 | 166.093 | 177.152 | 0.938x | 0.873-1.014x | 0.940x | 0.99-1.39x | NO | NO | 0.00391 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro | 641.024 | 647.851 | 0.989x | 0.955-1.024x | 0.990x | 0.94-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ctl_r64 | 641.024 | 641.024 | 1.000x | 0.966-1.035x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ctl_s2 | 641.024 | 640.000 | 1.002x | 0.966-1.038x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ctl_s5 | 641.024 | 649.557 | 0.987x | 0.953-1.021x | 0.992x | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | kernl | 641.024 | 639.659 | 1.002x | 0.966-1.037x | 1.006x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_clamp | 641.024 | 671.403 | 0.955x | 0.920-0.987x | 0.945x | 0.77-1.03x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32 | 641.024 | 659.456 | 0.972x | 0.927-1.006x | 0.981x | 0.97-1.14x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 666.624 | 659.456 | 1.011x | 0.964-1.048x | 1.014x | 0.97-1.30x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 641.024 | 647.851 | 0.989x | 0.955-1.025x | 0.990x | 0.94-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt32 | 666.624 | 647.851 | 1.029x | 0.993-1.067x | 1.023x | 0.97-1.15x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | ro_vs_tt38 | 1769.813 | 647.851 | 2.732x | 2.664-2.850x | 2.113x | 0.97-1.33x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | tt32 | 641.024 | 666.624 | 0.962x | 0.928-0.995x | 0.967x | 0.84-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_warm | tt38 | 641.024 | 1769.813 | 0.362x | 0.347-0.371x | 0.468x | 0.71-1.03x | NO | NO | 0.00195 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro | 653.107 | 648.806 | 1.007x | 0.952-1.033x | 1.000x | 0.97-1.42x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ctl_r64 | 653.107 | 646.554 | 1.010x | 0.966-1.036x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ctl_s2 | 653.107 | 651.264 | 1.003x | 0.959-1.040x | 1.000x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ctl_s5 | 653.107 | 648.806 | 1.007x | 0.951-1.043x | - | 0.97-1.43x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | kernl | 653.107 | 650.650 | 1.004x | 0.959-1.039x | 1.008x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_clamp | 653.107 | 677.683 | 0.964x | 0.912-0.989x | 0.947x | 0.89-1.19x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32 | 653.107 | 656.998 | 0.994x | 0.939-1.020x | - | 0.97-1.43x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 669.696 | 656.998 | 1.019x | 0.982-1.058x | - | 0.97-1.64x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 646.554 | 648.806 | 0.997x | 0.962-1.022x | 1.001x | 0.97-1.42x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt32 | 669.696 | 648.806 | 1.032x | 0.996-1.071x | 1.028x | 0.97-1.63x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | ro_vs_tt38 | 1778.893 | 648.806 | 2.742x | 2.650-2.814x | 2.109x | 0.97-1.38x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | tt32 | 653.107 | 669.696 | 0.975x | 0.922-1.001x | 0.974x | 0.84-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k1024_16x16x64_w4_s2_cold | tt38 | 653.107 | 1778.893 | 0.367x | 0.351-0.376x | 0.474x | 0.81-1.06x | NO | NO | 0.00195 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro | 803.499 | 671.061 | 1.197x | 1.179-1.213x | 1.189x | 0.97-1.20x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ctl_s2 | 803.499 | 1005.909 | 0.799x | 0.788-0.811x | 0.781x | 0.72-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ctl_s5 | 803.499 | 804.523 | 0.999x | 0.985-1.014x | 0.997x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | kernl | 803.499 | 836.267 | 0.961x | 0.951-0.978x | 0.953x | 0.89-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro_clamp | 803.499 | 670.037 | 1.199x | 1.181-1.215x | 1.208x | 0.97-1.24x | yes | yes | 0 | 12, 8 | 168, 239 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32 | 803.499 | 766.293 | 1.049x | 1.032-1.063x | 1.058x | 0.83-1.04x | NO | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro_tt32_vs_tt32 | 769.365 | 766.293 | 1.004x | 0.987-1.024x | 1.011x | 0.87-1.14x | yes | yes | 0 | 8, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt32 | 769.365 | 671.061 | 1.146x | 1.128-1.168x | 1.136x | 0.97-1.28x | yes | yes | 0 | 8, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | ro_vs_tt38 | 876.885 | 671.061 | 1.307x | 1.289-1.327x | 1.283x | 0.76-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | tt32 | 803.499 | 769.365 | 1.044x | 1.024-1.060x | 1.047x | 0.88-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_warm | tt38 | 803.499 | 876.885 | 0.916x | 0.901-0.927x | 0.927x | 0.97-1.50x | NO | NO | 0.0156 | 12, 8 | 168, 216 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro | 806.707 | 683.827 | 1.180x | 1.154-1.208x | 1.146x | 0.97-1.39x | yes | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ctl_s2 | 806.707 | 1019.699 | 0.791x | 0.774-0.805x | 0.772x | 0.67-0.82x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ctl_s5 | 806.707 | 800.563 | 1.008x | 0.977-1.023x | 0.976x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | kernl | 806.707 | 836.403 | 0.964x | 0.939-1.006x | 0.951x | 0.90-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro_clamp | 806.707 | 675.840 | 1.194x | 1.166-1.223x | 1.191x | 0.97-1.43x | yes | yes | 0 | 12, 8 | 168, 239 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32 | 806.707 | 766.157 | 1.053x | 1.029-1.082x | 1.067x | 0.93-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro_tt32_vs_tt32 | 769.229 | 766.157 | 1.004x | 0.975-1.036x | 1.033x | 0.97-1.11x | yes | yes | 0 | 8, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt32 | 769.229 | 683.827 | 1.125x | 1.094-1.157x | 1.109x | 0.97-1.49x | yes | yes | 0 | 8, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | ro_vs_tt38 | 876.339 | 683.827 | 1.282x | 1.220-1.312x | 1.226x | 0.76-1.03x | NO | yes | 0 | 8, 8 | 216, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | tt32 | 806.707 | 769.229 | 1.049x | 1.021-1.079x | 1.033x | 0.85-1.03x | NO | yes | 0 | 12, 8 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s5_cold | tt38 | 806.707 | 876.339 | 0.921x | 0.900-0.968x | 0.934x | 0.97-1.74x | NO | NO | 0.0156 | 12, 8 | 168, 216 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro | 843.776 | 783.019 | 1.078x | 1.063-1.090x | 1.068x | 0.77-1.03x | NO | yes | 0 | 8, 8 | 165, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ctl_s2 | 843.776 | 951.296 | 0.887x | 0.875-0.896x | 0.880x | 0.91-1.03x | NO | yes | 0 | 8, 12 | 165, 162 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ctl_s5 | 843.776 | 843.776 | 1.000x | 0.987-1.013x | 0.996x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | kernl | 843.776 | 877.227 | 0.962x | 0.947-0.975x | 0.960x | 0.93-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro_clamp | 843.776 | 722.261 | 1.168x | 1.155-1.186x | 1.189x | 0.64-1.03x | NO | yes | 0 | 8, 8 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32 | 843.776 | 737.621 | 1.144x | 1.127-1.163x | 1.159x | 0.97-1.11x | NO | yes | 0 | 8, 6 | 165, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro_tt32_vs_tt32 | 735.232 | 737.621 | 0.997x | 0.979-1.015x | 1.000x | 0.97-1.22x | yes | yes | 0 | 6, 6 | 168, 164 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt32 | 735.232 | 783.019 | 0.939x | 0.924-0.951x | 0.922x | 0.85-1.03x | yes | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | ro_vs_tt38 | 900.779 | 783.019 | 1.150x | 1.132-1.163x | 1.106x | 0.74-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | tt32 | 843.776 | 735.232 | 1.148x | 1.131-1.166x | 1.159x | 0.88-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_warm | tt38 | 843.776 | 900.779 | 0.937x | 0.925-0.952x | 0.966x | 0.97-1.06x | NO | NO | 0.0156 | 8, 6 | 165, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro | 843.162 | 784.589 | 1.075x | 1.056-1.090x | - | 0.97-1.08x | yes | yes | 0 | 8, 8 | 165, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ctl_s2 | 843.162 | 954.573 | 0.883x | 0.873-0.897x | 0.877x | 0.76-1.03x | yes | yes | 0 | 8, 12 | 165, 162 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ctl_s5 | 843.162 | 843.366 | 1.000x | 0.988-1.015x | 0.997x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | kernl | 843.162 | 877.978 | 0.960x | 0.948-0.983x | 0.969x | 0.94-1.03x | yes | yes | 0 | 8, 8 | 165, 165 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro_clamp | 843.162 | 718.234 | 1.174x | 1.159-1.192x | 1.186x | 0.83-1.13x | NO | yes | 0 | 8, 8 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32 | 843.162 | 730.522 | 1.154x | 1.133-1.180x | 1.176x | 0.97-1.40x | yes | yes | 0 | 8, 6 | 165, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro_tt32_vs_tt32 | 723.149 | 730.522 | 0.990x | 0.965-1.022x | 0.998x | 0.97-1.51x | yes | yes | 0 | 6, 6 | 168, 164 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt32 | 723.149 | 784.589 | 0.922x | 0.899-0.943x | - | 0.97-1.13x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | ro_vs_tt38 | 890.470 | 784.589 | 1.135x | 1.096-1.147x | - | 0.74-1.03x | NO | yes | 0 | 6, 8 | 168, 166 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | tt32 | 843.162 | 723.149 | 1.166x | 1.139-1.190x | 1.179x | 0.90-1.03x | NO | yes | 0 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_32x64x32_w2_s5_cold | tt38 | 843.162 | 890.470 | 0.947x | 0.937-0.977x | - | 0.97-1.34x | NO | NO | 0.0156 | 8, 6 | 165, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro | 975.872 | 814.421 | 1.198x | 1.174-1.227x | 1.210x | 0.97-1.25x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ctl_s2 | 975.872 | 976.555 | 0.999x | 0.986-1.015x | 1.003x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ctl_s5 | 975.872 | 761.173 | 1.282x | 1.259-1.306x | 1.299x | 0.97-1.36x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | kernl | 975.872 | 1075.883 | 0.907x | 0.889-0.923x | 0.915x | 0.88-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro_clamp | 975.872 | 886.443 | 1.101x | 1.084-1.126x | 1.112x | 0.97-1.36x | yes | yes | 0 | 12, 8 | 168, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32 | 975.872 | 825.685 | 1.182x | 1.160-1.206x | 1.197x | 0.97-1.22x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro_tt32_vs_tt32 | 814.763 | 825.685 | 0.987x | 0.967-1.006x | 0.993x | 0.85-1.09x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt32 | 814.763 | 814.421 | 1.000x | 0.978-1.024x | 1.004x | 0.92-1.12x | yes | yes | 0 | 12, 8 | 168, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | ro_vs_tt38 | 1043.456 | 814.421 | 1.281x | 1.255-1.313x | 1.286x | 0.80-1.03x | NO | yes | 0 | 8, 8 | 212, 234 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | tt32 | 975.872 | 814.763 | 1.198x | 1.180-1.218x | 1.205x | 0.97-1.22x | yes | yes | 0 | 12, 12 | 168, 168 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_warm | tt38 | 975.872 | 1043.456 | 0.935x | 0.920-0.950x | 0.941x | 0.97-1.51x | NO | NO | 0.0156 | 12, 8 | 168, 212 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro | 977.715 | 818.381 | 1.195x | 1.179-1.204x | 1.194x | 1.04-1.25x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ctl_s2 | 977.715 | 977.920 | 1.000x | 0.988-1.005x | 1.000x | 0.97-1.03x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ctl_s5 | 977.715 | 765.542 | 1.277x | 1.261-1.294x | 1.290x | 1.24-1.47x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | kernl | 977.715 | 1067.827 | 0.916x | 0.901-0.922x | 0.906x | 0.90-0.98x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro_clamp | 977.715 | 886.374 | 1.103x | 1.085-1.114x | 1.110x | 1.22-1.46x | NO | yes | 0 | 12, 8 | 168, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32 | 977.715 | 828.416 | 1.180x | 1.164-1.188x | 1.195x | 1.10-1.21x | yes | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro_tt32_vs_tt32 | 817.766 | 828.416 | 0.987x | 0.980-0.994x | 0.990x | 1.00-1.07x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt32 | 817.766 | 818.381 | 0.999x | 0.992-1.008x | 0.990x | 0.96-1.10x | yes | yes | 0 | 12, 8 | 168, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | ro_vs_tt38 | 1047.347 | 818.381 | 1.280x | 1.271-1.294x | 1.264x | 0.67-0.90x | NO | yes | 0 | 8, 8 | 212, 234 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | tt32 | 977.715 | 817.766 | 1.196x | 1.181-1.203x | 1.207x | 1.05-1.18x | NO | yes | 0 | 12, 12 | 168, 168 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x32x32_w2_s2_cold | tt38 | 977.715 | 1047.347 | 0.934x | 0.920-0.939x | 0.944x | 1.24-1.58x | NO | NO | 0.0156 | 12, 8 | 168, 212 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro | 623.616 | 505.173 | 1.234x | 1.196-1.253x | 1.229x | 0.94-1.12x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ctl_s2 | 623.616 | 812.373 | 0.768x | 0.748-0.782x | 0.762x | 0.73-0.95x | yes | yes | 0 | 8, 8 | 241, 238 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ctl_s5 | 623.616 | 626.005 | 0.996x | 0.968-1.017x | 0.990x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | kernl | 623.616 | 638.976 | 0.976x | 0.950-0.994x | 0.973x | 0.95-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_clamp | 623.616 | 492.885 | 1.265x | 1.233-1.287x | 1.250x | 0.97-1.13x | NO | yes | 0 | 8, 8 | 241, 253 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32 | 623.616 | 533.163 | 1.170x | 1.136-1.196x | 1.173x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 245 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_full_tt32_vs_tt32 | 571.733 | 533.163 | 1.072x | 1.044-1.096x | 1.072x | 0.97-1.17x | yes | yes | 0 | 8, 8 | 243, 245 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32 | 623.616 | 463.531 | 1.345x | 1.305-1.374x | 1.346x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 241, 242 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_tt32_vs_tt32 | 571.733 | 463.531 | 1.233x | 1.199-1.259x | 1.230x | 0.97-1.16x | NO | yes | 0 | 8, 8 | 243, 242 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt32 | 571.733 | 505.173 | 1.132x | 1.099-1.148x | 1.123x | 0.95-1.12x | NO | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | ro_vs_tt38 | 724.309 | 505.173 | 1.434x | 1.405-1.457x | 1.417x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | tt32 | 623.616 | 571.733 | 1.091x | 1.060-1.120x | 1.094x | 0.96-1.03x | NO | yes | 0 | 8, 8 | 241, 243 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_warm | tt38 | 623.616 | 724.309 | 0.861x | 0.835-0.876x | 0.867x | 0.97-1.14x | NO | NO | 0.0156 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro | 624.845 | 505.037 | 1.237x | 1.201-1.301x | 1.232x | 0.99-1.27x | yes | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ctl_s2 | 624.845 | 815.923 | 0.766x | 0.741-0.780x | 0.751x | 0.66-0.80x | yes | yes | 0 | 8, 8 | 241, 238 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ctl_s5 | 624.845 | 622.592 | 1.004x | 0.971-1.021x | 0.995x | 0.97-1.03x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | kernl | 624.845 | 639.590 | 0.977x | 0.945-0.995x | 0.969x | 0.95-1.02x | yes | yes | 0 | 8, 8 | 241, 241 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_clamp | 624.845 | 492.544 | 1.269x | 1.232-1.314x | 1.225x | 0.99-1.27x | yes | yes | 0 | 8, 8 | 241, 253 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32 | 624.845 | 532.480 | 1.173x | 1.132-1.191x | 1.163x | 0.99-1.36x | yes | yes | 0 | 8, 8 | 241, 245 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_full_tt32_vs_tt32 | 572.006 | 532.480 | 1.074x | 1.050-1.095x | 1.070x | 0.99-1.37x | yes | yes | 0 | 8, 8 | 243, 245 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32 | 624.845 | 459.571 | 1.360x | 1.311-1.452x | 1.346x | 0.99-1.34x | NO | yes | 0 | 8, 8 | 241, 242 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_tt32_vs_tt32 | 572.006 | 459.571 | 1.245x | 1.216-1.335x | 1.239x | 0.99-1.35x | yes | yes | 0 | 8, 8 | 243, 242 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt32 | 572.006 | 505.037 | 1.133x | 1.113-1.196x | 1.134x | 0.99-1.28x | yes | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | ro_vs_tt38 | 699.187 | 505.037 | 1.384x | 1.359-1.464x | 1.370x | 0.87-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | tt32 | 624.845 | 572.006 | 1.092x | 1.056-1.111x | 1.087x | 0.96-1.02x | NO | yes | 0 | 8, 8 | 241, 243 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_64x128x32_w4_s4_cold | tt38 | 624.845 | 699.187 | 0.894x | 0.863-0.910x | 0.899x | 0.99-1.40x | NO | NO | 0.0156 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro | 2749.099 | 2633.728 | 1.044x | 0.954-1.146x | 1.047x | 0.94-1.03x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ctl_r64 | 2749.099 | 2768.213 | 0.993x | 0.880-1.104x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ctl_s2 | 2749.099 | 2759.680 | 0.996x | 0.890-1.082x | 0.998x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ctl_s5 | 2749.099 | 2594.133 | 1.060x | 0.958-1.171x | - | 0.97-1.22x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | kernl | 2749.099 | 2858.667 | 0.962x | 0.865-1.041x | 0.961x | 0.89-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_clamp | 2749.099 | 2787.328 | 0.986x | 0.877-1.048x | 0.978x | 0.77-1.03x | yes | yes | 0 | 32, 24 | 64, 80 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32 | 2749.099 | 2685.611 | 1.024x | 0.918-1.152x | 1.032x | 0.97-1.14x | yes | yes | 0 | 32, 32 | 64, 63 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_tt32_vs_tt32 | 2674.688 | 2685.611 | 0.996x | 0.952-1.121x | 1.017x | 0.97-1.30x | yes | yes | 0 | 28, 32 | 68, 63 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_ctl_r64 | 2768.213 | 2633.728 | 1.051x | 0.972-1.157x | 1.049x | 0.94-1.03x | NO | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt32 | 2674.688 | 2633.728 | 1.016x | 0.989-1.115x | 1.032x | 0.97-1.15x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | ro_vs_tt38 | 7247.872 | 2633.728 | 2.752x | 2.654-3.054x | 2.765x | 0.97-1.33x | NO | yes | 0 | 20, 28 | 90, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | tt32 | 2749.099 | 2674.688 | 1.028x | 0.914-1.085x | 1.015x | 0.84-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_warm | tt38 | 2749.099 | 7247.872 | 0.379x | 0.334-0.404x | 0.379x | 0.71-1.03x | NO | NO | 0.0156 | 32, 20 | 64, 90 | warm |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro | 2774.221 | 2586.829 | 1.072x | 0.956-1.194x | 1.053x | 0.97-1.42x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ctl_r64 | 2774.221 | 2822.963 | 0.983x | 0.895-1.088x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ctl_s2 | 2774.221 | 2797.158 | 0.992x | 0.895-1.137x | 0.999x | 0.97-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ctl_s5 | 2774.221 | 2577.408 | 1.076x | 0.959-1.231x | - | 0.97-1.43x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | kernl | 2774.221 | 2895.053 | 0.958x | 0.864-1.066x | 0.961x | 0.91-1.03x | yes | yes | 0 | 32, 32 | 64, 64 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_clamp | 2774.221 | 2820.301 | 0.984x | 0.880-1.081x | 0.979x | 0.89-1.19x | yes | yes | 0 | 32, 24 | 64, 80 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32 | 2774.221 | 2676.326 | 1.037x | 0.915-1.156x | - | 0.97-1.43x | yes | yes | 0 | 32, 32 | 64, 63 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_tt32_vs_tt32 | 2772.582 | 2676.326 | 1.036x | 0.906-1.130x | - | 0.97-1.65x | yes | yes | 0 | 28, 32 | 68, 63 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_ctl_r64 | 2822.963 | 2586.829 | 1.091x | 0.987-1.188x | 1.054x | 0.97-1.42x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt32 | 2772.582 | 2586.829 | 1.072x | 0.947-1.168x | 1.037x | 0.97-1.64x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | ro_vs_tt38 | 7366.656 | 2586.829 | 2.848x | 2.627-3.132x | 2.773x | 0.97-1.38x | NO | yes | 0 | 20, 28 | 90, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | tt32 | 2774.221 | 2772.582 | 1.001x | 0.911-1.134x | 1.016x | 0.84-1.03x | yes | yes | 0 | 32, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m1024_n4096_k4096_16x16x64_w4_s2_cold | tt38 | 2774.221 | 7366.656 | 0.377x | 0.340-0.409x | 0.380x | 0.81-1.06x | NO | NO | 0.0156 | 32, 20 | 64, 90 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_warm | ro_bestcfg | 27.246 | 24.229 | 1.125x | 1.123-1.125x | 1.103x | 0.86-1.26x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_warm | ro_bestcfg_vs_tt32 | 27.083 | 24.229 | 1.118x | 1.116-1.119x | 1.062x | 0.94-1.33x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_warm | ro_bestcfg_vs_tt38 | 25.655 | 24.229 | 1.059x | 1.057-1.072x | 1.045x | 0.72-0.84x | NO | yes | 0 | 4, 4 | 211, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_cold | ro_bestcfg | 39.322 | 33.997 | 1.157x | 1.137-1.183x | 1.189x | 1.08-1.19x | yes | yes | 0 | 4, 4 | 165, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_cold | ro_bestcfg_vs_tt32 | 37.888 | 33.997 | 1.114x | 1.095-1.140x | 1.135x | 1.16-1.24x | NO | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k1024_bestcfg_cold | ro_bestcfg_vs_tt38 | 31.539 | 33.997 | 0.928x | 0.911-0.945x | 0.944x | 0.50-0.84x | NO | yes | 0 | 4, 4 | 211, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_warm | ro_bestcfg | 51.040 | 45.216 | 1.129x | 1.127-1.134x | 1.124x | 0.85-1.27x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_warm | ro_bestcfg_vs_tt32 | 48.966 | 45.216 | 1.083x | 1.082-1.085x | 1.060x | 0.94-1.35x | yes | yes | 0 | 4, 4 | 168, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_warm | ro_bestcfg_vs_tt38 | 48.480 | 45.216 | 1.072x | 1.063-1.079x | 1.071x | 0.70-0.83x | NO | yes | 0 | 4, 4 | 211, 233 | warm |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_cold | ro_bestcfg | 70.246 | 59.802 | 1.175x | 1.164-1.186x | 1.195x | 1.08-1.20x | yes | yes | 0 | 4, 4 | 165, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_cold | ro_bestcfg_vs_tt32 | 70.246 | 59.802 | 1.175x | 1.164-1.186x | 1.188x | 1.17-1.25x | yes | yes | 0 | 4, 4 | 168, 238 | cold |
| kernl_fused_ff | A100 | m512_n512_k2048_bestcfg_cold | ro_bestcfg_vs_tt38 | 54.886 | 59.802 | 0.918x | 0.908-0.928x | 1.187x | 0.48-0.83x | NO | yes | 0 | 4, 4 | 211, 238 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_warm | ro_bestcfg | 161.178 | 155.238 | 1.038x | 1.021-1.057x | 1.031x | 0.97-1.03x | NO | yes | 0 | 28, 28 | 64, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_warm | ro_bestcfg_vs_tt32 | 158.720 | 155.238 | 1.022x | 1.007-1.040x | 1.033x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 68, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_warm | ro_bestcfg_vs_tt38 | 191.104 | 155.238 | 1.231x | 1.219-1.248x | 1.244x | 0.97-1.03x | NO | yes | 0 | 4, 28 | 168, 68 | warm |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_cold | ro_bestcfg | 176.947 | 174.694 | 1.013x | 0.995-1.024x | 1.016x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 64, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_cold | ro_bestcfg_vs_tt32 | 175.718 | 174.694 | 1.006x | 0.991-1.019x | 1.007x | 0.97-1.03x | yes | yes | 0 | 28, 28 | 68, 68 | cold |
| kernl_fused_ff | A100 | m16_n11008_k4096_bestcfg_cold | ro_bestcfg_vs_tt38 | 211.968 | 174.694 | 1.213x | 1.193-1.227x | - | 0.97-1.03x | NO | yes | 0 | 4, 28 | 168, 68 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_warm | ro_bestcfg | 804.864 | 683.349 | 1.178x | 1.148-1.201x | 1.180x | 0.86-1.10x | NO | yes | 0 | 8, 8 | 241, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_warm | ro_bestcfg_vs_tt32 | 727.723 | 683.349 | 1.065x | 1.009-1.090x | 1.065x | 0.81-1.10x | yes | yes | 0 | 8, 8 | 243, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_warm | ro_bestcfg_vs_tt38 | 856.747 | 683.349 | 1.254x | 1.228-1.284x | 1.230x | 0.92-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | warm |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_cold | ro_bestcfg | 808.141 | 678.093 | 1.192x | 1.147-1.234x | 1.180x | 0.98-1.26x | yes | yes | 0 | 8, 8 | 241, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_cold | ro_bestcfg_vs_tt32 | 731.341 | 678.093 | 1.079x | 1.033-1.123x | 1.068x | 0.98-1.27x | yes | yes | 0 | 8, 8 | 243, 255 | cold |
| kernl_fused_ff | A100 | m512_n11008_k4096_bestcfg_cold | ro_bestcfg_vs_tt38 | 847.258 | 678.093 | 1.249x | 1.211-1.299x | 1.244x | 0.88-1.03x | NO | yes | 0 | 8, 8 | 255, 255 | cold |
| kernl_rmsnorm | A100 | N4096_M1_warm | ro | 2.627 | 2.161 | 1.216x | 1.212-1.217x | - | 1.07-1.33x | yes | yes | 0 | 4, 4 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M1_warm | ro2 | 2.627 | 2.020 | 1.300x | 1.297-1.302x | - | 1.13-1.60x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M1_warm | ro3 | 2.627 | 2.015 | 1.304x | 1.298-1.304x | - | 1.14-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M4_warm | ro | 2.706 | 2.250 | 1.203x | 1.203-1.204x | - | 1.07-1.33x | yes | yes | 0 | 4, 4 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M4_warm | ro2 | 2.706 | 2.097 | 1.291x | 1.289-1.292x | - | 1.13-1.60x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M4_warm | ro3 | 2.706 | 2.094 | 1.292x | 1.292-1.295x | - | 1.14-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M16_warm | ro | 2.819 | 2.350 | 1.199x | 1.198-1.199x | - | 1.07-1.33x | yes | yes | 0 | 4, 4 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M16_warm | ro2 | 2.819 | 2.189 | 1.288x | 1.288-1.288x | - | 1.13-1.60x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M16_warm | ro3 | 2.819 | 2.155 | 1.308x | 1.308-1.308x | - | 1.14-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M64_warm | ro | 3.026 | 2.596 | 1.166x | 1.166-1.167x | - | 1.07-1.33x | yes | yes | 0 | 4, 4 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M64_warm | ro2 | 3.026 | 2.519 | 1.201x | 1.200-1.201x | - | 1.13-1.60x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M64_warm | ro3 | 3.026 | 2.271 | 1.333x | 1.333-1.334x | - | 1.14-1.79x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M256_warm | ro | 3.896 | 3.338 | 1.167x | 1.166-1.169x | - | 1.07-1.26x | yes | yes | 0 | 12, 12 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M256_warm | ro2 | 3.896 | 3.397 | 1.147x | 1.146-1.150x | - | 1.11-1.45x | yes | yes | 0 | 12, 12 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M256_warm | ro3 | 3.896 | 3.187 | 1.222x | 1.220-1.224x | - | 1.15-1.63x | yes | yes | 0 | 12, 12 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M1_warm | ro | 3.059 | 2.278 | 1.343x | 1.340-1.343x | - | 1.13-1.57x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M1_warm | ro2 | 3.059 | 2.181 | 1.403x | 1.401-1.403x | - | 1.17-1.82x | yes | yes | 0 | 4, 4 | 32, 60 | warm |
| kernl_rmsnorm | A100 | N5120_M1_warm | ro3 | 3.059 | 2.166 | 1.413x | 1.410-1.413x | - | 1.19-2.04x | yes | yes | 0 | 4, 4 | 32, 58 | warm |
| kernl_rmsnorm | A100 | N5120_M4_warm | ro | 3.128 | 2.363 | 1.324x | 1.323-1.325x | - | 1.13-1.57x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M4_warm | ro2 | 3.128 | 2.281 | 1.371x | 1.371-1.373x | - | 1.17-1.82x | yes | yes | 0 | 4, 4 | 32, 60 | warm |
| kernl_rmsnorm | A100 | N5120_M4_warm | ro3 | 3.128 | 2.255 | 1.387x | 1.387-1.388x | - | 1.19-2.04x | yes | yes | 0 | 4, 4 | 32, 58 | warm |
| kernl_rmsnorm | A100 | N5120_M16_warm | ro | 3.236 | 2.458 | 1.317x | 1.316-1.317x | - | 1.13-1.57x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M16_warm | ro2 | 3.236 | 2.363 | 1.369x | 1.368-1.369x | - | 1.17-1.82x | yes | yes | 0 | 4, 4 | 32, 60 | warm |
| kernl_rmsnorm | A100 | N5120_M16_warm | ro3 | 3.236 | 2.312 | 1.400x | 1.399-1.401x | - | 1.19-2.04x | yes | yes | 0 | 4, 4 | 32, 58 | warm |
| kernl_rmsnorm | A100 | N5120_M64_warm | ro | 3.538 | 2.726 | 1.298x | 1.298-1.299x | - | 1.13-1.57x | yes | yes | 0 | 4, 4 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M64_warm | ro2 | 3.538 | 2.698 | 1.311x | 1.311-1.313x | - | 1.17-1.81x | yes | yes | 0 | 4, 4 | 32, 60 | warm |
| kernl_rmsnorm | A100 | N5120_M64_warm | ro3 | 3.538 | 2.596 | 1.363x | 1.363-1.364x | - | 1.19-2.03x | yes | yes | 0 | 4, 4 | 32, 58 | warm |
| kernl_rmsnorm | A100 | N5120_M256_warm | ro | 4.457 | 3.686 | 1.209x | 1.207-1.211x | - | 1.09-1.38x | yes | yes | 0 | 12, 12 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N5120_M256_warm | ro2 | 4.457 | 3.871 | 1.151x | 1.150-1.154x | - | 1.13-1.54x | yes | yes | 0 | 12, 12 | 32, 60 | warm |
| kernl_rmsnorm | A100 | N5120_M256_warm | ro3 | 4.457 | 3.912 | 1.139x | 1.137-1.141x | - | 1.18-1.73x | NO | yes | 0 | 12, 12 | 32, 58 | warm |
| kernl_rmsnorm | A100 | N8192_M1_warm | ro | 3.843 | 2.634 | 1.459x | 1.458-1.461x | - | 1.20-1.89x | yes | yes | 0 | 4, 4 | 40, 72 | warm |
| kernl_rmsnorm | A100 | N8192_M1_warm | ro2 | 3.843 | 2.662 | 1.443x | 1.442-1.444x | - | 1.22-2.06x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M1_warm | ro3 | 3.843 | 2.619 | 1.467x | 1.465-1.468x | - | 1.23-2.08x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M4_warm | ro | 3.930 | 2.703 | 1.454x | 1.450-1.455x | - | 1.20-1.89x | yes | yes | 0 | 4, 4 | 40, 72 | warm |
| kernl_rmsnorm | A100 | N8192_M4_warm | ro2 | 3.930 | 2.734 | 1.437x | 1.435-1.440x | - | 1.22-2.06x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M4_warm | ro3 | 3.930 | 2.691 | 1.460x | 1.459-1.463x | - | 1.23-2.08x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M16_warm | ro | 4.063 | 2.803 | 1.449x | 1.447-1.450x | - | 1.20-1.89x | yes | yes | 0 | 4, 4 | 40, 72 | warm |
| kernl_rmsnorm | A100 | N8192_M16_warm | ro2 | 4.063 | 2.862 | 1.419x | 1.417-1.420x | - | 1.22-2.06x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M16_warm | ro3 | 4.063 | 2.798 | 1.452x | 1.451-1.453x | - | 1.23-2.08x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M64_warm | ro | 4.324 | 3.279 | 1.318x | 1.318-1.320x | - | 1.20-1.88x | yes | yes | 0 | 4, 4 | 40, 72 | warm |
| kernl_rmsnorm | A100 | N8192_M64_warm | ro2 | 4.324 | 3.231 | 1.338x | 1.338-1.339x | - | 1.22-2.04x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M64_warm | ro3 | 4.324 | 3.123 | 1.384x | 1.384-1.386x | - | 1.23-2.07x | yes | yes | 0 | 4, 4 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M256_warm | ro | 5.570 | 4.973 | 1.120x | 1.118-1.123x | - | 1.16-1.60x | NO | yes | 0 | 12, 12 | 40, 72 | warm |
| kernl_rmsnorm | A100 | N8192_M256_warm | ro2 | 5.570 | 5.202 | 1.071x | 1.068-1.074x | - | 1.17-1.69x | NO | yes | 0 | 12, 12 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N8192_M256_warm | ro3 | 5.570 | 4.870 | 1.144x | 1.142-1.147x | - | 1.18-1.71x | NO | yes | 0 | 12, 12 | 40, 84 | warm |
| kernl_rmsnorm | A100 | N4096_M1024_warm | ro | 7.520 | 7.289 | 1.032x | 1.027-1.036x | - | 1.00-1.14x | yes | yes | 0 | 40, 40 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M1024_warm | ro2 | 7.520 | 7.121 | 1.056x | 1.051-1.062x | - | 1.00-1.15x | yes | yes | 0 | 40, 40 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M1024_warm | ro3 | 7.520 | 6.891 | 1.091x | 1.085-1.097x | - | 1.00-1.15x | yes | yes | 0 | 40, 40 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M4096_warm | ro | 56.174 | 53.277 | 1.054x | 1.048-1.061x | - | 0.95-1.06x | yes | yes | 0 | 64, 48 | 32, 38 | warm |
| kernl_rmsnorm | A100 | N4096_M4096_warm | ro2 | 56.174 | 52.078 | 1.079x | 1.070-1.086x | - | 0.95-1.06x | NO | yes | 0 | 64, 40 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M4096_warm | ro3 | 56.174 | 52.253 | 1.075x | 1.066-1.083x | - | 0.95-1.06x | NO | yes | 0 | 64, 40 | 32, 48 | warm |
| kernl_rmsnorm | A100 | N4096_M1_decode | ro | 8.397 | 7.441 | 1.128x | 1.099-1.158x | - | 1.09-1.37x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M1_decode | ro2 | 8.397 | 7.032 | 1.194x | 1.162-1.227x | - | 1.16-1.66x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M1_decode | ro3 | 8.397 | 6.758 | 1.242x | 1.214-1.277x | - | 1.18-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M4_decode | ro | 8.294 | 7.475 | 1.110x | 1.081-1.144x | - | 1.09-1.37x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M4_decode | ro2 | 8.294 | 7.032 | 1.180x | 1.148-1.235x | - | 1.16-1.66x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M4_decode | ro3 | 8.294 | 6.963 | 1.191x | 1.159-1.235x | - | 1.18-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M16_decode | ro | 8.499 | 7.612 | 1.117x | 1.089-1.140x | - | 1.09-1.37x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M16_decode | ro2 | 8.499 | 7.270 | 1.169x | 1.144-1.206x | - | 1.16-1.66x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M16_decode | ro3 | 8.499 | 7.066 | 1.203x | 1.177-1.229x | - | 1.18-1.80x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M64_decode | ro | 8.841 | 8.021 | 1.102x | 1.084-1.139x | - | 1.09-1.36x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M64_decode | ro2 | 8.841 | 7.509 | 1.177x | 1.158-1.212x | - | 1.15-1.66x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M64_decode | ro3 | 8.841 | 7.373 | 1.199x | 1.184-1.229x | - | 1.18-1.79x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M256_decode | ro | 9.523 | 8.738 | 1.090x | 1.069-1.119x | - | 1.08-1.31x | yes | yes | 0 | 12, 12 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M256_decode | ro2 | 9.523 | 8.738 | 1.090x | 1.065-1.123x | - | 1.14-1.54x | NO | yes | 0 | 12, 12 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M256_decode | ro3 | 9.523 | 8.568 | 1.112x | 1.091-1.146x | - | 1.18-1.67x | NO | yes | 0 | 12, 12 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M1_decode | ro | 9.421 | 7.714 | 1.221x | 1.197-1.247x | - | 1.15-1.59x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M1_decode | ro2 | 9.421 | 7.304 | 1.290x | 1.258-1.311x | - | 1.21-1.89x | yes | yes | 0 | 4, 4 | 32, 60 | cold |
| kernl_rmsnorm | A100 | N5120_M1_decode | ro3 | 9.421 | 7.270 | 1.296x | 1.264-1.311x | - | 1.22-2.01x | yes | yes | 0 | 4, 4 | 32, 58 | cold |
| kernl_rmsnorm | A100 | N5120_M4_decode | ro | 9.114 | 7.680 | 1.187x | 1.153-1.230x | - | 1.15-1.59x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M4_decode | ro2 | 9.114 | 7.270 | 1.254x | 1.222-1.294x | - | 1.21-1.89x | yes | yes | 0 | 4, 4 | 32, 60 | cold |
| kernl_rmsnorm | A100 | N5120_M4_decode | ro3 | 9.114 | 7.270 | 1.254x | 1.228-1.313x | - | 1.22-2.01x | yes | yes | 0 | 4, 4 | 32, 58 | cold |
| kernl_rmsnorm | A100 | N5120_M16_decode | ro | 9.284 | 7.816 | 1.188x | 1.155-1.223x | - | 1.15-1.59x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M16_decode | ro2 | 9.284 | 7.339 | 1.265x | 1.234-1.286x | - | 1.21-1.89x | yes | yes | 0 | 4, 4 | 32, 60 | cold |
| kernl_rmsnorm | A100 | N5120_M16_decode | ro3 | 9.284 | 7.407 | 1.253x | 1.228-1.280x | - | 1.22-2.01x | yes | yes | 0 | 4, 4 | 32, 58 | cold |
| kernl_rmsnorm | A100 | N5120_M64_decode | ro | 9.626 | 8.124 | 1.185x | 1.167-1.213x | - | 1.15-1.59x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M64_decode | ro2 | 9.626 | 7.782 | 1.237x | 1.212-1.267x | - | 1.21-1.88x | yes | yes | 0 | 4, 4 | 32, 60 | cold |
| kernl_rmsnorm | A100 | N5120_M64_decode | ro3 | 9.626 | 7.987 | 1.205x | 1.181-1.239x | - | 1.22-2.00x | NO | yes | 0 | 4, 4 | 32, 58 | cold |
| kernl_rmsnorm | A100 | N5120_M256_decode | ro | 10.342 | 9.489 | 1.090x | 1.060-1.109x | - | 1.12-1.45x | NO | yes | 0 | 12, 12 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N5120_M256_decode | ro2 | 10.342 | 9.387 | 1.102x | 1.071-1.129x | - | 1.17-1.66x | NO | yes | 0 | 12, 12 | 32, 60 | cold |
| kernl_rmsnorm | A100 | N5120_M256_decode | ro3 | 10.342 | 9.079 | 1.139x | 1.111-1.159x | - | 1.21-1.81x | NO | yes | 0 | 12, 12 | 32, 58 | cold |
| kernl_rmsnorm | A100 | N8192_M1_decode | ro | 10.991 | 8.056 | 1.364x | 1.322-1.422x | - | 1.26-2.00x | yes | yes | 0 | 4, 4 | 40, 72 | cold |
| kernl_rmsnorm | A100 | N8192_M1_decode | ro2 | 10.991 | 7.714 | 1.425x | 1.368-1.473x | - | 1.31-2.26x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M1_decode | ro3 | 10.991 | 7.612 | 1.444x | 1.386-1.493x | - | 1.31-2.28x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M4_decode | ro | 10.854 | 8.192 | 1.325x | 1.291-1.366x | - | 1.26-2.00x | yes | yes | 0 | 4, 4 | 40, 72 | cold |
| kernl_rmsnorm | A100 | N8192_M4_decode | ro2 | 10.854 | 7.748 | 1.401x | 1.346-1.438x | - | 1.31-2.26x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M4_decode | ro3 | 10.854 | 7.816 | 1.389x | 1.364-1.451x | - | 1.31-2.28x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M16_decode | ro | 10.786 | 8.192 | 1.317x | 1.293-1.352x | - | 1.26-2.00x | yes | yes | 0 | 4, 4 | 40, 72 | cold |
| kernl_rmsnorm | A100 | N8192_M16_decode | ro2 | 10.786 | 7.816 | 1.380x | 1.343-1.412x | - | 1.31-2.26x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M16_decode | ro3 | 10.786 | 7.816 | 1.380x | 1.343-1.405x | - | 1.31-2.28x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M64_decode | ro | 11.162 | 8.738 | 1.277x | 1.244-1.321x | - | 1.26-2.00x | yes | yes | 0 | 4, 4 | 40, 72 | cold |
| kernl_rmsnorm | A100 | N8192_M64_decode | ro2 | 11.162 | 8.158 | 1.368x | 1.342-1.411x | - | 1.30-2.25x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M64_decode | ro3 | 11.162 | 8.226 | 1.357x | 1.336-1.417x | - | 1.31-2.27x | yes | yes | 0 | 4, 4 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M256_decode | ro | 12.493 | 10.581 | 1.181x | 1.167-1.207x | - | 1.22-1.75x | NO | yes | 0 | 12, 12 | 40, 72 | cold |
| kernl_rmsnorm | A100 | N8192_M256_decode | ro2 | 12.493 | 10.650 | 1.173x | 1.152-1.195x | - | 1.25-1.91x | NO | yes | 0 | 12, 12 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N8192_M256_decode | ro3 | 12.493 | 10.035 | 1.245x | 1.221-1.273x | - | 1.26-1.92x | NO | yes | 0 | 12, 12 | 40, 84 | cold |
| kernl_rmsnorm | A100 | N4096_M1_cold | ro | 8.499 | 7.509 | 1.132x | 1.080-1.156x | - | 1.09-1.35x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M1_cold | ro2 | 8.499 | 7.066 | 1.203x | 1.163-1.235x | - | 1.15-1.62x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M1_cold | ro3 | 8.499 | 6.861 | 1.239x | 1.191-1.273x | - | 1.18-1.74x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M16_cold | ro | 8.568 | 7.646 | 1.121x | 1.079-1.164x | - | 1.09-1.35x | yes | yes | 0 | 4, 4 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M16_cold | ro2 | 8.568 | 7.236 | 1.184x | 1.144-1.220x | - | 1.15-1.62x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M16_cold | ro3 | 8.568 | 6.997 | 1.224x | 1.182-1.275x | - | 1.18-1.74x | yes | yes | 0 | 4, 4 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M256_cold | ro | 10.854 | 10.342 | 1.050x | 1.036-1.077x | - | 1.07-1.24x | NO | yes | 0 | 12, 12 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M256_cold | ro2 | 10.854 | 10.308 | 1.053x | 1.033-1.081x | - | 1.11-1.40x | NO | yes | 0 | 12, 12 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M256_cold | ro3 | 10.854 | 10.206 | 1.064x | 1.050-1.084x | - | 1.14-1.50x | NO | yes | 0 | 12, 12 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M1024_cold | ro | 19.320 | 18.876 | 1.024x | 1.009-1.033x | - | 1.04-1.12x | NO | yes | 0 | 40, 40 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M1024_cold | ro2 | 19.320 | 18.705 | 1.033x | 1.018-1.042x | - | 1.06-1.19x | NO | yes | 0 | 40, 40 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M1024_cold | ro3 | 19.320 | 18.671 | 1.035x | 1.022-1.046x | - | 1.08-1.22x | NO | yes | 0 | 40, 40 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M4096_cold | ro | 63.010 | 59.631 | 1.057x | 1.048-1.066x | - | 0.95-1.06x | yes | yes | 0 | 64, 48 | 32, 38 | cold |
| kernl_rmsnorm | A100 | N4096_M4096_cold | ro2 | 63.010 | 58.266 | 1.081x | 1.072-1.092x | - | 0.95-1.06x | NO | yes | 0 | 64, 40 | 32, 48 | cold |
| kernl_rmsnorm | A100 | N4096_M4096_cold | ro3 | 63.010 | 58.266 | 1.081x | 1.073-1.091x | - | 0.95-1.06x | NO | yes | 0 | 64, 40 | 32, 48 | cold |
- kernl_fused_ff A100 m16_n11008_k4096_128x256x64_w8_s3_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m16_n11008_k4096_128x256x64_w8_s3_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m16_n11008_k4096_64x256x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m16_n11008_k4096_64x256x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m16_n11008_k4096_128x128x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m16_n11008_k4096_128x128x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_128x256x64_w8_s3_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_128x256x64_w8_s3_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_64x256x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_64x256x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_128x128x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k1024_128x128x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_128x256x64_w8_s3_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_128x256x64_w8_s3_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_64x256x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_64x256x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_128x128x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n512_k2048_128x128x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_128x256x64_w8_s3_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_128x256x64_w8_s3_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_64x256x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_64x256x32_w4_s4_cold: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_128x128x32_w4_s4_warm: only 'orig' rows, no reordered variant
- kernl_fused_ff A100 m512_n11008_k4096_128x128x32_w4_s4_cold: only 'orig' rows, no reordered variant
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_64x128x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m64_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m128_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m256_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n1024_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k1024_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m1024_n4096_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x32x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_128x64x32_w4_s4_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_64x32x32_w2_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_32x64x32_w2_s5_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_16x16x64_w4_s2_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k1024_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n512_k2048_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m16_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_warm
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_fused_ff H100 m512_n11008_k4096_bestcfg_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_warm
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N5120_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M1_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M4_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M16_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M64_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N8192_M256_decode
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M16_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M256_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M1024_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_cold
- prediction without a measurement: kernl_rmsnorm H100 N4096_M4096_cold
- prediction without a measurement: kernl_rmsnorm_sass A100 0
- prediction without a measurement: kernl_rmsnorm_sass A100 0
- prediction without a measurement: kernl_rmsnorm_sass A100 1
- prediction without a measurement: kernl_rmsnorm_sass A100 1
- prediction without a measurement: kernl_rmsnorm_sass A100 2
- prediction without a measurement: kernl_rmsnorm_sass A100 2
- prediction without a measurement: kernl_rmsnorm_sass A100 3
- prediction without a measurement: kernl_rmsnorm_sass A100 3
- prediction without a measurement: kernl_rmsnorm_sass A100 4
- prediction without a measurement: kernl_rmsnorm_sass A100 4
- prediction without a measurement: kernl_rmsnorm_sass A100 5
- prediction without a measurement: kernl_rmsnorm_sass A100 5
- prediction without a measurement: kernl_rmsnorm_sass A100 6
- prediction without a measurement: kernl_rmsnorm_sass A100 6
- prediction without a measurement: kernl_rmsnorm_sass A100 7
- prediction without a measurement: kernl_rmsnorm_sass A100 7
- prediction without a measurement: kernl_rmsnorm_sass A100 8
- prediction without a measurement: kernl_rmsnorm_sass A100 8
- prediction without a measurement: kernl_rmsnorm_sass A100 9
- prediction without a measurement: kernl_rmsnorm_sass A100 9
- prediction without a measurement: kernl_rmsnorm_sass A100 10
- prediction without a measurement: kernl_rmsnorm_sass A100 10
- prediction without a measurement: kernl_rmsnorm_sass A100 11
- prediction without a measurement: kernl_rmsnorm_sass A100 11
- prediction without a measurement: kernl_rmsnorm_sass A100 12
- prediction without a measurement: kernl_rmsnorm_sass A100 12
- prediction without a measurement: kernl_rmsnorm_sass A100 13
- prediction without a measurement: kernl_rmsnorm_sass A100 13
- prediction without a measurement: kernl_rmsnorm_sass A100 14
- prediction without a measurement: kernl_rmsnorm_sass A100 14
- prediction without a measurement: kernl_rmsnorm_sass A100 15
- prediction without a measurement: kernl_rmsnorm_sass A100 15
- prediction without a measurement: kernl_rmsnorm_sass A100 16
- prediction without a measurement: kernl_rmsnorm_sass A100 16
- prediction without a measurement: kernl_rmsnorm_sass A100 17
- prediction without a measurement: kernl_rmsnorm_sass A100 17

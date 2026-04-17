# Strong-Coupling Benchmark Analysis

## Summary
- PASS: schema completeness and dimension alignment are satisfied.

## Schema Completeness
- Reference missing keys: none
- Scan missing columns: none
- Reduction missing columns: none

## MC vs Literature
| Metric | MC | Literature | |Δ| | Current FRG | |Δ| |
|:---|---:|---:|---:|---:|---:|
| binder | 0.4939 | 0.4656 | 0.0283 | 0.4656 | 0.0283 |
| xi_over_L | 0.6346 | 0.6431 | 0.0085 | 0.6431 | 0.0085 |
| eta | -0.1087 | 0.0363 | 0.1450 | 0.0360 | 0.1447 |
| nu | 0.6857 | 0.6300 | 0.0557 | 0.6440 | 0.0417 |

## MC vs Current FRG
- Reference pass flag: True
- Current FRG source: Paper V §5.5.9 DE2 3D Ising benchmark

## Reference Gate
| Metric | Value | Target | |Δ| | Tolerance | Pass |
|:---|---:|---:|---:|---:|:---:|
| binder | 0.4939 | 0.4656 | 0.0283 | 0.2000 | yes |
| xi_over_L | 0.6346 | 0.6431 | 0.0085 | 0.2500 | yes |
| eta | -0.1087 | 0.0363 | 0.1450 | 0.2000 | yes |
| nu | 0.6857 | 0.6300 | 0.0557 | 0.2500 | yes |

## Scan Surface
- Rows loaded: 75
- dimension_mode values: ['fractional_proxy']
- coupling_ids: ['n2.68_m1.500_lam1.000', 'n2.70_m1.000_lam0.500', 'n2.78_m0.400_lam1.000', 'n2.90_m0.430_lam0.600', 'n3.00_m1.500_lam0.500']
- observables: ['acceptance_rate', 'binder', 'magnetization_abs', 'susceptibility', 'xi_over_L']
- scan_mode: fractional_proxy
- formal_n values: ['2.680000', '2.700000', '2.780000', '2.900000', '3.000000']
- n_eff values: ['1.680000', '1.700000', '1.780000', '1.900000', '2.000000']
- transverse_weight values: ['0.840000', '0.850000', '0.890000', '0.950000', '1.000000']
- t_axis_weight values: ['0.000000']
- proxy_kinds: ['t_projected_direct']
- schedule_modes: ['per_n']
- schedule_sources: ['built_in_direct_v1']

## Gamma Reduction Surface
| formal_n | coupling_id | sizes | eta_proxy | LPA' γ proxy | LPA' status | DE2 γ proxy | DE2 status |
|:---:|:---|:---|---:|---:|:---|---:|:---|
| 2.68 | n2.68_m1.500_lam1.000 | 4,6,8 | 1.4497 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.70 | n2.70_m1.000_lam0.500 | 4,6,8 | 2.2782 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m0.400_lam1.000 | 4,6,8 | 2.3728 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.90 | n2.90_m0.430_lam0.600 | 4,6,8 | 1.6728 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 3.00 | n3.00_m1.500_lam0.500 | 4,6,8 | 1.0110 | -- | out_of_anchor_band | -- | out_of_anchor_band |
- calibrated_rows: 0 / 5
- note: これは η = γ の同一視ではなく、Paper V の FRG 表を anchor にした calibrated reduction surface である。

## Future Fractional Proxy
- ready_for_fractional_proxy: True
- ready_for_gamma_comparison: False
- scan_mode: fractional_proxy
- rationale: Phase 0 gate is open and the fractional scan already satisfies the shared schema.

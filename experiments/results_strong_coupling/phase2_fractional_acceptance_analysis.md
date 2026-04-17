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
- Rows loaded: 20
- dimension_mode values: ['fractional_proxy']
- coupling_ids: ['n2.78_m1.050_lam1.050']
- observables: ['acceptance_rate', 'binder', 'magnetization_abs', 'susceptibility', 'xi_over_L']
- scan_mode: fractional_proxy
- formal_n values: ['2.780000']
- n_eff values: ['1.780000']
- transverse_weight values: ['0.890000']
- t_axis_weight values: ['0.000000']
- proxy_kinds: ['t_projected_direct']
- schedule_modes: ['per_n']
- schedule_sources: ['path']

## Gamma Reduction Surface
| formal_n | coupling_id | sizes | eta_proxy | LPA' γ proxy | LPA' status | DE2 γ proxy | DE2 status |
|:---:|:---|:---|---:|---:|:---|---:|:---|
| 2.78 | n2.78_m1.050_lam1.050 | 6,8,10,12 | 1.8706 | -- | out_of_anchor_band | -- | out_of_anchor_band |
- calibrated_rows: 0 / 1
- note: これは η = γ の同一視ではなく、Paper V の FRG 表を anchor にした calibrated reduction surface である。

## Future Fractional Proxy
- ready_for_fractional_proxy: True
- ready_for_gamma_comparison: False
- scan_mode: fractional_proxy
- rationale: Phase 0 gate is open and the fractional scan already satisfies the shared schema.

## Local Foothold
- largest_calibrated_component_size: 0
- selected_component_formal_n: none
- selected_component_couplings: none
- local_foothold: False
- blocking_reason: Metropolis-family exhausted

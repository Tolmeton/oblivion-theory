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
- Rows loaded: 120
- dimension_mode values: ['fractional_proxy']
- coupling_ids: ['n2.78_m1.000_lam1.000', 'n2.78_m1.000_lam1.050', 'n2.78_m1.000_lam1.100', 'n2.78_m1.000_lam1.200', 'n2.78_m1.050_lam1.150']
- observables: ['acceptance_rate', 'binder', 'magnetization_abs', 'structure_factor_kmin', 'susceptibility', 'xi_over_L']
- scan_mode: fractional_proxy
- formal_n values: ['2.780000']
- n_eff values: ['1.780000']
- transverse_weight values: ['0.890000']
- t_axis_weight values: ['0.000000']
- proxy_kinds: ['t_projected_direct']
- schedule_modes: ['per_n']
- schedule_sources: ['path']

## Gamma Reduction Surface
| formal_n | coupling_id | estimator | source | sizes | eta_proxy | LPA' γ proxy | LPA' status | DE2 γ proxy | DE2 status |
|:---:|:---|:---|:---|:---|---:|---:|:---|---:|:---|
| 2.78 | n2.78_m1.000_lam1.000 | chi_connected | susceptibility | 6,8,10,12 | 2.0280 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.000 | kmin_structure | structure_factor_kmin | 6,8,10,12 | 1.7112 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.050 | chi_connected | susceptibility | 6,8,10,12 | 1.9355 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.050 | kmin_structure | structure_factor_kmin | 6,8,10,12 | 1.8330 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.100 | chi_connected | susceptibility | 6,8,10,12 | 2.1539 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.100 | kmin_structure | structure_factor_kmin | 6,8,10,12 | 1.6841 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.200 | chi_connected | susceptibility | 6,8,10,12 | 2.2139 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.000_lam1.200 | kmin_structure | structure_factor_kmin | 6,8,10,12 | 1.7214 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.050_lam1.150 | chi_connected | susceptibility | 6,8,10,12 | 1.8713 | -- | out_of_anchor_band | -- | out_of_anchor_band |
| 2.78 | n2.78_m1.050_lam1.150 | kmin_structure | structure_factor_kmin | 6,8,10,12 | 1.7274 | -- | out_of_anchor_band | -- | out_of_anchor_band |
- calibrated_rows: 0 / 10
- note: これは η = γ の同一視ではなく、Paper V の FRG 表を anchor にした calibrated reduction surface である。

## Future Fractional Proxy
- ready_for_fractional_proxy: True
- ready_for_gamma_comparison: False
- scan_mode: fractional_proxy
- rationale: Phase 0 gate is open and the fractional scan already satisfies the shared schema.

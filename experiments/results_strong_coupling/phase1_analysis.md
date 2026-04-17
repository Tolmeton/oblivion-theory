# Strong-Coupling Benchmark Analysis

## Summary
- PASS: schema completeness and dimension alignment are satisfied.

## Schema Completeness
- Reference missing keys: none
- Scan missing columns: none

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

## Integer Proxy Scan
- Rows loaded: 20
- dimension_mode values: ['integer_proxy']
- coupling_ids: ['m6.000_lam1.000', 'm8.000_lam1.000']
- observables: ['acceptance_rate', 'binder', 'magnetization_abs', 'susceptibility', 'xi_over_L']

## Future Fractional Proxy
- ready_for_fractional_proxy: True
- rationale: Phase 0 gate is open and the integer-proxy schema is reusable.

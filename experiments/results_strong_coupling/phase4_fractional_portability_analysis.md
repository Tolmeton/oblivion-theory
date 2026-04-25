# Fractional Transfer Portability Analysis

## Setup
- formal_n values: ['2.780000', '2.900000', '3.000000']
- sizes: [6, 8, 10, 12]
- anchor_method: de2
- per_n transfer max_cv: 0.1
- cross_n portability max_cv: 0.2

## Critical-Line Surface
| formal_n | crossing_records | selected_couplings | selected_scan_rows | line_status |
|:---:|---:|---:|---:|:---|
| 2.780000 | 33 | 5 | 120 | selected_line_found |
| 2.900000 | 58 | 5 | 120 | selected_line_found |
| 3.000000 | 44 | 5 | 120 | selected_line_found |

## Per-n Transfer Stability
| formal_n | estimator | median_factor | cv | stable | status |
|:---:|:---|---:|---:|:---:|:---|
| 2.780000 | chi_connected | 63.3749186406 | 0.0630325763 | True | stable_transfer_candidate |
| 2.780000 | kmin_structure | 53.7929295156 | 0.0293975475 | True | stable_transfer_candidate |
| 2.900000 | chi_connected | 74.3930593520 | 0.2682994010 | False | unstable_transfer_candidate |
| 2.900000 | kmin_structure | 71.1423253600 | 0.0449510123 | True | stable_transfer_candidate |
| 3.000000 | chi_connected | 111.8821966000 | 0.1051893008 | False | unstable_transfer_candidate |
| 3.000000 | kmin_structure | 94.1349172316 | 0.0620504665 | True | stable_transfer_candidate |

## Cross-n Portability
| estimator | stable_n_count | factor_min | factor_max | cross_n_cv | portability_pass | status |
|:---|---:|---:|---:|---:|:---:|:---|
| chi_connected | 1/3 | 63.3749186406 | 63.3749186406 | 0.0000000000 | False | nonportable_transfer_candidate |
| kmin_structure | 3/3 | 53.7929295156 | 94.1349172316 | 0.2262723138 | False | nonportable_transfer_candidate |

## Interpretation
- portable_estimators: none
- interpretation: the transfer factor may be stable locally but does not survive cross-n portability. In that case H5 is insufficient as a general explanation and the main failure returns to proxy topology or critical-surface definition.

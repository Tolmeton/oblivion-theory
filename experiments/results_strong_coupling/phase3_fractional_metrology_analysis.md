# Fractional Metrology Transfer Analysis

## Setup
- anchor_method: de2
- estimators_loaded: 2
- transfer_rows: 10

## Estimator Stability
| estimator | n_rows | median_factor | mean_factor | cv | stable | status |
|:---|---:|---:|---:|---:|:---:|:---|
| chi_connected | 5 | 63.3749186406 | 63.7660165562 | 0.0630325763 | True | stable_transfer_candidate |
| kmin_structure | 5 | 53.7929295156 | 54.2320411844 | 0.0293975475 | True | stable_transfer_candidate |

## Transfer-Corrected Surface
| coupling_id | estimator | eta_proxy | factor_raw | eta_transfer_corrected | gamma_transfer_corrected | status |
|:---|:---|---:|---:|---:|---:|:---|
| n2.78_m1.000_lam1.000 | chi_connected | 2.0279973965 | 63.3749186406 | 0.0320000000 | 0.4620000000 | stable_transfer_candidate |
| n2.78_m1.000_lam1.050 | chi_connected | 1.9354738290 | 60.4835571563 | 0.0305400602 | 0.4409221188 | stable_transfer_candidate |
| n2.78_m1.000_lam1.100 | chi_connected | 2.1538979090 | 67.3093096562 | 0.0339865984 | 0.4906815145 | stable_transfer_candidate |
| n2.78_m1.000_lam1.200 | chi_connected | 2.2138556839 | 69.1829901219 | 0.0349326789 | 0.5043405518 | stable_transfer_candidate |
| n2.78_m1.050_lam1.150 | chi_connected | 1.8713378306 | 58.4793072062 | 0.0295280510 | 0.4263112365 | stable_transfer_candidate |
| n2.78_m1.000_lam1.000 | kmin_structure | 1.7112077892 | 53.4752434125 | 0.0318110169 | 0.4592715563 | stable_transfer_candidate |
| n2.78_m1.000_lam1.050 | kmin_structure | 1.8330390265 | 57.2824695781 | 0.0340758357 | 0.4919698775 | stable_transfer_candidate |
| n2.78_m1.000_lam1.100 | kmin_structure | 1.6840673577 | 52.6271049281 | 0.0313064816 | 0.4519873280 | stable_transfer_candidate |
| n2.78_m1.000_lam1.200 | kmin_structure | 1.7213737445 | 53.7929295156 | 0.0320000000 | 0.4620000000 | stable_transfer_candidate |
| n2.78_m1.050_lam1.150 | kmin_structure | 1.7274386716 | 53.9824584875 | 0.0321127458 | 0.4636277675 | stable_transfer_candidate |

## Interpretation
- stable_estimators: ['chi_connected', 'kmin_structure']
- interpretation: estimator-specific inflation factors are approximately stable along the selected critical line. This keeps the H5 metrology hypothesis alive, but the correction remains anchor-dependent and therefore is not an independent resolution.

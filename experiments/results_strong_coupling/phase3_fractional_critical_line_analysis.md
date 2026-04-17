# Fractional Critical-Line Analysis

## Setup
- formal_n: 2.780000
- sizes: [6, 8, 10, 12]
- mass_like grid: [0.9, 0.95, 1.0, 1.05, 1.1]
- lambda_like grid: [1.0, 1.05, 1.1, 1.15, 1.2]
- crossing_records: 33
- phase0_reference_pass: True

## Crossing Candidates
| lambda_like | support | observables | size_pairs | mean_crossing_mass | scatter | selected_mass_like | selected_coupling_id |
|:---:|---:|:---|:---|---:|---:|---:|:---|
| 1.00 | 8 | binder|xi_over_L | 10-12|6-8|8-10 | 0.9901740938 | 0.0595272138 | 1.000000 | n2.78_m1.000_lam1.000 |
| 1.05 | 7 | xi_over_L | 10-12|8-10 | 0.9879084784 | 0.0493041776 | 1.000000 | n2.78_m1.000_lam1.050 |
| 1.20 | 7 | xi_over_L | 10-12|8-10 | 0.9933250754 | 0.0643167278 | 1.000000 | n2.78_m1.000_lam1.200 |
| 1.10 | 6 | xi_over_L | 10-12|6-8|8-10 | 1.0071360016 | 0.0571329066 | 1.000000 | n2.78_m1.000_lam1.100 |
| 1.15 | 5 | binder|xi_over_L | 10-12|8-10 | 1.0511369489 | 0.0331290841 | 1.050000 | n2.78_m1.050_lam1.150 |

## Selected Line
- selected_couplings: ['n2.78_m1.000_lam1.000', 'n2.78_m1.000_lam1.050', 'n2.78_m1.000_lam1.100', 'n2.78_m1.000_lam1.200', 'n2.78_m1.050_lam1.150']
- selected_scan_rows: 100

## Eta On Pseudo-critical Line
| coupling_id | sizes | eta_proxy | DE2 status | DE2 γ proxy | LPA' status |
|:---|:---|---:|:---|---:|:---|
| n2.78_m1.000_lam1.000 | 6,8,10,12 | 2.0279973965 | out_of_anchor_band | -- | out_of_anchor_band |
| n2.78_m1.000_lam1.050 | 6,8,10,12 | 1.9354738290 | out_of_anchor_band | -- | out_of_anchor_band |
| n2.78_m1.000_lam1.100 | 6,8,10,12 | 2.1538979090 | out_of_anchor_band | -- | out_of_anchor_band |
| n2.78_m1.000_lam1.200 | 6,8,10,12 | 2.2138556839 | out_of_anchor_band | -- | out_of_anchor_band |
| n2.78_m1.050_lam1.150 | 6,8,10,12 | 1.8713378306 | out_of_anchor_band | -- | out_of_anchor_band |
- calibrated_rows: 0 / 5
- interpretation: current window contains crossing-supported couplings, but they still may miss the FRG anchor band.

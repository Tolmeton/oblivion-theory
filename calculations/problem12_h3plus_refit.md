# Problem 12 H3+ 再 fit メモ

作成日: 2026-04-25

## 0. Scope

対象は Problem 12 の `arg lambda_dom(q)` proxy。既存 H3 `beta + gamma/q` に対し、H3+ `beta + gamma_1/q + gamma_2/q^2` を同じ SOURCE データで再 fit した。

SOURCE:

| surface | path |
|:---|:---|
| Problem 12 本文 | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` |
| q=5..10 / q=11..15 数値 | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_自動数学_キュー10_スペクトル_周期性.md` |
| 再現スクリプト | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/problem12_h3plus_refit.py` |
| JSON 出力 | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/problem12_h3plus_refit.json` |

入力値は local note の丸め済み `arg` 値:

| q | 5 | 6 | 7 | 8 | 9 | 10 |
|:---|---:|---:|---:|---:|---:|---:|
| arg | 1.793 | 1.451 | 1.321 | 1.250 | 1.206 | 1.174 |

Stress data:

| q | 11 | 12 | 13 | 14 | 15 |
|:---|---:|---:|---:|---:|---:|
| arg | 1.162 | 1.152 | 1.147 | 1.145 | 1.145 |

## 1. Kernel

H3+ は数値 fit として H3 より強い。Phase B `q=5..10` で RMSE は `0.053121 -> 0.011178`、R² は `0.936705 -> 0.997198`、AICc は `-27.222 -> -35.926` へ改善する。q=11..15 を Phase B 学習の外挿 stress として当てると、RMSE は `0.168758 -> 0.049787` へ下がる。

ただし、この改善は `beta` の意味を安定化しない。H3 では `beta=0.521008±0.112971` だったが、H3+ では `beta=1.625333±0.139950` に跳ぶ。さらに H3+ の曲線は `q≈10.84` で底を打って上向きへ転じる。これは「q→∞ の漸近角」を読める形ではなく、Phase B 端点の曲率を吸収する局所 proxy と読むべき結果である。

## 2. Fit Table

| fit | data | beta | gamma_1 | gamma_2 | RMSE | R² | AICc | LOOCV RMSE | condition | turning q |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| H3 | q=5..10 | 0.521008 | 5.994258 | - | 0.053121 | 0.936705 | -27.222 | 0.108823 | 29.916 | - |
| H3+ | q=5..10 | 1.625333 | -9.610719 | 52.079413 | 0.011178 | 0.997198 | -35.926 | 0.049865 | 1057.729 | 10.838 |
| H3 stress | q=5..15 | 0.779418 | 4.350493 | - | 0.067507 | 0.872934 | -53.801 | 0.108262 | 24.898 | - |
| H3+ stress | q=5..15 | 1.407446 | -6.632652 | 42.432959 | 0.011774 | 0.996135 | -88.293 | 0.033987 | 663.700 | 12.795 |

`condition` は設計行列の条件数。H3+ の値が大きいので、係数の意味づけは fit 精度より弱い。

## 3. Candidate Beta Stress

H3+ で `beta` を固定し、`gamma_1/q + gamma_2/q^2` だけを fit した条件付き比較。

| fixed beta | value | Phase B RMSE | Phase B AICc | LOOCV RMSE |
|:---|---:|---:|---:|---:|
| `2 atan(1/phi)` | 1.107149 | 0.026380 | -35.622 | 0.064098 |
| `pi/5` | 0.628319 | 0.047314 | -28.611 | 0.111778 |
| `pi/6` | 0.523599 | 0.052019 | -27.474 | 0.122306 |
| prior H3 beta | 0.520900 | 0.052141 | -27.446 | 0.122577 |
| `log(phi)` | 0.481212 | 0.053930 | -27.041 | 0.126572 |

ここから言えるのは次の一点に限る。v0.30 の「H3 の beta として golden angle は棄却」は維持される。一方で、H3+ の curvature term を許すと `2 atan(1/phi)` 固定モデルは Phase B で条件付きに競争力を持つ。これは golden/cyclotomic/F5 系のどれかが曲率を作る可能性を残すが、fit だけでは三者を分離しない。

## 4. 判定

SOURCE から確定:

| item | 判定 |
|:---|:---|
| H3+ は H3 の U 字 residual を吸収するか | Yes |
| q=11..15 stress residual は下がるか | Yes |
| H3 の low beta が安定定数として残るか | No |
| H3+ の free beta を q→∞ limit と読めるか | No |
| golden / cyclotomic / F5 defect の三候補を fit だけで分離できるか | No |

INFERENCE:

Problem 12 は「beta 候補の数当て」から「曲率項を生む algebraic mechanism の同定」へ移るべきである。次に見る面は追加 fit ではなく、signature transition、cyclotomic trace、F5 angular defect のどれが `gamma_2/q^2` 型の曲率を要求するかである。

## 5. Body Patch Candidate

本文へ入れる最小更新:

> v0.32: H3+ `beta + gamma_1/q + gamma_2/q^2` 再 fit により、Phase B `q=5..10` では RMSE `0.0531 -> 0.0112`、R² `0.9367 -> 0.9972` と改善し、q=11..15 stress RMSE も `0.1688 -> 0.0498` に低下した。ただし free beta は `0.5210` から `1.6253` へ跳び、turning point `q≈10.84` を持つため、beta を漸近定数として読む解釈は崩れる。`2 atan(1/phi)` 固定 H3+ は条件付きに競争力を持つが、fit だけでは golden / cyclotomic / F5 angular defect を分離しない。Problem 12 の次段は追加 beta fit ではなく、曲率項の代数的発生源の同定である。

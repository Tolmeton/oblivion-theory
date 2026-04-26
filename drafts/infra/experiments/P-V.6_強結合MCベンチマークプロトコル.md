# P-V.6 強結合 MC benchmark protocol

**日付**: 2026-04-26
**状態**: Round 1 protocol 固定 / Phase 0 gate open / strong-coupling anchor 未到達
**対象**: Paper V §6.8.4 実験 III、特に $\gamma_\Phi^{\mathrm{obs}}\approx0.86$ の残余乖離
**目的**: MC を first benchmark として固定し、残余乖離が FRG truncation error なのか、Paper IV 側の observable / scale ratio / 可観測化の問題なのかを分離する。

## 0. SOURCE 境界

| SOURCE | 役割 |
|:---|:---|
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である_草稿.md` §5.4, §5.5, §6.8, §7.2 | 摂動 no-go、LPA' / DE2 到達、MC first cut、Open status の本文側 SOURCE |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である.meta.md` §M5, §M6 C4 | MC first / BMW second の meta contract |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/plans/P-V.6_強結合benchmark計画_v1.md` | 設計書。なぜ BMW first ではないかを固定 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` | MC の負・曖昧・未成熟な結果を claim impact / next operation / forbidden interpretation に事前対応させる |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_common.py` | 共有 schema、FRG anchors、Paper IV target $\gamma_\Phi=0.86$ |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_mc_reference.py` | Phase 0 reference gate |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_mc_scan.py` | Phase 1 integer proxy scan |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_compare.py` | reference / scan / reduction の同一面比較 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase1_analysis.md` | 現行 Phase 0 / integer proxy の通過状態 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase5_fractional_topology_analysis.md` | H3/H4 後の anchor 未到達状態 |

**TAINT / 次段 SOURCE 化が必要な面**

Paper IV の $\gamma_\Phi^{\mathrm{obs}}\approx0.86$ は target として使うが、この protocol はその値を再証明しない。MC が担うのは 0.86 の正当化ではなく、0.86 へ向かう残余乖離の帰属判定である。

## 1. Operational Thesis

P-V.6 の実験 III は solver 開発ではない。問いは次で固定する。

> $\gamma_\Phi^{\mathrm{obs}}\approx0.86$ の残余乖離は、FRG truncation error か。それとも Paper IV 側の observable / scale ratio / 可観測化の問題か。

この問いに答えるため、first benchmark は MC とする。BMW は benchmark ではなく、MC が DE2 を系統的に上回った場合にだけ起動する second-phase solver である。

## 2. Non-Goals

| 非目的 | 理由 |
|:---|:---|
| この protocol だけで 0.86 を解く | 現段階では帰属判定が目的であり、完全再現は Open |
| BMW first に進む | FRG 系列の内側だけを延長しても observable / R / truncation を分離できない |
| DE2 外挿 0.651 を勝利宣言にする | 外挿は benchmark ではない |
| 0.86 を 0.46 側へ弱める | Paper V の射程縮小であり、C4 の棄却 ledger に反する |

## 3. Phase Gate

| Phase | 目的 | 入力 | 出力 | 通過条件 |
|:---|:---|:---|:---|:---|
| Phase 0 | MC pipeline が既知 universality class を壊していないことを確認 | 3D Ising reference | `phase0_reference.json` | `pass=true` かつ binder / xi_over_L / eta / nu が許容帯内 |
| Phase 1 | integer proxy schema を固定 | 3D scalar $\phi^4$ local Metropolis | `phase1_scan.csv`, `phase1_analysis.md` | schema completeness と dimension alignment が PASS |
| Phase 2 | fractional / T-projected proxy を生成 | formal $n=3.0,2.9,2.78,2.7,2.68$ | `phase2_fractional_scan.csv`, `phase2_gamma_reduction.csv` | FRG anchors へ calibrated rows が出る |
| Phase 3 | metrology / critical-line surface を比較 | Phase 2 outputs | phase3/4/5 analysis | local stability だけでなく cross-$n$ portability を満たす |
| Phase 4 | BMW 昇格判定 | MC vs DE2 差分 | BMW go / no-go | MC が DE2 を系統的に上回り、momentum dependence が残差主因と読める |

## 4. Canonical Commands

実行 cwd は常に次とする。

```bash
/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion
```

Phase 0:

```bash
python experiments/strong_coupling_mc_reference.py
```

Phase 1:

```bash
python experiments/strong_coupling_mc_scan.py
python experiments/strong_coupling_compare.py
```

Fractional / gamma reduction surface:

```bash
python experiments/strong_coupling_fractional_proxy.py
python experiments/strong_coupling_gamma_reduction.py
python experiments/strong_coupling_compare.py \
  --scan experiments/results_strong_coupling/phase2_fractional_scan.csv \
  --reduction experiments/results_strong_coupling/phase2_gamma_reduction.csv \
  --out experiments/results_strong_coupling/phase2_fractional_analysis.md
```

H3/H4 topology surface:

```bash
python experiments/strong_coupling_fractional_topology_surface.py
```

## 5. Decision Table

| 観測結果 | 読み | 次の操作 |
|:---|:---|:---|
| MC が DE2 と同程度で、両者とも 0.86 から遠い | FRG truncation ではなく Paper IV 側の observable / $R$ / calibration が主因 | Paper IV 側の可観測化とスケール比を再較正 |
| MC が DE2 を系統的に上回り、0.86 側へ寄る | truncation error が主因 | BMW 昇格 |
| MC を再現できるのが momentum-dependent solver のみ | 運動量依存性が本質 | BMW を本命化 |
| MC が安定せず finite-size drift が大きい | benchmark 面が未成熟 | lattice / update kernel / scaling window を修正 |
| topology / selector 変更でも anchor 未到達 | selector tweak では不足 | long-range / hierarchical など新 proxy family へ進む |

## 6. 現在地

| 面 | 現状 |
|:---|:---|
| Phase 0 reference | `phase1_analysis.md` 上では `Reference pass flag: True` |
| Phase 1 integer proxy | schema completeness と dimension alignment は PASS |
| Phase 2+ fractional surfaces | gamma reduction / metrology / topology surface は実装済みだが、0.86 anchor には未到達 |
| H3/H4 | `phase5_fractional_topology_analysis.md` では全 surface が `out_of_anchor_band` |
| BMW | 未起動。MC が DE2 を上回る残差を示すまで second phase に留める |

## 7. Update Contract

この protocol を変更した場合、次の面も同期する。

| 面 | 同期内容 |
|:---|:---|
| `drafts/series/論文V_繰り込みは忘却である_草稿.md` §7.2 | Proved / Diagnosed / Open の Open 面と benchmark 記述 |
| `drafts/series/論文V_繰り込みは忘却である.meta.md` §M6 C4 | 次の実化操作と判定条件 |
| `plans/P-V.6_強結合benchmark計画_v1.md` | 設計書から本 protocol への参照 |
| `drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` | 負・曖昧・未成熟な観測結果の事前帰属表 |
| `experiments/tests/test_strong_coupling_benchmarks.py` | schema / gate が変わった場合のテスト |

## 8. Rejection Ledger

| 棄却 | 理由 |
|:---|:---|
| BMW first | benchmark ではなく FRG 内部の solver extension になり、帰属判定が残る |
| DE2 外挿だけで close | 外挿は 0.86 の再現ではない |
| local stability だけで accept | cross-$n$ portability と anchor reach を満たさない |
| selector tweak の反復 | H3/H4 で全 surface が out-of-anchor のため、同じ proxy family の selector 変更だけでは情報利得が低い |

負・曖昧・未成熟な観測結果の詳細な事前帰属は `drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` に固定する。

## 9. Exit Criteria

P-V.6 の MC benchmark は、次のどれかで一段閉じる。

1. MC が DE2 と一致し、0.86 から遠い。
   → Paper IV observable / $R$ / calibration 問題へ差し戻す。
2. MC が DE2 を超え、0.86 側へ寄る。
   → BMW を起動する。
3. MC が安定しない。
   → lattice / update / finite-size scaling の protocol を作り直す。

どの場合でも、0.86 を「解いた」とは書かない。帰属判定がこの protocol の成果である。
結果解釈は、まず `drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` の failure ID に割り当ててから行う。

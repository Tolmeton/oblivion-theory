# Handoff Drift 検証レポート - AgentSwing SOURCE 昇格後 v0.2

## §1 Executive Summary

OP-X-6 の到達度は **部分** のまま。ただし 2026-04-26 の arXiv source 昇格により、根拠面は `Paper X embedded summary` から `AgentSwing arXiv source TeX/PDF` へ上がった。

今回 SOURCE として固定できるのは、Appendix case study、aligned context-management table、Figure 9 transition matrix である。raw per-turn logs / evaluation JSON / plotting CSV は未取得なので、`χ(t)` の実測、Drift-Performance 逆 U 字、全戦略の trajectory-level 比較はまだ実化していない。

重要な更新は 2 点である。

1. synthetic `χ` calibration は旧レポートから維持できる。Type 1 は low-`χ` と KLN、Type 2 は high-`χ` と DA に対応する。
2. aligned table の exact 値では、AgentSwing routing が 3 モデルすべてで Pass@1 の最良値を取る。一方、terminal precision `ρ` は固定 DA が 3 モデルすべてで最大である。

したがって安全な結論は、「DA が普遍的に最良」ではなく、**router は状態依存に finish rate と terminal precision の tradeoff を調整して勝っている**である。

## §2 SOURCE Ledger

| 面 | SOURCE |
|:---|:---|
| arXiv record | `https://arxiv.org/abs/2603.27490` |
| arXiv source | `https://arxiv.org/e-print/2603.27490` |
| aligned results | `table/01_aligned_results.tex` |
| case studies | `table/03_app_cast.tex` |
| transition matrices | `pic/transition_matrix_1x3.pdf` |
| appendix description | `sections/8_appendix.tex` |
| local structured data | `experiments/agentswing_ref_data.yaml` |
| synthetic drift output | `experiments/handoff_drift_synthesis_results.json` |
| operational mapping | `plans/codex_handoff_drift_mapping.md` |

## §3 Synthetic χ Calibration

この節は旧 Task 4 の synthetic calibration を維持する。理由は、estimator の検証対象が AgentSwing table ではなく、`V_null / V_carrier` の operational mapping だからである。

| Scenario | carrier_step / null_step | mean `χ` | p10 / p50 / p90 | `χ>1` pair | Regime |
|:---|:---:|:---:|:---:|:---:|:---|
| Type 1 clue recovery | 3 / 1 | 0.354 | 0.286 / 0.333 / 0.500 | 0 / 30 | carrier-recovery |
| Type 2 dead-end loop | 1 / 2 | 2.017 | 1.950 / 2.000 / 2.500 | 28 / 30 | drift-dominant |
| Type 3 mixed | 2 / 2 | 1.071 | 0.980 / 1.000 / 1.250 | 8 / 30 | boundary / mixed |

読み:

- Type 1 は `χ<1` で、担体回復が欠如境界の進行より速い。recent useful clue を残す KLN と整合する。
- Type 2 は `χ>1` で、欠如境界の進行が支配的である。dead-end loop を切る DA と整合する。
- Type 3 は `χ≈1` の境界域である。ただし AgentSwing arXiv source には Type 3 case がない。

## §4 AgentSwing Case Alignment

| State | arXiv case | observed optimal strategy | synthetic `χ` reading | 判定 |
|:---|:---|:---|:---|:---|
| Type 1: recent useful clue | Mando case | KLN | low-`χ` / carrier recovery | 一致 |
| Type 2: dead-end loop | live-crickets case | DA | high-`χ` / drift dominant | 一致 |
| Type 3: mixed / session boundary | AgentSwing source には無し | 未観測 | boundary `χ≈1` | 未検証 |

Case 1 では Turn 23 の `$tupid Young` clue を KLN が保持し、その後 Mando answer へ進む。Case 2 では PDF extraction loop を DA が切り、alternative extraction path から live crickets answer へ進む。

ここから言えるのは、state-dependent optimal forgetting の 2 点支持である。Type 3 を閉じるには、別 case 追加か、local rerun が要る。

## §5 Aligned Context-Management Results

### 5.1 Pass@1 と routing gain

| Model | best fixed strategy | best fixed Pass@1 | AgentSwing Pass@1 | absolute gain | relative gain |
|:---|:---:|---:|---:|---:|---:|
| GPT-OSS-120B | KLN | 0.352 | 0.418 | +0.066 | +18.8% |
| DeepSeek-v3.2 | DA | 0.329 | 0.356 | +0.027 | +8.2% |
| Tongyi-DR-30B-A3B | DA | 0.200 | 0.311 | +0.111 | +55.5% |

戦略平均:

| Strategy | Pass@1 | `η` finish rate | `ρ` terminal precision | avg turns |
|:---|---:|---:|---:|---:|
| DA | 0.272 | 0.403 | 0.701 | 302.1 |
| Sum | 0.263 | 0.774 | 0.359 | 198.6 |
| KLN | 0.289 | 0.802 | 0.374 | 180.6 |
| AgentSwing | 0.362 | 0.809 | 0.454 | 181.9 |

読み:

- DA は `ρ` が最も高いが、`η` が低い。正答できるときは強いが、finish rate が重い。
- KLN と Sum は `η` が高いが、`ρ` が低い。
- AgentSwing は `η` を KLN/Sum 水準に保ちつつ、`ρ` を固定 KLN/Sum より上げている。

したがって、AgentSwing の勝ち筋は「最も強い固定忘却」ではなく、**状態依存 routing による二指標の折衷**である。

### 5.2 Figure 9 transition matrix reading

SOURCE 値は transition matrix であり、単純な strategy frequency ではない。行を現在 strategy、列を次 strategy と読む Markov 近似を置くと、定常分布は次のようになる。

| Model | Summary | Keep-Last-N | Discard-All |
|:---|---:|---:|---:|
| GPT-OSS-120B | 0.263 | 0.244 | 0.492 |
| DeepSeek-v3.2 | 0.542 | 0.267 | 0.191 |
| Tongyi-DR | 0.573 | 0.191 | 0.236 |

この表は INFERENCE である。SOURCE は PDF label の 3x3 matrix であり、上の値は row-stochastic Markov chain として読んだ場合の派生量である。

読みとしては、routing policy はモデル依存である。GPT は DA へ寄り、DeepSeek/Tongyi は Summary へ寄る。したがって Paper X の state taxonomy は、次の実験で model-dependent prior と分離して検証する必要がある。

## §6 Paper X §6.3 Ceiling Recalculation

Paper X §6.3 の `r_obs ≤ sqrt(ρ/(K+1))` を `K=1` で評価する。

| Model | DA | Sum | KLN | AgentSwing |
|:---|---:|---:|---:|---:|
| GPT-OSS-120B | 0.586 | 0.507 | 0.486 | 0.532 |
| DeepSeek-v3.2 | 0.548 | 0.391 | 0.466 | 0.437 |
| Tongyi-DR-30B-A3B | 0.640 | 0.358 | 0.327 | 0.454 |

戦略平均 ceiling は `DA=0.591`, `Sum=0.419`, `KLN=0.426`, `AgentSwing=0.474`。

この ceiling は terminal precision 由来なので、DA が最大になる。一方、Pass@1 は `η × ρ` に近い挙動を持つため、AgentSwing が勝つ。ここを混同すると、Paper X の実験的読みを誤る。

安全な言い方:

- high-`χ` state では DA 的 reset が terminal precision を上げうる。
- low-`χ` state では KLN 的 preservation が clue を残しうる。
- routing は、その state mixture を見て `η` と `ρ` の両方を最適化する。

まだ言えないこと:

- `χ(t)` と Pass@1 の逆 U 字が実測された、とは言えない。
- AgentSwing の transition matrix だけから state-level Drift を復元した、とは言えない。
- Type 3 の最適戦略が検証された、とは言えない。

## §7 OP-X-6 / OP-XII-6 到達度

| OP | 完了基準 | 今回の到達 | 欠けているもの | 評価 |
|:---|:---|:---|:---|:---|
| OP-X-6 | AgentSwing 全戦略の Drift が `χ` で定量化される | arXiv SOURCE で Case 1/2、Table、Figure 9 を固定。synthetic `χ` と case direction は整合 | raw trajectory、戦略別時系列、state-level `χ(t)` | **部分** |
| OP-XII-6 | handoff residual `χ` が 1 媒体以上で実測される | estimator と synthetic calibration はある | Bucher / AgentSwing / Hyphē の実測 `χ(t)` | **未達** |

## §8 Branch-level Pseudo Trajectory Run

2026-04-26 に、arXiv Appendix C の all lookahead branches 6 本を turn-level pseudo trajectory へ落とし、既存 `estimate_drift` に流した。

| Artifact | Path |
|:---|:---|
| pseudo trajectory input | `experiments/agentswing_case_pseudo_trajectories.json` |
| pseudo drift output | `experiments/agentswing_case_pseudo_drift_results.json` |
| scoring audit | `experiments/agentswing_case_pseudo_scoring_audit.md` |
| scoring robustness | `experiments/agentswing_case_pseudo_robustness_results.json` |
| estimator | `20_機構｜Mekhane/_src｜ソースコード/mekhane/lethe/handoff_drift_estimator.py` |

重要な制約:

- turn text は arXiv Appendix C の table summary に基づく SOURCE である。
- `support_scores` と `margin_scores` は manual INFERENCE である。
- raw AgentSwing logs ではないため、この run は OP-X-6 の完了ではなく、case-level operationalization の dry-run である。
- scoring rubric は全 branch で同じである。carrier front は target-relevant useful unit の回復、null front は誤焦点・曖昧性・dead-end loop の拡大を表す。

### 8.1 Primary result (`p=0.5`)

| Pair | selected | outcome | `V_carrier` | `V_null` | `χ` | reading |
|:---|:---:|:---|---:|---:|---:|:---|
| `mando_DA_lookahead` | no | failure | 1.0 | 1.5 | 1.500 | clue-losing reset |
| `mando_KLN_lookahead` | yes | success-direction | 3.0 | 0.5 | 0.167 | carrier-recovery |
| `mando_Summary_lookahead` | no | failure | 1.0 | 0.5 | 0.500 | late correction |
| `live_crickets_DA_lookahead` | yes | success-direction | 1.5 | 2.0 | 1.333 | controlled high-drift |
| `live_crickets_KLN_lookahead` | no | failure | 1.0 | 2.0 | 2.000 | loop-preserving drift |
| `live_crickets_Summary_lookahead` | no | failure | 1.0 | 1.0 | 1.000 | abstraction without break |

### 8.2 Sensitivity (`p=0.9`)

| Pair | `χ_p90` |
|:---|---:|
| `mando_DA_lookahead` | 1.900 |
| `mando_KLN_lookahead` | 0.300 |
| `mando_Summary_lookahead` | 0.900 |
| `live_crickets_DA_lookahead` | 1.053 |
| `live_crickets_KLN_lookahead` | 2.000 |
| `live_crickets_Summary_lookahead` | 1.000 |

### 8.3 Reading

この dry-run は、旧 synthetic calibration の方向を branch-level に写しても壊れないことを示す。

- Mando / Type 1 では、router-selected KLN が最も低い `χ` を持つ。recent useful clue が carrier front を強く進め、null front を抑える。
- live-crickets / Type 2 では、router-selected DA が `χ>1` の controlled high-drift になる。KLN も `χ>1` だが、これは failed extraction loop を保存する drift であり、carrier が弱い。
- Summary は両 case で中間域に落ちる。構造は保つが、Mando では wrong basin correction が遅く、live-crickets では extraction bottleneck を切れない。

したがって、この段階での最小主張は次である。

> AgentSwing Appendix C の 2 case / 6 lookahead branches では、router-selected branch は state type に対応する Drift regime を持つ。ただし `χ` 単独ではなく、`V_carrier` と branch semantics を併読する必要がある。

ただし、ここでの `χ` は scoring design に依存する。次に必要なのは、manual front assignment を固定せず、judge による `support_scores / margin_scores` 生成へ置き換えることである。

### 8.4 Scoring robustness (`±1` front perturbation)

Manual front assignment への攻撃面を確認するため、各 branch の `carrier_front` / `null_front` を turn ごとに独立に `-1/0/+1` 揺らし、範囲 clamp と単調 repair だけを入れて 5000 trial を走らせた。outcome に合わせた補正は入れていない。

| criterion | pass rate |
|:---|---:|
| Mando: selected KLN has `χ < 1` | 1.000 |
| Mando: selected KLN has lowest `χ` among Mando branches | 0.844 |
| Mando: selected KLN has highest `V_carrier` among Mando branches | 0.698 |
| live-crickets: selected DA has `χ > 1` | 0.597 |
| live-crickets: selected DA has lower `χ` than KLN | 0.699 |
| live-crickets: selected DA has `V_carrier >= KLN` | 0.905 |
| live-crickets: DA controlled condition (`χ>1`, `χ<KLN`, `V_carrier>=KLN`) | 0.325 |
| both selected branches match expected `χ` regime | 0.597 |

Pair-level median `χ`:

| Pair | median `χ` | p10 | p90 | `χ>1` rate | huge `χ>10` rate |
|:---|---:|---:|---:|---:|---:|
| `mando_DA_lookahead` | 1.500 | 0.667 | 4.000 | 0.643 | 0.072 |
| `mando_KLN_lookahead` | 0.167 | 0.000 | 0.429 | 0.000 | 0.000 |
| `mando_Summary_lookahead` | 1.000 | 0.000 | 3.000 | 0.272 | 0.057 |
| `live_crickets_DA_lookahead` | 1.333 | 0.750 | 2.500 | 0.597 | 0.000 |
| `live_crickets_KLN_lookahead` | 2.000 | 1.000 | 5.000 | 0.857 | 0.073 |
| `live_crickets_Summary_lookahead` | 1.000 | 0.333 | 3.000 | 0.377 | 0.072 |

読み:

- Mando case は頑健である。KLN は `χ<1` を 100% 維持し、84.4% の trial で Mando branch 内の最低 `χ` になる。
- live-crickets case は `χ` 単独では頑健性が中程度である。DA が KLN より低い `χ` になる割合は 69.9% だが、controlled condition 全体は 32.5% に落ちる。
- したがって Paper X 側の安全な表現は、`χ` 単独による winner prediction ではない。`χ + V_carrier + branch semantics` の三点セットで、DA が harmful loop を切る状態依存操作として読める、である。

## §9 次の実化操作

次は 2 択である。

1. **annotation route**: `experiments/agentswing_case_pseudo_scoring_audit.md` を使い、第二 scorer が front 値を blind 修正する。
2. **robustness route**: perturbation を `±2` へ広げるか、case 別に perturbation の妥当範囲を制限する。
3. **実測 route**: SWE-bench real trajectory または local boot⊣bye logs に対して judge-based scoring を実装し、manual INFERENCE から SOURCE 寄りの測定へ移る。

GPU はこの段階では不要である。必要なのは turn text、judge、既存 estimator である。GPU が要るのは、open-weight agent をローカルで再実行する場合だけである。

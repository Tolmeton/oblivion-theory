# Handoff Drift 検証レポート — Brief 1 Task 4 成果物

## §1 Executive Summary

- OP-X-6 到達度は **部分**。`estimate_drift` を public API として用いた synthetic boot⊣bye 実行で、Type 1/2/3 の `χ` 序列 `0.354 < 1.071 < 2.017` を再現し、AgentSwing の case study の向きと整合した。
- OP-XII-6 到達度は **未達**。Bucher / AgentSwing / Hyphē のいずれでも `χ(t)` の実測時系列はまだ得ておらず、今回は synthetic ペアによる予備検証に留まる。
- Step 1 では 3 シナリオ各 `N=30` を `mekhane.lethe.estimate_drift` で推定し、期待帯 `Type 1 ≈ 0.3`, `Type 2 ≈ 2.0`, `Type 3 ≈ 1.0` を満たした。
- Step 2 では Type 1 の low-`χ` と `KLN` 最適、Type 2 の high-`χ` と `DA` 最適の対応を確認した。Type 3 は `forced_session_boundary` analogue として境界域 `χ≈1` に置けるが、`optimal_strategy` 自体は YAML 側で未定義である。
- Step 3 では Paper X §6.3 の `r_obs ≤ √(ρ/(K+1))` を `K=1` で評価し、Table 2 の `DA` が全 3 モデルで最大 ceiling (`0.548–0.640`) を持つことを確認した。

## §2 合成データ検証

### 2.1 実行条件

- 使用 API: `mekhane.lethe.estimate_drift`
- 生成物: `experiments/引継ぎ漂流_合成_結果.json`
- 乱数 seed: `42`
- 各シナリオ: `N=30`, `turn_count=7`, `unit_count=48`
- `handoff_drift_estimator.py` の private helper は使っていない。Task 2 テスト参照先 `_make_synthetic_pair` は現行 tree では参照できなかったため、brief 指定の `carrier_step` / `null_step` をそのまま public API 入力 (`support_scores`, `margin_scores`) に再構成した。

### 2.2 結果

| Scenario | carrier_step / null_step | mean `χ` | p10 / p50 / p90 | `χ>1` pair | 判定 |
|:---|:---:|:---:|:---:|:---:|:---|
| Type 1 clue recovery | 3 / 1 | 0.354 | 0.286 / 0.333 / 0.500 | 0 / 30 | carrier-recovery |
| Type 2 dead-end loop | 1 / 2 | 2.017 | 1.950 / 2.000 / 2.500 | 28 / 30 | drift-dominant |
| Type 3 mixed | 2 / 2 | 1.071 | 0.980 / 1.000 / 1.250 | 8 / 30 | boundary / mixed |

### 2.3 読み

- Type 1 は `χ<1` で安定し、null front の進行より carrier front の回復が優勢である。recent useful clue を保持したい場面の低 drift regime と読める。
- Type 2 は `χ>1` が支配的で、dead-end loop のような有害文脈を切るための forgetting が carrier recovery より先に必要な regime になっている。
- Type 3 は `χ≈1` に集中し、保持と切断の利得が拮抗する境界域として機能している。

## §3 AgentSwing 整合性

### 3.1 Case study 対応

| Synthetic scenario | YAML case_study | AgentSwing state_type | optimal_strategy | 合成 `χ` 解釈 | 整合性 |
|:---|:---|:---|:---|:---|:---|
| Type 1 clue recovery | `case_1_mando` | recent useful clue | `KLN` | `χ=0.354` の low-drift | 一致 |
| Type 2 dead-end loop | `case_2_live_crickets` | dead-end loop | `DA` | `χ=2.017` の high-drift | 一致 |
| Type 3 mixed | `case_3_mythos` | forced session reset analogue | `null` | `χ=1.071` の境界域 | 部分一致 |

### 3.2 論理整合

- Type 1 では useful clue の担体を残すほうが得なので、`χ<1` と `KLN` 最適は同じ向きを向く。
- Type 2 では loop 自体が有害 carrier になっているため、`χ>1` で `DA` 最適になる。これは「強い忘却が性能回復を生む」側の regime である。
- Type 3 は `Mythos` の session discontinuity analogue であり、YAML でも `KLN`/`Sum`/`DA` の最適化比較は提示されていない。ここでは境界域の説明に使えるが、戦略最適性の直接検証には使えない。

### 3.3 Table 2 との接続

Paper X から抽出された `table_2_n240` では、3 モデルすべてで `DA` の `ρ` が最大だった。

| Model | `ρ_DA` | `ρ_Sum` | `ρ_KLN` | 最大 `ρ` |
|:---|:---:|:---:|:---:|:---|
| GPT-OSS-120B | 0.686 | 0.600 | 0.525 | DA |
| DeepSeek-V3 | 0.600 | 0.486 | 0.543 | DA |
| Tongyi-qwq-32B | 0.818 | 0.571 | 0.478 | DA |

- この並びは、少なくとも Table 2 の aggregate 指標が「dead-end loop を切った後の高精度」を DA 側へ寄せていることを示す。
- synthetic 側で high-`χ` regime を Type 2 に割り当てた判断は、この `ρ_DA` 優位と矛盾しない。

## §4 Paper X §6.3 二重天井結合

### 4.1 K=1 baseline ceiling

Paper X §6.3 の命題 X.7 は

`r_obs ≤ √(ρ/(K+1))`

を与える。baseline として `K=1` を置くと `r_obs ≤ √(ρ/2)` になる。

| Model | DA | Sum | KLN |
|:---|:---:|:---:|:---:|
| GPT-OSS-120B | 0.586 | 0.548 | 0.512 |
| DeepSeek-V3 | 0.548 | 0.493 | 0.521 |
| Tongyi-qwq-32B | 0.640 | 0.534 | 0.489 |

戦略平均 ceiling は `DA=0.591`, `Sum=0.525`, `KLN=0.507`。

### 4.2 `χ` との対応

- `χ>1` の drift-dominant regime では、文脈を保持するほど performance が落ちる側の状態に入る。Type 2 がこれに当たる。
- ただし Paper X の ceiling は「最適 routing をしても超えにくい上限」であって、`χ` から直接 `r_obs` を復元する式ではない。今回の結合は **regime mapping** であり、回帰式の同定ではない。
- したがって現時点の安全な言い方は次の通りである。
  - low-`χ` (`χ<1`) では clue preservation 側の戦略が有利になりやすい。
  - high-`χ` (`χ>1`) では reset / forgetting が性能 ceiling の改善条件になりうる。
  - それでも ceiling 自体は `√(ρ/2)` に抑えられ、今回の Table 2 では最良でも `0.640` を超えない。

## §5 OP-X-6 / OP-XII-6 到達度評価

| OP | 完了基準 | 今回の到達 | 欠けているもの | 評価 |
|:---|:---|:---|:---|:---|
| OP-X-6 | boot⊣bye の Drift が AgentSwing 全戦略について `χ` で定量化される | synthetic `χ` 序列を作り、Type 1/2/3 と AgentSwing case logic を接続した | AgentSwing raw trajectory、戦略別時系列、all-strategy 実測 `χ` | **部分** |
| OP-XII-6 | `χ` が Bucher / AgentSwing / Hyphē のうち最低 1 媒体で実測値として得られる | estimator の synthetic 挙動を検証し、計測手順の一部を dry-run した | 実媒体での `χ(t)` 測定、probe space 固定、first-passage `τ_χ` の実記録 | **未達** |

### 5.1 判定理由

- OP-X-6 は「戦略ごとの drift 指標系が閉じるか」の問いであり、今回そこに向かう最初の bridge はできた。ただし raw AgentSwing を流していないので criterion には届かない。
- OP-XII-6 は criterion 文言が厳密で、**実測 medium が 1 つもない** 以上、現段階を「部分」へ繰り上げる根拠は弱い。
- よって、Task 4 の honest 判定は `OP-X-6 = 部分`, `OP-XII-6 = 未達` である。

## §6 残余と次のアクション

### 6.1 残余

- AgentSwing 原典 PDF / raw Appendix C trajectory が未取得で、case-level embedded 数値しかない。
- Hyphē または実 boot⊣bye log の JSONL pair が今回の入力に含まれていない。
- `probe space X` の固定は synthetic では `memory slot` に置いたが、Paper XII OP-XII-2 の invariance 検証は未着手。
- optional PNG は今回は生成していない。Step 2-4 の判定には不要だったため skip した。

### 6.2 次のアクション

1. AgentSwing の raw per-turn / per-chunk data を取得し、`DA/Sum/KLN` 全戦略へ同一 estimator を流す。
2. Hyphē または Hegemonikon 実 boot⊣bye log `N≥20` を pair 化し、`χ(t)` と `τ_χ` を出す。
3. `memory slot / chunk / semantic coordinate` の 3 probe space で estimator を再実行し、OP-XII-2 の invariance debt を先に減らす。

### 6.3 OP 台帳更新提案 diff

現行 read では `批判反証レジストリ.md` に standalone の `OP-X-6` エントリが見当たらず、`OP-XII-6` の説明文中でのみ参照されていた。以下は **提案 diff** であり、本文・台帳への直接編集は行っていない。

```diff
--- a/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/リファレンス/批判反証レジストリ.md
+++ b/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/リファレンス/批判反証レジストリ.md
@@
+#### OP-X-6: boot⊣bye の Drift を AgentSwing データから推定
+**内容** [SOURCE: 論文X §7 OP table]: 各 CM 戦略の Drift を `χ` で定量化し、Type 1/2/3 state と結び付ける。
+**状態案**: 🟡 部分解決
+**進捗案**: Brief 1 Task 4 により synthetic boot⊣bye `N=30×3` で `χ` mean = `0.354 / 1.071 / 2.017` を再現。Type 1 < Type 2 の序列は AgentSwing case study (`KLN` optimal / `DA` optimal) と整合。
+**残余案**: raw AgentSwing trajectory 未取得のため「全戦略の `χ` 実測」は未達。
@@
 #### OP-XII-6: Handoff Drift の定量化
 **内容** [TAINT: 外部レポート]: context 引き継ぎ時の情報損失を `χ` として定量。Hegemonikon boot⊣bye サイクルでの計測が実験台。
-**状態**: 🔵 Testable (W3 Codex 発注済み 2026-04-17 — OP-X-6 と連動)
+**状態**: 🔵 Testable (W3 Codex 発注済み 2026-04-17 — OP-X-6 と連動)
+**進捗案**: synthetic estimator は稼働確認済みだが、Bucher / AgentSwing / Hyphē のいずれでも `χ(t)` 実測値は未取得。完了基準はまだ未充足。
 ```

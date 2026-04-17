# Codex 委託 brief: Handoff Drift 定量化 (OP-X-6 + OP-XII-6)

**発注日**: 2026-04-17
**優先度**: 中
**担当論文**: Paper X §4 (boot⊣bye 随伴), Paper XII §5 (Measurement Protocol)
**関連 OP**: OP-X-6 (boot⊣bye の Drift を AgentSwing データから推定), OP-XII-6 (handoff 残差 χ の計測)
**登録元**: 批判反証レジストリ §4.2/§4.3

---

## 目的

`boot⊣bye` 随伴サイクル (= context handoff) で生じる Drift を定量化する指標系を実装し、Hegemonikon 内部のセッション引き継ぎデータから χ (= V_null/V_carrier) を推定する。外部 SOURCE (AgentSwing Feng et al. 2026) の指標系との整合性を確認する。

**最終アウトカム**: OP-X-6 と OP-XII-6 を同一指標系で閉じ、論文 X §6 と論文 XII §11 の「Testable」ステータスを「検証済/部分検証」に昇格可能にする。

---

## 背景

### SOURCE 確認済みの枠組み

- **Paper X §4.2** [SOURCE]: boot⊣bye 随伴は `L ⊣ R`、右随伴 bye (= R: Session → Memory 圧縮 = 忘却) の適用で Drift が生じる。
- **Paper X §4.4** [SOURCE]: AgentSwing の各 CM 戦略 (DA/Sum/KLN) の Drift は state-dependent。Table 1, Table 2, Fig 9 が外部 SOURCE。
- **Paper XII §5** [SOURCE]: χ = V_null/V_carrier は probe space `X` 上で定義。null 境界 `B_t^ε = ∂N_t^ε` の法線速度 / carrier front `Σ_t^{κ_c}` の法線速度の比。
- **Paper XII §3 Measurement Protocol** [SOURCE]: Bucher / AgentSwing / Hyphē 各媒体での χ 測定方法を列挙。

### 既知の不足

1. **Hegemonikon 内部 boot⊣bye ログ** の χ 抽出スクリプトは未実装
2. **AgentSwing Table 2** は外部公開データだが Hegemonikon workspace 内に取り込まれていない
3. **V_null / V_carrier の operational 定義** が LLM handoff 文脈でどう写像されるか未固定

---

## タスク (4 段階、優先度順)

### Task 1 (最優先): Handoff 指標の operational 写像 (30 分)

`boot⊣bye` サイクルで測定すべき 2 速度の operational 定義を確定する。

**入力**:
- Paper X §4 (boot⊣bye 定式化)
- Paper XII §3-§5 (χ, V_null, V_carrier の定義)
- Hyphē skill 定義 (ある場合は Hegemonikon 内部 Mekhane で位置確認)

**成果物**: `codex_handoff_drift_mapping.md` に以下を記載
- **V_carrier**: LLM handoff で何が「担体輸送速度」に相当するか (候補: δ-log-prob 復元時間 / tokens per session / 意味保存率の逆数)
- **V_null**: 「欠如境界の移動速度」に相当するもの (候補: 文脈忘却率 / 情報エントロピー勾配速度)
- **χ の計算式**: LLM文脈に写像した具体式
- **3 候補以上** を提示し、各々の計測可能性・理論的整合性・精度を評価

### Task 2: handoff_drift_estimator.py 実装 (1.5 時間)

Task 1 で選定した operational 定義を使い、Hegemonikon 内部の boot⊣bye ログから χ を推定するスクリプトを実装。

**ファイル名**: `20_機構｜Mekhane/_src｜ソースコード/mekhane/lethe/handoff_drift_estimator.py`
(既存 Mekhane モジュール構造に合わせ配置)

**仕様**:
- **入力**: JSONL 形式の session 対 (pre-handoff, post-handoff)
  - もしくは Hyphē ログディレクトリのパス
- **処理**:
  - 各 handoff イベントで V_carrier, V_null を測定
  - χ_i = V_null_i / V_carrier_i を計算
  - χ の分布統計 (mean, std, quantile)
- **出力**:
  - CSV: `handoff_drift_results.csv` (各 handoff イベントの χ)
  - JSON: `handoff_drift_summary.json` (統計量 + Paper XII の予測との比較)
  - PNG: `chi_distribution.png` (χ のヒストグラム)

**テスト**:
- 合成データ 100 サンプル (既知の χ = 0.5 を埋め込み) で estimator 精度確認
- pytest で assertion

### Task 3: AgentSwing 外部 SOURCE の取り込み (30 分)

Paper X が参照する AgentSwing データ (Table 1, 2, Fig 9) を Hegemonikon workspace に構造化取り込み。

**成果物**: `experiments/agentswing_ref_data.yaml`
- Table 1: 戦略 × モデル の成功率
- Table 2: 3 モデル × aligned cases の N=240 統計
- Fig 9: state-dependent 最適戦略マップ
- SOURCE URL と version 番号を明記

取り込めない箇所は「未取得 (要論文 PDF 精読)」として flag。

### Task 4: Drift vs Performance 二重天井の検証 (1 時間)

Paper X §6.3 の「メタ二重天井予測 `r_obs ≤ √(ρ/(K+1))`」を Task 2 の χ 推定結果と組み合わせて予備検証。

**成果物**: `codex_report_handoff_drift.md` に以下を記載
- 合成データ + 内部 boot⊣bye ログ での χ 分布
- Paper X 予測 X.6 (F_par ⊣ G_route 統計的随伴) との整合性
- Paper XII OP-XII-6 の完了基準 (後述) への到達度
- 残る課題 (Task 3 で未取得の AgentSwing データ 等)

---

## 成功基準

| ID | 基準 |
|:---|:---|
| S1 | Task 1 の operational 写像が 3 候補以上、各候補に計測可能性評価付き |
| S2 | handoff_drift_estimator.py が合成データで χ = 0.5 ± 0.05 の精度で復元 |
| S3 | Hegemonikon 内部 boot⊣bye ログ N ≥ 20 で χ 分布を推定 |
| S4 | AgentSwing Table 2 の数値を Hegemonikon workspace に構造化取り込み |
| S5 | Paper X 予測 X.6 と Paper XII OP-XII-6 の両方に直接リンク可能な指標系が確立 |

**OP-X-6 完了基準**: boot⊣bye の Drift が AgentSwing 全戦略について χ で定量化される
**OP-XII-6 完了基準**: handoff 残差 χ が実測値として Paper XII §5 Measurement Protocol の 3 媒体 (Bucher/AgentSwing/Hyphē) のうち最低 1 つで得られる

---

## Failure Condition (停止条件)

以下が発生した場合、Codex は Tolmetes に報告し停止:

1. Task 1 で operational 写像が 1 候補も見つからず、Paper X/XII の定式化に本質的欠陥がある可能性がある場合
2. Task 2 で合成データでの復元精度が 10% を超える誤差を持つ場合 (estimator 自体が不健全)
3. AgentSwing データの取得が著作権・ライセンス的に不可能で、代替の外部データもない場合

---

## 委託範囲外 (明示)

- **Codex がやらないこと**:
  - Paper X/XII の本文改訂 (Tolmetes 担当)
  - AgentSwing 論文の全文 scrape (要 Hegemonikon Periskopē 使用、別 brief)
  - 新規 LLM handoff 実験の実施 (要 API quota、別 brief)

- **本 brief の出力は advisor review 対象**:
  - Codex 完了後、Claude (advisor) が成果物をレビューし、Tolmetes へ要約

---

## 参考正本 (事前 Read 推奨)

1. `03_忘却論｜Oblivion/drafts/series/論文X_ContextRotは忘却である_草稿.md` §4-§6
2. `03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である_草稿.md` §3-§5, §8
3. `03_忘却論｜Oblivion/drafts/infra/リファレンス/批判反証レジストリ.md` §4.2 OP-X-6, §4.3 OP-XII-6
4. 既存類似 brief: `plans/codex_brief_liang6_phaseB_reproducibility.md` (形式参考)
5. 既存 Mekhane Lethe モジュール (`20_機構｜Mekhane/_src｜ソースコード/mekhane/lethe/`) — 配置先確認

---

## 成果物一覧

- [ ] `codex_handoff_drift_mapping.md` (Task 1)
- [ ] `mekhane/lethe/handoff_drift_estimator.py` (Task 2)
- [ ] `experiments/agentswing_ref_data.yaml` (Task 3)
- [ ] `plans/codex_report_handoff_drift.md` (Task 4, 最終報告)
- [ ] pytest が通ること
- [ ] OP-X-6 と OP-XII-6 のステータス更新提案 (diff 形式)

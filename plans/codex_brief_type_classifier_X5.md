# Codex 委託 brief: Type 1/2/3 状態分類器 (OP-X-5)

**発注日**: 2026-04-17
**優先度**: 中
**担当論文**: Paper X §2 (Case Study), §5 (予測), §6 (Open Problems)
**関連 OP**: OP-X-5 (Type 1/2/3 分類器: 状態型を自動判定し最適 CM 戦略を予測するモデル)
**登録元**: 批判反証レジストリ §4.2

---

## 目的

AgentSwing Case Study で観測される 3 状態型 (Type 1/2/3) を、context feature から自動判定する分類器を実装する。Paper X §2 の分類を operational にし、CM (Context Management) 戦略の適応的選択を可能にする。

**最終アウトカム**: Paper X §6 予測 X.2 「状態依存最適忘却」の Testable 要件を満たし、OP-X-5 を「Testable」→「検証済」に昇格。

---

## 背景

### SOURCE 確認済みの枠組み

Paper X §2 で定義される 3 状態型 [SOURCE: 論文X §2, line 89-91]:

| 状態型 | 特徴 | 最適 CM 戦略 | 忘却強度 |
|:---|:---|:---|:---|
| **Type 1: recent useful clue** | 直近に有望な手がかりがある | KLN (Keep Last N) | 弱い忘却 |
| **Type 2: dead-end loop** | 繰り返しのループに陥っている | DA (Discard All) | 強い忘却 |
| **Type 3: correct hypothesis, wrong action** | 仮説は正しいが行動が不適切 | Sum では不十分 | 中程度 + 行動摂動 |

**Paper X §2 撤回条件** [SOURCE line 97]: N ≥ 10 の大規模 Case Study で Type 1/2 分類が予測精度 < 60% のとき。

**関連予測** [SOURCE 論文X §6]:
- **P-E2a** [推定 70%]: Summary は σ 非単射性により Type 1 で有害
- **P-E2b** [推定 70%]: DA は全リセットにより Type 1 で有害

### 既知の不足

1. Type 1/2/3 の operational 特徴定義が Paper X 本文に明示なし (Case Study 事例記述のみ)
2. 分類器の入力 feature vector が未定義 (context embedding? trajectory signature? logit distribution?)
3. 訓練データ: AgentSwing Case 1+2 の N=2 のみ [SOURCE: Paper X §2] → N≥10 への拡張が必要

---

## タスク (4 段階、優先度順)

### Task 1 (最優先): 状態型の operational 特徴定義 (1 時間)

Paper X §2 の 3 状態型を、測定可能な context feature の関数として定義する。

**入力**:
- Paper X §2 Case 1, Case 2 の詳細記述
- Paper X §3-§4 (forgetting functor 族 U_R, boot⊣bye 随伴)
- (任意) 既存 LLM reasoning trajectory 分析文献

**成果物**: `codex_type_features_spec.md` に以下を記載
- **Type 1 特徴** (候補):
  - (a) 直近 k=3 ターンの logit 最大値が閾値 τ_1 を超える
  - (b) trajectory 後半で Q(response) > Q(context) (品質単調増加)
  - (c) 意味的密度 (Paper X §5.3 の τ) が上昇傾向
- **Type 2 特徴** (候補):
  - (a) 同一行動の反復頻度が閾値 r_2 を超える
  - (b) trajectory が閉ループを形成 (固定点への収束)
  - (c) σ (要約) 固着率が閾値を超える
- **Type 3 特徴** (候補):
  - (a) 仮説品質 Q_hyp が高いが行動品質 Q_act が低い
  - (b) context vs action の embedding 距離が発散
- **3 候補以上 per type** を提示し、各々の計測コスト・予測精度見込みを評価

### Task 2: type_classifier.py 実装 (2 時間)

Task 1 で選定した特徴を使う分類器を実装。

**ファイル名**: `20_機構｜Mekhane/_src｜ソースコード/mekhane/lethe/type_classifier.py`

**仕様**:
- **入力**: context trajectory (list of turns with logits/embeddings)
- **特徴抽出**: Task 1 の仕様に従い feature vector 生成
- **分類器候補** (3 つ以上、比較):
  - (A) ロジスティック回帰 (baseline)
  - (B) Random Forest (特徴量重要度分析)
  - (C) 小型 Transformer (context-aware)
- **出力**:
  - 予測 Type ∈ {1, 2, 3}
  - 各タイプの確率分布
  - 予測根拠 (特徴量寄与度)

**テスト**:
- 合成 trajectory 100 サンプル (Type 1/2/3 を 30+30+30+10 rare で生成) で精度評価
- pytest で分類精度 ≥ 60% (Paper X §2 撤回条件の下限)

### Task 3: 訓練データセット作成 (1.5 時間)

Paper X §2 Case Study N=2 を N≥10 に拡張するため、合成 trajectory を生成。

**成果物**: `experiments/type_classifier_trainset.jsonl` (N=50 目標)

**生成方法**:
- **Type 1 生成**: context に有望な手がかりを埋め込み、最後のターンでそれが活かされる ideal 軌跡
- **Type 2 生成**: 同一行動が k=3 回以上繰り返される ideal ループ軌跡
- **Type 3 生成**: 仮説は正しいが行動が外れる軌跡 (例: 正しい仮説表明 → 無関係な行動)
- 各軌跡に ground truth Type ラベルを付与

**ラベル検証**: Codex が生成した軌跡を別モデル (例: 簡易ヒューリスティック) で cross-check。

### Task 4: 検証と CM 戦略ルーターの proposal (1 時間)

分類器を Paper X §6 予測 X.2 と統合し、state-dependent 最適戦略選択の proposal を作成。

**成果物**: `codex_report_type_classifier.md` に以下を記載
- 分類精度 (baseline / RF / Transformer 比較表)
- Paper X §2 撤回条件との対応 (精度 ≥ 60% の確認)
- Paper X §6.1 予測 X.2 (状態依存最適忘却) の empirical 裏付け
- CM ルーター proposal: Type 予測 → 戦略選択 (Type 1→KLN, Type 2→DA, Type 3→要実験)
- 残る課題 (Type 3 用の perturbation 戦略, 実データでの再現)

---

## 成功基準

| ID | 基準 |
|:---|:---|
| S1 | Task 1 の特徴定義が Type ごとに 3 候補以上 |
| S2 | type_classifier.py が合成データで ≥ 60% 精度 (Paper X 撤回条件下限) |
| S3 | N ≥ 10 の訓練データ (50 目標) が生成され、ラベル品質が cross-check 済 |
| S4 | 3 分類器 (LR / RF / Transformer) の比較表が存在 |
| S5 | Paper X §6.1 予測 X.2 への empirical evidence が提示される |

**OP-X-5 完了基準 (緩和版)**: 合成データで 60% 精度、実データへの拡張経路が明示される

---

## Failure Condition (停止条件)

1. Task 1 で Type 3 の operational 特徴が定義できない (Paper X §2 の「correct hypothesis, wrong action」が測定不能な概念である可能性) → Tolmetes 判断要
2. Task 2 で合成データ精度 < 40% (特徴定義 or 分類器設計に本質的欠陥)
3. Task 3 で訓練データ生成に LLM API が必要だが quota 不足

---

## 委託範囲外 (明示)

- **Codex がやらないこと**:
  - 実 LLM trajectory の大規模収集 (要 API quota)
  - Paper X §2 本文の改訂 (Tolmetes 担当)
  - Type 3 用の具体的 perturbation 戦略設計 (OP-X-5 拡張で別 brief)

- **本 brief の出力は advisor review 対象**:
  - Codex 完了後、Claude (advisor) が成果物をレビューし、Tolmetes へ要約

---

## 参考正本 (事前 Read 推奨)

1. `03_忘却論｜Oblivion/drafts/series/論文X_ContextRotは忘却である_草稿.md` §2 (Case Study), §5.3 (τ-r 関係), §6 (予測)
2. `03_忘却論｜Oblivion/drafts/infra/リファレンス/批判反証レジストリ.md` §4.2 OP-X-5
3. 既存類似 brief: `plans/codex_brief_liang6_phaseB_reproducibility.md` (形式参考)
4. 既存 Mekhane Lethe モジュール (`20_機構｜Mekhane/_src｜ソースコード/mekhane/lethe/`) — 配置先

---

## 成果物一覧

- [ ] `codex_type_features_spec.md` (Task 1)
- [ ] `mekhane/lethe/type_classifier.py` (Task 2)
- [ ] `experiments/type_classifier_trainset.jsonl` (Task 3)
- [ ] `plans/codex_report_type_classifier.md` (Task 4, 最終報告)
- [ ] pytest が通ること (≥ 60% 精度 assertion)
- [ ] OP-X-5 のステータス更新提案 (diff 形式)

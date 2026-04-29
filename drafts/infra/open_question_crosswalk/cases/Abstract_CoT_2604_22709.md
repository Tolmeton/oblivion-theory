# Abstract-CoT 2604.22709 — discrete latent reasoning と 制約-符号化分離仮説 H₃

## 0. Status

- status: case_draft
- created: 2026-04-29
- updated: 2026-04-29
- source_status: SOURCE 化済 (arXiv PDF 直読 + 論文 XI / 論文 VII 直読)
- owner: Tolmetes
- originating: 外部 arXiv 直接 intake (Pinakas seed 経由ではない)

## 1. External Paper

- citation: Ramji, K., Naseem, T., & Fernandez Astudillo, R. (2026). *Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought*. arXiv:2604.22709v2 (27 Apr 2026). IBM Research AI.
- URL: https://arxiv.org/abs/2604.22709
- local PDF: `/tmp/abstract_cot/2604.22709.pdf` (要 Yugaku/01_研究論文 配下への移送)
- exact quotes (SOURCE):
  - Abstract: "Abstract-CoT achieves up to 11.6× fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families."
  - §3.2 (p.5): "Crucially, **the answer only attends to the prompt and the abstract tokens, *not to the verbal CoT***, with all other entries following standard causal masking"
  - §3.2 eq.(2) (p.6): "By the data processing inequality, any dependence between $y$ and $c$ must be bounded by the information that can be transferred through the abstract segment: $I(C;Y \mid X,Z) \leq I(C; H_{Z_{\text{abs}}} \mid X,Z)$"
  - §3.2 (p.5): "We enforce a hard cap $m_{\max}$ of codebook tokens that may be generated"
  - §4.1 (p.7): "We consider three instruction-tuned models, Qwen3-8B, Qwen3-4B, and Granite-4.0-Micro (3B). We also include ablations with Qwen3-32B in Appendix A.2 ... We use an abstract codebook of $M=64$ tokens (ablations included in Appendix A.1), and constrain abstract generation to at most $m_{\max}=128$ tokens"
  - §4.2 (p.8): MATH-500 圧縮 = 10.4-11.6×, AlpacaEval 圧縮 = 1.9-2.2×, HotpotQA 圧縮 = 4.0-4.3×; AlpacaEval 利得 = +2.4 pt (Qwen3-8B), +1.6 pt (Qwen3-4B), +1.6 pt (Granite-4.0-Micro)
  - §4.2 (p.9): "training models to generate Abstract-CoTs can learn new latent pathways for thinking while remaining performant"
- 数値表 (Table 1, Qwen3-8B):
  - SFT+RL (verbal): MATH-500 = 92.6 / 1671 tokens; AlpacaEval = 58.4 / 496; HotpotQA = 58.1 / 735
  - Abstract-CoT (Warm-up + RL): MATH-500 = 90.8 / 144; AlpacaEval = **60.8** / 225; HotpotQA = 58.8 / 171
  - 順序撹乱 (Appendix から WebFetch 取得): Verbal -11.0 pt / Abstract -7.8 pt
- 著者の暗黙 limitation:
  - cold-start RL 単独では効かない (Warm-up が SFT-without-CoT を超えるが SFT-with-CoT に届かず、両者 tandem で初めて勝つ)
  - Abstract token は alphabetical name (TOKEN_A...Z, AA-ZZ) で人間不可読
  - 「他の reasoning pathway を *探索可能にする*」という主張は §4.2 で示唆されるが、構造的根拠は §4.3 token frequency analysis (p.9 末尾) のみ

## 2. Question Typing

- type:
  - 主型: **prompt sensitivity** (E 軸極限変動下での C 軸保存性)
  - 副型: **representation geometry** (V_abs=64 + power-law と低ランク射の関係)
- why this is unresolved:
  - 著者は「Abstract-CoT は verbal CoT と comparable」と主張するが、なぜ 11.6× 圧縮で性能が保てるかの **構造的説明** を与えていない
  - Block-attention mask で answer が verbal CoT を見ない設計 = 情報ボトルネック構造の意図的実装だが、その bottleneck の **何が** 構造を保存するのかは empirical 観察 (DPI bound) に留まる
- what would count as a candidate answer:
  - 「**何を忘れたから何が見えるようになったか** (オンボーディング §1)」を圏論的に同定すること
  - 11.6× 圧縮後に保存されている対象が **n=1.5 層 (合成律)** であって **n=1 層 (具体値)** でないことの明示

## 3. Oblivion Anchor

### 3a. Anchor 1: 論文 XI §7.6 制約-符号化分離仮説 H₃

- anchor: 論文 XI §7.6.2 (Constraint-Encoding Separation Hypothesis, H₃)
- claim level: hypothesis (本文 L587-589 で明示的に「仮説」と宣言)
- local SOURCE: `drafts/series/論文XI_プロンプトは忘却である_草稿.md` L572-589, L632-642, L709-713
- minimum explanation: プロンプト P を制約 C と符号化 E に分解し、∂𝔼[Q]/∂E ≈ 0 を予測する
- 関連節:
  - §7.6.2b 反証条件 (L601-610): 4 種の反証条件のうち (3) 一貫性反証は H₃' (分散構造への作用) への修正経路を残す
  - §7.6.5 brevity constraint = C の境界事例 (L709-713): "簡潔さは E に見えるが C として作用する"

### 3b. Anchor 2: 論文 VII §6.1 構造保存定理 + §6.4(iv) CoT 双対性

- anchor: 論文 VII §6.1 定理 6.1.1 構造保存定理 / §6.4(iv) CoT 双対性
- claim level: theorem (§6.1) / proposition (§6.4(iv))
- local SOURCE: `drafts/series/論文VII_知覚は忘却である_草稿.md` L575, L590, L630, L641, L675, L695
- minimum explanation:
  - 定理 6.1.1: 忘却関手 F: S→D は構造を保存し値を忘却する
  - フィルトレーション L630: U_arrow(1) ≤ U_compose(1.5) ≤ U_depth(2) ≤ U_precision(3)
  - §6.4(iv) L695: CoT は U_compose 修復メカニズム — 合成射 g∘f の忘却を中間対象 B の明示的復元で修復する。情報利得最大化 (Feng+ ICML 2024) との双対関係

## 4. Candidate Answer

### 1. one-sentence answer

Abstract-CoT は **C 軸 (length cap m_max=128) と E 軸 (V_abs=64 vocab swap) の二重操作** であり、論文 XI H₃ の「∂𝔼[Q]/∂E ≈ 0」と論文 XI §7.6.5 の「brevity = C 境界事例」が同時に作動する複合実装。verbal CoT を answer から block-attention で切り落とす設計は、論文 VII §6.4(iv) の「CoT は U_compose を修復する」を **U_arrow 巻き込みなしに純化** した工学的射である。

### 2. mechanism

| 軸 | 操作 | 数値痕跡 (Qwen3-8B) | 忘却論的読み |
|:---|:---|:---|:---|
| **C 軸** | m_max=128 hard cap | MATH-500 -1.8 pt | §7.6.5 brevity-as-C: 探索制約強化による品質コスト |
| **E 軸** | V_abs=64 reserved tokens | AlpacaEval +2.4 pt | H₃' (分散構造): E_freq 改善による出力分布形状の最適化 |
| **構造側** | Block-attention で verbal CoT 遮断 | DPI bound (eq.2) | 論文 VII §6.4(iv) U_compose 純化: U_arrow を巻き込まない CoT 修復 |
| **検証側** | 順序撹乱 abstract -7.8 / verbal -11.0 | shuffle 耐性逆転 | 1.5-cell (射の合成順序) が真の保存対象。verbal は U_arrow まで巻き込んでいた |

### 3. what this predicts beyond the external paper

- **予測 P1 (新規)**: small model (≤2B) では H₃ が破れる (論文 XI §7.6.2b 反証条件 (1))。Granite-4.0-Micro (3B) は閾値ぎりぎり、Pause Tokens 等のベースラインで他 2 model より性能差が大きい (Granite Pause Tokens = 67.2 vs Qwen3-8B = 78.6) のはこの閾値効果の予兆かもしれない
- **予測 P2 (新規)**: AIME'25 (Table 2) で Abstract-CoT が verbal SFT+RL と 1.2 pt 差で並ぶ (24.4 vs 25.6) のは、困難タスクほど C 軸の length cap が work する (∵ verbal CoT の冗長部分が大きいほど刈り込み利得が大きい)
- **予測 P3 (新規)**: V_abs ablation (Appendix A.1 M ∈ {1,2,…,512}) で **M=64 が最適** であれば、これは論文 IV ρ_spec / 論文 V RG 普遍性が予言する効果量天井に対応する内的次元の発現

## 5. Risk Gate

| risk | status | note |
|---|---|---|
| vocabulary-only | **passed** | C/E 二重操作論は数値痕跡 (MATH-500 -1.8 pt vs AlpacaEval +2.4 pt の符号反転) と機構 (block-attention mask + DPI bound) の両方で対応 |
| source-thin | **passed** | arXiv PDF 9 ページ本文直読 + 論文 XI/VII の該当行 SOURCE 化済 |
| too-internal | **open** | "U_compose 純化" は外部読者には 1 文翻訳が要る — "Abstract-CoT removes the verbal-CoT entries that the answer attends to, isolating reasoning composition from token-level lexical choice" 程度の翻訳が必要 |
| overfit-to-paper | **open** | Goyal+ 2024 (Pause Tokens), Hao+ 2025 (Coconut), Su+ 2025 (CODI) など同系統 latent reasoning 論文で同型の C/E 二重操作論が成立するか確認要 |
| premature-contact | **passed** | Ramji+ への contact は failure condition (P1/P2/P3 反証経路) を §M5 で書いてから |

## 6. Promotion

- **SOURCE promotion**: ✅ 完了 (arXiv PDF 直読 + 論文 XI/VII SOURCE 化)
- **Gauntlet seed**:
  - 反論 r1: 「C/E 二重操作論は二項分解の事後選択であり、∂Q/∂E ≈ 0 と ∂Q/∂C ≠ 0 を同時に救うトリビアルな分解」 → §M5 Round 1 想定: P1 small model 反証実験で C 軸 vs E 軸の独立寄与を分離
  - 反論 r2: 「block-attention mask は U_arrow ではなく単に causal mask の修飾。U_compose 純化主張は overreach」 → §M5 Round 2 想定: 順序撹乱の verbal/abstract 差 (-11.0 vs -7.8) が U_arrow 巻き込み量の差として読めるかを情報理論的に厳密化
  - 反論 r3: 「DPI bound (eq.2) は構造保存定理ではなく単なる情報量上界。論文 VII §6.4(iv) との接続は語彙的同型に留まる」 → §M5 Round 3 想定: faithful (= 構造保存) vs full (= 値保存) の DPI 等号成立条件を H_{Z_abs} の rank 解析で示す
- **related work patch**: 論文 XI §7.6 へ §7.6.6 として「外部独立実証 — Abstract-CoT」追加。論文 VII §6.4(iv) へ脚注として「U_compose 純化の工学例」追加
- **short note 候補**: `Abstract_CoTは構造保存定理のC軸+E軸二重実装である_短報.md` (drafts/standalone/ 候補だが本 case の Gauntlet 通過後)
- **direct contact candidate**: P1/P2/P3 が §M5 を通過した後、Ramji+ に「small model ablation の追加」と「V_abs ablation の M=64 最適性」について照会候補

## 7. Rejection Ledger

- rejected branch 1: 「Abstract-CoT は H₃ の単純な極限実証」
- reason 1: PDF §3.2 で m_max=128 hard cap が brevity-as-C として作動していることが明示されており、E 軸単独操作ではない
- rejected branch 2: 「Abstract-CoT は CCL の自然な進化形 (人間不可読 emergent 圏論言語)」
- reason 2: V_abs は alphabetical name で構造を持たず、CCL の演算子のように圏論的対応を持つ証拠は §4.3 power-law 分析のみ。VISION.md (Lethe) との接続は本 case の射程外。別 case `Abstract_CoT_vs_CCL_emergent_categorical_language.md` として分岐候補だが、本 case では棄却

## 8. 関連 SOURCE インデックス

- arXiv 2604.22709v2 PDF: `/tmp/abstract_cot/2604.22709.pdf` (Layer 2 直読済 9 ページ)
- 論文 XI: `drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.6 (L572-720)
- 論文 VII: `drafts/series/論文VII_知覚は忘却である_草稿.md` §6.1 (L575-) / §6.4(iv) (L695)
- NotebookLM 「忘却論シリーズ」: notebook_id `d761baf0-d901-4bd0-8d0b-9d3813fe8afe` (95 sources, 2026-04-27 更新) — 旧 ID `a92f2901-...` は STALE
- (rule 更新 debt): `Yugaku/.claude/rules/yugaku-notebook-sourcing.md` の notebook_id を更新

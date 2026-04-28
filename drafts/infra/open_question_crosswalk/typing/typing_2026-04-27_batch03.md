# Open Question Crosswalk — Typing Batch 03

- 作成日: 2026-04-27
- 入力: `../intake/intake_2026-04-27_batch03.md`
- 型カタログ: `../question_type_catalog.md`
- 目的: Bergsträßer-Cotterell-Lin (2025) の未解決問・限界を、忘却論 anchor 探索前の問い型へ分類する。

## Phase 0 — Candidates

受け取り:

| input | 件数 | status |
|---|---:|---|
| OQ-B03 intake rows | 1 | arXiv PDF 直読 SOURCE |
| domain scope seeds | 0 | — |

棄却:

| branch | 理由 |
|---|---|
| QT-EMERGENCE 単独 | 二重指数 gap は emergence 議論ではなく representation 効率の量化。emergence 型に閉じ込めると本論文の verification 軸が消える。 |
| QT-CONTEXT 単独 | Context Rot との接続候補はあるが (派生主張)、本論文は context degradation を扱わない。型分類段階では棄却。 |
| QT-COMP-GEN 単独 | succinctness は圧縮幾何だが、本論文の punchline は formal verification の硬い結論である。COMP-GEN 単独では verification 側の anchor 接続が弱まる。 |

## Phase 1 — Evaluation Criteria

| criterion | 判定方法 |
|---|---|
| C1 欠落の主語 | UHAT の verification cost (EXPSPACE) の練習用工具化、softmax / arbitrary-precision への拡張、representation 効率と検証コストの双対関係。 |
| C2 問いの作用 | (a) 検証可能性の硬い天井 (formal verification 型)、(b) 圧縮の量化 (compression-generalization 型)、(c) 形式言語と neural 表現の bridge (syntax-semantics 型)。 |

## Phase 2 — Type Assignment

| OQ ID | primary type | secondary types | 根拠 | mapping note |
|---|---|---|---|---|
| OQ-B03-001 | QT-FORMAL-VERIF | QT-COMP-GEN, QT-SYN-SEM | 主結果は EXPSPACE-completeness — UHAT の検証は本質的に困難。succinctness gap は「圧縮側の量」として読み replaceable に COMP-GEN へ流せるが、verification 側で**両側 bound が一致**する点が本論文の独自性。formal language theory ↔ neural network の syntax-semantics bridge も同時に構築している。 | Lane C (formal coherence) の primary 候補。Lane A (compression geometry) と Lane C の橋として読む。OQ-B01-002 (mechanistic interpretability) の symbolic reduction と並列。 |

## Phase 3 — Type Distribution

| primary type | count | OQ IDs | 解釈 |
|---|---:|---|---|
| QT-FORMAL-VERIF | 1 | OQ-B03-001 | 既存 QT-FORMAL-VERIF (OQ-B01-002 の 1 件) に加わる 2 件目。UHAT の検証硬さを「圧縮の代償」として読む anchor 候補が立ち上がる。 |

## Phase 4 — Split Queue

| parent OQ | split reason | child candidates |
|---|---|---|
| OQ-B03-001 | 4 つの未解決問が独立 | `OQ-B03-001a` future work: practical verification of transformers (実機ツール化), `OQ-B03-001b` softmax / arbitrary-precision への拡張可能性, `OQ-B03-001c` star-free 閉じ込み外への拡張, `OQ-B03-001d` Zipf / Hindu-Arabic 観点での "succinctness ≈ U" 哲学的接続 |

## Carry Forward

次段の anchor 探索 priority:

| rank | target | 理由 |
|---|---|---|
| 1 | QT-FORMAL-VERIF + QT-COMP-GEN | 「圧縮の量化」と「検証の硬さ」が **同じ n に対し doubly-exponential で一致** することは、忘却論の `U⊣N` 経済性の matched bound 候補として最強。`mapping_QT-COMP-GEN_2026-04-26.md` の Kolmogorov source-thin gap への代替 anchor として組み込む。 |
| 2 | QT-SYN-SEM | UHAT-LTL bidirectional translation は formal syntax (LTL) と learned semantics (transformer attention) の bridge。Paper XI の C-E 分離 ($E_{\text{struct}}$ = 構造記法) との接続候補。 |
| 3 | OQ-B03-001a の practical verification | Paper IV / Paper IX の実験面と接続しやすいが、本論文は理論的主張のみ。case 化前に local anchor 強化が必要。 |

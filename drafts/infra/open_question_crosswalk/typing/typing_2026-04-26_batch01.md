# Open Question Crosswalk — Typing Batch 01

- 作成日: 2026-04-26
- 入力: `../intake/intake_2026-04-26_batch01.md`
- 型カタログ: `../question_type_catalog.md`
- 目的: 第一 intake batch の open question / limitation / future work を、忘却論 anchor 探索前の問い型へ分類する。

## Phase 0 — Candidates

受け取り:

| input | 件数 | status |
|---|---:|---|
| OQ-B01 intake rows | 16 | arXiv PDF 直読 SOURCE |
| domain scope seeds | 12 | WEAK INPUT。今回は補助分類のみ |

棄却:

| branch | 理由 |
|---|---|
| field-only classification | 分野名だけで型を決めると vocabulary-only になるため棄却。 |
| single-axis classification | emergence/context/representation だけでは formal verification, measurement deformation, closure failure を吸収できないため棄却。 |
| oblivion-anchor-first classification | まだ local 忘却論 anchor を読んでいないため、外部論文側の欠落から先に分類する。 |

## Phase 1 — Evaluation Criteria

| criterion | 判定方法 |
|---|---|
| C1 欠落の主語 | 著者が「何が未解決」と言っているか。feature, verification, loop, metric, geometry など。 |
| C2 問いの作用 | 説明が足りないのか、測定が歪むのか、境界が閉じないのか、別系へ移らないのか。 |
| C3 mapping 有用性 | 次段で忘却論 theorem/proposition/concept を探すとき、検索 anchor が狭くなるか。 |

## Phase 2 — OQ Typing Matrix

| OQ ID | primary type | secondary type | 判定理由 | next action |
|---|---|---|---|---|
| OQ-B01-001 | QT-REP-ONTO | QT-DECOMP-REC | feature の正体と network decomposition の理論基礎が欠けている。まず「単位は何か」の問い。 | MI feature / superposition を representation ontology case に昇格。 |
| OQ-B01-002 | QT-FORMAL-VERIF | QT-DECOMP-REC, QT-SYN-SEM | toy model 的理解を frontier formal verification へ拡張できるか、NN計算を symbolic code に還元できるかが中心。 | symbolic reduction の限界として case 化。 |
| OQ-B01-003 | QT-TRANSFER-INV | QT-REP-ONTO | MI の知見・手法が architecture / modality を跨ぐかという不変性の問い。 | Transformer-specific vs substrate-independent の判定軸を作る。 |
| OQ-B01-004 | QT-META-AGENDA | QT-GROUNDING, QT-MEAS-DEFORM | 14 topics / 45 directions の束。単一の問いではなく、child OQ に分割すべき agenda。 | reasoning, grounding, culture, applied NLP へ分割。 |
| OQ-B01-005 | QT-MEAS-DEFORM | QT-GROUNDING | memorized pattern と reasoning/knowledge の区別、contamination / Goodhart / reliable metrics が中心。modal fusion は grounding 側。 | reasoning benchmark と multimodal grounding を分ける。 |
| OQ-B01-006 | QT-CLOSURE | QT-GROUNDING | LLM の action-perception loop が閉じていないことが主問題。self-identification と future training feedback が境界維持に接続。 | closure failure case として保持。 |
| OQ-B01-007 | QT-COMP-GEN | QT-DECOMP-REC | 過大モデルが random labels を記憶できるのになぜ一般化するか。巨大モデルを simple と見る測度が未発見。 | effective simplicity / learning-as-forgetting anchor を探索。 |
| OQ-B01-008 | QT-COMP-GEN | QT-GEOM-OBSTR | IB の情報平面上で hidden layers が異なる点へ収束する理由。圧縮過程と幾何的収束点の問い。 | IB / GeoIB / α-connection anchor を探索。 |
| OQ-B01-009 | QT-EMERGENCE | QT-COMP-GEN | deep が shallow より効率的になる関数クラス境界、no-flattening theorem の射程。閾値的効率の問い。 | depth efficiency as emergence case にする。 |
| OQ-B01-010 | QT-CLOSURE | QT-GEOM-OBSTR | Markov blanket の構成粒子が交換・更新される場合、blanket identity をどう保つか。wandering sets が境界維持の障害。 | MB persistence / renewing boundary case にする。 |
| OQ-B01-011 | QT-CONTEXT | QT-MEAS-DEFORM | extended-context models が入力文脈をどう使うか不明で、長文脈化が利用能力を保証しない。 | Context Rot / non-uniform forgetting anchor を探索。 |
| OQ-B01-012 | QT-MEAS-DEFORM | QT-REP-ONTO, QT-DECOMP-REC | どの representation を抽出し、どの metric で alignment を測るかが結論を変える。representation と computation の関係も残る。 | alignment metrics と representation role を分割候補にする。 |
| OQ-B01-013 | QT-EMERGENCE | QT-MEAS-DEFORM | emergent abilities の発生条件・予測可能性が問い。一方 Mirage 論文が metric-induced artifact を突く。 | emergence mechanism と measurement deformation の paired case。 |
| OQ-B01-014 | QT-GEOM-OBSTR | QT-COMP-GEN | Kolmogorov complexity / Shannon entropy の inequality/profile 構造、secret key の限界が未解決。構造存在条件の問い。 | information inequality / common secret を別 case に分ける。 |
| OQ-B01-015 | QT-GEOM-OBSTR | QT-REP-ONTO | divergence, α-connection, infinite-dimensional IG, operator Sinkhorn の幾何構造が主問題。 | divergence definition と α≠±1 use case を分割。 |
| OQ-B01-016 | QT-SYN-SEM | QT-TRANSFER-INV | constraints semantics と implementation syntax の bridge 欠如が中心。all architectures へ広げる不変性も副軸。 | categorical DL bridge case として保持。 |

## Phase 3 — Integrated Type Distribution

| primary type | count | OQ IDs | 解釈 |
|---|---:|---|---|
| QT-REP-ONTO | 1 | OQ-B01-001 | feature/object/divergence の存在論。次段で忘却論の定義系 anchor が必要。 |
| QT-DECOMP-REC | 0 | - | primary には出なかったが secondary として強い。formal verification と representation alignment に潜む。 |
| QT-FORMAL-VERIF | 1 | OQ-B01-002 | toy-to-frontier の保証問題。忘却論側では「何を捨てても保証が残るか」を問う。 |
| QT-TRANSFER-INV | 1 | OQ-B01-003 | architecture/modalities を跨ぐ保存性。構造保存定理の接続候補。 |
| QT-CLOSURE | 2 | OQ-B01-006, OQ-B01-010 | loop / boundary / identity persistence の問題。LLM と Markov blanket にまたがる。 |
| QT-CONTEXT | 1 | OQ-B01-011 | 長文脈での選択的利用・劣化。Context Rot 系へ接続。 |
| QT-COMP-GEN | 2 | OQ-B01-007, OQ-B01-008 | compression, simplicity, generalization。IB / Kolmogorov / 学習=忘却に接続しやすい。 |
| QT-EMERGENCE | 2 | OQ-B01-009, OQ-B01-013 | depth/scale/threshold。測定論との混線に注意。 |
| QT-MEAS-DEFORM | 2 | OQ-B01-005, OQ-B01-012 | benchmark/probe/metric が対象を歪める問い。忘却論側では観測関手の扱いが必要。 |
| QT-GROUNDING | 0 | - | primary には出ないが OQ-B01-005/006 の secondary。第二バッチで semiotics / multimodal / embodiment から増える見込み。 |
| QT-GEOM-OBSTR | 2 | OQ-B01-014, OQ-B01-015 | 情報不等式・divergence・connection など構造存在条件。形式面の強い候補。 |
| QT-SYN-SEM | 1 | OQ-B01-016 | syntax と semantics の bridge。圏論的DLと CPS の接続候補。 |
| QT-META-AGENDA | 1 | OQ-B01-004 | survey bundle。mapping 前に child OQ 化が必要。 |

## Domain Scope Seed Typing

これは SOURCE 分類ではなく、第二 intake batch の探索優先度を決めるための仮分類。

| scope id | likely primary type | likely secondary type | note |
|---|---|---|---|
| DS-HOTT | QT-DECOMP-REC | QT-GEOM-OBSTR | truncation / proof relevance は「証人をどこまで消せるか」の recoverability と構造存在条件。 |
| DS-TDA-COH | QT-GEOM-OBSTR | QT-DECOMP-REC | cohomological obstruction / nerve は障害類の問い。 |
| DS-ENRICHED | QT-REP-ONTO | QT-GEOM-OBSTR | 連続値の同定能力・距離・忘却度の object 定義。 |
| DS-HYPERBOLIC | QT-EMERGENCE | QT-GEOM-OBSTR | 位相特異点・超光速運動は閾値的現象と幾何障害の両方。 |
| DS-SPIN-STAT | QT-GEOM-OBSTR | QT-TRANSFER-INV | 複製可能性/不能性の構造条件。 |
| DS-HOLOGRAPHY | QT-COMP-GEN | QT-GEOM-OBSTR, QT-DECOMP-REC | 情報喪失・時空創発・reconstruction が絡む。 |
| DS-PSYCH-ASD-DISS | QT-CLOSURE | QT-MEAS-DEFORM | precision weighting と境界維持、診断測定の歪み。 |
| DS-SLEEP-MEM | QT-COMP-GEN | QT-CLOSURE | 記憶固定・スキーマ形成は圧縮/再構成と自己境界維持。 |
| DS-OPT-SAM | QT-COMP-GEN | QT-MEAS-DEFORM | flatness/sharpness 測定と generalization の関係。 |
| DS-GEOIB | QT-COMP-GEN | QT-GEOM-OBSTR | IB の幾何化。 |
| DS-SEMIOTICS | QT-GROUNDING | QT-MEAS-DEFORM | sign / prompt / difference-based identification。 |
| DS-HYPHE-CHEM | QT-COMP-GEN | QT-EMERGENCE | 溶解・析出・再結晶化は metaphor risk があるため P3 のまま。 |

## Carry Forward

次段で優先する mapping order:

| rank | target | 理由 |
|---|---|---|
| 1 | QT-COMP-GEN | 忘却論の中核「学習=忘却」に最も近く、OQ-B01-007/008/014/015/DS-GEOIB/DS-SLEEP-MEM へ横断しやすい。 |
| 2 | QT-CLOSURE | LLM active inference と Markov blanket が同型的に並ぶ。候補回答の見栄えが強い。 |
| 3 | QT-MEAS-DEFORM | emergence mirage / alignment metrics / reasoning benchmark を束ねられる。忘却論の観測関手で答えやすい。 |
| 4 | QT-GEOM-OBSTR | 情報幾何・Kolmogorov・HoTT/TDA/enriched の形式線へ進める。 |
| 5 | QT-REP-ONTO + QT-DECOMP-REC | MI feature ontology と representation alignment を、忘却論の定義系へ対応づける。 |

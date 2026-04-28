# Open Question Crosswalk — Typing Summary Batches 01-02

- 作成日: 2026-04-26
- 入力:
  - `../intake/intake_2026-04-26_batch01.md`
  - `../intake/intake_2026-04-26_batch02.md`
  - `typing_2026-04-26_batch01.md`
  - `typing_2026-04-26_batch02.md`
- 目的: 32件の open question を横断して、忘却論 anchor 探索の入口を決める。
- 注意: ここでは anchor mapping はまだ行わない。外部論文側の問いの型だけを固定する。

## Integrated Distribution

| primary type | count | OQ IDs | mapping cue |
|---|---:|---|---|
| QT-GEOM-OBSTR | 6 | OQ-B01-014, OQ-B01-015, OQ-B02-004, OQ-B02-007, OQ-B02-008, OQ-B02-009 | 情報幾何・Kolmogorov・HoTT・higher structures。形式 anchor の鉱脈。 |
| QT-COMP-GEN | 4 | OQ-B01-007, OQ-B01-008, OQ-B02-003, OQ-B02-006 | 学習=忘却、IB/GeoIB、SAM、generalization。最優先 mapping lane。 |
| QT-MEAS-DEFORM | 3 | OQ-B01-005, OQ-B01-012, OQ-B02-005 | metric / benchmark / proxy が対象を作る型。emergence mirage も secondary で合流。 |
| QT-CLOSURE | 2 | OQ-B01-006, OQ-B01-010 | action-perception loop と Markov blanket persistence。 |
| QT-EMERGENCE | 2 | OQ-B01-009, OQ-B01-013 | depth/scale/threshold。measurement deformation と切り分け必須。 |
| QT-FACT-AMB | 2 | OQ-B02-001, OQ-B02-012 | holography / fermionic QI の部分系・factorization 問題。 |
| QT-PRECISION-MECH | 2 | OQ-B02-013, OQ-B02-014 | precision weighting の機構・障害別 specificity。 |
| QT-MEM-CONSOL | 2 | OQ-B02-015, OQ-B02-016 | sleep / memory consolidation / down-selection。 |
| QT-SYN-SEM | 2 | OQ-B01-016, OQ-B02-010 | categorical DL と enriched/higher category の bridge。 |
| QT-REP-ONTO | 1 | OQ-B01-001 | feature / representation の単位問題。 |
| QT-DECOMP-REC | 1 | OQ-B02-002 | holographic reconstruction。secondary では MI / HoTT にも広がる。 |
| QT-FORMAL-VERIF | 1 | OQ-B01-002 | toy-to-frontier verification。 |
| QT-TRANSFER-INV | 1 | OQ-B01-003 | architecture / modality transfer。 |
| QT-CONTEXT | 1 | OQ-B01-011 | long-context degradation。 |
| QT-OBS-ACCESS | 1 | OQ-B02-011 | hyperbolic media の観測アクセス問題。 |
| QT-META-AGENDA | 1 | OQ-B01-004 | NLP open agenda bundle。child OQ 分割が先。 |
| QT-GROUNDING | 0 | - | primary なし。secondary として OQ-B01-005/006 に潜る。 |

## Mapping Lanes

| lane | 含める型 | 代表 OQ | anchor 探索の入口 |
|---|---|---|---|
| Lane A: compression geometry | QT-COMP-GEN, QT-MEAS-DEFORM | OQ-B01-007, OQ-B01-008, OQ-B02-003, OQ-B02-004, OQ-B02-005, OQ-B02-006 | 学習=忘却、IB/GeoIB、SAM、観測関手、proxy failure |
| Lane B: boundary and reconstruction | QT-CLOSURE, QT-FACT-AMB, QT-DECOMP-REC | OQ-B01-006, OQ-B01-010, OQ-B02-001, OQ-B02-002, OQ-B02-012 | MB維持、CPS分解、部分系境界、reconstruction residual |
| Lane C: formal coherence | QT-GEOM-OBSTR, QT-SYN-SEM, QT-FORMAL-VERIF | OQ-B01-014, OQ-B01-015, OQ-B01-016, OQ-B02-007, OQ-B02-008, OQ-B02-009, OQ-B02-010 | HoTT witness erasure、cohomological obstruction、α-connection、syntax-semantics bridge |
| Lane D: representation and transfer | QT-REP-ONTO, QT-TRANSFER-INV, QT-CONTEXT | OQ-B01-001, OQ-B01-003, OQ-B01-011, OQ-B01-012 | feature ontology、構造保存、Context Rot、representation alignment |
| Lane E: precision and consolidation | QT-PRECISION-MECH, QT-MEM-CONSOL | OQ-B02-013, OQ-B02-014, OQ-B02-015, OQ-B02-016 | precision anisotropy、忘却バンドル相転移、sleep as selective forgetting |
| Lane F: observational calibration | QT-OBS-ACCESS | OQ-B02-011 | 観測アクセス、解像度限界、外部較正点。早期 contact ではなく最後に検査。 |

## First Anchor-Search Priority

| priority | target | 理由 | next file to create/update |
|---|---|---|---|
| P1 | Lane A: compression geometry | 32件中で最も忘却論中核に近く、SAM / GeoIB / IB / generalization を一束にできる。 | 既存 `../mappings/mapping_QT-COMP-GEN_2026-04-26.md` を B02-003/004/005/006 で増補。必要なら後で lane file へ分割 |
| P2 | Lane B: boundary and reconstruction | LLM active inference, Markov blanket, holography, fermionic factorization が同じ「境界の切り方」へ寄る。 | `../mappings/mapping_lane_B_boundary_reconstruction.md` |
| P3 | Lane C: formal coherence | HoTT / information geometry / category theory は数理的に強いが、local anchor 精読が必要。 | `../mappings/mapping_lane_C_formal_coherence.md` |
| P4 | Lane E: precision and consolidation | 認知科学・精神病理・睡眠に接続しやすい。実験的主張水準を慎重に分ける。 | `../mappings/mapping_lane_E_precision_consolidation.md` |

## Rejection Guard

| risk | guard |
|---|---|
| vocabulary-only | 型名と忘却論語彙が似ているだけでは mapping しない。必ず外部 SOURCE quote と local Oblivion SOURCE を対にする。 |
| over-bundling | `QT-META-AGENDA` と split queue は、そのまま single case にしない。child OQ 化してから mapping する。 |
| premature-contact | contact candidate は `mapped -> gauntlet -> note_ready` を通過したものだけ。typing 段階では接触判断しない。 |
| physics metaphor drift | holography / hyperbolic media は比喩接続に流れやすい。factorization / observational access の技術的問いとして扱う。 |

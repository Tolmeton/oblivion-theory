# Open Question Crosswalk — Typing Batch 02

- 作成日: 2026-04-26
- 入力: `../intake/intake_2026-04-26_batch02.md`
- 型カタログ: `../question_type_catalog.md`
- 目的: expanded scope の open question / limitation / future work を、忘却論 anchor 探索前の問い型へ分類する。
- SOURCE 規律: type 判定は intake の SOURCE 行に基づく。下表の「判定理由」は Codex の分類推論であり、外部論文の主張そのものではない。

## Phase 0 — Candidates

受け取り:

| input | 件数 | status |
|---|---:|---|
| OQ-B02 intake rows | 16 | arXiv PDF / open-access PDF / PMC HTML 直読 SOURCE |
| batch01 type catalog | 13 types | そのまま使える型と、batch02 で増補が必要な型を分離 |

棄却:

| branch | 理由 |
|---|---|
| batch01 type への強制押し込み | precision / sleep / factorization / observational access が潰れるため棄却。 |
| 物理・HoTT・睡眠を「幾何」の一語に畳む | mapping 前の探索 anchor が粗くなりすぎるため棄却。 |
| 忘却論側の概念名で分類する | まだ local anchor を読んでいないため、外部論文側の欠落を優先する。 |

## Phase 1 — Added Type Surface

batch02 で catalog に追加した型:

| type id | 追加理由 |
|---|---|
| QT-FACT-AMB | holography と fermionic QI で、部分系・内部・marginal・entanglement の切り方自体が問題になる。 |
| QT-OBS-ACCESS | hyperbolic media と holographic interior で、対象への operational / experimental access が主問題になる。 |
| QT-PRECISION-MECH | precision weighting の neuromodulatory mechanism と障害別 specificity は、batch01 の measurement deformation だけでは弱い。 |
| QT-MEM-CONSOL | sleep / memory consolidation は compression-generalization に近いが、保持・刈り込み・再結晶化の時間過程を別に保持する。 |

## Phase 2 — OQ Typing Matrix

| OQ ID | primary type | secondary type | 判定理由 | next action |
|---|---|---|---|---|
| OQ-B02-001 | QT-FACT-AMB | QT-DECOMP-REC, QT-CLOSURE | information paradox は puzzle bundle だが、state dependence / firewall / subregion duality は「どの部分系・内部をどう切るか」が中心。 | interior/firewall と subregion duality を child OQ に分割。 |
| OQ-B02-002 | QT-DECOMP-REC | QT-OBS-ACCESS, QT-GEOM-OBSTR | black-hole interior の real-time operational framework と tensor networks beyond RT は、境界側から何を再構成できるかの問い。 | holographic reconstruction case として保持。 |
| OQ-B02-003 | QT-COMP-GEN | QT-MEAS-DEFORM | SAM の optimizer-generalization 関係、二階項、m-sharpness は generalization をどの局所量で測るかの問題。 | SAM generalization proxy case へ送る。 |
| OQ-B02-004 | QT-GEOM-OBSTR | QT-COMP-GEN, QT-MEAS-DEFORM | Euclidean neighborhood を Fisher geometry で置き換えるが、natural gradient / distributed m-sharpness / proximal relation の構造が未定。 | Fisher geometry anchor 探索へ送る。 |
| OQ-B02-005 | QT-MEAS-DEFORM | QT-COMP-GEN | SAM single-step ascent の近似が不正確・不安定で multi-step で劣化する。proxy が対象を歪める型。 | local proxy failure として B02-003/004 と束ねる。 |
| OQ-B02-006 | QT-COMP-GEN | QT-GEOM-OBSTR, QT-TRANSFER-INV | GeoIB の temporal/causal/multimodal 拡張と high intrinsic dimension / non-manifold limitation は、圧縮幾何の拡張可能性。 | GeoIB direct-relevance case として高優先。 |
| OQ-B02-007 | QT-GEOM-OBSTR | QT-FORMAL-VERIF, QT-DECOMP-REC | Cubical Agda 上の computational cohomology benchmark と classical approaches との接続は、構造存在と形式計算の障害。 | witness / computation obstruction case へ送る。 |
| OQ-B02-008 | QT-GEOM-OBSTR | QT-SYN-SEM | strict equality / two-level type theory は semi-simplicial types と internal `(∞,1)` categories の構成障害に向く。 | witness erasure / coherence case として保持。 |
| OQ-B02-009 | QT-GEOM-OBSTR | QT-TRANSFER-INV | higher structures の invariance under weak equivalence / Quillen equivalence は、構造がモデル間で保存される条件の問い。 | HoTT invariance case へ送る。 |
| OQ-B02-010 | QT-SYN-SEM | QT-GEOM-OBSTR | higher Gray tensor product analogues は enriched / higher category の syntax-semantics bridge と構造存在条件。 | enriched category bridge case として保持。 |
| OQ-B02-011 | QT-OBS-ACCESS | QT-GEOM-OBSTR | phase singularity ensemble の full phase-space correlations が未探索・実験的に inaccessible。測定解像度そのものが欠落。 | external calibration case。anchor mapping は慎重に行う。 |
| OQ-B02-012 | QT-FACT-AMB | QT-GEOM-OBSTR | fermionic Fock space で unrestricted に部分系を切ると entanglement definition が ambiguous になる。 | superselection / factorization ambiguity case へ送る。 |
| OQ-B02-013 | QT-PRECISION-MECH | QT-CLOSURE | precision の neuromodulatory mechanism、脳内実装、psychosis precision changes が open question。 | precision anisotropy / MB維持 anchor を探索。 |
| OQ-B02-014 | QT-PRECISION-MECH | QT-MEAS-DEFORM | predictive coding theories が just-so stories を越え、ASD 固有の predictive power を示す必要がある。機構と測定の両方。 | ASD precision specificity case として保持。 |
| OQ-B02-015 | QT-MEM-CONSOL | QT-COMP-GEN, QT-MEAS-DEFORM | SHY が睡眠効果を完全には説明できず、downscaling の role / mechanism / function が未確定。 | sleep consolidation conflict case へ送る。 |
| OQ-B02-016 | QT-MEM-CONSOL | QT-DECOMP-REC | sleep 後に memory-supporting synapse の絶対強度がどう変わるか unknown。何が残り何が刈られるかの問い。 | down-selection / recoverability case として保持。 |

## Phase 3 — Type Distribution

| primary type | count | OQ IDs | 解釈 |
|---|---:|---|---|
| QT-FACT-AMB | 2 | OQ-B02-001, OQ-B02-012 | 部分系・内部・entanglement の切り方が不安定。物理側の強い横断候補。 |
| QT-DECOMP-REC | 1 | OQ-B02-002 | holographic reconstruction。batch01 の MI recoverability と遠く接続可能。 |
| QT-COMP-GEN | 2 | OQ-B02-003, OQ-B02-006 | SAM / GeoIB。忘却論の「学習=忘却」に最も近い batch02 線。 |
| QT-GEOM-OBSTR | 4 | OQ-B02-004, OQ-B02-007, OQ-B02-008, OQ-B02-009 | Fisher geometry, HoTT, higher structures。形式面の anchor 候補。 |
| QT-MEAS-DEFORM | 1 | OQ-B02-005 | SAM 近似の proxy failure。batch01 の emergence mirage と束ねられる。 |
| QT-SYN-SEM | 1 | OQ-B02-010 | enriched / higher category の構成 bridge。 |
| QT-OBS-ACCESS | 1 | OQ-B02-011 | hyperbolic media の外部較正点。比喩化せず、観測アクセス問題として保持。 |
| QT-PRECISION-MECH | 2 | OQ-B02-013, OQ-B02-014 | precision の mechanism と disorder specificity。認知・精神病理線。 |
| QT-MEM-CONSOL | 2 | OQ-B02-015, OQ-B02-016 | 睡眠・記憶固定・down-selection。選択的忘却線。 |

## Phase 4 — Split Queue

| parent OQ | split reason | child candidates |
|---|---|---|
| OQ-B02-001 | information paradox の puzzle bundle が広い。 | `B02-001a interior/firewall`, `B02-001b subregion duality Hamiltonian` |
| OQ-B02-006 | extension と limitation が別問題。 | `B02-006a temporal/causal/multimodal GeoIB`, `B02-006b high-dimensional/non-manifold failure` |
| OQ-B02-007 | computational benchmark と classical/synthetic bridge が別問題。 | `B02-007a Cubical Agda computation`, `B02-007b synthetic-classical cohomology bridge` |
| OQ-B02-015 | SHY insufficiency と downscaling mechanism が別問題。 | `B02-015a SHY explanatory gap`, `B02-015b downscaling role/mechanism/function` |

## Carry Forward

次段の anchor 探索 priority:

| rank | target | 理由 |
|---|---|---|
| 1 | QT-COMP-GEN + QT-MEAS-DEFORM | SAM / Fisher SAM / GeoIB は「圧縮幾何」と「proxy failure」を同時に持つ。忘却論側の optimization / IB anchor を探しやすい。 |
| 2 | QT-GEOM-OBSTR | HoTT / cohomology / enriched / Fisher geometry は形式線。witness erasure, coherence, curvature の anchor 候補。 |
| 3 | QT-FACT-AMB + QT-DECOMP-REC | holography と fermionic QI を、boundary / reconstruction / factorization ambiguity として束ねられる。 |
| 4 | QT-PRECISION-MECH | precision weighting と psychopathology は、忘却バンドル相転移・異方的精度の候補回答へ接続しやすい。 |
| 5 | QT-MEM-CONSOL | sleep / memory consolidation は「何を忘れることで保持するか」を直接問う。 |
| 6 | QT-OBS-ACCESS | hyperbolic media は外部較正点として有望だが、語彙接続だけになりやすいので anchor mapping は最後に回す。 |

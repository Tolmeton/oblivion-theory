# OQ-B01-008 Information Plane — CKA-KL Decomposition

## 0. Status

- status: gauntlet_passed
- created: 2026-04-26
- updated: 2026-04-26
- source_status: external PDF text SOURCE + local Oblivion SOURCE
- owner: Tolmetes / Codex

## 1. External Paper

- citation: Schwartz-Ziv, R. & Tishby, N. (2017). Opening the Black Box of Deep Neural Networks via Information. arXiv:1703.00810.
- URL / DOI: https://arxiv.org/abs/1703.00810
- local text: `/tmp/oqc_papers_20260426/1703.00810.txt`
- exact open question quote excerpt: "it remains unclear why different hidden layers converge to different points in the information plane"
- quote SOURCE: `/tmp/oqc_papers_20260426/1703.00810.txt:527-534`

## 2. Question Typing

- type: `QT-COMP-GEN` primary; `QT-GEOM-OBSTR` secondary
- why this is unresolved: IB paper gives a compression / diffusion story, but the layer-specific endpoints on the information plane remain underexplained. The gap is not merely "does compression happen?" but "why do different layers settle at different geometric positions?"
- what would count as a candidate answer: a mechanism that separates the scalar information-plane coordinates from hidden representation geometry, and predicts when two layers can look similar under one measurement while differing under another.

## 3. One-to-One Crosswalk

| external unresolved point | Oblivion anchor | claim level | local SOURCE | candidate bridge |
|---|---|---|---|---|
| Hidden layers converge to different information-plane points. | `I-T6.8.1` CKA-KL 分離 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:897-905` | The information-plane point is not one primitive object. It can be decomposed into shape-sensitive and scale-sensitive components of the forgetting field. |
| Gradient noise / maximum-entropy explanation remains incomplete. | `I-P6.8.2/3` CKA-KL direction preservation / proportionality | proposition | `drafts/series/論文I_力としての忘却_草稿.md:907-923` | The relevant question becomes whether the observed compression direction preserves the KL-forgetting direction, not whether one scalar compression story explains all layers. |
| Compression phase is tied to a phase-transition-like process. | `I-T5.1` 方向性定理 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:203-235` | The phase transition should be read through the nonalignment condition of forgetting direction, not only through entropy maximization. |

## 4. Candidate Answer

1. one-sentence answer: Different hidden layers converge to different information-plane points because the information plane collapses multiple components of the forgetting field; CKA/KL decomposition separates the shape component from the full scale-plus-shape forgetting geometry.
2. mechanism: IB observes a low-dimensional projection of representation dynamics. Paper I says CKA measures mainly shape while KL measures shape plus scale; therefore a layer's apparent compression endpoint can differ because its forgetting field has a different decomposition, not because each layer simply finds a different scalar maximum-entropy state.
3. what this predicts beyond the external paper: When the scale component is suppressed, CKA and KL trajectories should align more strongly. When scale changes dominate, information-plane convergence can look compressed while CKA-based representation geometry fails to show the same endpoint. α-SAM / OA-SAM should move endpoints by changing update direction without requiring accuracy improvement.

## 5. Risk Gate

| risk | status | note |
|---|---|---|
| vocabulary-only | passed | The bridge is not "information = forgetting"; it uses a specific theorem, `I-T6.8.1`, to split measured components. |
| source-thin | passed_for_draft | External quote and local theorem lines are both identified. Full case should still cite the PDF page in final note. |
| too-internal | open | Need a reader-facing explanation of CKA and KL without importing all of Paper I. |
| overfit-to-paper | open | Needs a second IB / GeoIB paper check before note_ready. |
| premature-contact | blocked | Not contact-ready until a short note or small replication plan exists. |

## 6. Promotion

- SOURCE promotion: promote external quote and `I-T6.8.1` to case SOURCE.
- Gauntlet seed: passed preliminary Gauntlet on 2026-04-26; strongest remaining issue is empirical demonstration.
- related work patch: usable in Paper I / Paper IX discussion of IB and representation measurement.
- short note: strong candidate, title seed: `Information-plane endpoints as forgetting-field projections`.
- contact candidate: hold until short note includes at least one plotted CKA/KL toy example or published support.

## 7. Rejection Ledger

- rejected branch: "This solves the Information Bottleneck account of deep learning."
- reason: The case only gives a measurement decomposition and candidate mechanism for layer-specific endpoints. It does not validate every IB claim.
- rejected branch: "Hidden layer compression is just entropy maximization."
- reason: The Oblivion anchor requires direction and decomposition, not only scalar entropy increase.

## 8. Refutation Gauntlet

### Round 1 — measurement-only objection

- refutation r: CKA-KL decomposition may only explain a measurement mismatch. It may not explain why hidden layers dynamically converge to different information-plane endpoints.
- SFBT question: Is this impossible, or is the missing premise merely unstated?
- premise strengthening: split the case into two layers. The core case is a diagnostic answer to the endpoint question: the information-plane endpoint is a projection of a richer representation geometry. The dynamic claim is conditional: if endpoint differences are driven by forgetting-field components, then CKA/KL decomposition should predict layerwise endpoint divergence.
- realization operation: boundary condition added. The case no longer depends on proving the whole IB compression phase; it must show that layer endpoints differ along shape / scale / direction components.
- result: scope preserved. The candidate still answers the stated external gap, but as a decompositional mechanism rather than a complete training-dynamics proof.
- verdict: pass.

### Round 2 — MI-vs-representation mismatch objection

- refutation r: The external paper asks about mutual-information coordinates, not CKA/KL representation geometry. The crosswalk may be changing the object.
- SFBT question: Can the same question be reached from another angle without replacing the object?
- premise strengthening: define the bridge observable: compare layer orderings under information-plane coordinates, CKA shape distance, and KL scale-plus-shape distance. If the information-plane endpoints are genuine projections of forgetting-field geometry, at least one systematic correspondence or divergence pattern should appear.
- realization operation: prediction added. The case now has a measurable crosswalk rather than a vocabulary mapping.
- result: scope preserved. The case remains about information-plane endpoints, while adding a representation-geometry diagnostic that can fail.
- verdict: pass.

### Round 3 — overextension absorption

- refutation r: Mentioning α-SAM / OA-SAM may overextend the case from explanation to intervention.
- SFBT question: Can the objection be absorbed as a structural separation?
- absorption strategy: separate `core answer` from `extra prediction`. Core answer = CKA-KL decomposition of endpoint geometry. Extra prediction = α-SAM / OA-SAM should move endpoints by altering update direction. Failure of the intervention does not immediately kill the decomposition case; failure of the decomposition does.
- realization operation: falsification hierarchy added.
- result: scope preserved with testable layers. No retreat to a weaker claim; the case gains a sharper failure condition.
- verdict: pass.

### Falsification Conditions

| condition | effect |
|---|---|
| CKA/KL decomposition shows no systematic relation to information-plane endpoints across layers | kills core case |
| CKA and KL trajectories are identical where the case predicts scale/shape divergence | strongly weakens core case |
| α-SAM / OA-SAM fails to move endpoints while CKA/KL decomposition still holds | kills intervention extension only |
| A second IB / GeoIB source gives a better explanation with no representation-geometry residue | demote from short-note candidate to related-work patch |

### Gauntlet Result

- result: gauntlet_passed
- survived claim: information-plane endpoints can be treated as projections of a decomposed forgetting field, with CKA/KL giving a falsifiable measurement split.
- remaining debt: one toy or published example comparing information-plane coordinates against CKA/KL layer trajectories.

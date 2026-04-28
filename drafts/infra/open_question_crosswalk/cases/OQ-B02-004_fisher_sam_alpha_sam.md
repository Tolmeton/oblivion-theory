# OQ-B02-004 Fisher SAM — α-SAM Extension

## 0. Status

- status: oblivion_sam_case
- created: 2026-04-26
- updated: 2026-04-29
- source_status: external PDF text SOURCE + local Oblivion SOURCE
- owner: Tolmetes / Codex

## 1. External Paper

- citation: Kim, M., Li, D., Hospedales, T. & Simo-Serra, E. (2022). Fisher SAM: Information Geometry and Sharpness Aware Minimisation. arXiv:2206.04920.
- URL / DOI: https://arxiv.org/abs/2206.04920
- local text: `/tmp/oqc_papers_20260426_batch02/2206.04920.txt`
- exact future-work quote excerpts:
  - "we leave it and related further extensive study as future work"
  - "Several research questions remain: natural gradient updates combined with the Fisher SAM loss"
- quote SOURCE: `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:268-276`, `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:548-556`

## 2. Question Typing

- type: `QT-GEOM-OBSTR` primary; `QT-COMP-GEN` and `QT-MEAS-DEFORM` secondary
- why this is unresolved: Fisher SAM replaces Euclidean neighborhoods with Fisher geometry, but leaves open how to combine Fisher SAM with natural-gradient updates, distributed m-sharpness, and proximal-gradient interpretations.
- what would count as a candidate answer: a principled extension that keeps Fisher metric as the intrinsic neighborhood geometry while moving the update direction through an α-connection or forgetting-field term.

## 3. One-to-One Crosswalk

| external unresolved point | Oblivion anchor | claim level | local SOURCE | candidate bridge |
|---|---|---|---|---|
| Natural-gradient updates combined with Fisher SAM loss are left open. | `I-P6.7.1` α-接続近傍 and `I-P6.7.2` 表現制御定理 | definition / proposition | `drafts/series/論文I_力としての忘却_草稿.md:789-821` | Keep the Fisher metric fixed, but let α enter through the connection / update direction. |
| Fisher SAM is an intrinsic-neighborhood correction to SAM. | `I-P6.6.1` 曲率の α_I-線形性 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:760-766` | α intervention changes the forgetting curvature linearly, giving a controlled way to vary the update direction. |
| Distributed m-sharpness and proximal-gradient relations remain open. | `I-P6.8.1` α-Oblivion SAM 包含 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:864-893` | Fisher SAM becomes an α=0 / λ=0 section of a larger family where forgetting-field regularization can be tested as an additional axis. |

## 4. Candidate Answer

1. one-sentence answer: Fisher SAM's future-work gap can be reframed as a missing connection-level control problem: the metric should remain Fisher, while the update direction is varied by α and optionally by a forgetting-field regularizer.
2. mechanism: Paper I separates the intrinsic metric from the α-connection. Fisher SAM corresponds to the α=0 Levi-Civita section; α-SAM changes the path of the perturbation without inventing a new metric; α-Oblivion SAM adds a forgetting-field gradient term that can test whether sharpness and forgetting direction are separable.
3. what this predicts beyond the external paper: Natural-gradient Fisher SAM and α-SAM should diverge most on parameter regions with anisotropic forgetting curvature. If α only changes update direction, representation geometry should shift along `d(ΦT)` while the Fisher neighborhood radius remains comparable. If λ affects forgetting attractors, accuracy and sharpness can remain similar while CKA/KL forgetting profiles diverge.

## 5. Risk Gate

| risk | status | note |
|---|---|---|
| vocabulary-only | passed | The bridge is anchored in specific propositions about α-linearity, α-neighborhoods, and α-SAM inclusion. |
| source-thin | passed_for_draft | External future-work excerpts and local proposition lines are both identified. |
| too-internal | improved | E0a recovery smoke and protocol now separate implementation coherence from empirical training recovery. |
| overfit-to-paper | medium | Fisher SAM is one paper; the case should check later SAM variants before note_ready. |
| premature-contact | blocked_for_direct_contact | E0/E1/E2 toy probes exist, but full Amari α-connection, stronger λ effect, and torch/CIFAR external-validity upgrade remain open. |

## 6. Promotion

- SOURCE promotion: promote `I-P6.6.1`, `I-P6.7.1/2`, `I-P6.8.1` as internal anchors for SAM-family mapping.
- Gauntlet seed: passed preliminary Gauntlet on 2026-04-26; E0a definition smoke, E0b trainable recovery, E1 direction probe, and E2 lambda probe passed.
- related work patch: usable in Paper I §6.7-§6.8 discussion and in an optimization-focused note.
- short note: strong candidate, title seed: `Fisher SAM as the α=0 section of α-SAM`.
- contact candidate: hold until implementation sketch exists.

## 7. Rejection Ledger

- rejected branch: "Fisher SAM open questions are solved by α-SAM."
- reason: α-SAM gives a candidate family and testable route. Distributed m-sharpness and proximal-gradient relations are not yet derived.
- rejected branch: "A new α-dependent metric is needed."
- reason: Paper I deliberately keeps Fisher as the unique metric and puts α into the connection / update direction.

## 8. Refutation Gauntlet

### Round 1 — reparameterization objection

- refutation r: α-SAM may be only a reparameterization of Fisher SAM or natural-gradient SAM, not a substantive candidate answer.
- SFBT question: Is this impossible, or is the missing discriminant merely unstated?
- premise strengthening: make the discriminant explicit. The metric radius is held fixed by Fisher geometry, while α changes the connection / update direction. The case survives only if changing α changes representation trajectory or forgetting curvature under comparable Fisher-neighborhood radius.
- realization operation: nontriviality test added.
- result: scope preserved. The claim is not "α-SAM is automatically new"; it is "Fisher SAM's open natural-gradient direction can be tested as connection-level control."
- verdict: pass.

### Round 2 — partial-answer objection

- refutation r: Fisher SAM lists multiple open questions: natural-gradient updates, distributed m-sharpness, and proximal-gradient relations. α-SAM directly addresses only the first.
- SFBT question: Can a different premise absorb the rest without pretending to solve them?
- premise strengthening: split the future-work list by answer type. Natural-gradient update is the direct bridge. Distributed m-sharpness becomes a multi-site averaging question over α / λ profiles. Proximal-gradient relation becomes a regularization-form question for the forgetting-field term.
- realization operation: answer taxonomy added.
- result: scope preserved with internal subdivision. The case remains a strong answer to the natural-gradient part and a research route for the other two.
- verdict: pass.

### Round 3 — implementation-gap objection

- refutation r: The α-connection story may be elegant but unusable if it cannot recover Fisher SAM in practice or if the α perturbation is numerically unstable.
- SFBT question: Can the objection become a gate rather than a reason to retreat?
- absorption strategy: add an implementation recovery gate. First, α=0 and λ=0 must recover Fisher SAM behavior. Second, varying α at λ=0 must change representation trajectory without changing the Fisher metric definition. Third, λ must be introduced only after the α recovery gate passes.
- realization operation: staged experiment gate added.
- result: scope preserved. The objection becomes a falsification protocol.
- verdict: pass.

### Falsification Conditions

| condition | effect |
|---|---|
| α=0 / λ=0 does not recover Fisher SAM behavior | kills mapping |
| varying α changes only notation and not update / representation trajectory | kills α-SAM nontriviality |
| Fisher radius cannot be held comparable while α varies | weakens connection-level interpretation |
| distributed m-sharpness and proximal-gradient terms cannot be expressed as α / λ profile questions | limits case to natural-gradient subquestion |

### Experiment Sketch

| stage | setup | expected signal |
|---|---|---|
| E0a definition smoke | run NumPy-only Fisher-ball perturbation and α-SAM wrapper with α=0, λ=0 | passed: perturbation and surrogate-loss differences are numerical zero |
| E0b training recovery | run Fisher SAM baseline and α-SAM with α=0, λ=0 in a trainable model | passed: training trajectories match to numerical tolerance |
| E1 direction | vary α with Fisher radius fixed | passed: nonzero α changes hidden representation trajectory while Fisher radius remains comparable |
| E2 forgetting term | add λ after E0/E1 | passed: λ changes profile weakly but nonzero while accuracy remains comparable |
| E3 distributed | average α / λ profiles across workers | m-sharpness becomes a profile-aggregation question |

### Gauntlet Result

- result: oblivion_sam_case
- survived claim: Fisher SAM's future-work gap can be framed as connection-level control over update direction while preserving Fisher metric geometry.
- remaining debt: stronger λ effect, full Amari α-connection implementation, torch/CIFAR external-validity upgrade, and E3 distributed profile. The case is α-Oblivion-SAM-shaped, not direct-contact ready.

## 9. Implementation Gate

| gate | artifact | result | interpretation |
|---|---|---|---|
| E0a definition smoke | `experiments/fisher_alpha_sam_recovery_smoke.py` and `experiments/results/fisher_alpha_sam_recovery_smoke.json` | pass | α=0, λ=0 recovers the Fisher-ball perturbation within numerical tolerance on the 2D Gaussian toy manifold. |
| E0b training recovery | `experiments/fisher_alpha_sam_training_recovery.py` and `experiments/results/fisher_alpha_sam_training_recovery.json` | pass | Fisher SAM and α-SAM(α=0, λ=0) produce matching trajectories on a NumPy trainable logistic model. |
| E1 direction probe | `experiments/fisher_alpha_sam_direction_probe.py` and `experiments/results/fisher_alpha_sam_direction_probe.json` | pass | Nonzero α changes NumPy MLP hidden representations while perturbations are projected back to the same Fisher radius. |
| E2 lambda probe | `experiments/fisher_alpha_sam_lambda_probe.py` and `experiments/results/fisher_alpha_sam_lambda_probe.json` | pass | λ changes CKA/KL forgetting profile weakly but nonzero while preserving comparable accuracy and Fisher radius. |

E1 is a toy connection-side direction probe, not a full Amari α-connection implementation. The signal is not uniformly large across all seed/α pairs: mean final `1-CKA` is high, but the weakest final CKA shift is small while diagonal-Gaussian KL remains nonzero. Therefore the surviving claim is direction controllability in the implementation surface, not a universal performance or large-shift claim.

E2 strengthens the theory case by adding the λ axis. The observed effect is deliberately recorded as weak: max accuracy delta is 0.0052, mean final absolute CKA-profile delta is 0.00095, and mean final absolute diagonal-Gaussian KL delta is 1.0163. The surviving claim is not "λ strongly improves optimization"; it is "a λ-weighted forgetting term can perturb the representation profile without reducing the task to an accuracy change."

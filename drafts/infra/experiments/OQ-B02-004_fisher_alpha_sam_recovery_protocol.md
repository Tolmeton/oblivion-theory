# OQ-B02-004 Fisher SAM / alpha-SAM Recovery Protocol

## 0. Position

- case: `OQ-B02-004`
- status: `oblivion_sam_case`
- created: 2026-04-26
- purpose: turn the Gauntlet-passed Fisher SAM / alpha-SAM bridge into an implementation-gated case.

## 1. SOURCE Anchors

| source | role |
|---|---|
| `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:268-276` | Fisher SAM explicitly leaves natural-gradient update with Fisher SAM loss as future work. |
| `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:548-556` | Fisher SAM conclusion lists natural-gradient, distributed m-sharpness, and proximal-gradient relation as remaining questions. |
| `/home/makaron8426/Sync/oikos/oblivion-theory/drafts/series/論文I_力としての忘却_草稿.md:775-821` | alpha-SAM is defined as Fisher-metric neighborhood plus alpha-connection update direction. |
| `/home/makaron8426/Sync/oikos/oblivion-theory/drafts/series/論文I_力としての忘却_草稿.md:864-893` | alpha-Oblivion SAM includes Fisher SAM at alpha=0, lambda=0. |
| `/home/makaron8426/Sync/oikos/oblivion-theory/drafts/series/論文I_力としての忘却_草稿.md:961-1028` | E12 gives CKA-based forgetting profile measurement and lambda-sign control as prior internal experiment. |

## 2. Claim Under Test

Fisher SAM's future-work gap can be treated as a connection-control problem:

1. the metric radius remains Fisher;
2. alpha does not introduce a new metric;
3. alpha changes the update direction through the connection side;
4. lambda is introduced only after the alpha=0 recovery gate passes.

This protocol does not claim that alpha-SAM is empirically better. It tests whether the bridge is implementation-coherent enough to remain a contactable case.

## 3. Gate Structure

| gate | question | pass condition | fail effect |
|---|---|---|---|
| E0a definition smoke | Does alpha=0, lambda=0 reduce to the Fisher SAM perturbation in the same implementation surface? | perturbation and surrogate loss match to numerical tolerance on a 2D Fisher toy manifold | demote case; mapping is only prose |
| E0b training recovery | Does alpha=0, lambda=0 recover Fisher SAM behavior in a trainable model? | loss/accuracy/robustness are comparable to a Fisher SAM baseline under same rho and seed budget | demote case; no contact |
| E1 direction | With Fisher radius fixed, does alpha variation change representation trajectory? | CKA/KL profile changes while Fisher-radius accounting remains comparable | keep as alpha-control case |
| E2 lambda term | After E0/E1, does lambda alter forgetting profile without merely changing accuracy? | similar accuracy with different CKA/KL forgetting attractor | promote to alpha-Oblivion SAM case |
| E3 distributed profile | Can distributed m-sharpness be expressed as alpha/lambda profile aggregation? | profile aggregation reproduces or explains m-sharpness behavior | extend beyond natural-gradient subquestion |

## 4. Immediate Execution Plan

### P0: No-install smoke

Use a NumPy-only 2D Gaussian parameter manifold to test E0a.

- parameter: theta = (mu, log_sigma)
- Fisher metric: diag(exp(-2 log_sigma), 2)
- loss: Fisher SAM paper's 2D mixture-style KL energy, simplified into a deterministic toy objective
- Fisher perturbation: first-order Fisher-ball maximizer
- alpha-SAM wrapper: must be exactly Fisher perturbation at alpha=0, lambda=0

Output:

- JSON result in `experiments/results/fisher_alpha_sam_recovery_smoke.json`
- pass/fail flag for E0a
- max perturbation difference
- max surrogate-loss difference

### P1: Training recovery

Run only after E0a passes. A NumPy trainable recovery is sufficient for the specialization gate; a torch/CIFAR runner is a later external-validity upgrade.

- model: binary logistic regression first; small MLP/CNN later if torch exists
- data: deterministic synthetic two-class dataset first, then CIFAR-10 if torch/data stack is available
- conditions: Fisher SAM baseline vs alpha-SAM(alpha=0, lambda=0)
- fixed: rho, seed, batch order, Fisher approximation
- output: training curves, robustness proxy, CKA profile if hidden states are available

### P2: alpha direction probe

Run only after P1 passes.

- vary alpha in a small grid, e.g. `[-0.5, 0.0, 0.5]`
- keep Fisher radius comparable
- measure CKA/KL trajectory deltas
- do not discuss performance unless representation trajectory moves.

## 5. Promotion Rule

| outcome | status update |
|---|---|
| E0a fails | `gauntlet_passed` -> `demoted_definition_failure` |
| E0a passes, E0b not run | `gauntlet_passed` -> `experiment_scaffolded` |
| E0b passes | `experiment_scaffolded` -> `recovery_passed` |
| E1 passes | `recovery_passed` -> `direction_control_case` |
| E2 passes | `direction_control_case` -> `oblivion_sam_case` |

## 6. Current Result

| date | gate | artifact | result |
|---|---|---|---|
| 2026-04-26 | E0a definition smoke | `/home/makaron8426/Sync/oikos/oblivion-theory/experiments/fisher_alpha_sam_recovery_smoke.py` | pass |
| 2026-04-27 | E0b training recovery | `/home/makaron8426/Sync/oikos/oblivion-theory/experiments/fisher_alpha_sam_training_recovery.py` | pass |
| 2026-04-29 | E1 direction probe | `/home/makaron8426/Sync/oikos/oblivion-theory/experiments/fisher_alpha_sam_direction_probe.py` | pass |
| 2026-04-29 | E2 lambda probe | `/home/makaron8426/Sync/oikos/oblivion-theory/experiments/fisher_alpha_sam_lambda_probe.py` | pass |

Observed summary:

```json
{
  "status": "pass",
  "max_eps_diff": 7.152448122690996e-18,
  "max_surrogate_loss_diff": 4.440892098500626e-16,
  "max_fisher_radius_error": 6.938893903907228e-18,
  "n_points": 63
}
```

E0b observed summary:

```json
{
  "status": "pass",
  "max_theta_diff": 2.220446049250313e-16,
  "max_loss_diff": 8.326672684688674e-17,
  "max_accuracy_diff": 0.0,
  "max_eps_diff": 1.6653345369377348e-16,
  "max_fisher_radius_diff": 2.0816681711721685e-17,
  "max_surrogate_loss_diff": 2.220446049250313e-16
}
```

Interpretation: E0a/E0b verify recovery of the α=0, λ=0 section. They do not validate nonzero α direction control or the full alpha-connection. E1 remains mandatory before any contact-ready claim.

E1 observed summary:

```json
{
  "status": "pass",
  "max_fisher_radius_error": 1.3877787807814457e-17,
  "mean_final_phi_cka": 0.6901881722221624,
  "min_final_phi_cka": 5.411484728101712e-07,
  "mean_final_diag_gaussian_kl": 14809.295433546087,
  "min_final_diag_gaussian_kl": 0.010434801926313245,
  "max_theta_delta": 2.254033086426843
}
```

Interpretation: E1 verifies direction control inside the NumPy MLP probe: Fisher radius remains fixed and nonzero α changes hidden representations. The weakest final CKA shift is small, so the result should not be described as uniform large movement. The case is still blocked from direct contact until a full α-connection or torch/CIFAR external-validity runner exists.

E2 observed summary:

```json
{
  "status": "pass",
  "max_fisher_radius_error": 1.3877787807814457e-17,
  "max_accuracy_delta": 0.00520833333333337,
  "mean_final_abs_phi_delta": 0.0009506837817393587,
  "min_final_abs_phi_delta": 4.491015512964047e-05,
  "mean_final_abs_kl_delta": 1.016303650638522,
  "min_final_abs_kl_delta": 0.0116957392706869,
  "max_theta_delta": 0.01576653248631094
}
```

Interpretation: E2 adds the λ axis and preserves comparable accuracy. The profile effect is weak in CKA and clearer in diagonal-Gaussian KL, so the correct claim is a minimal nonzero profile-control signal, not a strong optimization improvement.

## 7. Rejection Ledger

- reject: "alpha-SAM solves Fisher SAM's future work."
- reason: the current bridge only survives as a staged implementation question.
- reject: "local NumPy smoke is empirical confirmation."
- reason: E0a only checks implementation coherence of the specialization; E0b/E1 are required for empirical contact.
- reject: "performance improvement is the first target."
- reason: Paper I's own hierarchy makes representation control primary and performance secondary.

# AgentSwing case pseudo scoring audit - 2026-04-26

## §1 Scope

This audit surface documents the manual scoring used in `agentswing_case_pseudo_trajectories.json`.

SOURCE:

- AgentSwing arXiv record: `https://arxiv.org/abs/2603.27490`
- AgentSwing arXiv source: `https://arxiv.org/e-print/2603.27490`
- Source file inside e-print: `table/03_app_cast.tex`

Status:

- Turn text is SOURCE from AgentSwing Appendix C table summaries.
- `carrier_front`, `null_front`, `support_scores`, and `margin_scores` are INFERENCE.
- This is not raw AgentSwing trajectory logging.

## §2 Rubric

Carrier front:

- Advances when a branch recovers or verifies target-relevant useful units.
- In the Mando case, target-relevant units include `$tupid Young`, `Mando`, `Mozzy`, and the father-prison clue.
- In the live-crickets case, target-relevant units include `The Victorian Sideshow`, supporting source-family clues, alternative extraction, and `live crickets`.

Null front:

- Advances when a branch expands misleading focus, low-distinguishability noise, or dead-end loop context.
- In the Mando case, null units include generic October-born rapper search, Lil Durk wrong-focus, Hit-Boy as misleading main path, and underfocused date-anchor search.
- In the live-crickets case, null units include failed direct PDF extraction, Scribd inaccessibility, repeated snippet search, and the old loop context.

Guard:

- Fronts are monotone because the estimator tracks cumulative support/margin state within each branch.
- Null-advancing turns receive at least minimal carrier observation to avoid pseudo no-progress turns becoming division artifacts.

## §3 Front Assignment

| pair | strategy | selected | outcome | carrier_front | null_front | V_carrier | V_null | chi | rubric_notes |
|:---|:---:|:---:|:---|:---|:---|---:|---:|---:|:---|
| `mando_DA_lookahead` | DA | false | failure_within_lookahead | `0/1/2` | `10/12/13` | 1 | 1.5 | 1.5 | DA loses the recent `$tupid Young` clue; useful carrier advances only generically while wrong-focus space expands. |
| `mando_KLN_lookahead` | KLN | true | success_within_lookahead_direction | `1/4/7` | `10/10/11` | 3 | 0.5 | 0.167 | KLN preserves the decisive recent clue and rapidly advances target-relevant carrier units. |
| `mando_Summary_lookahead` | Summary | false | failure_within_lookahead | `0/1/2` | `11/12/12` | 1 | 0.5 | 0.5 | Summary keeps structure but initially preserves the wrong Lil Durk/Hit-Boy basin; it starts correcting too late. |
| `live_crickets_DA_lookahead` | DA | true | success_within_lookahead_direction | `1/3/4` | `6/8/10` | 1.5 | 2 | 1.33 | DA cuts the harmful recent loop while rebuilding useful source-family carrier; this is controlled high-drift. |
| `live_crickets_KLN_lookahead` | KLN | false | failure_within_lookahead | `0/1/2` | `7/9/11` | 1 | 2 | 2 | KLN preserves the recent failed extraction loop; null/noise advances faster than useful carrier. |
| `live_crickets_Summary_lookahead` | Summary | false | failure_within_lookahead | `1/2/3` | `6/7/8` | 1 | 1 | 1 | Summary preserves correct abstraction but does not break the extraction bottleneck; carrier and null advance together. |

## §4 Attack Surface

The strongest objection is not the arithmetic. The arithmetic follows the estimator. The objection is the manual front assignment.

Therefore, the next hardening step is to replace this file with either:

1. a two-pass blind annotation by a second scorer, or
2. judge-based support/margin generation from the same turn text.

Until then, this artifact should be cited as pseudo-measurement, not as AgentSwing raw-log measurement.

## §5 Robustness Follow-up

The first robustness run is stored at `agentswing_case_pseudo_robustness_results.json`.

Setup:

- 5000 trials.
- Random seed: `20260426`.
- Each `carrier_front` and `null_front` turn receives an independent `-1/0/+1` perturbation.
- Perturbed fronts are clamped to valid unit indices and repaired to be monotone.

Summary:

| criterion | pass rate |
|:---|---:|
| Mando selected KLN remains `χ < 1` | 1.000 |
| Mando selected KLN remains lowest-`χ` branch | 0.844 |
| live-crickets selected DA remains `χ > 1` | 0.597 |
| live-crickets selected DA has lower `χ` than KLN | 0.699 |
| live-crickets selected DA has `V_carrier >= KLN` | 0.905 |
| live-crickets full controlled condition | 0.325 |

Interpretation:

- Mando/KLN is robust under local scoring perturbation.
- live-crickets/DA is not reducible to `χ` alone. It needs `V_carrier` and branch semantics to distinguish controlled reset from loop-preserving drift.

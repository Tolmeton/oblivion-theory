# Issue Draft — e2 / Lucas threshold framing

**Target**: https://github.com/the-omega-institute/automath/issues/new
**Suggested title**: `q=6,7 counterexamples to the e2(A_q)=L_q extension; q=5 as the first visible second-lift threshold`

---

## Issue body

Following the closure of #25 and the merge of PR #28, I want to isolate the first of the two research questions raised in the final comment there.

## What q=6,7 settle

The coincidence

\[
e_2(A_5)=L_5
\]

does **not** extend as a family law to `q=6,7`.

So the main numerical question now has a clean answer: the Lucas equality breaks immediately beyond `q=5`.

## Local probe

I re-ran the local reconstruction script from the exact `momentSum` data:

- source-backed prefix validation passes for `q=2,3,4,5,6,7`
- the `q=5` official kernel remains the sign-flipped version of the exact moment companion
- I then checked both:
  - the exact moment-companion side, and
  - the sign convention that reproduces the official `q=5` kernel

### Exact moment-companion side

| q | e2(A_q) | L_q |
|---|---:|---:|
| 5 | -11 | 11 |
| 6 | -17 | 18 |
| 7 | -26 | 29 |

### Sign extension matching the official q=5 kernel

| q | e2(A_q) | L_q |
|---|---:|---:|
| 5 | 11 | 11 |
| 6 | 17 | 18 |
| 7 | 26 | 29 |

So the identity fails immediately for `q>5` under either reading.

## What survives structurally

What survives is not a Lucas-trace law, but a threshold phenomenon at low `q`.

At `q=4 -> 5` one has the exact coordinate exchange

\[
(\operatorname{tr}(\mathrm{Sym}^2 A_4),\operatorname{tr}(\Lambda^2 A_4))
=
(11,-7)
\to
(-7,11)
=
(\operatorname{tr}(\mathrm{Sym}^2 A_5),\operatorname{tr}(\Lambda^2 A_5)).
\]

This is accompanied by the supertrace flip

\[
\operatorname{str}(W_4)=+18 \to -18=\operatorname{str}(W_5),
\qquad
W_q:=\mathrm{Sym}^2(V_q)\oplus \Pi \Lambda^2(V_q).
\]

That is why I no longer read `e_2(A_5)=L_5` as the beginning of an extension law.

I read it instead as a one-step coincidence at the exact boundary where the second-lift balance changes sign: the exterior sector has just overtaken the symmetric sector, and at that same boundary its trace happens to match `L_5`.

So my current formulation is:

- `e2(A_5)=L_5` is **not** a persistent Lucas law
- `q=5` remains special because the second-lift balance changes sign there
- the clean positive statement is that `q=5` is the **first visible second-lift threshold**, not that Lucas agreement continues afterward

## Secondary observation on higher q

For the reconstructed `q=6,7` kernels, the decomposition itself does not degrade:

\[
\operatorname{tr}(\mathrm{Sym}^2 A_q)+\operatorname{tr}(\Lambda^2 A_q)=\operatorname{tr}(A_q)^2,
\]

and in the current reconstructed/proxy extension through `q=10`, the `\Lambda^2` sector remains dominant rather than swapping back:

| q | tr(Sym^2 A_q) | tr(Lambda^2 A_q) |
|---|---:|---:|
| 8 | -36 | 40 |
| 9 | -58 | 62 |
| 10 | -92 | 96 |

I am **not** claiming that this has already been established in the official higher-q collision-kernel basis. This is only a local proxy coming from the reconstructed moment companion. The intended hard claim here is still just the `q=6,7` counterexample to the Lucas extension.

## Proposed formulation

So the formulation I would now propose is:

1. a negative result about the extension `e2(A_q)=L_q`, and
2. a positive result that `q=5` is the first visible second-lift threshold, where the symmetric/exterior balance changes sign.

That seems cleaner to me than asking whether the Lucas coincidence itself persists, because the coincidence does not persist, while the threshold structure does.

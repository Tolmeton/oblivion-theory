# Issue Draft v3 — final

**Target**: https://github.com/the-omega-institute/automath/issues/new
**Title**: Your carry defect has an information-geometric interpretation

---

## Issue Body

### What I found

I read your Lean 4 source (`CarryDefect.lean`, `WalshStokes.lean`, `CollisionKernel.lean`, `Fold.lean`). Your carry defect — the fact that folding doesn't commute with addition — has a parallel in **information geometry** (Amari 2016) that may be useful for your "Bridge to known mathematics" narrative.

In the geometry of probability distributions, projecting a high-dimensional model to a lower-dimensional one also fails to commute with composition, and the error generates **curvature**. I've proved that this curvature is nonzero iff the projection loses information non-uniformly across directions. Your carry defect appears to be the **discrete, finite-field version** of this.

### Five correspondence points

I'm being explicit about what's proved and what's not:

| # | Your theorem (Lean 4) | Continuous parallel | Status |
|:--|:--|:--|:--|
| 1 | `restrict_functorial` — fold composes | Coarse-graining composes: projecting A→C = projecting A→B→C | **Both proved** |
| 2 | `restrict_stableAdd_carry_defect` — fold doesn't commute with addition (κ ≠ 0) | Projection doesn't commute with composition; the error is called curvature | **Your side: Lean-proved. My side: conjecture.** The bridge (a functor from distribution spaces to hypercubes) is unproved |
| 3 | `walshFlux` + `deltaSet` — discrete Stokes | Curvature decomposes into a "direction mismatch" part and a "twist" part (Leibniz rule) | **Both proved** (different spaces) |
| 4 | `momentSum_two_mono'` — S₂ is monotone | Information loss under projection is monotone (data processing inequality) | **Both proved** |
| 5 | σ-algebra non-expansion G^{L+1} ⊆ G^{L} | Coarser observation loses structure monotonically | **Both proved** |

**On Point 2 specifically**: your κ ∈ {0,1} discretizes a continuous curvature condition. The structural parallel is strong — both measure the failure of projection to preserve algebraic operations. But I want to be honest: the formal bridge (a composition-preserving functor between your space and mine) does not yet exist. What exists is a candidate: interpret each bit position as a binary random variable, stable words as constrained product distributions, and fold as marginalization. Whether this candidate preserves composition is my open problem.

### What I don't have (and you might)

Your collision kernels share **tr = 2, det = −2** across moment orders q = 2, 3, 4. This spectral invariant has no counterpart in my framework. A naive guess: since your Perron eigenvalues satisfy r_q^{1/q} → √φ, perhaps tr and det encode a constraint that forces the golden ratio to appear as the spectral limit — but I don't have the tools to check this. If you have intuition about why these values are universal, I'd be very interested.

### Reference

I've written a [detailed dictionary](https://github.com/Tolmeton/oblivion-theory/blob/main/bridge/automath/dictionary.md) mapping your Lean 4 theorems to my framework, with precision labels on each entry. There are also two short essays if you want more context. [^1]

[^1]: [Curvature is the Carry of Oblivion](https://github.com/Tolmeton/oblivion-theory/blob/main/bridge/automath/curvature_is_the_carry_of_oblivion.md) (carry defect as discrete curvature, with three analogies) and [It from Oblivion](https://github.com/Tolmeton/oblivion-theory/blob/main/bridge/automath/It_from_Oblivion_en.md) (broader connections including The Omega). English translations are AI-assisted; math is exact.

Happy to discuss if any of this resonates.

**Tolmetes** ([@tolmeton](https://github.com/Tolmeton)) — [full theory (14 papers)](https://github.com/Tolmeton/oblivion-theory)

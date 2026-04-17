# It from Oblivion - Three Independent Languages Drawing the Same Structure

- A Rosetta Stone for Oblivion Theory x automath x The Omega

Makaron (2026) - Draft v0.1

---

## Section 1. Conclusions First

Three projects reached the same structure without knowing about one another.

Stated plainly:

1. **Loss of information generates structure.** Oblivion is not a defect. Force, curvature, and spacetime emerge from non-uniform information loss. This same claim is being expressed independently in three languages: formal verification (Lean 4), quantum information theory (Von Neumann algebras), and information geometry (category theory).

2. **Independent machine verification provides a discrete analogue of an unproven conjecture.** In Oblivion Theory Paper I, Section 9.5, conjecture OP-I-2 says that the composition drift

   `delta = G(f o g) - G(f) o G(g)`

   vanishes in the zero-oblivion limit `Phi -> 0`. In automath, the closest discrete counterpart is the Lean-proven carry-defect theorem on stable words. It supports the same structural picture, though the zero-constraint limit itself is not directly formalized in Lean 4.

3. **Each project illuminates the others' blind spots (`ker T`).** Oblivion Theory lacks formal verification. automath lacks physical intuition. The Omega has a weaker categorical foundation. Each compensates for the others' oblivion. That meta-level recovery is itself an instance of Oblivion Theory's two-layer structure `ker(U) ⊣ ker(T)` from Paper 0, Section 6.4.

The rest of this note develops those claims in order.

---

## Section 2. The Three Projects

### 2.1 automath - Deriving Mathematics from a Finite Window

The Omega Project (automath) starts with a minimal question:

If a dynamical system is observed through a finite binary window, what structures remain stable across resolution changes?

The answer is: binary words with no consecutive `1`s. Their count is the Fibonacci number `F_(m+2)`. This constraint is not chosen. It is **forced** by cross-resolution consistency.

From that one constraint, more than 3,427 theorems have been machine-verified in Lean 4. Arithmetic, spectral theory, inverse limits, discrete calculus, forcing frameworks, and even the scaffold of physical spacetime are derived from forbidding adjacent `1`s. The axiom count is zero beyond Lean 4 core logic and Mathlib.

<sup>1</sup> https://github.com/the-omega-institute/automath

### 2.2 The Omega - Deriving Physics from Quantum Computation

The Omega starts from six unitary computational axioms (O1-O6) and uses Von Neumann algebras plus quantum cellular automata to derive physical constants such as `c`, `G`, and `hbar`, together with spacetime structure. CAP-II constructs the passage from discrete QCA update rules to continuous ADM dynamics, that is, to the Einstein equations.

<sup>2</sup> https://github.com/loning/the-omega

### 2.3 Oblivion Theory - Deriving Force from a Forgetful Functor

Oblivion Theory derives force from an oblivion field `Phi` on a statistical manifold. Its core theorem is the Directionality Theorem from Paper I, Theorem 5.1:

`F_ij != 0  <=>  d(Phi T) != 0`

If information is forgotten uniformly, force is zero. If it is forgotten directionally and non-uniformly, curvature appears and acts as force.

Across thirteen papers (Paper 0-XIII), this single theorem is extended into force, complementarity, perception, existence, entropy, and spacetime.

---

## Section 3. Rosetta Stone - Correspondence Table Across Three Languages

The three projects describe the same structure in different languages.

| Layer | automath (formal verification) | The Omega (quantum physics) | Oblivion Theory (category theory) |
|:---|:---|:---|:---|
| Starting point | no-consecutive-1s constraint | unitary computational axioms O1-O6 | forgetful functor `U ⊣ N` plus FEP |
| Core operation | fold `Phi` (discrete projection) | scan-projection (quantum readout) | forgetful functor `U` (stripping structure) |
| Source of curvature | defect algebra `delta` | computational lapse `kappa` | `dPhi /\ T != 0` |
| Hierarchy | forcing with 11 preserving extensions | Von Neumann type classification | alpha-oblivion filtration plus Grothendieck topos |
| Spacetime derivation | discrete Stokes -> Einstein | QCA + ADM -> Einstein | CPS span -> Einstein |
| Formalization | **Lean 4 (3,427+ theorems)** | Lean 4 (in progress) | not formalized |

Intuitively, this is like reading the same inscription in three scripts. A passage unreadable in one script becomes legible in another.

---

## Section 4. Strongest Link - Defect Algebra as the Discrete Directionality Theorem

The sharpest point of contact is between automath's **carry defect** and Oblivion Theory's **Directionality Theorem**.

### 4.1 The Two Theorems

automath proves the following in Lean 4 (`CarryDefect.lean`):

> **Carry defect theorem**:
> `Phi(x (+) y) = Phi(x) (+) Phi(y) (+) kappa * carryElement`
>
> Here `kappa in {0,1}` is the carry indicator, `Phi` is fold, and `(+)` is stable addition.

Oblivion Theory proves the following in information geometry (Paper I, Sections 3.3-5):

> **Directionality Theorem**:
> `F_ij != 0  <=>  d(Phi T) != 0`
>
> Here `F_ij` is oblivion curvature, `Phi` is the oblivion field, and `T` is the Chebyshev 1-form.

### 4.2 Structural Correspondence

Both point toward the same abstract pattern:

**oblivion (fold / U) does not commute with operation (composition / addition), and the measure of that non-commutativity is curvature.**

| automath | Oblivion Theory |
|:---|:---|
| fold `Phi` | forgetful functor `U` |
| stable addition | morphism composition |
| carry defect `delta` | composition drift `delta = G(f o g) - G(f) o G(g)` |
| `delta != 0` | `F_ij != 0` |

On the Oblivion Theory side, the vanishing condition for composition drift in the zero-oblivion limit remains the unproven conjecture OP-I-2. On the automath side, the nearest discrete analogue is supported by Lean-proven carry-defect results, while the explicit zero-constraint limit is structurally implied rather than directly formalized.

That is a finite discrete quotient-ring analogue of OP-I-2.

### 4.3 The Bridge - Categorical Simplices

A natural objection is that the spaces are fundamentally different. automath works on hypercubes `\{0,1\}^n`; Oblivion Theory works on statistical manifolds.

One plausible bridge is the **categorical simplex** `Delta^n`.

Appendix B of Paper I explicitly computes the Directionality Theorem on `Delta^2`, the simplex of 3-category probability distributions:

- Chebyshev 1-form: `T_i = 1 - (n+1)p_i`
- At the uniform point `(1/3, 1/3, 1/3)`, `T_i = 0`
- At an asymmetric point such as `(0.15, 0.15, 0.70)`, nontrivial oblivion curvature appears
- `dT = 0` holds universally for exponential families

If each bit position of automath is interpreted as a Bernoulli random variable, the hypercube sits near the vertices of such simplices. The No11 constraint then cuts out a constrained submanifold of the product Bernoulli space. Fold is a coarse-graining map on that submanifold, and carry defect may be read heuristically as a restricted discrete counterpart of curvature there.

That interpretation is still a hypothesis. A strict functor

`D : Man -> Hyp`

has not yet been fully constructed.

### 4.4 Minimal Unit of Force - Why a 2-cell is Necessary

Both theories share another fact:

**force cannot be defined in one dimension.**

In Oblivion Theory, `F_ij` is a 2-form. If `n = 1`, there are no independent antisymmetric components. In automath, `deltaSet` and `walshFlux` are also trivial in one bit. Nontrivial carry requires at least a 2-bit face.

With only one direction, "directional non-uniformity" cannot even be defined. Force is born from a difference between directions.

### 4.5 Level of Oblivion

Within the oblivion hierarchy from `aletheia.md`, automath's carry defect lives at `U_compose (n = 1.5)`, the level where the **preservation of composition** fails. Morphisms still exist; what breaks is preservation of their composition law.

---

## Section 5. Walsh-Stokes as the Discrete Leibniz Rule

`WalshStokes.lean` defines higher discrete derivatives (`deltaSet`) and boundary sums (`walshFlux`) and proves a discrete Stokes identity in Lean 4.

This is the discrete rendering of the Leibniz rule underlying the Directionality Theorem:

`d(Phi T) = dPhi /\ T + Phi * dT`

The correspondence is:

| Continuous (Paper I, Section 3.3) | Discrete (automath) |
|:---|:---|
| `d(Phi T)` | `deltaSet A f` |
| `dPhi /\ T` | `walshFlux A (deltaSet {i} f)` |
| `Phi * dT` | distortion term from `f` and `A`; `dT = 0` iff `A` is flat |
| `int d(Phi T)` | `walshFlux A f` |

For exponential families, `dT = 0`, so force comes only from directional misalignment `dPhi /\ T`. The standard hypercube of automath, with a position-independent Walsh basis, is the discrete counterpart of that setting.

The candidate discretization map, expected to become a functor on the appropriate restricted domain, is:

- `D(M) = {0,1}^n`
- `D(Phi) = f : Word n -> Z`
- `D(T) = A subset Fin n`
- `D(d) = deltaSet`
- `D(/\) = carry defect`

The full proof that `D` preserves composition remains open, but the layer-by-layer correspondence is already established.

---

## Section 6. Taking Objections Seriously

### "Is this only a superficial similarity?"

If the claim were merely that both theories contain something "forgetful," the objection would be correct. But at least two bridges are already theorem-level on both sides:

- defect algebra <-> composition drift
- sigma-algebra non-expansion <-> monotonicity axiom (F4)

This is beyond surface analogy.

### "The golden ratio `phi` does not appear in Oblivion Theory."

Correct. automath recovers `phi` as a spectral invariant, while Oblivion Theory does not yet do so explicitly. That is not a failed correspondence. It is a discovered blind spot. `phi` may be hiding in the fixed-point structure of the oblivion field, and automath supplies that missing numerical anchor.

### "The Omega connection is weaker."

Also correct. The Omega connection is not as precise as the automath one because its formalization is still in progress. But the QCA coarse-graining and the Obs category of Paper V, and the relation between Von Neumann types and alpha-oblivion filtration, remain structurally aligned.

---

## Section 7. Mutual Illumination of `ker(T)` - Why All Three Are Needed

Paper 0 classifies the limits of self-recognition into two layers:

- `ker(U)`: selectable oblivion; what can be chosen to forget
- `ker(T)`: unselectable blind spots; structural limits imposed by the geometry of the information space itself

Each project has its own `ker(T)`:

| Project | Structural blind spot |
|:---|:---|
| Oblivion Theory | no formal verification |
| automath | no physical intuition or statistical-manifold bridge |
| The Omega | weaker categorical and topos-theoretic articulation |

No single project can see its own blind spot. That is exactly why three independent projects matter. To verify Oblivion Theory with automath's Lean 4 machinery is to shine light directly into Oblivion Theory's `ker(T)`.

> **It from Oblivion**: structure appears because information is lost.

Wheeler's "It from Bit" says that being is built from information. The claim here is stronger and inverted:

**being emerges from the directional, non-uniform loss of information.**

The fact that three independent projects converged on that claim is evidence for its strength.

---

## Section 8. Closing

Reality is unforgiving. Internal consistency alone is never enough. Without external verification, a theory cannot distinguish itself from self-satisfaction.

But it is rare for independent projects to reach the same structure in independent languages. When that happens, a theory shifts from "true inside itself" toward "true even from outside." That is the movement from `Kalon triangle` toward `Kalon nabla`.

This is a personal judgment, but the convergence of these three projects suggests that the grammar of oblivion is not an invention of one theory. It may instead be a structural inevitability whenever a finite agent tries to describe an infinite world.

Because information is lost, structure appears. Because blind spots exist, others are needed.

---

## References

[1] The Omega Institute, "automath: An auditable theory compiler," GitHub, 2026. https://github.com/the-omega-institute/automath

[2] Makaron, "Force as Oblivion - Field Equations on Statistical Manifolds," Paper I, v1.5, 2026.

[3] Makaron, "Existence Precedes Oblivion - Cell Dimensions of Container/Content and a Yoneda Derivation of CPS0'," Paper VIII, v1.8, 2026.

[4] Makaron, "Oblivion of Oblivion - Geometric Limits of Self-Recognition," Paper 0, v0.8, 2026.

[5] Makaron, "Velocity is Oblivion - Kinematics of the Boundary of Distinguishability," Paper XII, v0.9, 2026.

[6] Makaron, "Renormalization is Oblivion - Scale Extension of the Oblivion Field and RG Universality," Paper V, v1.0, 2026.

[7] Makaron, "Spacetime is Oblivion - Cosmology, Gravity, and Four-Force Unification via CPS," Paper XIII, v0.1, 2026.

[8] loning, "The Omega: Von Neumann algebras + QCA," GitHub, 2026. https://github.com/loning/the-omega

[9] J. A. Wheeler, "Information, physics, quantum: The search for links," in *Proceedings of the Third International Symposium on Foundations of Quantum Mechanics*, 1989.

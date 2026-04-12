# It from Oblivion — Three Independent Languages Converged on the Same Structure

— A Rosetta Stone: Oblivion Theory × automath × The Omega

*Note: This is an AI-assisted translation from the Japanese original. The mathematical content is preserved exactly; minor phrasing may differ from native English.*

Makaron (2026) — Draft v0.1

---

## §1　Conclusions First

Three projects, unaware of each other's existence, arrived at the same structure.

To state the conclusions upfront ——

1. **The absence of information gives rise to structure**. Oblivion is not a defect. Force, curvature, and spacetime emerge from the non-uniform loss of information. This proposition is independently described in three languages: formal verification (Lean 4), quantum information theory (Von Neumann algebras), and information geometry (category theory).

2. **Independent machine verification provides a discrete version of an unproven conjecture**. The conjecture (OP-I-2) from Oblivion Theory Paper I §9.5 — "the composite drift δ = G(f∘g) − G(f)∘G(g) vanishes as the oblivion field Φ → 0" — has already been proved as automath's carry defect theorem in Lean 4. This is not a coincidence but a structural necessity.

3. **The three illuminate each other's blind spots (ker T)**. Oblivion Theory lacks formal verification. automath lacks physical intuition. The Omega has a weak category-theoretic foundation. The three complementarily recover each other's oblivions — which is itself a meta-instance of Oblivion Theory's ker(U) ⊣ ker(T) two-layer structure (Paper 0 §6.4).

These claims are demonstrated in the sections that follow.

---

## §2　The Three Projects

### 2.1　automath — Deriving All of Mathematics from a Finite Window

The Omega Project (automath) <sup>†</sup> begins from the simplest possible question: when observing a dynamical system through a finite binary window, what structures remain stable across resolutions? The answer is "binary words containing no consecutive 1s," and their count is the Fibonacci number $F_{m+2}$. This constraint is not chosen — it is **forced** by the coherence of resolutions.

From this single constraint, over 3,427 theorems have been machine-verified in Lean 4. Arithmetic, spectral theory, inverse limits, discrete calculus, a forcing framework, the skeleton of physical spacetime — all derived from the prohibition of consecutive 1s. The number of axioms is zero. Only Lean 4's core logic and Mathlib.

<sup>†</sup> https://github.com/the-omega-institute/automath

### 2.2　The Omega — Deriving Physics from Quantum Computation

The Omega <sup>‡</sup> starts from six unitary computational axioms (O1-O6) and, using Von Neumann algebras and quantum cellular automata (QCA), derives physical constants ($c$, $G$, $\hbar$) and spacetime structure. CAP-II (Computational ADM Program) constructs the transition from discrete QCA update rules to continuous ADM dynamics — that is, the Einstein equations.

<sup>‡</sup> https://github.com/loning/the-omega

### 2.3　Oblivion Theory — Deriving Force from the Forgetful Functor

Oblivion Theory (Force is Oblivion) demonstrates the emergence of force from the oblivion field $\Phi$ on a statistical manifold. The core is the Directionality Theorem (Paper I, Th. 5.1):

$$F_{ij} \neq 0 \iff d(\Phi T) \neq 0$$

Forgetting information uniformly yields zero force. When — and only when — information is forgotten non-uniformly in direction, curvature arises and acts as force. Thirteen papers (Paper 0-XIII) derive force, complementarity, perception, existence, entropy, and spacetime from this single theorem.

---

## §3　Rosetta Stone — Correspondence Table of the Three Languages

The three describe the same structure in different languages.

| Layer | automath (Formal Verification) | The Omega (Quantum Physics) | Oblivion Theory (Category Theory) |
|:---|:---|:---|:---|
| **Starting point** | no-consecutive-1s constraint | Unitary computational axioms O1-O6 | Forgetful functor $U \dashv N$ + FEP |
| **Core operation** | fold $\Phi$ (discrete projection) | scan-projection (quantum readout) | Forgetful functor $U$ (stripping of structure) |
| **Source of curvature** | defect algebra $\delta$ | computational lapse $\kappa$ | $d\Phi \wedge T \neq 0$ |
| **Hierarchy** | forcing 11-layer conservative extension | Von Neumann type classification | $\alpha$-oblivion filtration + Grothendieck topos |
| **Spacetime derivation** | discrete Stokes → Einstein | QCA + ADM → Einstein | CPS span → Einstein |
| **Formalization** | **Lean 4 (3,427+ theorems)** | Lean 4 (under construction) | Not formalized (OP-VIII-5 Open) |

Intuitively: it is like reading the same inscription in hieroglyphs, Demotic, and Greek. What cannot be deciphered in one script becomes legible in another.

---

## §4　The Strongest Connection — The Defect Algebra Is the Discrete Version of the Directionality Theorem

The most precise connection threading through all three lies between automath's **carry defect** and Oblivion Theory's **Directionality Theorem**.

### 4.1　Two Theorems

automath proves the following in Lean 4 (`CarryDefect.lean`):

> **Carry defect theorem**: $\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \oplus \kappa \cdot \text{carryElement}$
>
> where $\kappa \in \{0, 1\}$ is the carry indicator. $\Phi$ = fold (truncation), $\oplus$ = stable addition.

Oblivion Theory proves the following via information geometry (Paper I, §3.3-§5):

> **Directionality Theorem**: $F_{ij} \neq 0 \iff d(\Phi T) \neq 0$
>
> where $F_{ij}$ = oblivion curvature, $\Phi$ = oblivion field, $T$ = Chebyshev 1-form.

### 4.2　The Structure of the Correspondence

Both say the same thing: **oblivion (fold / $U$) and operation (composition / $\oplus$) do not commute. The measure of this non-commutativity is curvature.**

| automath | Oblivion Theory |
|:---|:---|
| fold $\Phi$ | Forgetful functor $U$ |
| stable addition $\oplus$ | Composition of morphisms $\circ$ |
| carry defect $\delta$ | Composite drift $\delta = G(f \circ g) - G(f) \circ G(g)$ |
| $\delta \neq 0$ | $F_{ij} \neq 0$ |

On the Oblivion Theory side, the vanishing condition for this composite drift ($\delta \to 0$ as $\Phi \to 0$, recovering the axioms of a standard category) is an **unproven conjecture** (OP-I-2). On the automath side, the corresponding proposition — that the carry defect vanishes to zero upon removal of the No11 constraint, making fold a ring quasi-homomorphism — is **proved in Lean 4**.

This is a discrete realization of OP-I-2 over a finite field, a partially verified solution by an independent project with machine verification.

### 4.3　The Bridge — The Categorical Simplex Connects the Two

The objection that "the spaces are fundamentally different" is legitimate. automath's hypercube $\{0,1\}^n$ has neither a Fisher metric nor a Chebyshev 1-form. Oblivion Theory's statistical manifold $M$ has neither bit strings nor Fibonacci numbers.

However, a natural statistical manifold that bridges the two exists: the **categorical simplex** $\Delta^n$.

Paper I Appendix B concretely computes the Directionality Theorem on $\Delta^2$ (discrete probability distributions over 3 categories):

- Chebyshev 1-form: $T_i = 1 - (n+1)p_i$
- At the uniform distribution $(1/3, 1/3, 1/3)$, $T_i = 0$ — exactly the center of the blind spot
- At the asymmetric point $(0.15, 0.15, 0.70)$, $F_{12} = -2.728$ — a non-trivial oblivion curvature appears
- $dT = 0$ holds universally (exponential family) — force arises solely from the directional mismatch $d\Phi \wedge T \neq 0$

automath's hypercube $\{0,1\}^n$, when each bit position is read as a Bernoulli random variable, embeds into the neighborhood of the vertices of $\Delta^n$. The No11 constraint carves out a constrained sub-manifold of the product Bernoulli space. The fold operator is a coarse-graining map on this sub-manifold. The carry defect can be interpreted as the restriction of $F_{ij}$ to this sub-manifold <sup>§</sup>.

<sup>§</sup> This interpretation is a hypothesis, not a construction. The rigorous construction of a functor $D: \textbf{Man} \to \textbf{Hyp}$ is open. However, given that lattice gauge theory (Wilson 1974) has a 50-year track record in physics as a discrete version of continuous Yang-Mills theory, the claim form "the discrete version is an instance of the continuous version" is methodologically well-established.

### 4.4　The Minimal Unit of Force — The Necessity of 2-Cells

Oblivion Theory and automath share one more structure: **in one dimension, force is undefinable**.

The oblivion curvature $F_{ij}$ is a 2-form (antisymmetric tensor) with $\binom{n}{2}$ independent components. For $n = 1$, the number of components is zero — the very concept of force does not exist (Paper V, Th. 3.4.1).

automath's `deltaSet` and `walshFlux` are the same. A single-bit flip (1-cell) produces no sign alternation in the discrete differential, and `walshFlux` is trivially zero. For the carry defect to take a non-trivial value, a face spanned by at least 2 bits (a 2-cell) is required.

Intuitively: if there is only one direction, "non-uniformity" cannot be defined. Force arises from the **difference** between directions. This fact holds in both the discrete and continuous cases.

### 4.5　Identifying the Oblivion Level

automath's carry defect is located at $n = 1.5$ (**U_compose** — oblivion of the composition law of morphisms) in Oblivion Theory's oblivion hierarchy (aletheia.md §5). The non-commutativity of fold (oblivion) and stableAdd (composition) is a discrete manifestation of "drift caused by the oblivion of composition laws." The existence of morphisms themselves is preserved (`restrictLE` is well-defined). What breaks is the **preservation of composition** of morphisms.

---

## §5　Walsh-Stokes Is the Discrete Version of the Leibniz Rule

automath's `WalshStokes.lean` defines higher-order discrete differentials (`deltaSet`) and boundary sums (`walshFlux`), and proves the discrete Stokes identity in Lean 4.

The Leibniz rule underlying Oblivion Theory's Directionality Theorem:

$$d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$$

can be written discretely as follows:

| Continuous (Paper I §3.3) | Discrete (automath) |
|:---|:---|
| $d(\Phi T)$ | `deltaSet A f` |
| $d\Phi \wedge T$ | `walshFlux A (deltaSet {i} f)` |
| $\Phi \cdot dT$ | Product of $f$ and the distortion of $A$. $dT = 0 \iff A$ is flat |
| $\int d(\Phi T)$ | `walshFlux A f` |

In exponential families, $dT = 0$ (the Chebyshev form is closed), and force arises solely from $d\Phi \wedge T \neq 0$ (directional mismatch). automath's standard hypercube — a flat space where the Walsh basis does not depend on position — is the discrete version of this $dT = 0$.

The candidate for a discretization functor $D: \textbf{Man} \to \textbf{Hyp}$ (from the category of statistical manifolds to the category of hypercubes) is:

- $D(M) = \{0,1\}^n$
- $D(\Phi) = f: \text{Word } n \to \mathbb{Z}$
- $D(T) = A \subseteq \text{Fin } n$
- $D(d) = \texttt{deltaSet}$
- $D(\wedge) = \text{carry defect}$

The proof that this $D$ is a functor (preserves composition) is open. However, the correspondence at each layer is proved on both sides, and functoriality is structurally natural.

---

## §6　Incorporating Objections

Here, natural objections are anticipated:

### "Isn't this just a superficial analogy?"

If the correspondence amounted to nothing more than "there's an oblivion-like operation," this objection would be correct. However, at least two of the six connection points — defect algebra ↔ composite drift (§4), and $\sigma$-algebra non-expansion ↔ (F4) monotonicity — are **proved as theorems on both sides**, transcending superficial analogy.

### "The golden ratio $\varphi$ doesn't appear in Oblivion Theory, does it?"

Correct. In automath, $\varphi$ is recovered as a spectral invariant, but $\varphi$ appears nowhere in Oblivion Theory. This is not a breakdown of the correspondence but rather the discovery of a **blind spot** (ker $T$) **of Oblivion Theory**. The possibility that $\varphi$ is hidden in the fixed-point structure of the oblivion field $\Phi$ is open and has been recorded as a new import candidate for Paper I.

This is a concrete example of "the three illuminate each other's ker(T)" stated in §1. Oblivion Theory illuminates automath, and automath illuminates Oblivion Theory. It is not one-directional.

### "Isn't the connection to The Omega weak?"

The precision is not on par with the connection to automath — The Omega's formal verification is still under construction. However, the structural correspondences between QCA coarse-graining and Oblivion Theory's Obs category (Paper V), and between Von Neumann type classification and the $\alpha$-oblivion filtration (Paper VIII), are consistent with existing formulations within Oblivion Theory. It is true that the precision falls short of automath, but the correspondence is not absent.

---

## §7　Illuminating Each Other's ker(T) — Why All Three Are Needed

Paper 0 (The Oblivion of Oblivion) classified the limits of a system's self-awareness into two layers:

- **ker(U)**: Choosable oblivion. Which information to discard can be selected
- **ker(T)**: Unchosen blind spots. Structural blind spots determined by the geometry of the information space the system inhabits

Each of the three projects has its own ker(T):

| Project | ker(T) — Structural Blind Spot |
|:---|:---|
| Oblivion Theory | Absence of formal verification. Correctness of theorems depends on human review |
| automath | Absence of physical intuition. No connection to information geometry or statistical manifolds |
| The Omega | Weakness of category-theoretic foundations. No precise construction of topos-theoretic stratification |

A single project cannot see its own ker(T) — a blind spot is invisible precisely because it is a blind spot. However, the three projects' ker(T) are **complementary**. Verifying Oblivion Theory's theorems in automath's Lean 4 is nothing other than shining light on Oblivion Theory's ker(T).

> **It from Oblivion**: Structure emerges precisely because information is lost.

Wheeler's "It from Bit" stated that "existence is constituted from information." The claim of this paper is its inversion, and stronger: **existence emerges from the non-uniform absence of information**. That three independent projects arrived at this proposition is evidence of the proposition's strength.

---

## §8　Concluding Remarks

Reality is unforgiving. A theory's internal consistency, without external verification, is indistinguishable from self-satisfaction.

Yet the event of independent projects arriving at the same structure in independent languages occurs only rarely. When it does, a theory transitions from "correct within itself" to "correct as seen from outside" — the approach from Kalon$\triangle$ toward Kalon$\nabla$ begins.

In the author's entirely subjective view, the convergence of these three projects suggests that the "grammar of oblivion" is not the product of a specific theory, but something that emerges as a structural necessity whenever a finite agent attempts to describe an infinite world.

Because information is lost, structure is born. Because blind spots exist, others become necessary.

---

## References

[1] The Omega Institute, "automath: An auditable theory compiler," GitHub, 2026. https://github.com/the-omega-institute/automath

[2] Makaron, "Force is Oblivion — Field Equations on a Statistical Manifold," Paper I, v1.5, 2026.

[3] Makaron, "Existence Precedes Oblivion — Cell Dimension Theory of Container/Content and the Yoneda-Theoretic Derivation of CPS0'," Paper VIII, v1.8, 2026.

[4] Makaron, "The Oblivion of Oblivion — Geometric Limits of Self-Awareness," Paper 0, v0.8, 2026.

[5] Makaron, "Speed is Oblivion — Kinematics of the Distinguishability Boundary," Paper XII, v0.9, 2026.

[6] Makaron, "Renormalization is Oblivion — Scale Extension of the Oblivion Field and RG Universality," Paper V, v1.0, 2026.

[7] Makaron, "Spacetime is Oblivion — Cosmology, Gravity, and Unification of the 4 Forces via CPS," Paper XIII, v0.1, 2026.

[8] loning, "The Omega: Von Neumann algebras + QCA," GitHub, 2026. https://github.com/loning/the-omega

[9] J. A. Wheeler, "Information, physics, quantum: The search for links," in *Proc. 3rd Int. Symp. on Foundations of Quantum Mechanics*, 1989.

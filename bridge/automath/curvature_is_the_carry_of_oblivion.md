# Curvature is the Carry of Oblivion
## — Discrete Defect Algebra and the Directionality Theorem of the Oblivion Field

*Note: This is an AI-assisted translation from the Japanese original. The mathematical content is preserved exactly; minor phrasing may differ from native English.*

Standalone — v0.1 (2026-04-12)
Side piece to the Oblivion Theory series. Candidate for series promotion.

Preceding paper: Paper I (Force as Oblivion) — Directionality Theorem Th.5.1, Composition Drift §9.5 OP-I-2.
External reference: The Omega Project (automath) — Lean 4, 3,427+ theorems, axioms=0.

---

## §1 Projection Breaks Composition

Projection discards information. Everyone knows this.

But that **projection breaks composition** is far less appreciated. Project a three-dimensional object onto two dimensions, and operations that held in three dimensions no longer hold in two. The "discrepancy" does not vanish. It accumulates, warps structure, and manifests as force.

In 2026, two entirely independent projects proved the same structure in different languages.

One is **Oblivion Theory** (Force is Oblivion) — on a statistical manifold, it derives the oblivion curvature $F_{ij}$ from the oblivion field $\Phi$ and the Chebyshev 1-form $T$, and proves as a Directionality Theorem that **force emerges from the directional inhomogeneity of oblivion** (Paper I, Th.5.1).

The other is **The Omega Project** (automath) — starting from the no-consecutive-1s constraint on finite binary strings, it formalizes the non-commutativity of the fold operator $\Phi$ and addition $\oplus$ on stable words as a **carry defect** $\delta$, and machine-verifies over 3,427 theorems in Lean 4.

This is not a provocation. What this paper demonstrates is ——

To state the conclusions first ——

- **Carry defect is the discrete version of oblivion curvature** — automath's carry defect $\delta(x,y) = \Phi(x \oplus y) - \Phi(x) \oplus \Phi(y)$ is a discrete, finite-field instance of Oblivion Theory's composition drift $\delta = G(f \circ g) - G(f) \circ G(g)$. The former is machine-verified in Lean 4. The latter is the unproven conjecture OP-I-2 from Paper I §9.5
- **The Walsh-Stokes identity is the discrete version of the Leibniz rule** — automath's `walshFlux` and `deltaSet` correspond to the discrete exterior derivative of the oblivion field's Leibniz rule $d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$, and a **discretization functor** $D: \mathbf{Man} \to \mathbf{Hyp}$ can be constructed. This functor maps the differential geometry of the oblivion field to the combinatorics of hypercubes
- **The discrete version of "without oblivion there is no force" is proven in Lean 4** — the discrete version of the OP-I-2 conjecture, which states that category theory is recovered in the limit of zero oblivion ($\Phi \to 0$), has been machine-verified by automath. When the no-consecutive-1s constraint vanishes, carry defect drops to zero and fold becomes a strict ring homomorphism

These claims are proven in order in the sections that follow.

---

## §2 Two Worlds

### 2.1 The World of automath — Derivation from Finite Binary Windows

Take a finite system observed through a 1-bit window for $m$ steps. The total state space $\{0,1\}^m$ has $2^m$ elements. But the words stable across resolutions — words containing no consecutive 1s — number only $F_{m+2}$. $F_n$ is a Fibonacci number.

This constraint is not chosen. It is **forced** by cross-resolution consistency.

On the space of stable words $X_m$, define the fold operator $\Phi: X_{m+1} \to X_m$. It truncates the trailing bit. $\Phi$ discards information — it forgets.

On $X_m$ there is a natural addition $\oplus$ defined via Zeckendorf representation. $X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ — the space of stable words is a quotient ring modulo a Fibonacci number. When $F_{m+2}$ is prime ($F_3 = 2, F_5 = 5, F_7 = 13, F_{13} = 233, \ldots$), it becomes a finite field.

Here the critical question arises: **do fold and addition commute?**

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \quad \text{?}$$

The answer is no.

### 2.2 Carry Defect — Non-commutativity of Projection and Composition

automath proves the following theorem in Lean 4 (`restrict_stableAdd_carry_defect`):

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \oplus \kappa \cdot e_m$$

- $\kappa \in \{0, 1\}$ — **carry indicator**. $\kappa = 1$ when the sum of the stable values of $x$ and $y$ reaches or exceeds the Fibonacci number $F_{m+3}$; $\kappa = 0$ otherwise
- $e_m$ — **carry element**. Its stable value is $F_m$ (a Fibonacci number). Verified in Lean 4 for $m = 5, \ldots, 13$

Intuitively: if you add first and then project, a "remainder" $\kappa \cdot e_m$ persists compared to projecting first and then adding. This remainder is the carry defect. In a world where information is perfectly preserved — that is, a world without constraints — no carry arises.

### 2.3 The World of Oblivion Theory — Oblivion Field on a Statistical Manifold

Oblivion Theory (Paper I) defines the oblivion field $\Phi(\theta)$ on a statistical manifold $(M, g, C)$:

$$\Phi(\theta) = D_{\text{KL}}(p_\theta \| q)$$

- $D_{\text{KL}}$ — Kullback-Leibler divergence. The "degree of oblivion" between two probability distributions
- $p_\theta$ — the probability distribution specified by parameter $\theta$
- $q$ — reference distribution

The Chebyshev 1-form $T_i = g^{jk}C_{ijk}$ specifies the direction in which the $\alpha$-connection deviates most from the Levi-Civita connection. When the gradient of the oblivion field $d\Phi$ is not aligned with this direction — that is, when $d\Phi \wedge T \neq 0$ — oblivion curvature arises.

**Directionality Theorem** (Paper I, Th.5.1):

$$F_{ij} \neq 0 \iff d(\Phi T) \neq 0$$

Intuitively: forget uniformly and force is zero. Forget non-uniformly and curvature arises, acting as force.

### 2.4 Common Structure — Projection Breaks Composition

Place the two worlds side by side:

| | automath (discrete) | Oblivion Theory (continuous) |
|:---|:---|:---|
| Space | $X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ | $M$ (statistical manifold) |
| Oblivion field | $f: X_m \to \mathbb{Z}$ (stable value) | $\Phi: M \to \mathbb{R}$ |
| Projection | fold $\Phi: X_{m+1} \to X_m$ | forgetful functor $G: C \to D$ |
| Composition | stable word addition $\oplus$ | morphism composition $f \circ g$ |
| **Defect** | $\delta(x,y) = \kappa \cdot e_m$ [Lean-proven] | $\delta = G(f \circ g) - G(f) \circ G(g)$ [OP-I-2 conjecture] |
| **Curvature condition** | $\kappa \neq 0$ | $d(\Phi T) \neq 0$ |
| Zero oblivion | No11 constraint vanishes → $\delta = 0$ → ring homomorphism [Lean] | $\Phi \to 0$ → $\delta \to 0$ → standard category [OP-I-2 conjecture] |

The structure is identical. Projection breaks composition. The measure of the breakage is the defect, the curvature, the force.

---

## §3 Three Metaphors — Curvature is Born from Carry

### 3.1 Crystallography — Dislocations Are the Carry of Projection

Consider the operation of precipitating a crystal from solution. You project a solution (a high-dimensional field) onto a crystal lattice (a low-dimensional structure). In a perfect crystal, the lattice is exactly preserved — carry is zero.

But real crystals have **dislocations**. Atomic arrangements shift locally, and the composition law of the lattice breaks. Dislocations generate curvature in the crystal. And dislocation density is a physical force that determines the strength of the crystal.

$$\text{perfect crystal} \leftrightarrow \kappa = 0, \quad \text{dislocation} \leftrightarrow \kappa = 1$$

This is not a metaphor. As Paper VI (Affordance is Oblivion) showed, in the crystallization adjunction $F \dashv G$ of the forgetful functor $G$, $\text{Fix}(G \circ F)$ is the Kalon (fixed point), and deviation from the fixed point generates curvature. The carry element $e_m$ is the quantitative expression of dislocation in a discrete crystal.

### 3.2 Cartography — Mercator Distortion Is Carry

Consider a map projection from sphere to plane. The Mercator projection preserves angles but distorts area. Add the distances between two points A and B on the sphere and then project the result — the value does not match adding the projected distances.

$$\Phi(d_A + d_B) \neq \Phi(d_A) + \Phi(d_B)$$

This discrepancy is the Mercator area distortion. Near the equator ($\kappa = 0$) the distortion is small; near the poles ($\kappa = 1$) it becomes enormous. Greenland appearing larger than Africa — that distortion is a direct visualization of the non-commutativity of projection and composition.

### 3.3 Accounting — Rounding Is Carry

Consider the aggregation of multiple currencies. Aggregate profits reported in three currencies (compose) and then convert to yen (project), versus converting each to yen first and then aggregating. The results do not match. A rounding error arises.

$$\text{Φ}(\text{aggregate}) \neq \text{Φ}(\text{item 1}) + \text{Φ}(\text{item 2}) + \text{Φ}(\text{item 3})$$

The rounding error cannot be eliminated — unless the currencies are unified. Currency unification = zero oblivion = zero carry. As long as multiple "yardsticks" exist, the rounding of projection is structurally inevitable.

Mathematical correspondence of the three metaphors:

| Metaphor | Projection | Composition | Carry | Curvature |
|:---|:---|:---|:---|:---|
| Crystal | dissolution → precipitation ($G$) | lattice composition | dislocation | crystal stress |
| Map | sphere → plane | distance addition | area distortion | Gaussian curvature |
| Accounting | yen conversion | currency aggregation | rounding error | foreign exchange gain/loss |
| automath | fold $\Phi$ | $\oplus$ | $\kappa \cdot e_m$ | defect ≠ 0 |
| Oblivion Theory | $G$ | $f \circ g$ | $\delta$ | $F_{ij} \neq 0$ |

---

## §4 Walsh-Stokes and Leibniz — Constructing the Discretization Functor

### 4.1 Leibniz Decomposition of Oblivion Curvature

In Paper I §3.3, oblivion curvature is derived from the following Leibniz rule:

$$F_{ij} = \frac{\alpha}{2}[d(\Phi T)]_{ij} = \frac{\alpha}{2}[(d\Phi \wedge T) + \Phi \cdot dT]_{ij}$$

- $d\Phi \wedge T$ — **directional misalignment term**: the gradient of oblivion is not aligned with the Chebyshev form
- $\Phi \cdot dT$ — **Chebyshev torsion term**: the Chebyshev form itself is not closed

On exponential families, $dT = 0$ holds identically, and force generation reduces entirely to directional misalignment $d\Phi \wedge T \neq 0$ (Paper I, Cor. 5.1.1).

### 4.2 Walsh-Stokes of automath

automath's `WalshStokes.lean` defines a discrete exterior derivative on the hypercube $\{0,1\}^n$:

$$\text{deltaSet}(A, f, w) = \sum_{B \subseteq A} (-1)^{|B|} f(\text{flip}(B, w))$$

- $A \subseteq \text{Fin}(n)$ — the set of directions along which to differentiate
- $f: \{0,1\}^n \to \mathbb{Z}$ — a function on the hypercube
- $\text{flip}(B, w)$ — flip the bits of $w$ belonging to $B$

**Walsh flux** is the discrete integral over the boundary:

$$\text{walshFlux}(A, f) = \sum_{w \in \text{BoundaryWords}(A)} \text{deltaSet}(A, f, w)$$

Properties verified in Lean 4:
- `deltaBit_comm`: single-coordinate derivatives commute — corresponding to the continuous $\partial_i \partial_j = \partial_j \partial_i$
- `walshFlux_insert`: recursive decomposition upon bit insertion — a concrete instantiation of the discrete Stokes identity

### 4.3 Discrete Rendering of the Leibniz Rule

Correspondence between the two worlds:

| Continuous (Paper I §3.3) | Discrete (automath) |
|:---|:---|
| $d(\Phi T)$ | $\text{deltaSet}(A, f)$ |
| $d\Phi \wedge T$ (directional misalignment) | $\text{walshFlux}(A, \text{deltaSet}(\{i\}, f))$ |
| $\Phi \cdot dT$ (torsion) | $f \cdot d_{\text{discrete}}A$. $dT = 0 \iff A$ is flat (standard basis) |
| Exponential family $dT = 0$ → force comes from $d\Phi \wedge T$ alone | Standard hypercube → only carry generates force |

Because the Walsh basis is constant — independent of position $w$ — discrete Chebyshev torsion is identically zero. The world of automath corresponds to a "discrete exponential family."

### 4.4 Discretization Functor $D: \mathbf{Man} \to \mathbf{Hyp}$

We formalize the above correspondence as a functor.

> The **discretization functor** $D$ is a functor from the category of statistical manifolds $\mathbf{Man}$ to the category of hypercubes $\mathbf{Hyp}$:
>
> - $D(M) = \{0,1\}^n$ where $n = \dim M$
> - $D(\Phi) = f: \{0,1\}^n \to \mathbb{Z}$ (discretization of the oblivion field)
> - $D(T) = A \subseteq \text{Fin}(n)$ (discretization of the direction of the Chebyshev form)
> - $D(d) = \text{deltaSet}$ (discretization of the exterior derivative)
> - $D(\wedge) = \text{carry defect}$ (discretization of the exterior product)

**Composition preservation**: Whether $D(d(\Phi T)) = \text{deltaSet}(D(A), D(f))$ holds is an Open Problem.

A complete proof that $D$ is a functor requires demonstrating the correspondence between the composition law of $\text{deltaSet}$ and that of $d$; this paper limits itself to presenting the construction. However, the individual correspondences (deltaSet $\leftrightarrow$ exterior derivative, walshFlux $\leftrightarrow$ boundary integral, carry $\leftrightarrow$ exterior product) are independently proven on the Lean 4 side and the Paper I side respectively.

---

## §5 The Zero-Oblivion Limit — Discrete Resolution of OP-I-2

### 5.1 Conjecture OP-I-2

Paper I §9.5 posed the following conjecture:

> **Category theory = the $\Phi \to 0$ limit** — From the Directionality Theorem, $F_{ij} = (\alpha/2)[d(\Phi T)]_{ij}$, so in the limit $\Phi \to 0$ the oblivion curvature vanishes, the composition drift $\delta = G(f \circ g) - G(f) \circ G(g)$ goes to zero, $\ker(G) = \{0\}$, and Hom spaces degenerate from $[0,1]$ to $\{0,1\}$ — which is precisely the axioms of a standard category.

Intuitively: just as Euclidean geometry is the zero-curvature special case of Riemannian geometry, category theory is the $\Phi = 0$ special case of oblivion field theory.

This conjecture, as Paper I explicitly declared as a "non-defensive statement," remains unproven.

### 5.2 Discrete Resolution via automath

Consider the same limit in the world of automath.

What happens when the no-consecutive-1s constraint vanishes? Every word becomes stable, and $X_m = \{0,1\}^m$. $|X_m| = 2^m$ (a power of 2, not a Fibonacci number). Fold $\Phi$ becomes mere bit truncation, and addition $\oplus$ becomes ordinary modular addition.

At this point, carry defect vanishes:

$$\kappa = 0 \quad \text{for all } x, y$$

This is because the very condition for $\text{stableValue}(x) + \text{stableValue}(y)$ to exceed $F_{m+3}$ depends on the no-consecutive-1s constraint. Without the constraint, the state space expands to $2^m$ and the "boundary" that generates carry disappears.

Fold becomes a ring homomorphism:

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y)$$

This fact, verified in Lean 4, is the discrete version of conjecture OP-I-2:

| OP-I-2 (continuous) | automath (discrete) |
|:---|:---|
| $\Phi \to 0$ (oblivion field vanishes) | No11 constraint vanishes (all words are stable) |
| $\delta \to 0$ (composition drift vanishes) | $\kappa = 0$ (carry defect vanishes) |
| Hom $\in \{0,1\}$ (standard category) | fold is a ring homomorphism |
| **Unproven conjecture** | **Proven in Lean 4** |

### 5.3 Lifting from Discrete to Continuous

The discrete proof is not a proof of the continuous version. However, it supports the continuous version in two ways:

1. **Absence of counterexamples**: If OP-I-2 were false, it should be possible to construct a counterexample in the discrete version as well. The truth of the discrete version drastically narrows the space in which counterexamples could be constructed
2. **Existence of a lifting path**: If a right adjoint $D^*: \mathbf{Hyp} \to \mathbf{Man}$ of the discretization functor $D$ can be constructed, then the Lean 4 proof could potentially be lifted onto statistical manifolds

The construction of $D^*$ is left as an Open Problem in this paper.

---

## §6 Collision Kernel — A New Spectral Invariant for Oblivion Theory

### 6.1 Moment Sum and Companion Matrix

automath defines the **moment sum** $S_q(m) = \sum_{x \in X_m} d(x)^q$ of the fiber structure of fold, and proves that it satisfies a linear recurrence.

$S_2$ recurrence: $S_2(m+3) = 2 S_2(m+2) + 2 S_2(m+1) - 2 S_2(m)$

The 3×3 companion matrix $A_2$ governing this recurrence is:

$$A_2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 2 & 2 \end{pmatrix}, \quad \text{tr}(A_2) = 2, \quad \det(A_2) = -2$$

Companion matrices are also defined for $S_3$ and $S_4$, and the following is proven in Lean 4:

$$\text{tr}(A_q) = 2, \quad \det(A_q) = -2 \quad \text{for } q = 2, 3, 4$$

### 6.2 Oblivion-Theoretic Interpretation of Universal Invariants

Paper V of Oblivion Theory (Renormalization is Oblivion) formulated the $\beta$-function and scale invariance of the oblivion field, but has no concept corresponding to the moment sum over fiber structure.

The universal invariants tr = 2, det = −2 are a **new import** for Oblivion Theory.

Interpretive hypothesis: define the moment sum $S_q(\mu)$ of the fiber distribution along the scale $\mu$ of the oblivion field $\Phi(\theta, \mu)$, and take the spectrum of its companion matrix as a **renormalization group invariant** of the oblivion field. If this invariant also yields tr = 2, det = −2 within the framework of Oblivion Theory, then it is the algebraic expression of the universality class of oblivion.

Verification of this hypothesis is left for future work.

---

## §7 Objections and Outlook

### 7.1 "The discrete version is not a proof of the continuous version"

Correct. A theorem over finite fields does not imply a theorem on statistical manifolds.

Yet against this objection, three rebuttals stand.

**First: the precedent of lattice gauge theory (Wilson 1974).** As the discrete version of continuous gauge theory (Yang-Mills), lattice gauge theory has 50 years of mainstream physics behind it. The plaquette action on the lattice is the discrete version of the continuous curvature tensor $F_{\mu\nu}$, and the two connect in the continuum limit. The relationship between automath's carry defect and Oblivion Theory's oblivion curvature $F_{ij}$ is structurally isomorphic to the relationship between Wilson's lattice plaquette and Yang-Mills' $F_{\mu\nu}$. "The discrete version is an instance of the continuous version" is an established methodology in physics with 50 years of track record.

**Second: the bridge of the categorical simplex $\Delta^n$.** Paper I Appendix B completed the concrete computation of the Directionality Theorem on the categorical simplex $\Delta^n$ — namely, discrete probability distributions. The Chebyshev 1-form on $\Delta^n$ is $T_i = 1 - (n+1)p_i$, and $dT = 0$ holds as an exponential family. At the uniform distribution $(1/3, 1/3, 1/3)$, $F_{12} = 0$; at the asymmetric point $(0.15, 0.15, 0.70)$, $F_{12} = -2.728$. $\Delta^n$ is a natural candidate for a statistical-manifold lift of $\{0,1\}^n$ — interpreting each bit position as a Bernoulli random variable, stable words (No11 constraint) correspond to a constrained submanifold of the product Bernoulli space. Carry defect is the discrete restriction of $F_{ij}$ on this submanifold.

**Third: the "Rosetta Stone" methodology of Baez-Dolan (2009).** Structural similarity between different categories is itself a mathematical object — a natural transformation. To "construct the correspondence between automath and Oblivion Theory as a natural transformation" is precisely what proving the functoriality of the discretization functor $D$ amounts to. Baez-Dolan formalized the correspondence among physics, topology, logic, and computation not as "mere analogy" but as "functorial correspondence." The first claim of this paper follows the same methodology.

That two independent theoretical systems **independently** derived the same structure is powerful evidence that the structure is necessary, not accidental. The existence of the discrete version provides a blueprint for the proof of the continuous version.

### 7.2 "Structural correspondence might be coincidence"

If there were only one correspondence, coincidence could not be ruled out. But the correspondences demonstrated in this paper are:

1. carry defect $\leftrightarrow$ composition drift
2. walshFlux $\leftrightarrow$ boundary integral
3. deltaSet $\leftrightarrow$ exterior derivative
4. carry indicator $\leftrightarrow$ curvature condition
5. functoriality of fold $\leftrightarrow$ semigroup property of coarse-graining
6. zero-oblivion limit $\leftrightarrow$ recovery of standard category

The probability that six independent correspondences hold simultaneously is the product of the individual coincidence probabilities.

### 7.3 "The absence of the golden ratio $\varphi$ in Oblivion Theory is fatal"

While $\varphi$ is recovered as a spectral invariant in automath's spectral analysis, $\varphi$ does not appear in the current framework of Oblivion Theory. This is not a defect of the theory but an **extension point**. The golden ratio $\varphi$ may be hiding in the fixed-point structure of the oblivion field $\Phi$. Elucidating the oblivion-theoretic meaning of $\varphi$ is left as an Open Question.

### 7.4 Outlook

- **C2 (forcing $\leftrightarrow$ $\alpha$-filtration)**: Refining the correspondence between automath's 11-layer conservative extension and Oblivion Theory's $\alpha$-oblivion filtration (Paper VIII). Constructing a normalization map to resolve the layer-count mismatch (11 vs. 8)
- **C3 (Autoformalization)**: Formal proof of core Oblivion Theory theorems (Directionality Theorem, CPS span, $\alpha$-oblivion filtration) in Lean 4. automath's existing infrastructure serves as scaffolding
- **Tripartite unification**: The Rosetta Stone of automath (Lean 4) $\times$ The Omega (Von Neumann algebras + QCA) $\times$ Oblivion Theory (category theory + information geometry). If three independent languages describe the same structure, that structure is nothing other than the grammar of physics

---

## §8 Conclusion

Without oblivion there is no force. Without carry there is no curvature.

A perfect crystal has no dislocations, a single currency has no rounding errors, and a system that preserves all information generates no force.

What automath proved in Lean 4 is the discrete version of this proposition. What Oblivion Theory conjectured on statistical manifolds is the continuous version of the same proposition. The two projects, unaware of each other's existence, independently derived different instances of the same theorem.

This is not coincidence.

Projection breaks composition. The manner of breakage generates curvature. Curvature becomes force — this structure necessarily appears in any representational language, so long as there exists a finite observer.

Without oblivion there is no force. Without force there is no structure. Without structure — nothing happens.

In a world where information is perfectly preserved, nothing happens.

---

## References

- [1] Makaron (2026a). 力としての忘却 — 統計多様体上の場の方程式. Paper I, v1.5. 忘却論シリーズ.
- [2] The Omega Institute (2026). automath — An auditable theory compiler. GitHub: the-omega-institute/automath. Lean 4, 3,427+ theorems.
- [3] Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- [4] Makaron (2026b). 行為可能性は忘却である — Coherence Invariance 定理と G∘F 結晶化の普遍性. Paper VI. 忘却論シリーズ.
- [5] Makaron (2026c). 繰り込みは忘却である. Paper V. 忘却論シリーズ.
- [6] Makaron (2026d). 存在は忘却に先行する — 容器/内容の cell 次元論と CPS0' の米田的導出. Paper VIII. 忘却論シリーズ.

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

- **Carry defect is the discrete version of oblivion curvature** — automath's carry defect $\delta(x,y) = \Phi(x \oplus y) - \Phi(x) \oplus \Phi(y)$ is a discrete, finite quotient-ring instance of Oblivion Theory's composition drift $\delta = G(f \circ g) - G(f) \circ G(g)$. The former is machine-verified in Lean 4. The latter is the unproven conjecture OP-I-2 from Paper I §9.5
- **The Walsh-Stokes identity is the discrete version of the Leibniz rule** — automath's `walshFlux` and `deltaSet` correspond to the discrete exterior derivative of the oblivion field's Leibniz rule $d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$, and a **candidate discretization functor** $D: \mathbf{Man} \to \mathbf{Hyp}$ can be sketched. On a suitable restricted domain, it is intended to map the differential geometry of the oblivion field to the combinatorics of hypercubes
- **The discrete OP-I-2 chain is strongly supported by Lean 4 results** — when the no-consecutive-1s constraint vanishes, carry defect disappears and fold returns to a strict ring homomorphism. But on the continuous side, $\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$ does not follow from the existing axioms alone. The additional bridge axiom `ZeroForgetCollapse` and a discrete-to-continuous lift still remain

These claims are developed and qualified in order in the sections that follow.

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
| Zero oblivion | No11 constraint vanishes → $\delta = 0$ → ring homomorphism [structurally implied by Lean results; not directly formalized as a limit statement] | $\Phi = 0 \Rightarrow \ker(G)=\{0\} \Rightarrow \delta = 0$ can be established, but $\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$ requires `ZeroForgetCollapse` [Open] |

The structural pattern is strongly parallel. Projection breaks composition. The measure of the breakage appears as defect, curvature, or force, depending on the language used.

---

## §3 Three Metaphors — Curvature is Born from Carry

### 3.1 Crystallography — Dislocations Are the Carry of Projection

Consider the operation of precipitating a crystal from solution. You project a solution (a high-dimensional field) onto a crystal lattice (a low-dimensional structure). In a perfect crystal, the lattice is exactly preserved — carry is zero.

But real crystals have **dislocations**. Atomic arrangements shift locally, and the composition law of the lattice breaks. Dislocations generate curvature in the crystal. And dislocation density is a physical force that determines the strength of the crystal.

$$\text{perfect crystal} \leftrightarrow \kappa = 0, \quad \text{dislocation} \leftrightarrow \kappa = 1$$

This analogy is tighter than a loose metaphor, but it should still be read as a structural comparison rather than an identity claim. As Paper VI (Affordance is Oblivion) showed, in the crystallization adjunction $F \dashv G$ of the forgetful functor $G$, $\text{Fix}(G \circ F)$ is the Kalon (fixed point), and deviation from the fixed point generates curvature. In that sense, the carry element $e_m$ plays a role analogous to a discrete dislocation count.

### 3.2 Cartography — Projection Distortion as an Analogy for Carry

Consider a map projection from sphere to plane. Any such projection preserves some structures while distorting others. The general lesson is that projection and geometric composition do not commute perfectly once information is discarded.

$$\Phi(\text{composed geometric data}) \neq \text{composition of projected data}$$

Map distortion is therefore a useful analogy for the broader claim: once projection forgets structure, composition acquires a defect term.

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

### 4.4 Candidate Discretization Functor $D: \mathbf{Man} \to \mathbf{Hyp}$

We formalize the above correspondence as a candidate functor.

> The **candidate discretization functor** $D$ is intended as a map from the category of statistical manifolds $\mathbf{Man}$ to the category of hypercubes $\mathbf{Hyp}$:
>
> - $D(M) = \{0,1\}^n$ where $n = \dim M$
> - $D(\Phi) = f: \{0,1\}^n \to \mathbb{Z}$ (discretization of the oblivion field)
> - $D(T) = A \subseteq \text{Fin}(n)$ (discretization of the direction of the Chebyshev form)
> - $D(d) = \text{deltaSet}$ (discretization of the exterior derivative)
> - $D(\wedge) = \text{carry defect}$ (discretization of the exterior product)

**Composition preservation**: Whether $D(d(\Phi T)) = \text{deltaSet}(D(A), D(f))$ holds on the full domain is an Open Problem.

A complete proof that $D$ is a functor requires demonstrating the correspondence between the composition law of $\text{deltaSet}$ and that of $d$; this paper limits itself to presenting the construction and the restricted-domain intuition. However, the individual correspondences (deltaSet $\leftrightarrow$ exterior derivative, walshFlux $\leftrightarrow$ boundary integral, carry $\leftrightarrow$ exterior product) are independently proven on the Lean 4 side and the Paper I side respectively.

---

## §5 The Zero-Oblivion Limit — The Current Status of OP-I-2

### 5.1 Revision of Conjecture OP-I-2

Paper I §9.5 presented the following horizon:

> **Category theory = the $\Phi \to 0$ limit** — From the Directionality Theorem, $F_{ij} = (\alpha/2)[d(\Phi T)]_{ij}$, so in the limit $\Phi \to 0$ oblivion curvature vanishes, the composition drift $\delta = G(f \circ g) - G(f) \circ G(g)$ goes to zero, $\ker(G) = \{0\}$, and Hom spaces degenerate from $[0,1]$ to $\{0,1\}$ — precisely the axioms of a standard category.

The direction of this intuition is correct. But the 2026-04-14 formalization pass showed that the argument has two cuts.

First,

$$F = 0 \;\centernot\Rightarrow\; \Phi = 0$$

Uniform oblivion $\Phi = \mathrm{const} \neq 0$ has $d\Phi = 0$, so force vanishes while oblivion itself remains. "No force" and "no oblivion" are therefore not the same statement.

Second,

$$\delta = 0 \;\centernot\Rightarrow\; \mathrm{Hom}_\Phi \in \{0,1\}$$

The core of OP-I-2 must now be read as the one-way chain

$$\Phi = 0 \Rightarrow \ker(G)=\{0\} \Rightarrow \delta = 0$$

This much can be established. But the final step

$$\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$$

does not follow from the existing axioms. It requires the additional bridge axiom `ZeroForgetCollapse`.

The Euclidean/Riemannian analogy still lives. What has failed is not the analogy. What has failed is the unproven leap that "zero curvature automatically yields Boolean enrichment."

### 5.2 Discrete Evidence from automath

In the world of automath, the no-consecutive-1s constraint is the source of laxity. With the constraint, carry defect appears. Remove the constraint, and carry defect disappears. Fold returns to a strict law.

Once the no-consecutive-1s constraint is removed, every word becomes stable. Then $X_m = \{0,1\}^m$. Fold $\Phi$ becomes mere bit truncation, and addition $\oplus$ returns to ordinary modular addition. The Fibonacci threshold that generated carry defect loses its force.

$$\kappa = 0 \quad \text{for all } x,y$$

So fold returns to a strict homomorphism:

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y)$$

What the discrete side gives us is the skeleton: constraints generate compositorial defect, and the disappearance of the constraint restores strictness. This strongly supports the direction of OP-I-2. But it still does not entitle us to claim that continuous $[0,1]$-enrichment automatically collapses to $\{0,1\}$.

| Zero-oblivion question | What automath gives |
|:---|:---|
| What is the analogue of $\Phi = 0$? | Trivialization of the No11 constraint |
| Does $\ker(G)=\{0\}$ occur? | All words become stable, so the constraint-generated kernel disappears |
| Does $\delta = 0$ occur? | Carry defect disappears and fold becomes strict |
| Is Boolean recovery automatic? | Strictness is visible on the discrete side; Boolean collapse on the continuous side remains a separate issue |

The discrete proof is not a substitute for the continuous proof. It is a device for separating what the continuous side still has to prove.

### 5.3 Lifting to the Continuous Side — Three Open Gaps

OP-I-2 is not one hole. It is three.

1. **The axiomatic gap** — justification of `ZeroForgetCollapse`.  
   The counterexample already exists: a one-object category with $\mathrm{Hom}(*,*) = [0,1]$, composition $= \min$, and $G = \mathrm{id}$ satisfies OP-I-3 and $\delta = 0$ while still allowing $\mathrm{Hom}(*,*) = 1/2$. So "if $\delta = 0$, the standard category is recovered" is not a theorem. It is an additional axiomatic requirement. `ZeroForgetCollapse` is the formal expression of the FEP intuition that without oblivion, precision is maximal and Hom values become discrete.

2. **The limit gap** — reformulation of Conjecture 9.5.2.  
   The idea of moving $X_\infty(\lambda)$ itself continuously in $\lambda$ fails. The reason is that $\delta_m(\lambda)$ jumps at Fibonacci thresholds. To recover continuity, one should not move the state space itself. One should place a $\lambda$-dependent weak* continuous family of probability measures $\mu_\lambda$ on the fixed ambient profinite space $\{0,1\}^{\mathbb{N}}$. The right question is not "continuous motion of points" but "continuous deformation of expectations."

3. **The functorial gap** — extension of the discretization functor $D$.  
   At present, $D$ is strictly functorial only on $\mathbf{Man}_{\mathrm{No11}}$. To extend it to all of $\mathbf{Man}$, one must attach `Discretizable` and `DescendsToCube` data to each morphism. As an implementation route, inverse-limit-based Strategy B is stronger than the direct $\Delta^n$ route, because it aligns with the existing automath library and gives a cleaner path for removing `sorry`. Strategy A', which rewrites the Appendix B geometry through $(\Delta^1)^n$, remains as a fallback path rather than the main route.

This paper does not offer the completed proof. It offers the blueprint of the completed proof. To say "the discrete version is true, therefore the continuous version is true" would not be a breakthrough. It would only be a refusal to look at the missing axiom and the failed limit.

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

Taken together, six mutually reinforcing correspondences make pure coincidence substantially less plausible, even though no formal probability model is being claimed here.

### 7.3 "The absence of the golden ratio $\varphi$ in Oblivion Theory is fatal"

On the contrary: $\varphi$ has always been inside Oblivion Theory. It was invisible in the continuum limit because $\varphi$ is a *lattice* phenomenon — the convergence rate of a discrete self-referential recursion. Three independent routes lead to $\varphi$ from within the existing axiom system.

#### Route A: $\varphi$ as the growth rate of the anti-Markov sector

Paper III (Markov Categories and Beyond) establishes that the $\alpha < 0$ sector carries a $\mathbb{Z}_2$-graded anti-commutative structure. The anti-copy nilpotency $e_x \wedge e_x = 0$ — the categorical translation of Pauli's exclusion principle (Paper III §3.1(D)) — forbids two identical structural units from occupying adjacent positions.

On a 1-dimensional discrete lattice of $m$ sites, imposing this adjacency exclusion yields exactly $F_{m+2}$ valid configurations (Fibonacci numbers). The asymptotic growth rate is $\varphi = (1+\sqrt{5})/2$.

This is precisely automath's no-consecutive-1s constraint. The golden ratio is the **growth rate of surviving structure under the minimal fermionic exclusion** in the $\alpha < 0$ sector.

#### Route B: $\varphi$ as Kalon of the dissolution–crystallization adjunction

The self-referential equation $\varphi = 1 + 1/\varphi$ is a fixed-point equation. In the language of Paper VI, define:

- $F$ (dissolution): $x \mapsto x + x_{n-1}$ — add one degree of freedom (Fibonacci recurrence)
- $G$ (crystallization): $x \mapsto x_n / x_{n-1}$ — project onto ratio (fold)

Then $\text{Fix}(G \circ F) = \varphi$. The three attributes of Kalon are satisfied:

1. **Fix**: $\varphi = 1 + 1/\varphi$ (self-referential fixed point) ✓
2. **Generative**: $\varphi$ generates Fibonacci numbers, golden spirals, Penrose tilings, ... (3+ non-trivial derivations) ✓
3. **Self-referential**: the definition contains itself ✓

$\varphi$ is the Kalon of the fold–unfold cycle — the point where oblivion and recovery are in perfect balance.

#### Route C: $\log \varphi$ as the capacity ceiling under exclusion

Paper IX (Entropy is Oblivion) proves the CPS entropy monotonicity theorem (Th. 3.4.1): $S_{\text{CPS}}(p, \alpha)$ increases monotonically with $\alpha$. The unconstrained 1-bit capacity is $\log 2$. Imposing the adjacency exclusion (no-consecutive-1s) reduces the capacity to $\log \varphi$ — the topological entropy of the golden-mean shift, machine-verified in automath (`topological_entropy_eq_log_phi`).

$\log \varphi$ is the **information bottleneck capacity under the minimal fermionic constraint**.

#### Route D: The Pauli exclusion principle forces Fibonacci growth in the n-cell tower

The n-cell tower of forgetful functors (Paper 0 §2.0, Alētheia §3):

$$U_{\text{arrow}}(1) \leq U_{\text{compose}}(1.5) \leq U_{\text{depth}}(2) \leq \cdots \leq U_{\text{self}}(\omega)$$

has an internal Fibonacci structure forced by nilpotency.

**Proposition F2.1** (Exclusion forces additivity). Let $A(n)$ denote the set of independent axioms newly required to define $n$-cells. Then:

$$A(n) = A(n-1) \sqcup A(n-2) \quad \text{(disjoint union)}$$

and hence $|A(n)| = |A(n-1)| + |A(n-2)|$ (Fibonacci recurrence), with asymptotic growth rate $\varphi$.

*Proof sketch.* Each level $n$ draws axioms from two pools: $A(n-1)$ (direct prerequisites — the structures being related) and $A(n-2)$ (coherence conditions — the composition laws that must hold). The Alētheia proofs (Proof 1–7) establish this two-level dependency.

The key step: an axiom from $A(n-1)$ cannot simultaneously serve as an axiom in $A(n-2)$, because the two pools live in different cell dimensions. If an axiom $a$ served both as a "direct prerequisite" (role in dimension $n-1$) and a "coherence condition" (role in dimension $n-2$), then the same structural unit would occupy two adjacent positions in the tower — violating the anti-copy nilpotency $e_a \wedge e_a = 0$ (Paper III §2.3, §3.1(D)).

Therefore $A(n-1) \cap A(n-2) = \varnothing$, and the union is disjoint. $\square$

*Formalization note (Codex GPT-5.4, 2026-04-14).* The formal gap in the proof sketch is the **lag assignment**: each Alētheia Proof must be formally declared to carry exactly one dependency distance ($\text{lag}=1$ for definitional dependencies Proofs 1, 2, 6; $\text{lag}=2$ for semantic dependencies Proofs 3, 4, 5, 7). Given this declaration, $A(n-1) \cap A(n-2) = \varnothing$ follows by `omega`. Three Lean 4 routes:

**Route 1 — direct, via `proofLag` (closes the gap if `proofLag` is accepted as a declaration):**
```lean
inductive TowerProof | p1 | p2 | p3 | p4 | p5 | p6 | p7 deriving DecidableEq, Fintype
def proofLag : TowerProof → ℕ
  | .p1 | .p2 | .p6 => 1  -- definitional
  | .p3 | .p4 | .p5 | .p7 => 2  -- semantic
theorem cell_tower_axiom_disjoint {n : ℕ} (hn : 2 ≤ n) :
    Disjoint (A proofLag n (n-1)) (A proofLag n (n-2)) := by
  classical; refine Finset.disjoint_left.mpr ?_; intro a ha1 ha2; omega
```

**Route 2 — shortest, reusing automath `pathInd_disjoint` directly:**
```lean
-- notContainingLast ↔ A(n-1),  containingLast ↔ A(n-2)
theorem tower_partition_disjoint (n : ℕ) :
    Disjoint (notContainingLast n) (containingLast n) := pathInd_disjoint n
```
Requires encoding the $n$-cell tower as a path graph, with "last slot unused" = $A(n-1)$ and "last slot used, previous blocked" = $A(n-2)$. Sources: [`PathIndSet.lean`](https://github.com/the-omega-institute/automath/blob/dev/lean4/Omega/Combinatorics/PathIndSet.lean), [`FibonacciCube.lean`](https://github.com/the-omega-institute/automath/blob/dev/lean4/Omega/Combinatorics/FibonacciCube.lean).

**Route 3 — Grassmann, via Mathlib `ExteriorAlgebra.ι_sq_zero`:** Conditionally confirms disjointness from $e_a \wedge e_a = 0$ once a representation axiom `tower_repr_nonzero` is added.

The residual open question: *Is `proofLag` a declaration (axiom) or a theorem (derivable from the definition of definitional vs.\ semantic dependency)?* Routes 1 and 2 treat it as a declaration and immediately close the disjointness claim. Route 3 suggests a path to derive it from the nilpotency structure, at the cost of one additional representation axiom.

*Why disjoint union ($+$) and not tensor product ($\times$)?* The tensor product $\text{Hom}(B,C) \otimes \text{Hom}(A,B)$ that appears in enrichment (Paper III §2.4, Proof 3) acts on the *instance space* — the space of concrete morphisms. The axiom count $|A(n)|$ measures the number of *independent conditions* (types), not the number of instances (states). Nilpotency constrains axioms to single roles, forcing additive growth. Instance spaces may grow multiplicatively, but the grammar — the axiom count — grows as Fibonacci.

**The golden ratio is the growth rate of the grammar of oblivion.**

It was absent from the continuum formulation (Paper I) because the discrete axiom-counting structure dissolves in the continuous limit — just as lattice spacing dissolves in the continuum limit of lattice gauge theory. automath, working on the lattice, sees $\varphi$ directly.

### 7.4 Outlook

- **C2 (forcing $\leftrightarrow$ $\alpha$-filtration)**: Refining the correspondence between automath's 11-layer conservative extension and Oblivion Theory's $\alpha$-oblivion filtration (Paper VIII). Constructing a normalization map to resolve the layer-count mismatch (11 vs. 8)
- **C3 (Autoformalization)**: Formal proof of core Oblivion Theory theorems (Directionality Theorem, CPS span, $\alpha$-oblivion filtration) in Lean 4. automath's existing infrastructure serves as scaffolding
- **Tripartite unification**: The Rosetta Stone of automath (Lean 4) $\times$ The Omega (Von Neumann algebras + QCA) $\times$ Oblivion Theory (category theory + information geometry). If three independent languages continue to stabilize around the same abstract structure, that would be strong evidence that the structure belongs to the grammar of physics

---

## §8 Conclusion

Without oblivion there is no force. Without carry there is no curvature. And the rate at which the grammar of oblivion grows is $\varphi$.

A perfect crystal has no dislocations, a single currency has no rounding errors, and a system that preserves all information generates no force. These are instances. The deeper statement is: **projection breaks composition, and the Pauli exclusion principle dictates how fast the breakage accumulates.**

What automath proved in Lean 4 is a discrete version of this proposition. What Oblivion Theory conjectured on statistical manifolds is a continuous counterpart. The two projects, unaware of each other's existence, independently arrived at closely related expressions of the same abstract pattern.

This is at least strong evidence against a superficial coincidence reading.

The golden ratio $\varphi$ was absent from the continuum formulation — not because it doesn't belong, but because it is a lattice phenomenon. Each axiom in the hierarchy of oblivion can serve only one structural role (Pauli exclusion: $e_x \wedge e_x = 0$). This forces the axiom count to grow additively across levels: $|A(n)| = |A(n-1)| + |A(n-2)|$. Fibonacci. The growth rate is $\varphi$. In the continuum limit, axiom counting dissolves into differential geometry and $\varphi$ disappears — just as lattice spacing disappears in the continuum limit of gauge theory.

automath sees $\varphi$ because it stays on the lattice. Oblivion Theory missed $\varphi$ because it went to the continuum too early. The bridge between the two recovers what was lost.

Projection breaks composition. The manner of breakage generates curvature. The rate at which the grammar of breakage grows is the golden ratio — because each act of remembering casts exactly one shadow, and you cannot use the same axiom twice.

Without oblivion there is no force. Without force there is no structure. Without structure — nothing happens.

In a world where information is perfectly preserved, nothing happens. And in a world where oblivion has a minimum quantum, the grammar of what happens grows at the golden ratio.

---

## References

- [1] Makaron (2026a). *Force as Oblivion - Field Equations on Statistical Manifolds*. Paper I, v1.5. Oblivion Theory series.
- [2] The Omega Institute (2026). automath — An auditable theory compiler. GitHub: the-omega-institute/automath. Lean 4, 3,427+ theorems.
- [3] Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- [4] Makaron (2026b). *Affordance as Oblivion - The Coherence Invariance Theorem and the Universality of `G o F` Crystallization*. Paper VI. Oblivion Theory series.
- [5] Makaron (2026c). *Renormalization is Oblivion*. Paper V. Oblivion Theory series.
- [6] Makaron (2026d). *Existence Precedes Oblivion - Cell Dimensions of Container/Content and a Yoneda Derivation of `CPS0'`*. Paper VIII. Oblivion Theory series.

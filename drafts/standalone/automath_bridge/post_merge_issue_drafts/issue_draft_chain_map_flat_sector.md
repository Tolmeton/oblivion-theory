# Issue Draft — three-layer bridge problem

**Target**: https://github.com/the-omega-institute/automath/issues/new
**Suggested title**: `Three layers of the bridge problem: strict projection, flat-sector chain map, and global coherence`

---

## Issue body

Following the closure of #25 and the merge of PR #28, I want to isolate the second research question raised in the final comment there:

> is there a candidate chain map from the Amari-Chentsov complex to the Walsh-Stokes complex, even at the cochain level?

I think the right answer is three-layered rather than simply yes/no.

## Proposed reformulation

From my side the bridge problem now looks like this:

1. **strict projection layer**  
   already certified on the discrete side
2. **flat/cubical chain-map layer**  
   there is a concrete cochain-level candidate
3. **global coherence layer**  
   this is where the actual open problem still lives

So I would no longer phrase the open problem as "is there any chain map at all?".

I would phrase it as:

> what is the correct extension of the flat strict square once the global defect/coherence data become active?

## Layer A: strict projection

This part is already certified by PR #28 / the underlying Lean facts:

- projection functoriality is strict
- the defect already satisfies the xor-cocycle composition law

So the projection part is no longer the bottleneck.

## Layer B: flat/cubical chain-map candidate

The candidate becomes honest if one first restricts the continuous side to:

- product Bernoulli charts
  \[
  M_I=(\Delta^1)^I
  \]
- multilinear observables, equivalently the linear span of cylinder observables

This is the same sector in which the projection part is already strict and in which `deltaSet` matches mixed partial cell integrals.

## Cochain-level candidate

Let `A \subseteq I` be a coordinate face and let `w` be the boundary word fixing the complementary coordinates.

For a differential form `\omega` on `M_I`, define

\[
\mathcal D_A(\omega)(w)
:=
(-1)^{|A|}
\int_{[0,1]^A}\iota_{A,w}^* \omega,
\]

where `\iota_{A,w}` is the standard embedding that varies the `A`-coordinates and fixes the others by `w`.

If `\omega=df` with `f` multilinear, then

\[
\mathcal D_A(df)(w)
=
\delta_A(f|_{\{0,1\}^I})(w).
\]

So on this restricted sector one gets a genuinely strict square:

- `d` is sent to `deltaSet`
- cubical boundary integration is sent to `walshFlux`

In other words, the following part is already available:

\[
d \mapsto \deltaSet,
\qquad
\int \mapsto walshFlux,
\]

provided we stay inside the product-Bernoulli / multilinear / cubical chart sector.

## Relation to PR #28

PR #28 isolates the already-certified discrete side:

- strict projection functoriality
- xor-cocycle coherence for the defect

What this candidate adds is a continuous-side flat-sector model in which the cochain map is no longer only suggestive.

## Layer C: what still remains open

The real obstruction is the extension beyond that flat sector.

The unresolved part is not whether a strict map exists on the flat sector, but how to extend it when the continuous term

\[
\Phi \cdot dT
\]

becomes active and the discrete side simultaneously acquires the carry-defect cocycle.

That is why my current reading is that the final bridge is probably not an ordinary functor. It looks more like a defect-bearing bridge, or perhaps a lax/pseudofunctorial object, whose coherence failure is the real invariant to identify.

## Why I think this is the right slicing

This slicing seems better than a flat yes/no question because it separates:

- what is already strict
- what can already be modeled strictly on the flat sector
- what still genuinely requires new mathematics

So the core open problem is not "chain map or no chain map?" but rather:

> how should the global coherence defect be packaged once the flat strict square is known?

## Proposed next target

If this matches your reading, the next formal target would be:

1. a statement of the flat-sector cochain map between explicitly named subcomplexes, and
2. a separate issue for the global coherence / obstruction class problem.

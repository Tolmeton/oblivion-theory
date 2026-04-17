We apologize for the 404s on the bridge files referenced in the issue. They had been prepared locally but were not yet pushed.

The bridge PR material is now ready:

- `lean4/Omega/Frontier/OblivionBridge.lean`
- `theory/bridges/oblivion-theory/README.md`

The Lean wrapper exposes the strict projection part of the bridge together with the defect-coherence law, backed by the existing `restrict_functorial` and `globalDefect_compose` results.

The README follows the precision-label convention used in this issue. It does **not** claim a canonical full functor `Man -> Hyp`.

The smallest honest claim at this point is:

- strict projection functoriality is now certified
- the remaining open problem is whether the continuous-side composition drift is equal to the discrete carry defect
- a second open design question is what 2-categorical language best organizes the bridge (for example lax monoidal functor, pseudofunctor, or another defect-bearing coherence formalism)

If this direction looks right, we will open the PR against `dev` unless you would prefer another base branch.

import Omega.Folding.Defect

namespace Omega.Frontier

/-- Projection-only discretization shadow used by the oblivion bridge.
    This is the strict 1-functor part of the candidate bridge. -/
def discretizeProjMap (h : m ≤ n) : X n → X m :=
  X.restrictLE h

@[simp] theorem discretizeProjMap_apply (h : m ≤ n) (x : X n) :
    discretizeProjMap h x = X.restrictLE h x :=
  rfl

@[simp] theorem discretizeProj_id (x : X n) :
    discretizeProjMap (Nat.le_refl n) x = x := by
  simp [discretizeProjMap]

/-- Projection-only discretization is strictly functorial on coordinate restriction maps.
    This is the certified strict part of the oblivion bridge.
    thm:oblivion-bridge-projection-functorial -/
theorem discretizeProj_comp (h₁ : m ≤ n) (h₂ : n ≤ k) (x : X k) :
    discretizeProjMap h₁ (discretizeProjMap h₂ x) =
      discretizeProjMap (Nat.le_trans h₁ h₂) x := by
  simpa [discretizeProjMap] using X.restrict_functorial h₁ h₂ x

/-- Function-level version of the strict projection functoriality. -/
theorem discretize_proj_functorial (h₁ : m ≤ n) (h₂ : n ≤ k) :
    discretizeProjMap h₁ ∘ discretizeProjMap h₂ =
      discretizeProjMap (Nat.le_trans h₁ h₂) := by
  funext x
  exact discretizeProj_comp h₁ h₂ x

/-- The bridge is not strictly monoidal at finite resolution; its coherence datum is the
    carry defect cocycle already formalized in `globalDefect_compose`.
    thm:oblivion-bridge-defect-two-cell -/
theorem discretizeProj_defect_two_cell (hmk : m ≤ k) (hkn : k ≤ n) (ω : Word n) :
    globalDefect (Nat.le_trans hmk hkn) ω =
      xorWord
        (globalDefect hmk (restrictWord hkn ω))
        (restrictWord hmk (globalDefect hkn ω)) :=
  globalDefect_compose hmk hkn ω

/-- Adjacent-scale form of the defect two-cell, useful for bridge diagrams. -/
theorem discretizeProj_poincare_band (hmn : m + 1 ≤ n) (ω : Word n) :
    globalDefect (Nat.le_trans (Nat.le_succ m) hmn) ω =
      xorWord
        (globalDefect (Nat.le_succ m) (restrictWord hmn ω))
        (restrictWord (Nat.le_succ m) (globalDefect hmn ω)) :=
  globalDefect_poincare_band hmn ω

/-- Compact package for the current certified bridge surface:
    strict projection functoriality plus the defect-bearing coherence law.
    thm:oblivion-bridge-projection-package -/
theorem paper_oblivion_bridge_projection_package
    (h₁ : m₁ ≤ m₂) (h₂ : m₂ ≤ m₃) (x : X m₃) (ω : Word m₃) :
    discretizeProjMap h₁ (discretizeProjMap h₂ x) =
        discretizeProjMap (Nat.le_trans h₁ h₂) x ∧
      globalDefect (Nat.le_trans h₁ h₂) ω =
        xorWord
          (globalDefect h₁ (restrictWord h₂ ω))
          (restrictWord h₁ (globalDefect h₂ ω)) := by
  exact ⟨discretizeProj_comp h₁ h₂ x, discretizeProj_defect_two_cell h₁ h₂ ω⟩

universe u v w

/-- Minimal ambient model for the continuous side of the oblivion bridge.
    `no11Compatible` isolates the certified subcategory `Man_No11`; the general `StatMan`
    still needs explicit descent data. -/
structure StatMan where
  Carrier : Type u
  no11Compatible : Prop := False

/-- Morphisms on the continuous side, kept intentionally minimal for the bridge interface. -/
structure StatMor (M N : StatMan.{u}) where
  toFun : M.Carrier → N.Carrier

namespace StatMor

/-- Composition of continuous-side morphisms. -/
def comp {M N P : StatMan.{u}} (g : StatMor N P) (f : StatMor M N) : StatMor M P where
  toFun := g.toFun ∘ f.toFun

@[simp] theorem comp_apply {M N P : StatMan.{u}} (g : StatMor N P) (f : StatMor M N)
    (x : M.Carrier) :
    (comp g f).toFun x = g.toFun (f.toFun x) :=
  rfl

end StatMor

/-- The certified strict subcategory on which the current discretization functor is already
    functorial without extra coherence data. -/
abbrev Man_No11 := { M : StatMan.{u} // M.no11Compatible }

/-- Forget fields are represented only up to the zero-field test needed by the bridge axiom. -/
abbrev ForgetField (M : Type u) := M → ℝ

/-- Minimal enriched category surface used by the ZeroForgetCollapse bridge axiom. -/
class OblivionEnrichment (C : Type v) where
  Obj : Type w
  hom : Obj → Obj → ℝ

abbrev Obj (C : Type v) [e : OblivionEnrichment C] : Type w :=
  e.Obj

abbrev hom_Φ {C : Type v} [e : OblivionEnrichment C] :
    Obj C → Obj C → ℝ :=
  e.hom

/-- Bridge axiom: at zero oblivion, the continuous enrichment collapses to Boolean hom-values.
    This is independent of the existing OP-I-3 interface. -/
class ZeroForgetCollapse (M : Type u) (C : Type v) [OblivionEnrichment C] where
  hom_zero_or_one :
    ∀ (Φ : ForgetField M), Φ = 0 →
      ∀ A B : Obj C, hom_Φ A B = 0 ∨ hom_Φ A B = 1

/-- Skeleton theorem for the `(d) → (e)` step of OP-I-2.
    The theorem is available only after assuming `ZeroForgetCollapse`. -/
theorem zero_forget_recovers_boolean_enrichment
    {M : Type u} {C : Type v} [OblivionEnrichment C]
    [ZeroForgetCollapse M C]
    (Φ : ForgetField M) (hΦ : Φ = 0)
    (A B : Obj C) :
    hom_Φ A B = 0 ∨ hom_Φ A B = 1 :=
  ZeroForgetCollapse.hom_zero_or_one Φ hΦ A B

/-- Objects in the full category `Man` become discretizable only after choosing an explicit
    coding into the automath hypercube side. -/
class Discretizable (M : StatMan.{u}) where
  dim : ℕ
  code : M.Carrier → X dim

/-- A morphism descends to the hypercube side only after an explicit cube map is provided.
    This is the extra data needed outside `Man_No11`. -/
class DescendsToCube {M N : StatMan.{u}}
    [dM : Discretizable M] [dN : Discretizable N] (f : StatMor M N) where
  D_map : X dM.dim → X dN.dim
  commutes : ∀ x, dN.code (f.toFun x) = D_map (dM.code x)

/-- Composition law for explicit descent data. This is the compile-ready skeleton for
    Strategy B on the Lean side. -/
def descendsToCubeComp {M N P : StatMan.{u}}
    [dM : Discretizable M] [dN : Discretizable N] [dP : Discretizable P]
    {f : StatMor M N} {g : StatMor N P}
    [hf : DescendsToCube f] [hg : DescendsToCube g] :
    DescendsToCube (StatMor.comp g f) where
  D_map := hg.D_map ∘ hf.D_map
  commutes := by
    intro x
    rw [StatMor.comp_apply, hg.commutes, hf.commutes]

@[simp] theorem descendsToCubeComp_D_map {M N P : StatMan.{u}}
    [dM : Discretizable M] [dN : Discretizable N] [dP : Discretizable P]
    {f : StatMor M N} {g : StatMor N P}
    [hf : DescendsToCube f] [hg : DescendsToCube g] :
    (descendsToCubeComp (f := f) (g := g)).D_map = hg.D_map ∘ hf.D_map :=
  rfl

end Omega.Frontier

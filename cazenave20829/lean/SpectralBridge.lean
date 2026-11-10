import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Tactic.Ring

/-! The one- and two-dimensional Rayleigh bounds needed by the counterexample. -/

open scoped RealInnerProductSpace BigOperators Matrix
open Matrix WithLp

namespace Cazenave20829

private theorem euclidean_inner {n : ℕ} (x y : EuclideanSpace ℝ (Fin n)) :
    ⟪x, y⟫ = ∑ i, y i * x i := by
  rw [EuclideanSpace.inner_eq_star_dotProduct, dotProduct]
  simp [mul_comm]

section Symmetric

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] {T : E →ₗ[ℝ] E} {n : ℕ}

private theorem first_le (hT : T.IsSymmetric) (hn : Module.finrank ℝ E = n + 2) (t : ℝ)
    (hRay : ∀ x, ⟪x, T x⟫ ≤ t * ⟪x, x⟫) :
    hT.eigenvalues hn 0 ≤ t := by
  let e := hT.eigenvectorBasis hn 0
  have hunit : ⟪e, e⟫ = 1 := (hT.eigenvectorBasis hn).inner_eq_one 0
  have he : T e = (hT.eigenvalues hn 0) • e := hT.apply_eigenvectorBasis hn 0
  simpa only [he, real_inner_smul_right, hunit, mul_one] using hRay e

private theorem second_gt (hT : T.IsSymmetric) (hn : Module.finrank ℝ E = n + 2)
    (q : ℝ) (u v : E)
    (hRay : ∀ a b : ℝ, a ≠ 0 ∨ b ≠ 0 →
      q * ⟪a • u + b • v, a • u + b • v⟫ <
        ⟪a • u + b • v, T (a • u + b • v)⟫) :
    q < hT.eigenvalues hn 1 := by
  let B := hT.eigenvectorBasis hn
  let c : ℝ := B.repr u 0
  let d : ℝ := B.repr v 0
  have hex : ∃ a b : ℝ, (a ≠ 0 ∨ b ≠ 0) ∧ B.repr (a • u + b • v) 0 = 0 := by
    by_cases hc : c = 0
    · exact ⟨1, 0, Or.inl one_ne_zero, by simpa using hc⟩
    · refine ⟨d, -c, Or.inr (neg_ne_zero.mpr hc), ?_⟩
      rw [B.repr_apply_apply, inner_add_right, real_inner_smul_right, real_inner_smul_right,
        ← B.repr_apply_apply, ← B.repr_apply_apply]
      change d * c + (-c) * d = 0
      ring
  obtain ⟨a, b, hab, hx0⟩ := hex
  let x := a • u + b • v
  change B.repr x 0 = 0 at hx0
  have hq : q * ⟪x, x⟫ < ⟪x, T x⟫ := hRay a b hab
  have hup : ⟪x, T x⟫ ≤ hT.eigenvalues hn 1 * ⟪x, x⟫ := by
    rw [← B.repr.inner_map_map x (T x), ← B.repr.inner_map_map x x]
    simp only [euclidean_inner, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    have hi : B.repr (T x) i = hT.eigenvalues hn i * B.repr x i :=
      hT.eigenvectorBasis_apply_self_apply hn x i
    rw [hi]
    by_cases hzero : i = 0
    · subst i
      simp [hx0]
    · calc
        (hT.eigenvalues hn i * B.repr x i) * B.repr x i =
            hT.eigenvalues hn i * (B.repr x i) ^ 2 := by ring
        _ ≤ hT.eigenvalues hn 1 * (B.repr x i) ^ 2 :=
          mul_le_mul_of_nonneg_right
            (hT.eigenvalues_antitone hn (Fin.one_le_of_ne_zero hzero)) (sq_nonneg _)
        _ = hT.eigenvalues hn 1 * (B.repr x i * B.repr x i) := by ring
  exact lt_of_not_ge fun hle ↦
    (not_lt_of_ge (mul_le_mul_of_nonneg_right hle real_inner_self_nonneg)) (hq.trans_le hup)

end Symmetric

section Matrices

variable {n : ℕ} {A : Matrix (Fin (n + 2)) (Fin (n + 2)) ℝ}

/-- Eigenvalues in nonincreasing order, including multiplicities. -/
noncomputable def orderedEigenvalues (hA : A.IsHermitian) : Fin (n + 2) → ℝ :=
  (Matrix.isHermitian_iff_isSymmetric.mp hA).eigenvalues finrank_euclideanSpace_fin

private theorem euclidean_quad (x : EuclideanSpace ℝ (Fin (n + 2))) :
    ⟪x, A.toEuclideanLin x⟫ = WithLp.ofLp x ⬝ᵥ (A *ᵥ WithLp.ofLp x) := by
  rw [EuclideanSpace.inner_eq_star_dotProduct]
  change (A *ᵥ ofLp x) ⬝ᵥ star (ofLp x) = _
  rw [star_trivial, dotProduct_comm]

private theorem euclidean_norm_sq (x : EuclideanSpace ℝ (Fin (n + 2))) :
    ⟪x, x⟫ = WithLp.ofLp x ⬝ᵥ WithLp.ofLp x := by
  rw [EuclideanSpace.inner_eq_star_dotProduct, star_trivial]

/-- A universal quadratic-form upper bound controls the largest eigenvalue. -/
theorem largest_eigenvalue_le (hA : A.IsHermitian) (t : ℝ)
    (hRay : ∀ x : Fin (n + 2) → ℝ, x ⬝ᵥ (A *ᵥ x) ≤ t * (x ⬝ᵥ x)) :
    orderedEigenvalues hA 0 ≤ t := by
  apply first_le (Matrix.isHermitian_iff_isSymmetric.mp hA) finrank_euclideanSpace_fin
  intro x
  rw [euclidean_quad, euclidean_norm_sq]
  exact hRay (WithLp.ofLp x)

/-- A strict quadratic-form bound on a plane controls the second-largest eigenvalue. -/
theorem second_eigenvalue_gt (hA : A.IsHermitian) (q : ℝ) (u v : Fin (n + 2) → ℝ)
    (hRay : ∀ a b : ℝ, a ≠ 0 ∨ b ≠ 0 →
      let x := a • u + b • v
      q * (x ⬝ᵥ x) < x ⬝ᵥ (A *ᵥ x)) :
    q < orderedEigenvalues hA 1 := by
  apply second_gt (Matrix.isHermitian_iff_isSymmetric.mp hA) finrank_euclideanSpace_fin
    q (WithLp.toLp 2 u) (WithLp.toLp 2 v)
  intro a b hab
  rw [euclidean_quad, euclidean_norm_sq]
  exact hRay a b hab

end Matrices

end Cazenave20829

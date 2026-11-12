import Mathlib

/-!
Coordinate-level algebra for the even Wachs polytope.
This is a candidate Lean 4/mathlib file, NOT compiled or kernel checked.
The finite Wachs-permutation bijection and convex-hull theorem remain to formalize.
-/

namespace WachsAffine

/-- One adjacent pair of coordinates in the original permutation vector. -/
def forward (p : ℝ × ℝ) : ℝ × ℝ :=
  ((p.1 + p.2 + 1) / 4, p.2 - p.1)

/-- The inverse affine coordinate change. -/
def backward (p : ℝ × ℝ) : ℝ × ℝ :=
  (2 * p.1 - 1 / 2 - p.2 / 2, 2 * p.1 - 1 / 2 + p.2 / 2)

theorem forward_backward (p : ℝ × ℝ) : forward (backward p) = p := by
  rcases p with ⟨a, b⟩
  simp only [forward, backward, Prod.mk.injEq]
  constructor <;> ring

theorem backward_forward (p : ℝ × ℝ) : backward (forward p) = p := by
  rcases p with ⟨x, y⟩
  simp only [forward, backward, Prod.mk.injEq]
  constructor <;> ring

/-- Coordinatewise extension to `m` adjacent pairs. -/
def forwardVec {m : ℕ} (x : Fin m → ℝ × ℝ) : Fin m → ℝ × ℝ :=
  fun i => forward (x i)

def backwardVec {m : ℕ} (x : Fin m → ℝ × ℝ) : Fin m → ℝ × ℝ :=
  fun i => backward (x i)

theorem forwardVec_backwardVec {m : ℕ} (x : Fin m → ℝ × ℝ) :
    forwardVec (backwardVec x) = x := by
  funext i
  exact forward_backward (x i)

theorem backwardVec_forwardVec {m : ℕ} (x : Fin m → ℝ × ℝ) :
    backwardVec (forwardVec x) = x := by
  funext i
  exact backward_forward (x i)

/-- Block formula: permutation value `j` and orientation `e`. -/
def block (j e : ℝ) : ℝ × ℝ :=
  (2 * j - 1 / 2 - e / 2, 2 * j - 1 / 2 + e / 2)

theorem forward_block (j e : ℝ) : forward (block j e) = (j, e) := by
  simp only [forward, block, Prod.mk.injEq]
  constructor <;> ring

end WachsAffine

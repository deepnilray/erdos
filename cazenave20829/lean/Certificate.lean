import Mathlib.Data.Real.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Exact real quadratic-form certificates for the 11-vertex witness.
The coordinate order is (u₁,v₁,w₁,w₁',p₁,u₂,v₂,w₂,w₂',p₃,p₂).
The connecting path is u₁,p₁,p₂,p₃,u₂. -/

namespace Cazenave20829

abbrev Vec := Fin 11 → ℝ

def normSq (x : Vec) : ℝ :=
  x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 + x 4 ^ 2 +
  x 5 ^ 2 + x 6 ^ 2 + x 7 ^ 2 + x 8 ^ 2 + x 9 ^ 2 + x 10 ^ 2

def lapForm (x : Vec) : ℝ :=
  (x 0 - x 2) ^ 2 + (x 0 - x 3) ^ 2 + (x 1 - x 2) ^ 2 +
  (x 1 - x 3) ^ 2 + (x 2 - x 3) ^ 2 + (x 0 - x 4) ^ 2 + (x 4 - x 10) ^ 2 +
  (x 5 - x 7) ^ 2 + (x 5 - x 8) ^ 2 + (x 6 - x 7) ^ 2 +
  (x 6 - x 8) ^ 2 + (x 7 - x 8) ^ 2 + (x 5 - x 9) ^ 2 + (x 9 - x 10) ^ 2

def adjForm (x : Vec) : ℝ :=
  2 * (x 0 * x 2 + x 0 * x 3 + x 1 * x 2 + x 1 * x 3 + x 2 * x 3 +
    x 0 * x 4 + x 4 * x 10 + x 5 * x 7 + x 5 * x 8 + x 6 * x 7 +
    x 6 * x 8 + x 7 * x 8 + x 5 * x 9 + x 9 * x 10)

private noncomputable def sideSquares (u v w q z : ℝ) : ℝ :=
  (5 / 4) * q ^ 2 + (21 / 8) * (v + (16 / 21) * w) ^ 2 +
  (313 / 84) * (w + (168 / 313) * u) ^ 2 +
  (313 / 168) * (z + (168 / 313) * u) ^ 2 + (37 / 2504) * u ^ 2

private theorem lap_sos (x : Vec) :
    (37 / 8) * normSq x - lapForm x =
      sideSquares (x 0) (x 1) ((x 2 + x 3) / 2) ((x 2 - x 3) / 2) (x 4) +
      sideSquares (x 5) (x 6) ((x 7 + x 8) / 2) ((x 7 - x 8) / 2) (x 9) +
      (21 / 8) * (x 10 + (8 / 21) * (x 4 + x 9)) ^ 2 +
      (8 / 21) * (x 4 - x 9) ^ 2 := by
  unfold normSq lapForm sideSquares
  ring

theorem lap_bound (x : Vec) : lapForm x ≤ (37 / 8) * normSq x := by
  apply sub_nonneg.mp
  rw [lap_sos]
  unfold sideSquares
  positivity

def witness (a b : ℝ) : Vec :=
  ![3 * a, 3 * a, 4 * a, 4 * a, a, 3 * b, 3 * b, 4 * b, 4 * b, b, 0]

theorem witness_norm (a b : ℝ) : normSq (witness a b) = 51 * (a ^ 2 + b ^ 2) := by
  simp [normSq, witness]; ring

theorem witness_adj (a b : ℝ) : adjForm (witness a b) = 134 * (a ^ 2 + b ^ 2) := by
  simp [adjForm, witness]; ring

theorem witness_adj_strict (a b : ℝ) (hne : a ≠ 0 ∨ b ≠ 0) :
    (21 / 8) * normSq (witness a b) < adjForm (witness a b) := by
  have hpos : 0 < a ^ 2 + b ^ 2 := by
    rcases hne with ha | hb
    · exact add_pos_of_pos_of_nonneg (sq_pos_of_ne_zero ha) (sq_nonneg b)
    · exact add_pos_of_nonneg_of_pos (sq_nonneg a) (sq_pos_of_ne_zero hb)
  apply sub_pos.mp
  rw [witness_norm, witness_adj]
  have heq : 134 * (a ^ 2 + b ^ 2) - (21 / 8) * (51 * (a ^ 2 + b ^ 2)) =
      (1 / 8) * (a ^ 2 + b ^ 2) := by ring
  rw [heq]
  exact mul_pos (by norm_num) hpos

end Cazenave20829

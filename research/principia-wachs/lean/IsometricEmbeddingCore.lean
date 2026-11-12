import Mathlib

/-!
Uncompiled Lean 4 / Mathlib proof sketch for the coordinate inversion.
This file is deliberately limited to elementary algebra, not the main polytope theorem.
The theorem statements below use no `sorry`, but have NOT been kernel checked.
-/
namespace Wachs

def encode (a b : ℝ) : ℝ × ℝ := ((a + b + 1) / 4, b - a)
def decode (p : ℝ × ℝ) : ℝ × ℝ :=
  (2 * p.1 - 1 / 2 - p.2 / 2, 2 * p.1 - 1 / 2 + p.2 / 2)

theorem decode_encode (a b : ℝ) : decode (encode a b) = (a, b) := by
  simp only [decode, encode]
  apply Prod.ext <;> dsimp <;> ring

theorem encode_decode (p : ℝ × ℝ) : encode (decode p) = p := by
  rcases p with ⟨a,b⟩
  simp only [decode, encode]
  apply Prod.ext <;> dsimp <;> ring

end Wachs

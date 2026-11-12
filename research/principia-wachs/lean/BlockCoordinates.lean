import Mathlib

/-!
# Affine block coordinates for Wachs vertices

This is a small, independently stated algebraic component of the full proof.
It has NOT been compiled in the present run.
-/

namespace WachsProduct

def encode (a b : ℚ) : ℚ × ℚ :=
  (2 * a - (1 / 2 : ℚ) - b / 2,
   2 * a - (1 / 2 : ℚ) + b / 2)

def decode (x : ℚ × ℚ) : ℚ × ℚ :=
  ((x.1 + x.2 + 1) / 4, x.2 - x.1)

theorem decode_encode (a b : ℚ) : decode (encode a b) = (a, b) := by
  simp only [decode, encode, Prod.mk.injEq]
  constructor <;> ring

theorem encode_decode (x : ℚ × ℚ) : encode (decode x) = x := by
  rcases x with ⟨u, v⟩
  simp only [decode, encode, Prod.mk.injEq]
  constructor <;> ring

end WachsProduct

import Certificate
import SpectralBridge
import Mathlib.Combinatorics.SimpleGraph.LapMatrix
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith

/-! The explicit connected graph and the spectral disproof. -/

open Matrix
open scoped BigOperators Matrix

namespace Cazenave20829

private def edges : List (ℕ × ℕ) :=
  [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 4), (4, 10),
   (5, 7), (5, 8), (6, 7), (6, 8), (7, 8), (5, 9), (9, 10)]

/-- Two diamonds joined at their degree-two vertices by a path with four edges. -/
def graph : SimpleGraph (Fin 11) where
  Adj i j := (i.val, j.val) ∈ edges ∨ (j.val, i.val) ∈ edges
  symm := by intro i j h; exact h.symm
  loopless := ⟨by decide⟩

instance : DecidableRel graph.Adj := fun i j =>
  inferInstanceAs (Decidable ((i.val, j.val) ∈ edges ∨ (j.val, i.val) ∈ edges))

private theorem step (i j : Fin 11) (h : graph.Adj i j) : graph.Reachable i j := h.reachable

theorem graph_connected : graph.Connected := by
  rw [graph.connected_iff_exists_forall_reachable]
  refine ⟨10, fun i => ?_⟩
  have left := step 10 4 (by decide)
  have leftPort := left.trans (step 4 0 (by decide))
  have leftTwin := leftPort.trans (step 0 2 (by decide))
  have right := step 10 9 (by decide)
  have rightPort := right.trans (step 9 5 (by decide))
  have rightTwin := rightPort.trans (step 5 7 (by decide))
  fin_cases i
  · exact leftPort
  · exact leftTwin.trans (step 2 1 (by decide))
  · exact leftTwin
  · exact leftPort.trans (step 0 3 (by decide))
  · exact left
  · exact rightPort
  · exact rightTwin.trans (step 7 6 (by decide))
  · exact rightTwin
  · exact rightPort.trans (step 5 8 (by decide))
  · exact right
  · exact SimpleGraph.Reachable.refl _

private theorem adj_hermitian : (graph.adjMatrix ℝ).IsHermitian := by
  rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial]
  exact graph.isSymm_adjMatrix

private theorem lap_hermitian : (graph.lapMatrix ℝ).IsHermitian := by
  rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial]
  exact graph.isSymm_lapMatrix

private theorem sum11 (f : Fin 11 → ℝ) :
    (∑ i, f i) = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 + f 7 + f 8 + f 9 + f 10 := by
  simp only [Fin.sum_univ_succ, Fin.sum_univ_zero]
  change f 0 + (f 1 + (f 2 + (f 3 + (f 4 + (f 5 + (f 6 + (f 7 + (f 8 + (f 9 + (f 10 + (0))))))))))) = _
  simp only [add_zero, add_assoc]

private theorem norm_eq (x : Vec) : x ⬝ᵥ x = normSq x := by
  simp only [dotProduct, sum11, normSq]
  ring

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
private theorem adj_eq (x : Vec) : x ⬝ᵥ (graph.adjMatrix ℝ *ᵥ x) = adjForm x := by
  rw [graph.dotProduct_mulVec_adjMatrix]
  norm_num [sum11, graph, edges, adjForm]
  simp (disch := decide) only [if_neg]
  ring

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
private theorem lap_eq (x : Vec) : x ⬝ᵥ (graph.lapMatrix ℝ *ᵥ x) = lapForm x := by
  rw [← Matrix.toLinearMap₂'_apply', SimpleGraph.lapMatrix_toLinearMap₂']
  norm_num [sum11, graph, edges, lapForm]
  simp (disch := decide) only [if_neg]
  ring

private theorem witness_linear (a b : ℝ) :
    a • witness 1 0 + b • witness 0 1 = witness a b := by
  funext i
  fin_cases i <;> simp [witness, Pi.add_apply] <;> ring

/-- Cazenave's Conjecture 2 fails on this connected simple graph on 11 vertices. -/
theorem counterexample : graph.Connected ∧
    orderedEigenvalues lap_hermitian 0 - orderedEigenvalues adj_hermitian 1 < 2 := by
  refine ⟨graph_connected, ?_⟩
  have hlap : orderedEigenvalues lap_hermitian 0 ≤ 37 / 8 :=
    largest_eigenvalue_le lap_hermitian (37 / 8) fun x => by
      rw [lap_eq, norm_eq]
      exact lap_bound x
  have hadj : 21 / 8 < orderedEigenvalues adj_hermitian 1 :=
    second_eigenvalue_gt adj_hermitian (21 / 8) (witness 1 0) (witness 0 1) fun a b hab => by
      dsimp only
      rw [witness_linear, norm_eq, adj_eq]
      exact witness_adj_strict a b hab
  linarith

#print axioms counterexample

end Cazenave20829

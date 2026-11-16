# LOG — winter 2026 open-conjecture attack (folder winter2026/02_math)

## 2026-11-17, session 1: target chosen (SSNC, case n = 2δ + 3)

Verdict: target chosen, nothing new proved yet. Worst news first: the area is crowded (2026 preprints, several
AI-assisted), and Brukhman's own remark says his counting fails at n = 2δ + 3.

### Prior-art gate
See TARGETS.md. Conway–Guy optimality rejected (false at n = 12 per OEIS A276661).
Brukhman 2608.11530 Lemma 2.1 and Thm 1.1 re-derived line by line: correct (PROVED, by them; checked by me).

### Forecast (written before any computation)
- The SAT encoding for (n, δ) = (2δ + 3, δ) will be UNSAT for δ ≤ 6 (forced by Kaneko–Locke). Expected solve
  time grows steeply with δ; I expect δ ≤ 4 in seconds, δ = 5 or 6 to be slow without symmetry breaking, and
  δ = 7 (n = 17) out of reach in this session. Probability that δ = 7 closes here: low.
- On the theory side, I expect an exact identity reducing the case n = 2δ + 3 to bounding the number of vertices
  whose fixed-target capacity is zero, and that this bound is where new ideas are needed.

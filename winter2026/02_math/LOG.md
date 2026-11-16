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

### Session 1, step 2 (2026-11-17): reduction identity and SAT scaling

Verdict: no new case of SSNC settled. Worst news: plain SAT and CP-SAT cannot reach δ = 7 (n = 17); the time grows
about 600× from δ = 4 to δ = 5. Theory gives an exact reduction (below) whose remaining obstruction is a set Z of
"complete" vertices.

Notation: D oriented, n = 2δ + 3, δ = min outdegree, j_v = d⁺(v) − δ, σ_v = d⁺(v) − 1 − |N2(v)| (σ_v ≥ 0 for all v
iff D has no Seymour vertex), T(x) = non-in-neighbours of x, q_x = |T(x)| − δ, U(v) = targets not reachable from v
in ≤ 2 steps, P(x) = {v : x ∈ U(v)}, p_x = |P(x)|, M = set of non-adjacent pairs.

- I1 PROVED (direct double count; any oriented D with n = 2δ + 3):
  Σ_x (p_x − 2q_x + 1) = Σ_v σ_v.
- I2 PROVED: q_x = deg_M(x) + j_x. Hence q_x = 0 iff x has no missing edge and d⁺(x) = δ (so d⁻(x) = δ + 2).
  Call this set Z.
- I3 PROVED (refinement of Brukhman Lemma 2.1, same count kept exact): if p = p_x > 0 then
  p(2q_x − 1 − p)/2 ≥ J_P + m_P + r_x, with J_P = Σ_{v∈P(x)} j_v, m_P = missing pairs inside P(x),
  r_x = #{(v,t) : v ∈ P(x), t ∈ T(x) \ P(x), v ↛ t}.
- Consequence C1 PROVED: in a counterexample, with D_x := 2q_x − 1 − p_x, one has D_x ≥ 0 for x ∉ Z,
  D_x = −1 for x ∈ Z, D_x ≥ 1 if p_x = 0 and x ∉ Z, and Σ_x D_x = −Σ_v σ_v ≤ 0. So a counterexample needs
  |Z| ≥ Σ_{x∉Z} D_x + Σ_v σ_v. Brukhman's n = 2δ + 2 case is the analogue where Z cannot occur.
- C2 PROVED (tight targets): if D_x = 0 and p_x > 0, then P(x) is a regular tournament of order 2q_x − 1, every
  member has outdegree δ, and every member dominates all of T(x) \ P(x).
- C3 PROVED (the case Z = ∅): then every σ_v = 0 and every D_x = 0 with p_x > 0; vertices with j_v ≥ 2 are impossible
  (|U(v)| = 3 − 2j_v), and vertices with j_v = 1 would have |U(v)| = 1 but lie in no P(x) (members of P(x) have
  j = 0 by C2), contradiction. So D is out-regular of degree δ, |N2(v)| = δ − 1 and |U(v)| = 3 for every v,
  q_x = deg_M(x) ≥ 1, |M| = n, and every P(x) has the structure of C2.
- C4 PROVED: for z ∈ Z, N⁻(z) = N2(z) ∪ U(z) and, for y ∈ U(z), T(y) = {z} ∪ N⁺(z) ∪ X_y with
  X_y ⊆ N⁻(z) \ {y}, |X_y| = q_y − 1; if moreover D_y = 0 then X_y ⊆ P(y).
- VERIFIED: I1, I2, I3 hold on 1500 random oriented graphs with n = 2δ + 3, δ = 1..5 (`check_identities.py`);
  planted failure (I1 with +0, I3 with +1 extra) fires on 1500/1500 and 1287/1500 graphs.
- VERIFIED (SAT, `ssnc_sat.py`, CaDiCaL 1.9 via pysat): no counterexample with n = 2δ + 3 for δ = 1..5
  (δ = 5: 193 s); n = 2δ + 4 for δ = 3, 4. These are known-answer controls (Kaneko–Locke), not new results.
  Out-regular subcase (`--regular`): δ = 5 in 31 s. Planted failure: with the constraint weakened to
  |N2| ≤ d⁺ (`--slack 1`) every tested instance is SAT and the model passes the independent checker
  (e.g. the Paley tournament on 7 vertices, all (3,3)).
- CP-SAT (`ssnc_cpsat.py`) with the redundant Lemma 2.1 constraints: δ = 4 in 2.3 s, δ = 5 not solved in 400 s.

Dead ideas
- Plain SAT / CP-SAT for (n, δ) = (17, 7): extrapolated 10⁵ s or more; also the δ = 7 case is the one
  arXiv:2606.30588 claims, so a certificate there would only be an independent check.
- Adding Brukhman's capacity inequalities as redundant CP-SAT constraints: slower, not faster.

Next step (exact): prove C3's structure impossible (out-regular, |M| = n, every P(x) a regular tournament of order
2 deg_M(x) − 1 dominating T(x) \ P(x)), then charge each z ∈ Z to a target y ∈ U(z) with D_y ≥ 1 using C4.

### Session 1, step 3 (2026-11-17): the case Z = ∅ is closed, and |Z| ≥ 2 in any counterexample

Verdict: PROVED a new partial result for the dense case n = 2δ + 3 (write-up `ssnc_2d3.tex` / `ssnc_2d3.pdf`).
Worst news: the full case n = 2δ + 3 is still open; the remaining case has at least two complete vertices of
outdegree δ, and I have no charging argument for it yet. Not yet checked by anyone else.

- Lemma 1 PROVED: the capacity inequality I3 is an equality, p(2q_x − 1 − p)/2 = J_P + m_P + r_x.
- Lemma 3 PROVED (any oriented graph): if x is tight (p_x > 0, D_x = 0) and v ∈ P(x), then T(x) ⊆ R(v)
  ("x is covered for v"). Proof: P(x) is a regular tournament of order 2q − 1 dominating T(x) \ P(x); an in-neighbour
  w of v in P(x) cannot beat all q − 1 out-neighbours of v there, so w ∈ N2(v).
- Lemma 4 PROVED (any oriented graph): each v has at most one covered target, because a covered x receives arcs
  from every other y ∈ U(v).
- Theorem PROVED: a counterexample with n = 2δ + 3 satisfies |Z| = Σσ + Σ_E(2q − 1) + Σ_N D_x ≥ |N| ≥ max_v|U(v)| − 1 ≥ 2.
  So SSNC holds for every oriented graph with n = 2δ + 3 having at most one vertex of outdegree δ adjacent to all
  others. (Replaces C3 of step 2, which is the special case Z = ∅.)
- VERIFIED: Lemma 3 on 502 tight (x, v) pairs and Lemma 4 on all sources of 1500 random graphs (n = 2δ + 3, δ ≤ 5):
  0 violations; planted false claim "no covered target" refuted at 3942 sources (`check_identities.py`).
- SAT with a Z-vertex fixed as vertex 0 (`--zvertex`, sound by the Theorem): δ = 5 in 33.5 s (was 193 s), control
  `--slack 1` SAT. Still not enough for δ = 7.

Next step (exact): take z1 ≠ z2 in Z (complete, outdegree δ, N⁻(z) = N2(z) ∪ U(z)). Show the targets in U(z1) ∪ U(z2)
that are non-tight carry total deficiency Σ D_x > |Z|, e.g. by proving that a non-tight target x ∈ U(z) has
D_x ≥ 2 or is shared by at most one element of Z. Also run `ssnc_sat.py 15 6 --zvertex` in the background with a
second Z vertex fixed (cases: z2 ∈ N⁺(z1) or z2 ∈ N⁻(z1)) to measure δ = 6.

### Session 1, step 4 (2026-11-17): structure at a complete vertex; δ = 6 SAT runs

- Lemma 6 PROVED (in ssnc_2d3.tex): for z ∈ Z with k = |U(z)| ≥ 3: every y ∈ U(z) has all in-neighbours in
  N⁻(z) = N2(z) ∪ U(z); T(y) = {z} ∪ N⁺(z) ∪ X_y with |X_y| = q_y − 1; y is covered iff X_y ∩ U(z) = ∅; at most one
  y ∈ U(z) has q_y = 1; Σ_{y∈U(z)} q_y ≥ k(k+1)/2 (≥ 6).
- SAT with two Z vertices fixed (`--zvertex --z2 out|in`, sound by the step-3 Theorem; labels inside N⁺(0) and
  inside N⁻(0) are interchangeable): δ = 5 UNSAT in 5.7 s + 4.2 s (was 193 s without any of the theory).
  Controls with `--slack 1` SAT. δ = 6 (n = 15) runs started: both cases still running after 20 min CPU each.
  Result for δ = 6 would only re-confirm Kaneko–Locke; its purpose is to extrapolate the cost of δ = 7.

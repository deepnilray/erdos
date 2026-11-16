# Open conjecture attack (difficulty about 19 to 39 on the scale Riemann hypothesis = 100)

Status 2026-11-17: IN PROGRESS. Target chosen: Seymour's second neighbourhood conjecture, dense case n = 2δ + 3
(see TARGETS.md). PROVED so far: any counterexample with n = 2δ + 3 has at least two vertices of outdegree δ adjacent
to all other vertices (ssnc_2d3.tex/.pdf). Open: the case |Z| ≥ 2. Details and next step in LOG.md.

## Rules for the agent that picks this up
1. Read `../../CHECKPOINTS.md` on branch `claude/all-checkpoints` first. Do not choose any problem listed there, nor:
   Erdős–Straus, Andrica, Legendre, Erdős #203, #455, #1110, #39, #249, #454, #413, #287, #389, #699, #727, sunflower,
   unfair 0–1 polynomials, Gilbreath/SpikeBound, Stanley's Fibonacci-product conjectures, Cazenave's graph conjectures,
   the Principia Chebyshev product, lonely runner, Giuga, Lehmer, Brocard, Fonollosa, Wachs, Zeilberger-type OEIS recurrences.
2. Selection criteria: stated by a named mathematician in the literature; real partial results; still open in November 2026
   (open the erdosproblems.com page or arXiv and check for 2025–2026 solutions, many by AI systems); plausibly reducible to a
   finite certificate (case analysis, LP/SDP dual, SAT/ILP with symmetry breaking, flag algebras, explicit construction).
   Not low-hanging (not a freshly machine-mined conjecture), not a famous monster.
3. Write `TARGETS.md` with 4 verified candidates (exact statement, source URL, date checked, best partial results with arXiv
   ids, attack plan, main risk, difficulty estimate), then pick one and attack it.
4. Protocol: prior-art gate on the mathematical object before computing; forecast before computing; every computation has a
   planted-failure control that fires; label everything PROVED / VERIFIED (with bound) / CONJECTURED; verdict first; dead-idea
   ledger; never call a verified claim proved.
5. Log every session in `LOG.md` here (dated: what was tried, results with labels, dead ideas, next step) and commit and push,
   so no later run repeats work.

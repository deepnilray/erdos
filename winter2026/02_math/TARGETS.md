# TARGETS — open-conjecture selection (difficulty 19–39, RH = 100)

Checked 2026-11-17. Exclusion list in `STATUS.md` and `CHECKPOINTS.md` (branch `claude/all-checkpoints`) respected.
Citations below were opened this session unless marked "not re-opened".

## CHOICE: Candidate 1, Seymour's second neighbourhood conjecture, first open dense case n = 2δ + 3

## Disqualified during search
- **Conway–Guy optimality** (the Conway–Guy sets give the least possible largest element of an n-element
  sum-distinct set). DEAD: OEIS A276661 (queried via OEIS JSON, 2026-11-17) records a(12) ≤ 1157 < 1164 = A005318(12)
  (Ven Popov, Nov 27 2025), and a(10) = 309 computed by P. W. Dyson (GitHub pwdyson/erdos_1, 2025). So the
  optimality conjecture is false at n = 12 and the small cases are being cleared by others.

## Candidate 1 (CHOSEN): Seymour's second neighbourhood conjecture (SSNC)
- **Statement.** Every finite oriented graph D has a vertex v with |N⁺⁺(v)| ≥ |N⁺(v)|, where N⁺⁺(v) is the set of
  vertices at out-distance exactly 2 from v (a "Seymour vertex"). Seymour (1990), see Dean–Latka.
- **Sources opened.** arXiv:2608.11530 (J. Brukhman, 12 Aug 2026, PDF read in full); arXiv:2606.30588 (Sadhukhan,
  Sandeep, Sen, 29 Jun 2026, abstract: SSNC-type statement for minimum outdegree ≤ 7; title on arXiv is "Locating a
  Seymour vertex in oriented graphs having minimum outdegree at most 7", which differs from the title Brukhman cites);
  arXiv:2603.29626 (Guo–Kang–Zwaneveld, Seymour-tight orientations); arXiv:2403.02842 (Espuny Díaz–Girão–Granet–
  Kronenberg); arXiv:2601.21563 (Halkiewicz, Pisa graphs, computation only to 7 vertices).
- **Status.** Open as of Nov 2026 (no claimed full proof among the sources above).
- **Best partial results.** Tournaments: Fisher (1996, JGT 23). Minimum outdegree δ ≤ 6: Kaneko–Locke (2001, Congr.
  Numer. 148; not re-opened, cited via 2608.11530); δ = 7: 2606.30588 (preprint). Missing-edge structures: Fidler–
  Yuster (2007), Ghazal (2012), Dara–Francis–Jacob–Narayanan (2022), arXiv:2406.03635. Dense case n = 2δ + 2 for
  every δ: 2608.11530 Thm 1.1 (I re-derived the proof, see LOG.md: correct). Consequence: a counterexample has
  n ≥ 2δ + 3, order ≥ 17 unconditionally, ≥ 19 using 2606.30588.
- **Target.** Prove SSNC for all oriented graphs with n = 2δ + 3 (Brukhman's remark: his counting fails there).
  This would raise the counterexample order bound to 18 unconditionally and to 20 conditionally. Finite sub-target:
  a SAT/PB certificate for (n, δ) = (17, 7), the smallest unconditionally open case.
- **Attack plan.** (a) Exact identity for n = 2δ + 3 linking source deficits and target capacities; sharpen
  Brukhman's fixed-target lemma at the vertices where it is slack. (b) SAT/PB encoding of "no Seymour vertex, min
  outdegree δ, n = 2δ + 3", run on δ = 3..6 (must be UNSAT by Kaneko–Locke: known-answer control) to measure scaling,
  then δ = 7. Planted-failure control: weakened constraint must become SAT and the model must pass an independent
  checker.
- **Main risk.** SAT symmetry (17! labellings) may make δ = 7 infeasible; the general n = 2δ + 3 argument may need
  genuinely new ideas (crowded area: AI-assisted groups active in 2026).
- **Difficulty.** Full SSNC about 45; the case n = 2δ + 3 about 22.

## Candidate 2: Erdős #64 (Erdős–Gyárfás): min degree ≥ 3 ⇒ cycle of length 2^k
- **Source.** https://www.erdosproblems.com/64 and forum thread (opened 2026-11-17; page edited 10 Apr 2026). Open.
- **Partial results.** Liu–Montgomery (large minimum degree); Markström 2004 (cubic counterexample ≥ 30 vertices),
  Nowbandegani–Esfandiari 2011 (bipartite ≥ 32) as cited on the page; forum: Tranquilli arXiv:2608.02675 (cubic
  bipartite ≥ 60, not re-opened) and an AI-assisted search to 62 vertices (cubic bipartite); general cubic search only
  to 34 vertices.
- **Plan.** Orderly generation of cubic graphs (girth/cycle pruning) to push the general cubic bound past 30–34.
- **Risk.** Only a bound extension, crowded by AI-assisted searchers. **Difficulty** about 35 (full), bound work low value.

## Candidate 3: Erdős #107, Happy Ending f(7) = 33
- **Source.** https://www.erdosproblems.com/107 (opened 2026-11-17, edited 11 Apr 2026). Open; f(6) = 17 known
  (Szekeres–Peters 2006, not re-opened).
- **Plan.** Signature/SAT encoding (Szekeres–Peters style) for 33 points with no convex 7-gon.
- **Risk.** Compute: far beyond this budget. **Difficulty** of n = 7 case about 30.

## Candidate 4: Frankl union-closed sets conjecture, small-universe case
- **Source.** arXiv:1508.05718 (abstract opened: conjecture true for separating families with
  |A| ≤ 2(m + m/(log₂m − log₂log₂m))); survey arXiv:1309.3297 (not re-opened). Gilmer's constant-fraction bound
  arXiv:2211.09055 (not re-opened). Open.
- **Plan.** FC-family / weight-LP certificates for the next universe size.
- **Risk.** Famous (closer to 45), heavy formal-verification prior work. **Difficulty** about 40.

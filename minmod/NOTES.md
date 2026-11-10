# Fonollosa's minimum-modulus conjecture — research log (run of 2026-11-10)

Verdict: **PARTIAL**. Conjecture 1 of arXiv:2607.08366 is not proved. New: a sign characterization, a cyclic-order
lemma with two consequences, exhaustive verification for n = 8, a refined conjecture, a sporadic class, and a
negative result about the "all-anchor dissociated" weakening. Paper: `minmod.tex` / `minmod.pdf`.

## Step 1. Candidates considered (status sources: erdosproblems database `teorth/erdosproblems` at 2026-11-09,
`google-deepmind/formal-conjectures` at 2026-11-09, arXiv pages; "FC-open" = marked `research open` there, not
independently re-verified by me beyond that)

| # | Problem | Status seen | Difficulty (RH = 100) | Why it might yield / why dropped |
|---|---|---|---|---|
| 1 | Fonollosa Conj. 1 (min modulus, unique multiset sums), arXiv:2607.08366 | open: author repo README (24 Jul 2026), public issue of 22 Oct 2026, FC-open | 25–35 | three months old, finite and combinatorial, exact computation possible. **Chosen.** |
| 2 | Amdeberhan–Medina–Moll: tan(arctan 1 + … + arctan n) not an integer for n ≥ 5 | FC-open; Ono (arXiv:2607.05739) proves integer values are rare | 40 | reduces to "M_n − 1 is not a square" for an explicit Gaussian-integer norm; needs a transcendence-type input. Dropped. |
| 3 | Berndt–Bhat–Meyer–Xie–Zaharescu, S(k) > 0 for odd primes k (arXiv:2501.03234) | FC-open | 30 | S(k) is a cubic moment of L(0,χ) over odd characters; S(k)/k fluctuates between 2.5 and 4.9 for k near 1000, so positivity needs an explicit main term. Dropped for length. |
| 4 | Graffiti (WOWII) Conj. 84: tree(G) ≥ 2 rad(G)/δ(G) | FC-open | 12 | reduces to: a connected graph with a leaf has an induced tree on 2·rad vertices. Low weight; kept as a fallback. |
| 5 | TxGraffiti Conj. 3: i(G) ≤ μ*(G) for regular graphs (arXiv:2507.17780) | FC-open | 20 | counterexample search plausible; not attempted. |
| 6 | Catch-Up game conjecture (draw when N(N+1)/2 is even) | FC-open | 25 | needs explicit strategies for all N. |
| 7 | MathOverflow 339137 (0–1 polynomial factors) | FC-open | 35 | long-standing. |
| 8 | Balister–Győri–Schelp conjecture in F_2^s | FC-open | 35 | |
| 9 | Dean's conjecture, k = 5 (cycle length divisible by 5) | FC-open | 35 | |
| 10 | Erdős #242 Erdős–Straus (checkpoint §1) | open | 60 | gap is a primes-in-progressions statement. |
| 11 | Erdős #203 (checkpoint §3) | open | 45 | needs Opera de Cribro Lemma 6.3 or a bound on c(e). |
| 12 | Erdős #455 (checkpoint §4) | open | 50 | 22 dead ideas already. |
| 13 | Erdős #307 (two prime sets, product of reciprocal sums = 1) | "verifiable" in the database | 40 | pure search; heavily tried. |
| 14 | Erdős #1110, pairs (9,2), (5,3) (checkpoint §5) | open, files not in repo | 35 | cannot resume without files. |
| 15 | Kurepa's left-factorial conjecture | FC-open | 60 | |
| 16 | Curling number conjecture | FC-open | 45 | |
| 17 | SpikeBound(5) / Chase–Hunter–Tao question (checkpoint §5) | files not in repo | 40 | |

The Erdős database (2026-11-09) lists 588 problems as open; these have been swept by many groups and AI systems for
a year, so a fresh conjecture was preferred.

## Forecast written before computing (problem 1)
The conjecture is probably true. Expected outcome: PARTIAL — a structural reformulation plus an improved lower bound
or an extended verification; a full proof needs an argument that uses cyclicity, because (Z_2)^(n-1) reaches 2^(n-1).

## What was done, with labels
- PROVED: sign characterization (valid ⇔ every nonzero sum-zero relation has an entry ≥ 2 and an entry ≤ −2).
- PROVED: heredity, affine invariance, quotient by a subgroup containing all differences; Inal's 2^(n-1) bound re-derived.
- PROVED: cyclic-order lemma (for a pair a, c and subsets S ≠ S' of the rest with |S'| ≥ |S|: if x_S' − x_S = i(a−c) then i ∉ [−1, |S'|−|S|+1]).
- PROVED: if some difference is a unit, N ≥ 2^(n-1) + n − 2.
- PROVED: if a−c is a unit and A contains 3a−2c, 4a−3c, 3c−2a or 4c−3a, then N ≥ 5·2^(n-3).
- VERIFIED (exhaustive, n ≤ 8, 2^(n-1) ≤ N < 2^n): valid n-sets exist exactly for N = 2^n − 2^k with 2^k ≤ n. Logs in `logs/`.
- VERIFIED: sporadic valid class {0,1,3,10} mod 15.
- VERIFIED: AAD sets (n ≤ 7): same moduli as valid sets for n ≤ 6; for n = 7 they exist at N = 120, 124, 126, 127.
- VERIFIED: one-dimensional structure minimum 5·2^(m-1) for m ≤ 5 (`oned.c`).
- VERIFIED: with only k = 3 unrestricted coordinates the minimum is 6, 10, 20, 40 for n = 3..6 (`lk.c`); with k = 2 it is 2^(n-1).
- CONJECTURED: refined conjecture (N < 2^n ⇒ N | 2^n − 2^k, 2^k ≤ n); 1D bound for all m.

## Controls
See Section 5.1 of the paper. Every "no valid set" answer comes from a program that finds the known valid sets at
neighbouring moduli, agrees with two less-pruned programs for n ≤ 7, and whose outputs pass an independent checker
that rejects planted invalid sets.

## Dead ideas (obstruction in one line each; details in the paper's appendix)
1. Clique/pigeonhole and LP bounds that ignore cyclicity: capped at 2^(n-1) by (Z_2)^(n-1).
2. Union of two translated (or dilated, or differently anchored) cubes: overlaps exceed the deficit in every example.
3. A single virtual anchor covering Z_N: fails for the sporadic class mod 15.
4. Parseval / Riesz products / cyclotomic norms / F_p moment polynomial: restate "one relation", no new bound.
5. Averaging collisions over all translations: gives only C(2n,n)/2^n (known).
6. Replace validity by AAD: false at n = 7 (N = 120).
7. Parity induction for even N: no control of the split sizes.
8. "Double the smallest element" injection into the complement of the cube: coincidences with lighter points are allowed.
9. 1D bound by halving along a generator or by counting gap-2 steps: (5,7,9) mod 23 blocks both.
10. Hajós/Rédei replacement, near-factorizations, difference sets: the cube is not a factor, not a difference set (overlaps 4 vs 8 at N = 31).

## Next attack
1. Prove the 1D bound (Conjecture 2 of the paper) — the LP dual for a fixed cyclic order is explicit; find a uniform certificate.
2. Use relation vectors with two entries equal to ±2 (the AAD failure at n = 7 shows they are needed): in the b-cycle
   picture they forbid 2β_l − β(T) ∈ [1−|T|, 1]; brute force with these constraints added should give the constants
   beyond 5/8 and suggest the induction.
3. Extend the exhaustive search to n = 9 (N < 504): needs 512-bit bitsets and a stronger canonical form; estimated
   a few hundred CPU-hours with the present pruning.
4. Formalize Proposition 1 and Lemma 3 in Lean 4 against the existing statement in formal-conjectures.

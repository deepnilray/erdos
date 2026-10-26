# Erdős #203 — project hub (single source of truth)

Headed from the Andrica session; Andrica work lives separately on branch `claude/andrica-state` (`andrica/`).
Problem: is there an m (coprime to 6) such that 2^k·3^l·m + 1 is composite for all k, l ≥ 1? Status: **OPEN**.
Current verdict: NO more likely [CONJECTURED] — see `VERDICT.md` and `verdict/1–5`.

## Proved / verified so far (see the linked files)
- All pure coverings with e_p ≤ 4·10⁵ excluded; B(4·10⁵) = 0.730584 exact rational [PROVED, `DISTORTION.md`].
- Mixed certificates (primes + algebraic factorisations) excluded for e_p ≤ 4·10⁵ [PROVED, `MIXED.md`, Theorem E].
- B(8·10⁵) = 0.742445 in floating point [VERIFIED, float; exact-rational check pending].
- The 4–8·10⁵ pool (47583 primes) is certified complete by the second (gcd) route: all 20 chunks of (4·10⁵, 8·10⁵] give `certified complete: True` [VERIFIED, `verdict3/certify_range.py`, logs in `verdict3/chunks/`].
- Every m ≤ 10¹⁰ coprime to 6 has a prime 2^k3^l·m+1 with k,l ≥ 1 [VERIFIED, `verdict3/search_l1.c`; the old `search.c` wrongly allowed l=0]. Hardest m = 6257518159, first prime at (k,l)=(16,10), proved prime by a Lucas certificate.
- Erdős–Odlyzko 1979 Thm 2: positive lower density of m with a prime [literature].

## Public state (erdosproblems.com forum thread 203, read 2026-10-25)
- Status OPEN, no solution claims. Posted work: |H_p| = lcm of orders and Σ1/|H_p| ≥ 1 (AnimishSharma, Jun 2026), no covering with lcm < 5040 for p ≤ 5·10⁷; covering searches plateau at 71.7% (N=5040) and 76.0% (N=55440), density bound < 1 at N=720720 (veljjanoski, Sep 2026); "shallow" search 10¹⁰–10¹¹ with no match (emil467q, Nov 2025; convention and depth unstated).
- So our search to 10¹⁰ is not new as a range; its value is the k,l ≥ 1 convention with proved primes. Our exclusion of all coverings with e_p ≤ 4·10⁵ and no lcm condition goes far beyond anything posted.

## Run log
- 2026-10-10: five-direction assessment (verdict/1–5).
- 2026-10-17/22: scheduled all-agents run (trigger trig_016THwwcVavtrWxeAPL3Eiv1) fired; no commits came back
  (the parallel Andrica run failed on the usage limit, likely the same cause).
- 2026-10-23: two Sonnet agents launched from the head session (run3): agent A = YES-side certification,
  agent B = NO-side and literature. Reports go to `verdict3/`.
- 2026-10-23 (evening): both agents hit the usage limit, resumed after reset. B finished: `B_noside.md`, `APPROACHES.md`; no literature beyond Erdős–Odlyzko 1979; `verdict/5_priorart.md` wrongly calls #202 solved (it is open).

- 2026-10-26: run4 agents: A (certify, resumed), C (all-E no-covering), L (literature, continuous), V (check + Aristotle prompts). V status 1: no flaw; exposition gap — DISTORTION.md must state the CRT augmentation lemma (all pool sets nonempty) that MIXED.md states; fix in the paper.

## Run4 results (2026-10-26)
- **Theorem Z** (agent C, checked by V): any covering certificate has ≥ 10 300 primes with e_p > 8·10⁵ [VERIFIED on float B′=0.7984 at δ-cap 0.28; per-prime cost 1.68·10⁻⁵ CONFIRMED by V; exact B′ running]. Lettl–Sun alone gives ≥ 20.
- **Theorem A** (agent D, checked by V): all but ≈ 2.76% (ρ−1, ρ ≈ 1.0276) of m ≤ x coprime to 6 have k,l ≥ 1 with Ω(2^k3^l m+1) ≤ 19 [PROVED modulo the fundamental lemma of sieve theory, exact citation still to be matched; ρ VERIFIED numerically, no interval enclosure]. No prior art found (limited search).
- Proved lemmas: equal-index lattices sharing a primitive vector are equal; alignment criterion (2-D → 1-D iff gcd(e_p,e_q) | α_pβ_q−β_pα_q pairwise); common discrete log ⇒ 1-D, (3/p)=(2/p)^T, 5 and 13 incompatible, no common-T covering with e_p ≤ 8000; homogeneous (subgroup) certificates impossible; direction-lemma dichotomy.
- Dead routes (proved obstructions): every route to bound c(e)=#{p: e_p=e} (Minkowski, Möbius/gcd size, irredundance); density one for primes (parity, Chebyshev ceiling ≈ 0.49); Maynard dense clusters (too few forms); density one even for almost-primes (would imply no covering); literature YES constructions (all 1-D with free multiplier).
- Withdrawn: "uncovered density ≥ 0.2694" (B(E) bounds the tilted measure, not uniform density; counterexample 31 primes with e_p | 5040 cover 71.7%). Conditional theorems of A and C: stage-wise hypotheses false pointwise; being restated with aggregate hypotheses.

## Run3 assignments
- **A (certify):** second-route completeness certificate for `poolE_400k_800k.jsonl`; exact-rational B(8·10⁵);
  Theorem E at 8·10⁵; conditional all-E theorem with explicit hypothesis H; push E to 1.6·10⁶ if feasible.
- **B (no side + literature):** literature ledger `verdict3/APPROACHES.md`; best provable unconditional statement
  toward "every m has a prime"; extend the exhaustive search beyond 3·10⁹; Bateman–Horn refinement; red team of A.

## Aristotle (Lean) prompts
Prompts for formal verification are collected here when a result is ready for it.

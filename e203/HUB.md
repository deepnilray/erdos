# Erdős #203 — project hub (single source of truth)

Repo `deepnilray/erdos`, branch `claude/open-conjecture-search-h6tgg3`, folder `e203/`. Andrica work is separate
(branch `claude/andrica-state`, folder `andrica/`). Headed by Claude for Deepnil Ray. Last full update: 2026-10-30.

**Problem.** Is there an m coprime to 6 such that 2^k·3^l·m + 1 is composite for all k, l ≥ 1?
**Status: OPEN.** Nothing here proves YES or NO. Verdict: NO is more likely [CONJECTURED, `VERDICT.md`, `verdict/1–5`].

Labels: PROVED = complete argument; VERIFIED = computation with a control that can fail; CONJECTURED = evidence only.

---------------------------------------------------------------------------------------------------------------------
## 1. What is proved or verified (the results a paper can state)

### YES side — constructions of m are blocked
| # | statement | label | where |
|---|---|---|---|
| Y1 | No covering (finite set of primes p∤6 whose killed cosets cover Z²) uses only primes with e_p = \|⟨2,3⟩ mod p\| ≤ 4·10⁵. Bound B(4·10⁵) = 0.730584 < 1, exact rational. | PROVED | `DISTORTION.md` |
| Y2 | Same for mixed certificates (primes + algebraic factorisations; Capelli says these are the only algebraic ones). e_p ≤ 4·10⁵: bound 0.953242. **e_p ≤ 8·10⁵: totals ≤ 0.887544 (3 ∤ g) and ≤ 0.963820 (3 \| g), 2026-10-30** — B exact, R3 = 250822656/3288355921 exact (`verdict3/mixed_800k.log`), S bounded above with δ and every term rounded up (`verdict3/mixed_S_upper.py`, `mixed_800k_upper.log`), because `verify_mixed.py`'s exact S sum died at 8·10⁵ (huge common denominator). V CONFIRMED (independent 60-digit S = 0.1450987005; every δ value is an exact multiple of 0.01; R3 recomputed with the 8·10⁵ light mass, it depends on E through λ′). | PROVED (4·10⁵ and 8·10⁵) | `MIXED.md` Thm E |
| Y3 | **No covering uses only primes with e_p ≤ 8·10⁵.** B(8·10⁵) = 0.742445 < 1 in EXACT rational arithmetic (`verdict3/verify23_800k.log`, all 15 279 stages, 2026-10-30; δ file sha256 in `verify23_800k.delta.sha256`). Theorem E at 8·10⁵: see Y2. | PROVED (given Y4) | `verdict3/A_certify.md` |
| Y4 | Pool of all 100 814 primes with e_p ≤ 8·10⁵ is complete: gcd route (20/20 chunks, planted control 60/60), sieve route over all p < 2·10⁹ (exact match), V's own sieve to 3·10⁶. 12 primes > 2·10⁹ are covered only by the gcd route. | VERIFIED | `A_certify.md` §1, `V_check.md` §7 |
| Y5 | **Theorem Z.** Every covering contains at least N_Z primes with e_p > 8·10⁵. **N_Z = 13 184 PROVED**: B′ = 0.798372 < 1 at δ cap 0.28 in EXACT rational arithmetic (`verdict3/V_verify_cap028.log`, all 15 279 stages, 2026-10-30). N_Z = **14 082** with the jointly optimised δ (`verdict3/C_delta_final.json`): VERIFIED (float B′), exact check running (`C_run_exact.sh`, `C_ckpt_final.txt`). Key step: a single new prime's image in (Z/144)² is cyclic of order gcd(e_p,144), so its price is ≤ 2.2419 (V confirmed). | 13 184: PROVED (given Y4); 14 082: VERIFIED | `verdict3/C_allE.md` §3, §3d |
| Y6 | Lettl–Sun: every covering has ≥ 20 primes (superseded by Y5). | PROVED | `C_allE.md` |
| Y7 | Structural lemmas: equal-index lattices sharing a primitive vector are equal; alignment criterion (2-D problem is 1-D iff gcd(e_p,e_q) \| α_pβ_q − β_pα_q pairwise); common discrete log 3 ≡ 2^T mod p reduces to a 1-D covering, (3/p) = (2/p)^T, primes 5 and 13 are incompatible, no common-T covering with e_p ≤ 8000; subgroup (homogeneous) certificates are impossible (Fermat); direction-lemma dichotomy. | PROVED | `C_allE.md` §1, `V_check.md` |

### NO side — every m (or almost every m) has a prime
| # | statement | label | where |
|---|---|---|---|
| N1 | Every m ≤ 10¹⁰ coprime to 6 has a prime 2^k3^l·m+1 with k,l ≥ 1. Hardest m = 6257518159, first prime at (16,10), proved by a Lucas certificate. | VERIFIED | `verdict3/B_noside.md` §6, `search_l1.c` |
| N2 | Erdős–Odlyzko 1979: m with a prime have positive lower density. | literature | `B_noside.md` §2 |
| N3 | **Theorem A (almost-primes).** For x ≥ x₀, all but **2.0%** of m ≤ x coprime to 6 have k,l ≥ 1 with Ω(2^k3^l m+1) ≤ 22; 1.1% at Ω ≤ 23; 0.6% at Ω ≤ 26; 0.57% as Ω → ∞. Method: fundamental lemma (z-rough pair counts are asymptotic, so no parity problem) + Chebyshev/Paley–Zygmund inside classes mod ∏_{5≤p<31} p (exact class data by FFT). Lemma U (box convergence) PROVED by V. ρ enclosed in [1.02751, 1.02820]. | PROVED **conditional on the explicit form of Friedlander–Iwaniec, Opera de Cribro, Lemma 6.3** (error e^(9κ−s)K^10, never opened) and on floating-point sums | `verdict3/D_almostall.md` §0, §11.6 |
| N4 | Covering by-product: for every y, m covered by primes < y have density ≤ 0.58% (exactly 0 for y ≤ 31). | same as N3 | `D_almostall.md` §11 |
| N5 | Romanoff lemma for {2,3}, pair-correlation Lemma D, conductor lemma (real characters of 3-smooth conductor). | PROVED | `B_noside.md` §1–2 |

### Conditional (hypotheses unproved)
| # | statement | where |
|---|---|---|
| C1 | **Theorem C″.** If two aggregate hypotheses hold (stage-range sums of first moments and of squares of the large-prime tail are at most κ_L, κ_Q² times the random-lattice model), then no covering exists at any size. Bound 0.8722 at (κ_L, κ_Q) = (1, 1.34), 0.8858 at (1, 1.5), 0.8571 at the measured per-range κ. Data support κ_Q ≈ 1.34 on primes < 8·10⁵ only. Earlier pointwise versions WITHDRAWN (false in the model, found by V). | `C_allE.md` §5c |
| C2 | Same, with C2's divisibility-class hypothesis H_cls for large stages. | `verdict3/C2_ce.md` |
| C3 | A's version of C1 (same numbers). | `A_certify.md` §3 |

### Withdrawn claims (do not reuse)
- "Uncovered density ≥ 0.2694": B(E) bounds a tilted measure, not uniform density (31 primes with e_p \| 5040 cover 71.7%).
- Theorem A with r0 = 19, and with the old K constants (1.5% at Ω ≤ 22): superseded by N3.
- Pointwise hypotheses H_dens, H_n, per-stage H_L/H_Q.
- `verdict/5_priorart.md` calling #202 solved (it is open). Cremona–Koymans as a covering tool (it is about sublattices).

---------------------------------------------------------------------------------------------------------------------
## 2. What is open, and what would close it

**To settle #203 itself** (neither is in reach of known methods):
- **YES** needs an explicit covering or mixed certificate. Any one must use ≥ 14 082 primes with e_p > 8·10⁵ (Y5), and every literature construction is 1-dimensional with a free multiplier, which #203 does not allow.
- **NO** needs a prime in 2^k3^l·m+1 for every m. That requires beating the parity barrier for a family with only (log x)² members per m; even density one for primes is blocked (Chebyshev ceiling ≈ 0.49 for this method), and density one for almost-primes is as hard as the no-covering problem.

**To close the strongest intermediate theorem, "no covering exists at any size"** (would kill every known YES mechanism):
- needs a bound on c(e) = #{p : e_p = e} (pointwise c(e) ≤ exp(c(log e)^θ), θ < ½, or the aggregate hypotheses of C1). The one-base analogue is an open Erdős conjecture; Minkowski, Möbius/gcd-size and irredundance routes are proved dead (`C2_ce.md`).

**Concrete open items in this project (closable):**
1. Exact-rational B′ for the final δ (`verdict3/C_run_exact.sh`, checkpoint `C_ckpt_final.txt`) → Theorem Z with 14 082 becomes PROVED. (DONE 2026-10-30: cap-0.28 check → 13 184 PROVED.)
2. DONE 2026-10-30: exact-rational B(8·10⁵) = 0.742445. DONE: Theorem E at 8·10⁵ (Y2), V confirmed.
3. Read Friedlander–Iwaniec, *Opera de Cribro*, Lemma 6.3 / Cor. 6.10 (or Halberstam–Richert Thm 2.5) and match hypotheses → Theorem A becomes PROVED. Needs the book (Deepnil may get it via Ashoka).
4. Interval arithmetic on Theorem A's floating sums; independent check of `D_eprimes.c` and the tail τ = 3.2·10⁻⁴.
5. Common-T maximum at E = 300 (C: 0.5627), independent check deferred.
6. Write the #203 paper (.tex + PDF): Y1–Y7, N1, N3–N5, C1 as conditional; add the CRT augmentation lemma to the pure theorem's statement (gap V found in `DISTORTION.md`).
7. Prior-art check for Theorem A (none found; limited search) before any priority claim.

---------------------------------------------------------------------------------------------------------------------
## 3. How to resume (for any future session)

1. `git clone --branch claude/open-conjecture-search-h6tgg3 https://github.com/deepnilray/erdos e203wt`; `pip install gmpy2 sympy numpy scipy`.
2. Gitignored and regenerable: `verdict3/B_E800000.pkl` + `verdict3/stages_E800000.npz` (`python3 verdict3/run_bound.py poolE800000.jsonl 800000 0.578318 200000`, ≈ 40 min, reproduces 0.742445); `verdict3/D_data/` (D's scripts); `/tmp/C_rhoset.pkl` (`C_rhoset.py`).
3. Exact verifiers are resumable from their checkpoint files; each background job dies at 2 h, so restart from the checkpoint. Stages run largest first (cost ∝ size²), so progress by count understates progress by work.
4. Agents used: A (certify), V (check + Lean prompts), C (no-covering), C2 (c(e)), D (almost-all), L (literature), B (no side, run3). Reports: `verdict3/{A_certify,V_check,C_allE,C2_ce,D_almostall,L_literature,B_noside,APPROACHES}.md`.

## 4. Public state (erdosproblems.com/forum/thread/203, read 2026-10-25)
Open, no solution claims (re-read 2026-10-30; page last edited 20 Jan 2026). Also seen 2026-10-30, neither claims a solution: github.com/Neo7672/erdos-203-covering-search (16–17 Sep 2026, budget analysis, plateau 17–21% uncovered) and issue #9414 of the-omega-institute/trureturing (log; 252-row family leaves ≥1.48676% uncovered under a global phase vector). Posted work: |H_p| = lcm of orders and Σ1/|H_p| ≥ 1 (AnimishSharma, Jun 2026); no covering with lcm < 5040 for p ≤ 5·10⁷; covering searches plateau at 71.7% (N=5040), 76.0% (N=55440) (veljjanoski, Sep 2026); shallow search 10¹⁰–10¹¹ (emil467q, Nov 2025). Our Y1 (no lcm condition) is far beyond anything posted; our search range (N1) is not new.

Consolidated literature ledger, audit of this file, level ladder and untried-methods list: `LITERATURE.tex` / `LITERATURE.pdf` (2026-10-30).

## 5. Aristotle (Lean 4 + Mathlib) prompts
Ready statements, all elementary: `verdict3/V_aristotle.md` (AV1–AV9: gcd characterisation of e_p, pool completeness from the gcd certificate, quadratic majorant, tilt weights, Bonferroni, algebraic factorisations, periodic-set lemma, CRT augmentation, intersection constant), `verdict3/B_noside.md` §8 (AP1–AP4: conductor lemma, lattice point count, killed set is a lattice coset, reformulation), `verdict3/C_allE.md` §6 (L1–L4: homogeneous certificates, quadratic-character parity, 5/13 incompatibility, equal-kernel lemma). Send these to Aristotle when the paper is being finalised.

## 6. Run log
- 2026-10-10: five-direction assessment (`verdict/1–5`).
- 2026-10-17/22: scheduled all-agents run; nothing came back (usage limit).
- 2026-10-23: run3, agents A (certify) and B (no side); search to 10¹⁰; l = 0 bug in old search fixed.
- 2026-10-25/26: run4, agents A, C, L, V, then C2, D. Theorem Z (10 300), Theorem A first version, lemmas, dead routes, withdrawals; completeness of the 8·10⁵ pool.
- 2026-10-30 (Friday, scheduled 11:00 IST): container replaced, repo re-cloned, δ regenerated (0.742445 reproduced). C: cyclic price, Theorem Z → 14 082, C″ → 0.8722. D: stratified Theorem A, ρ enclosure; V proved Lemma U and corrected D's sieve constants (2.0% at Ω ≤ 22). Three exact verifiers running.
- 2026-10-30 (afternoon): audit run with independent code (N1 hardest m, pool for p < 3·10⁶ with planted-deletion control, lattice forms, c(e) histogram) all confirmed; 11 arXiv citations opened and corrected; numeric odds removed from VERDICT.md, verdict/1_heuristic.md, TARGET.md; two exact verifiers resumed (C final, V cap 0.28); LITERATURE.tex/pdf written.
- 2026-10-30 (evening): exact-rational B′ for the cap-0.28 δ FINISHED: 0.798372 < 1 (`verdict3/V_verify_cap028.log`, 15 279 checkpoint lines). Y5 with N_Z = 13 184 is VERIFIED exactly (pending V's cross-read of the run); the final-δ check (N_Z = 14 082) is still running (`C_ckpt_final.txt`). Function-field experiment in `ff/` (no covering found, see `ff/README.md`).

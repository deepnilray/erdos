# Agent A (run3): certification of B(8·10^5), Theorem E at 8·10^5, conditional all-E bound

Date 2026-10-23..26. Nothing here settles #203, which stays OPEN. Labels: PROVED (mathematical proof or
exhaustive/exact computation with the stated scope), VERIFIED (computation with a stated bound and a control that can
fail), CONJECTURED (hypothesis or heuristic). No file here was committed. Large binaries (`B_E800000.pkl`, 479 MB) are in `.gitignore`.

## Verdict (summary)

| item | result | label |
|---|---|---|
| Completeness of the pool for levels e in (4·10^5, 8·10^5] | all 400 000 levels pass; 20/20 chunks `certified complete: True`, 0 INCOMPLETE, 247 612 nontrivial G(e) levels divided out to 1 | VERIFIED (gcd route re-run, code independent of the pool builder) |
| Same pool, independent sieve route (no gcd) | every prime p < 2·10^9 with e_p ≤ 8·10^5 matches the pool exactly: 100 802 = 100 802, 0 missing, 0 extra, 0 wrong e | PROVED for p < 2·10^9 (exhaustive) |
| Pool forms (α, β, e) define the right lattice | 100 814/100 814 pass (explicit kernel basis + index argument) | PROVED (exhaustive) |
| B(8·10^5), float | 0.742445 (reproduces agent 3 and the 4·10^5 → 8·10^5 trend) | VERIFIED (float) |
| B(8·10^5), exact rational | EXACT_PENDING | PROVED once the pool is complete (see scope) |
| Theorem E at 8·10^5 | MIXED_PENDING | see section 2 |
| Conditional all-E bound | 0.9833 (+5·10^-4) under H(κ=1, ε=0.85); closes only for κ ≲ 1–1.5 | CONJECTURED hypothesis, VERIFIED arithmetic |
| Push to E = 1.6·10^6 | not done (cost: about 8·10^5 gcds of 1.6·10^6-bit numbers, ≈ 0.15 s each ≈ 35 h CPU, plus factoring) | — |

Scope caveats, all load-bearing:

1. The new certificate covers only levels e in (4·10^5, 8·10^5]. Levels e ≤ 4·10^5 rest on the earlier `certify_pool.py` run
   (HUB/DISTORTION.md, its log `certify400000.log` is git-ignored and not in this worktree) plus the earlier sieve to 10^8. I did not re-run them here.
2. Twelve primes of the new pool exceed 2·10^9 (largest 21 056 375 647). They are covered only by the gcd route, not by the sieve.
3. The gcd route and the pool builder both compute gcd(2^e−1, 3^e−1). The certificate re-divides by pool primes and re-validates every pool prime
   (primality, e_p recomputed with `n_order`), so it checks the builder's factoring, not the gcd arithmetic (GMP). The sieve is the logically independent check.
4. "B(8·10^5) is PROVED" means: the exact-rational verifier reproduces the bound from the pool; the bound then is a theorem for the pool.
   Passing it to "all primes with e_p ≤ 8·10^5" uses the completeness above (scope items 1 and 2).

## 0. Why run_bound_800k.log shows r-source counters all zero

The first (killed) run printed `r-source {'coupled': 8718700, 'minU': 0, 'bonf': 0}`: 8 718 700 coupled terms, 0 fallbacks.
A session reset killed it during the optimiser, after the pickled build `verdict3/B_E800000.pkl` had been written. The rerun reloaded the pickle
(`run_bound.py` now does so if it exists), so the counters, which are filled only inside `build`, stay at zero. The bound is identical (0.742445 in both).
The 4·10^5 log showed coupled=3 321 441 because it was built freshly. All 8 718 700 terms at 8·10^5 were coupled types from the existing 1908-type table
(tag 200000: `types_E200000.json`, `coupled_full_E200000.txt`).

## 1. B(8·10^5)

### 1a. Completeness certificate (levels in (4·10^5, 8·10^5])

`verdict3/certify_range.py LO HI pool1 pool2` follows `certify_pool.py`: for each e in (LO, HI], G(e) = gcd(2^e−1, 3^e−1) divided with multiplicity
by every pool prime with e_p | e must leave 1 (p | G(e) iff e_p | e). It first validates every pool prime (prime, > 3, unique, e_p recomputed).
Run in 20 chunks of 20 000 (`verdict3/run_chunks.sh`, resumable, two drivers on two cores):

```
verdict3/run_chunks.sh 400000 600000 20000 poolE400000.jsonl poolE_400k_800k.jsonl
verdict3/run_chunks.sh 600000 800000 20000 poolE400000.jsonl poolE_400k_800k.jsonl
```
Logs `verdict3/chunks/cert_*.log`; every one ends `RESULT ... certified complete: True`; `grep -l INCOMPLETE` finds none.

Planted control (`--control 60`, `verdict3/control_planted.log`): delete one pool prime at a random level in range; the certificate must leave that prime in
the leftover. Result: **60/60 planted deletions detected**, 5 unplanted levels clean. (A first 40/40 control on a 400-level window also fired.)

### 1b. Independent sieve route

`verdict3/sieve_e2.c` computes e_p = lcm(ord_p 2, ord_p 3) from scratch for every prime 5 ≤ p < 2·10^9 (factor p−1 by trial division, exact orders), no gcd, no pool.
`verdict3/compare_sieve.py`: 98 222 285 primes scanned, 100 802 with e_p ≤ 8·10^5, equal to the 100 802 pool primes below 2·10^9;
range (4·10^5, 8·10^5]: 47 575 = 47 575. Control: dropping one pool prime makes the comparison report it (prime 538621) and `equal: False`.
Log `verdict3/sieve_compare.log`. (The sieve output file is git-ignored.)

### 1c. Forms

`verdict3/audit_forms.py`: gcd(α,β,e) = 1 makes ψ onto Z/e, so ker ψ has index e; its explicit basis (e/g, 0), (c, g) is checked to satisfy 2^k 3^l ≡ 1 (mod p),
and |⟨2,3⟩| = e, so ker ψ equals the true kernel. 100 814/100 814 pass; control (α+1) rejected 400/400.

### 1d. Float bound

```
python3 verdict3/run_bound.py poolE800000.jsonl 800000 0.578318 200000     # 4213 s total
```
`BOUND=0.742445` (poolE800000.jsonl = poolE400000 + poolE_400k_800k, 100 814 primes, light {2,3} mass 0.04850936, α* = 0.626827).
Per-stage costs at 8·10^5: ℓ=5: 0.2400, 6 ≤ ℓ < 30: 0.4116, 30–100: 0.0729, 100–1000: 0.0179, ≥ 1000: 0. δ values 0.34–0.49 for ℓ ≤ 1000.

### 1e. Exact rational

```
VERIFY_CKPT=verdict3/verify_ckpt.txt VERIFY_WORKERS=2 python3 verify_distortion23.py poolE800000.jsonl 800000 \
  5,7,13,17,19,37,73,97,577 delta23r_E800000.json 5,7,13,17,19,37 2770/5184 types_E200000.json coupled_full_E200000.txt
```
(`verify_distortion23.py` now prints `EXACT FRACTION`, can use worker processes and a checkpoint file; the arithmetic is unchanged. Check:
E = 2·10^4 with 2 workers still gives 0.633429.) Tables: the 1908-type tables of tag 200000 cover every type at 8·10^5 (agent 3 and this run: 0 fallback);
types missing from the table would only fall back to larger values, so the result is a valid upper bound either way. The light-mass correction
(1−OPT_h−0.0485)/(1−OPT_h−λ) is applied exactly, as for 4·10^5.

EXACT_RESULT_PENDING

## 2. Theorem E at 8·10^5

MIXED_RESULT_PENDING

## 3. Conditional all-E bound

Numbers from `verdict3/tail_bound.py`, `align_stats.py`, `check_H_n.py`; arithmetic is float, so these are VERIFIED (float), not PROVED.

**What "no covering at any E" means.** A covering is a finite set P of primes, so E = max e_p is finite; the full pool of all primes with e_p ≤ E dominates P
(augmentation lemma). So the claim is sup_E B(E) < 1, where for each E the bound uses the same δ vector.

**Reduction [PROVED, from L1, L3 and 1-Lipschitzness of (x−δ)_+].** Fix δ_ℓ from the 8·10^5 optimum for ℓ < 1000 and δ_ℓ = 1/2 for every ℓ ≥ 1000 (the finite bound stays 0.742445). For every E:
 - stage ℓ ≤ Q0: cost_ℓ(E) ≤ cost_ℓ(8·10^5) + R*/(1−δ_ℓ) · Σ_{p: e_p>8·10^5, P+(e_p)=ℓ} Λ_p/e_p;
 - any stage: cost_ℓ(E) ≤ min over majorants (a·m1 + b·m2)/(1−δ_ℓ) (the code's family), with m1 = Σ Λ_p r_p/e_p, m2 = diagonal + Σ_{p≠q} Λ_pΛ_q r c^<_{pq}/(e_p e_q);
 - here R* = 1/(1−α*) = 2.680 bounds every r, and c^<_{pq} ≤ ℓ-free part of gcd(e_p, e_q).

**The worst-case gcd bound alone cannot close.** With c^< replaced by gcd'(e_p,e_q) the pair term gains a factor ∏_{q<ℓ}(1+4/q) ~ (ln ℓ)^4,
and even with n(e) at exactly its Artin–Kummer model values the total is 22.8 [VERIFIED (float), `tail_bound.py 1.0 1000` with alignment]. So **no hypothesis on n(e) alone suffices for this method**.
Alignment of the forms must be controlled too.

**Hypothesis H(κ, ε) [CONJECTURED].** n̂(e) := 0.813 · (e/φ(e)) / ln(8·10^5), the Artin–Kummer prediction with 1/ln e relaxed to 1/ln E0 (an upper bound for e > E0).
 - (H_n) for e > E0 = 8·10^5, all stage functionals Σ_{p ∈ stage ℓ, e_p>E0} Λ_p/e_p are at most κ times those of n̂;
 - (H_c) in every stage the alignment excess is at most ε: Σ_{p≠q} w_p w_q (c^<_{pq}−1) ≤ ε (Y_1² + Y_1/ℓ), w_p = Λ_p/e_p, Y_1 = Σ w_p.

**Theorem (conditional).** Under H(κ, ε): B(E) ≤ T(κ, ε) for all E, with the following values of T (sums over ℓ < 3·10^6; the rest is < 5·10^-4 by the ℓ^-2 decay of the last terms):

| κ | ε | T |
|---|---|---|
| 1.0 | 0.00 | 0.8748 |
| 1.0 | 0.50 | 0.9386 |
| 1.0 | 0.85 | 0.9832 |
| 1.0 | 1.00 | 1.0024 (fails) |
| 1.2 | 0.30 | 0.9639 |
| 1.5 | 0.00 | 0.9811 |
| 2.0 | 0.00 | 1.1156 (fails) |
| 0.8 | 1.00 | 0.9332 |

So the method closes iff roughly κ ≲ 1.5 at ε = 0, κ ≲ 1 at ε ≈ 0.9. The per-stage minimum chooses the linear tail bound for ℓ ≲ 30 and the second-moment bound above.

**Data check [VERIFIED].**
 - Alignment excess (all stages with ≥ 2 primes, e ≤ 8·10^5): max 0.85, mass-weighted means 0.17–0.33 by ℓ bucket (`align_stats.py`), so ε = 0.85 holds on the data.
 - Stage masses against n̂ on the top half of the range (4·10^5, 8·10^5]: ratio 1.37 (P+<7, mass 3·10^-5), 1.17 (7–30), 1.12 (30–100), 1.02 (100–1000), 0.99 (1000–10^4), 0.94 (≥ 10^4), total 1.006
   (`check_H_n.py`; on (2·10^5, 8·10^5]: total 1.031). So κ ≈ 1.0–1.2 on the data, which sits at the edge of what the proof tolerates. There is real slack only because the data decay like 1/ln e while H_n uses 1/ln E0; I did not exploit this.

**Closest known results.** None implies H. Bugeaud–Corvaja–Zannier (Math. Z. 243, 2003) gives log gcd(2^e−1, 3^e−1) ≤ εe, hence n(e) ≤ εe/ln e: a power of e short of any bound of the shape needed.
GRH-conditional Kummer/Artin counts for the two-generator group ⟨2,3⟩ control primes up to index about p^{1/6}–p^{1/4} and are averages over p, not statements about the smooth levels e that H needs; Romanoff-type convergence (Σ 1/(n·ord_n a) < ∞) is of the same family and also does not give H.
H_c (non-alignment of directions in P¹(F_q)) has no known proof either.

## Aristotle prompt

Formalise and prove (Lean 4 + Mathlib). Definitions: for a prime p with p ≠ 2, 3, work in `(ZMod p)ˣ`; let `e := Nat.lcm (orderOf (2 : ZMod p)) (orderOf (3 : ZMod p))`.
Let `S : AddSubgroup (ℤ × ℤ) := { x | (2 : ZMod p) ^ x.1 * (3 : ZMod p) ^ x.2 = 1 }` (integer powers in the unit group).
Theorem A: `S.index = e` (for `p` prime, `p ≠ 2`, `p ≠ 3`).
Theorem B: for every `m : ℤ` and all `(k,l)`, if `p ∣ 2^k * 3^l * m + 1` for natural `k l` then `{(k',l') : ℕ × ℕ | (p : ℤ) ∣ 2^k' * 3^l' * m + 1}` equals the intersection of `ℕ × ℕ` with a coset `(k,l) + S` (i.e. `(k',l')` belongs iff `(k'−k, l'−l) ∈ S`).
Theorem C (kernel basis used in `audit_forms.py`): if `α β : ℤ` with `Int.gcd (Int.gcd α β) e = 1` describe a surjective homomorphism ψ(k,l) = αk+βl mod e whose kernel is contained in S and `[ℤ² : ker ψ] = e`, then `ker ψ = S`.
Optional Theorem D (inequality used in L3): for reals `x ≥ 0`, `δ > 0`: `max (x − δ) 0 ≤ x^2 / (4 * δ)`.

## Files

`verdict3/`: `certify_range.py`, `run_chunks.sh`, `chunks/cert_*.log`, `control_planted.log`, `sieve_e2.c`, `compare_sieve.py`, `sieve_compare.log`, `audit_forms.py`, `run_bound.py`, `run_bound_800k.log`,
`stages_E800000.npz`, `run_verify.sh`, `verify23_800k.log`, `tail_bound.py`, `align_stats.py`, `check_H_n.py`. Repo: `poolE800000.jsonl`, `delta23r_E800000.{npy,json}`; edited `verify_distortion23.py`, `verify_mixed.py` (parametrised, defaults reproduce 4·10^5), `.gitignore`.

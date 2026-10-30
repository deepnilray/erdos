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
| Conditional all-E bound (aggregate H_L, H_Q) | 0.904 at κ_Q² = 1.44, 0.928 at κ_Q² = 1.8 (data level), 0.963 at κ_Q² = κ_L² = 2.25 | hypotheses CONJECTURED; bound VERIFIED (float, C's run) |
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

**Status 2026-10-30: PENDING.** The container was replaced and the git-ignored `delta23r_E800000.json` was lost. The head session is
regenerating it (`verdict3/run_bound_800k_regen.log`) and will start `verdict3/run_verify.sh` once the regenerated δ reproduces 0.742445.
- **Checkpoint decision.** The 22 stage costs from the old run (`verify_ckpt.txt`) can no longer be tied to the old δ file, and mixing stage
  costs from two δ vectors is not a valid bound (one global δ is required). So I moved the checkpoint aside to `verdict3/verify_ckpt.old_delta.txt`,
  and the run recomputes from scratch.
- **Cross-check after the run.** Compare the overlapping stages of the old and new checkpoints line by line. Equality is evidence that the
  regenerated δ matches the old one, but it is not used in the bound.
- **Guard.** `run_verify.sh` now records sha256 of the δ file and refuses to resume a checkpoint if the file has changed.

## 2. Theorem E at 8·10^5

**Status: PENDING the exact fraction.** `verify_mixed.py` is parametrised: `verify_mixed.py POOL E DELTA B_EXACT`; with no arguments it
reproduces the 4·10⁵ run. Run `verdict3/run_mixed.sh` once `verify23_800k.log` shows `EXACT FRACTION:`. The script takes that fraction,
records the δ sha256 and runs
`verify_mixed.py poolE800000.jsonl 800000 delta23r_E800000.json <fraction>` → `verdict3/mixed_800k.log`.

What the 8·10⁵ run changes compared with 4·10⁵:
- the λ′ in R3 uses the 8·10⁵ light mass (0.04850936, larger, so R3 is conservative);
- S sums over 5 ≤ q ≤ 8·10⁵ with the 8·10⁵ δ;
- the tail term becomes 1/(8·10⁵ − 1).

The same δ file must be used for B and for S, and the script enforces this by using one path.

Expected size (not yet a result): B ≈ 0.7424, S ≈ 0.146–0.15, R3 ≈ 0.076. That gives about 0.89 for 3 ∤ g and about 0.97 for 3 | g, which is below 1 but with a thinner
margin than at 4·10⁵ (0.953).

## 3. Conditional all-E bound (restated with aggregate hypotheses, 2026-10-30)

**Status: hypotheses CONJECTURED; the implication is proved modulo float arithmetic (bound VERIFIED, float). It does not settle #203.**

**Withdrawn.** My first version (2026-10-24) assumed (H_n) "every stage functional of n is ≤ κ times that of n̂" plus a per-stage
alignment cap ε. V showed (V_check.md §3.4) that the pointwise-in-d form of such density hypotheses is false even in the Poisson model it
was calibrated on: a single realised e beats the expected mass of all multiples of d. My H_n quantified over the same functionals, so it is
withdrawn, and so is its table (0.8748 … 1.0024). Two findings survive. (i) With worst-case alignment c^<_pq = gcd′(e_p, e_q) the method
gives 22.8, so **no hypothesis on n(e) alone suffices; alignment must be controlled** [VERIFIED, float]. (ii) The alignment excess on the data
is small (max 0.85 per stage in my normalisation; C's Lemma M model fits the pair sums to within 6%).

**What the proof uses** (C_allE.md §5b, Theorem C′; the reduction is the one in my first version: δ fixed from the 8·10⁵ run for ℓ < 1000,
δ = ½ for ℓ ≥ 1000, then L1 + L3 + 1-Lipschitz). For each stage ℓ ≥ 5, only two aggregates of the tail e > E₀ = 8·10⁵ enter:
- the first moment Y₁^>(ℓ) = Σ_{e>E₀, P⁺(e)=ℓ} n(e)Λ(e)/e;
- the sum of squares Q^>(ℓ) = Σ_d θ(d)(Y_d^>)², where Y_d^> is the same sum restricted to d | e/ℓ^{v_ℓ(e)} and θ(d) = ∏_{q|d}(q−1)/(q+1).

The model values Y₁^mod and Q^mod come from n̂(e) = τ·e/φ(e) with τ = 0.813/ln E₀. This is the Artin–Kummer prediction with 1/ln e relaxed to 1/ln E₀.

**Hypotheses.**
- H_L(κ_L): Y₁^> ≤ κ_L·Y₁^mod for every ℓ.
- H_Q(κ_Q²): Q^> ≤ κ_Q²·Q^mod for every ℓ (the squares may exceed the model by the factor κ_Q²).
- H_align(0): pair sums take the random-form (Lemma M) value.

The pool–tail cross term is bounded by Cauchy–Schwarz, so no mixed hypothesis is needed.

**Theorem (conditional).** Under H_L(κ_L), H_Q(κ_Q²) and H_align(0), no finite set of primes covers, so no pure covering certificate exists
at any E. The bounds below come from C's `C_tail.py … tailonly` (`C_tailQ_grid2.log`); stages ℓ < 3·10⁶ are summed and the remainder is about 4·10⁻⁵.

| κ_L | factor on squares κ_Q² | bound |
|---|---|---|
| 1.0 | 1.00 | 0.8719 |
| 1.0 | 1.44 | 0.9038 |
| 1.0 | 1.80 | 0.9280 |
| 1.2 | 1.80 | 0.9303 |
| 1.0 | 2.25 | 0.9574 |
| 1.5 | 2.25 | 0.9633 |

**A factor of up to 1.4 on the squares closes with margin: at κ_Q² = 1.44 and κ_L = 1 the bound is 0.904 < 1.** It still closes at κ_Q² = 2.25.
I did not recompute these numbers in this container. The 8·10⁵ stage file and build pickle were lost with the old container, and both cores
are busy. They are C's numbers, VERIFIED (float). My own earlier run with c = 1 and ε = 0 gave 0.8748 at κ = 1. That is consistent with C's 0.8719,
up to the different cross-term treatment.

**Data check [VERIFIED; C_testQ.py, C_testH.py, my check_H_n.py].** On the out-of-sample windows (E₁, 8·10⁵]:
- First moment: the total ratio is 1.006 on (4·10⁵, 8·10⁵], with buckets 0.94–1.37. The 1.37 bucket (ℓ = 5) carries only 3·10⁻⁵ of the mass.
- Squares: the total ratio is 1.25–1.30, rising to 1.77 in the ℓ < 12 buckets.

**So the data do not satisfy H_Q(1.44) in the small-ℓ buckets. They support κ_Q² ≈ 1.8 (bound 0.928, margin 7%), not 1.4.** The ratios do not
shrink as E₁ grows, and an independent-Poisson model of n(e) does not reproduce them (the data are over-dispersed). Extending H to all
e > 8·10⁵ is therefore an assumption with no theoretical support.

**Closest known results.** None implies H_L or H_Q.
- Bugeaud–Corvaja–Zannier (2003) give log gcd(2^e−1, 3^e−1) ≤ εe for large e (ineffective). That yields only n(e) ≤ εe/ln e, a power of e too weak.
- GRH-conditional Kummer/Chebotarev counts for ⟨2,3⟩ (Cangelmi–Pappalardi 1999 and successors) give averages over p, up to index about
  x^{1/30} (published), not bounds on n(e) at smooth levels e.
- Nothing is known about the alignment statistics.

The weakest clean form of what is needed is a square-sum bound on n(e) along multiples of d inside each P⁺-stage, uniform in ℓ. As far as
I know, no GRH-conditional theorem implies it.

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

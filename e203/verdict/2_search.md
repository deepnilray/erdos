# Agent 2: direct computational search for a YES candidate (Erdős #203)

All code and logs are in this directory: `search.c` (main C search), `fam.py` (sieve and PRP tools, gmpy2),
`control.py`, `obvious.py` / `obvious_pp.py`, `hard.py`, `construct.py`, and the `*.log` files.
CPU used: about 47 single-core minutes, with one heavy process at a time.

## Verdict

**No computational sign of a YES m.** Every m found a prime quickly. The record first-prime size grows like a
smooth power of N, with nothing anomalous. Heuristically this favours **NO** for every m that is not a
covering. It cannot exclude a covering m, which would be astronomically large (see the repo's DISTORTION.md).
This search therefore speaks only to "no small or accidental m". [CONJECTURED]

## 1. Main search, m ≤ 3·10⁹

`search.c` works as follows. For each m coprime to 6 it walks (k,l) in increasing order of s = 2^k·3^l. It
sieves the first 256 candidates with bitmasks for the 62 primes 5..307, and treats k=0 as even. It then runs
Miller–Rabin with Sinclair's 7 bases, which is deterministic for n < 2^64, so the primes found are
**proved** prime. Any m with no prime below 2^64 is printed as a SURVIVOR for gmpy2 to handle.

- **[VERIFIED, m ≤ 3·10⁹]** All 10⁹ values of m coprime to 6 with m ≤ 3·10⁹ have a prime 2^k3^lm+1 with
  2^k3^l ≤ 805306368 (< 2^29.6). There were 0 survivors. The run made 2.33·10⁹ MR calls in 1611 s.
- **Record m = 2970893047** (prime). Its first prime is at **k=28, l=1**:
  n = 2^28·3·2970893047+1 = **2392479089396023297** (19 digits). The prime is the 301st (k,l) in size order,
  and log2 n = 61.05. It is PROVED prime: deterministic 64-bit MR, sympy.isprime, and MR bases 7 and 11 agree.
- Record chain (m: k,l): 237983: 2,9 · 1467397: 9,5 · 2199587: 1,11 · 5838871: 17,1 · 6913051: 15,3 ·
  7497953: 6,10 · 7728803: 22,1 · 100831399: 8,10 · 372469021: 12,8 · 591092197: 21,3 · 1275536711: 13,9 ·
  1323982369: 4,15 · 2970893047: 28,1. All of these first primes are sympy-proved.
- Distribution of the first-prime size, as P(log2 s ≥ b) over the 10⁹ m: b=4: 0.60, 8: 0.096, 12: 6.3e-3,
  16: 2.2e-4, 20: 4.8e-6, 24: 6.9e-8, 27: 5e-9, 29: 1e-9. The tail is **super-exponential**: the fit is
  ln P ≈ −0.014 b² − 0.43 b. That is the shape the random model predicts, since the number of candidates
  grows ∝ b², so P(no prime up to s) ≈ exp(−c·(log s)²/log m).
- Growth fit over the 22 records with m ≥ 10³: **ln s_rec ≈ 0.99 ln N − 1.6**, so s_rec ≈ 0.2·N and
  n_rec ≈ N². (ln s)²/(ln N·ln(Ns)) drifts slowly from 0.34 to 0.46. Extrapolating, the record s is about
  2^34 at N=10¹¹, consistent with the forum's [10¹⁰,10¹¹] finding nothing; about 2^47 at 10¹⁵; about 2^63 at
  10²⁰. This growth is polynomial and smooth, with no plateau and no outlier.
- **Correctness checks.** On m ∈ [1,30000] and [123456789, 123556789], the per-m first-prime histograms from
  C match an independent gmpy2 brute force exactly. They also match on [10¹²,10¹²+2·10⁴]. At 3·10¹⁵ they
  match up to the documented 2^64 cutoff, beyond which C correctly reports survivors. *This cross-check
  caught a real bug*: a uint8 overflow in the sieve table for p > 255. It was fixed before the main run.

## 2. Are the hardest m covering-like? (`hard.py`, `hard.log`)

For the last 12 record m, I compared each against random m of the same size.
- Fraction of [0,200]² killed by primes p < 10⁴: 0.83–0.86. The random baseline is 0.822 ± 0.029, so z is
  between +0.2 and +1.3. **Globally the record m are ordinary.**
- Fraction of the *searched window* (cells with 2^k3^l < s_found, k ≥ 1) killed by p < 10⁴: 0.90–0.95.
  The random baseline is about 0.83 ± 0.03, so z is between +2 and +3.5. The remaining ~10–25 unsieved
  candidates were all composite through larger factors.
- The heavy primes are always the generic small-e_p ones: 5 (e=4), 7 (6), 11 (10), 23 (11), 13 (12),
  17 (16), 19 (18), 29 (28). None of them is special to a given m.
- **Conclusion:** the records are local bad luck in a small window. They show no covering structure. All of
  them already had proved primes, so there was nothing to push further.

**YES-direction probe (`construct.py`).** I built m by CRT so that each small-e_p prime kills a greedy-best
coset of a box. The aim was to manufacture the most covering-like m possible and then push it.
| primes used (e_p ≤) | Σ1/e | box covered | m digits | first-PRP log2 s: constructed (mean / max) | random m of the same size |
|---|---|---|---|---|---|
| 60 (20 primes) | 1.15 | 76% of log2 s ≤ 128 | 37 | 14.4 / 18.8 | 11.5 / 21.0 |
| 400 (105) | 1.63 | 92.8% of ≤ 128 | 252 | 50.2 / 108.9 | 21.5 / 44.8 |
| 2000 (258) | 1.85 | **100%** of ≤ 128 | 733 | 138.5 / 162.7 (30 trials) | 39.7 / 98.5 |
| 8000 (631, p < 10⁶) | 2.05 | **100%** of ≤ 256 | 2078 | 299.6 / **359.1** (6 trials) | 82.9 / 175.1 |

Full coverage of a finite box is easy. For the e_p ≤ 2000 case I re-checked it independently with gcd: 0 of
5192 cells escape. The prime nevertheless appears **just outside the box**, at log2 s ≈ 128–163 and
≈ 256–359 respectively. The most resistant family I found is the e_p ≤ 8000 construction. Its trial 2 first
gives a PRP at **k=142, l=137** (log2 s=359.1, 1852 PRP tests), n ≈ 2190 digits; this n is BPSW-PRP only and
was not re-tested. For the e_p ≤ 2000 case I re-tested two first PRPs (775 and 773 digits) with BPSW, MR
bases 7 and 11, and gmpy2.is_prime(25). All agree, but these remain [PRP], not proved. m is saved in
`constructed_m_trial*.txt`. This matches the repo's result that a full torus covering is far out of reach.

## 3. Obvious candidates (`obvious.log`, `obvious_pp.log`, `izotov.log`)

All primes in this section are sympy-proved.
- **Sierpiński numbers.** Each has a prime with tiny (k,l): 78557: (1,2)→1414027 · 271129: (3,1) ·
  271577: (1,3) · 322523: (1,1) · 327739: (2,1) · 482719: (1,2) · 575041: (2,2) · 603713: (1,1) ·
  903983: (3,1) · 934909: (4,2)→134626897 · 965431: (2,2). For all 11, the l=0 row (k ≤ 400) has no prime,
  as expected, and that doubles as a detector check.
- **Riesel numbers** 509203, 762701, 777149, 790841, 992077 give primes at k ≤ 5, l ≤ 2.
- **Perfect powers M^g**, for g ∈ {2,3,4,5,6,12} and every M < 200 coprime to 6 (66 values of M per g):
  all have primes. The hardest is 107⁵ at (9,6), log2 s=18.5; next is 157¹² at (12,4).
- **Izotov's perfect-power Sierpiński number** 44745755⁴ = 4008735125781478102999926000625 (coprime to 6):
  its l=0 row has no PRP for k ≤ 1000, but **6m+1 is prime** (k=l=1, 32 digits).

## Controls (the detector can fire)

- Negative control: for 78557·2^k+1 with l=0 and k ≤ 2000, a direct BPSW test of all 2001 numbers finds 0 PRPs.
  The sieve kills all 2001, the covering {3,5,7,13,19,37,73} hits every k, and `first_prime(l0only)` returns
  None. In C, the l=0 mode reports 78557 and 271129 as SURVIVORs.
- Positive control: 78559 with l=0 has a PRP at k=546. *This control caught a second bug*: the l0only branch
  iterated an empty range, which made the negative control pass vacuously. It was fixed and rerun.
- Label legend: [PROVED] means a deterministic test (n < 2^64, or sympy); [PRP] means BPSW plus extra MR bases;
  [VERIFIED, bound] means exhaustive within the stated bound; [CONJECTURED] means a heuristic extrapolation.

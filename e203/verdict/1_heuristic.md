# Erdős #203: the probabilistic (Cramér / Bateman–Horn) model, agent 1

**Verdict: NO is much more probable** (no m with gcd(m,6)=1 makes every 2^k·3^l·m+1 composite). Confidence about **95%**.
Under the model, YES requires a local obstruction of density exactly 0, which in practice means a covering. Such a covering
would need primes with e_p > 4·10⁵, which the repo has not excluded. The model cannot price that option, and it is the
whole of the remaining 5%. The model passes every data check I ran, after one correction (§4.4). Its first version failed
the perfect-power control. I report that failure below and explain how it was fixed.

Scripts and data are all in this directory and use the `h_` prefix. Labels: [PROVED] means a rigorous argument;
[VERIFIED, bound] means computed exactly up to the stated bound; [CONJECTURED] means a heuristic or model statement.

---

## 1. The model and its growth law

Fix m. Write N = N_{k,l} = 2^k3^lm+1 and H_p = ⟨2,3⟩ ⊂ 𝔽_p^×, with e_p = |H_p| = lcm(ord_p2, ord_p3) and index i_p = (p−1)/e_p.

**Local densities [PROVED].** The map ψ_p:(k,l) ↦ 2^k3^l mod p is a surjective homomorphism ℤ² → H_p. So
{(k,l) : p | N} is empty or one coset of a lattice of index e_p. It is nonempty iff −m^{−1} ∈ H_p, iff (−m)^{e_p} ≡ 1 (mod p).
So ν_p(m) = δ_p/e_p with δ_p ∈ {0,1}. For p = 2, N is even iff k = 0. For p = 3, only the line l = 0 can be hit.
- If H_p = 𝔽_p^× (index 1), then ν_p = 1/(p−1) for every m with p ∤ m. These primes do not depend on m.
- Only index > 1 primes carry m-dependence. The first ones are p = 23 (e = 11), 47, 71, 73, …
- Averaged over m mod p, E[(1−ν_p)/(1−1/p)] = 1 exactly. So the mean of C over m is 3: the factor 2·(3/2) comes from
  p = 2, 3. The search found mean 3.000000 [VERIFIED, m < 10⁷].

**Model [CONJECTURED].** P(N prime) = ∏_{p≤z} 1[p∤N]/(1−1/p) · 1/ln N, which is a sieve to z followed by Cramér.
Averaged over (k,l), this gives E_m(X) = C(m)·G(m,X). Here C(m) = lim_z dens{(k,l) : no p≤z divides N}·∏_{p≤z}(1−1/p)^{−1},
and G = Σ_{k≥1, l≥0, N≤X} 1/ln N.

Two versions of C(m) are used below:
- **C_exact** is the exact joint density, which includes the lattice correlations.
- **C_ind** = 3∏_{p≥5}(1−ν_p)/(1−1/p) is the independence Euler product.

**Growth.** Let T = ln(X/m) and L = ln m. Then
- **2D:** G ≈ [T − L·ln(1+T/L)]/(ln2·ln3) → ln X/(ln2 ln3), so E_m(X) ~ 1.313·C(m)·ln X.
- **1D** (2^k m+1): G₁ ≈ ln(1+T/L)/ln2, so E ~ (C₁/ln2)·ln ln X.

**Why 2D is so much richer in primes.**
1. *Candidate count.* The set {2^k3^l} below X has ≈ (ln X)²/(2 ln2 ln3) elements, against ≈ ln X/ln2 for {2^k}. Each
   candidate is prime with probability ~C/ln N. So the 2D sum is Σ_t (t/(ln2 ln3))·(1/t) ~ ln X, while the 1D sum is
   Σ 1/k ~ ln ln X.
2. *Weak sieve.* In 1D the obstruction sets are progressions mod ord_p(2). Small orders are plentiful:
   Σ_{ord_p(2)≤20} 1/ord = 2.02 [VERIFIED], and the sum is ≥ 6.1 by order 1000. That is why a 7-prime covering works for
   78557. In 2D a prime needs p | gcd(2^e−1, 3^e−1) to have e_p = e. Here Σ_{e_p≤E} 1/e_p is only 0.52 at E = 10, 1.26 at
   100, 1.83 at 10³ and 2.79 at 4·10⁵ (repo pool, [VERIFIED]). It grows like about 1.5·ln ln E, mostly from "generic"
   primes with e_p ≈ p. Those act exactly like Mertens sieving, which the Cramér factor ln N cancels.
3. *Forced overlaps.* The 2D lattices overlap in ways the residue choices cannot avoid (DISTORTION.md). The local
   factor therefore stays far from 0. See §2.

## 2. Values of C(m)

**Convergence check** (C_ind with p ≤ 10³ / 10⁴ / 10⁵ / 10⁶), for 6 random m ∈ [10⁸,10⁹): 2.610/2.612/2.611/2.610,
2.388/2.370/2.370/2.371, …. The product converges to about 0.1% [VERIFIED for those m].

**Exhaustive search over m < 10⁷** (3.33M values coprime to 6; `h_minsearch.py`, `h_core.py`, `h_cexact.py`):

| quantity | value |
|---|---|
| C_ind, min / 1% quantile / median / 99% quantile / max | 2.168 / 2.367 / 2.850 / 4.513 / 6.163 |
| min C_ind, refined to p ≤ 10⁶ | **2.1753** (m = 680293) |
| exact torus correction for the heavy core {5,7,13,17,19,37,73,97} on (ℤ/144)²: ratio ρ = exact/independent | 0.927 to 1.107 (mean 1.0000) |
| **min C_exact** (box sieve z = 1000 plus tail; best of 300 candidates) | **≈ 2.00** (m = 714739); also 8085799: 2.016 |
| random m: C_exact/C_ind | 0.9945 ± 0.0044 |

**Sierpiński numbers in 2D.** C_ind = 2.786, 2.463, 2.757, 2.485, 2.915, 2.614, 2.923, 3.026, 2.539, 2.584, all typical.
Their 1D covering primes {3,5,7,13,19,37,73} are almost all index-1 primes in 2D, where ν_p does not depend on m.

**The floor.** Choose the best residue at every p ≤ y. Then inf C_ind = 3∏(1−1/e_p)/(1−1/p): 2.06 (y = 10³), 1.80 (10⁴),
1.57 (10⁵), 1.39 (10⁶). The typical size of m needed to reach this floor is 10^17.5, 10^136, 10^1168 and 10^9880 respectively
[VERIFIED for the product; the size of m is a heuristic count]. So C → 0 is possible only like (ln y)^{−0.57}, that is,
for log log m enormous. For any m of reasonable size, C ≥ about 1.3 [CONJECTURED]. **A small C can come only from an
exact structured covering, never from accumulated bad luck at independent primes.**

**What the minimum implies.** At C ≈ 2.0 the expected counts are: 237 primes ≤ 10⁶⁰, 465 primes ≤ 10¹⁰⁰, and ~5900
primes ≤ 10¹⁰⁰⁰. Observed for m = 714739: **468 primes ≤ 10¹⁰⁰, with 470 predicted.**

## 3. P(no prime) and sums over m

The model has passed the tail test in §4.5, so I use P(no prime with N ≤ X | m) ≈ exp(−E_m(X)) [CONJECTURED].

- **Each m has E = ∞, so P(no prime ever) = 0.** In both 2D and 1D, every m with C(m) > 0 has E_m(∞) = ∞. By
  Borel–Cantelli, P(no prime ever) = 0. Hence Σ_{m: C>0} P = 0. Every YES witness, in either dimension, must therefore have
  C(m) = 0, which means a covering, possibly infinite. The difference between 1D and 2D lies in how fast this happens.
- **1D survival does not decay in m.** P(no prime ≤ m^A) ≈ A^{−C₁/ln2} for every m. For C₁ = 1.5 that is 0.23 at A = 2,
  0.097 at A = 3 and 0.032 at A = 5. A fixed fraction of all m survive to any polynomial height, so the sum over m diverges
  linearly. Finite search therefore never makes 1D Sierpiński numbers implausible. Data: 1,850 of 100,000 m in (10⁵, 4·10⁵)
  have no prime 2^k m+1 with k ≤ 300.
- **2D survival decays as a power of m.** P(no prime ≤ m^A) ≈ m^{−κ(A)·C}, with κ = ((A−1) − ln A)/(ln2 ln3):
  κ(2) = 0.403, κ(3) = 1.184, κ(5) = 3.139. With C ≥ 2.07, Σ_{10⁵<m<10⁶⁰} P(no prime ≤ m³) = **3.5·10⁻⁸**. Even at the
  floor value C = 1.39 the sum is 6·10⁻⁴. For A = 5 it is 10⁻²⁸ to 10⁻¹⁸.
- **Small m are all settled** [VERIFIED, m < 4·10⁵]. Every m < 4·10⁵ coprime to 6 has a prime N < m^{1.93}. The worst case
  is m = 2657, with 2^9·3·2657+1. So the finite-height version of "a non-covering counterexample exists" has model
  probability ≤ 10⁻³, and realistically ~10⁻⁸.
- **Far out, at a fixed height.** For m ~ 10⁹, P(no prime ≤ 10⁶⁰) ≈ e^{−211} in 2D, against ≈ 0.017 in 1D.

## 4. Data tests (gmpy2.is_prime, single process, about 25 CPU-minutes in total)

1. **S1: 10,000 random m ∈ [10⁶, 10⁹), values ≤ 10⁶⁰.** Actual 3,138,169 primes; model 3,137,569 (z = 1000 exact sieve plus
   tail). **Ratio 1.0002 ± 0.0006** [VERIFIED].
   - The local factor matters. Binned by C_ind, (Σ actual)/(Σ G) runs 2.442, 2.582, 2.756, 3.027, 3.500, 4.069 against mean
     C = 2.440, 2.582, 2.752, 3.026, 3.501, 4.075.
   - The regression actual/G = 0.015 + **0.995**·C_ind; the model's slope is 1. The correlation is 0.933.
   - z-scores have mean 0.004 and sd 0.905, so the counts are slightly sub-Poisson. The lowest count is 195 (E = 228).
2. **S2: values ≤ 10¹⁰⁰.**
   - Sierpiński ×10: 6,426 actual vs 6,356 predicted (1.011 ± 0.013). Each has 572 to 698 primes.
   - Lowest-C ×40: 0.9885 ± 0.0072. Highest-C ×40: 1.0017 ± 0.0043. Random ×40: 1.0004 ± 0.0060.
   - The independence model E1 is off by 7.5% on the lowest-C group, while C_exact is correct. Lattice correlations are
     real and matter.
3. **Control 1 (could fail; fires as required).** 1D, 2^k·s+1 for each of the 10 Sierpiński numbers s: the model predicts
   **exactly 0** survivors for k ≤ 199 (covering), and the actual count is 0. The independence product C₁,ind
   (0.82 to 1.16) does **not** fire: it predicts about 4 primes each. So C(m) must be defined as the exact joint density,
   and the independence product is not enough. 1D random ×3000: 12,645 actual vs 12,672 predicted (0.998).
4. **Control 2 (perfect powers): first version FAILED.** The test used 332 cubes M³ and 20 fifth powers. Model v1 used the
   unconditional ν_p beyond z. It predicted 103,622 primes for the cubes, against 109,277 actual: **ratio 1.0546 ± 0.003,
   a 17σ failure.**
   - The unconditional Euler product for m = M^q also seemed to drift to 0 like (ln P)^{−c}, with c ≈ 0.10 (cubes), 0.16
     (g = 105) and 0.31 (m = 1). That suggested a thin YES mechanism.
   - **Diagnosis [PROVED, a short computation].** Within a class (k,l) mod q, 2^k3^l runs over one coset of the q-th
     powers. For p ≡ 1 (mod q), one third of the hits fall in the algebraic class qℤ², which is already composite. The
     excess hits of index-q primes also land there.
   - **Model v2** computes ν_p conditional on (k,l) ∉ Alg(m). Its product converges: for m = 125 it is 1.3224, 1.3339,
     1.3347 at P = 10³, 10⁴, 10⁵. For cubes it gives **1.0024 ± 0.006**, and for fifth powers 0.997 ± 0.012 [VERIFIED].
     The apparent drift was an artefact, so there is no hidden YES mechanism in perfect powers.
5. **Waiting-time / tail test.** This is the exact discrete Poisson time change, a randomised PIT that must be Uniform(0,1).
   - 2D: 100,000 m ∈ (10⁵, 4·10⁵), deciles flat (χ²₉ = 8.9). The top 0.1% holds 89 values, against 100 expected.
   - 1D: χ²₉ = 15.6, top 0.1% holds 100 against 100 expected.
   - So the model's P(no prime up to height h) is right out to probabilities of 10⁻³ [VERIFIED].

## 5. Interpretation and residual risk

The model is quantitatively correct to 0.06% in aggregate, tracks the m-dependence of C(m) with slope 0.995, and gets the
survival tail right. Under it, YES ⇔ some m has C_exact(m) = 0. For that, the (k,l) plane must be covered exactly by
finitely many primes, or by infinitely many with density → 0 faster than 1/ln z.
- Finite coverings with e_p ≤ 4·10⁵ are excluded [PROVED in the repo, including mixed algebraic ones].
- Over all residue choices, the independence product reaches 0 only in the limit y → ∞, at rate (ln y)^{−0.57}.
- No exact covering appeared among all m < 10⁷. The minimum is C ≈ 2.0, about 2/3 of the mean.

The residual uncertainty is the existence of an exotic covering built from primes with large e_p. That is a combinatorial
question about which the model says nothing.

**Surprises.**
- The min-C m are boring: C ∈ [2.0, 6.2] over all m < 10⁷.
- The Sierpiński numbers are completely generic in 2D.
- The apparent "(log X)^{1−c} thinning" for perfect powers was real in model v1 but did not survive the data test. Model v2
  fixes it.

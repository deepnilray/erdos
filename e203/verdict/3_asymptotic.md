# Agent 3: can a covering use large e_p? (asymptotics of the 2D distortion bound)

Scratch work, scripts and logs: `scratchpad/agents5/a3/` (driver.py, stats.py, artin2.py, lam.py, lamfit.py,
missing.py, align1d.py, align_sup.py, backtest.py, stagean.py, `stages_E*.npz`, `drv_*.log`). No repo files were changed.

## Verdict
**NO (no such m) is the more probable answer.** Getting YES through a covering would need the distortion bound
to reach 1 at some point. On every model that survives a back-test it levels off at about 0.79–0.85 and never reaches 1.
The only YES route ever used (a Sierpiński-type 1D covering) is structurally useless here. My estimate is
P(YES via covering) ≲ 5%. [CONJECTURED]

## 0. New computed value: B(8·10⁵)
- I ran the repo pipeline unchanged (my `driver.py` is the `__main__` of `distort23r.py` plus per-stage dumps). Inputs: pool = poolE400000 ∪ poolE_400k_800k
  (100 814 primes), heavy core 0.578318, type tables tag 200000. Every term found a coupled type (8 718 700 coupled, 0 fallback), so all
  types at 8e5 are among the existing 1908. λ = 0.0485094.
- **B(8·10⁵) = 0.742445 → no covering with all e_p ≤ 8·10⁵.** [VERIFIED, bound: float pipeline only. It has not been re-verified in
  exact rationals, and it is conditional on completeness of the 4e5–8e5 pool, which is uncertified by a second route.]
- Reproduced the known values exactly: 0.633429 (2e4), 0.715690 (2e5), 0.730584 (4e5). New intermediate points:
  **0.673161 (5e4), 0.697867 (1e5)**.
- Run time: 6 + 31 min single-threaded for 8e5.

## 1. Prime statistics (task 1)
| E | #primes | S(E)=Σ1/e_p |
|---|---|---|
|2e3|442|1.9731|
|2e4|3469|2.3756|
|2e5|28164|2.7005|
|4e5|53231|2.7875|
|8e5|100814|2.8702|

- The increment of S per unit of loglog E is constant to within ±2% over 1.25e4 to 8e5: 1.55, 1.53, 1.56, 1.58, 1.58, 1.58.
  The fit is S(E) ≈ −1.18 + 1.55·loglog E (max residual 0.004). So **Σ1/e_p diverges like 1.58·loglog E** [CONJECTURED, fits the data].
- Writing n(e) ≈ κ·(e/φ(e))/log e gives κ = 0.781, 0.789, 0.805, 0.815, 0.812, 0.813, 0.813 over buckets up to 8e5, so κ is stable at 0.81.
  The slope 1.58 equals κ·mean(e/φ(e)) = 0.813·1.944. This is consistent.
- The index distribution i = (p−1)/e is the same in (0,4e5] and (4e5,8e5]: 44% have i=1, 25% i=2, about 10% have i≥10, and P(i≥k) ~ k^{-1.07}.
  That matches a density of about 1/i².
- **Artin/Kummer test:** the prediction is n(e) = Σ_i Pr[ie+1 prime]·Σ_{d|e} μ(d)·P(2,3 both id-th powers), with 2500 random e per bucket.
  - The naive 1/(id)² rule fits at E~1e4 but overpredicts by 33–37% at 2e5 and 8e5.
  - The Kummer-degeneracy-only version (√2∈Q(ζ8), √3∈Q(ζ12)) overpredicts by 20–30%. The excess is worst for odd e (factor about 2).
  - With the exact quadratic entanglement (Legendre (2/p), (3/p) fixed by p mod 24 = ie+1 mod 24) the ratio of actual to predicted is
    **1.04, 1.12, 0.97 (±0.05)**.
  - The predicted mass over (4e5,8e5] is 0.079; the actual is 0.083.
  - So the Artin-type heuristic with local corrections explains n(e). I found no anomalous large-index excess. [VERIFIED numerically]
- **Large G(e):** I used L(e) = Σ_{e_p|e} log p, which equals log G(e) up to prime-power multiplicity.
  - L(e)/e is largest only at tiny e: 12 (0.51), 36 (0.47), 4, 6, 11, 48.
  - The absolute maxima are at highly composite e: 720720 (log G ≈ 713), 706860, 655200, 786240. These scale like τ(e), nowhere near εe.
  - The "new part" Σ_{e_p=e} log p has mean 1.68 and a maximum of 59 (e=450990, 4 primes). The largest n(e) is 4.
  - None of this is anomalous.

## 2. Where the bound comes from, and B(∞) (task 2)
**Stage decomposition at 8e5** (cost by bucket of ℓ = P⁺(e_p)):

| ℓ bucket | 2e4 | 1e5 | 2e5 | 4e5 | 8e5 |
|---|---|---|---|---|---|
| 5 | .2316 | .2364 | .2399 | .2400 | .2400 |
| [6,30) | .3747 | .3991 | .4030 | .4080 | .4116 |
| [30,100) | .0271 | .0590 | .0646 | .0691 | .0729 |
| [100,1000) | 0 | .0034 | .0082 | .0135 | .0179 |
| ≥1000 | 0 | 0 | 0 | 0 | 0 |

**All of the cost lies in stages with P⁺(e_p) < 1000.** All 15 218 stages with ℓ ≥ 1000 are "free": Acap ≤ δ, so the tilt removes them at zero cost.
The growth of B comes from small and medium stages filling up with primes whose e = ℓ·e' has a large ℓ-smooth cofactor e'. It also
comes from the re-balancing of δ that this forces on the small stages.

**Stage-mass model.** Write λ_ℓ(E) = ℓ·Σ_{stage ℓ, e≤E} 1/e_p. It follows λ_ℓ(E) ≈ λ_∞·(1 − I(u₀)), where I(u₀) = ∫_{u₀}^∞ ρ(u)/(1+u)du
(Dickman ρ), u₀ = log(E/ℓ)/log ℓ, and λ_∞ = 1.42–1.44 in every bucket from ℓ=5 to 10⁴ and every E. Note that ∫₀^∞ρ/(1+u) = 1. [VERIFIED fit]

So at E = ∞ every stage has about 1.43 expected active primes per fibre. For large ℓ the moment majorant gives
cost_ℓ ≲ m₂/(4δ) ~ C/ℓ² (the fit is C ≈ 15; the exponent fitted on 11≤ℓ<100 is −1.78). This is summable, so **Σ_ℓ cost_ℓ converges heuristically**:
- saturated [100,1000): 0.025–0.033 (currently 0.018);
- all ℓ ≥ 1000 together: 0.002–0.004;
- ℓ < 100 are ≥ 97% saturated, but their observed increments still decay only geometrically (about 0.8 per doubling). [CONJECTURED]

**Back-tested extrapolations of B(E)** (L4″ series, 6 points):
- Increments per doubling are 0.0301, 0.0247, 0.0178, 0.0149, 0.0119. The successive ratios are **0.82, 0.72, 0.84, 0.80**.
- Each asymptotic shape implies a ratio per doubling: loglog E ≈ 0.95, 1/log E ≈ 0.90, 1/log²E ≈ 0.86, E^{-1/4} = 0.84.
- The data therefore reject the loglog (divergent) and 1/log E shapes.
- Two-point fits on (2e5,4e5) predicting 8e5 (actual 0.742445). Every shape over-predicts, so convergence is faster than all of them:

  | shape | error at 8e5 | implied B(∞) |
  |---|---|---|
  | loglog | +0.0023 | diverges |
  | 1/log | +0.0015 | 0.963 |
  | 1/log² | +0.0008 | 0.850 |
  | E^{-1/4} | +0.0007 | 0.805 |

- Fits on (2e4,2e5) predicting 4e5: errors +.0068, +.0041, +.0017, +.0019 for the same four shapes.
- **Missing-mass regression:** B against the Dickman-predicted missing raw mass M in stages ℓ<1000. M = 0.295, 0.157, 0.128, 0.1035 at 2e4, 2e5, 4e5, 8e5.
  - The slope is 0.595 → 0.512 → 0.488 and still falling.
  - Back-test: the (2e5,4e5) slope predicts B(8e5) = 0.7430, error +0.0006. The (2e4,2e5) slope predicts 0.7330 for 4e5 (+0.0024) and 0.7475 for 8e5 (+0.005).
  - Extrapolating to M=0 gives 0.793, or 0.823 if the [1e3,1e4) missing mass is also charged at the current rate.
- **Geometric extrapolation** with the mean of the observed ratios. The estimate of B(∞) is stable as data are added:
  0.810 (data ≤1e5), 0.775 (≤2e5), 0.788 (≤4e5), 0.788 (≤8e5).
  - Back-test from ≤2e5: it predicted 0.7294 and 0.7400 against the actual 0.7306 and 0.7424 (−0.001, −0.002).
- **Estimate: B(∞) ≈ 0.80, plausible range 0.76–0.86** [CONJECTURED].
  - B reaches 1 only if the increment ratio stays ≥ 0.956 per doubling forever, i.e. decay slower than 1/log E. The observed ratios are 0.72–0.84.
  - Under the rejected loglog shape B would reach 1 at E ≈ 10^18.
- **Caveats:**
  - The [1000,10⁴) bucket turns costly only at E ~ 10⁶–10⁷. That may push the ratio up temporarily; this is included in the 0.82–0.86 upper end.
  - The heuristic assumes Artin-type statistics hold uniformly. Large-index control is unproved, as DISTORTION.md says.

## 3. What a covering with huge e_p would need (task 4)
- [PROVED, repo theorem] Some prime with e_p > 4·10⁵ is needed. With B(8e5) < 1, one with e_p > 8·10⁵ is needed. [VERIFIED, float, pool caveat]
- **Necessary density.** Adding primes to a stage raises its true cost by at most their P_{<ℓ} mass, by L1 and the 1-Lipschitz property of (x−δ)₊.
  So any covering P must satisfy Σ_{p∈P, e_p>8e5} Λ_p r_p/(e_p(1−δ_{P⁺(e_p)})) ≥ 1 − 0.7424 = 0.258.
- **Only smooth e_p help.** Under the optimised δ, primes with P⁺(e_p) ≥ 1000 are removed for free. Asymptotically, sets in stages with large ℓ cost
  ~ℓ^{-2}. So the extra density must come from e_p = ℓ·e' with small ℓ and a huge ℓ-smooth e'. That supply is finite and almost exhausted:
  the missing raw mass in all stages ℓ<1000 is about 0.10, against a needed 0.26 weighted. The random-coset (coupon) heuristic points the
  same way: S(E) ~ 1.58·loglog E is far below the ~2 log N needed for unaligned cosets, and the 2D gain (forms equidistributed on ℙ¹(F_ℓ))
  is exactly the absence of alignment.
- **Sierpiński (1D) mechanism.** Every A_p must be a union of lines parallel to one primitive v, i.e. p | 2^a3^b − 1 or p | 2^a − 3^b.
  Equivalently, the joint image of the ψ_p must be cyclic. A necessary condition is S₁(v) = Σ_{ψ_p(v)=0} 1/e_p ≥ 1.
  - Box search over |a|,|b| ≤ 160 with e_p ≤ 2e4: max 0.446 at v=(41,109).
  - Exact maximum on the heavy torus (ℤ/144)²: 0.326.
  - Explicit CRT-greedy construction with e_p ≤ 8e5: aligned mass **0.672** (a lower bound on the sup). The crude upper bound is 1.146, and the
    tail beyond 1e5 adds about 0.09.
  - So density ≥ 1 is not excluded. But the greedy gains at ℓ ≥ 100 are single primes per stage, and those stages are free under distortion.
    The aligned mass in costly stages is ≈ 0.33 + 0.05 + 0.20 = 0.57 < 1. So a 1D covering is implausible. [CONJECTURED; numbers VERIFIED]
- **Conclusion.** A covering would need the bound to fail at some enormous E. That in turn needs many primes with very smooth e_p and aligned forms,
  in a regime where both the mass model (validated to ~5%) and the back-tested trend say no. Without a covering, the standard prime heuristic
  (Σ_{k,l} 1/log(2^k3^l m) diverges) predicts infinitely many primes for every m. So **NO** is more probable.

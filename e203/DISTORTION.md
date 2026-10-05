# A 2D distortion method for Erdős #203

**Theorem (computer-assisted).** Let P be any finite set of primes p ∤ 6 with e_p = |⟨2,3⟩ mod p| ≤ 4·10⁵
for every p ∈ P. Then for every m coprime to 6 there are k, l ≥ 0 such that no p ∈ P divides 2^k·3^l·m + 1.

There is *no condition on lcm(e_p)*. Earlier exclusions needed lcm(e_p) to divide a fixed N ≤ 2.3·10⁸.
Here lcm(e_p) is unrestricted. The pool of candidate primes has
Σ1/e_p = 2.79, far beyond what density alone can rule out. The argument absorbs that excess through
second moments that are small *because the problem is two-dimensional*.

| primes allowed | primes | Σ1/e_p | bound, L4′ (Bonferroni price) | bound, L4″ (exact coupled price) |
|---|---|---|---|---|
| e_p ≤ 2000 | 442 | 1.973 | 0.5701 [PROVED] | — |
| e_p ≤ 20000 | 3469 | 2.376 | 0.7349 [PROVED] | **0.6334** [PROVED] |
| e_p ≤ 100000 | 14856 | 2.608 | 0.8087 [PROVED] | — |
| e_p ≤ 200000 | 28164 | 2.701 | 0.8677 [PROVED] | **0.7157** [PROVED] |
| e_p ≤ 400000 | 53231 | 2.788 | **0.8854** [PROVED] | **0.7306** [PROVED] |

[PROVED] means the bound is reproduced in exact rational arithmetic by an independent verifier
(`verify_distortion23.py`): 0.570147, 0.734931, 0.808684, 0.867666, 0.885439 (L4′) and 0.633429, 0.715690, 0.730584 (L4″).
Every pool is **certified complete**: for each e ≤ E, dividing gcd(2^e − 1, 3^e − 1) by the pool primes
with e_p | e leaves exactly 1 (`certify_pool.py`).

How each refinement moves the bound at E = 20000:

| method | bound |
|---|---|
| density (Σ1/e_p) | 2.376 |
| distortion, moment bounds only | 1.088 |
| + exact stage 2 with forced overlaps (L4) | 0.898 |
| + merged exact {2,3} stage (L4′) | 0.769 |
| + tighter α*_heavy (exact 6-core) | 0.735 |
| + exact coupled removal price (L4″) | **0.633** |

**Scope.** A *covering* here is a certificate made of **prime divisors only**. Certificates that also use
algebraic factorisations (m a perfect power) are treated in [`MIXED.md`](MIXED.md), Theorem E: they are
also excluded for e_p ≤ 4·10⁵ (bound 0.953242).

**Audit (2026-10-02/03).** Nine independent agents checked this work. Results:
- *Mathematics:* every lemma GOOD (M1, L1–L4″), with a toy end-to-end check to 1e-16.
- *Independent recomputation:* reproduces 0.570147, 0.769150 and 0.734931 exactly, and re-derives
  e_p and the kernel lattice of all 3469 primes with e_p ≤ 20000.
- *Red team:* found no unsound case in 4391 genuine coverings, the minimum bound being exactly 1. It also
  checked each lemma inequality term by term on about 57k instances, with 0 violations.
- *Prime data:* all 53231 forms (α, β) define the right lattice.
- *Pool completeness, second route* (`sieve_e.c`): an independent sieve computes e_p from scratch for
  every prime p < 10⁸ (factoring p − 1 and taking exact orders). It finds exactly the pool's 53147 primes
  below 10⁸ with e_p ≤ 4·10⁵, with 0 missing, 0 extra and 0 wrong e. The 84 pool primes above 10⁸ rest on
  the gcd certificate.
- *Coupled prices:* an independent exact solver reproduces the R values (16 types, identical rationals).

The audit raised two residuals:
- `maxratio.c` prunes in double precision, so each certificate proves its R is attained, not that it is
  the maximum. The possible effect is about 1e-14, against a margin of 0.27.
- Forms must be primitive (gcd(α, β, e) = 1). All pool forms are, and `build` now asserts it.

## Setting

For p ∤ 6, ψ_p : ℤ² → ℤ/e_p is (k,l) ↦ log_h(2^k 3^l), where h generates H_p. The set
{(k,l) : p | 2^k 3^l m + 1} is empty or a level set A_p = {ψ_p = c_p}. The primes 2 and 3 only hit the axes.
With N = lcm e_p, G = ℤ²/Nℤ² = ∏_ℓ G_ℓ with G_ℓ = (ℤ/ℓ^{a_ℓ})². The set A_p reads only the coordinates
ℓ | e_p, and in coordinate ℓ it is a coset of index ℓ^{v_ℓ(e_p)}.

## The measures and the covering criterion

Stage ℓ holds the p with P⁺(e_p) = ℓ; write e′_p = e_p/ℓ^{v_p} and B_ℓ = ⋃_{stage ℓ} A_p. Starting from
the first-stage measure, each later stage ℓ = 5, 7, 11, … tilts coordinate ℓ given x_{<ℓ}. With α(x_{<ℓ})
the density of B_ℓ in the fibre:

- w = 1[x ∉ B_ℓ]/(1 − α) if α < δ_ℓ;
- w = (1[x ∉ B_ℓ] + 1[x ∈ B_ℓ](α − δ_ℓ)/α)/(1 − δ_ℓ) otherwise.

**(M1) [PROVED].** Under P_{<ℓ}, the coordinates ≥ ℓ are uniform and independent. w averages to 1 over the
fibre and satisfies w ≤ (1 − δ_ℓ)^{−1}. Later stages preserve the marginal of x_{<i}. Hence
P_final(B_ℓ) = E_{P_{<ℓ}}[(α − δ_ℓ)₊]/(1 − δ_ℓ) =: cost_ℓ. If P covers, then 1 = P_final(⋃B) ≤ Σ cost_ℓ.

## Estimates

**(L1) Local inflation [PROVED].** If A reads only the coordinates S, then
P_{<ℓ}(A) ≤ P_first(A)·∏_{i∈S, i<ℓ, i≥5} (1 − δ_i)^{−1}. Bound w_i for i ∈ S, then sum out the other
coordinates from the top down; each averages to 1. Only the primes dividing e_p inflate p's terms, which is
why Σδ may diverge.

**(L2) Moments [PROVED].** With α ≤ Σ_active ℓ^{−v_p}, capped at 1:
- m₁ = Σ_p Λ_p r_p/e_p;
- m₂ = Σ_p Λ_p r_p ℓ^{−v_p}/e_p + Σ_{p≠q} Λ_{pq} r_{pq} c^<_{pq}/(e_p e_q),
with c^<_{pq} = the ℓ-free part of gcd(α_pβ_q − β_pα_q, e_p, e_q).
**The 2D gain:** c^< = 1 unless the two forms align at a shared prime, and alignment is rare because the
directions are spread evenly over ℙ¹(𝔽_ℓ). So m₂ ≈ m₁² + (diagonal).

**(L3) Majorants [PROVED].** From (x − δ)₊ ≤ a x + b x², cost_ℓ ≤ (a m₁ + b m₂)/(1 − δ). The candidates
are (1, 0), the pure quadratic on [0, A], and tangent parabolas b = δ/t², a = 1 − 2δ/t with t ≥ 2δ.

**(L4′) Exact merged first stage with forced overlaps [PROVED].** B₂₃ = ⋃_{P⁺(e_p) ≤ 3} A_p reads only
(x₂, x₃), so its density α₂₃ is a constant. Define P₂₃ = u·1[x ∉ B₂₃]/(1 − α₂₃); it costs 0. For any set A
(a coset with lattice L_A):

  P₂₃(A) = u(A \ B₂₃)/(1 − α₂₃) ≤ u(A)·(1 − LB(A))/(1 − α*),
  LB(A) = Σ_{i forced} 1/e_i − Σ_{i<j forced} 1/|(ψ_i, ψ_j)(L_A)| over the 9 heavy {2,3}-smooth primes.

Here "forced" means ψ_i(L_A) = ℤ/e_i, which gives u(A ∩ A_i) = u(A)/e_i exactly, for *every* choice of
offsets. If A reads neither x₂ nor x₃, then P₂₃(A) = u(A). α* ≥ α₂₃ is built as follows:
- the heavy primes {5, 7, 13, 17, 19, 37, 73, 97, 577} give
  OPT ≤ 2770/5184 + (one-layer terms for 73, 97, 577) = 0.578318;
- 2770/5184 is the exact optimum of the 6-core, by exhaustive enumeration in two independent ways (HNF cells
  and the raw torus (ℤ/144)²; CP-SAT's best feasible value, 0.569010, lies below it, as it must);
- the light {2,3}-smooth primes add at most Σ1/e_p ≈ 0.048 (union bound).

**(L4″) Exact coupled removal price [PROVED; computer-assisted].** The heavy sets read only x mod 144, and
the uniform measure on a coset A pushes forward to the uniform measure on the image of L_A in (ℤ/144)².
So, with one set of heavy offsets c for numerator and denominator,

  P₂₃(A)/u(A) ≤ R(A) = max_c (1 − cov_A(c)) / (1 − cov_G(c) − λ),

where cov_A is the covered fraction of the image of A, cov_G the global heavy coverage, and λ ≥ the light
{2,3} mass. R depends only on the subgroup L_A + 144ℤ². Every single and pair term of the e_p ≤ 4·10⁵ pool
falls into one of **1908** such subgroups (canonical HNF keys). R is computed exactly for all of them by
branch and bound (`maxratio.c`), which is valid because both coverages only grow along a branch. Each
value is stored as integer counts (bestA, n_A, bestG, n_G), so the verifier recomputes R as an exact
rational. The decoupled bound (1 − minU(A))/(1 − α*), with minU the exact minimum coverage
(`minunion.c`), is kept as a fallback. A side fact: the heavy family can never cover less than 48.12% of
the torus. The table used λ = 0.0485. At E = 4·10⁵ the actual light mass is 0.0485017, and the rigorous
correction factor (1 − OPT_h − λ)/(1 − OPT_h − λ′) (the ratio is increasing in the heavy coverage
g ≤ OPT_h) is applied exactly.
Checks: both B&B solvers match plain exhaustive enumeration to 10 digits on a reduced family; canonical
keys match brute-force images 60/60; every certificate reproduces its value; 1 ≤ R ≤ decoupled for all
1908 types. The weighted mean price drops from 1.936 (decoupled) to 1.707 (coupled).

## Controls

- **Soundness [VERIFIED].** On 15 genuine coverings of ℤ² (synthetic ψ data, each checked to cover by brute
  force), every version of the bound stays ≥ 1. These include 2D coverings by non-parallel lines, 1D
  Sierpiński-type coverings along (1,0), (1,2) and (1,3), mixed stage-2/3 coverings, and four coverings where
  a stage-5 set must finish after the {2,3}-stage. On all tight 2D ones the bound is exactly 1.0000, so the
  method is *sharp*.
- **Planted failures, all firing on genuine coverings.** (i) Zeroing a block of m₂ terms. The write-up first
  called this "dropping the diagonal"; the block actually mixes diagonal and pair terms, and I corrected it
  after tagging diagonal rows explicitly. (ii) Declaring every stage-2 overlap forced. (iii) Understating α*
  by 0.2.
- **Bugs caught by the controls:** a δ = 0 majorant bug in the vectorised code (caught by comparing
  against the scalar code), and a backwards tangent grid for δ > ½ in the heuristic script (the rigorous
  paths already guard with t ≥ 2δ).
- **Independent verifiers** (`verify_distortion.py`, `verify_distortion23.py`). They share no code with the
  search: image sizes come from determinantal divisors, arithmetic is exact rational, and α* is re-derived
  independently. They reproduce 0.791821, 0.570147, 0.769150, 0.734931, 0.808684 and 0.867666 exactly.

## What this does *not* do: all coverings

**The theorem covers every E for which a certified pool can be built. It does not rule out all coverings.**
The obstruction is precise:

- The stage sums range over infinitely many primes. Primes of small index k_p = (p−1)/e_p are dominated by
  Σ_n 2^{ω(n)}/(n·P⁺(n)) < ∞.
- Primes of **large index** (2 and 3 both high-power residues mod p) would need log gcd(2^e − 1, 3^e − 1)
  to be e^{o(1)} on average over e with fixed P⁺(e). Bugeaud–Corvaja–Zannier (εe, ineffective) falls short
  by a power of e, and GRH-conditional Chebotarev results are uniform only up to index about √p for one generator. For
the two generators ⟨2,3⟩ the expected range is p^{1/6} to p^{1/4}, and only x^{1/30} is published
(Cangelmi–Pappalardi, JNT 75, 1999).
- Empirically the large-index tail is thin: #{p : e_p = e} ≈ κ·(e/φ(e))/log e with κ = 0.78–0.82, stable
  over e ≤ 2·10⁵, and the index distribution decays like 1/k² (45% have k = 1, 10% have k ≥ 10). But this
  is not a proof.

**Would the method reach E = ∞ if the tail were controlled? Unknown, but the margin is now real.** With the
exact coupled price, the bound is 0.6334 (2·10⁴), 0.7157 (2·10⁵) and 0.7306 (4·10⁵), a rise of 0.0149 for
the last doubling. The L4′ series rose by 0.0295, 0.0212 and 0.0178 over its last three doublings. Earlier
assessment, kept for the record: The bound grows slowly: 0.570
(2·10³), 0.769 (2·10⁴), 0.817 (5·10⁴), 0.846 (10⁵), 0.868 (2·10⁵), with the α* = 0.5955 series. That is
about 0.03 per doubling of E, and slowly decreasing. A heuristic extrapolation, whose per-stage masses
match the data to within ±25%, **failed its back-test**. From E = 2·10⁴ it predicted B(10⁵) = 0.787, but
the true value is 0.846. The reasons are that (i) re-optimising the δ's globally matters (the same δ's give
1.028 at 10⁵), and (ii) new primes carry inflation Λ·r ≈ 2.3 against 1.3. So I report **no estimate of
B(∞)**. Geometric decay of the increments would stay below 1, and 1/log E decay would not; the data cannot
separate the two.

## Reproduce

```
python3 poolE.py 200000 poolE200000.jsonl && python3 certify_pool.py poolE200000.jsonl 200000
python3 distort23.py poolE200000.jsonl 20000,200000 5,7,13,17,19,37,73,97,577 0.578318
python3 export_delta.py poolE200000.jsonl 20000 delta23_E20000_a0.5783.npy d.json
python3 verify_distortion23.py poolE200000.jsonl 20000 5,7,13,17,19,37,73,97,577 d.json 5,7,13,17,19,37 2770/5184
python3 control_distort.py; python3 control_distort2.py; python3 control_distort23.py
```

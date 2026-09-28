# Erdős #203: covering constructions

> **Update: 2D distortion method ([`DISTORTION.md`](DISTORTION.md)).** No covering exists that uses only
> primes with e_p ≤ 2·10⁵, **for any lcm** (bound 0.8677, 28164 primes, pool certified complete). Every bound
> in the table, up to 2·10⁵, is proved in exact rational arithmetic by an independent verifier. This
> replaces the lcm-restricted table below as the main result. It does **not** rule out every covering:
> primes of large index ⟨2,3⟩ ⊂ (𝔽_p^×)^k are the open end, and DISTORTION.md explains why.

## Earlier: lcm-restricted exclusion

**Verdict: PARTIAL.** No covering was found. What I proved instead is that none can exist below a large
modulus.

> **Theorem (computer-assisted, exact arithmetic).** Take any finite set P of primes, and suppose
> e_p = |⟨2,3⟩ mod p| divides N for every p ∈ P, where N is one of
> 720720, 1441440, 2162160, 3603600, 4324320, 12252240, 21621600, 36756720, 61261200, 73513440,
> 232792560. Then for every m coprime to 6 there are k, l ≥ 0 such that no p ∈ P divides
> 2^k·3^l·m + 1.

So any m that answers #203 through a covering needs covering primes whose lcm(e_p) divides *none* of
these numbers, the largest being lcm(1, …, 22). Before this, the best exclusion was lcm < 5040, and only
for primes p ≤ 5·10⁷ (forum, 2026-06). This result covers primes of every size, because each pool is
certified complete.

## Risks (worst first)

1. **This does not settle #203.** The question stays open. The theorem only rules out one route (coverings)
   below a finite modulus. An m that exists for non-covering reasons, like Izotov's perfect-power Sierpiński
   numbers, is untouched.
2. **The method has a ceiling.** The bound rises with Σ1/e_p, which grows like log log N. Near Σ ≈ 1.4 the
   one-layer bound reaches 1 and stops excluding anything. Pushing further needs a 2D version of the
   Balister–Bollobás–Morris–Sahasrabudhe–Tiba distortion method.
3. **698377680 has a weaker status than the theorem list.** It is excluded only with the 7-prime core, whose
   optimum is certified by CP-SAT alone; with the brute-force 6-core the bound is 1.000077. An 8-prime
   core (adding 31) did not finish: CP-SAT's bound after 4800 s was 0.996, which is useless.
4. **The core optimum is computed, not derived.** It rests on exhaustive enumeration (`brute_core.c`, all
   207360 coset choices). CP-SAT agrees independently (4915/8640).

## The mechanism: why 2D coverings are starved

For p ∤ 6, let h generate H_p = ⟨2,3⟩ mod p and set ψ_p(k,l) = log_h(2^k 3^l) ∈ ℤ/e_p. The pairs (k,l)
where p | 2^k 3^l m + 1 form the level set {ψ_p = c_p}, where c_p can be chosen freely through m mod p.
Everything below rests on one lemma.

**Independence lemma [PROVED].** The map ℤ² → ∏_{p∈T} ℤ/e_p is onto if and only if, for every prime ℓ, at
most two p ∈ T have ℓ | e_p, and when two do, their forms ψ_p mod ℓ have different kernel lines in 𝔽_ℓ².
*Proof:* CRT splits the map into its ℓ-parts. Each ℓ-part is onto iff it is onto mod ℓ (Nakayama), and mod
ℓ this is rank = |T ∩ {ℓ | e_p}| in 𝔽_ℓ², which forces at most two members with independent rows.

**Consequence.** If {i} ∪ J is jointly independent, then |A_i \ ⋃_J A_j| = w_i ∏_J (1 − w_j) exactly (with
w = 1/e), *whatever cosets are chosen*. Take the primes in any order. Then

  coverage ≤ OPT(core) + Σ_{i ∉ core} w_i ∏_{j∈J_i} (1 − w_j),  with J_i earlier and {i} ∪ J_i independent.

The bound bites because the kernel lines are spread evenly over ℙ¹(𝔽_ℓ). The three heaviest primes, 5, 7
and 13 (e = 4, 6, 12), have mod-2 kernels k+l, l and k: all three lines of 𝔽₂². So their overlaps are
forced. [VERIFIED] At N = 720720, the 95 primes with 2 | e_p split 33/31/31 over the three lines. At
ℓ = 13 no line holds more than 7 of the 44 primes, which is fewer than the 13 parallel lines needed to
clear a fibre.

## Certified results

| N | factorisation | primes | Σ1/e | coverage ≤ (6-core, exact rational) | 7-core (CP-SAT) |
|---|---|---|---|---|---|
| 720720 | 2⁴3²·5·7·11·13 | 99 | 1.2490 | 0.9094 | — |
| 12252240 | 2⁴3²·5·7·11·13·17 | 192 | 1.3159 | 0.9534 | 0.9442 |
| 21621600 | 2⁵3³5²·7·11·13 | 229 | 1.3433 | 0.9718 | 0.9627 |
| 36756720 | 2⁴3³·5·7·11·13·17 | 258 | 1.3471 | 0.9746 | 0.9654 |
| 61261200 | 2⁴3²5²·7·11·13·17 | 281 | 1.3654 | 0.9853 | 0.9762 |
| 73513440 | 2⁵3³·5·7·11·13·17 | 299 | 1.3636 | 0.9854 | 0.9763 |
| 232792560 | lcm(1..22) | 322 | 1.3561 | 0.9777 | 0.9685 |
| 698377680 | 2⁴3³·5·7·11·13·17·19 | 449 | 1.3894 | 1.000077 (not proved) | **0.9909** [VERIFIED: relies on the CP-SAT-certified 7-core, 0.588575] |
| 367567200 | 2⁵3³5²·7·11·13·17 | 435 | 1.4142 | — | 1.0088 **(inconclusive: ceiling reached)** |
| 1163962800 | 2⁴3²5²·7·11·13·17·19 | 479 | 1.4071 | — | 1.0018 (inconclusive) |

The 6-core column is reproduced end to end by `verify_exclusion.py` (output in `verify_all.log`). It uses
exact rationals, computes kernel lines without discrete logs, and shares no code with the search.
The one-layer bound (no core) also excludes 5040, 10080, 27720, 55440, 1441440, 2162160, 3603600 and
4324320 (`exclude.py`). Every pool is **certified complete**: G(N) = gcd(2^N − 1, 3^N − 1) is divisible by
exactly the primes with e_p | N, and after dividing out the found primes the cofactor is exactly 1.

## Construction attempts and what they showed

- **Density is scarce [VERIFIED, complete pools].** Σ1/e_p is 1.021 at N = 5040, 1.249 at 720720, and
  1.356 at 232792560. Compare the classical Sierpiński covering, which reaches Σ = 1.33 with perfect
  nesting. The pool contains only primes where *both* 2 and 3 have small order.
- **Aligned (nested) families are thin [VERIFIED, beam search, pool e_p ≤ 20000].** The best density
  reachable on a group of size |G_S| ≤ B is 0.60 at B = 10³, 0.72 at 10⁴, 0.90 at 10⁶, 0.99 at 10⁷,
  1.066 at 7·10⁷, 1.131 at 10⁹, 1.177 at 10¹⁰, and 1.210 at 10¹¹. That is about +0.04 per decade: each
  step of nesting multiplies the group size, while density grows only additively.
- **Exact optima are barely above random [VERIFIED, CP-SAT, and brute force for the 6-core].**
  {5,7,11,13}: 0.4903 against 0.4844 random. The 6-core: 0.5689 against 0.5435. The 7-core: 0.5886.
- **The best nested family found plateaus at 71.8%** under C local search (25 primes, Σ = 1.066,
  |G| = 6.99·10⁷). That matches the forum's 72–76%, so the wall is structural, not a failure of search.

## Dead ideas

| id | idea | why it fails |
|---|---|---|
| D1 | m = M^q to get free algebraic cosets qℤ² (x^q + 1 factors) | [PROVED] Take a prime p with 3 ∣ e_p and v₃(e_p) = v₃(p−1). Since −1 = (−1)³, p's killed set lies inside {ψ_p ≡ 0 (3)} ⊇ 3ℤ²: the cells the cube already covers. The same holds for every odd q. This matches the forum's observation that perfect powers *lowered* coverage. |
| D2 | a single direction (a 1D Sierpiński problem in t = ak + bl) | its primes divide 2^b − 3^a. The joint quotient must be cyclic, so the captured density is ≈ Σ 1/e_p² |
| D3 | strip families ℤ_N × ℤ_d with unit direction J | contained in the beam search (all directions, including non-unit ones), which is still thin |

## Not established

- Whether a covering exists at some N beyond the table. The exclusion stops once the bound reaches 1.
- Anything about m that are not coverings.
- A proof that no covering exists at all. That needs an asymptotic 2D distortion bound. It is the natural
  next target, and it would show #203 cannot be settled YES by the standard method.

## Reproduce

```
python3 poolbig.py N                      # certified-complete pool -> poolN_N.jsonl
gcc -O2 -o brute_core brute_core.c && ./brute_core     # 6-core optimum 4915/8640
python3 verify_exclusion.py 720720 12252240 ...        # independent verifier, exact rationals
python3 control.py                        # soundness + planted-failure controls
```

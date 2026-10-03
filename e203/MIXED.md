# Mixed certificates: covering primes plus algebraic factorisations

**Theorem E (computer-assisted).** Let m ≥ 1 with gcd(m, 6) = 1. Allow m to be a perfect power M^g of any
exponent g. Let P be any finite set of primes p ∤ 6 with e_p = |⟨2,3⟩ mod p| ≤ 4·10⁵. Then some k, l ≥ 0
make 2^k·3^l·m + 1 **divisible by no p ∈ P and not factored by any binomial identity**.

This closes the only known way of answering #203 YES within the certified range: Sierpiński-type
certificates of every kind, from pure coverings to Izotov-style mixtures. It does **not** settle #203, as the
last section explains.

Sources: Root 9 derived the theorem. I re-verified every number independently, and the derivation went
through a hostile mathematical audit (Root 1) and an adversarial soundness search (Root 5).

## 1. Which algebraic factorisations exist [PROVED]

Write A = 2^k 3^l m. A binomial identity means A + 1 = c·z₀^d + 1 with c·z^d + 1 reducible in ℚ[z]. By
Capelli's theorem (Lang, *Algebra*, VI §9) that happens iff c is a q-th power for an odd prime q | d, or
4 | d and c ∈ 4ℚ⁴. Since v₂(A) = k and v₃(A) = l, the factorised set for m = M^g is

  Alg(m) = ⋃_{odd primes q | g} qℤ²  ∪  [ C₄ = (2,0) + 4ℤ² if 4 | g ].

The identities are x^q + 1 = (x + 1)Φ(x) and 4y⁴ + 1 = (2y² + 2y + 1)(2y² − 2y + 1). Every other identity
(27y⁶ + 1, Aurifeuillean splittings of Φ_n) lies inside these cosets.
*Check:* `capelli_check.py` factors c·z^d + 1 with sympy for c = 2^a 3^b M^j and d ≤ 12: 27144 cases,
978 reducible, **0 mismatches**. Dropping the 4ℚ⁴ clause produces 9 mismatches, so the control fires.

## 2. What a perfect power does to the primes [PROVED]

If m = M^g, the set where p divides the value is {ψ_p = c}, with h^c = −M^{−g}. Not every offset c is
reachable. Writing n = p − 1, d = gcd(g, n) and o = e_p/gcd(e_p, n/d):

- if n/d is even, the reachable offsets are c ≡ 0 (mod o);
- if n/d is odd and o is even, they are c ≡ o/2 (mod o);
- if both are odd, none is reachable, and p is useless.

*Check:* `constraint.py`, 3318 pairs (p, g) against brute force over every M: 0 mismatches. Dropping the
sign (−1)^{n/d} gives 99 mismatches.

Two consequences matter:

- **Every heavy {2,3} prime is always usable.** All their e_p are even, so o is even whenever n/d is odd.
- **C₄ is useless on its own.** If 5 ∤ M and 4 | g, then on C₄ we have 2^k ≡ 4, 3^l ≡ 1 and M^g ≡ 1
  (mod 5), so 5 divides every value there: C₄ already lies inside A₅.

## 3. The reduction that does the work [PROVED]

**Lemma (augmentation).** If (m = M^g, P) is a mixed certificate, then so is (M′^g, P ∪ U) for every set U
of usable primes. In particular, we may assume WLOG that every usable prime with e_p ≤ 4·10⁵ is used,
and that 5 ∤ M.

*Proof.* Choose M′ by CRT: M′ ≡ M modulo every p ∈ P and modulo 6, and M′ chosen modulo each other prime
so that the prime is reachable (or so that 5 ∤ M′). For p ∈ P we have M′^g ≡ M^g (mod p), so the sets
A_p do not change. The set Alg depends only on g. So everything covered before is still covered. ∎

This lemma is load-bearing. Drop it, and let core primes go unused, and R3 rises from 0.0763 to 0.1304,
which pushes the total to 1.0074: no conclusion.

## 4. The bound

Take the measure P_final built for the pure theorem (DISTORTION.md, L4″, δ from `delta23r_E400000.json`).
If X ∪ Alg covered everything, where X is the union of the prime sets, then

  1 ≤ P_final(X) + [3 | g]·P_final(3ℤ²) + Σ_{q ≥ 5} P_final(qℤ²).

The three terms:

1. **P_final(X) ≤ B = 0.730584.** This is the pure theorem, verified in exact rationals. It holds for the
   used primes: by the lemma that is the full pool minus useless primes. Every heavy prime is still there,
   so the coupled prices stay valid and every other term only shrinks.
2. **P_final(qℤ²) ≤ q⁻²/(1 − δ_q).** This is L1, since qℤ² reads only coordinate q. The sum S over
   5 ≤ q ≤ 4·10⁵ is **0.146379**. The tail beyond 4·10⁵ (coordinate untouched) adds less than 2.5·10⁻⁶.
3. **P_final(3ℤ²) = P₂₃(3ℤ²) ≤ R3,** where

   R3 = max u(3ℤ² ∖ B_core) / (1 − u(B_core) − λ′)

   over the reachable offsets of the 6-core {5, 7, 13, 17, 19, 37}, for **every g with 3 | g**. Here
   λ′ = light {2,3} mass + 1/36 + 1/48 + 1/144 = 0.104057. The result is
   **R3 = 250822656/3288415339 = 0.076275**, attained at gcd(g, 144) = 3.

| case | bound |
|---|---|
| 3 ∤ g | 0.730585 + 0.146379 + 0.0000025 = **0.876967 < 1** |
| 3 \| g | + 0.076275 = **0.953242 < 1** |
| control: reachable-offset constraint ignored (R3 = 0.216) | 1.093, inconclusive |

**Independent reproduction** (`verify_mixed.py`). It never uses α, β or the offset theorem. For each
core prime it enumerates every M mod p and marks the cells of (ℤ/144)² where 2^k 3^l M^g ≡ −1 (mod p),
maximises over all g′ = gcd(g, 144) with 3 | g′, and computes S in exact rationals with the tail included.
It reproduces R3 as **the identical fraction**, and the totals above.

## 5. What remains open

- **Primes with e_p > 4·10⁵.** A covering or mixed certificate could still use them. Excluding them needs
  control of large-index primes (DISTORTION.md, last section), which no known theorem provides, with or
  without GRH. In two-generator Artin problems, GRH-uniform results reach index about p^{1/6} to p^{1/4},
  and only x^{1/30} is published.
- **m whose compositeness has no certificate at all.** Theorem E excludes every Sierpiński-type witness
  in range. It says nothing about an m whose values 2^k 3^l m + 1 are all composite "by accident". Proving
  #203 NO means showing that every such family contains a prime. That is the Sierpiński-problem barrier,
  and it is far beyond current methods.

**Status of #203 after this work: OPEN.** What is closed is every certificate-based YES answer whose primes
have e_p ≤ 4·10⁵.

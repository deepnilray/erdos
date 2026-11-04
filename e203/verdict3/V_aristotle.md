# V_aristotle: Lean 4 + Mathlib prompts for elementary lemmas (agent V)

Statements are NOT compiled (no Lean on this machine). Each was checked by hand and, where marked, by a brute-force run.
Where a statement may need small repairs (casts, `Nat.sub`), say so to Aristotle and ask it to repair the statement but keep the meaning.
Prompts from B_noside.md section 8 (AP1 conductor lemma, AP2 lattice point count, AP3 killed set, AP4 reformulation) were re-read: all four statements are TRUE and
match their proofs; AP1 verified by hand (D = 1, -3 and 4d with d in {-1,2,-2,3,6,-6}).

## AV1. gcd characterisation of e_p (basis of the pool certificate)
Prove in Lean 4 / Mathlib:
```lean
theorem gcd_char (p : ℕ) [Fact p.Prime] (hp : 5 ≤ p) (e : ℕ) (he : 0 < e) :
    p ∣ Nat.gcd (2^e - 1) (3^e - 1) ↔
      Nat.lcm (orderOf (2 : ZMod p)) (orderOf (3 : ZMod p)) ∣ e
```
Sketch: `Nat.dvd_gcd_iff`; p ∣ 2^e - 1 (natural subtraction, 2^e ≥ 1) iff ((2:ZMod p))^e = 1 (`ZMod.natCast_zmod_eq_zero_iff_dvd`/`ZMod.natCast_self_eq_zero`, `Nat.cast_sub`, `Nat.one_le_two_pow`);
`orderOf_dvd_iff_pow_eq_one`; `Nat.lcm_dvd_iff`.

## AV2. Pool completeness follows from the gcd certificate
```lean
theorem pool_complete (P : Finset ℕ) (E : ℕ)
    (hcert : ∀ e, 1 ≤ e → e ≤ E → ∀ q : ℕ, q.Prime → q ∣ Nat.gcd (2^e - 1) (3^e - 1) → q ∈ P) :
    ∀ p : ℕ, p.Prime → 5 ≤ p →
      Nat.lcm (orderOf (2 : ZMod p)) (orderOf (3 : ZMod p)) ≤ E → p ∈ P
```
(Uses `haveI := Fact.mk hp`, AV1 with e := the lcm, which is positive because orders of nonzero elements of a finite group are positive; 2 and 3 are nonzero mod p for p ≥ 5.)
Remark for the human: the repo's "divide out pool primes with e_q | e, remainder must be 1" is equivalent to hcert, because q | G_e iff e_q | e.
A wrong e_q in the pool data can only make the check fail, never pass falsely (checked in the red team).

## AV3. Quadratic majorant of (x - delta)_+ (L3)
```lean
theorem majorant (δ t x : ℝ) (hδ : 0 ≤ δ) (ht : 2 * δ ≤ t) (htp : 0 < t) (hx : 0 ≤ x) :
    max (x - δ) 0 ≤ (1 - 2 * δ / t) * x + (δ / t ^ 2) * x ^ 2
```
Sketch: RHS - (x - δ) = δ (x/t - 1)^2 >= 0, and RHS >= 0 because 1 - 2δ/t >= 0 and x >= 0. (`field_simp`, `nlinarith`.)
Companion (the pure quadratic): for 0 < δ, A > 0, x0 = min (2δ) A, b = (x0 - δ)/x0^2, every x in [0, A] satisfies max (x - δ) 0 <= b x^2. (If x0 <= δ then b <= 0; the claim then needs A <= δ, so state it with hypothesis δ < x0.)

## AV4. Tilt weights (M1)
```lean
theorem tilt_weights (δ α : ℝ) (hδ0 : 0 ≤ δ) (hδ1 : δ < 1) (hα0 : 0 < α) (hα1 : α ≤ 1) :
    let w0 : ℝ := if α < δ then 1 / (1 - α) else 1 / (1 - δ)          -- weight outside B
    let w1 : ℝ := if α < δ then 0 else (α - δ) / (α * (1 - δ))        -- weight inside B
    (1 - α) * w0 + α * w1 = 1 ∧ 0 ≤ w0 ∧ w0 ≤ 1 / (1 - δ) ∧ 0 ≤ w1 ∧ w1 ≤ 1 / (1 - δ) ∧
    α * w1 = max (α - δ) 0 / (1 - δ)
```
(If α = 1 and α < δ is impossible since δ < 1; w0 = 1/(1-α) only used when α < δ < 1.)

## AV5. Bonferroni lower bound for a union (used for LB(A))
```lean
theorem bonferroni {ι α : Type*} [DecidableEq α] [LinearOrder ι] (s : Finset ι) (A : ι → Finset α) :
    (∑ i ∈ s, (A i).card : ℤ) - ∑ i ∈ s, ∑ j ∈ s.filter (fun j => i < j), ((A i ∩ A j).card : ℤ)
      ≤ (s.biUnion A).card
```
Sketch: induction on s, or count for each x: with n = number of i with x in A i, n - C(n,2) <= 1[n >= 1].

## AV6. Algebraic factorisations (MIXED.md section 1 identities)
```lean
theorem odd_pow_add_one_dvd (z : ℤ) (q : ℕ) (hq : Odd q) : (z + 1) ∣ z ^ q + 1
theorem aurifeuille4 (y : ℤ) : 4 * y ^ 4 + 1 = (2 * y ^ 2 + 2 * y + 1) * (2 * y ^ 2 - 2 * y + 1)
theorem composite_of_odd_power (q M a b : ℕ) (hq : q.Prime) (hq3 : 3 ≤ q) (ha : 1 ≤ a) (hb : 1 ≤ b) (hM : 2 ≤ M) :
    ¬ (2 ^ (q * a) * 3 ^ (q * b) * M ^ q + 1).Prime
```
Third: z = 2^a 3^b M, value = z^q + 1, (z+1) divides it, 1 < z + 1 < z^q + 1 (z >= 12, q >= 3). (`Odd.add_dvd_pow_add_pow` is the Mathlib name for the first.)
The perfect power exponent in MIXED.md is g with q | g; the statement above is the case m = M^q, which suffices because m = (M^{g/q})^q.

## AV7. Periodic set that misses a point misses the open quadrant
```lean
theorem periodic_quadrant (N : ℤ) (hN : 0 < N) (S : Set (ℤ × ℤ))
    (hk : ∀ k l, (k, l) ∈ S ↔ (k + N, l) ∈ S) (hl : ∀ k l, (k, l) ∈ S ↔ (k, l + N) ∈ S)
    (hne : ∃ x, x ∉ S) : ∃ k l : ℤ, 1 ≤ k ∧ 1 ≤ l ∧ (k, l) ∉ S
```
Proof: for x = (a,b) take k = a mod N + N, l = b mod N + N; shift by multiples of N (`Int.emod_add_ediv`, induction via `Int.induction_on`).

## AV8. Augmentation by CRT (pure and mixed theorems)
```lean
theorem augmentation (S U : Finset ℕ) (hdisj : Disjoint S U) (hS : ∀ p ∈ S, p.Prime ∧ 5 ≤ p)
    (hU : ∀ q ∈ U, q.Prime ∧ 5 ≤ q) (m : ℕ) (target : ∀ q ∈ U, ℕ) (htarget : ∀ q (hq : q ∈ U), ¬ (q ∣ target q hq)) :
    ∃ m' : ℕ, m' % 6 = m % 6 ∧ (∀ p ∈ S, m' % p = m % p) ∧ ∀ q (hq : q ∈ U), m' % q = target q hq % q
```
Here target q = a residue with -1/m' in H_q. Sketch: `Nat.chineseRemainderOfFinset` / `ZMod.prodEquivPi` with pairwise coprime moduli {6} ∪ S ∪ U.
Mathematical statement the repo needs: for every pool prime q there exists a nonzero residue r with -1/r in <2,3> mod q (take r = -h^{-1}, h in H_q), so A_q(m') is nonempty.

## AV9. Intersection constant (hard, optional)
For positive integers a, b and integer forms (α,β), (α',β') with gcd(α,β,a) = 1 and gcd(α',β',b) = 1, put D = αβ' - βα' and c = gcd(D, a, b). For N = lcm(a,b) and every pair of targets (s,t) the number of (k,l) in (Z/N)^2 with αk+βl ≡ s (mod a) and α'k+β'l ≡ t (mod b) is either 0 or N^2 c/(ab).
Verified by brute force on 2163 random instances (V_coker.py); Lean proof via Smith normal form, expected to be long. Only submit if Aristotle has budget.

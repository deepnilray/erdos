# Agent 4: structural and necessary conditions for Erdős #203; theory and literature

Scripts and outputs: `scratchpad/agents5/a4/`. I modified no repo files.
"PRP" means a gmpy2 Miller–Rabin probable prime (25 rounds). "Prime [PROVED]" means sympy `isprime` on a number below 2^64, where it is deterministic.

## Verdict

**NO is more probable.** In other words, every m coprime to 6 probably has a prime of the form 2^k 3^l m + 1. Four independent reasons:
(i) The originators expected NO-type behaviour. See L1: Erdős–Odlyzko 1979 is the origin of the question.
(ii) A 2026 conjecture says the only obstructions in the closest analogue are coverings (Granville–Pappalardi, L3).
(iii) The repo proves no covering or mixed certificate exists with e_p ≤ 4·10^5.
(iv) The 2D heuristic is far more robust than the 1D one: about c·log x expected primes up to x, against c·log log x for k·2^n + 1.

No theoretical proof exists either way. A NO proof is out of reach because it would at least require primes in a sequence of density about (log x)^2 / x. A YES proof needs a 2D covering with heavy primes beyond e_p = 4·10^5, or a mechanism that has never been seen.

## 1. Literature (each item read on its primary source)

**L1. Origin of the problem, and the best known partial NO result.**
Source: P. Erdős and A. M. Odlyzko, "On the density of odd integers of the form (p−1)2^{−n} and related questions", J. Number Theory 11(2) (1979) 257–263. I read the reprint PDF at static.renyi.hu/~p_erdos/1979-12.pdf through its OCR text layer. The zbMATH review is Zbl 0405.10036, by I. Z. Ruzsa.

- *Theorem 2 [PROVED, EO79].* For primes p_1, …, p_r, the integers k coprime to p_1⋯p_r for which k·p_1^{n_1}⋯p_r^{n_r} + 1 is prime for some n_i have **positive lower density**. With r = 2 and p_i = 2, 3, this is the strongest unconditional partial NO result I found: a positive proportion of m are not YES. I found nothing stronger, such as "almost all m" or an almost-prime (P_r) statement for every m. Sieve methods cannot reach a set of size about (log x)^2 below x.
- *Page 258 (paraphrased; the OCR is garbled).* For r ≥ 2 "the situation could conceivably be quite different from that of Theorem 1". The text says all integers k coprime to p_1⋯p_r might be of the form (p − 1)p_1^{−a_1}⋯p_r^{−a_r}. "The simplest case of this question is r = 2, p_1 = 2, p_2 = 3." They report that every k < 50,000 with (k, 6) = 1 has 2^a 3^b k + 1 prime with a, b small; the OCR reads "a ? b < 9". **So #203 is the Erdős–Odlyzko question, posed in 1979 with a lean towards "all k are represented" (NO).** Ruzsa's review also names it as the most interesting open problem.
- *My check [VERIFIED].* For k < 50000 with gcd(k, 6) = 1, a prime exists with max(a, b) ≤ 7 in every case. The minimal a + b is at most 9, and k = 2657 needs exactly 9. So the OCR "a ? b < 9" is true read as "a, b < 9" and false read as "a + b < 9".
- *Reformulation [PROVED, trivial].* YES holds if and only if some m with (m, 6) = 1 is not s(p) for any prime p, where s(p) = (p − 1)/(2^{v_2} 3^{v_3}) is the 6-free part of p − 1.

**L2. Filaseta–Finch–Kozek.**
Source: M. Filaseta, C. Finch, M. Kozek, "On powers associated with Sierpiński numbers, Riesel numbers and Polignac's conjecture", J. Number Theory 128 (2008) 1916–1940. I read the authors' draft hosted at whittier.edu; the DOI 10.1016/j.jnt.2008.02.004 is taken from the Whittier repository record.

- Erdős conjectured that every Sierpiński number "must be obtainable from an argument involving a covering", citing Guy, UPINT F13. FFK's Conjecture 2, also attributed to Erdős, says the least prime factor of k·2^n + 1 is bounded.
- FFK argue that Izotov's k = ℓ^4 with ℓ = 734110615000775 (from Izotov, Fibonacci Quart. 33 (1995)) "likely" refutes it. Their support is numerical evidence (Table 2), not a proof. In their words, a "proof" that their examples cannot arise from a covering "seems out of reach".
- **Answer to Task 1(a): no Sierpiński number is known to be proved to have no covering.** Izotov-type numbers are *proved* Sierpiński by a covering plus the Aurifeuillean identity 4x^4 + 1. Only the claim that no pure covering exists for them is conjectural.
- FFK state an open 2D cousin of #203: "We do not know whether there is a k such that the infinite list k, k^2, k^3, … are all simultaneously Sierpiński numbers … the same as asking whether … all of the numbers of the form 2^i k^j + 1 … are composite."

**L3. Granville–Pappalardi.**
Source: A. Granville and F. Pappalardi, "Two dimensional covering systems and possible prime producing a^m − b^n", arXiv:2601.10296 (v1 15 Jan 2026, v2 11 Apr 2026). I read the abstract page and the HTML text.

- They build lattice-coset 2D coverings for a^m ≡ b^n (mod p). Their structure is the same as the repo's L_p, with index lcm(ord_p a, ord_p b).
- *Conjecture 1.* |a^m − b^n| takes infinitely many prime values unless a covering obstruction exists (with an extra clause for perfect powers). They expect about c·log x primes up to x, that is, linear in the height.
- They do not mention #203. Their framework is the closest analogue, and it predicts that for 2^k 3^l m + 1 the only obstructions are coverings and Capelli-type factorisations.

**L4. Filaseta–Groth–Luckner.**
Source: M. Filaseta, R. Groth, T. Luckner, "Generalized Sierpiński numbers", arXiv:2305.09219 (2023). I read the abstract only. For every A, there is an odd k with k·a^n + 1 composite for every base 2 ≤ a ≤ A and every n. This is a single exponent with many bases; it is not 2D and does not bear on #203 directly.

**L5. Data sources: OEIS and Prime Puzzles.**
- OEIS A123159 gives the conjectured smallest base-3 Sierpiński number of the second kind, 125050976086. Its cached primeform digest (a123159_1.txt) gives the covering {5, 7, 13, 17, 19, 37, 41, 193, 757} found by M. Klasson in 2004, and Brennen's covering sets.
- Prime Puzzles problem 49 lists Sierpiński numbers divisible by 3. The smallest known is 7592506760633776533 (Wesolowski 2023, "probably the smallest such number").
- I re-verified every covering I use, below.

## 2. Necessary conditions on a YES m

- **N1 [PROVED].** Column k = 0 is always composite, because 3^l m + 1 is even and greater than 2 when m > 1. So YES holds if and only if both of the following hold:
  - (a) 3^l m is a Sierpiński number (2^k·(3^l m) + 1 composite for every k ≥ 1) for **every** l ≥ 0;
  - (b) 2^k m is a base-3 Sierpiński number of the second kind (3^l·(2^k m) + 1 composite for every l ≥ 0) for **every** k ≥ 1. Condition (b) is implied by (a) together with N1.
- **N2 [PROVED].** For l ≥ 1, a covering of row l cannot use the prime 3, since 2^k 3^l m + 1 ≡ 1 (mod 3). So 3^l m must be a Sierpiński number divisible by 3, whose covering avoids 3. Zsigmondy's theorem restricts the allowed row moduli: 2^6 − 1 = 3^2·7 has no primitive prime divisor, so no prime has ord_p 2 = 6, and only 3 has ord_p 2 = 2. Row moduli for l ≥ 1 therefore lie in {3, 4, 5, 7, 8, …}, never 2 or 6. Likewise for columns k ≥ 1, 3^2 − 1 = 8 means ord_p 3 ∉ {1, 2}. The heaviest prime of the 1D Sierpiński problem (3, density 1/2) is available on one row only.
- **N3 [PROVED, density].** Let P be the covering set. Prime p is active (divides some element) in exactly a 1/d_p share of the rows, where d_p = e_p/ord_p 2 = [⟨2,3⟩ : ⟨2⟩]. In an active row it covers a share 1/ord_p 2. Every row l ≥ 1 needs Σ_{p active in row l} 1/ord_p 2 ≥ 1, and row 0 gets an extra 1/2 from the prime 3. Averaging over rows recovers Σ 1/e_p ≥ 1. The same holds for columns with ord_p 3.
- **N4 [PROVED].** A finite certificate is a 2D covering. Suppose rows l ≥ 0 are covered by a *finite* prime set P (plus the Capelli sets, which are also lattice cosets). Everything is periodic with period N = lcm e_p in both coordinates, so the certificate is a covering of ℤ^2: exactly the object the repo excludes for e_p ≤ 4·10^5.
  - Hence a YES m is one of three kinds: (i) a 2D covering with some heavy prime of e_p > 4·10^5; (ii) a mixed covering plus Capelli certificate, with the same restriction (MIXED.md); or (iii) a family whose least prime factor is unbounded, needing infinitely many primes across rows. Kind (iii) is a 2D counterexample to Erdős's Conjecture 2.
  - No instance of (iii) is known in **any** analogous problem. Even in 1D, the only proposed instances (Izotov's, FFK) are really of kind (ii).
- **N5 [PROVED].** The repo's Capelli analysis (MIXED.md §1) lists every binomial identity c·z^d + 1. I see no other algebraic mechanism for a 2-parameter family c·X^i Y^j + 1 with X, Y ∈ ⟨2, 3⟩. On any sublattice the value is c'·Z^q + 1 with Z a {2,3}-unit, so Capelli applies along the lattice.
- **N6 [PROVED, S-unit theorem].** For each finite set Q of primes, only finitely many (k, l) have 2^k 3^l m + 1 composed solely of primes in Q (finiteness of S-unit equations, Evertse). So the cofactors outside any covering set must contain new primes infinitely often. This is consistent with coverings and gives no obstruction; I record it for completeness.

## 3. Computations

**C1. Known Sierpiński numbers fail at the very first row l = 1 [PROVED primes].** For each of the 25 numbers s in the task list, I found the first k with 3·s·2^k + 1 prime. Every value is below 2^64, so sympy `isprime` is deterministic.

```
78557:13  271129:3  271577:7  322523:1  327739:2  482719:3  575041:4  603713:1  903983:3
934909:35 965431:10 1259779:3 1290677:20 1518781:21 1624097:4 1639459:2 1777613:1 2131043:2
2131099:7 2191531:1 2510177:5 2541601:9 2576089:3 2931767:1 2931991:2
```

For example, 3·78557·2^13 + 1 = 1930616833 is prime. So **3·78557 is not Sierpiński**, and no listed s has 3^l s Sierpiński for every l.
Sanity check: row 0 had no PRP for k < 600, consistent with s being Sierpiński.
Beyond that, two short-range checks. Rows l = 1…40 all contain a PRP with k ≤ 300, except 1 row for s = 2931991. Columns k = 1…40 all contain a PRP with l ≤ 300, except 2 columns for s = 2541601 and 1 for s = 2931991. Column k = 0 is always even, so it never has a prime. The exceptions are short-range misses, not claims.

**C2. Base-3 Sierpiński numbers [VERIFIED coverings; PROVED witnesses].** For each K, I checked that K·3^n + 1 is covered for every n mod L.

| K = 2m | covering | L | 2D failure (column k = 2 already) |
|---|---|---|---|
| 125050976086 = 2·62525488043 | {5,7,13,17,19,37,41,193,757} | 144 | 2^2·3^9·m + 1 = 4922756724601477, prime |
| 3574321403229074 | {5,7,13,17,41,73,97,193,769,6481} | 48 | 2^4·m + 1 = 28594571225832593, prime |
| 73570980583989386 | {5,7,13,17,41,73,97,193,577,6481} | 48 | 2^4·3^2·m + 1 = 5297110602047235793, prime |

- For each, column k = 1 has no PRP for l < 400, as it should.
- The covering for 125050976086 does not cover K·3^n − 1 (88 of 144 residues are left uncovered). The digest's 2·31532322469 and 2·17630689120601 are *Riesel* coverings, not Sierpiński.
- Columns k = 2…12 each have a PRP at small l, and so does row 0.

**C3. Sierpiński numbers divisible by 3 (the only candidates for rows l ≥ 1) [VERIFIED coverings].** I re-checked five covering claims from Prime Puzzles problem 49, each with uncovered = 0:

| K | v_3(K) | covering lcm |
|---|---|---|
| 4423988484893019254861842753686117 (Keller) | 1 | 720 |
| 1139634035240881514319907179 (Masser) | 1 | 720 |
| 4563308668738348027581 | 1 | 360 |
| 1934207927446756722099 | 1 | 360 |
| 7592506760633776533 | 4 | 720 |

21484572547591559649 is also divisible by 3, but no covering was given for it. It has no PRP for n < 3000.

For each, m = K/3^{v_3} fails 2D immediately: other rows have PRPs at small k. For example, for m = 93734651365849093 the first PRP k in rows l = 0…7 is [192, 5, 26, 4, —, 3, 16, 5], with row 4 = K. A covering-type YES needs 3^l m to be such a number for **every** l ≥ 1. The smallest known one is 7.6·10^18, against 78557 for the plain problem. That is suggestive but not a proved lower bound.

**C4. Simultaneous rows (Task 2) [PROVED via SAT/density, with the complete prime list].** I used every prime p with ord_p 2 | 720: 38 primes, a complete factorisation of 2^720 − 1, checked by a product test. A YES must cover all rows simultaneously.

- *Density bound [PROVED].* A prime with d_p ≥ R is active in at most ⌈R/d_p⌉ of R consecutive rows. Summing ⌈R/d_p⌉/ord_p 2, plus 1/2 for row 0, gives at most 11 consecutive rows coverable. The all-rows average Σ 1/e_p over this pool is about 0.92 < 1.
- *SAT (CaDiCaL, exact).*
  - Rows {0, 1}: coverable. So m and 3m can be simultaneously Sierpiński.
  - Row {1} alone: coverable.
  - Rows {0, 1, 2}: unresolved after 900 s.
  - Rows {1, 2}: unresolved after 900 s.
- *Row 0 plus column 1, both covered at once [VERIFIED] (`double_sat.py`).* Using primes with ord_p 2 | 720 or ord_p 3 | 144, SAT finds a solution in 1.8 s. CRT gives a 256-digit m ≡ 1 (mod 6) with these properties:
  - m is Sierpiński: every k mod 720 is covered, and the prime 3 is used.
  - 2m is a base-3 Sierpiński number: every l mod 144 is covered.
  - The rest of the family fails quickly. Rows l = 1…7 have their first PRP at k = 322, 1015, 15, 71, 200, 10, 99. Columns k = 2…6 have theirs at l = 102, 79, 32, 196, 74.
  - Column k = 7 has no PRP for l < 2000, yet 701 of those l escape every covering prime. That is a short-range miss, not a covering.
  - So double (row plus column) Sierpiński numbers exist, and they are just as far from YES as the plain ones.
- *Row 0 plus column 1 by shifted classical coverings.* I took the 78557 covering on row 0 and the 125050976086 covering on column 1. They share the primes 5, 7, 13, 19 and 37, and **no** pair of shifts (2^j, 3^i) makes them compatible: 0 of 36·144 combinations. Coverings for different lines cannot be chosen independently, because a shared prime's single residue m mod p fixes its classes on every row and column at once.
- *2D structure.* Rows l and l + d_p see the same prime p, with its class shifted by a fixed s_p. For primes with 3 ∈ ⟨2⟩ (d_p = 1, e.g. 5, 11, 13, 19, 37, 61, 97, 181, 577), each row is the previous row shifted modulus by modulus. Independent coverings on infinitely many lines would need infinitely many fresh primes, which is case N4(iii).

## 4. Theory: routes either way

- **NO.** There is no unconditional route. Even "infinitely many Pierpont primes 2^k 3^l + 1" (m = 1) is open. EO79 Theorem 2 (positive lower density of good m) is the best known result. A conditional route would be: a 2D form of Erdős's Conjecture 2 (unbounded least prime factor forces infinitely many primes) or Granville–Pappalardi-type heuristics, plus a proof that no 2D covering exists at all. The latter needs the repo's distortion bound to hold uniformly in e_p.
- **YES.** The only known mechanisms are (i) and (ii) from N4. Both need a prime with e_p > 4·10^5 and a nesting structure the repo shows to be starved. Kind (iii) has no precedent and probability 0 in the Cramér model:
  - With a positive local factor κ_m, about c·H primes are expected below height H, so P(no prime) ≲ e^{−cH} → 0.
  - κ_m = 0 without an exact covering would need an "asymptotic covering". The variance Σ_p 1/(e_p p) converges, which makes such conspiracies atypical.

# HYP.md — hypothesis agent ("big leaps"), 2026-11-08

I cut this to 8 hypotheses because the budget got tight. H4, H2, H6 and H3 are the PRIORITY ones, ranked by chance of being true times payoff.
Labels follow BRIEF rule 1. Scratch script: /tmp/hyp/t2star.py (it has a planted-failure control).

## 0. New facts established here (read these first)

**F1 (PROVED, derivation).** Here is Chamberland's Type II with no coprimality assumption. Write s1 = g·a and s2 = g·b with g = gcd(s1, s2). Then q ≡ -1 (mod 4gab), so q = 4gab·c - 1. Put d = cr - g. This gives:

  **n has a Type II rep  <=>  there are A, g, d, r >= 1 with n + r = 4·A·g·d and r | g + d.**

You may take A = ab to be arbitrary, by setting a = A and b = 1. Compare Type I: n + k + l = k·l·t with k ≡ t ≡ 3 (mod 4).

**F2 (PROVED).** Let g = 1 above. Then Type II contains Type II\*, the set of n with a point of S_n : xyz - x - y = n that has 4 | x. (Take s1 = x/4, s2 = 1, q = xz - 1.)

- So Type I is the set of points of S_n with x ≡ z ≡ 3 (mod 4), and Type II\* is the set of points of S_n with x ≡ 0 (mod 4).
- A point of S_n with residues (3, 0, 3) mod 4 gives a Type I solution and a Type II solution at the same time (by the x↔y symmetry).

**F3 (VERIFIED, n ≡ 1 mod 4, n <= 20000, with t2star.py).** Type II\* is strictly smaller than Type II.

- Non-squares with no Type II\* rep: 33, 105, 145, **193**, 369, 385, 753, 1705, 2041, 2049, **2521**, 2961, ... These include primes (193, 2521).
- **105 and 2961 have no rep in Type I ∪ II\*.** So the extra gcd parameter g in Type II is essential to C\*.
- Controls:
  - No odd square has a Type II\* rep (consistent with F2 plus Elsholtz–Tao).
  - Planted bogus rule (allow x ≡ 2 mod 4): 21 of 21 odd squares <= 2000 get reps.
  - Type II\* ⊆ Type II held with 0 exceptions.

## Table (all statements are CONJECTURED unless marked)

| # | Statement | Analogy | Cheap falsifying test | If true → E–S (weak links marked !) |
|---|---|---|---|---|
| **H4 (P1)** | **2-adic equidistribution of points.** Let N(n) be the number of integral points of S_n ∪ T_n, where T_n is F1's variety. Let N_Ω(n) be the number of those points in the Egyptian region (Type I or Type II). Then N_Ω(n) >= δ·N(n) for every non-square n ≡ 1 (mod 4), for some fixed δ > 0. For squares N_Ω = 0. | Linnik / Duke equidistribution of lattice points among local classes. Here squares play the role that spinor-exceptional classes play. | Compute min over non-squares of N_Ω/N in each dyadic range up to 1e6. It is falsified if the minimum tends to 0 along some sequence. (It already does for Type I alone, through V. Test the union.) | It gives C\* immediately, because N(n) >= 1 always: t = 1 gives a point. ! An equidistribution proof needs Kloosterman / spectral input for one specific n, which is the sieve barrier D7. |
| **H2 (P2)** | **The square obstruction is Brauer–Manin for 2-adic strong approximation.** β = (-n, xz-1) + (z, 1-xz) lies in Br(S_n). I checked the residues along xz = 1 (where -nz = 1, a square), z = 0 and x = 0; the other boundary divisors are NOT checked. Prediction: inv_q β is constant on S_n(Z_q) for every odd q, and inv_2 on the Ω-cells forces a contradiction exactly when n is a square. | Colliot-Thélène–Xu: BM for strong approximation. Hilbert reciprocity. Prop C is the computation at odd q. | On random integral points of S_n (any residues, e.g. z = 1), compute Σ_{odd q} inv_q β. It is falsified if this sum depends on anything other than (n, x mod 8, z mod 8). | Cor D becomes conceptual. "Squares are the only BM obstruction" is then a CT-type conjecture. ! V is a non-BM failure: **V is not closed under multiplying by squares** (105·9 = 945 is not in V; the U-file has no t·k² pattern). So BM explains squares only, and C\* needs a non-BM input. |
| **H6 (P3)** | **Small height.** Every non-square n ≡ 1 (mod 4) has a Type I rep with t <= C·log² n or a Type II rep with c <= C·log² n. | GRH bounds on the least non-residue (Ankeny). Prop C ties reps to non-residues. | Extend es_combined to record the minimal t or c. Six primes escape every t <= 199 in Type I alone; check whether Type II catches them at small c. | A finite search per n. A GRH-conditional route is plausible. ! You still need a divisor of a specific integer nz+1 in a residue class (barrier S3). |
| **H3 (P4)** | **Class-number-relation analogue.** With 2-adic character weights, the count R_Ω(n) has a mock-modular generating function whose shadow is ∝ θ = Σ q^{k²}. So Σ_s R_Ω(n - s²) (suitably weighted) is an explicit divisor sum. | Kronecker–Hurwitz: Σ H(4n - s²) = 2σ(n) - λ(n). Zwegers' Appell–Lerch sums. The weight Σ_{d\|N} χ_{-4}(d) = r_2(N)/4 arises naturally because "a divisor ≡ 3 mod 4" = (1 - χ_{-4})/2. | Compute G(n) = Σ_s R_I(n - s²) up to 1e5. Fit it against divisor sums of level 4 and 8. It is falsified if no level-8 divisor-sum basis fits. | Positivity would follow from an identity, which bypasses sieves. ! The untwisted d(N) parts are not modular, so the identity may only hold for the χ-twisted part. |
| H8 | **Disjoint exceptions.** The Type II exceptions among non-squares are finite, {4545}, and disjoint from V. | Spinor exceptions are finite in number. | Search Type II beyond 2e7 with q <= 4N+1. It is falsified by a second non-square Type II failure that also lies in V. | This is C\* itself. ! It is only evidence; there is no mechanism. |
| H5 | **Spinor/ternary form.** Some ternary Q has genus classes matching Type I and Type II, and the squares are its spinor exceptions. | Duke–Schulze-Pillot. | Same test as H2's weak link: the exceptions of a spinor-type explanation must be unions of square classes t·k². | **Likely FALSE for V** (V is not square-class closed, as above). It could hold only for squares, which add nothing. |
| H7 | **Unipotent lifting.** Conjugating [[A,n],[z,B]] by [[1,k],[0,1]] maps S_n to S_{n'} with n' = n + kz(y - x - k). This identity is PROVED. Hope: it gives a descent. | Vieta / Markoff orbit descent. | Not needed. | **DEAD as a descent.** Taking k ≡ 0 mod 4 just re-parametrises points, and the fibres have no infinite group (log, Session 2c). |
| H1 | Type II = Type II\* (only points of S_n with 4 \| x). | Unifying on one surface. | Done: t2star.py. | **FALSE** (F3: 33, 105, 193, ...). The corrected unification is F1. |

## The most useful next tests
- H4: the ratio test using the F1 form, which is cheap in C with the same slicing as es_combined.
- H2: the invariant-constancy test.
- H6: the minimal height of Type I ∪ II reps for the six hard primes that escape t <= 199.

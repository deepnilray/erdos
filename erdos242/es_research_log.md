# Erdős–Straus research log (Erdős #242)

Started 2026-11-08. Goal: prove 4/n = 1/x + 1/y + 1/z for every n ≥ 2.

## Literature state (checked 2026-11-08)
- Verified to 10^18 (Mihnea–Dumitru, arXiv 2509.00128). No accepted proof.
- Chamberland (INTEGERS 26 (2026) #A42): reduces to the unproved "Prime Representation Conjecture" p = qr − 4 s1 s2, q ≡ 3 mod 4, s1, s2 | (q+1)/4.
- Bradford (arXiv 2602.11774): valid families, no global covering proof (secondary report, unverified).
- Cambridge Open Engage preprint (Aug 2026) claims a proof via a "residual constant"; unrefereed, unverified.
- Mordell: only primes p ≡ 1, 121, 169, 289, 361, 529 (mod 840) remain; all six are squares mod 840, so no finite set of polynomial identities can cover them (Schinzel).

## Setup (exact)
For prime p ≡ 1 mod 24, put x = (p+3)/4 + t, m = 4x − p = 4t + 3, n = px.
Then gcd(m, n) = 1 and 4/p = 1/x + 1/y + 1/z is solvable iff some d | n² satisfies d ≡ −n (mod m); then y = (n+d)/m, z = (n + n²/d)/m.

## Verified result 1 (computation, es_experiment.py)
All 765 primes p < 3·10^5 in the six hard classes have a decomposition with offset t ≤ 14.
Minimal offset histogram: {0:266, 1:159, 2:211, 3:38, 4:43, 5:32, 6:3, 7:11, 9:1, 14:1}.
Worst case: p = 118801, t = 14, (x,y,z) = (29715, 59834124, 5077395546660).
Every decomposition is checked with exact Fraction arithmetic in the script.

## Structural observation (algebraic, to be written up)
Since 4x = p + m, we have x ≡ p/4 and n ≡ p²/4 (mod m). Writing d = p^i · e with i ∈ {0,1,2}, e | x², the condition reads
  p^i · e ≡ −p²/4 (mod m).
If x is prime (x = q), e ∈ {1, q, q²} with q ≡ p/4, which leaves nine congruences on p modulo m, for example
  i=2, e=1: m | 5;  i=2, e=q: p ≡ −1;  i=1, e=1: p ≡ −4;  i=2, e=q²: p² ≡ −4 (mod m).
So an offset t is blocked for a prime x exactly when p avoids these classes mod m = 4t+3. A proof must therefore handle the case where x_t = (p+4t+3)/4 is prime for many t at once, which ties the problem to prime constellations. Next: tabulate all nine congruences, then study which p survive offsets t = 0..T when every x_t is prime or a prime times a small cofactor.

## Theorem A (PROVED, 2026-11-08) — see erdos_straus_family.tex/pdf
If p = mut − m − u with m, u, t positive integers and mt ≡ 1 (mod 4) (forces m ≡ t ≡ 3, p ≡ 1 mod 4), then
4/p = 1/(uw) + 1/(p·w·X) + 1/(u·w·X), w = (mt−1)/4, X = ut−1.
u = 1 is Obláth's criterion (p+1 has a divisor ≡ 3 mod 4). Route e = x² is dead (divisors of p²+4 are ≡ 1 mod 4).
VERIFIED to p < 2·10^7: all 39391 hard primes have a hit, worst minimal u = 890 at p = 5101441 (u = 161 at p = 30241). Exact-Fraction check of the identity passed for all; controls fired (39391/39391 and 55265/78782).
Prior art: NOT identical to Chamberland's p=qr-4s1s2 representation-wise (VERIFIED p<400: p=17 has Chamberland q=7 but no family m=7; p=37 has family m=3 but no Chamberland q=3); equivalence as covering statements unknown; Elsholtz-Tao not checked symbol by symbol; no priority claimed. erdosproblems.com/242 lists the problem as open, no AI results (checked 2026-11-08).

## Open next steps
1. Enumerate the full congruence list for x prime, x = q·r (r small), x = q².
2. Check whether the survivors of finitely many offsets are forced into a contradiction by a mod-m_t argument (Schinzel-type obstruction means expect failure; find exactly where).
3. Compare against Chamberland's Type II parametrization to see whether the Prime Representation Conjecture is equivalent to this offset covering.

## Proposition B (PROVED, 2026-11-08)
p ≡ 1 mod 4 is in the family iff exists t ≡ 3 mod 4 and a | pt+1 with 4 | a, a ≡ −1 (mod t). VERIFIED independently (es_t_form.py): all 4519 hard primes < 2·10^6 hit with t ≤ 367 (worst p = 830041, t = 367, m = 87, u = 26); control p = 7 gives no hit.
STATUS: full conjecture still OPEN. Remaining gap: show some t works for every prime (a multiplicative-covering statement, Schinzel barrier applies to any fixed finite set of t).

## Covering analysis (subagent, spot-checked 2026-11-08)
Reduction: p in family iff exists m≡3 (4), u≥1, divisor a of p+m, 4|a, a≡−1 (mod m); t=(a+1)/m. Each (t,m) is one class p ≡ −m (mod mt−1).
t=3 and p≡1 (8): works iff (3p+1)/4 has a prime factor ≡ 2 (mod 3).
PROVED (agent, quadratic reciprocity): no finite set of (t,m) pairs covers all primes (Dirichlet + (−m/a') = −(2/m)^e). Fixed t with m unbounded is NOT excluded and is what the computation uses.
VERIFIED p<5·10^6: greedy t=3,7,15,11,23,39,31,47 ... covers 78.7%, 95.9%, 98.2%, 99.5% (5 t), 99.943% (12 t), 99.997% (all useful t≤199). Uncovered by every t≤199: 594721, 601849, 830041, 1040161, 2466481, 4149601.
Sufficient failure of prime t≡3 (4): (p/q)=+1 for every odd prime q | pt+1. Needs sieve/primes-in-progressions input, not a congruence on p.

Large-prime sample (VERIFIED, random, seed 20261108): 40 hard primes at each of 12/15/18 digits, all in the family, min-u <= 12/8/5. Control p=1000003 (3 mod 4): no hit. Script es_large.py.
IDENTITY of 'Ado's trust' in the user's message read as Erdős–Straus (voice-to-text); Andrica paper already exists per 26 Oct chat.

Symbolic CAS check (es_symbolic.py, sympy): 4/n − [1/(uw)+1/(nwX)+1/(uwX)] simplifies to 0 identically in m,u,t with n = mut−m−u, w = (mt−1)/4, X = ut−1; (mt−1)(ut−1) − (nt+1) = 0; control with X→ut does not vanish. This is a CAS confirmation of the hand proof, not a kernel-checked proof.
Lean formalization NOT done: installing Lean (elan installer download) was denied by the permission classifier; left to the user.

---
# Session 2 (2026-11-08): attack on the GAP. Worst news first.

## Worst news
1. VERIFIED (exhaustive, hard primes <= 2e6): the number of family representations R(p) = #{(m,t,u)} does not have a growing minimum.
   mean R by decade: 5.2 (1e3), 9.2 (1e4), 15.2 (1e5), 19.1 (1e6) ~ 0.09 ln^2 p, but min R = 1 (p=2521, 21169), 3 (p=104161), 2 (p=1282009).
   A Poisson model with the observed mean would make R=2 at mean 19 a ~1e-6 event per prime; it occurred. The lower tail is heavy, so no probabilistic
   heuristic here supports a proof (CONJECTURED model, and it fails its own sanity check).
2. VERIFIED to 2e7 (39391 hard primes, all covered): smallest working modulus m peaks at m = 583 (p = 1282009); no larger value occurs from there to 2e7
   (records: 3, 11, 23, 87, 159, 191, 223, 583). Growth is irregular, not a clean function of p.
3. PROVED (Prop C/Cor D below) and VERIFIED: the family is NOT a statement about all integers. Every odd perfect square is missed (<= 3000),
   plus composites 105, 465, 585, 801, 2641, 2929, 2961. So primality of p is genuinely used and a purely integer-covering proof cannot exist for this family.
4. Any sieve / primes-in-progressions route yields only "exceptional set of density 0" (see S below). No route to "every prime" found.

## Prop C (PROVED, hand proof; VERIFIED n = 1 mod 4 <= 20001: 40261 hits, 0 violations; control 61% violations)
Let n = 1 mod 4, m = 3 mod 4, a = mt-1 with 4 | a, a | n+m (n+m = ua). Write a = 2^e a', e >= 2, a' odd. Then Jacobi (a'/n) = -(2/m)^e.
Proof. (mt-1)(ut-1) = nt+1, so for each odd prime q | a': mt = 1, nt = -1 (mod q); q does not divide n, m, t. Since mt is a square mod q, (m/q) = (t/q);
since nt = -1, (n/q)(t/q) = (-1/q). So (n/q) = (-m/q) and, multiplying with multiplicity, (n/a') = (-m/a'). Reciprocity with n = 1 mod 4 gives (n/a') = (a'/n).
With m = 3 mod 4: (m/a') = (a'/m)(-1)^{(a'-1)/2} and (-1/a') = (-1)^{(a'-1)/2}, so (-m/a') = (a'/m). Finally a = -1 mod m gives a' = -(2^{-1})^e mod m,
so (a'/m) = (-1/m)(2/m)^e = -(2/m)^e. QED.
Cor D (PROVED). No odd perfect square n = k^2 is represented. Proof: gcd(a, n) = 1, so (a'/n) = 1; thus (2/m)^e = -1, i.e. e odd and m = 3 mod 8; e >= 2 forces e >= 3, so 8 | a | n+m and n = -m = 5 (mod 8), contradicting n = 1 (mod 8). QED.
Cor E (PROVED, same argument). For a prime p = 1 mod 8 (all six Mordell hard classes are 1 mod 8) every representation has (a'/p) = -1, hence a' has a prime factor q with (q/p) = -1, so a >= 4 l(p), l(p) = least prime quadratic non-residue.
VERIFIED link (es_lnr.py, 732 hard primes in [1e5, 4e5]): mean R falls as l(p) grows: l=11: 14.4, 13: 12.9, 17: 11.7, 19: 10.1, 23: 9.2. The rarest-representation primes are those with large l(p).
Consequence: a covering proof must, for p a QR at all small primes, produce a divisor of p+m whose odd part contains a prime that is a non-residue mod p. That is a quadratic-character
condition on the factorisation of p+m, the kind of input that Siegel-zero-type phenomena control. This is the structural reason the problem is hard, not just a gap in technique.

## Dead-idea ledger
D1 DEAD (PROVED): finitely many (m,t) cannot cover. Simpler proof than the reciprocity one: class p = 1 mod L, L = lcm of moduli M_i = m_i t_i - 1, contains primes (Dirichlet); p = -m_i mod M_i would need M_i | m_i + 1, impossible as t_i >= 3.
D2 DEAD (log): divisor choice e = x^2.
D3 DEAD (log, Schinzel): finitely many polynomial identities cannot cover the six Mordell classes.
D4 DEAD (VERIFIED to 3000, PROVED for squares): "family covers every n = 1 mod 4". False.
D5 DEAD: Poisson/probabilistic model of R(p) as evidence for a proof (fails sanity check, point 1).
D6 DEAD (VERIFIED p <= 400): Chamberland equivalence via q = m, q = t, or inclusion of q-sets. C.q is never contained in F.m or F.t; F.m in C.q for only 13/37 primes (control with planted wrong rule changed the outcome 7/7 vs 4/7 at p <= 60).
   Both formulations have a rep for all 37 primes (trivially consistent). Equivalence as covering statements: STILL UNKNOWN. Chamberland's rule here is as stated in the task, not re-read from the paper; q searched only up to 4p+1.
D7 DEAD (barrier, not a proof): sieving to cover all p. See S.

## S: sieve / primes-in-progressions analysis
Two sufficient mechanisms. Fixed m: (p+m)/4 has a prime factor q = -4^{-1} (mod m) => a = 4q works. Fixed t (Prop B): pt+1 has a prime factor q = -4^{-1} (mod t) => a = 4q works.
(S1) PROVED (3 lines): for p = 1 mod 8, t = 3 works iff (3p+1)/4 has a prime factor = 2 (mod 3); m = 3 works iff (p+3)/4 has a prime factor = 2 (mod 3). (a = 4c, 4c = 2 mod 3 iff c = 2 mod 3; a product of primes = 1 mod 3 is = 1.)
(S2) NOT PROVED HERE (standard upper-bound sieve + Bombieri-Vinogradov, derivation only sketched): for each fixed modulus the primes p <= x failing it number << pi(x) (log x)^(-1/phi(modulus)). So each fixed modulus covers a density-1 set of primes. This is weaker than the exceptional-set results of Vaughan and Elsholtz-Tao; I have not re-derived those and claim nothing new.
(S3) BARRIER: a proof for every p needs a divisor-in-a-class statement about one specific integer p+m (or pt+1) for some m or t that you may choose. Sieves cannot give an existence statement for a single integer (parity / no lower bound for specific values). Choosing m or t as a function of p just returns the equation p = mut - m - u. Dispersion-method (Bombieri-Friedlander-Iwaniec-type) arguments for the family would give an asymptotic for the average of R(p) and, with a second moment, positivity for almost all p; a lower bound R(p) >= 1 for every p would need control at the same strength as the original problem (point 1: min R does not grow).
(S4) CONJECTURED: min over hard p in [X, 2X] of R(p) tends to infinity. The data above neither supports nor refutes it (min R = 3, 2 at 1e5, 1e6).

## Controls used this session
es_minm.py tamper (identity corrupted): 4519/4519 failures caught. es_minm.py control (p = 3 mod 4): 74515/74515 no hit (the mod 4 argument predicts exactly this). es_count control (p = 3 mod 4): R = 0 for all 4189+ primes per decade.
es_jacobi.py control pairs (a not = -1 mod m): 61% violate the formula, so the check has power. es_compare bogus rule changed the output.
New scripts: es_minm.py, es_compare.py, es_allints.py, es_jacobi.py, es_count.c, es_lnr.py. Log: minm_2e7.log.

---
# Session 2b: structured attack, rounds 1-5 (2026-11-08). No proof yet. Ledger below.

## Reformulations used (all PROVED, elementary)
(R-a) p in family  <=>  exist k = 3 (mod 4) and l >= 1, gcd(k,l)=1 (p prime), with k | p+l, l | p+k and t = (p+k+l)/(kl) = 3 (mod 4).   [p = klt - k - l]
(R-b) (tk-1)(tl-1) = pt+1.  Fixed t: pt+1 needs a factorisation with both factors = -1 (mod t) and 4 | one of them.
(R-c) The family is the union, over m,t = 3 (mod 4), of the residue classes p = -m (mod mt-1). Uncovered set U = {n = 1 mod 4 : n in no class}.
Special cases: l = 1: Oblath (p+1 has a divisor = 3 mod 4).  l = 2: p+2 has a divisor = 5 (mod 8).  t = 1 would always work (p+1 = (k-1)(l-1)) but t = 1 violates t = 3 (mod 4): the mod-4 condition IS the whole difficulty.

## Round 1: does the two-squares decomposition p = x^2+y^2 explain the parameters?  DEAD.
es_pattern.py on 2370 hard primes < 1e6: best linear forms alpha*x+beta*y (|alpha|,|beta| <= 8) hit the reps' parameters no more often than a planted control with random (x,y) (top counts 47 vs 58). Ledger: D8.

## Round 2: look at the hardest primes.
Primes with R(p)=1,2 (2521, 5569, 21169, 43969, 1201, 3361, 5209, 9601): in every rep pt+1 has only 2-5 prime factors and a is 4*(one or two primes). Thin factorisations, no algebraic pattern.

## Round 3: characterise U exactly (VERIFIED, es_U.c).  KEY STRUCTURAL FINDING.
U = {all odd squares} U V, V a sparse set of composites, all = 1 mod 8.  Up to 3e5 (complete): |U| = 294 = 273 odd squares (= ALL odd squares <= 547) + 21 non-squares, 0 primes.
Partial run reaching n >= 4.8e6: 1095 odd squares (= all odd squares in range, consistent with Cor D) + 26 non-squares (5 beyond 3e5: 698569, 1116801, 1126945, 1243089, 1618521), 0 primes.
V counts: 7 below 3e3, 21 below 3e5, 26 below 4.8e6. Sparse and thinning; whether V is finite is UNKNOWN (CONJECTURED sparse).
Target statement (CONJECTURED): the family represents every non-square n = 1 mod 4 outside V; since V has no primes in range, this would give Erdos-Straus. The obstruction to squares is exactly Prop C/Cor D (a quadratic-character obstruction, the Brauer-Manin-like phenomenon); for non-squares the character (./n) is nontrivial.
Why this matters: the question moves from 'cover primes' to 'what extra obstruction (beyond the trivial-character one) makes V?'. Understanding V's elements is the next step.

## Round 4: the least non-residue is the carrier (VERIFIED, es_lnr2.py, 2370 hard primes < 1e6).
l(p) | pt+1 in some rep: 2069/2370 (87%); l(p) | a: 1767 (75%).  Planted control (random residue prime): 89 and 68. So Prop C's necessary prime is typically the smallest one available.
Burgess gives l(p) << p^{0.1516} unconditionally; GRH gives << log^2 p. A proof from here needs an explicit construction of (m,t,u) from q = l(p). Not found. Rep in which l(p) divides pt+1 fails for 13% of hard primes, so 'least non-residue only' is insufficient; a second non-residue or a product is needed.

## Round 5: restrict the shape of a = mt-1 (VERIFIED, es_shape.py).
Some rep with a = 4q (q prime) for 2216/2370 = 93.5%; odd part of a prime: 2336 (98.6%); odd part with exactly two primes: 2304. No single shape covers all hard primes < 1e6.

## Ledger additions
D8 DEAD (control-tested): linear forms in two-squares decomposition.
D9 DEAD: a = 4q only (93.5%), a with prime odd part (98.6%), l(p) | a only (75%) - none reaches 100%, so a construction must allow several shapes.
D10 OPEN, highest value: characterise V (is it finite? what obstruction?) and prove 'non-square n outside V is represented' by an induction/descent on integers, where composite n gives extra structure. Next rounds: (6) structure of V elements' Jacobi tables; (7) hypothesis test: V = {n : (q/n) = +1 for all primes q < c*log n ...}; (8) prove the representation for n with a large prime factor.
Files: es_reps.c es_pattern.py es_U.c es_lnr2.py es_shape.py U_3e5.txt.  (reps_hard_1e6.txt is regenerable with es_reps.c; not committed.)

## Round 3 final data (VERIFIED, es_U.c; supersedes the partial counts above)
The 12e6 run hit its 580 s timeout and was NOT completed to 1.2e7. Guaranteed complete range: n <= 4,800,481 (the file's largest entry; 1095 squares = every odd square <= that bound).
In that range: |U| = 1122 = 1095 odd squares + 27 non-square composites, 0 primes. (An intermediate message quoted 26 non-squares from a partially flushed file; 27 is the final count.)

---
# Session 2c: rounds 6-7 (2026-11-08)

## Reformulation (PROVED, elementary): matrix / Farey / surface form
p = klt - k - l  <=>  det [[A, p],[t, B]] = 1 with A = tk-1, B = tl-1, i.e. an SL2(Z) matrix congruent to -[[1,-p],[0,1]] mod t with off-diagonal entries exactly (p, t).  Geometrically: integral points on the cubic surface S_n : xyz - x - y = n (equivalently (xz-1)(yz-1) = nz+1), a Markoff-type surface; odd squares are the Brauer-Manin-type failures (Cor D). Hasse-principle failure for the surface is thin (the uncovered set U = squares + sparse V).
Unlike Markoff surfaces S_n has no infinite Vieta-jumping group (for fixed z the fibre is a hyperbola), so the orbit/strong-approximation machinery of Ghosh-Sarnak does not apply directly. NOT checked against the literature (Loughran-Mitankin, Bright-Loughran); next step is to read them.

## Round 6: is V the set of integers with unusually large least non-residue l(n)?  DEAD (VERIFIED, es_ell.c, n <= 4.8e6).
The 27 non-square exceptions have SMALL l(n): e.g. 465 and 2929 have l = 7, 105 has l = 11, 1618521 has l = 13; the largest l among them is 37.
Covered non-squares have l(n) up to 61 (e.g. covered n near 3.3e6 with l = 61).  So (i) V is not characterised by large l, and (ii) 'l(n) small => n represented' is FALSE (counterexamples 465, 2929, ...).  This kills the construction 'build (m,t,u) from the least non-residue alone'. Ledger D11.

## Round 7: are primes special inside the non-square hard classes?  NO (VERIFIED, es_Rcomp.c, window [1e5,3e5)).
Non-square n in the six hard classes: primes (492): mean R = 12.68, frac(R <= 3) = 1.2%, zeros 0.  Composites (883): mean R = 12.07, frac(R <= 3) = 2.0%, zeros 0.
So primes behave like typical non-square members of these classes; nothing in the data says primality helps. The exceptional set V is composite-only in range, but the zero-rate of composites in this window is already 0, so the evidence that primes are safer than composites is weak. The problem is the integral Hasse principle for S_n on non-squares; Erdos-Straus needs it on primes.
Ledger D11 (above), D12 DEAD: 'primes are special'.

---
# Session 2d: literature round (2026-11-08). Chamberland read from the primary source (INTEGERS 26 (2026) #A42, math.colgate.edu/~integers/aa42/aa42.pdf).

## What the paper actually says (quoted/paraphrased from the PDF text)
Theorem 1 (exact iff): for prime p there are a<=b<=c with p not| a, p | b, p | c and 4/p = 1/a+1/b+1/c   <=>   p = qr - 4 s1 s2, q,r,s1,s2 in Z+, q = 3 (mod 4), s1, s2 | (q+1)/4.
So Chamberland's representation is EXACTLY the statement 'p has a Type II solution' (Elsholtz-Tao terminology: Type II = exactly two denominators divisible by p). Explicit identity (4):
4/(qr-4s1s2) = 1/(r(q+1)/4 - s1s2) + 1/(((q+1)/4)(qr-4s1s2)) + 1/((1/s1)((q+1)/4)(r(q+1)/(4 s2) - s1)(qr-4s1s2)) -- see paper eq. (4)-(6) for the exact form.
Conjecture 2 = 'every prime has a Type II solution'; it is an extrapolation from computer tests, not a theorem. The paper makes no equivalence claim with other families. No r-range restriction: r any positive integer, s1,s2 not required distinct; q unbounded (my es_compare.py search used q <= 4p+1, so it can only under-count Chamberland reps).

## Resolution of the 'Chamberland equivalence' item (VERIFIED + PROVED)
VERIFIED (exact fractions, 34336 reps of hard primes < 1e6, es_types.py): EVERY family solution 4/p = 1/(uw)+1/(pwX)+1/(uwX) has exactly ONE denominator divisible by p: the family is a TYPE I family. Chamberland's is Type II. Hence they are different families by construction (consistent with the 'p=17 has q=7 but no m=7' check), and neither conjecture is known to imply the other. Elsholtz-Tao/Bradford: any solution has p not| a, p | c, so every prime solution is Type I or Type II; thus Erdos-Straus <=> for each p, Type I or Type II exists. Each of the two conjectures is a priori STRONGER than Erdos-Straus.

## New: reciprocity law for Chamberland's Type II (PROVED; VERIFIED on all 748 reps with q <= 4p+1, p = 1 mod 4, p < 400; wrong-sign control fails 748/748)
For p = qr - 4 s1 s2 with q = 3 mod 4 (q any odd positive integer, Jacobi symbols), s_i | (q+1)/4:   (p/q) = -(2/q)^{v2(s1)+v2(s2)}.
Proof. p = -4 s1 s2 (mod q), (-1/q) = -1 and (4/q)=1, so (p/q) = -(s1 s2/q). For odd part s' of s_i: q = -1 (mod s'), so (q/s') = (-1/s'); reciprocity with q = 3 mod 4 gives (s'/q) = (q/s')(-1)^{(s'-1)/2} = 1. The power of 2 in s_i contributes (2/q)^{v2(s_i)}. QED.
Parallel with Prop C (Type I): Type II needs the MODULUS q to be a quadratic non-residue-type for p ((p/q) = -1 unless an odd 2-power and q = 3 mod 8), Type I needs the ODD PART a' of a to satisfy (a'/p) = -(2/m)^e. Both obstructions are quadratic-reciprocity laws of the same shape; both kill odd squares p = k^2 in the same way (Jacobi symbol of a square is +1), which is the Mordell/Schinzel 'squares mod 840' phenomenon seen from both Type I and Type II.

## Literature seen (search results only; not read in full - verify before citing)
Loughran-Mitankin, 'Integral Hasse principle and strong approximation for Markoff surfaces' (arXiv 1807.10223): for x^2+y^2+z^2-xyz = m, a Brauer-Manin obstruction forces m-4 mod squares into <-1,2,3,5>; BM-obstructed m are O(B^{1/2}); non-BM Hasse failures exist with count >> M^{1/2}/log M (reported by search snippets, unchecked).
Elsholtz-Tao (arXiv 1107.1010): sum_{p<=N} f(p) between N log^2 N and N log^2 N loglog N; odd squares have neither Type I nor Type II solutions (quoted in Chamberland's intro). Dao and others extend BM analysis to Markoff-type cubic and Wehler K3 surfaces (2202.07142, 2302.11515; unchecked).
Analogy NOT yet checked: our surface xyz - x - y = n has BM-type obstruction exactly at squares (Cor D); the sporadic composite exceptions V would then be 'non-BM' failures, which in the Markoff case are conjecturally thin but do exist.

---
# Session 2e: combined-type coverage + Loughran-Mitankin assessment (2026-11-08)

## Round 8: Type I (family) union Type II (Chamberland) -- VERIFIED to n <= 2e7 (es_combined.c, Chamberland q <= 4N+1)
For n = 1 mod 4, 5 <= n <= 2e7 (output combined_2e7.txt):
  - odd squares: 2235; with a family rep 0; with a Type II rep 0 (matches Elsholtz-Tao: odd squares have neither type -- this is an independent theory control of the Chamberland code).
  - missing family: 2264 = 2235 squares + 29 non-squares.   missing Type II: 2236 = 2235 squares + ONE non-square, n = 4545 (= 3^2 * 5 * 101).
  - missing BOTH: 2235 = exactly the odd squares.  So Type I union Type II covers EVERY non-square n = 1 mod 4 up to 2e7, primes included.
  - 4545 has no Chamberland rep for q <= 6e6 (checked separately, ~1300 n) but it has a family rep; absence of a Type II rep for 4545 is NOT proved, only unseen.
  - All 27 family exceptions found earlier (<= 4.8e6) have explicit Type II reps (es_Vcham.py), e.g. 105 = 47*3 - 4*3*3 (3 | 12), 465 = 7*67 - 4, 698569 = 19*36767 - 4.
Controls: bogus rule (drop s_i | (q+1)/4) makes all odd squares acquire Type II reps (9/9 at N = 400), python and C implementations agree exactly at N = 60000 (138 / 122 / 121), squares < 1e5 have no Type II rep with q <= 1e5.
New structural observation (CONJECTURED): the sporadic non-square failures of the two types are DISJOINT (V for Type I, {4545,...} for Type II), and the only common failures are squares. If this persists, 'every non-square n = 1 mod 4 is Type I or Type II' is the right integer statement; Erdos-Straus for primes would follow, since a prime is a non-square. No proof of this statement.

## Loughran-Mitankin (arXiv 1807.10223): what the paper does and does not give (ar5iv text; sections beyond ~4.1 only seen through a summary)
Verbatim statements: Thm 1.1/1.2: #{|m| <= B : weak approximation holds / closure property} << B^{1/2}; Thm 1.3: Brauer-Manin obstruction => m-4 mod squares in <±1,2,3,5>; Thm 1.4: #{m: local solutions everywhere but Br-Manin set empty} ~ B^{1/2}/(log B)^{1/2}; Thm 1.5: Hasse failures explained by BM are >> B^{1/2}/log B. They cite Ghosh-Sarnak numerics suggesting B^gamma (1/2 < gamma < 1) Hasse failures, i.e. MORE than BM-explained ones.
CORRECTION to my earlier remark: the paper does NOT prove that non-BM Hasse failures are thin. It computes the Brauer group of a smooth cubic surface with three coplanar lines at infinity and counts m with BM obstruction. Method = Brauer group calculation (Gysin sequence, W(E6) Galois action, quaternion algebras, Tauberian counting) -- not a sieve, not Vieta orbits.
Transfer to S_n : xyz - x - y = n (VERIFIED symbolically with sympy): the projective closure F = xyz - x w^2 - y w^2 - n w^3 has NO affine singular points but is singular at the three vertices of the triangle at infinity; the vertex (0:0:1:0) has local form XY = W^3 (W+n), an A_2 point (the other two are A_1 by hand: yz = w^2*unit). So S_n is a singular cubic surface (type A_2 + 2A_1); the smooth-surface Section 2 of L-M does not apply verbatim; one would work on its minimal resolution (a weak del Pezzo of degree 3). Prop C/Cor D is an elementary Hilbert-symbol/reciprocity computation that plausibly IS the corresponding BM obstruction at squares (CONJECTURED, not checked).
Consequence: L-M cannot give 'sporadic failures are thin' (they do not prove it even for Markoff). The BM route could at most explain squares, which we already have. Ledger D13: 'transfer L-M thin-failure theorem' DEAD as stated.

## Ledger additions
D13 DEAD: transferring Loughran-Mitankin's thinness of failures (they prove it only for BM-explained failures; our surface is singular).
D14 OPEN, best lead: prove 'Type I union Type II covers all non-squares' or find a relation (maybe a bijection or correspondence) between Type I reps (m,t,u) and Type II reps (q,r,s1,s2) showing sporadic failures cannot coincide. Elsholtz-Tao's parametrisation of Type I/II solutions is the place to look; not read yet.
Files: es_combined.py es_combined.c es_Vcham.py combined_2e6.txt combined_2e7.txt.

---
# Session 3 (2026-11-08): multi-agent phase 1 started; credit budget ~30% of week left.
Literature agent report (agents/LIT.md, UNVERIFIED-SOURCE items marked there):
- PRIORITY WARNING (CONJECTURED, variable dictionary not checked): our Type I family looks like a re-parametrisation of Elsholtz-Tao Prop 2.3 'n = 4acd - f with f | 4a^2 d + 1' (credited to Nakayama) and related Yamamoto/Aigner classes (Prop 1.9). Do NOT claim the family as new until the dictionary is checked. Props C, D, E and the union conjecture (C*) are not in E-T beyond their Prop 1.6 (odd squares have neither type).
- E-T give no correspondence between Type I and Type II (both are N-points of one 3-dim variety Sigma_n, mapping to the surface S_n); exceptional-set bound is Vaughan's N exp(-c log^{2/3} N).
- No accepted proof in 2024-26 literature. Bradford 2602.11774 only outlines; Mallba 2602.20036 density-one (Oblath case); Cambridge Open Engage 'Modulo 24 obstructions' preprints unrefereed; erdosproblems forum rebutted a finite-CRT attempt for n=529 mod 840; Bright-Loughran: no Brauer-Manin obstruction.

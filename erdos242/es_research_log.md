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

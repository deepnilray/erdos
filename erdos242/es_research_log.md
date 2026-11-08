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

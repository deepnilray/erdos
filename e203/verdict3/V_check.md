# V_check: red-team log (agent V). Labels: CONFIRMED / FLAW / UNCHECKABLE. No odds.

Started 2026-10-25. Inputs read: HUB.md, DISTORTION.md, MIXED.md, B_noside.md, verify_distortion23.py, certify_range.py, poolE.py.
A_certify.md, C_allE.md, L_literature.md did not exist at this time; entries for them are pending.

## 1. Pre-existing claims

### 1.1 Pool completeness by the gcd route (certify_range.py logic): CONFIRMED (logic)
p | gcd(2^e-1,3^e-1) iff ord_p2 | e and ord_p3 | e iff e_p | e (p>3). Removing, with multiplicity, all pool primes with e_p | e
leaves 1 for every e<=E iff no prime with e_p<=E is missing, by induction on e (a missing q with e_q=e' is left over at level e').
Sound, including prime powers (while-loop). 2 and 3 never divide G_e.

### 1.2 Pool 800000 sampled independently (V_poolchk.py): CONFIRMED (sample only)
Own code, shares nothing with repo. 100814 distinct primes; every entry: prime, >3, e exact (2^e=3^e=1, no proper e/r works),
and the form (alpha,beta) satisfies 2^k3^l=1 <=> alpha k+beta l = 0 mod e on 30 random (k,l) each.
510 levels (500 random in [2,8e5] + 10 highly composite) leave exactly 1. Planted deletion of one pool prime: 60/60 detected.
This is a sample, not a certificate. A full independent run is queued under nice when cores are free.

### 1.3 Pair-intersection constant c = gcd(alpha_p beta_q - beta_p alpha_q, e_p, e_q) (L2): CONFIRMED (V_coker.py)
Brute force over (Z/lcm)^2 for 2163 random primitive form pairs with moduli in {2..36}: maximal intersection density
over ALL offsets equals c/(e_p e_q) exactly in 2163/2163 (so the bound is an equality, never exceeded).
Planted failure (ignore alignment, c:=1): fires 1382/1382 tested identical-form pairs.

### 1.4 Augmentation in the PURE theorem: CONFIRMED, but missing from DISTORTION.md (exposition gap)
R(A) and LB(A) assume all 9 heavy primes (5,7,13,17,19,37,73,97,577) have a NON-EMPTY set A_p. For a given m this fails when p | m or
-1/m not in H_p (index-2 and index-4 primes 73, 97, 577 and any p | m). The ratio (1-a)/(1-alpha) is not monotone in removing a set,
so this is load-bearing. It is repaired by the same CRT trick as MIXED.md section 3: if m is covered by P, choose m' = m mod every p in P
and mod 6, and mod each other pool prime q a residue with -1/m' in H_q; then all sets of P are unchanged, all other pool sets are nonempty,
so m' is covered by the full pool. DISTORTION.md only states the setting "empty or a level set" and never says this. Recommend adding it.
Not a flaw in the theorem.

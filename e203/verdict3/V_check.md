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

## 2. Coordinator priority checks on L's leads (2026-10-26)

### 2.1 (c) Two index-e lattices sharing a primitive vector are equal: CONFIRMED (proof + brute force)
Proof. Let v be primitive in Z^2; extend to a basis (v,w). Any lattice Lambda of index e containing v is determined by its image in Z^2/Zv = Z w, a subgroup of index e (because [Z^2:Lambda] = [Z^2/Zv : Lambda/Zv]), i.e. eZ w. Hence Lambda = Zv + Z e w, independent of Lambda. Cyclicity of the quotient is not even needed.
Primitive is essential: Lambda_1 = <(1,0),(0,2)> and Lambda_2 = <(1,1),(0,2)> both have index 2 and both contain (2,0) (= 2(1,1) - (0,2)), but differ.
Brute force (V_prim.py): all index-e lattices in HNF, e = 2..40, every v in [-8,8]^2 \ 0. Primitive v: 6864 cases, 0 with more than one lattice. Non-primitive v: 1968 cases with more than one lattice (the control fires).
Data: in poolE800000 (100814 primes) no two primes share a lattice (V_mult.py: max number of primes per lattice = 1), and max number of primes with the same e is n(e) = 4 (hist 1:89200, 2:5412, 3:250, 4:10) for e <= 8e5.

### 2.2 (b) Sun, arXiv:math/0411144 Thm 1.3 (Lettl-Sun): CONFIRMED applicable, with the following exact content
Opened the paper (2026-10-26). G is ANY abelian group (finite not required); cosets a_s + G_s with G_s arbitrary subgroups (finite index not required in the statement); m-cover means covering function >= m everywhere.
Thm 1.3: for a with w(a) = m exactly: N_a = [G : cap_{s: a in a_s+G_s} G_s] <= 2^{k-m} and k >= m + f(N_a). If {a_s+G_s}_{s != t} is NOT an m-cover (t irredundant), then [G:G_t] <= 2^{k-m} and k >= m + f([G:G_t]). f(n) = sum over p | n of v_p(n)(p-1).
Application to #203 with G = Z^2, m = 1, G_t = Lambda_p: legitimate directly (no need to pass to Z^2/Lambda_S). In a MINIMAL sub-certificate every prime is irredundant, so every prime in it has k >= 1 + f(e_p) and e_p <= 2^{k-1}. L's second claim ("point covered only by T: k >= 1 + f(lcm e_p)") holds but is weaker than the theorem's f(N_a) (N_a is a multiple of the lcm, f is monotone under divisibility); N_a is the index of the intersection, not the lcm. Hypothesis w(a) = m exactly is needed for that version and holds for some point in every minimal 1-cover.
Independent brute force (V_sun_test.py): random minimal covers of (Z/N)^2, N in {6,8,9,10,12}, by cosets of random subgroups: 19177 (cover, coset) pairs, 0 violations of k >= 1+f(index) and index <= 2^{k-1}; 1917 of them tight.
Strength: weak. With the repo theorem (a covering needs a prime with e_p > 4e5) it only yields k >= 1 + f(e_p) >= 1 + log2(4e5) > 19. It restricts the primes of a minimal certificate to those with f(e_p) <= k-1, which is a real constraint only for small k. Not a route to NO by itself.

### 2.3 (a) Li-Wang-Yi arXiv:2302.05946: framework CONFIRMED to apply; L's "unconditional tail" claim is L's inference and is NOT justified
Opened the paper (ar5iv). Facts:
- Thm 2.1: S finite, pi_j: S -> T_j an inverse system, B_j pi_j-measurable, delta_j in [0,1/2], P_0 pi-measurable, P_j(x) = P_{j-1}(x) times [1_{x notin B_j}/(1-alpha_j) if alpha_j < delta_j; (alpha_j - 1_{x in B_j} delta_j)/(alpha_j(1-delta_j)) else]. Conclusion: if sum_j min{M1_j, M2_j/(4 delta_j(1-delta_j))} < 1 then P_J(union B_j) < 1. This is exactly the repo's tilt (weights 1/(1-delta) outside B, (alpha-delta)/(alpha(1-delta)) inside), with S = Z^2/N Z^2, pi_j = projection to coordinates <= q_j, P_0 = P_23 (pi-measurable). So S = Z^2/Lambda_S with stages by q = P^+(e_p) is allowed. Only difference: the paper restricts delta_j <= 1/2; repo's cost bound is the sharper (x - delta)_+ majorant.
- Stages are ordered by INCREASING norm of the prime (smallest first), B_j = union of ideals with largest prime p_j ("P_min" in their notation). Same as repo.
- Lemma 3.3 (1),(2) is for ideals I_i in a number field K, "distinguishable" (unique prime factor of largest norm), with multiplicity s = max_I #{j : I_j = I}. (2) says M2_j << s^2 (log ||p_j||)^6/||p_j||^2. The paper does not state what the implied constant depends on; the proof's Euler product uses Mertens in K, so it depends at least on K. (1) needs delta_i = 0 for i < j and ||I_i|| >= ||I_1||.
- So the "tail" bound is in the paper, but for COVERINGS WITH BOUNDED MULTIPLICITY s. In #203 the multiplicity of a modulus e is n(e) = #{p : e_p = e}, and the transplant needs sup_e n(e) < infinity (or at least control of sum over stage-q primes of n(e)/e and of n(e)^2 pairs). Unconditionally one only knows n(e) <= log2(G_e)/log2(e) << e/log e (Bugeaud-Corvaja-Zannier gives log G_e <= eps e, ineffective). Empirically n(e) <= 4 up to 8e5, but heuristically sup_e n(e) = infinity (sum over e of P(n(e) >= k) ~ sum (c/ln e)^k diverges for every k). So the claim "unconditional in the number of primes" replaces the divergent sum of 1/p by a multiplicity hypothesis that is exactly the missing large-index control. M2 ~ s^2 (log q)^6/q^2 is therefore [CONJECTURED-conditional on n(e) = O(1) or on bounded moments], not [LEAD unconditional].
- The 2D analogue of Lemma 3.3(2) is also not in the paper: cross terms c^< for aligned pairs; the repo's Lemma 2 handles it per pair but a uniform (log q)^C bound requires counting aligned pairs (p,p') in the same stage, which brings Lambda_p cap Lambda_p' of index e e'/c, and the data (C_align.py) is what addresses it. Not checked yet.
- L11 (Minkowski): pool(E) << E^{3/2}: CONFIRMED (box |i|,|j| <= sqrt(e_p) contains a nonzero point of Lambda_p by Minkowski; each 2^i3^j - 1 has << sqrt(E) prime factors). It does not give n(e) = O(1), only mean n(e) << sqrt(E).

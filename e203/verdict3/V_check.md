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

## 3. Agent C (C_allE.md), checked 2026-10-26

### 3.1 Theorem Z (>= N_Z primes with e_p > 8e5): per-prime cost CONFIRMED; pool bound B' PENDING
- rho(e) = r(e) prod_{q|e,q>=5} g_q / e with g_q = 1/(1-min(delta_q,cap)), r = 2.6145 if gcd(e,6)>1 else 1. My own segmented sieve over every e in (8e5, 1e8] (V_rho.py) plus the analytic tail e >= 1e8 (w distinct primes >= 5, e >= max(P_w, 1e8)): cap 0.5: max 3.8940e-5 at e = 832370; cap 0.28: max 1.6806e-5 at e = 803985; tails < 3.4e-6 and 2.6e-7. Matches C (3.894e-5, 1.68e-5).
- r_max = 2.6145 is the maximum of coupled_full_E200000.txt, which contains 781 of the 782 cyclic-quotient subgroups of (Z/144)^2 (I enumerated them; only the index-1 lattice is absent, price 1). So r_max covers every possible new prime.
- New primes do not create overlap/second-moment terms: cost_l(F u G) <= cost_l(F) + E[alpha_G]/(1-delta_l) since (x+y-delta)_+ <= (x-delta)_+ + y and alpha_{FuG} <= alpha_F + alpha_G. Pool stage bounds are monotone in the family and valid for any earlier sets (L1 uses deltas only). The only coupling is B_23: new 3-smooth primes (each mass < 1/E0) raise alpha_23 by <= N/E0 and every price scales by <= s(N) = (1-a*)/(1-a*-N/E0). Augmentation (CRT) makes all pool primes active without touching P's tail primes. No flaw found.
- B' (pool bound with delta capped) is float (C's distort_fast). I am running the exact-rational verifier (verify_distortion23.py, not C's code) on delta capped at 0.28: verdict3/V_run_cap.sh, ckpt V_ckpt_cap028.txt. Status: see HUB/V messages. Note: the log shows N increasing as the cap decreases (0.5: 6183, 0.4: 6661, 0.3: 10001, 0.28: 10300), so the optimum cap is probably lower still.
### 3.2 Lemma A (alignment criterion): CONFIRMED
V_lemmaA.py: 5640 random families of primitive forms (moduli in {2..36}), the criterion g_pq | D_pq for all pairs agrees with 'the intersection of the kernels contains a primitive vector' (brute force over (Z/L)^2) in 5640/5640; 1036 had a primitive vector. Planted wrong criterion (min(e,f) instead of gcd) disagrees in 643/3000.
### 3.3 Common discrete log (Lemmas T1, T2): CONFIRMED (logic); B&B numbers: partially
T2 is Euler's criterion. T1 is generalised CRT. My independent branch and bound (V_commonT.py, pool read from poolE800000 but 3 in <2> and t_p recomputed by brute force) agrees with an exhaustive search over T mod lcm at E=40 (0.46851). C's 0.5627 at E=300 not yet reproduced (my run was killed twice by the machine reset and CPU contention; rerun pending).
### 3.4 Hypothesis H_dens(kappa) as literally stated: FLAW (the statement is false in its own model)
H_dens says: for EVERY prime l >= 5 and EVERY d, sum_{e>E0, P+(e)=l, d|e} n(e)G(e)/e <= kappa-model. In C's own Poisson model (n(e) ~ Poisson(tau e/phi(e)), tau = 0.813/ln E0, G from the 8e5 run, RHS summed over ALL multiples of d by exact geometric sums, LHS truncated at e <= 1e10 so violations are undercounted), V_Hmodel2.py: for l = 5 and l = 7 the probability that H_dens(kappa) fails for some d is 1.0 at kappa = 1, 1.5 and 2 (100 trials each, worst d has LHS/RHS = 6.2 and 6.3). Reason: take d = a realised e; the single term G/e exceeds the expected mass of all its multiples, which is only about 0.3 G/phi(d) for smooth stages. So no constant kappa <= 2 makes the pointwise hypothesis true, even if the density heuristic is exactly right.
What survives: the quantity the proof really consumes is the aggregate quadratic functional Q = sum_d theta(d) Y_d^2 (and the linear one). In the same model V_Hmodel3.py gives Q_real/Q_model: l = 5: mean 1.08, median 1.04, 90% 1.48, max 2.20; l = 7: mean 1.02, 90% 1.25, max 1.52 (100 trials). So an aggregate hypothesis of the form 'Q <= kappa^2 Q_model' with kappa about 1.5 is consistent with the model, but Theorem C should be restated with that aggregate hypothesis (and the totals recomputed), not with the pointwise one. The data-side bucket test (C_testH) is aggregate and unaffected. (My data version V_Hdata.py is truncated to the window and is NOT evidence.)

## 4. Agent C2 (C2_ce.md)
- Lemma 1 (Minkowski/Hermite short vector, p < 6^{sqrt e}): CONFIRMED (proof standard; its 100814/100814 run is consistent with my own pool validation).
- Lemma 2 (uniqueness of lattice with given primitive vector and index): CONFIRMED (my 2.1; V_prim.py).
- Lemma 3 (budget sum_e lambda(Lambda(v,e)) log(e+1) <= log N(v)): CONFIRMED (distinct e give distinct primes, every prime p with e_p = e has p >= e+1 since e | p-1).
- Prop 4 (c*(e) = floor(phi(e) log 2 / log(e+1)) satisfies every inequality sum_{e|n} c(e) log(e+1) <= n log 2): CONFIRMED (sum_{e|n} phi(e) = n; drop e=1 and use (n-1) log 2 < log(2^n-1) for n >= 2). It shows the gcd-size system alone cannot beat c(e) ~ e/log e. It does not use p | 3^n-1 or the lattice constraint, which C2 says (and I agree) leaves the conclusion unchanged for a single e.
- Section 5 (H_cls reduction): the identity 1/lcm = sum_{d|gcd} phi(d)/(ab) and pair density <= 1/lcm(e_p,e_q) are correct (image of Z^2 in Z/e_p x Z/e_q surjects onto both factors). Proposition 5 then follows: cost_l <~ l^{-2} sum_d phi(d) Y_d^2 <= l^{-1-2eta} log l. CONFIRMED as a conditional implication. H_cls (polynomial room l^{1/2-eta}) is far weaker than C's pointwise H_dens and is not subject to the Poisson failure in 3.4 (a single prime contributes <= 2^omega/d to Y_d). Gap to state: H_cls only covers stages l >= Q. For the small stages (l < Q ~ 30..100) infinitely many y-smooth e > 8e5 are still allowed, and the sum of n(e)G/e over them is not controlled by H_cls (C2's own data show mu_l/sqrt(l) up to 1.83 for l < 30, so H_cls fails there); some separate input on smooth e (finiteness or a density bound for primes with y-smooth e_p) is needed for a complete conditional theorem.

## 5. FLAW: "uncovered density >= 1 - B(E)" (B_noside.md section 3.3; reused in D_almostall.md section 4)
Claim (B_noside 3.3): for every m coprime to 6 the set of (k,l) with 2^k3^l m+1 divisible by no pool prime has lower density >= 1 - 0.730584 = 0.2694, "PROVED in the repo".
Not proved, and false as a uniform-density statement. B(E) bounds the P_final-measure of the union (P_final is the tilted measure of M1; it has density up to prod 1/(1-delta) w.r.t. the uniform measure), so 1 - B(E) only bounds P_final(uncovered). It gives positivity of the uniform density (P_final is absolutely continuous with bounded density for a finite pool), not the constant.
Counterexample (V_unif.py, exact count on the torus (Z/5040)^2, hill-climbing offsets, reproduces veljjanoski's 71.7% plateau): the 31 pool primes with e_p | 5040 and e_p <= 2000 (offsets are all realisable by CRT on m) cover uniform density 0.71705. The claim at E=2000 would give uncovered >= 1 - 0.570147 = 0.4299, but this family leaves only 0.28295. The same 0.71705 also exceeds B(20000)=0.6334 and B(200000)=0.7157. For E=4e5 (0.7306) the published 76.0% at N=55440 (veljjanoski, HUB.md) exceeds it.
Consequence: any use of the number 0.2694 as a uniform density is invalid. Positivity (and the Theorem E / Theorem statements) is unaffected. D's Lemma S side condition 'N_r >= c|B|/log w uniformly in w' therefore has no support from the repo: for each fixed w only 'N_r >= c(w)|B|' with an uncontrolled c(w) follows.

## 6. Agent D (D_almostall.md), checked 2026-10-26

### 6.1 Theorem A (rough-number second moment, 97.2% of m): CONFIRMED modulo the cited fundamental lemma
- Sieve setting re-derived. For fixed u, {A_u m+1 : m in (x/2,x], (m,6)=1}: for primes 5 <= p < z the condition p | A_u m+1 removes exactly one class of m mod p (p does not divide A_u), so |r_d| <= 1 uniformly in A_u, in particular for A_u up to x^{0.1}; the coefficient size enters only through the class, not through the error. For pairs (u,u'): rho(p) = 1 if p | A_{u'}-A_u else 2, |r_d| <= 2^{omega(d)}, rho(p) <= 2 < p for p >= 5, so the dimension-2 fundamental lemma with level D = x^{1/2} = z^s (s >= 19 = 9*kappa+1) applies pair by pair; (log x)^4 pairs times remainder D (log D)^2 is o(x/log^4 x). Uniformity in the 3-smooth coefficients: fine, because only the congruence class mod d matters.
- Omega bound: n = A_u m+1 <= x^{0.1} x + 1 <= x^{1.1}; all prime factors >= z = x^{1/(2s)} gives Omega(n) <= log n/log z <= 1.1 * 2s = 2.2 s. CONFIRMED (n > 1 trivially).
- E[R_z] ~ |B| * 3 e^{-gamma}/log z with |B| ~ 0.003 log^2 x gives E R ~ 0.01 s log x -> infinity, so the 1/E term vanishes.
- rho: independent recomputation (V_rho_D.py: own prime loop, own lattice test 2^i 3^j = 1 mod p on the grid |i|,|j| < N, weights = number of ordered pairs with that difference) gives prod_{p>=5}(1-1/(p-1)^2) = 0.88022, mean F = 1.16700, rho = 1.02721 at N=80, p<2e4. D: 1.02721. CONFIRMED. (Control: independent cells give 0.88022.) A rigorous enclosure is still missing, as D says.
- Chebyshev step: P(R_z = 0) <= Var/E^2 = rho_x - 1 + O(e^{-s}) + 1/E. CONFIRMED.
### 6.2 Lemma S and 'density one': the covering problem is hidden in the hypotheses
If density one held for 'R_z(m) > 0' with z -> infinity, it would contradict the existence of any finite covering: for m in the class m0 mod prod P of a covering with prime set P, every n = 2^k3^l m+1 has a prime factor in P < z, so R_z(m) = 0 on a set of positive density. Hence Lemma S together with its side condition (N_r >= c |B|/log w uniformly in r mod W and in w) is at least as strong as 'no covering exists'. D lists the side condition as CONJECTURED but ranks Lemma S as 'provable lattice combinatorics'; only the F_w part is combinatorial. And the repo does not supply the side condition (see 5: the constant 0.2694 is not a uniform density). So the route 'almost-primes at density one' is not independent of C's target; it is equivalent to a quantitative version of it.
### 6.3 Statement about Maynard (section 1) and parity (section 5): UNCHECKABLE here
Relayed hypotheses of arXiv:1405.2593 Thm 3.1 not seen typeset; I do not vouch for k <~ sqrt(log x / log log x). The ceiling 1/(kappa*rho) <= 0.49 is correct as a statement about the method (parity gives kappa >= 2).

## 7. Agent A (A_certify.md), checked 2026-10-26
### 7.1 Pool completeness (4e5, 8e5]: CONFIRMED (logic; sampled and partial independent re-derivation)
Logic of the certificate re-derived (section 1.1). My own independent checks: V_poolchk.py (510 levels, 60/60 planted deletions caught), V_sieve.py (own spf sieve and own order computation for all 216814 primes 5 <= p < 3e6: 88923 with e_p <= 8e5, identical to the pool entries below 3e6; planted deletion detected). A's sieve to 2e9 and the 12 primes above 2e9 (gcd route only) not re-run.
### 7.2 Exact-rational B(8e5), Theorem E at 8e5: PENDING in A's file (EXACT_PENDING, MIXED_PENDING). Nothing to check yet.
### 7.3 Conditional theorem H(kappa, eps): arithmetic UNCHECKED; hypothesis (H_n) as stated is FALSE stage by stage
(H_n) demands, for each stage l, sum over primes in the stage with e_p > E0 of Lambda_p/e_p <= kappa * (model). Pool test on the window (4e5, 8e5] (V_Hn_stage.py), per-stage realised/model: aggregate ratios 1.17 (l<30), 1.12 (30-100), 1.04 (100-1000), 0.99 (1e3-1e4), 0.99 (1e4-1e5), 0.85 (>=1e5), but individual stages exceed 1.5x model in 5.4% (1e3-1e4), 28.5% (1e4-1e5), 9.7% (>=1e5) of stages, max stage ratio 33. Same reason as 3.4: stages with few e are sparse Poisson-like. So H_n must be stated for aggregates over stage ranges (sums of first moments and of squares); the sums of squares (realised/model) are 1.24, 1.09, 1.01, 1.37, 4.97 in the ranges 30-100, 100-1000, 1e3-1e4, 1e4-1e5, >=1e5 (the last range carries 2e-8 in absolute size). With aggregate hypotheses the proof structure survives; the theorem should be restated and the totals recomputed with those.
The 'worst-case gcd cannot close, 22.8' remark and the necessity of controlling alignment: consistent with C (c^< model).
### 7.4 Aristotle prompt of A: statements A, B, D are true as stated (A: S.index = e; B: coset; D: max(x-delta,0) <= x^2/(4 delta) for delta>0). C (kernel contained in S with index e implies equal) is true (a subgroup of index e contained in a subgroup of index e is equal).

## 8. Round 4 (2026-10-30): restated material

### 8.1 A_certify.md section 3: NOT YET RESTATED
The file still states (H_n) stage by stage ("all stage functionals ... at most kappa times"). My section 7.3 finding stands unchanged: false stagewise on the data window (up to 33x in single large stages). Recheck when A's restatement lands.

### 8.2 C_allE.md section 5b (Theorem C', aggregate hypotheses): FLAW in the wording, repairable; numbers not re-run
- The pointwise-in-d problem (my 3.4) is fixed: only Y_1 and Q = sum_d theta(d) Y_d^2 are used. The Cauchy-Schwarz cross term 2 sum theta Y^pool Y^> <= 2 sqrt(S2pool) sqrt(Q^>) <= 2 kappa_Q tau sqrt(S2pool S2tail) is correct.
- But H_L and H_Q are still stated "for every l >= 5", i.e. pointwise in the STAGE. For large stages this is false on the data in the same way: a stage l >= 1e4 holds only a handful of e in any window, and single-stage first-moment ratios realised/model reach 8 (l in [1e4,1e5)) and 33 (l >= 1e5) on (4e5,8e5], with 28.5% and 9.7% of stages above 1.5 (V_Hn_stage.py); squares are worse. C's own test (C_testQ) is by buckets of l, so it does not support the 'every l' form either; C says so in gap (b).
- Repair (no change to the proof): for stages where delta_l is fixed (l >= 1000, delta = 1/2) the stage bound is linear in m2, so only sum_{l in range} Q_l^> / (4 delta_l(1-delta_l)) is consumed; for l < 1000 a fixed choice of majorant per stage is also linear in (m1, m2). State H_L, H_Q for these weighted sums over the stage ranges actually used (or per bucket), and check that C_tail.py applies kappa_L, kappa_Q^2 uniformly (then the totals 0.87-0.96 are unchanged). The 'min per stage' must be replaced by a fixed per-stage choice for the hypothesis to stay aggregate.
- Evidence statement CONFIRMED as honest: ratios 1.25-1.30 total, worst bucket 1.77, not shrinking with the window, and C itself reports the Poisson model under-predicts Q. So kappa_Q ~ 1.34 is empirical, margin ~7%.

### 8.3 D_almostall.md sections 10-11
- 10.1 conditional implication (density one for R_z > 0 implies no finite covering): CONFIRMED (it is my 6.2). 
- 10.1 'delta_cov <= rho - 1': CONFIRMED with one precision. For a fixed finite family of coverings (all primes < y), the covered classes have R_z = 0 once z > y, and Theorem A with s -> infinity (z = x^{1/(2s)} still -> infinity) gives density <= rho - 1 + o(1); this does not need the fundamental-lemma constant at a fixed s. The statement must read "for every y, the density of m admitting a covering with all primes < y is <= rho - 1", uniformly in y; it is not a statement about the (countable) union over all y, whose natural density need not exist. With that reading it is a clean new statement (modulo the fundamental lemma and the numerical rho).
- 10.2 rho: CONFIRMED numerically. My independent code: N=80: 1.02721; N=160: 1.02747; N=300: 1.02754 (p < 5000; D: 1.02748, 1.02755 with p < 2e4). Rigorous enclosure still missing, as D states.
- 10.3 'r_0 = 19': FLAW. s_0 = 9 kappa + 1 = 19 is the threshold at which the fundamental lemma (Friedlander-Iwaniec, Opera de Cribro Lemma 6.3, recalled, not opened) is VALID; its relative error there is of size e^{9 kappa - s} K^{10} = e^{-1} K^{10} >= 0.37, not small. Theorem A needs the relative errors of first and pair moments to be << rho - 1 = 0.028 (the Chebyshev bound is Var/E^2 = rho(1+O(eta)) - (1+O(eta))^2 + ..., an O(eta) error swamps 0.028). That forces s >= 9 kappa + log(K^{10}/eta), i.e. s around 25-45 depending on K, and r_0 = floor(s(1+c)/(1-eps)) accordingly. D's own section 3.4 remark (c) (r_0 about 40-55) was the consistent version. So "all but 2.8% of m have some cell with Omega <= 19" is not supported; "all but 2.8% + O(e^{9 kappa - s} K^{10}) have Omega <= s(1+c)/(1-eps)" is. (Uniformity in A_u and the level x^{1-eps}: CONFIRMED.)
- Section 11 (exact bad-class measure for small w): only a plan in the file; nothing to check yet.

### 8.4 Pending
- Exact-rational B' at cap 0.28: running under the coordinator's restart (9 of the stages checkpointed at 2026-10-30).
- Common-T E=300 comparison: not rerun (not light: my B&B did not finish in 280 s; deferred while the cores are busy).

## 9. Round 5 (2026-10-30): C_allE.md sections 3d and 5c

### 9.1 Section 3d (cyclic-type price for a new prime): CONFIRMED
- Cyclic quotient: Z^2/(Lambda_p + 144Z^2) = (Z/e_p)/144(Z/e_p) = Z/gcd(e_p,144). It is cyclic of order exactly gcd(e_p,144). Pool sample: psi mod gcd(e,144) is onto in 3000/3000 (V_cyc.py).
- The table holds every cyclic type: my own parse of coupled_full_E200000.txt (V_cyc.py) finds, for every n | 144 with n > 1, exactly n*prod_{q|n}(1+1/q) cyclic types (gcd(a,c,d) = 1). Max price by index: 1:1, 2:1.648, 3:1.4623, 4:1.8296, 6:2.1057, 8:1.8355, 9:1.4881, 12:2.2413, 16:1.8355, 18:2.1057, 24:2.2419, 36:2.2413, 48/72/144:2.2419. These are identical to C's table. RMAX 2.6145 belongs to a non-cyclic type.
- DFS ratios: max r(2g)/r(g) = 1.648 < 2 and max r(3g)/r(g) = 1.462 < 3 over all g | 144; there are no violations. Multiplying by 2 or 3 once v_2 or v_3 is saturated leaves r unchanged.
- rho_max, independent (V_rho2.py: own segmented sieve over every e in (8e5, 1e8], price r(gcd(e,144)), plus an analytic tail for e > 1e8):
  - cap-0.28 vector: 1.24965e-5 at e = 870870 (tail < 2.3e-7). C: 1.2496e-5 at 870870.
  - C_opt_best.json snapshot (sweep 1): 1.23933e-5 at e = 903210 (tail < 2.9e-6). C: 1.2393e-5.
- Minor: the table prices use lambda = 0.0485, but the light mass at 8e5 is 0.04850936. The correction factor CORR = 1.0000251 should multiply r. My numbers include it; C's apparently do not. The effect on N_Z is below one prime.
- N_Z = 13184 at cap 0.28 rests on the float B' = 0.798372. My exact check of that B' is still running (restarted by the coordinator; 69 of 15279 stages done, largest first). The joint-delta values (13813, 13962, and 14006 at sweep 2) rest on float B' for re-optimised vectors that nobody has verified exactly. Each final vector needs its own exact run.

### 9.2 Section 5c (Theorem C'', range-sum hypotheses): CONFIRMED as a repair (logic); totals not independently re-run
- Fixing one majorant per stage from the model alone is legitimate: any fixed (a,b) with (x-delta)_+ <= a x + b x^2 on the relevant range is a valid bound. The cost is then linear in (Y_1^>, Q_l^>, cross_l).
- cross_l <= 2 sqrt(S_l Q_l^>) is the theta-weighted Cauchy-Schwarz bound. Summing over a range, sum v (2 sqrt(S Q) + Q) <= 2 sqrt(sum vS) sqrt(sum vQ) + sum vQ is Cauchy-Schwarz in l with v >= 0. Both are correct. So only the eight range sums are consumed, which is exactly the aggregate form I asked for in 8.2.
- Remaining caveats (C states all of them):
  - The weights depend on delta, so a re-optimised delta (9.1) changes the hypothesis and needs a re-test.
  - The top ranges are thin in every window below 8e5. In [1e5, inf) the stages see only cofactors e' <= 8, so the Q-ratio of 5.25 there is not evidence about e > 8e5.
  - The ratios do not shrink as the window grows.
  - The Lipschitz stages could use 2.2419 instead of R* = 2.680 (this would help).
- The totals (0.9084 with the per-range empirical kappas, 0.9961 with the crude kappas) come from C's own code and have not been re-run independently.

## 10. Round 6 (2026-10-30): D_almostall.md section 11

### 10.1 Lemma U: PROVED (proof below). Both Theorem A and the stratified version are released from this gap.
Claim: for u, u' uniform with u != u' in [1,N]^2 and Delta = u'-u, limsup_N E_N[F(Delta)] <= W := sum_d g(d)/e(d). Here F(Delta) = sum_{d | n(Delta)} g(d) (d squarefree with primes >= 5) and g(d) = prod 1/(p-2).
Proof.
- (a) Each Delta has probability <= N^2/(N^2(N^2-1)) = (1+o(1))/N^2. Hence E_N[F] = sum_d g(d) P(Delta in Lambda_d \ 0).
- (b) Lattice count. Let v be the shortest vector of Lambda_d; Gauss reduction gives |v|^2 <= (2/sqrt3) e(d). The points of Lambda_d lie on lines parallel to v spaced e/|v| apart. The box [-N,N]^2 meets at most 2 sqrt2 N |v|/e + 1 of these lines, with at most 2 sqrt2 N/|v| + 1 points on each. So #(Lambda_d cap box \ 0) <= 8N^2/e + C N/|v| with C = 2 sqrt2 (1 + 2/sqrt3), using N|v|/e <= (2/sqrt3) N/|v|. The count is 0 if |v| > sqrt2 N.
- (c) Shortest vectors are long for large d. Since v != 0 lies in Lambda_d, d divides the numerator n(v) of 2^a 3^b - 1, and 0 < n(v) <= 6^{|v|}. So lambda1(d) = |v| >= log d/log 6, and d <= 6^{sqrt2 N} whenever the count is nonzero.
- (d) Split at T.
  - The finitely many d with e(d) <= T (all their primes have e_p <= T) are periodic, so P -> 1/e(d).
  - The rest contribute <= (1+o(1)) [8 sum_{e(d)>T} g(d)/e(d) + (C log 6/N) sum_{1<d<=6^{sqrt2 N}} g(d)/log d].
  - The first sum is a tail of the convergent series W (g(d) <= 3^{omega(d)}/d and e(d) >= ord_d 2, Lemma R).
  - For the second, sum_{d<=X} g(d) <= prod_{5<=p<=X}(1+1/(p-2)) << log X, so partial summation gives sum_{1<d<=X} g(d)/log d << log log X << log N. That term is << log N/N -> 0.
  - Letting T -> infinity gives limsup E_N[F] <= W.
- Inside classes the argument is the same. The pairs are restricted to S_r, the weight per Delta is at most (1+o(1))/(nu_r^2 N^2), and cosets of Lambda_d cap Lambda_W replace Lambda_d. The extra +1 per coset contributes <= |H_W| (1/N^2) sum_{d<=6^{sqrt2 N}} g(d) << 1/N. lambda1 can only grow. The character average over S_r converges for the finitely many d with e(d) <= T. Truncating at p < z only lowers F.
The gap D flagged was the crude Lemma D boundary sum over all primes up to 6^N. The fix is (c): the boundary term is weighted by 1/lambda1(d), and lambda1(d) is at least log d/log 6.

### 10.2 Explicit K constants: FLAW. D's K is too small, and the explicit r0 table shifts.
The Omega(kappa) condition prod_{w1<=p<w2}(1-kappa/p)^{-1} <= K (log w2/log w1)^kappa must hold for all real w1 < w2. D_Kconst.py takes w2 only at the next prime, so it misses w2 just above a prime. Correct values (V_Kfix.py):
- Primes >= 5: the sup is the single prime p = 5 with w2 -> 5+. K1 = (1-1/5)^{-1} = 1.25, so K1^10 = 9.31 (D: 1.396). K2 = (1-2/5)^{-1} = 5/3, so K2^10 = 165.4 (D: 3.75).
- Primes >= 31: K1 = 1.03612, K1^10 = 1.426; K2 = 1.07482, K2^10 = 2.058, both attained on [41,43] (D: 1.01597 and 1.03270, K2^10 = 1.379).
Recomputed with D's own formula and D's nu distribution (eta1 = e^{9-s} K1^10, eta2 = e^{18-s} K2^10, rho <= 1.028192, s = (r0+1)(0.999/1.001)):

| r0 | unstratified, D's K | unstratified, corrected K | stratified w=31, D's K | stratified w=31, corrected K |
|---|---|---|---|---|
| 22 | 0.0525 | 0.551 | 0.0153 | 0.0200 |
| 23 | 0.0368 | 0.320 | 0.0093 | 0.0110 |
| 24 | 0.0309 | 0.161 | 0.0070 | 0.0077 |
| 25 | 0.0287 | 0.0811 | 0.0062 | 0.0064 |
| 26 | 0.0279 | 0.0479 | 0.0059 | 0.0060 |
| 28 | 0.0275 | 0.0303 | 0.0057 | 0.0058 |
| 29 | 0.0274 | 0.0285 | 0.0057 | 0.0057 |

Corrected headline statements:
- Stratified: all but 2.0% of m have a cell with Omega <= 22, 1.1% with Omega <= 23, and 0.6% with Omega <= 26.
- Unstratified: <= 3% first holds at r0 = 29 (2.85%); D's "2.85% at Omega <= 26" becomes 4.8%.
- The large-r0 limits and the covering corollary (<= 0.58%, uniform in y) are unchanged, because they let s -> infinity.
On my earlier "r0 about 40+": that was too pessimistic. With an explicit K the stratified sieve over primes >= 31 really reaches the low 20s, so I withdraw that estimate. Both D's and my numbers rely on the same unopened reading of FI Lemma 6.3 (error e^{9 kappa - s} K^{10}). Until someone opens Opera de Cribro, that reading stays UNCHECKABLE.

### 10.3 Paley-Zygmund per class, character formula, Parseval: CONFIRMED
- P(R > 0) >= (E R)^2 / E R^2 with E R >= (1-eta1) mu and E R^2 <= (1+eta2) pairs + (1+eta1) mu gives the stated bound as mu -> infinity.
- The factorisation (1-rho(p)/p)/(1-1/p)^2 = (1-1/(p-1)^2)(1+g(p) 1[Delta in Lambda_p]) holds for both rho(p) = 2 and rho(p) = 1.
- Only characters of Z^2/(Lambda_W + Lambda_d) survive the class average, which is exact after 10.1.
- Parseval gives sum_{psi != 1} |T^(psi)|^2/|T|^2 = 1/nu - 1.
- C_w = prod_{p>=w} is the limit of prod_{w<=p<z} (each factor < 1, so it is the right side as z -> infinity).
- Classes with nu = 0 count with weight 1.
nu_r: my own exhaustive enumeration over every class r mod W on the full exponent torus (no logs, no FFT) gives min nu = 0.5583 (w=13) and 0.5097 (w=17), with mean nu = prod(1-1/p) to 10 digits. Both match D.

### 10.4 rho enclosure: partially CONFIRMED
- A(1), the mean of F_{<31} over H_W, is exactly sum_{d | 5*7*...*29} g(d)/e(d). My exact-rational computation, with e(d) = |<2,3> mod d| from the forms (cross-checked by BFS for small d) and |H_W| = 665280, gives A(1) = 1.1562606807, identical to D. A first attempt with e(d) = lcm(ord 2, ord 3) gave 1.1667; that formula is wrong for composite d, and this is a trap for anyone re-deriving it.
- The lower bound (A(1) + singles, all terms >= 0) and the upper bound (C_5 is the product truncated at 1e8) are logically sound.
- Not checked independently: the single-prime sum over 31 <= q <= 1e8 (needs D_eprimes.c, which I have not compared with my own sieve beyond 3e6) and the composite/unknown-prime tail tau_31 = 3.2e-4.
- The interval [1.02751, 1.02820] contains my box values 1.02747-1.02754 (p < 5000, N <= 300). These sit about 4e-5 below the lower end, which is consistent with the p < 5000 truncation and the 1/N boundary effect (D's own N=600 value is 1.02758).

## 11. Theorem E at 8e5 (2026-10-30): CONFIRMED
- (1) Rounding. P_final(qZ^2) <= q^-2/(1-delta_q) must use the same delta as the measure behind B. That delta is the verifier's F(round(100 v), 100). 1/(1-delta) increases with delta, so rounding delta UP, and each term up to a multiple of 1e-40, can only enlarge S, which is the conservative direction. In fact every value in delta23r_E800000.json is an exact multiple of 0.01 (0 of 15279 are not), so nearest = up = the verifier's delta and nothing is lost. At 4e5, verify_mixed.py and verify_distortion23.py apply the same round-to-nearest to the same delta file, so S at 4e5 used exactly the measure's delta. There is no MIXED.md issue. (delta23r_E400000.json is not in this worktree, so I could not inspect its raw values, but the identical-rounding argument does not need them.)
- (2) Formula. S = sum_{5<=q<=8e5} 100/(q^2 (100-k_q)) with k_q = 100 delta_q, and delta_q = 0 for the 48670 primes with no stage, the same convention as the verifier. The tail sum_{q>E} q^-2 < 1/(E-1) uses untouched coordinates. My independent 60-digit decimal sum gives S = 0.1450987005 (A's upper bound: 0.145099). With B = 0.7424445189 (exact fraction from verify23_800k.log, first line) and R3 = 250822656/3288355921, the totals are 0.88754447 (3 not| g) and 0.96382048 (3 | g). Both match mixed_800k_upper.log and both are < 1.
- (3) R3 is NOT independent of E as an exact number: 4e5 gives 250822656/3288415339 and 8e5 gives 250822656/3288355921. lambda' contains the light {2,3} mass (0.0485017 at 4e5, 0.04850936 at 8e5), and that mass grows with E. The claim must be reworded. The value used is correct, because mixed_800k.log recomputed R3 with the 8e5 light mass, which is the mass of the full pool. Its float is 0.076276 (4e5: 0.076275).

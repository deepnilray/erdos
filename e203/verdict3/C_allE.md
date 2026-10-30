# Erdős #203, agent C: what can be proved toward "no covering certificate for any finite set of primes"

Labels: **PROVED** (complete argument here or in a cited theorem I read), **VERIFIED** (computation with a control that can fail; floating point where stated), **CONJECTURED**, **HYPOTHESIS** (explicit assumption).
#203 itself stays **OPEN**. Scripts: `verdict3/C_*.py` (run from `e203/`). Notation as in DISTORTION.md: Λ_p = ker(ψ_p), ψ_p(k,l) = α k + β l mod e_p, Z²/Λ_p ≅ H_p cyclic of order e_p, n(e) = #{p : e_p = e}, a *covering* is a finite P and cosets c_p + Λ_p (p ∈ P) with union Z² (any offsets occur, by CRT on m).

## 0. Results in one table

| # | statement | label |
|---|---|---|
| Z | **Every covering has at least N_Z primes p with e_p > 8·10⁵** (hence ≥ N_Z primes), N_Z = **14 013** with the cyclic-type price of §3d and the jointly optimised δ (`C_opt_best.json`); 13 184 with the same price and the cap-0.28 vector, 10 300 with the old price RMAX (6183 at cap 0.5; table in §3) | VERIFIED (uses float pool bound B' = 0.785224 for the optimised δ (0.7984 for the cap-0.28 δ, exact check by V pending); PROVED given that number). In particular: **no covering certificate with at most 14 012 primes** |
| S | Every covering has ≥ 20 primes (exact, B(4·10⁵)) and ≥ 21 (float, B(8·10⁵)); superseded by Z, but the finite pools S_K = {e : f(e) ≤ K−1} (|S_34| = 4266) are the right object for "size ≤ K" statements | PROVED / VERIFIED |
| C″ (§5c; supersedes C′ wording) | hypotheses on weighted stage-RANGE sums H_L^R, H_Q^R ⇒ no covering; total 0.9471 at uniform (1, 1.34), 0.9084 at the per-range empirical κ. Old row:  **Conditional all-E theorem (restated)**: aggregate hypotheses H_Q(κ_Q) per stage (tail quadratic functional) and H_L(κ_L) (linear), plus H_align(ε) ⇒ no covering exists. Bound 0.872 (κ_Q=1), 0.928 (κ_Q=1.34, κ_L=1), 0.957–0.963 (κ_Q=1.5). The earlier Theorem C with pointwise H_dens is **WITHDRAWN** (false in its own model, found by V). | HYPOTHESIS-conditional; bound VERIFIED (float); hypotheses unproved. H_Q is supported out of sample only at the level κ_Q² ≈ 1.8 (see §5b) |
| T | General tail inequality B(∞) ≤ B(E) + T(E), with T explicit; T(E) = ∞ if δ_q = 0 beyond Q (§4.1); the quadratic tail needs only a *smooth-set* multiplicity bound, global second moments of n(e) are not enough (§4.3) | PROVED |
| A | Alignment criterion: ∩Λ_p contains a primitive vector ⇔ gcd(e_p,e_q) divides D_pq for all pairs; then the 2-D problem is exactly a 1-D covering of Z with moduli e_p | PROVED (+VERIFIED on 8918 families) |
| M | Lemma M: for random primitive forms E[c_pq] = ∏(1 + a_r (r−1)/(r+1)); matches the pool within 6% in every stage bucket | PROVED (Monte Carlo VERIFIED) + VERIFIED on data |
| U | **No unconditional all-E theorem was found**; every known gcd(2^n−1,3^n−1) bound is either ineffective (BCZ) or conditional | literature (§4.4) |

## 1. Structural lemmas

### 1.0 Remarks
(R1) Homogeneous certificates are impossible. If every killed set were a subgroup Λ_p (m ≡ −1 mod every p), take M = ∏(p−1) and (k,l) = (M+1, M): 2^k3^l ≡ 2 mod p for all p ∈ P, so p | 2−1, absurd. This uses only Fermat and also kills any certificate in which all killed sets are subgroups (Lean statement L3 below).
(R2) Cyclicity: Z²/Λ_p ≅ H_p is cyclic, so Λ_p ⊄ ℓZ² for every prime ℓ, and the image of Λ_p in F_ℓ² is a line L_p^{(ℓ)} if ℓ | e_p and everything if ℓ ∤ e_p.

### 1.1 Alignment criterion and 1-D reduction (answers 1(b) and the "direction lemma")
For p, q put D_pq = α_pβ_q − β_pα_q, g_pq = gcd(e_p, e_q).

**Lemma A [PROVED].** For a finite set P, M = ∩_{p∈P}Λ_p contains a primitive vector v of Z² ⇔ g_pq | D_pq for all p, q ∈ P.
*Proof.* M has finite index; its Smith form is diag(d₁, d₂) with d₁ | d₂, and M contains a primitive vector iff d₁ = 1 iff M_ℓ := M⊗Z_ℓ contains a primitive vector of Z_ℓ² for every ℓ. M_ℓ = ∩_{p: ℓ|e_p}Λ_{p,ℓ} (Λ_{p,ℓ} = Z_ℓ² if ℓ ∤ e_p). For ℓ | e_p, Λ_{p,ℓ} = ker(φ_p : Z_ℓ² → Z/ℓ^{a_p}) with φ_p primitive, a_p = v_ℓ(e_p). (⇒) a common primitive v has φ_p(v) = 0 = φ_q(v), and with φ_p, φ_q primitive this forces φ_p ≡ u φ_q (unit u) modulo ℓ^{min(a_p,a_q)}, i.e. ℓ^{min} | D_pq; take all ℓ. (⇐) Let p* maximise a_p and u a primitive generator of ker φ_{p*} (exists: some coordinate of φ_{p*} is a unit). The pairwise condition says ker(φ_p mod ℓ^{a_p}) = ker(φ_{p*} mod ℓ^{a_p}), so u ∈ Λ_{p,ℓ} for all p. ∎
(Check: `C_align.py` T1, 8918 families, pairwise criterion = direct lattice computation in all cases; the weaker criterion "lines coincide mod each prime ℓ" disagrees in 150, so the control fires.)

**Corollary (1-D reduction) [PROVED].** If v = (a,b) is primitive and v ∈ Λ_p for all p ∈ P, put π_v(k,l) = bk − al : Z² → Z. Then π_v(Λ_p) = e_pZ and A_p = π_v^{-1}(class mod e_p). So P covers Z² ⇔ the classes cover Z, with moduli exactly e_p, and p | 2^a3^b − 1 (or 2^a − 3^b) for all p ∈ P. No second-moment gain exists here (this is where the 2-D gain of DISTORTION.md disappears; the method is sharp on such families). `C_align.py` T2: 60 aligned families with random offsets, covered fractions in the torus and in Z/L agree; 60 non-aligned families fed through the same formula disagree in 58 (control).
Exact obstruction: such a family must have Σ_{p∈P}1/e_p ≥ 1; the best known aligned mass in the pool (agent B, CRT-greedy) is 0.672 at e_p ≤ 8·10⁵.

### 1.2 Common discrete logarithm T (answers 1(a))
Let 3 ∈ ⟨2⟩ mod p, 3 ≡ 2^{t_p}, t_p ∈ Z/o_p, o_p = ord_p 2. Then e_p = o_p, in the pool format this is gcd(α_p, e_p) = 1 with t_p = β_p α_p^{-1} (checked against pow(2, t_p, p) = 3 for all 59 574 such pool primes, `C_commonT.py`), and Λ_p = {(k,l): k + l t_p ≡ 0 mod o_p}. This is Lemma A with v = (T,−1).

**Lemma T1 [PROVED].** For finite P there is a common T (t_p ≡ T mod o_p for all p) ⇔ t_p ≡ t_q mod gcd(o_p, o_q) for all pairs (generalised CRT: pairwise suffices). Then P covers Z² ⇔ classes c_p mod o_p cover Z (j = k + lT).
**Lemma T2 (quadratic character) [PROVED].** If 3 ≡ 2^T mod p then (3/p) = (2/p)^T. So T even ⇒ every p ∈ P has p ≡ ±1 (mod 12); T odd ⇒ (3/p) = (2/p), i.e. p ≡ 1, 5, 19, 23 (mod 24).
*Instances.* p = 5: o = 4, 3 = 2³, T ≡ 3 (mod 4), T odd. p = 13: o = 12, 3 = 2⁴, T ≡ 4 (mod 12), T even. So **5 and 13 are never in the same common-T family** (t differ mod gcd = 4, and by T2). Also 7 (3 ∉ ⟨2⟩ = {1,2,4}), 17, 31, 73, 127 never appear (3 ∉ ⟨2⟩).
**What it kills [VERIFIED, `C_commonT.py`].** Σ_{e_p ≤ E} 1/e_p over primes with 3 ∈ ⟨2⟩: 1.299 (E=2000), 1.538 (2·10⁴), 1.731 (2·10⁵), 1.831 (8·10⁵) of the pool totals 1.973, 2.376, 2.700, 2.870. Splitting by T-parity: T even 0.792 / 0.965 / 1.107 / 1.181; T odd 0.927 / 1.104 / 1.246 / 1.321. So the parity lemma alone halves the usable mass but does not push it below 1 for large E. The exact maximum of Σ1/o_p over pairwise-compatible families (branch and bound, heavy primes first): 0.5627 (E=300), 0.6031 (1000), 0.6306 (3000), **0.6498 (8000, search complete)**, ≥ 0.6616 (20000, search hit the 600 s limit, so only a lower bound on the maximum). Hence **no covering with a common discrete log exists whose primes all have e_p ≤ 8000** (even without the distortion method), and the maximum grows by about 0.02 per factor 2.5 in E: CONJECTURED to stay < 1 (the expected value of Σ1/o_p over a compatible family is Σ1/o_p² < ∞ for a random T, so a covering needs a very atypical T). No proof for all E: the sum over pairwise coprime moduli o_p alone can reach 1 if n(o) is large (needs Σ_o n_1(o)/o over a coprime set), and bounding n_1(o) is the gcd problem of §4.4.

### 1.3 Other reductions
**Slice lemma [PROVED].** Restricting a covering to a line x₀ + Zv (v = (a,b) primitive) gives a 1-D covering of Z by classes mod m_p(v) = ord_p(2^a3^b) = e_p/gcd(φ_p(v), e_p), for those p whose coset meets the line; average of Σ_{active}1/m_p over x₀ equals Σ1/e_p, so no new density constraint.
**Direction lemma (L's lead 2) [PROVED].** If φ_p(v) is a unit mod e_p for every p ∈ P (⇔ v mod ℓ ∉ L_p^{(ℓ)} for every ℓ | e_p), every p is active on every parallel line and the restriction is a 1-D covering with moduli exactly e_p (each used n times for n primes of equal e). Such a v exists iff for every prime ℓ the lines {L_p^{(ℓ)} : ℓ | e_p} are not all ℓ+1 directions of F_ℓ² (CRT, v primitive since v ≢ 0 mod ℓ). **What it proves unconditionally: nothing beyond Σ1/e_p ≥ 1.** The 1-D theorems (Hough–Nielsen: some modulus divisible by 2 or 3 for *distinct* moduli; BBMST: distinct moduli have min ≤ 616 000; Klein–Koukoulopoulos–Lemieux, arXiv:2212.01299 Thm 3: multiplicity s ⇒ min modulus ≤ exp(c log²(s+1)/log log(s+2))) bound the *smallest* modulus, whereas every covering contains primes with tiny e_p (5, 7, 13, …); they would apply only to a residual family after the small primes are removed, and the residual is not a covering. So I get no theorem from them.
**Local remark.** For a prime ℓ and Γ = preimage of a line L' ⊂ F_ℓ², A_p ∩ (s+Γ) is a coset of index e_p (L_p ≠ L') or lies in a single coset of Γ with relative density ℓ/e_p (L_p = L'); the averages over the ℓ cosets agree with Σ1/e_p. This is the elementary shadow of the distortion step.

## 2. Sun–Lettl pruning (L's lead 2 of the first message)
**Theorem (Z.-W. Sun, Acta Arith. 2008, arXiv:math/0411144, Thm 1.3; I read the statement).** For a cover {a_sG_s}_{s≤k} of an abelian group G (arbitrary, not necessarily finite) by cosets and a coset t whose removal destroys the cover: [G:G_t] ≤ 2^{k−1} and k ≥ 1 + f([G:G_t]), f(n) = Σ_{q^a‖n} a(q−1).
Apply to G = Z², G_s = Λ_p. A minimal sub-certificate with k primes has e_p ≤ 2^{k−1}, f(e_p) ≤ k−1 and P⁺(e_p) ≤ k for each of its primes.
**Corollary S [PROVED given B].** A covering with ≤ 19 primes has a minimal sub-certificate with e_p ≤ 2^{18} < 4·10⁵, excluded by the exact B(4·10⁵) = 0.730584 (rational). With ≤ 20 primes: e_p ≤ 2^{19} < 8·10⁵, excluded by B(8·10⁵) (float; certified pool). So **a covering has ≥ 20 primes (exact) / ≥ 21 (float)**. (Agent V: the same.) The finite pools S_K = {e : f(e) ≤ K−1} are tiny: |S_21| = 565, |S_28| = 1786, |S_34| = 4266, of which above 8·10⁵: 1, 211, 1265 (`C_sun.py`). For K ≤ 20 the pool is inside the certified range; K = 21 adds only e = 2²⁰ (3-smooth: it can only increase the light mass λ).

## 3. Theorem Z: a covering needs thousands of large-index primes [VERIFIED; PROVED given the float B']

Let E₀ = 8·10⁵, δ = the optimised vector of the 8·10⁵ run with δ_q replaced by min(δ_q, CAP) (`stages_E800000.npz`), g_q = 1/(1−δ_q) (g = 1 for q = 2, 3 and for q outside the run), B' := the distortion bound of the *whole* pool with this δ (`distort_fast.costs`, `B_E800000.pkl`; with CAP = 1 it reproduces B(8·10⁵) = 0.742445, the control).
**Claim.** If P is a covering and P_> = {p ∈ P : e_p > E₀}, N = |P_>|, then
 1 ≤ s(N)·B' + Σ_{p∈P_>} ρ(e_p),  ρ(e) = r(e) ∏_{q | e, q ≥ 5} g_q / e,  r(e) = R_max = 2.6145 if gcd(e,6) > 1 else 1,  s(N) = (1−α*)/(1−α*−N/E₀), α* = 0.626827.
*Proof.* (i) By M1 (DISTORTION.md), 1 ≤ Σ_ℓ cost_ℓ(P_ℓ). (ii) cost_ℓ(F ∪ G) ≤ cost_ℓ(F) + E[α_G]/(1−δ_ℓ) since (x+y−δ)₊ ≤ (x−δ)₊ + y. (iii) For F = P ∩ pool, the stage bounds of the run are monotone in the family (m₁, m₂ are sums of nonnegative terms, the majorant coefficients are nonnegative) and valid for any earlier sets (L1 uses only δ), so Σ cost_ℓ(F_ℓ) ≤ B'. (iv) For p ∈ G, E[α_p] ≤ P_{<ℓ}(A_p) ≤ r_p ∏_{q | e_p, 5 ≤ q < ℓ}(1−δ_q)^{-1}/e_p (L1 + L4″), and the stage factor (1−δ_ℓ)^{-1} completes the product over all q | e_p; set δ_q = 0 for q outside the run (such stages are empty in the pool, so B' is unchanged). (v) Tail primes with 3-smooth e_p lie in B₂₃ and raise α₂₃ by Σ1/e_p ≤ N/E₀; every price scales by at most (1−α*)/(1−α*−N/E₀), and costs scale at most linearly in the prices (the majorants are linear in m₁, m₂). ∎
**Bounding ρ.** ρ is multiplicative apart from r and every prime power has h(q^a) = g_q/q^a < 1, so ρ(e) is maximised by a DFS over 400-smooth e just above E₀ (exact, `C_size.py`); e = m·Q with a prime Q > 400, m ≤ E₀ smooth, is bounded by RMAX·∏g(m)·g_max^w/max(401^w m, E₀+1) for w = 1…4 large primes and RMAX(g_max/401)^5 beyond; e > 64E₀ is bounded by 2⁴RMAX/(64E₀). **Result.** s(N)B' + Nc ≥ 1 first holds at N = N_Z, so a covering contains ≥ N_Z primes with e_p > 8·10⁵ (hence ≥ N_Z primes in all). Table (`C_size.py CAP`; the control CAP = 1 reproduces 0.742445):

| CAP | B' | c = max ρ | N_Z |
|---|---|---|---|
| 0.10 | 1.231 | 5.5·10⁻⁶ | none (B' > 1) |
| 0.20 | 0.9226 | 9.9·10⁻⁶ | 5916 |
| 0.25 | 0.8362 | 1.37·10⁻⁵ | 9869 |
| 0.27 | 0.8100 | 1.57·10⁻⁵ | 10275 |
| **0.28** | **0.7984** | **1.68·10⁻⁵** | **10300** |
| 0.285 / 0.29 / 0.27 / 0.26 / 0.24 / 0.22 / 0.20 / 0.17 / 0.14 | 0.7931 / 0.7882 / 0.8100 / – / – / – / – / – / – | – | 10266 / 10202 / 10275 / 10135 / 9457 / 8093 / 5916 / 815 / 1 |

Cap scan below 0.28 (`C_size_caps2.log`, plus `C_size_caps.log`): N peaks at cap 0.28 (10300), falls for caps below 0.27, and is 1 at cap 0.14. Optimum over the scanned caps is 0.28. Joint re-optimisation of δ for (1−B′)/ρ_max was not done (gap).
| 0.30 | 0.7795 | 1.93·10⁻⁵ | 10001 |
| 0.35 | 0.7538 | 2.76·10⁻⁵ | 8153 |
| 0.50 | 0.7435 | 3.89·10⁻⁵ | 6183 |

Smaller caps lower the inflation g_q of large-q stages (the optimiser's own δ has spikes up to 0.95 near q = 307, which would give g = 20) at the price of a larger B'; the best cap is a compromise and a joint optimisation of δ for this objective would increase N_Z further (not done).
**Scaling.** N_Z ∝ (1 − sB')/c ∝ E₀: a certified pool up to 1.6·10⁶ would roughly double it.
Reading (CAP 0.28 numbers): the large-index primes of a covering must carry *weighted* reciprocal mass ≥ 1 − s B' ≈ 0.17, each prime carrying at most 1.7·10⁻⁵. Combined with Sun: each of them has f(e_p) ≤ |P|−1, so |P| ≥ 6183 forces nothing more than smoothness e_p ≤ 2^{|P|−1}.
This is the unconditional theorem I can prove toward the target; it does not touch the all-E question because the number of allowed tail primes is unbounded.

### 3b. L's "stages q ≤ k" route, quantified
For a minimal certificate with k primes Sun gives P⁺(e_p) ≤ k and n(e) ≤ k, so only stages q ≤ k occur and a Li–Wang–Yi tail costs ≪ Σ_{y<q≤k} k²(log q)⁶/q² ≈ k²(log k)⁵/y. This is **weaker than Theorem Z's treatment**: with at most k primes in all, the *first-moment* (Lipschitz) bound already gives tail cost ≤ k·max_{e>E₀}ρ(e) ≤ k·1.7·10⁻⁵, and for primes in stages q > y the weight is ρ ≤ RΛ/q so their total is ≤ kRΛ_max/y, smaller than k²/y. The quadratic method only pays when the number of tail primes is unbounded, which is exactly the all-E case. So the best explicit unconditional K I can prove is the Z value K = 10 299 (it grows linearly with the certified pool, not like √y).

### 3c. Direction lemma, dichotomy per prime ℓ [PROVED] and what it gives
Fix ℓ and reduce mod ℓ: for ℓ | e_p, A_p mod ℓ is a coset of the line L_p^{(ℓ)} = Λ_p mod ℓ ⊂ F_ℓ², i.e. an affine line (index-ℓ coset), while for ℓ ∤ e_p it is everything. A nonzero v ∈ F_ℓ² lies in exactly one line through 0, namely the one it spans; φ_p(v) ≢ 0 mod ℓ ⇔ v ∉ L_p. Hence a vector v mod ℓ with φ_p(v) a unit-at-ℓ for all p with ℓ | e_p exists **iff the set {L_p^{(ℓ)}} of kernel directions is not all of P¹(F_ℓ)** (ℓ+1 lines). If this holds for every ℓ | lcm(e_p), CRT gives a primitive v ∈ Z² with φ_p(v) coprime to e_p for all p; then every slice x₀ + Zv is a 1-D covering of Z with moduli exactly e_p (each prime once; ψ_p restricted to the slice is t ↦ φ_p(v)t + const, a bijection of Z/e_p). If instead for some ℓ all ℓ+1 directions occur, no v works (this is the aligned-at-no-direction case, which needs ≥ ℓ+1 primes with ℓ | e_p).
**Corollary D (unconditional, uses recalled BBMST).** If P is a covering whose primes satisfy the dichotomy at every ℓ, have pairwise distinct e_p, and all e_p > 616 000, then the slice is a covering of Z with distinct moduli > 616 000, contradicting Balister–Bollobás–Morris–Sahasrabudhe–Tiba (min modulus of a covering with distinct moduli is ≤ 616 000; recalled from memory and from L6, not re-read). With multiplicity s = max n(e) the Klein–Koukoulopoulos–Lemieux bound (arXiv:2212.01299 Thm 3, as reported by L) replaces 616 000 by exp(c log²(s+1)/log log(s+2)) with an unspecified c. So the pure-large-modulus coverings (no prime with e_p ≤ 616 000, distinct e_p, generic directions) are excluded; this is of no use against general certificates because the small primes (e_p = 4, 6, 10, …) are exactly the ones a covering wants. It is a different regime from Theorem Z (which excludes coverings with few large primes).

### 3d. Sharper per-prime price for new primes [PROVED reduction; VERIFIED numbers] (round 4, 2026-10-30)
The price r_p = R(A_p) of a new prime p depends only on the image of Λ_p in (Z/144)² (rtypes.py: the heavy {2,3} sets read x mod 144). Z²/Λ_p is cyclic of order e_p, so Z²/(Λ_p+144Z²) is a cyclic group of order gcd(e_p,144) (a quotient of Z/e_p and of (Z/144)², and ψ_p mod gcd(e_p,144) is onto). Hence r_p ≤ r(gcd(e_p,144)) := max R over the CYCLIC-quotient types of that index in `coupled_full_E200000.txt` (HNF key (a,c,d) with gcd(a,c,d)=1, index ad). The file holds all 781 such types with index > 1 (n·∏_{r|n}(1+1/r) per index n | 144, checked; V §2 enumerated them independently). Table: r(1)=1, r(2)=1.648, r(3)=1.462, r(4)=1.830, r(6)=2.106, r(8)=r(16)=1.836, r(9)=1.488, r(12)=r(36)=2.2413, r(24)=r(48)=r(72)=r(144)=2.2419. **The old RMAX = 2.6145 is attained only by non-cyclic types (intersections), never by a single new prime.**
The DFS reduction of C_size.py stays valid: multiplying e by 2 or 3 multiplies r by at most 1.648 < 2 and 1.462 < 3 (all ratios r(2g)/r(g), r(3g)/r(g) in the table checked), and by q ≥ 5 multiplies ρ by g_q/q < 1.
**Result (`C_rho2.py`, `C_rho2_cap028.log`; δ = V_delta_cap028.json, B′ = 0.798372 float):** max ρ = 1.2496·10⁻⁵ at e = 870870 (gcd 6), was 1.6806·10⁻⁵ at e = 803985; large-prime part 8.46·10⁻⁶. **N_Z = 13 184** (was 10 300). Why the baseline moved: same cap 0.28, same δ-vector and same B′ = 0.798372 (reproduced with the regenerated pickle); the only change is ρ_max, from 1.6806·10⁻⁵ (price RMAX = 2.6145 for every e with gcd(e,6) > 1) to 1.2496·10⁻⁵ (cyclic-type price r(gcd(e,144)) ≤ 2.2419). N ≈ (1 − s·B′)/ρ_max scales by 1.6806/1.2496 = 1.345, and 10 300 × 1.345 ≈ 13 850 before the light-mass factor s(N), which grows with N; the exact solve gives 13 184. Joint δ re-optimisation (`C_opt.py`, coordinate ascent with steps 0.04/0.02/0.01/0.005 on δ_q for the 78 primes 5 ≤ q ≤ 400 plus a common cap Cbig ≤ 0.28 on q > 400 (base vector V_delta_cap028.json), objective = the N of C_size.py with B′ recomputed from the pickle and ρ_max from the incidence sets of `C_rhoset.py`; log `C_opt.log`, vector **`C_opt_best.json`**): N = 13 813 / 13 962 / 14 006 / 14 013 after sweeps 0–3. Final: B′ = 0.785224 (float), ρ_max = 1.2568·10⁻⁵ at e = 903210, checked independently of the optimiser by `C_rho2.py C_opt_best.json 0.785224` (`C_rho2_opt.log`): **N_Z = 14 013**. V's fix CORR = 1.0000251 (the table prices use λ = 0.0485, the light mass at 8·10⁵ is 0.04850936) is now applied to r in `C_rho2.py`: N_Z unchanged (14 013 for the optimised vector, 13 184 at cap 0.28). V confirmed the §3d reduction and ρ_max = 1.24965·10⁻⁵ (cap 0.28). The optimum keeps δ_q ≈ 0.28 for q ≤ 23 and raises δ_q to 0.32–0.50 for 29 ≤ q ≤ 400 (larger q only enter ρ_max through e with a large prime factor, where the factor g_q/q is small). The step gains are shrinking (+7 in the last sweep); Cbig never moved off 0.28, the upper end allowed by the base vector (raising it needs the uncapped base; not done). B′ for this vector is float; V's exact verifier was run on the cap-0.28 vector, not on this one.

## 4. The tail for all E

### 4.1 The linear tail and why δ_q = 0 beyond Q fails [PROVED]
Fix δ (any sequence in [0,1)). For every covering P: 1 ≤ Σ_ℓ[Ĉ_ℓ(P_ℓ ∩ {e ≤ E})] + T(E), with
 **T(E) = Σ_{p∈P, e_p>E} r_p ∏_{q|e_p, 5≤q}(1−δ_q)^{-1} / e_p**
(proof: §3 steps (ii)–(iv)). Taking sup over P, with δ_q = 0 for q > Q this is Σ_{p: e_p>E} r_p∏_{q|e_p,q≤Q}(1−δ_q)^{-1}/e_p ≥ Σ_{e_p>E}1/e_p, which **diverges** (Σ_{e_p ≤ E}1/e_p ≈ 1.58 log log E, data: increments 1.55–1.58 per unit log log over 1.25·10⁴ ≤ E ≤ 8·10⁵; CONJECTURED). So B(∞) ≤ B(E) + T(E) is vacuous with δ = 0 on large stages; large stages must be treated by the quadratic (second-moment) majorant, which is where multiplicity enters.

### 4.2 The quadratic tail [PROVED]
For a stage ℓ and δ_ℓ ∈ (0,1): (x−δ)₊ ≤ x²/(4δ) gives cost_ℓ ≤ m₂(ℓ)/(4δ_ℓ(1−δ_ℓ)); at δ_ℓ = ½ this is m₂(ℓ) = E_{P<ℓ}[(Σ_{active}ℓ^{-v_p})²] ≤ ℓ⁻²E[N_ℓ²], N_ℓ = number of active stage-ℓ primes. By the pair bound P(A_p ∩ A_q) ≤ 1/lcm(e_p,e_q) (Z²/(Λ_p∩Λ_q) surjects onto both cyclic quotients) and Λ_pq ≤ Λ_pΛ_q: E[N_ℓ²] ≤ R Σ_{p,q∈st(ℓ)} Λ_pΛ_q gcd(e'_p,e'_q)/(e'_p e'_q). With n(e) ≤ s(e): ≤ R s² Σ_{e',f' ℓ-smooth} 2^{ω(e')+ω(f')} gcd(e',f')/(e'f') ≪ s²(log ℓ)⁶, which is the Li–Wang–Yi shape. This is the only place multiplicity enters.

### 4.3 What multiplicity hypothesis suffices (answer to the coordinator's question)
Let st(ℓ) = {e : P⁺(e) = ℓ}. E[N_ℓ] = Σ_{e∈st(ℓ)} n(e)Λ(e)/e', e' = e/ℓ^v, a sum over ALL ℓ-smooth cofactors e'.
* **Pointwise polylog [suffices].** If n(e) ≤ (log e)^A for e > Q₁ then E[N_ℓ²] ≪_A (log ℓ)^{2A+6}, so Σ_{ℓ>Q₁} cost_ℓ ≪ (log Q₁)^{2A+5}/Q₁ → 0. More generally n(e) ≤ exp(c(log e)^θ) with θ < ½ works: Σ_{e' ℓ-smooth} exp((log e')^θ)/e' = exp(O((log ℓ)^{θ/(1−θ)})) = ℓ^{o(1)} by Dickman decay, while for θ ≥ ½ or any fixed power e^η this sum is ℓ^{ω(1)} or worse (Π_{q<ℓ}(1−q^{η−1})^{-1} = exp(ℓ^η/(η log ℓ))).
* **Pointwise in P⁺ [L's form] suffices.** n(e) ≤ P⁺(e)^{1/2−ε} for all e in stage ℓ gives E[N²] ≪ ℓ^{1−2ε}(log ℓ)⁶ and cost_ℓ ≪ ℓ^{−1−2ε}(log ℓ)⁶, summable. Heuristically this is false for astronomically smooth cofactors (n(e) can be ≈ log e/log log e), so I do not use it as H.
* **A global second moment Σ_{e≤X} n(e)² ≪ X^{1+ε} is NOT enough.** It allows n(e) ≈ e^{(1+ε)/2} on the sparse set of smooth e (there are only X^{o(1)} of them below X), and then E[N_ℓ] ≥ Σ_{e'} e'^{-1/2+ε/2} over ℓ-smooth e' = exp(Θ(√ℓ/log ℓ)). Averages must be taken over smooth sets and divisibility classes, which is the form of H_dens below.
* **Numerically (rough, not a proof).** With n(e) ≤ log e, g_q ≤ 2 and worst-case alignment, M₂(ℓ) ≈ 4·10⁻¹² at ℓ = 10¹² and Σ_{ℓ>Q₁}M₂ ≈ 0.16 at Q₁ = 10¹², ≈ 3·10⁻³ at Q₁ = 10¹⁴ (Mertens-level estimates; constants not certified). For small stages a pointwise bound is hopeless: the true mean of n(e) is ≈ 0.8(e/φ(e))/log e ≈ 0.06, while a constant bound s = 1 already costs > 2 at ℓ = 100.

### 4.4 Literature: unconditional input on gcd(2^n−1, 3^n−1) (all read 2026-10-26 from abstracts/slides/arXiv text)
* Bugeaud–Corvaja–Zannier 2003: log gcd(a^n−1, b^n−1) ≤ εn for n ≥ n₀(a,b,ε), via Schmidt's Subspace Theorem; **ineffective** (n₀ unspecified, confirmed in arXiv:2606.07959 §2 and Levin's slides). Extended to S-units (Corvaja–Zannier, Hernández–Luca), polynomials, recurrences (Levin, Grieve–Wang).
* Lower bound (Adleman–Pomerance–Rumely, via BCZ): log gcd(2^n−1,3^n−1) > exp(c log n/log log n) for infinitely many n; hence n(e) is unbounded in e unless the gcd is spread over many primes (consistent with CONJECTURED max n(e) ~ log e/log log e).
* Ailon–Rudnick (Acta Arith. 113, 2004): for integers, "a^k−1 and b^k−1 coprime for infinitely many k" is a **conjecture** (open for (2,3)); the polynomial case is proved.
* I found **no average (mean-value) result** for log gcd(2^n−1, 3^n−1), no effective power-saving bound, and nothing on #{p : e_p ≤ y} beyond the trivial n(e) ≤ e log 2/log(e+1) and the lattice count #{p : e_p ≤ E} ≪ E^{3/2} (L11: Minkowski gives (i,j) ∈ Λ_p with max(|i|,|j|) ≤ √e_p, so p | 2^i3^j−1).
* GRH-conditional: Moree–Stevenhagen (two-variable Artin: density of p with 3 ∈ ⟨2⟩ exists, positive, a rational multiple of ∏(1−p/(p³−1))); Agrawal–Pollack, arXiv:1912.02554 (ord_p 2 = ord_p 3 infinitely often, positive density). Unconditional lower bound for the two-variable Artin problem: arXiv:1711.06410. Matthews/Erdős–Murty/Elsholtz: |⟨2,3⟩ mod p| ≥ p^{2/3−ε} for almost all p, i.e. only density-one information, silent about the exceptional primes that form the pool.
**Conclusion U.** The tail Σ_{e_p>E} cannot be controlled unconditionally by any published result I found.

## 5. Theorem C with pointwise H_dens — WITHDRAWN (kept for the record; superseded by §5b)
**Withdrawn 2026-10-26.** V (V_check.md §3.4) showed H_dens(κ) "for every ℓ and every d" is false in the very Poisson model it was calibrated on: taking d equal to a realised e, the single term G/e exceeds the expected mass of all multiples of d (worst LHS/RHS 6.2 at ℓ=5,7, probability 1 of failure for κ ≤ 2). Nothing in §5 below this line is to be cited; the table is not a theorem.

**Data/model.** E₀ = 8·10⁵. Profile: δ = vector of the 8·10⁵ run for ℓ < 1000, δ = ½ for ℓ ≥ 1000 and for q outside the run (A's choice; the stage costs below ℓ = 1000 are the run's, ℓ ≥ 1000 is re-evaluated with moments). G(e) = ∏_{q|e,q≥5}(1−δ_q)^{-1}. Reference density n̂(e) = κ τ e/φ(e), τ = C₀/ln E₀, C₀ = 0.813 (calibrated on e ≤ E₀). Random-form weights θ(d) = ∏_{q|d}(q−1)/(q+1).
**H_dens(κ).** For every prime ℓ ≥ 5 and every d: Σ_{e>E₀, P⁺(e)=ℓ, d|e} n(e)G(e)/e ≤ Σ_{same} n̂(e)G(e)/e (this absorbs κ). [Includes the 3-smooth part: Σ_{3-smooth e>E₀} n(e)/e ≤ κ·4.2·10⁻⁶, which changes all prices by < 3·10⁻⁵ relative.]
**H_align(ε).** For every ℓ the tail pair sum Σ_{p≠q∈st(ℓ),>E₀ or one in pool} Λ_{pq}c^<_{pq}/(e_pe_q) is at most (1+ε)Σ_d θ(d)Y_d Y_d' (Y_d the corresponding first-moment functional).
**Theorem C.** Under H_dens(κ) and H_align(ε) no finite set of primes covers Z². Quantitatively (`C_tail.py κ L1 x ε`, stage costs min(linear, moment), stages ℓ < 3·10⁶ evaluated, tail beyond ≈ 4·10⁻⁵ by monotone extrapolation of the last term 2·10⁻¹⁰ per stage):

| κ | ε | total bound |
|---|---|---|
| 1.0 | 0 | 0.8635 |
| 1.2 | 0 | 0.8960 |
| 1.5 | 0 | 0.9507 |
| 2.0 | 0 | 1.0572 (inconclusive) |
| 1.0 | 0.25 | 0.8897 |
| 1.0 | 0.5 | 0.9160 |
| 1.5 | 0.25 | 0.9973 |
| 1.3 | 0.25 | 0.9514 |
| 1.3 | 0.10 | 0.9286 |

So H_dens(1.5) with H_align(0) or H_dens(1.3) with H_align(0.25) closes the problem; the margin is ≈ 5%. The proof is §4 with: pool part exact (M₁, M₂ of the run), tail part m₁ = R κτ F₁^{>}, m₂ = M₂^{pool} + R[2κτ Σ_d θ(d) Y_d^{pool} F_d^{>} + (κτ)² Σ_d θ(d)(F_d^{>})²] + m₁^{tail}/ℓ, F_d^{>} = (closed Euler product over all e) − (enumerated e ≤ E₀), R = 2.68 ≥ the largest coupled price; Σ_dθ(d)F_d² has the closed local factor s_q² + g_q²q⁴/((q−1)⁴(q+1)²) (derivation: Σ_{c≥1}ρ_q F_q(c)², F_q(c) = g_q q^{2−c}/(q−1)²). It differs from agent A's `tail_bound.py` (which I patched, copy `C_tail.py`) only in the alignment model: A's "noalign" used c = 1 (undercounts pair sums by 35–47%, see below) and r_p·R for pool-tail pairs (overcounts), its "align" mode used the worst case c = gcd (overcounts by 2.4–3.6×, total 22.8).
**Why the random-form model is justified.**
* **Lemma M [PROVED].** For independent uniform primitive forms mod e₁, e₂, g = gcd: P(g' | D) = 1/(g'∏_{r|g'}(1+1/r)) for g' | g (points of P¹(Z/g')), and Σ_{d|g}φ(d)P(d | D) = ∏_{r^a‖g}(1 + a(r−1)/(r+1)). Monte Carlo (9 pairs, 2·10⁵ samples each): max deviation 0.7%, the control c = τ(g) is off by up to 67% (`C_lemmaM.py`).
* **Data [VERIFIED, `C_alignmodel.py`]** Ratio actual Σ w_pw_q c^<_pq / model Σ w_pw_q E[c] over the 8·10⁵ pool, by stage bucket ℓ ∈ [5,6), [7,12), [12,30), [30,100), [100,300), [300,1000), ≥1000: 0.942, 1.011, 0.965, 0.991, 1.010, 1.005, 0.993 (up to 2.9·10⁶ pairs per bucket). Controls: against c = 1 the ratio is 1.35–1.47, against the worst case c = g it is 0.28–0.42. So ε = 0.05 is supported by the data.
* **H_dens out-of-sample [VERIFIED, `C_testH.py`].** C₀ calibrated on (E₁/2, E₁] only, tested on (E₁, 8·10⁵] with the stage weights G: total ratio data/model 1.008 (E₁ = 10⁵), 0.994 (2·10⁵), 0.999 (4·10⁵); by P⁺-bucket (5, 7, 30, 100, ≥1000): 1.25–1.30, 1.14–1.18, 1.05–1.09, 1.01, 0.94–0.95. The two small-ℓ buckets exceed 1 but carry < 0.5% of the tail mass (their κ is 1.3, which the table above covers). Controls: dropping e/φ(e) gives bucket ratios 2.1/1.8/1.35/1.07/0.87; 1/log²e gives 1.37/1.30/1.20/1.13/1.06; both have clearly worse bucket profiles, although the *total* ratios (1.04–1.13) are not discriminating, because the total is dominated by one bucket. **The bucket-by-(ℓ,d) form of H_dens is not tested; only 5 aggregated buckets.**
**Gaps, stated plainly.** (a) H_dens is an unproved statement about the multiplicity of e_p for e > 8·10⁵, for all ℓ and all d, extending to infinity; the calibration constant is fitted. (b) The sum over stages ℓ > 3·10⁶ is extrapolated, not summed (≈ 4·10⁻⁵, safe by two orders). (c) B(8·10⁵) is float, the 4·10⁵ exact value 0.730584 would need the whole tail redone at E₀ = 4·10⁵ (tail mass larger). (d) The pool-tail cross terms use single price R = 2.68 for all pairs (conservative). (e) The profile δ is not re-optimised against the tail; a joint optimisation should lower the totals.

## 5b. Theorem C′ (restated with aggregate hypotheses) [HYPOTHESIS-conditional]

The proof consumes only, per stage ℓ, the linear functional Y₁ = Σ_{e>E₀, P⁺(e)=ℓ} n(e)Λ(e)/e and the quadratic functional Q_ℓ^> = Σ_d θ(d)(Y_d^>)², Y_d^> = Σ_{e>E₀, P⁺(e)=ℓ, d|e'} n(e)Λ(e)/e, θ(d)=∏_{q|d}(q−1)/(q+1) (pointwise-in-d statements are never used). Model values: Y₁^{mod} = τ F₁^>, Q^{mod} = τ²Σ_dθ(d)(F_d^>)² with τ = C₀/ln E₀ (κ=1), F as in the withdrawn §5 (closed Euler products minus the enumerated e ≤ E₀).
* **H_L(κ_L).** For every ℓ ≥ 5 (small and large stages alike, including the y-smooth e > 8·10⁵ at ℓ < 30, and the 3-smooth part): Y₁^> ≤ κ_L Y₁^{mod}.
* **H_Q(κ_Q).** For every ℓ ≥ 5: Q_ℓ^> ≤ κ_Q² Q_ℓ^{mod}.
* **H_align(ε)** as before (pair alignment excess; Lemma M).
**Theorem C′.** Under H_L, H_Q, H_align no finite P covers Z². The cross term between the exact pool functional Y^{pool} and the tail is bounded by Cauchy–Schwarz in the θ-weighted inner product, 2Σθ Y^{pool}Y^> ≤ 2κ_Q τ √(S2data·S2tail), so no mixed hypothesis is needed. Totals (`C_tail.py κ_L 1000 x ε κ_Q tailonly`, `C_tailQ_grid2.log`; stages ℓ < 3·10⁶, tail beyond that ≈ 4·10⁻⁵):

| κ_L | κ_Q | ε | total bound |
|---|---|---|---|
| 1.0 | 1.0 | 0 | 0.8719 |
| 1.0 | 1.2 | 0 | 0.9038 |
| 1.0 | 1.34 | 0 | 0.9280 |
| 1.2 | 1.34 | 0 | 0.9303 |
| 1.0 | 1.5 | 0 | 0.9574 |
| 1.2 | 1.5 | 0 | 0.9598 |
| 1.5 | 1.5 | 0 | 0.9633 |

All totals < 1, so H_Q(κ_Q ≤ 1.5) with H_L(κ_L ≤ 1.5), H_align(0) gives the contradiction; the margin is 4–13%. H_align(0.25) is not in the grid for the tail-only version (the earlier pooled variant, which also scales the exactly known pool part by κ_Q², gives 1.03–1.18 and does not close; that variant is the wrong hypothesis because the pool part is known, listed in `C_tailQ_grid.log`).
**Testing H_Q out of sample [`C_testQ.py`, `C_testQ.log`].** C₀ calibrated on (E₁/2, E₁], Q_real/Q_model computed on the window (E₁, 8·10⁵] with real n(e) from the pool, prices Λ at cap 0.28, buckets of ℓ:
| window | ℓ=5–6 | 7–11 | 12–29 | 30–99 | 100–999 | ≥1000 | total |
|---|---|---|---|---|---|---|---|
| (10⁵, 8·10⁵] | 1.55 | 1.51 | 1.55 | 1.35 | 1.21 | 1.16 | 1.30 |
| (2·10⁵, 8·10⁵] | 1.64 | 1.66 | 1.47 | 1.29 | 1.20 | 1.17 | 1.25 |
| (4·10⁵, 8·10⁵] | 1.76 | 1.77 | 1.46 | 1.39 | 1.21 | 1.22 | 1.29 |
Controls: data inflated ×1.5 gives total 2.8–2.9 (the test detects a 1.5× excess of multiplicity); the model without e/φ(e) gives 2.0–2.1 total and 4–6.5 at ℓ < 30. So H_Q holds on these windows with κ_Q² ≈ 1.8, i.e. κ_Q ≈ 1.34 (the worst bucket, 1.77). Single stages 5…29 range 1.17–1.89 (stage 3 is the 3-smooth part and is erratic, 1.6–5.7; it is carried by the separate 3-smooth estimate).
**Finding that changes the picture.** The Poisson model of the withdrawn §5 underpredicts Q: `C_testQ_sim.py` (12 Poisson draws of n(e) with the same n̂) gives Q-ratios 1.0–1.2 per bucket with ranges that exclude the data values (1.2–1.8) for ℓ ≥ 12. So real multiplicities n(e) are over-dispersed or clustered across multiples relative to independent Poisson, and the earlier "model-consistent κ ≈ 1.05" is not available. The honest statement is the empirical κ_Q ≈ 1.34 from the table, with a ≈ 7% margin at that value.
**Gaps, stated plainly.** (a) H_L and H_Q are unproved statements about all e > 8·10⁵ for all stages; their evidence is three out-of-sample windows below 8·10⁵, in which the ratio is not shrinking toward 1 (1.25–1.30 total) and the Poisson model does not explain it; extrapolation to e → ∞ is an assumption. (b) The per-stage ratios at ℓ = 5, 7 are noisy (few e per window); the bucket value 1.77 is used for all stages, and large stages ℓ ≥ 1000 are tested only in aggregate. (c) The small-stage y-smooth e > 8·10⁵ are covered by H_Q/H_L directly but nothing proves finiteness or density of such e. (d) Items (b)–(e) of the withdrawn list (extrapolation beyond ℓ = 3·10⁶, float B(8·10⁵), single price R = 2.68, δ not re-optimised) still apply. (e) C₂'s H_cls route for ℓ ≥ Q remains a weaker alternative for large stages and does not cover ℓ < 30.

## 5c. Theorem C″: hypotheses on weighted stage RANGES (round 4; repairs V_check.md §8.2) [HYPOTHESIS-conditional]
V found that H_L, H_Q of §5b, stated "for every ℓ", fail stage by stage on the data (single large stages up to 8× and 33× the model). The proof never needs a single stage once the majorant is fixed in advance: for each stage ℓ, `C_tailR.py` fixes, from the model alone, one majorant that is **linear** in (m₁, m₂): either the Lipschitz one, cost = c_fin + R*·Y₁^>/(1−δ), or (a m₁ + b m₂)/(1−δ) with (a,b) ∈ {(1,0), quadratic (0,(x−δ)/x²), tangent (1−2δ/t, δ/t²)}. Then the stage cost is linear in Y₁^> and in X_ℓ = cross_ℓ + Q_ℓ^>, with cross_ℓ ≤ 2√(S_ℓ Q_ℓ^>) (θ-Cauchy–Schwarz, S_ℓ the exact pool functional), and over a range R, Σ v_ℓ(2√(S_ℓQ_ℓ) + Q_ℓ) ≤ 2√(Σ v S)√(Σ v Q) + Σ v Q (Cauchy–Schwarz in ℓ). So only the following are consumed, for the eight ranges R = [5,7), [7,12), [12,30), [30,100), [100,10³), [10³,10⁴), [10⁴,10⁵), [10⁵,∞):
* **H_L^R(κ_L,R):** Σ_{ℓ∈R} w_ℓ Y₁,ℓ^> ≤ κ_L,R Σ_{ℓ∈R} w_ℓ Y₁,ℓ^{mod},  w_ℓ = R*(a+b/ℓ)/(1−δ_ℓ) (Lipschitz stages: R*/(1−δ_ℓ));
* **H_Q^R(κ_Q,R):** Σ_{ℓ∈R} v_ℓ Q_ℓ^> ≤ κ_Q,R² Σ_{ℓ∈R} v_ℓ Q_ℓ^{mod},  v_ℓ = (1+ε)R* b/(1−δ_ℓ);
* H_align(ε) as before. The weights are fixed numbers, saved in `C_tailR_weights.npz` (choice made at κ_Q = 1.34).
`C_tail.py` scales the tail pieces uniformly: with the pieces saved at κ = 1 (`C_tailpieces_L1000.npz`; it reproduces the §5b total 0.8719), every tail term is Y₁^{mod}·κ_L or Q^{mod}·κ_Q² or the Cauchy–Schwarz cross term 2κ_Q√(S·Q^{mod}); nothing else depends on κ (checked in the code, lines m1/m2 of the tailonly mode).
**Totals (`C_tailR.log`):** uniform κ: (κ_L, κ_Q) = (1,1): 0.8863; (1,1.2): 0.9210; (1,1.34): 0.9471; (1.2,1.34): 0.9495; (1,1.5): 0.9789; (1.5,1.5): 0.9852. Fixing the majorant and summing over ranges costs 1.5–2% against the per-stage-min version of §5b.
**Out-of-sample test with these weights (`C_testQR.py`, `C_testQR.log`;** C₀ calibrated on (E₁/2, E₁], window (E₁, 8·10⁵], E₁ = 10⁵, 2·10⁵, 4·10⁵; max over the three windows**):**
| R | [5,7) | [7,12) | [12,30) | [30,100) | [100,10³) | [10³,10⁴) | [10⁴,10⁵) | [10⁵,∞) |
|---|---|---|---|---|---|---|---|---|
| κ_L (L-ratio) | 1.26 | 1.26 | 1.19 | 1.10 | 1.01 | 0.97 | 0.96 | 0.90 |
| κ_Q² (Q-ratio) | – (v=0) | 1.83 | 1.53 | 1.35 | 1.15 | 1.13 | 1.77 | 5.25 |
Control "no e/φ(e)": L 2.06–2.29 and Q 3.9–6.8 at ℓ < 30 (detected). With these per-range empirical κ the total is **0.9084**; with the cruder uniform κ_L = 1.5, κ_Q² = 2.25 on ℓ < 10⁴ and κ_Q² = 4, 9 on the two top ranges it is **0.9961** (still < 1, margin 0.4%). The top ranges [10⁴,∞) are thin in the window (few e per stage), their Q-ratios 1.4–5.3 are noisy, and they carry < 2% of the total.
**δ re-optimisation for C″ (`C_tailopt.sh`, `C_tailopt.log`; knobs: L1 = first stage set to DBIG, DSCALE multiplies the run δ, DCAP caps it):** totals at uniform (κ_L,κ_Q) = (1,1.34) / per-range empirical κ: base (L1=1000, DBIG=0.5) 0.9471 / 0.9084; DBIG 0.4: 0.9445 / 0.9054; DBIG 0.6: 0.9549 / 0.9169; L1=300: 0.9105 / 0.8810; L1=3000: 1.0400 / 0.9725; DSCALE 0.9: **0.8931 / 0.8682**; DCAP 0.5: 0.9154 / 0.8845 (DSCALE 1.1 pushes δ above 1: invalid). Cyclic price on the linear tail terms (V's fix 2; single new cosets have price ≤ 2.2419·CORR, pair terms keep R* = 2.680; `RLIN=2.24191`): base 0.9452 / 0.9064, DSCALE 0.9: 0.8914 / 0.8664 (gain ≈ 0.002). Lowering δ helps: the run δ was optimised for the finite pool and over-tilts against the tail. Second scan (combinations) running, `C_tailopt2.log`.
**Gaps.** (a) H_L^R, H_Q^R are unproved; the evidence is three windows below 8·10⁵, ratios do not shrink with the window. (b) The weights depend on δ; a re-optimised δ changes the hypothesis (re-tested for the final profile only). (c) Earlier gaps (extrapolation beyond ℓ = 3·10⁶, float B, single price R*) stand.

## 6. Lean-formalisable statements (elementary only)
```lean
-- L1 (R1, homogeneous certificates are impossible)
theorem no_homogeneous_cover (S : Finset ℕ) (hS : ∀ p ∈ S, p.Prime ∧ p ≠ 2 ∧ p ≠ 3) :
    ∃ k l : ℕ, 1 ≤ k ∧ 1 ≤ l ∧ ∀ p ∈ S, ¬ p ∣ 2 ^ k * 3 ^ l - 1
-- (proof sketch: M := ∏ (p-1), k := M+1, l := M, Fermat's little theorem gives 2^k 3^l ≡ 2 [MOD p], so p ∣ 1)

-- L2 (quadratic character parity, Lemma T2)
theorem legendre_three_eq_pow (p : ℕ) [Fact p.Prime] (hp : 5 ≤ p) (T : ℕ)
    (h : (3 : ZMod p) = 2 ^ T) : legendreSym p 3 = (legendreSym p 2) ^ T

-- L3 (5 and 13 are never in a common-T family)
theorem no_common_T_5_13 : ¬ ∃ T : ℕ, 2 ^ T % 5 = 3 ∧ 2 ^ T % 13 = 3
-- (periods 4 and 12: T % 4 = 3 and T % 12 = 4 contradict)

-- L4 (equal-index lattices sharing a primitive vector coincide, elementary part of L7)
theorem forms_eq_of_common_primitive (e a b a' b' x y : ℤ) (he : 0 < e)
    (hp : Int.gcd (Int.gcd a b) e = 1) (hp' : Int.gcd (Int.gcd a' b') e = 1) (hv : Int.gcd x y = 1)
    (h1 : e ∣ a * x + b * y) (h2 : e ∣ a' * x + b' * y) :
    ∀ k l : ℤ, e ∣ a * k + b * l ↔ e ∣ a' * k + b' * l
```
(L4 is the statement "two primitive forms mod e vanishing on the same primitive vector have the same kernel" — true because both kernels equal Zv + eZ²; to be stated in Aristotle with the hypothesis that the quotient is cyclic of order e.) The size theorem Z, Theorem C and Lemma A depend on the distortion machinery and are not Lean targets.

## 7. Reproduce
```
python3 verdict3/C_align.py            # Lemma A and the 1-D reduction (+controls)
python3 verdict3/C_commonT.py 300,1000,3000,8000   # common discrete log family, exact B&B (20000 takes >600 s)
python3 verdict3/C_sun.py 8e5 34       # pools S_K
python3 verdict3/C_lemmaM.py; python3 verdict3/C_alignmodel.py 800000; python3 verdict3/C_testH.py
python3 verdict3/C_size.py 0.5         # Theorem Z (needs B_E800000.pkl, 479 MB, gitignored)
python3 verdict3/C_tail.py 1.0 1000 x 0.0 1.34 tailonly   # Theorem C' (kappa_L, L1, unused, eps, kappa_Q, mode); ~1-2 min
PYTHONPATH=. python3 verdict3/C_testQ.py ; python3 verdict3/C_testQ_sim.py   # H_Q out-of-sample test + Poisson comparison
```

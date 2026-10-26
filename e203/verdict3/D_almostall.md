# Erdős #203, NO side, "almost all m" (agent D, 2026-10-26)

Labels: **PROVED** (full argument here, or a theorem I opened), **PROVED-mod-X** (complete argument except the named cited input X, which I did not re-prove), **VERIFIED** (computation with a control that can fail), **CONJECTURED**, **OPEN-STEP** (a specific missing step).
#203 stays OPEN. Nothing here decides it. Convention k,ℓ ≥ 1, gcd(m,6)=1, B = box of exponent vectors u=(a,b) in [1,N]², N ≍ log x, A_u = 2^a 3^b.

## 0. Summary (strongest statements)

1. **Density one for primes is not reachable by a second-moment/Chebyshev argument with any known input.** Precise obstruction (§5): Cauchy–Schwarz over m caps at P(R>0) ≥ 1/(κρ), where ρ ≈ 1.0272 is the exact local-factor loss (VERIFIED, §3.3) and κ is the sieve upper-bound constant for pairs (4 classically; 3.3996 for twin primes by Wu, abstract opened). Parity forces κ ≥ 2 for every sieve, so the method cannot exceed ≈ 0.49 even in the best case, and today gives ≈ 0.24–0.29 (and only after one more cited first-moment step, §5).
2. **Maynard's "Dense clusters of primes in subsets" does not fit (§1).** Its hypotheses force k ≤ c·√(log x / log log x) forms, its conclusion is x·exp(−O(k log log x)) integers, while a positive proportion of m needs k ≳ log x forms. PROVED as a statement about Theorem 3.1 as relayed by the page I fetched.
3. **New, and provable with standard sieve theory: an almost-prime version at density 1 − 0.028.** (§3) For z = x^{1/(2s)}, all but (ρ−1+o(1))x ≈ 0.028x of the m ≤ x coprime to 6 have some k,ℓ ≥ 1 with 2^k3^ℓm+1 free of prime factors < z, hence Ω(2^k3^ℓm+1) ≤ 2.2s. PROVED-mod-(fundamental lemma of the dimension-1 and dimension-2 sieve, cited) and mod the numerical value ρ (VERIFIED, rigorous enclosure not done). No primes, no zero-density input. There is no parity problem because only rough numbers are counted.
4. **Density one for the almost-prime statement** reduces to one lattice-equidistribution lemma (Lemma S, §4). Numerically the variance drops from 0.027 to ≈0.002 after stratifying m mod ∏_{5≤p<30}p (VERIFIED). Lemma S is OPEN-STEP, not proved here.
5. Pair correlations for primes on average over smooth moduli (§6): the objects are binary equations a'p − b'q = c with only (log x)⁴ coefficient pairs. No Bombieri–Vinogradov/Fouvry–Iwaniec/Drappeau-type average has enough moduli to act on, and even level 1 does not beat parity. The exact missing statement is an averaged two-point Chowla for dilates (§6).
6. Other statistics (§7): ± forms, larger families, log-density: none improve the Chebyshev ceiling.

Files: `D_cbox.py`, `D_rho.py`, `D_roughcheck.py`, `D_strat.py` (all in `e203/verdict3/`).

## 1. Maynard's theorem against our hypotheses (item 1)

Source opened: arXiv 1405.2593, "Dense clusters of primes in subsets" (Compositio 2016). I fetched the page twice; the tool returns a summary and the displays were in LaTeX, so conditions marked (relayed) were not seen as typeset formulas.

**Theorem 3.1 (relayed).** Let α>0, 0<θ<1. A a set of integers, P a set of primes, L = {L_i = a_i n + b_i} an admissible set of k forms with 1 ≤ a_i, b_i ≤ x^α, k ≤ (log x)^α, 1 ≤ B ≤ x^α. There is C = C(α,θ): if k ≥ C and Hypothesis 1 holds, and δ > 1/log k is a density parameter, then the number of n ∈ A(x) with at least C^{-1}δ log k of the L_i(n) in P is ≫ #A(x) / ((log x)^k exp(Ck)).
Hypothesis 1 (relayed): (1) A well distributed in progressions to modulus x^θ with total error ≤ #A(x)/(log x)^{100k²}; (2) the same for primes in L(A)∩P over most q ≤ x^θ, (q,B)=1; (3) A not concentrated in any progression.

**Fit check for A = (x/2,x]∩{(m,6)=1}, L_u(m) = A_u m + 1, u ∈ B.**
- Admissibility: for p ≥ 5 with small e_p (p=5, 7, 11, 13, 17 have H_p = F_p^×) the forms A_u m+1 kill every residue class of m mod p, so the full family is not admissible; one must restrict m to a class mod these primes, as in §3-4. A technical point, not the obstruction.
- Coefficients ≤ x^α: yes with α ≥ 1 allowed (A_u ≤ x^c).
- **k ≤ (log x)^α: allowed for α = 2, so k = |B| ≍ (log x)² is formally within the stated range.** The binding condition is (1): for integers m ≤ x the progression errors are O(1) each, so Σ_{q ≤ x^θ} ≤ x^θ, and (1) needs x^θ ≤ x (log x)^{-100k²}, i.e. k² ≤ θ log x / (100 log log x) (relayed formula). So k ≲ 0.1·√(θ log x / log log x). [PROVED as a consequence of the relayed hypothesis; if the exponent in the relayed formula were misread by me the range changes but not the next point.]
- **Conclusion count.** With k ≤ √log x the number of m produced is ≫ x·exp(−k log log x − Ck) = x^{1−o(1)}, not ≫ x. Worse, with k forms the expected number of m ≤ x having *any* prime among the k forms is ≍ k x / log x. A positive proportion of m therefore needs k ≳ log x. Gap between what the hypothesis allows (k ≲ √log x) and what is needed (k ≳ log x): a square. **VERDICT: Maynard cannot give even a positive proportion, let alone density one.** Its mechanism (sieve weights supported on m where all k forms are simultaneously rough, a set of density (log x)^{-k}) finds rare m with many primes, the opposite of the "almost all m, at least one prime" direction.

**Selberg/GPY weights in a second moment (item 1, first part).** The weighted statement one can prove is Σ_m w(m)(R(m) − t) > 0 with w(m) = (Σ_{d_u | A_u m+1} λ_{d})² ≥ 0. This gives an m with w(m) > 0 and R(m) > t, never a bound on the counting measure of {R = 0}, because w is concentrated on a set of m of relative density (log z)^{-k}. To convert to counting measure one needs w(m) ≥ c > 0 on almost all m, which a sieve weight is built not to satisfy. [CONJECTURED/no theorem; reasoning only.] The weights do not remove the constant κ either: the weighted second moment Σ w(m) R(m)² needs the same pair sums, so parity enters the same way.

## 2. Why the plain Chebyshev argument stalls (recap, with the exact local loss)

R(m) = #{u ∈ B : A_u m + 1 prime}. Cauchy–Schwarz: #{R>0} ≥ (ΣR)²/ΣR². Even with perfect (Hardy–Littlewood) pair asymptotics ΣR² = ΣR + ρ(ΣR)²(1+o(1)), where
ρ = lim E_m[c(m)²]/E_m[c(m)]², c(m) = (1/|B|)·Σ_u ∏_{p≥5}[p ∤ A_u m+1](1−1/p)^{-1} (local factor, mean 1).
EO79's route has κ·ρ with κ = sieve constant. Both factors are quantified below.

## 3. Rough numbers: second moment with a genuine asymptotic

### 3.1 Setup
z = x^{1/(2s)}, D = x^{1/2} = z^s. R_z(m) = #{u ∈ B : A_u m + 1 has no prime factor < z}. Box: N = ⌊0.1/ln 6 · log x⌋ so A_u ≤ x^{0.1}, |B| = N² ≍ (log x)². If R_z(m) > 0 then some n = A_u m+1 ≤ x^{1.1} has all prime factors ≥ z, so Ω(n) ≤ log n/log z ≤ 2.2 s.

### 3.2 Moments [PROVED-mod fundamental lemma]
Let I = (x/2,x], and split m into the classes 1,5 mod 6 (m = 6t+c).
- **First moment.** For fixed u the sequence {A_u m + 1} has, for squarefree d | P(z) (primes 5 ≤ p < z), exactly one forbidden class of m mod p, so |A_d| = X/d + r_d with |r_d| ≤ 1. Dimension-1 fundamental lemma (Friedlander–Iwaniec, Opera de Cribro, Cor. 6.10; Halberstam–Richert Thm 2.5; *recalled, not opened*): #{m} = X·∏_{5≤p<z}(1−1/p)·(1+O(e^{-s})) + O(D). Hence E[R_z] = (1+O(e^{-s}))·|B|·∏_{5≤p<z}(1−1/p) ≍ |B|·s/log x ≍ s·log x → ∞ (using ∏_{p<z}(1−1/p) ≍ 1/log z = 2s/log x).
- **Second moment.** For u ≠ u', the pair {A_u m+1, A_{u'} m+1} is a dimension-2 sieve problem: ρ(p) = 1 if p | A_{u'} − A_u, else 2, ρ(p) ≤ 2 < p for p ≥ 5, r_d ≤ 2^{ω(d)}. Dimension-2 fundamental lemma (same references): #{m} = X ∏_{5≤p<z}(1−ρ(p)/p)(1+O(e^{-s})) + O(D (log D)²) (valid for s ≥ 19, i.e. 9κ+1). Summing over (log x)⁴ pairs, total remainder ≪ (log x)⁴ x^{1/2} (log x)² = o(x/log⁴x).
- **No parity obstruction** because the event is "no prime factor < z", not "prime".

### 3.3 The constant ρ [VERIFIED numerically]
Ratio of pair main term to (first moment)²:
ρ_x = (1/|B|²) Σ_{u≠u'} ∏_{5≤p<z} (1−ρ(p)/p)/(1−1/p)², with ρ(p) = 1 iff 2^i3^j ≡ 1 mod p for (i,j) = u'−u.
Three independent computations:
- `D_rho.py` (weighted pair mean over the box, exact lattice condition, no independence assumption): ρ = 1.02629 (N=40, p<2·10⁴), 1.02721 (N=80, p<2·10⁴), 1.02721 (N=80, p<2·10⁵). Tail from p>2·10⁴ moves it by 10⁻⁶.
- `D_cbox.py`: direct box average of the exact survivor density over 1500 random m ∈ [10⁹,10¹²] with p ≤ 1000 (N=200) and p ≤ 300 (N=400): E[c²]/E[c]² = 1.0272, 1.0259; mean c = 0.996, 0.993 (should be 1: the first moment has local factor 1).
- `B_cvar.py` (agent B, independence model): 1.0268.
- Consistency: ρ = (∏_{p≥5}(1−1/(p−1)²)) · (mean F) = 0.8803 × 1.1680 = 1.0282, with mean F from `B_lemmaR.py` (1.168).
**Control that can fail** (`D_roughcheck.py`): for fixed z, R_z is periodic in m, so E[R_z²] and Var/E² are predicted exactly by the formula above. Observed vs predicted (N=30, 40000 random m): z=60: Var/E² 0.02699 vs 0.02654, E[R] 361.33 vs 361.21; z=200: 0.02819 vs 0.02780, E[R] 280.61 vs 280.52. (A first run had a bug, m ≡ 0 mod p treated as killing every cell, and gave Var/E² = 1.52; this was caught by the same control.)

### 3.4 Theorem A [PROVED-mod (fundamental lemma) and (value of ρ)]
For every ε > 0 and s ≥ s_0(ε) (the fundamental-lemma error e^{-s} ≤ ε/10), for x ≥ x_0(ε,s):
#{m ∈ (x/2,x], (m,6)=1 : min_{k,ℓ ≥ 1} Ω(2^k3^ℓ m + 1) > 2.2 s} ≤ (ρ_∞ − 1 + ε)·x, ρ_∞ ≈ 1.0272.
*Proof.* Chebyshev: P(R_z = 0) ≤ Var(R_z)/E[R_z]² = [E R_z² − (E R_z)²]/(E R_z)². Insert §3.2: = (1+O(e^{-s}))(ρ_x + 1/E[R_z]) − 1 + O(e^{-s}) ≤ ρ_x − 1 + O(e^{-s}) + o(1). ∎
Remarks. (a) Taking s = s(x) → ∞ slowly gives "all but (ρ−1+o(1))x of m have min Ω ≤ g(x) for any g → ∞". (b) The rigorous content of the constant: ρ_x is a finite lattice sum whose limit exists numerically; a rigorous upper bound ρ̄ needs interval arithmetic for p up to ~10⁵ plus a tail bound for p > Z (first-order tail Σ_{p>Z} 1/(p e_p) + 4N log N/N² is fine; higher-order terms need Lemma D with weights 3^{ω}); I did not do this. Without it the argument still gives a *positive* proportion (Lemma D bounds ρ_x ≤ C), which is weaker than what EO already know for primes. (c) s ≥ 19 is needed for the standard dimension-2 fundamental lemma, so the explicit Ω bound from this route is about 40–55; a Rosser–Iwaniec lower-bound sieve would reduce this at a cost in constants (not computed).
**Status vs the literature.** I found no paper stating this. It is elementary compared with EO79 and weaker in the arithmetic conclusion (Ω ≤ r_0 instead of prime), stronger in density (97.2% instead of an unspecified small c). I do not claim novelty beyond "not found in the sources I opened".

## 4. Density one for the almost-prime statement: Lemma S

Stratify m by r mod W, W = ∏_{5≤p<w}p. Given r, cells u surviving all p < w form S_r ⊂ B, |S_r| = N_r. Fundamental lemma applies to the primes in [w, z); the first moment is μ_r = N_r ∏_{w≤p<z}(1−1/p), the pair term is Σ_{u≠u' ∈ S_r} ∏_{w≤p<z}(1−ρ(p)/p). Then
Var_r/μ_r² ≤ O(e^{-s}) + 1/μ_r + [ (1/N_r²) Σ_{(u,u')∈S_r², u≠u'} F_w(u,u') − 1 ], F_w = ∏_{p>w, p | n(u'−u)} (1+1/(p−2)) (using ∏_{p∤Δ}(1−1/(p−1)²) ≤ 1).
- **Numerical evidence** (`D_strat.py`, N=30, w=30, z=200, 3000 m per class, 4 random classes): Var/E² = 0.0025, 0.0018, 0.0024, 0.0024, against 0.028 unstratified. VERIFIED (that is: the heuristic is right; sampling noise of order 10⁻³).
- **Lemma S (OPEN-STEP).** For every η > 0 there is w such that, uniformly in r mod W and for N ≥ N_0(w), (1/N_r²)Σ_{S_r²}(F_w − 1) ≤ η.
- *What is easy:* over all pairs, Σ_{(i,j)}(F_w − 1) = o_w(1)·N² at first order, since Σ_{p>w} 4N²/(p e_p) → 0 (Lemma R) and the boundary term 4N Σ_{w<p≤6^N}1/p ≍ N log N.
- *What is not:* S_r has density ≍ 1/log w in B, so the trivial reduction N_r ≳ |B|/log w costs a factor (log w)² against the o_w(1)N² bound. One needs equidistribution of S_r (a set periodic under the lattice Λ_P = ∩_{p<w}Λ_p, index I(w)) over cosets of Λ_d for d with all prime factors > w. When Λ_d and Λ_P have coprime indices this is a CRT statement; when gcd(e(d), I(w)) > 1 the loss is up to a factor depending on the overlap, and Σ over those d must still be o(1). I did not prove this; a natural attack: split d by gcd(e(d), I(w)) and bound the dependent part via Lemma R with the extra weight gcd.
- If Lemma S holds: Theorem A upgrades to **density one**: for every g(x) → ∞, almost all m have min_{k,ℓ≥1} Ω(2^k3^ℓm+1) ≤ g(x).
Also needed: N_r ≥ c(w)·|B|/log w uniformly in r (no covering by primes < w for any class). [CORRECTED 2026-10-26: the 0.2694 uniform density is withdrawn (V_check.md); for fixed w only N_r ≥ c(w)|B| with uncontrolled c(w) follows.] For fixed w this follows from the repo bound (uncovered density ≥ 0.2694 using pool primes with e_p ≤ 4·10⁵, Theorem E / DISTORTION.md, quoted not re-proved; primes < w with e_p > 4·10⁵ remove at most Σ_{p<w}1/e_p more). The needed uniform statement "N_r ≥ c|B|/log w" is stronger (positive *normalised* local factor, min over r), CONJECTURED for all w, VERIFIED only in sampled classes (min c(m) ≈ 0.73 in 1500 samples).

## 5. Primes: the Chebyshev ceiling and one conditional explicit constant

**Statement C [PROVED-mod (i) first-moment asymptotic FM, (ii) pair sieve with uniform constant κ, (iii) value of ρ].** If FM holds then #{m ≤ x, (m,6)=1 : some 2^k3^ℓm+1 (k,ℓ≥1) prime} ≥ (1/(κρ) − o(1))·(x/3), i.e. lower density ≥ 0.243 with κ = 4 (Selberg/Halberstam–Richert, Thm 3.11 as I recall it, *not reopened*) and ≥ 0.286 if Wu's constant κ = 3.3996 holds for shifts h = A_{u'} − A_u with the dilation structure (Wu's theorem proves it for twin primes only; abstract of arXiv 0705.1652 opened).
- **(FM)** ψ(y;q,a) = (y/φ(q))(1+o(1)) for q ∈ {A_u, 2A_u, 3A_u, 6A_u}, y ≍ xA_u, A_u ≤ x^{1/L}, L = L(x) → ∞ slowly. My derivation: Linnik–Gallagher log-free zero density N_q(σ,T) ≪ (qT)^{C(1−σ)} (statement opened in Zaman's BIRS notes, which also state that handling Landau–Siegel zeros is the delicate point) + Lemma A of `B_noside.md` (no exceptional zero for 3-smooth moduli: the only primitive real characters have conductor in {3,4,8,12,24}) + de la Vallée Poussin, gives zero contribution O(e^{-cL}) relative to the main term from zeros of height ≪ q^{O(1)}; large heights need a smoothed explicit formula. **I did not find a published statement of this asymptotic** (Zaman's notes give Linnik only as a lower bound; arXiv 2311.12470 contains no such theorem). Status: CONJECTURED-standard. This is the single cited step EO79 Lemma 1 already uses in lower-bound form; promoting it to an asymptotic is what an explicit constant costs.
- **Ceiling.** Selberg's parity example shows no sieve gives κ < 2 for pair problems [recalled, not opened]. Hence P(R>0) ≥ 1/(κρ) can never exceed ≈ 1/(2·1.027) = 0.487 by this method. Under Elliott–Halberstam the dimension-2 constant improves only toward the parity limit, never to 1.
- Density one for primes by second moments needs κ = 1, i.e. an asymptotic for the pair count, equivalently a parity-breaking input (§6).

## 6. Averaged pair correlations for primes (item 2)

The pair count is N(u,u') = #{m : A_u m+1 = p, A_{u'} m+1 = q both prime}. With a = A_{u'}/g, b = A_u/g (g = gcd) it is the number of prime pairs on the line a(p−1) = b(q−1)... i.e. a p − b q = a − b with a, b 3-smooth, p ≤ xA_u. Only (log x)⁴ pairs (u,u') occur.
1. **No averaging range.** Known unconditional averages for binary prime problems (Bombieri–Davenport/Mikawa-type results for Σ_{h≤H}|Σ Λ(n)Λ(n+h) − S(h)x|, Balog, Perelli, dispersion of Linnik/Bombieri–Friedlander–Iwaniec for Titchmarsh divisor problems) average over a parameter running through a *power* of x. Here the free parameter set has size (log x)⁴. *(Recalled, none of these papers opened; I only confirmed through the search listing that Drappeau's work concerns smooth numbers/moduli in the Fouvry–Iwaniec setting, not our shifts.)*
2. **3-smooth moduli are well factorable but sparse.** Well-factorability (q = q_1q_2 with q_1 of any prescribed size up to a factor 3) is what BFI/Zhang/Polymath use for levels beyond 1/2, but those theorems average over ≍ Q moduli to exploit Kloosterman-sum cancellation. With O((log Q)²) moduli the large sieve gives nothing beyond a single modulus, and for a single modulus unconditional control stops at q ≤ x^{1/L} (Linnik-type, §5) while GRH gives q ≤ x^{1/2−ε}. So level of distribution > 1/2 for the family {2^a3^b} is **not** available, and it would not matter: the first moment lives at level ≈ 0 (a single modulus A_u ≤ x^{1/L} with a = 1), and the second moment is limited by parity, not by level.
3. **Exact missing statement.** Replace Λ by the Liouville function: Σ_{u≠u'} Σ_{m ≤ x} λ(A_u m+1) λ(A_{u'} m+1) = o(|B|² x / ... ) uniformly for A_u, A_{u'} ≤ x^{ε}, i.e. an averaged two-point Chowla for dilates λ(n)λ(an − (a−1)), a = 2^i3^j, over (i,j) in a box of size (log x)². Known results I can name (recalled, not opened): Tao's logarithmic two-point Chowla for *fixed* linear forms, Matomäki–Radziwiłł–Tao's averaged Chowla over additive shifts h ≤ H. Neither covers dilates over a thin multiplicative family or ordinary (non-logarithmic) averages with growing coefficients. This is the precise obstruction; Bombieri's asymptotic sieve would turn it into κ = 1.
4. **Nothing beyond 1/2 for the moduli or beyond parity for pairs** is therefore proved here. [CONJECTURED as to the Chowla-type reduction; the parity statement is the standard barrier.]

## 7. Other statistics (item 3)

- **± forms** (A_u m ± 1): the family doubles, first and second moment both scale, κρ' is unchanged (pairs among (+,+), (−,−), (+,−) are all upper-bounded by κ·HL). No gain in the Chebyshev constant; the covering side is also different (two signs give the Riesel–Sierpiński mixed question, not studied).
- **More primes** (2^a3^b5^c m+1): more cells, E R grows, but the ceiling 1/(κρ) is unchanged. Rough-number statistic improves nothing either; Theorem A already has E R → ∞.
- **Log-density / weighted density:** positive lower density already implies positive log-density; density one for primes would need the same Var = o(E²), no easier.
- **P_2 instead of prime** (CONJECTURED, not worked out): the sequence {A_u m+1 : m ≤ x} has level of distribution D = x^{1−o(1)} relative to its size N = A_u x when A_u ≤ x^{o(1)}, so the linear sieve (Jurkat–Richert) gives a positive-proportion lower bound for P_2 for each u, but lower-bound constants f(s) are not asymptotics, so this gives only a small positive density combined with the dimension-2 upper bound. Not stronger than EO.
- **The one statistic that does reach 97.2% now:** "some cell has Ω ≤ r_0", Theorem A.

## 8. What to do next (ranked)

1. **Lemma S** (§4): turn 97.2% into density one for P_{g(x)}. Pure lattice combinatorics + Lemma R; I judge it provable. Proof plan: partition d by e(d) vs I(w); for d with gcd(e(d), I(w)) = 1 use CRT on the quotient; for the rest use Lemma R with a gcd weight and the convergence of Σ_{p>w} 1/(p e_p).
2. **Rigorous ρ̄** with interval arithmetic: gives an unconditional-modulo-fundamental-lemma explicit theorem "≥ 97% of m coprime to 6 have min Ω ≤ r_0".
3. **FM** (first-moment asymptotic with 3-smooth moduli): locate or prove the asymptotic version of EO79 Lemma 1; that single step converts §5 into an explicit constant ≈ 0.24 for primes, strictly more informative than "c > 0".
4. Do not spend time on Maynard/GPY weights or on Bombieri–Vinogradov-type averages for this family (§1, §6); the obstruction is not the level of distribution.

## 9. Sources actually opened

- Maynard, arXiv 1405.2593 (fetch; Theorem 3.1 and Hypothesis 1 relayed by the tool, LaTeX displays not seen).
- Wu, arXiv 0705.1652 (abstract/Theorem 3: π_2(x) ≤ 3.3996 Π(x); previous records 3.418 and 3.406 per the same page).
- Zaman, "An introduction to log-free zero density estimates" (BIRS notes): N_q(σ,T) ≪ (qT)^{C(1−σ)}, Linnik's theorem as lower bound, Landau–Siegel zeros left aside.
- Search listings only (content not read): Drappeau arXiv 1307.7554 and 2304.11696, arXiv 2311.12470 (fetched, no relevant theorem).
- Recalled, not opened: Halberstam–Richert Thms 2.5, 3.11; Friedlander–Iwaniec fundamental lemma; Selberg's parity example; Tao and Matomäki–Radziwiłł–Tao on Chowla.

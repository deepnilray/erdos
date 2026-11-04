# Erdős #203, run5 Phase B, agent 5 (NO side, analytic): Theorem A on an opened fundamental lemma

Written 2026-11-04 (final). Labels: PROVED / VERIFIED (with bound and control) / CONJECTURED. **#203 stays OPEN; nothing here decides it.**
Scripts and logs: `verdict2/a5/`. Regenerated data (gitignored): `verdict3/D_data/`.

## 0. Verdict

**VIABLE (for Theorem A): Theorem A is now PROVED. Every dependency has been read: the sieve input is Ford's lecture notes, Thms 2.3 and 3.2 (the same content as Ford–Halberstam 2000), opened on the primary page. Every constant has a rigorous enclosure.** The new error terms also lower r₀ a great deal.

New best statements. Each holds for x ≥ x₀, among the m ≤ x coprime to 6, with a cell k, ℓ ≥ 1 and 2^k3^ℓ ≤ x^{0.001}:

| Ω(2^k3^ℓm+1) ≤ | exceptional share, PROVED (no FFT; two exact moments) | exceptional share, VERIFIED (full FFT class distribution) | unstratified, PROVED | old (D §11.6, cited FI) |
|---|---|---|---|---|
| 10 | 10.2% | 10.14% | 12.1% | — |
| 12 | 3.9% | 3.84% | 5.94% | — |
| 13 | 2.64% | 2.60% | 4.73% | — |
| **14** | **1.04%** | 0.995% | 3.16% | — |
| 16 | 0.76% | 0.719% | **2.89%** | — |
| 18 | 0.64% | 0.598% | 2.77% | — |
| **19** | **0.63%** | 0.593% | 2.77% | — |
| 22 | 0.624% | 0.587% | 2.76% | 2.0% (strat.) |
| 26 | 0.623% | 0.586% | 2.76% | 0.6% (strat.) |
| r₀ → ∞ | **0.623%** | 0.586% | 2.755% | 0.57% / 2.74% |

(These are the upper enclosures, rounded up. Logs: `a5_delta_moments.log` (column 2), `a5_delta.log` (columns 3, 4).)
- **Covering corollary [PROVED]:** for every y, the m coprime to 6 whose exponent lattice is covered by the primes in [5, y) have density ≤ 0.623%, uniformly in y. The density is exactly 0 for y ≤ 31, since every class keeps at least 15.5% of its cells (union bound, PROVED); the exact minimum is 37.4% (VERIFIED, FFT).
- **ρ enclosure [PROVED]:** 1.027521 ≤ ρ = C₅W₅ ≤ 1.028321. D had [1.02751, 1.02820], computed with floats and with Rosser–Schoenfeld unopened.
- The large-r₀ limits are slightly *weaker* than D's 0.57% / 2.74%. This is deliberate: I replaced D's Rosser–Schoenfeld tail (a source I could not open) with an elementary in-house bound, so τ₃₁ goes from 3.20·10⁻⁴ to 3.81·10⁻⁴.

**Remaining assumptions, all explicit:**
- (a) Mertens' product theorem ∏_{p≤x}(1−1/p) ∼ e^{−γ}/log x. Classical; used as stated in Ford's notes, p. 5; not re-proved.
- (b) Lemma U (V_check §10.1). It is an in-house proof, which I re-checked line by line (§3). It is not formalised.
- (c) Correctness of the software: IEEE integer arithmetic in numpy (only exact integer operations are used in the bounds), mpmath interval arithmetic, and the C prime code. The C code was cross-checked by my own independent C code.
- The FFT column additionally relies on numpy's FFT rounding to the right integers. Every value is within 10⁻³ of an integer, and two exact-moment checks pass. That is why the column is labelled VERIFIED, not PROVED.

## RISKS (worst first)
1. **Lemma U is the deepest in-house step**: the box and class versions of the limsup pair average. It is V's proof, which I re-checked (§3). A gap there would affect every number above, though not the method. Suggest an Aristotle/Lean pass on the lattice-count part (b)–(d).
2. **Lemma 2.1 (the o(1) step) is my own proof.** It uses only Mertens and monotonicity of E. Someone should cross-read it, because it is exactly the step L3 flagged.
3. Greedy partitions are not optimal. This only makes the numbers weaker, never wrong: any configuration with cost < s is a valid sieve.
4. "x ≥ x₀" is ineffective. Mertens with o(1), and y₀ = exp(√log z) in Lemma 2.1, give no explicit x₀. An explicit x₀ would need explicit Mertens bounds, i.e. Rosser–Schoenfeld, which I could not open.
5. Prior art: D's limited search found no almost-prime statement of this kind for almost all m (D §10.4). I did not search again. No priority claim.

---------------------------------------------------------------------------------------------------------------------
## 1. The sieve statement used (read on the primary page)

**Source.** K. Ford, *Sieve methods lecture notes, Spring 2023*, PDF dated 10 Mar 2026 (pdfinfo CreationDate), ford126.web.illinois.edu/sieve2023.pdf. Local copy: `scratchpad/L3dl/fordnotes/s.pdf`, 129 pp.

**Setting (pp. 4–5).** A sieve problem is a finite (multi)set A, with A_d = #{a ∈ A : d | a}.
- (g): 0 ≤ g(p) < 1, with g multiplicative on squarefree d.
- (r): r_d := A_d − X g(d).
- (V): V(z) = ∏_{p≤z}(1 − g(p)).
- S(A,z) = #{a : (a, ∏_{p≤z} p) = 1}.

**Theorem 2.3 (p. 17), verbatim up to typesetting.** "Let A be a sieve problem and assume (g), (r) and (V). Partition the set of primes in [1, z] into P₁ ∪ ⋯ ∪ P_t, let P_i = ∏_{p∈P_i} p and let k₁, …, k_t be non-negative even integers. Then S(A, z) ≤ X V(z) e^E + R′, where E is given by (2.6) and R′ := Σ_{d∈P(z), ω((d,P_j)) ≤ k_j (1≤j≤t)} |r_d|."
- (2.4): V_j = ∏_{p∈P_j}(1 − g(p)), L_j = log(1/V_j).
- (2.6): E := Σ_{j=1}^t e^{L_j·1_{k_j>0}} L_j^{k_j+1}/(k_j+1)!.

**Theorem 3.2 (p. 31), verbatim up to typesetting.** "Let A be a sieve problem and assume (g), (r) and (V). Partition the set of primes in [2, z] as in (2.9) and let k₁, …, k_t be nonnegative even integers. Then S(A, z) ≥ X V(z)(1 − E) − R″, where E is given by (2.6) and R″ = Σ_{d∈P(z), d ≤ z₁^{k₁+1} z₂^{k₂} ⋯ z_t^{k_t}} |r_d|."
- (2.9) (p. 18): z_{t+1} = 2 < z_t < ⋯ < z₁ = z, with P_j = (z_{j+1}, z_j] for j < t and P_t = [2, z_t].

**Proofs read (pp. 13, 16–17, 30–31).** The ingredients are:
- Lemma 2.2: a product of Brun truncations is an upper-bound sieve.
- Lemma 1.6: Bonferroni, plus Σ_{ω(d)=k+1} g(d) ≤ (Σ g(p))^{k+1}/(k+1)!.
- g(p) ≤ −log(1 − g(p)).
- Lemma 3.1: x₁⋯x_t ≥ y₁⋯y_t − Σ_ℓ (y_ℓ − x_ℓ)∏_{j≠ℓ} y_j.

All steps are elementary, and I checked each line.

**Same content elsewhere.** Ford–Halberstam, "The Brun–Hooley sieve", J. Number Theory 81 (2000) 335–350; authors' PDF at `scratchpad/L3dl/fh/p.pdf`. The Theorem is on PDF p. 7 and holds for any finite prime set P and any partition. There e^{L_j} is kept also when k_j = 0, and a sharper E′ is given.

**Remarks used below.**
- (i) E is increasing in every L_j ≥ 0.
- (ii) In Thm 2.3, every d in R′ satisfies d ≤ ∏ z_j^{k_j} when P_j ⊂ [1, z_j].
- (iii) Suppose g(p) = 0 for p < w and A_d = 0 whenever d has a prime factor < w. Then r_d = 0 for those d, so both theorems sieve exactly by the primes in [w, z].

### 1.1 Hypothesis check against Theorem A's use [PROVED]

**Setup.** Fix w ∈ {5, 31}, W = ∏_{5≤p<w} p (W = 1 for w = 5), and M = 6W. Take a class r mod M with (r, 6) = 1, and put S_r = {u ∈ [1,N]² : (A_u r + 1, W) = 1}, where A_u = 2^a3^b. For x/2 < m ≤ x write m = r + Mt; then t runs over an interval I with #I = X + θ, X = x/(2M), |θ| ≤ 1.

**One form (first moment).** Take A = {a_u(t) = A_u(r+Mt) + 1}, u ∈ S_r.
- Each a_u(t) is odd, ≡ 1 mod 3, and prime to every p < w. So A_d = 0 for d with a prime factor < w, and g(p) = 0 there (remark iii).
- For w ≤ p ≤ z we have p ∤ A_u M, so exactly one class of t mod p is killed. With g(p) = 1/p this gives |r_d| ≤ 2.

**Pair (second moment), u ≠ u′ ∈ S_r.** Take the sequence a_u a_{u′}.
- The two killed classes coincide iff A_u ≡ A_{u′} (mod p), i.e. iff 2^i3^j ≡ 1 (mod p) with (i,j) = u′ − u.
- So ρ(p) ∈ {1,2}, g(p) = ρ(p)/p ≤ 2/p < 1, and |r_d| ≤ 2ρ(d) ≤ 2·2^{ω(d)}.
- L_j^{(uu′)} ≤ L̄_j := Σ_{p∈P_j} −log(1−2/p). By remark (i), a single E bound therefore serves all ≤ N⁴ pairs.
- (a_u a_{u′}, p) = 1 for all w ≤ p ≤ z exactly when both cells are z-rough, which is the count D needs.

**Level.**
- With z_j = z^{t_j}, the moduli satisfy d ≤ z^{Σ k_j t_j} for Thm 2.3, and d ≤ z^{1 + Σ k_j t_j} for Thm 3.2 (t₁ = 1).
- Both exponents are required to be < s, and z = x^{(1−ε)/s}. So every d ≤ D := x^{1−ε}.
- Σ_{d≤D} 2^{ω(d)} ≤ D ∏_{p≤D}(1+1/p)² ≤ D(1+log D)². Over ≤ N⁴ pairs this is ≪ x^{1−ε}(log x)⁶, which is o(main terms ≍ x(log x)²).

**What is no longer needed:** the Ω(κ) condition, the constant K, s ≥ 9κ+1, and *Opera de Cribro* altogether.

## 2. The o(1) step: deep blocks as z → ∞ (L3's risk 1) [PROVED]

**Input: Mertens' product theorem** (Ford notes p. 5). It gives, for κ ∈ {1,2},
 (M) η_κ(a) := sup_{b>a} |Σ_{a<p≤b} −log(1−κ/p) − κ log(log b/log a)| → 0 as a → ∞.
- For κ = 1 this is the ratio of the Mertens products at b and a.
- For κ = 2, write −log(1−2/p) = −2log(1−1/p) − log(1−1/(p−1)²). The last sum over p > a is ≤ Σ_{n>a} 2/(n−1)² → 0.

**Limit configuration.** Take K > 1, t_j = K^{1−j}, and even k_j ≥ 0 (j ≥ 1) with:
- (a) cost c := Σ_j k_j t_j < s (upper sieve), or c := 1 + Σ_j k_j t_j < s (lower sieve);
- (b) E^∞(λ) := Σ_j e^{λ1_{k_j>0}} λ^{k_j+1}/(k_j+1)! < ∞ for every λ > 0. This holds because the configurations used have k_j = 2j for j > 200.

Here λ = κ log K and σ := s − c > 0.

**Lemma 2.1.** For every η′ > 0 there is z₀ such that, for z ≥ z₀, there is a partition of the primes in [2, z] with even k's satisfying both:
- E(z) ≤ E^∞(κ log K) + η′, uniformly over all pair problems with g(p) ≤ κ/p;
- every remainder modulus d ≤ z^{c+σ/2}.

*Proof.* Put y₀ = exp(√log z) and ℓ = log log z, and let J be the largest j with z^{t_{j+1}} ≥ y₀.

Blocks:
- P_j = (z^{t_{j+1}}, z^{t_j}] for 1 ≤ j ≤ J, with the configured k_j;
- a bottom block P_{J+1} = [2, z^{t_{J+1}}] with k = 2⌈ℓ²⌉. Its primes below w have g = 0.

Explicit blocks:
- Every lower endpoint is ≥ y₀ → ∞, so L_j ≤ κ log K + η_κ(y₀) uniformly.
- Since E is increasing in each L_j, their total is ≤ E^∞(κ log K + η_κ(y₀)).
- E^∞(λ+1) < ∞, so by dominated convergence E^∞(λ + η) → E^∞(λ) as η → 0.

Bottom block:
- z^{t_{J+1}} < y₀^K, because z^{t_{J+2}} < y₀.
- Hence L ≤ κ log log y₀^K + O(1) = (κ/2)ℓ + O(1) ≤ ℓ for large z.
- With k+1 ≥ ℓ² and n! ≥ (n/e)^n, its term is ≤ e^ℓ(e/ℓ)^{ℓ²} → 0.

Level:
- The explicit blocks cost ≤ c.
- The bottom block contributes d ≤ (y₀^K)^{2⌈ℓ²⌉} = z^{O((log log z)²/√log z)} = z^{o(1)}. ∎

**Remark (correction to L3).** `fh_table.py` truncated the partition at 150 blocks and gave the primes below z^{t_150} no block. That is not a sieve: those primes still divide elements.
- Lemma 2.1 needs k_j → ∞ in the tail.
- `a5_fh.py` adds the tail k_j = 2j for j > 200 and bounds its error, e^λ λ^{n₀}/n₀!/(1 − λ/(n₀+1)) with n₀ = 403, and its cost, 2K Σ_{j>200} j K^{−j}, in closed form.
- The tail changes the numbers by less than 10⁻²⁰.
- L3's upper sieve also used the lower-bound level constraint (k₁+1) + …. The correct Thm 2.3 constraint Σ k_j t_j < s improves η₂ at r₀ = 19 from 5.2·10⁻⁴ (L3) to 7.0·10⁻⁵.

## 3. Theorem A‴ and its proof [PROVED, given §1, §2, Lemma U and the constants of §4]

**Notation.** c = ε = 0.001, N = ⌊c log x/log 6⌋, z = x^{(1−ε)/s}, and R(m) = #{u ∈ [1,N]² : (A_u m+1, ∏_{5≤p≤z} p) = 1}.
- If R(m) > 0, some n = 2^k3^ℓ m + 1 ≤ x^{1+c} + 1 has all prime factors > z. So Ω(n) ≤ s(1+c)/(1−ε) + o(1).
- Choosing s = (r₀+1)(1−ε)/(1+c) − 10⁻⁶ gives Ω(n) ≤ r₀ for large x.

**Per class r.** Cauchy–Schwarz gives #{R>0} ≥ Σ₁²/Σ₂.
- Σ₁ ≥ |S_r|[(1−E₁)XV₁ − D], by Thm 3.2 with κ = 1 and Lemma 2.1.
- Σ₂ ≤ |S_r|(e^{E₁⁺}XV₁ + D) + Σ_{u≠u′}[e^{E₂}XV_{uu′} + 2D(1+log D)²], by Thm 2.3 with κ = 2 and Lemma 2.1.
- Here |S_r| = ν_r N² + O(N), V₁ ≫ 1/log x, and D = x^{1−ε}.

This gives:
- #{R>0}/#I ≥ (1−E₁−o(1))²/(e^{E₂}·ratio_{r,x} + o(1));
- ratio_{r,x} ≤ ∏_{w≤p≤z}(1−1/(p−1)²)·mean_{u≠u′∈S_r} F_{≥w}(u′−u). This uses (1−ρ/p)/(1−1/p)² = (1−1/(p−1)²)(1 + 1[ρ=1]/(p−2)), checked for ρ = 1 and ρ = 2.

**Lemma U** (V_check §10.1). I re-checked each step:
- P(Δ = v) ≤ 1/(N²−1).
- #(Λ_d ∩ box ∖ 0) ≤ 8N²/e(d) + CN/λ₁(d), with λ₁² ≤ (2/√3)e(d).
- λ₁(d) ≥ log d/log 6, since d divides the numerator of 2^a3^b − 1, which is ≤ 6^{|v|}.
- Σ_{d≤X} g(d)/log d ≪ log log X.
- The d with e(d) ≤ T are finitely many and periodic.

Class version (D §11.1, V §10.3; re-derived):
- In the class average, ψ ∈ Ĥ_d survives only if ψ ∈ Ĥ_W, and then E ψ(u) = T̂_r(ψ)/|T_r|.
- Parseval gives Σ_{ψ≠1}|T̂|²/|T|² = 1/ν − 1.

Together: limsup ratio_{r,x} ≤ C_w(W_w + M_w(1/ν_r − 1)).

**Theorem A‴.** For every η′ > 0 and x ≥ x₀(r₀, η′), all but (δ_w(r₀) + η′)·x/3 of the m ≤ x coprime to 6 have k, ℓ ≥ 1, 2^k3^ℓ ≤ x^{0.001} and Ω(2^k3^ℓm+1) ≤ r₀.
- δ_w = E_r[φ(ν_r)], with φ(ν) = min(1, max(0, 1 − (1−E₁^∞)²/(e^{E₂^∞} C_w(W_w + M_w(1/ν−1))))).
- For w = 5: δ₅ = 1 − (1−E₁^∞)²/(e^{E₂^∞}ρ).
- From (x/2, x] to [1, x]: sum over dyadic ranges above x₀. The classes r mod W are uniform among m coprime to 6, by CRT.

## 4. Numbers: regenerated data, rigorous enclosures, independent checks

### 4.1 Regenerated (D's scripts) [VERIFIED reproductions]

| file | how | result |
|---|---|---|
| `D_data/ep_1e8.bin` | `D_eprimes.c`, 31 s | 5 761 453 records (all primes 5..10⁸), sha256 19ad8103… |
| `D_data/nu_w31.npz` | `D_classes.py 31`, 10 s | identical summary to D §11.3: total weight 1.000000000000, E[ν] = 0.4738416693, min ν = 0.37402, no ν = 0; sha256 836d52bf… |
| `D_data/W_w31.log` | `D_W.py 31 1e8`, 10 min | S1 = 0.00906658, A(1) = 1.156260681, max B1 = 3.0953·10⁻³, single part 0.0110916 (all = D) |
| `D_data/comp_w31.log` | `D_comp.py 31 3000 1e8`, 6.5 min | composite 2.8917·10⁻⁴ (= D); with T1 = 3.075·10⁻⁵ this gives D's τ = 3.199·10⁻⁴ |
| `D_data/r0table_rerun.log` | `D_r0table.py` on the regenerated npz | **byte-identical** to `D_r0table.log` (control: the regenerated ν data is D's) |

Note: `D_W.py` alone prints τ = 2.04·10⁻³ (the crude max-key bound). D's 3.2·10⁻⁴ needs `D_comp.py`.

### 4.2 Independent check of D_eprimes.c [VERIFIED, all primes 5 ≤ q ≤ 10⁸]

My code: `a5/a5_eprimes_check.c`.
- It factors with a smallest-prime-factor sieve, not trial division.
- It certifies e_q = |⟨2,3⟩ mod q| directly: 2^e = 3^e = 1, and for each prime r | e, 2^{e/r} and 3^{e/r} are not both 1.
- It checks D's (G, α, β) without any generator: gcd(α, β, G) = 1, and the HNF basis of {iα + jβ ≡ 0 mod G} must lie in the kernel of Z² → H_q/H_q^G.

Results:
- 0 mismatches in e, ord₂, ord₃, G; 0 lattice failures; the record set is exactly the primes 5..10⁸.
- **Planted control:** α → α+1 on every 1000th record with G > 1 (5347 records). 21 of these give the same lattice up to a unit and cannot be detected; exactly 5326 = 5347 − 21 detections fired.

### 4.3 Constants with rigorous enclosures (`a5_consts.py`, `a5_tau_iv.py`, `a5_civ.py`)

Method: integers with directed rounding (⌊10¹⁸/x⌋ or ⌈10¹⁸/x⌉, exact sums), exact rationals, and mpmath.iv. No floating-point value enters a bound.

| constant | value (enclosure) | independent of D? | control |
|---|---|---|---|
| A(1) = Σ_{d\|P(<31)} g(d)/e(d) | 1.15626068069 exact (lattice indices, no enumeration of H_W) | own lattice code | = V's exact 1.1562606807; the planted wrong formula e = lcm(ord₂, ord₃) gives 1.16674 (V's trap): fires |
| S1 = Σ_{31≤q≤10⁸} g/e | [0.009066580154, 0.009066580160] | own e_q | = D 0.00906658 |
| single-prime part of W₅ | [0.0110915507, 0.0110915508] | exact means via lattice indices (877 line classes) | = D 0.0110916 |
| max_{ψ≠1} B1(ψ) | ≤ 3.0953191·10⁻³ | own character parametrisation (X,Y) ∈ (Z/55440)²; each character checked to kill Λ_W | = D 3.095319·10⁻³; Σ_ψ B1 = 0.0546953 = D |
| **τ₃₁** | **≤ 3.81298·10⁻⁴** (D: 3.199·10⁻⁴) | own code, own unknown-prime bound U(y) (count bound plus a 30030-wheel; **no Rosser–Schoenfeld**), explicit tail beyond e = 10³⁰⁰ (≤ 6.4·10⁻¹⁸²; D called it negligible but did not bound it) | parts A, B agree with D to 4 digits (2.2747·10⁻⁴, 1.58·10⁻⁷); control below |
| C₃₁, C₅ | ≤ 0.99251798, and C₅ from the exact product for q < 1000 times exp(−Σ_{q≥1000}) | — | — |
| W₃₁ ≤ 1.00944788, M₃₁ ≤ 3.47662·10⁻³, W₅ ∈ [1.1673522, 1.1682596], **ρ ∈ [1.027521, 1.028321]** | | | ρ contains D's box value 1.02758 (N = 600) |

**Why τ differs from D's 3.2·10⁻⁴ (independent check of τ).**
- The composite part agrees in method and in parts A and B.
- D's unknown-prime mass uses Rosser–Schoenfeld (θ(x) ≥ x(1−1/ln x), θ(x) < 1.01624x, Mertens-sum bounds). I could not open the paper: Project Euclid returned an Incapsula block page.
- So I replaced it with an elementary bound. It costs +6·10⁻⁵, and I adopt the elementary value.
- D's number is plausible. I label it CONJECTURED-correct, because its input was not opened.
- **Control (`a5_tau_control.py`).** On the 22 primes 31 ≤ p ≤ 10⁸ with e_p ≤ 400 and e_p | 55440, the exact Σ_{|T|≥2} g(T)/e(T) = 1.8657·10⁻⁵ (2²² subsets, exact lattice indices). The two-key bound gives 1.0658·10⁻⁴ ≥ exact: PASS.
- Planted control: dropping Π and using e(d) := e₁e₂ gives 1.1676·10⁻⁵ < exact, so it fires. (The weaker plant, dropping Π only, gave 1.0156·10⁻⁴ and did not fire. The bound is loose here, and I report that.)

### 4.4 Class distribution (w = 31)

**[PROVED, no FFT]**
- Support: ν_r ≥ 1 − Σ_{5≤p<31} 1/e_p = 0.155321. A prime p in S kills a fraction exactly 1/e_p of H_W, because H_W → H_p is onto.
- Exact moments:
  - E[ν] = ∏(1−1/p) = 0.4738416693.
  - E[ν²] = Σ_T e(T)^{−1} ∏_{p∈T}(1/p) ∏_{p∉T}(1−2/p) = 0.2302358839 (exact rational).
  - Derivation: two cells survive p with probability 1 − 2/p, or 1 − 1/p if their difference lies in Λ_p.
- `a5_delta_moments.py` finds a quadratic q ≥ φ on [0.1553, 1] by LP, certifies it on adaptive subintervals with mpmath.iv (margin 10⁻⁶), and bounds δ ≤ E q(ν).
- **Control:** shifting q down by 10⁻⁴ makes the certificate fail. It fired.

**[VERIFIED, FFT]** `a5_classes_exact.py` runs D's FFT method with **exact integer weights** (common denominator) and bins of 64 cells; φ is evaluated at the lower bin edge, which is an upper bound since φ is decreasing.
- Controls:
  - total weight = 1 exactly;
  - E[ν] = ∏(1−1/p) exactly;
  - E[ν²] = the independent lattice formula exactly (rational equality).
- **Planted** (one count −1): both moment checks fail. They fired.
- Feeding D's own inputs (FI η's, D's W, M, C) through my bins reproduces D's stratified column at r₀ = 22, 23, 26, 29: 0.01995, 0.01102, 0.00599, 0.00574 (`a5_delta_control.log`).

### 4.5 Brun–Hooley errors (`a5_fh.py`, `a5_fh_all.log`) [PROVED enclosures]

| r₀ | s | E₁ (κ=1, lower) ≤ | η₂ = e^{E₂}−1 (κ=2, upper) ≤ |
|---|---|---|---|
| 10 | 10.978 | 2.30·10⁻³ | 1.01·10⁻¹ |
| 12 | 12.974 | 1.47·10⁻⁴ | 3.35·10⁻² |
| 14 | 14.970 | 6.32·10⁻⁶ | 4.11·10⁻³ |
| 16 | 16.966 | 4.23·10⁻⁷ | 1.34·10⁻³ |
| 19 | 19.960 | 3.27·10⁻⁹ | 7.03·10⁻⁵ |
| 22 | 22.954 | 1.88·10⁻¹¹ | 1.23·10⁻⁵ |
| 26 | 26.946 | 4.2·10⁻¹⁵ | 2.3·10⁻⁷ |

(FI 6.8 with K₂ = 5/3 gives η₂ = 3.0 at s = 22.)

Controls (`a5_fh_control.log`):
- Under L3's constraint my code reproduces L3's `E_of` to 10 digits at K = 1.5, 3, 4 (κ = 1, 2), including L3's η₂ = 5.19·10⁻⁴.
- An mpf re-evaluation lies inside the iv enclosure.
- A planted over-budget configuration (cost 21 > s = 19.96) is rejected.

## 5. Secondary items

### 5.1 Untried method 2: Maynard–Tao weights in m on the exponent box
- **Best density statement it can give:** zero density. It gives ≫_k x/(log x)^k values m ≤ x for which ≥ c log k of a fixed admissible k-subset of the forms A_u m + 1 are prime [CONJECTURED as to the exact order; the standard GPY/Maynard computation was not redone here].
- **Exact failure point:** converting weights to counting measure. Any lower bound for #{m : R(m) > 0} from a weight w ≥ 0 passes through Cauchy–Schwarz, #{R>0} ≥ (Σ_m w 1_{R>0})²/Σ_m w². For k-dimensional sieve weights, Σ w and Σ w² are both ≍ x(log x)^{−k} (w² is again a k-dimensional weight). So the certified set has relative density ≍ (log x)^{−k} → 0.
- Admissibility also fails for the full box mod 5, 7, 11, 13, 17 (H_p = F_p^×; D §1). One must restrict to sub-tuples, and that does not change the conclusion.
- Theorem A works because it uses the weight w ≡ 1 with the rough-number indicator, whose pair counts are asymptotic. Maynard–Tao adds nothing to it. For primes, the Chebyshev ceiling of about 0.49 (D §5) is the binding obstruction, not the weights.

### 5.2 L3 rows owned by 5 (`| 5 |`)

| row | used? | exact point |
|---|---|---|
| T1 Ford–Halberstam | **USED** (same content as T2) | §1 |
| T2 Ford notes Thms 2.3, 3.2 | **USED**, read on p. 17 and p. 31 | §1–§2; Thm 3.6 is not explicit and is not used |
| T3 Iwaniec 1980, Rosser sieve | not used | Thm 1 has explicit main terms F_κ, f_κ, but certified values of F₂(s), f₁(s) need the κ = 2 delay-ODE constants β₂, A₂ (§5 of that paper), not computed. It would only matter for r₀ ≤ 12, where Brun–Hooley's η₂ is ≥ 3·10⁻² |
| T4 FI *Opera* Lemma 6.8 | no longer needed | superseded; still S (never opened), and now not cited |
| T5 Iwaniec–Kowalski Lemma 6.3 | no | O-constant "depending only on κ": not explicit |
| T6 Tao 254A Lemma 17 | no | O_κ(e^{−s}): not explicit |
| T7 Heath-Brown lectures | no | κ ≤ 1 only; the pair problem has κ = 2 |
| T8 Thorner–Zaman Thm 6.1 | no | composition of two beta sieves; inherits e^{9κ−s}K^{10}, which is worse than T1 |
| T9 Gorodetsky | no | quotes Ford Thm 3.6 with a non-explicit C_{κ,B} |
| T17 Stadlmann / Mangerel | no | averages over ≍ x^θ squarefree smooth moduli; the moduli 2^a3^b number O((log x)²) and are not squarefree |
| T20 negative searches | — | nothing to use |

## 6. Corrections to earlier files
1. HUB N3/N4 and D §11.6: the dependency on "FI Lemma 6.3" is removed. It was Lemma 6.8 (L3), and it is now not needed.
2. D §11.2: D's "ρ ≤ 1.028192" and "τ₃₁ = 3.2·10⁻⁴" rest on Rosser–Schoenfeld, which was never opened, and on floating sums. They are replaced by the rigorous ρ ≤ 1.028321 and τ₃₁ ≤ 3.813·10⁻⁴. D_W.py's tail beyond 10³⁰⁰ was unbounded; it is now bounded by 6.4·10⁻¹⁸².
3. L3 §(c).2: the truncated partition is not a sieve (§2 remark). The upper-sieve level constraint should be Σk_jt_j < s, without the +1.
4. D §11.4 ("a weighted sieve cannot lower r₀ … only s ≳ 22 delivers errors below 10⁻²"): this is false with Brun–Hooley. η₂ < 10⁻² already at s ≈ 14.97 (r₀ = 14).

## 7. Reproduce
```
gcc -O2 verdict3/D_eprimes.c -o D_eprimes; ./D_eprimes 1000000 verdict3/D_data/ep_1e6.bin; ./D_eprimes 100000000 verdict3/D_data/ep_1e8.bin
cd verdict3 && python3 D_classes.py 31          # nu_w31.npz
gcc -O2 verdict2/a5/a5_eprimes_check.c -o chk; ./chk verdict3/D_data/ep_1e8.bin verdict3/D_data/a5_e_1e8.bin [plant]
cd verdict2/a5 && python3 a5_consts.py && python3 a5_tau_iv.py && python3 a5_classes_exact.py 64 && python3 a5_fh.py   # (+ a5_fh_small.log rows r0=6..9)
python3 a5_delta.py 64 && python3 a5_delta_moments.py; controls: a5_fh_control.py a5_tau_control.py 400 a5_delta_control.py
```
(`a5_tau.py` is the float version of `a5_tau_iv.py`, kept as a cross-check: 3.8026·10⁻⁴ vs 3.8130·10⁻⁴.)

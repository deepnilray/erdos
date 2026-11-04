# Erdős #203, run5 Phase-B agent 4: tools for the unconditional large-e_p tail (2026-11-04)

Labels: **PROVED** (closed argument, here or in a primary source I read), **VERIFIED** (computation with a control that can fail, bound stated), **CONJECTURED**.
Flags on sources: **P** = statement read on a primary page today; **S** = secondary quote; **U** = not seen.
Notation as in `verdict3/C_allE.md`: Λ_p = ker ψ_p ⊂ Z², index e_p = |⟨2,3⟩ mod p|, Z²/Λ_p cyclic; c(e) = #{p : e_p = e}; for a finite P, c_P(e) = #{p ∈ P : e_p = e}, s_P = max_e c_P(e). Scripts: `verdict2/a4/` (run from `e203/`). Downloads (untrusted, not executed): scratchpad `a4dl/`.

STATUS: complete (2026-11-04). Scripts and logs: `verdict2/a4/pencil_ffkpy.py` (+`.log`), `gcd_data.py` (`gcd_data.log`, `gcd_data_20000.log`), `kappa_fit.py` (`kappa_fit.log`). No heavy CPU job was run; the pool job was not touched.

---------------------------------------------------------------------------------------------------------------------
## 0. Verdict

**EMPTY for the target.** No tool on the list bounds the large-index tail unconditionally. Every one breaks at one of three steps, and they are the same three steps every time:
- (B1) it bounds a quantity that is **linear in e** (c(e) ≤ ε·e/log e, or Σ_{e_p=e} log p ≤ e log 2). Then each stage's first moment Σ_{P⁺(e)=ℓ} c(e)G(e)/e is +∞, because each stage holds infinitely many e.
- (B2) it bounds the **wrong multiplicity**: primes per lattice λ(L), or one prime containing two vectors. The tail needs primes per index, c(e), or pairs of *different* primes aligned mod q.
- (B3) it is about **generic primes** (density one, Chebotarev, exponential sums over large subgroups). The tail is made of the *exceptional* primes, those with e_p ≤ (log p)^{O(1)}… p^{o(1)}.

**PARTIAL on by-products** (all PROVED unless stated):
1. **FFKPY transplanted to Z².** Lemmas 2.1, 3.1–3.4 and Theorem 2 of FFKPY (JAMS 2007) hold for coset systems of cyclic-quotient lattices in Z². The moduli become the indices e_p and the multiplicity becomes the index multiplicity c_P(e). The hypothesis is *the same* as in 1-D. The 2-D gain (alignment) **cannot** be put into FFKPY's Lemma 2.1: the 2-D version with β summed only over aligned pairs is **false**. The counterexample is the pencil, ℓ+1 concurrent lines in F_ℓ²: pairwise independent, jointly covering (§1.2, VERIFIED by script).
2. **FFKPY Theorem 5 transfers to Z²**, including in a non-aligned form (pencil × FFKPY). For every large N there are exact coset coverings of Z² by cyclic-quotient lattices with all indices > 2N and index multiplicity ≤ 3·exp(√(log N log log N)). The lattices do **not** share a common primitive vector (§1.3). So in 2-D, as in 1-D, any no-covering theorem that sees only (index, multiplicity) data must assume a multiplicity bound. Whether a direction-aware hypothesis could replace c(e) is **not** settled by this.
3. **KKL Theorem 3 transfers to Z² directly.** No direction lemma is needed, so the saturated case is included. Every covering P of #203 satisfies min_{p∈P} e_p ≤ exp(c·log²(s_P+1)/log log(s_P+2)), with c absolute but unspecified (§6). This is the new YES-side constraint: **a covering that avoids all primes with e_p ≤ x must repeat some index at least exp(c′√(log x·log log x)) times.** Untried method 5 was only sketched in C_allE §1.3/§3c; this closes it.
4. **Pointwise multiplicity is the wrong hypothesis for the repo's machinery.** Even the hypothetical bound "c_P(e) ≤ 1 for every e > 8·10⁵" (no repeated large index at all) gives κ_L = κ_Q ≤ 16.7 in Theorem C″. The C″ total closes only for κ ≲ 1.57. What the tail needs is *sparsity* of occupied indices (about 0.06–0.1 primes per index), not bounded multiplicity (§7; estimate from logged C″ totals, label stated there).
5. Effective pointwise bound: c(e) < e·log 2/(2 log e − 2 log log e − 1) for e ≥ e₁. This is a factor-2 gain on the trivial bound and is useless for the tail by (B1) (§2.2).

## Ranked risks (worst first)
1. **The 2-D KKL corollary (item 3) uses the 2-D tilt lemma** (BBMST Lemma 3.4 in torus form, `DISTORTION.md` L1 + L4). I re-checked the KKL proof line by line against the arXiv v2 text, and every other step transfers. The constant c is not explicit, so the statement has no numeric content until someone makes c explicit.
2. The §7 estimate (κ ≲ 1.57 needed) is a 3-parameter fit to the logged C″ totals (`verdict3/C_tailR.log`). The pieces file `C_tailpieces_L1000.npz` is gitignored and absent, so it was **not** rerun. The conclusion "s = 1 is far from enough" has a factor ≈ 10 of room, but the threshold 1.57 is not certified.
3. Quantitative Subspace (row h): I did not find a published explicit count for the exceptional n in gcd(2^n−1, 3^n−1) > e^{εn}. The claim that such a count would exist but would not locate the exceptions is CONJECTURED from the structure of the Evertse–Schlickewei theorem. The break point, (B1) plus (B2), is PROVED and does not depend on it.
4. Matthews (1982) could not be opened (publisher challenge page). The bibliographic data is P via Crossref; the content is not seen. This does not matter: the statement Pehlivan attributes to him is proved in-house (C2_ce Lemma 3, and §4.1 here for any rank).

---------------------------------------------------------------------------------------------------------------------
## Table: tool | what it gives | where it breaks | label

| row | tool | what it gives for #203 | exact break | label |
|---|---|---|---|---|
| a1 | FFKPY Lemma 2.1 (δ ≥ α − β) in Z² | holds with β over pairs with gcd(e_i,e_j) > 1 | the aligned-pair β version is FALSE (pencil); the proof needs E_l independent of the σ-algebra of its "independent" set, and pairwise independence does not give that in Z² | PROVED + VERIFIED (§1.2) |
| a2 | FFKPY Lemmas 3.1–3.4, Thm 2 in Z² | residual density ≥ α^{(1+1/Q)/δ(C′)} − O(s² log²(QK)/Q), for indices in (N,KN] with index multiplicity ≤ s; Thm 2: no covering with all e_p > N, s_P ≤ exp(b√(log N loglog N)), Σ1/e_p ≤ c log L(N,s) | needs (i) s² ≪ Q/log²(QK) on (N,KN], unknown for c(e) (trivial s ~ N/log N); (ii) a lower bound on the **uniform** density δ(C′) of the Q-smooth part, which the repo does not have (B(E) bounds a tilted measure; HUB withdrawn list); (iii) Thm 2 needs min e_p > N, but #203 coverings may contain small e_p | PROVED (transfer); hypotheses unproved |
| a3 | FFKPY Thm 5 in Z² | exact coverings by cyclic-quotient cosets, indices > 2N, multiplicity ≤ 3exp(√(log N loglog N)), non-aligned | shows necessity only for (index, multiplicity) methods; says nothing about which lattices #203 primes realise | PROVED + VERIFIED small case (§1.3) |
| b1 | BCZ, Corvaja–Zannier, Hernández–Luca, Levin, Grieve–Wang | c(e) ≤ ε e/log e for e > e₀(ε), ineffective; λ(L) ≪ ε·(long basis vector)/log e outside finitely many proper-subtorus translates | (B1): linear in e, so every stage mass is still +∞; and ineffective; (B2) for the lattice version | PROVED break (§2) |
| b2 | trivial / elementary effective gcd bounds | Σ_{e_p=e} log p ≤ log gcd(2^e−1,3^e−1) < e log 2; c(e) < e log2/(2log e − 2loglog e − 1) | (B1) | PROVED (§2.2); data VERIFIED (§2.3) |
| c | Stewart 2013, Zsigmondy, Bilu–Hanrot–Voutier | existence of (large) primitive prime divisors | lower-bound / existence results: they produce primes, never cap c(e); Stewart's small-prime step is the trivial count p ≡ 1 mod n | PROVED break (§3) |
| d | Pehlivan Lemma 8 / Matthews; Erdős–Murty; Kurlberg–Pomerance; Elsholtz; Järviniemi; Ambrose | #{p : e_p ≤ t} ≪ t^{3/2}/log t (unconditional, = C2 Lemma 3); density-one lower bounds for e_p | t^{3/2} vs truth ≈ 0.12 t; partial summation gives Σ_{e_p≤E}1/e_p ≪ E^{1/2}, which diverges; density-one results are (B3) | PROVED (§4) |
| e | Bourgain, BGK, BKS, Konyagin–Shparlinski | cancellation in Σ_{h∈H} e(ah/p) for \|H\| ≥ p^δ or exp(log p/loglog p) | (B3) twice: covering data depend on p only through (Λ_p, coset), so additive characters of F_p are invisible (§5, PROVED lemma); and tail primes have \|H_p\| = e_p ≥ (log p/log 6)² only, far below every range | PROVED break |
| f4 | untried 4: CZ / HL for alignments c^< | bounds primes whose Λ_p contains two given independent vectors, i.e. λ(L) | (B2): c^<_{pq} is about two **different** primes with the same direction mod q (equal q-th power-residue ratio of 2 and 3); no gcd theorem speaks to that | PROVED break (§6.1) |
| f5 | untried 5: KKL multiplicity theorem | 2-D KKL Thm 3 directly (no slicing): min e_p ≤ exp(c log²(s_P+1)/loglog(s_P+2)) | gives a YES-side constraint only; c unspecified; tail needs bounds valid when small e_p are present | PROVED (§6.2) |
| g | L3 rows T10–T13 | see §8 | see §8 | §8 |
| h | quantitative Subspace (Evertse–Schlickewei, Evertse–Ferretti; CLP-type counts) | at best: explicit **number** of exceptional configurations, not their location | (B1) for c(e) and Σ log p (even an explicit everywhere bound ε e/log e leaves the stage masses infinite); (B2) for c^<; unlocated exceptions, each able to cost ≈ 0.1 of the budget | PROVED break; existence of the explicit count CONJECTURED (§9) |

---------------------------------------------------------------------------------------------------------------------
## 1. (a) FFKPY in two dimensions

Source: Filaseta, Ford, Konyagin, Pomerance, Yu, "Sieving by large integers and covering systems of congruences", J. Amer. Math. Soc. 20 (2007) 495–517, arXiv:math/0507374v3. I read §§2–5 in the PDF (P). Notation there: α(C) = ∏(1 − 1/n), β(C) = Σ_{i<j, gcd(n_i,n_j)>1} 1/(n_i n_j). "Multiplicity of n" = number of times n occurs as a modulus. L(N,s) = exp(log N · log log(s log N)/log(s log N)).

### 1.1 Setting
A *2-D residue system* is a finite list of cosets A_i = c_i + Λ_i ⊂ Z² with Z²/Λ_i ≅ Z/e_i cyclic, i.e. ψ_i(k,l) = a_i k + b_i l mod e_i with gcd(a_i,b_i,e_i) = 1. Density means density on the torus Z²/∩Λ_i. Every #203 certificate is one (`C_allE` §0). Two facts are used throughout, both PROVED:
- (F1) If gcd(e_i, [Z²:M]) = 1 for a lattice M, then Λ_i + M = Z². Proof: Z²/(Λ_i + M) is a quotient of both Z/e_i and Z²/M, so its order divides gcd(e_i, [Z²:M]).
- (F2) A k-fold intersection of cosets is empty or a coset of ∩Λ_{i_j}. Its index is ≥ lcm(e_{i_j}), because Z²/∩Λ surjects onto each Z/e_{i_j}. So its density is ≤ 1/lcm. This is L14(a) of `verdict3/L_literature.md`.

### 1.2 Lemma 2.1 (δ ≥ α − β)
**2-D Lemma 2.1 [PROVED].** For every 2-D residue system, δ ≥ α − β_gcd, where β_gcd sums 1/(e_ie_j) over the pairs with gcd(e_i,e_j) > 1.
*Proof.* This is FFKPY's induction (p. 7) with C″ = {j < l : gcd(e_j,e_l) = 1}. The one step that uses arithmetic is "the density of points in A_l not covered by C″ equals δ(C″)/e_l". That step needs A_l to be independent of the σ-algebra generated by C″, i.e. Λ_l + ∩_{j∈C″}Λ_j = Z². This follows from (F1), since [Z² : ∩_{C″}Λ_j] has only prime factors of the e_j, all coprime to e_l. The remaining steps are measure-theoretic. ∎

**The 2-D refinement is false [PROVED].** One would like the 2-D gain: replace "gcd(e_i,e_j) > 1" by "Λ_i + Λ_j ≠ Z²" (aligned pairs). This holds pairwise, but the proof needs independence from a whole σ-algebra, and pairwise independence does not give it in Z². Counterexample (the pencil): in F_ℓ² take the ℓ+1 lines through 0. Pulled back, these are ℓ+1 index-ℓ lattices in Z² with cyclic quotient. Any two distinct ones satisfy Λ_i + Λ_j = Z², so β_aligned = 0. The lines cover all 1 + (ℓ+1)(ℓ−1) = ℓ² points, so δ = 0 < (1 − 1/ℓ)^{ℓ+1} = α − β_aligned.
VERIFIED (`a4/pencil_ffkpy.py`, log `pencil_ffkpy.log`):
- ℓ = 2, 3, 5, 7: δ = 0, β_aligned = 0, and the aligned version fails; the gcd version holds. Control: dropping one line leaves density 1/4, 2/9, 4/25, 6/49 uncovered.
- 20 000 random systems (2–5 cosets, indices 2–6): **0** violations of the gcd version (PROVED, so a violation would mean a bug), and **588** violations of the aligned version. The control fires: the aligned version is false generically, not only for the pencil.

Consequence: inside the FFKPY framework the multiplicity hypothesis cannot be weakened by alignment. The alignment gain of `DISTORTION.md` lives only in the second-moment (distortion) framework, not in Bonferroni-type Lemma 2.1.

### 1.3 Lemmas 3.1–3.4 and Theorem 2
Write e_i = e′_i e″_i (Q-smooth part, Q-rough part). Let Λ′_i = Λ_i + e′_iZ² (index e′_i) and Λ″_i = Λ_i + e″_iZ² (index e″_i), so that Λ_i = Λ′_i ∩ Λ″_i by CRT in the cyclic group. Let Λ′ = ∩Λ′_i.
- **Lemma 3.1 (2-D) [PROVED].** For h ∈ Z²/Λ′, A_i ∩ (h + Λ′) is empty or (h + Λ′) ∩ (c_i + Λ″_i). The latter is a coset of Λ′ ∩ Λ″_i of relative index e″_i (by F1, since [Z²:Λ′] is Q-smooth). Its quotient is Λ′/(Λ′∩Λ″_i) ≅ Z²/Λ″_i, which is cyclic. So C_h is a 2-D residue system on Λ′ ≅ Z² with indices e″_i, and δ(C) = mean_h δ(C_h).
- **Lemma 3.2 (2-D) [PROVED].** If all e_i ∈ (N, KN] and every index value occurs at most s times, then mean_h β_gcd(C_h) ≪ s² log²(QK)/Q, with FFKPY's absolute constant. The proof on p. 11 uses only F(r,m,r′,m′) ≤ M/lcm[m,m′], i.e. P(i and j both active) ≤ 1/lcm(e′_i,e′_j). That is (F2) for the cosets of Λ′_i, Λ′_j. The rest is a sum over the index values (n, n′), with at most s² pairs (i,j) per value pair.
- **Lemma 3.3 (2-D) [PROVED].** The proof (AM–GM over the uncovered h, and "each coset produces its rough coset in exactly [Z²:Λ′]/e′_i of the C_h") is unchanged.
- **Lemma 3.4 and Theorem 2 (2-D) [PROVED].** The proof of Theorem 2 (pp. 15–17) uses only Lemma 3.4, Lemma 4.1 (smooth-number counts, no geometry), and the union bound 1 − δ ≤ Σ1/e. So: *for N ≥ N₀(b,c), no 2-D residue system with all indices > N, index multiplicity ≤ exp(b√(log N loglog N)) (b < 1/2) and Σ1/e_i ≤ c log L(N,s) (c < (1−4b²)/3) covers Z².*

**What multiplicity hypothesis the 2-D version needs.** Exactly the 1-D one, with modulus multiplicity replaced by c_P(e). On the window (N, KN], Lemma 3.2 is useful only if s² log²(QK) ≪ Q. By §1.2 a direction-aware weakening (count only pairs with the same direction mod a common rough prime q) is not available in this framework.

**Is it implied by anything known about c(e)? No [PROVED].** The best effective pointwise bound is c(e) < e log 2/(2 log e − 2 log log e − 1) (§2.2). BCZ gives c(e) ≤ ε e/log e, ineffectively. Both give s ≍ N/log N on (N, KN], and then s²/Q ≫ 1 for every Q ≤ N. The data has s ≤ 4 on e ≤ 8·10⁵ (VERIFIED, `gcd_data.log`), but the hypothesis is needed as N → ∞. There are two more breaks for #203 specifically:
- Lemma 3.4 needs a lower bound on the **uniform** density δ(C′) of the Q-smooth part, and the repo has only the tilted measure (HUB, withdrawn list).
- Theorem 2 needs every e_p > N, while #203 coverings are free to use the small primes.

### 1.4 Theorem 5 in two dimensions
FFKPY Theorem 5 (p. 20, P): for large N and s = exp(√(log N log log N)) there is an exact covering of Z with squarefree moduli > N and multiplicity ≤ s. The construction is a product over prime blocks P_j = (X_{j−1}, X_j], X_j = (j+1)^{j+1}: each class mod n is split into q classes mod nq, q ∈ P_{J+1}.
- **Aligned transfer [PROVED].** Pull back along π(k,l) = k. Each class r mod n becomes {k ≡ r mod n}, a coset of a lattice with quotient Z/n. This gives an exact covering of Z² by cyclic-quotient cosets, indices > N, index multiplicity ≤ s. All lattices contain (0,1): aligned (Lemma A), so it is the 1-D case in disguise.
- **Non-aligned transfer [PROVED].** Let C be the FFKPY covering, with every modulus odd. (In FFKPY's construction only the first block uses 2, via C₁ = {0,1 mod 2}. Start the induction instead from C₁ = {0,1,2 mod 3}: the same proof gives odd moduli > N/2 and multiplicity ≤ 3s/2.) Map Z² → F_2² × Z/M by (k,l) ↦ ((k,l) mod 2, k mod M) with M odd. This is onto by CRT. Take the cosets {φ_d ≡ 0 mod 2} × {k ≡ r mod n}, for the three lines d ⊂ F_2² and every (n,r) ∈ C. Then:
  - The quotient is Z/2 × Z/n ≅ Z/2n, which is cyclic.
  - The union is (∪ lines) × (∪ classes) = everything.
  - The indices are 2n > N.
  - The index multiplicity is ≤ 3 × (that of C).
  - No primitive vector lies in all the lattices, because it would have to lie in all three lines mod 2, i.e. be ≡ 0 mod 2.
  - The system is saturated at ℓ = 2 (all three directions occur), so the direction lemma does not apply either.
  VERIFIED on the small instance pencil(F_2²) × {0,1 mod 3; 2,5,8 mod 9}: 0 uncovered cells on (Z/18)², and dropping one coset leaves 9 (control); all quotients cyclic; no common primitive vector with |v|_∞ ≤ 36.

**Reading.** In 2-D, as in 1-D, coverings with arbitrarily large minimum index exist once the index multiplicity is about exp(√(log N loglog N)), with or without alignment. So **a bound on c(e) is provably necessary for every method that uses only (index, multiplicity) data** [PROVED]. These are abstract coverings: nothing says #203's primes realise these lattices (one lattice of index e is occupied with probability ≈ 0.12/ψ(e), L22). Whether a hypothesis about *which lattices* occur could replace c(e) is **not established** either way.

---------------------------------------------------------------------------------------------------------------------
## 2. (b) gcd and S-unit tools; the best effective bound on Σ_{e_p=e} log p

### 2.1 Ineffective tools
- **BCZ** (Math. Z. 243 (2003)): log gcd(a^n−1, b^n−1) < εn for n ≥ n₀(a,b,ε), ineffective. Statement P via the Ostafe MPIM abstract and Corvaja–Zannier arXiv:2608.28255 §3 ("The proof of Theorem 3.2 relies on the Subspace Theorem … hence the result is not effective"; P).
- **Corvaja–Zannier / Hernández–Luca** (Bol. Soc. Mat. Mexicana 9 (2003) 235–244, bibliographic data S) and **Levin** (Invent. Math. 215 (2019), Thm 1.1, statement P as quoted in Grieve–Wang arXiv:1902.09109 p. 1: log gcd(f(u), g(u)) < ε max h(u_i) for u ∈ Γ outside a finite union Z of translates of proper algebraic subgroups).
- **Grieve–Wang** (TAMS 373 (2020)): moving-target forms.
- **Luca** (Monatsh. Math. 146 (2005)) made Hernández–Luca "more explicit", but the constants C₁(S), C₂(S) are "not effectively computable" (Stewart's survey "On prime factors of integers which are sums or shifted products", p. 4, P).

**What they give, at best [PROVED from the statements].** c(e) log(e+1) ≤ Σ_{e_p=e} log p ≤ log gcd(2^e−1, 3^e−1) < ε e for e > e₀(ε). For a lattice L with reduced basis u, v (|u| ≤ |v|), the Levin form gives λ(L) log e ≤ ε·max(|u|_1,|v|_1)·log 6 outside the exceptional set Z. Combined with the trivial λ(L) log e ≤ |u|_1 log 3, this gives λ(L) ≪ √(ε e)/log e for lattices outside Z.

**Where it breaks [PROVED].**
- (B1): for every stage ℓ ≥ 5, the first-moment majorant m₁(ℓ) = Σ_{P⁺(e)=ℓ} c(e) r G(e)/e ≥ Σ_{P⁺(e)=ℓ} 1·(c(e)/e). Under c(e) ≤ εe/log e this is bounded only by Σ_{P⁺(e)=ℓ} ε/log e = ∞, since each stage holds the infinitely many e = ℓ^v e′. The same holds for the quadratic majorant through its diagonal. So no stage mass is finite, let alone summable.
- (B2): the lattice form bounds λ(L), not c(e) = Σ_{[Z²:L]=e} λ(L) over ψ(e) ≈ e lattices.
- And it is ineffective.

### 2.2 Best effective bounds
**Proposition E [PROVED].** For every e ≥ 2: Σ_{e_p=e} log p ≤ log gcd(2^e−1,3^e−1) < e log 2. If moreover c(e) ≥ e/(log e)², then c(e) < e log 2 / (2 log e − 2 log log e − 1).
*Proof.* The primes with e_p = e are distinct and divide 2^e − 1 and 3^e − 1. Each is ≡ 1 mod e (e = |⟨2,3⟩| divides p − 1), so the j-th smallest is ≥ 1 + je. Hence e log 2 > Σ log p ≥ c log e + log c! ≥ c(log e + log c − 1). If c ≥ e/(log e)², then log c ≥ log e − 2 log log e. ∎
So c(e) ≤ max(e/(log e)², (½+o(1)) e log 2/log e). This is a factor-2 gain on the trivial e log 2/log(e+1), and it breaks at (B1) like everything else.

**The published effective estimate is weaker than trivial [PROVED].** Masser's appendix to Corvaja–Zannier arXiv:2608.28255 (pp. 42–43, P) proves h((3^m−1)/(2^n−1)) ≥ 10⁻³² max(m,n) − 1, effectively, via linear forms in logarithms. With x = (3^m−1)/g, y = (2^n−1)/g in lowest terms (g the gcd), h = max(log x, log y), so log g ≤ max(m log 3, n log 2) − 10⁻³² max(m,n) + 1. The trivial bound is log g ≤ min(m log 3, n log 2) + O(1). Masser's bound beats it only when |m log 3 − n log 2| < 10⁻³² max(m,n), which never happens for m = n (the case of e_p). The paper itself says the estimate "is too weak to imply the non-integrality of the quotient".

**Answer to (b).** The best unconditional effective bound is Σ_{e_p=e} log p ≤ log gcd(2^e−1, 3^e−1) < e log 2, i.e. c(e) ≲ e log 2/(2 log e). For the stage masses it gives **+∞ at every stage** (B1). I found no effective o(e) bound and no effective (1 − c)e log 2 bound in any source.

### 2.3 What the truth looks like (VERIFIED, n ≤ 2·10⁴)
`a4/gcd_data.py` (logs `gcd_data.log`, `gcd_data_20000.log`) computes g_n = gcd(2^n−1, 3^n−1) exactly for n ≤ 20 000:
- max log g_n/(n log 2) = 0.736 (n = 12); 0.323 for n ≥ 100 (n = 120); 0.111 for n ≥ 1000 (n = 1080).
- **g_n is exactly explained by the certified pool**: Π over pool primes with e_p | n of p^{v_p(g_n)} = g_n for every n ≤ 20 000. This is an independent check of pool completeness for e ≤ 2·10⁴.
- Planted control: deleting one pool prime makes exactly the multiples of its e_p fail (fired).
- Proposition E has 0 violations on the pool (e ≤ 8·10⁵); max c(e) = 4.

---------------------------------------------------------------------------------------------------------------------
## 3. (c) Stewart 2013, Zsigmondy, primitive divisors
- **Stewart**, "On divisors of Lucas and Lehmer numbers", Acta Math. 211 (2013) 291–314 (bibliographic data and main bound S via Project Euclid and the MR summary): P(u_n) > n·exp(log n/(104 log log n)) for n large, effectively. With Kunrui Yu's p-adic forms (same issue).
- **Zsigmondy / Bilu–Hanrot–Voutier**: 2^n − 1 and 3^n − 1 have a primitive prime divisor for n > 6 (n ≠ 6 for base 2).

**What they give for #203 [PROVED].** Existence of primes p with ord_p 2 = n (so n | e_p), and (Stewart) such primes with p > n^{1+1/(104 log log n)}. These are **lower-bound / existence** statements: they add primes to the pool and can never cap c(e).

**Where Stewart's method would have to help, and why it does not [PROVED].** Stewart bounds the contribution of *small* primes p ≤ n^{1+δ} to Φ_n(α,β). The count part of that step is trivial: such p are ≡ 1 mod n, so there are ≤ n^δ of them. The deep part is a bound on valuations v_p (Yu). For c(e) the same split gives #{p : e_p = e, p ≤ e^{1+δ}} ≤ e^δ (trivial). The primes with p > e^{1+δ} number ≤ e log 2/((1+δ) log e) (size). No ingredient counts large primes better than size, so the bound stays ≍ e/log e, i.e. (B1).

---------------------------------------------------------------------------------------------------------------------
## 4. (d) Order statistics

### 4.1 Pehlivan Lemma 8 (attributed to Matthews 1982)
Pehlivan, arXiv:1504.01550, p. 4 (P, read today): "Next Lemma is implicit in the work of C. R. Matthews (see [4]). Lemma 8. Assume that Γ ⊆ Q* is a multiplicative subgroup of rank r ≥ 2 … #{p ∉ Supp Γ : |Γ_p| ≤ t} ≪_Γ t^{1+1/r}/log t."
- There is no GRH hypothesis in Lemma 8. The next result, Theorem 9, begins "Assume the GRH". So **Lemma 8 is stated unconditionally** (P).
- Reference [4] = C. R. Matthews, "Counting points modulo p for some finitely generated subgroups of algebraic groups", Bull. London Math. Soc. 14 (1982) 149–154. Title, author, volume and pages are P via Crossref (doi 10.1112/blms/14.2.149). The content is **U**: the publisher page returned a bot-challenge.

**In-house proof for any rank [PROVED].** Let T = ⌊t^{1/r}⌋. The (T+1)^r > t exponent vectors in [0,T]^r cannot have distinct images in Γ_p, so two of them collide. Their difference v ≠ 0 has |v|_∞ ≤ T and p | N(v) := numerator·denominator of ∏a_i^{v_i} − 1, with log N(v) ≪_Γ T. Each N(v) has ≪ T/log T prime factors > t. So #{p : |Γ_p| ≤ t} ≪ (2T+1)^r·T/log T + π(t) ≪ t^{1+1/r}/log t. For r = 2 this is C2_ce Lemma 3.

### 4.2 Almost-all results
Erdős–Murty (ord_p a ≥ p^{1/2+ε(p)} for almost all p), Matthews / Agrawal–Pollack (|⟨a_1..a_k⟩ mod p| ≥ p^{k/(k+1)−ε} for almost all p), Kurlberg–Pomerance (Acta Arith. 119 (2005)), and Elsholtz (Proc. AMS 130 (2002)) are density-one statements (S/P per L3 rows; I did not reopen them). Two GRH-conditional density results also fall here:
- Järviniemi, arXiv:1912.02554, "Equality of orders of a set of integers modulo a prime". Single author (P, today). Its results are GRH-conditional.
- **Citation conflict found:** `verdict3/C_allE.md` §4.4 attributes arXiv:1912.02554 to "Agrawal–Pollack". That is wrong. Agrawal–Pollack is arXiv:2006.15200 (per L17). Fix C_allE §4.4.
- Ambrose (on Artin/Rohrlich): about primes where a large-rank Γ contains a primitive root, i.e. *large* Γ_p. Not relevant to small e_p (title-level only, U).

### 4.3 Why no count of #{p : e_p ≤ t} can bound the tail [PROVED]
- (i) Lemma 8 gives t^{3/2}/log t, and partial summation gives Σ_{e_p≤E} 1/e_p ≪ E^{1/2}. The truth is ≈ 0.12t, and Σ_{e_p≤E}1/e_p ≈ 1.58 log log E (C_allE §4.1). That diverges too, so the linear tail diverges even at the truth.
- (ii) **Even the bound #{p : e_p ≤ t} ≤ t/log t — better than the truth — does not make a single stage finite.** Take c(7^k) = ⌊7^k/(4k log 7)⌋ and c(e) = 0 otherwise. This satisfies Proposition E and Σ_{e≤t} c(e) ≪ t/log t, yet the stage-7 union bound Σ_k c(7^k)/7^k = Σ 1/(4k log 7) = ∞.

So counting functions are the wrong shape. The tail needs class sums over smooth sets (H_cls, H_Q^R), as C_allE §4.3 and C2_ce §5 already state for second moments.

---------------------------------------------------------------------------------------------------------------------
## 5. (e) Exponential sums over small subgroups

**Lemma X [PROVED].** For p ∤ 6m: p | 2^k3^l m + 1 ⇔ 2^k3^l ≡ −m^{-1} (mod p). So the killed set is empty (−m^{-1} ∉ H_p) or a coset of Λ_p, and by CRT on m every coset of Λ_p occurs. Hence the set of certificates, and every quantity in the distortion bound, depends on p only through the lattice Λ_p ⊂ Z².

Two primes with the same Λ_p are interchangeable. Additive characters of F_p see how H_p = ⟨2,3⟩ sits inside (F_p, +), which Λ_p does not record.

**Where it breaks [PROVED].** Bourgain, Bourgain–Glibichuk–Konyagin (J. London Math. Soc. 73 (2006)), Bourgain–Konyagin–Shparlinski and Konyagin–Shparlinski give cancellation in Σ_{h∈H} e_p(ah) for |H| ≥ p^δ, or (Bourgain) somewhat below. Ranges are S from memory, not re-read today. These results:
- (1) do not count primes, while the tail needs counts of primes per index or class;
- (2) concern a structure that Lemma X shows is irrelevant to coverings;
- (3) do not reach the tail primes, which have |H_p| = e_p as small as (log p/log 6)² (C2_ce Lemma 1), far below every known range.

This is (B3).

---------------------------------------------------------------------------------------------------------------------
## 6. (f) The two untried methods

### 6.1 Untried method 4: Corvaja–Zannier / Hernández–Luca for alignments c^<
c^<_{pq} is the ℓ-free part of gcd(D_pq, e_p, e_q). A prime q′ divides it iff q′ | e_p, e_q and Λ_p ≡ Λ_q mod q′.

**Arithmetic form [PROVED].** For q′ | e_p, Λ_p mod q′ = {w : 2^{w₁}3^{w₂} ∈ H_p^{q′}}. So the direction of p mod q′ is the ratio (ind 2 : ind 3) ∈ P¹(F_{q′}), where ind is taken in the cyclic group H_p/H_p^{q′}. Alignment of p and q means two **different primes** whose q′-th power-class ratio of 2 and 3 agrees.

CZ/HL/Levin bound the primes dividing *both* 2^a3^b − 1 and 2^c3^d − 1. That is **one** prime whose Λ_p contains **two** independent vectors (then e_p | ad − bc), i.e. λ(L) (§2.1). No gcd theorem speaks about pairs of primes with equal power-class ratios.

Method 4 is **dead at (B2)** [PROVED]. It is also ineffective, and the per-lattice bound it would give, λ(L) ≪ √(εe)/log e, does not even sum to a c(e) bound.

### 6.2 Untried method 5: Klein–Koukoulopoulos–Lemieux multiplicity theorem
Source: KKL, arXiv:2212.01299v2 (P, PDF read today). Theorem 3: "Let A be a covering system of multiplicity s. Then there exists an absolute constant c > 0 such that its smallest modulus is ≤ exp(c log²(s+1)/log log(s+2))", with m(A) = max_d #{j : d_j = d}.

C_allE §1.3/§3c only noted that KKL could be applied after slicing in the unsaturated case, and drew no theorem from it. Done here directly, without slicing:

**Theorem K2 [PROVED, given DISTORTION.md L1/L4].** Every covering of Z² by cosets of cyclic-quotient lattices with index multiplicity s has min index ≤ exp(c log²(s+1)/log log(s+2)), with the same absolute c.
*Proof check (line by line, KKL pp. 3–7).* The proof uses:
- (i) BBMST's distortion lemma (KKL Lemma 3.1), valid for any finite abelian torus with the stage filtration. The repo's `DISTORTION.md` uses it on Z²/Λ_P.
- (ii) KKL Lemma 3.2, a union bound over i with P⁺(e_i) = p_j, writing e_i = g p_j^r. In 2-D the event "x ⊆ a_i + gZ" becomes "x lies in the Q_{j−1}-part coset of A_i", with the same count.
- (iii) Display (3.2): tilted probability of a k-fold intersection ≤ ∏_{p_i | [g]} (1−δ_i)^{−1}/[g₁,…,g_k]. In 2-D this is (F2) plus the tilt inflation lemma (DISTORTION.md L1 + L4, BBMST Lemma 3.4 in torus form).
- (iv) Multiplicity: at most s^k choices of (i₁..i_k) per value tuple.
- (v) Sums over g₁, g₂ | Q_{j−1} and smooth-number Lemma 3.4, which involve no geometry.
Nothing uses the line structure of Z. ∎

**Consequence for #203 (YES side) [PROVED].** For every covering P: min_{p∈P} e_p ≤ exp(c log²(s_P+1)/loglog(s_P+2)). Equivalently, *a covering that uses no prime with e_p ≤ x has some index repeated s_P ≥ exp(c′√(log x · log log x)) times.*

This is stronger than C_allE Corollary D in two ways:
- no unsaturation hypothesis;
- multiplicity s instead of distinct indices.

It is unconditional, but c is not explicit, so it has no numeric instance yet. An explicit c via the repo's code would need the worst-case alignment (2^{ω} factors): a rough estimate puts the s = 1 threshold far above 8·10⁵ (y ~ 10⁹ is needed to make the quadratic part small, and then the y-smooth mass above x is small only for x astronomically larger). Not computed.

**Why it is not a tail tool.** Its hypothesis is min e_p large, and #203 coverings may contain e_p = 4, 6, 10, …. Its tail part (η₂ ≪ s²(log y)⁵/y) is the repo's quadratic tail with n(e) ≤ s, which by §7 (an estimate, not certified) closes nothing at any s ≥ 1.

---------------------------------------------------------------------------------------------------------------------
## 7. Pointwise multiplicity cannot feed Theorem C″ [estimate; label below]
**Domination [PROVED].** If n(e) ≤ s for all e > E₀, then n(e) ≤ (s/τ)·τ e/φ(e) with τ = C₀/ln E₀ = 0.0598. Every stage and range functional is ≤ (s/τ) × model, and every Q-functional ≤ (s/τ)² × model. So H_L^R and H_Q^R hold with κ_L = κ_Q = s/τ = 16.7 s.

**Estimate.** `a4/kappa_fit.py` fits total = A + Bκ_L + Xκ_Q + Qκ_Q² to the six uniform-κ totals in `verdict3/C_tailR.log` (run-δ profile). Results:
- max residual 8·10⁻⁵;
- held-out point (1, 1.34) reproduced (0.9471);
- control: a planted wrong total shows residual 0.064.

The fitted total reaches 1 at κ ≈ 1.57. At s = 1 it is 13.7 (κ = 16.7), or 3.2 if one credits e/φ(e) ≈ 2.5 (κ = 6.7).

Label: the domination is PROVED. The numbers are an extrapolation of logged values (CONJECTURED), because a per-stage re-choice of majorant at large κ could lower them and the pieces file is absent. A factor ≥ 3 separates even the most generous version from 1, so the qualitative conclusion is robust: **the tail hypothesis must say that occupied indices are sparse (≈ 0.1 primes per index, κ ≲ 1.5), not merely that indices repeat boundedly**. Since c(e) ∈ {0,1,…}, no pointwise multiplicity bound of any size can be the missing input to C″.

---------------------------------------------------------------------------------------------------------------------
## 8. (g) L3 rows owned by 4

| L3 row | check | verdict |
|---|---|---|
| T10 Pehlivan Lemma 8 / Matthews | Lemma 8 re-read on arXiv:1504.01550 p. 4: unconditional statement, "implicit in the work of C. R. Matthews"; Matthews' bibliographic data P via Crossref, content U | CONFIRMED. Proof supplied for any rank (§4.1). Gives E^{3/2}/log E, no improvement, and counts are the wrong shape anyway (§4.3) |
| T11 Akbary–Yazdani, Erdős E_a(r) ≪ r^ε, Prachar | re-read arXiv:1505.06500 pp. 1–2: Conj. 1.2 verbatim ("E_a(r) = #{p prime; ord_p(a) = r} … ≪_ε r^ε", formulated in [4] for a = 2); Prachar Satz 2: #{p : (p−1)\|n} ≥ exp(c log n/(log log n)²) infinitely often | CONFIRMED. For #203: Σ_{d\|n} c(d) ≥ #{p ≥ 5 : (p−1)\|n} for those n (p−1 \| n ⇒ 2^n ≡ 3^n ≡ 1). That lower-bounds divisor sums only; τ(n) is larger still for such n, so it does not contradict any pointwise c bound |
| T12 Levin Invent. 2019 Thm 1.1 | statement re-read as quoted in Grieve–Wang arXiv:1902.09109 p. 1 (P for the quote; the Invent. text itself U) | CONFIRMED as quoted. Breaks at (B1)/(B2), ineffective (§2.1, §6.1) |
| T13 Grieve–Wang, Xiao, Luca 2005 | GW PDF header and Thm 1.1 read (P); Luca 2005: "constants not effectively computable" per Stewart's survey p. 4 (P for the survey) | CONFIRMED; ineffective, (B1) |
| N9 (L2) FFKPY | full §§2–5 read | done in §1: Lemmas 2.1, 3.1–3.4 and Thm 2 transfer; aligned refinement false; Thm 5 transfers, non-aligned too |

---------------------------------------------------------------------------------------------------------------------
## 9. (h) Quantitative Subspace Theorem (Evertse–Schlickewei, Evertse–Ferretti, Schmidt; CLP-type counts)

**What these theorems say [S].** For a system of linear forms and a fixed finite set S of places, the solutions x of the Subspace inequality with height H(x) ≥ H₀ (H₀ explicit) lie in at most N₁ proper linear subspaces, with N₁ explicit in the dimension, ε and |S|. Neither the subspaces nor the "small" solutions H(x) < H₀ are located. Statement S, as quoted by Cilleruelo–Luca–Pizarro-Madariaga (Math. Comp. 85 (2016), arXiv:1305.3580: "number of exceptional subspaces ≤ (2^{60M²}δ^{−7M})^s", per L1 row N3) and by Stewart's survey (p. 3: decomposable-form results "depend on quantitative versions of Schmidt's Subspace Theorem due to Schmidt and Schlickewei").

**What it would give here [CONJECTURED].** The BCZ argument uses a fixed S = {∞, 2, 3} and points of height ≍ n. Run with a quantitative Subspace Theorem, it should give #{n > n₁(ε) : log gcd(2^n−1,3^n−1) > εn} ≤ K(ε), with n₁ and K explicit and the exceptional n unlocated. The same holds for Levin-type statements on lattices. I found no paper that states this for gcd(a^n−1, b^n−1). The closest effective published statement is Masser's (§2.2), which is weaker than trivial. The CLP explicit Lemma 8 is the closest analogue in form (L1 N3).

**Where it breaks, even if that count is granted [PROVED].**
1. **c(e) and Σ_{e_p=e} log p.** Outside the K(ε) exceptions and above n₁(ε), the bound is c(e) ≤ εe/log e. That is linear in e, so every stage first moment is still +∞ (B1, §2.1). An explicit count of exceptions does not change the non-exceptional part, which is already divergent.
2. **Unlocated exceptions.** Each exceptional e may carry up to c(e) ≈ e log 2/(2 log e) primes (Proposition E). Its linear cost is then up to r·G(e)·c(e)/e ≈ 2.24·G·log 2/(2 log e) ≈ 0.06·G for e > 8·10⁵. So K(ε) ≥ 5 unlocated exceptions could by themselves exhaust the 1 − B′ ≈ 0.22 margin of Theorem Z. Locating them requires effective heights, which no quantitative Subspace Theorem provides.
3. **Alignment c^<.** A quantitative Levin/CZ statement counts lattices L with abnormally many primes λ(L), i.e. one prime containing two vectors. Alignment is about two different primes with the same direction mod q (§6.1), so (B2) applies unchanged.
4. **The range n ≤ n₁(ε).** It is explicit but astronomically large. Below it nothing is said, and the pool is certified only to 8·10⁵ (1.6·10⁶ in progress).

**Row (h) verdict.** Dead at (B1) for c(e) and Σ log p, and at (B2) for alignments. The "effective" content is a count, not a location, and even a located everywhere-bound of the BCZ shape would not close a single stage.

---------------------------------------------------------------------------------------------------------------------
## 10. The weakest unconditional YES-side statements this work yields (beyond Theorem Z)
1. **Theorem K2 (§6.2) [PROVED, c inexplicit].** Every covering P has min_{p∈P} e_p ≤ exp(c log²(s_P+1)/log log(s_P+2)). A covering avoiding all e_p ≤ x needs an index of multiplicity ≥ exp(c′√(log x loglog x)) within P.
2. **2-D FFKPY Theorem 2 (§1.3) [PROVED, N₀ inexplicit].** A covering with all e_p > N and s_P ≤ exp(b√(log N loglog N)) has Σ_{p∈P} 1/e_p > c log L(N, s_P). This forces a large reciprocal sum, not just ≥ 1.
3. **Necessity (§1.4) [PROVED].** Non-aligned, direction-saturated abstract coverings of Z² with indices > N and index multiplicity ≤ 3exp(√(log N loglog N)) exist. Hence no "no covering at any size" theorem can be proved from (index, multiplicity) information alone.
4. **lcm.** I found no improvement on L > 8·10⁵. The route via log gcd(2^L−1, 3^L−1) ≥ Σ_{p∈P} log p ≥ 14 082·log(8·10⁵) gives L ≥ 2.76·10⁵, which is weaker. [PROVED, and useless]
5. **Minimum number of primes.** Unchanged at 14 082 (Theorem Z). None of the tools above adds to it, since they all need min e_p large or c(e) bounds.

## NOT ESTABLISHED
- Whether a direction-aware hypothesis (which lattices occur, or equidistribution of q-th power-class ratios among primes with q | e_p) could replace c(e). §1.2 rules this out only inside FFKPY's Bonferroni framework, not inside the distortion framework.
- Explicit constants in Theorem K2 and in 2-D FFKPY Theorem 2.
- A published explicit exceptional count for BCZ (row h).
- The precise κ threshold for the final C″ profile (§7 used the run-δ profile).

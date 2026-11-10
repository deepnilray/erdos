# Erdős #203, literature agent L3: tools that could prove NO or bound the tail (2026-11-03)

Slice: shifted primes and their {2,3}-free parts, sieves on sparse/exponential sequences, S-unit and gcd bounds, order statistics for ⟨2,3⟩ mod p, sums over small subgroups, and **an explicit fundamental lemma for Theorem A**.
Flags: **P** = I read the statement on a primary page today (paper PDF, author-hosted PDF, scan). **S** = read in a secondary source that quotes it (named in the row). **U** = not verified.
Labels for my own claims: PROVED / VERIFIED (with a bound and a control) / CONJECTURED. Downloads are in `scratchpad/L3dl/` (untrusted data, not executed); my scripts are in `scratchpad/L3scripts/` (`fh_table.py`, `fh_E.py`).

---------------------------------------------------------------------------------------------------------------------
## (a) Verdict

**PARTIAL: one actionable result, several corrections, and nothing that settles #203 or bounds c(e).**

1. **Theorem A no longer needs *Opera de Cribro*.** The Brun–Hooley sieve in the form of Ford–Halberstam (J. Number Theory 81 (2000) 335–350; the authors' PDF is open) and of Ford's 2023 lecture notes, Thms 2.3 and 3.2 (open), is a fully explicit fundamental lemma. It assumes no dimension condition and has no K^{10} factor. I read and checked it on the primary page (P).
   - The upper bound S ≤ XV(z)e^E + R′ and the lower bound S ≥ XV(z)(1 − E) − R″ hold for any partition of the primes and any even k_j, with E = Σ_j e^{L_j·1[k_j>0]} L_j^{k_j+1}/(k_j+1)!.
   - In the x → ∞ regime that Theorem A uses, I computed the errors (VERIFIED, model stated in §(c).4, control fired). The pair error is η₂ ≤ 2.1·10⁻⁴ at s = 22 (κ = 2). FI's e^{18−s}K₂^{10} with K₂ = 5/3 gives 3.0 at the same s.
   - So the dependency would be removed **and** r0 would come down: the unstratified exceptional share falls to ≤ 2.8% already at Ω ≤ 19, where FI needs Ω ≤ 29. The owner (5) must still write out one asymptotic step and rerun the stratified table.
2. **Numbering correction.** The explicit lemma with error e^{9κ−s}K^{10} is *Opera de Cribro* **Lemma 6.8**, not 6.3. Three open papers quote it under that number with the same form (S). "Lemma 6.3" is the Iwaniec–Kowalski number, and IK Lemma 6.3 is a different, **non-explicit** statement (O-constant depending on κ, per Sofos and Da Silva). The repo's "Lemma 6.3, explicit e^{9κ−s}K^{10}" therefore names a statement that does not exist in that form under that number.
3. **Untried method 6** (image of p ↦ {2,3}-free part of p−1). I found **no result on this map's image or fibres** beyond Erdős–Odlyzko, Sun–Fang and Chen, which are already in the ledger.
   - The neighbouring literature studies other objects: y-smooth shifted primes (Baker–Harman, Lichtman), or Linnik bounds for moduli with small core (Iwaniec 1974, Chang, Banks–Shparlinski). The latter give "for each A = 2^a3^b some m ≤ A^{L−1} is hit", never "every m is hit".
   - Absence is weak evidence: I ran four searches.
4. **c(e)**: still no unconditional bound beyond the trivial one.
   - Pehlivan's Lemma 8 (the E^{3/2} pool count) is stated with no GRH hypothesis (P), but with no proof; it is attributed to Matthews 1982.
   - The gcd results of Levin (Invent. 2019) and Grieve–Wang (TAMS 2020) generalise BCZ, Corvaja–Zannier and Hernández–Luca. All use the Subspace Theorem and are ineffective.
   - Erdős's conjecture E_a(r) ≪ r^ε is re-read on the page (P).

Risks, worst first:
1. My Brun–Hooley table uses the limit L_j → κ·log(t_j/t_{j+1}) as z → ∞. This is legitimate because Theorem A is stated for x ≥ x₀, but the deep intervals near the bottom of the partition need a written o(1) argument (§(c).4) before Theorem A can be called PROVED.
2. The FI Lemma 6.8 statement is still second-hand (S). Its κ-range differs between quoters: Matomäki–Teräväinen write κ ≥ 1, Thorner–Zaman κ > 0.
3. The searches on smooth parts of shifted primes and on sieves for 2^a3^b + c were few, so absence of results there is weak evidence.

---------------------------------------------------------------------------------------------------------------------
## (b) New rows

| # | source (verified) | technique | exact statement or what it proved | how it could apply to #203 | owner | flag |
|---|---|---|---|---|---|---|
| T1 | K. Ford, H. Halberstam, "The Brun–Hooley sieve", J. Number Theory 81(2) (2000) 335–350 (venue from the bibliographies of arXiv:2608.14190 and 2304.04805); text read in the authors' PDF ford126.web.illinois.edu/wwwpapers/hooleysieve.pdf, §3, p. 7 | Hooley's almost-pure sieve: Brun truncation on each block of a partition of the primes, plus Lemma 1 (x₁⋯x_r ≥ y₁⋯y_r − Σ(y_ℓ−x_ℓ)∏_{j≠ℓ}y_j) | **Theorem** (p. 7): S(A,P) ≤ X∏_{p∈P}(1−ω(p)/p)·exp E + R, and S(A,P) ≥ (1−E)X∏(1−ω(p)/p) − R − R′, with E = Σ_j L_j^{k_j+1}e^{L_j}/(k_j+1)!, L_j = log W_j^{−1}, W_j = ∏_{p∈P_j}(1−ω(p)/p), any partition P = ∪P_j, any even k_j. R and R′ are sums of \|r_d\| over d = d₁⋯d_r with ν(d_j) ≤ k_j (one block k_ℓ+1 for R′). No dimension hypothesis is needed for this Theorem. | **Replaces FI Lemma 6.8 in Theorem A; fully explicit; gives smaller errors** (§(c)). | 5 | P (content), S (venue) |
| T2 | K. Ford, *Sieve methods lecture notes, Spring 2023* (PDF dated 10 Mar 2026), ford126.web.illinois.edu/sieve2023.pdf: Thm 2.3 p. 17, Thm 3.2 p. 31, Thm 3.6 p. 38 | Same sieve, with a refinement | Thm 2.3: S(A,z) ≤ XV(z)e^E + R′ with E = Σ_j e^{L_j 1_{k_j>0}} L_j^{k_j+1}/(k_j+1)! (the factor e^{L_j} is dropped when k_j = 0). Thm 3.2: S(A,z) ≥ XV(z)(1−E) − R″, with R″ over d ≤ z₁^{k₁+1}z₂^{k₂}⋯z_t^{k_t}. Thm 3.6 (Fundamental Lemma) adds (Ω) and gets 1 + O(e^{−s log s + s log₃ s + O_{κ,B}(s)}) for s ≥ 100, with a non-explicit constant. | Thms 2.3 and 3.2 are the citable explicit forms; Thm 3.6 is not explicit. | 5 | P |
| T3 | H. Iwaniec, "Rosser's sieve", Acta Arith. 36 (1980) 171–202; scan matwbn.icm.edu.pl/ksiazki/aa/aa36/aa36210.pdf (read as images) | Rosser–Iwaniec (beta) sieve, any dimension κ | Hypothesis (1.3): ∏_{w≤p<z}(1−ω(p)/p)^{−1} < (log z/log w)^κ(1 + K/log w). **Thm 1** (p. 172), for all y ≥ z ≥ 2: S < XV(z){F(s) + e^{√K}Q(s)(log y)^{−1/3}} + Σ_{d<y, d\|P(z)}\|R(A,d)\|, with the lower bound using f(s). Q(s) < exp{−s log s + s log log 3s + O(s)} (1.6). F and f solve (1.8)–(1.9). Implied constants depend only on κ. **Thm 4** (Fundamental Lemma, p. 177): S = XV(z){1 + θ₁e^{√K}Q(s)} + θ₂Σ_{d<y}\|R\|, \|θ_i\| ≤ 1. | Not explicit: the O(s) in Q is unspecified. **But** for fixed s and x → ∞ the error term vanishes, so Thm 1 gives Theorem A with η = F_κ(s) − 1 and 1 − f_κ(s), which are explicit functions. Computing F₂ rigorously needs β₂ and A₂ from §5 of the paper (a delay-ODE computation). This is a second route to replacing FI; T1 is simpler. | 5 | P |
| T4 | Friedlander–Iwaniec, *Opera de Cribro* (AMS Colloq. Publ. 57, 2010), **Lemma 6.8**, quoted by (i) Matomäki–Teräväinen, arXiv:2301.07679, Lemma 9.1, PDF p. 32; (ii) Thorner–Zaman, arXiv:1803.02823 (ANT 13 (2019)), Lemma 6.2 p. 19 and Thm 6.1 p. 18; (iii) Grimmelt, arXiv:1809.10008, Lemma 2.4 p. 17 (κ = 1) | Beta sieve, β = 9κ+1 | MT Lemma 9.1, verbatim apart from typesetting: "Let κ ≥ 1 be fixed. Let z ≥ 2 and let D = z^s with s ≥ 9κ+1. There exist coefficients λ^±_d [with] \|λ^±_d\| ≤ 1, supported on {d ≤ D : d \| P(z)}, Σ_{d\|n}λ^−_d ≤ 1_{(n,P(z))=1} ≤ Σ_{d\|n}λ^+_d. If h : N → [0,1) is multiplicative with ∏_{w₁≤p<z₁}(1−h(p))^{−1} ≤ K(log z₁/log w₁)^κ for any z₁ ≥ w₁ ≥ 2, then Σλ^+_d h(d) ≤ (1 + e^{9κ−s}K^{10})∏_{p<z}(1−h(p)) and Σλ^−_d h(d) ≥ (1 − e^{9κ−s}K^{10})∏_{p<z}(1−h(p))." TZ quote the same bound as "essentially [FI, Lemma 6.8]" for κ > 0, with the hypothesis "[FI, Eq. 5.38]". | This is the input Theorem A uses (D_almostall §10.6, §11.6), under the wrong number 6.3. Its hypotheses match D's use: K is a sup over real intervals, which D computes (K₁ = 1.25, K₂ = 5/3 for p ≥ 5). | 5 | S (three independent quotes agree) |
| T5 | Iwaniec–Kowalski, *Analytic Number Theory*, Lemma 6.3, as quoted by Sofos, arXiv:1602.03140, Lemma 6.1 p. 31, and by Da Silva, arXiv:2604.12697, Lemma 4.1 p. 29 | Beta sieve | Hypothesis: ∏_{w≤p<z}(1−g(p))^{−1} ≤ (log z/log w)^κ(1 + K/log w). Conclusion: Σλ^±_d g(d) = (1 + O(e^{−s}(1 + K/log z)^{10}))∏(1−g(p)), "the implied constant depending only on κ". | **Not explicit**, so it cannot replace FI 6.8. This is what "Lemma 6.3" refers to in the literature. | 5 | S |
| T6 | T. Tao, 254A Notes 4 "Some sieve theory" (blog, 21 Jan 2015), Lemma 17, Cor. 19, Exercise 18 | Beta sieve with crude bounds | Lemma 17: if z = D^{1/s} then Σλ^±_d g(d) = V(z)(1 + O_κ(e^{−s})), assuming V(w) ≪_κ (log z/log w)^κ V(z). Exercise 18 improves this to O(e^{−(1−ε)s log s}). | The proof is half a page and could be made explicit, but T1 already is. Not explicit as stated. | 5 | P |
| T7 | D. R. Heath-Brown, "Lectures on sieves", arXiv:math/0209360: Thm 5.1, Cor. 5.1, "The Fundamental Lemma" p. 38 | Rosser–Iwaniec, κ ≤ 1 | S ≤ XW(z){F(s) + O(e^{−s}(log y)^{−1/3})} + Σ_{d<y}\|R_d\|. FL: S ∼ XW(z) if s → ∞. | Linear sieve only, O-constants; does not cover κ = 2. Not a replacement. | 5 | P |
| T8 | Thorner–Zaman, arXiv:1803.02823, Thm 6.1 p. 18 | Composition of two beta sieves for two independent sequences | If s > 9κ+1+10 log K: the reduced composition ΣΣ_{(d₁,d₂)=1}λ′λ″g′g″ lies between ∏(1−g′−g″)(1 − e^{9κ−s}K^{10}) and ∏(1−g′−g″)(1 + e^{9κ−s}K^{10})². | An alternative way to do Theorem A's pair count: two one-dimensional sieves instead of one sieve of dimension 2. It inherits FI's constants. Low value once T1 is used. | 5 | P |
| T9 | O. Gorodetsky, "A Kubilius model for sieve-theoretic sequences", arXiv:2608.14190 (2026), Prop. 3.1 and Cor. 3.3 (quoting Ford's notes Thm 3.6) | Probabilistic restatement of the FL | P(gcd(R,P(z)) = 1) = ∏(1−g(p))(1 + O(e^{−s log s + s log₃ s + C_{κ,B}s})) + Δ·Σ_{d≤D}\|P(d\|R) − g(d)\| for any N-valued random variable R. | A neat formalism for Theorem A's "random m" language. Not explicit. | 5 | P |
| T10 | C. Pehlivan, arXiv:1504.01550 v2, Lemma 8 (p. 4) | Lattice count (attributed to Matthews, Bull. London Math. Soc. 14 (1982) 149–154) | "Assume that Γ ⊆ Q* is a multiplicative subgroup of rank r ≥ 2 … #{p ∉ Supp Γ : \|Γ_p\| ≤ t} ≪_Γ t^{1+1/r}/log t." No GRH hypothesis; the next result, Theorem 9, is the one that says "Assume the GRH". No proof is given ("implicit in the work of C. R. Matthews"). | Confirms that pool(E) ≪ E^{3/2}/log E is unconditional; C2_ce Lemma 3 proves it in-house. No improvement. | 4 | P (statement); proof U |
| T11 | A. Akbary, S. Yazdani, arXiv:1505.06500, Conj. 1.2 and the Prachar statement, pp. 1–2 | Orders and divisor counts | Conj. 1.2 (Erdős, Arch. Math. 27 (1976) 159–163, for a = 2): E_a(r) = #{p : ord_p(a) = r} ≪_ε r^ε. Prachar (Monatsh. Math. 59 (1955), Satz 2): #{p : (p−1)\|n} ≥ exp(c log n/(log log n)²) for infinitely many n, so ω(a^n−1) is that large infinitely often. | Two-generator analogue: Σ_{d\|n}c(d) = ω(gcd(2^n−1,3^n−1)) ≥ #{p ≥ 5 : (p−1)\|n} for those n, so c-sums are sometimes large. The tail bound needs a c(e) bound weaker than Erdős's conjecture, and none is known. | 4 | P |
| T12 | A. Levin, "Greatest common divisors and Vojta's conjecture for blowups of algebraic tori", Invent. Math. 215(2) (2019) 493–533; Thm 1.1 as quoted by Grieve–Wang, arXiv:1902.09109 p. 1 | Subspace Theorem | For finitely generated Γ ⊂ G_m^r(Q̄) and coprime f, g not both vanishing at 0: for each ε there is a finite union Z of translates of proper algebraic subgroups such that log gcd(f(u),g(u)) < ε·max h(u_i) for u ∈ Γ∖Z. | With f = x−1, g = y−1 and Γ = ⟨2,3⟩²: primes common to Λ-vectors (a,b),(c,d) have total log o(max norm) outside proper-subgroup translates. These exceptions are exactly the parallel-vector pairs, where the lattices share a vector. This is the strongest form of route 4 in LITERATURE §5. Ineffective, so it gives no c(e) bound and no computable alignment bound. | 4 | S (statement via GW); venue S |
| T13 | N. Grieve, J. T.-Y. Wang, "Greatest common divisors with moving targets and consequences for linear recurrence sequences", arXiv:1902.09109; TAMS 373(11) (2020) 8095–8126 (the PDF says "published in TAMS", doi 10.1090/tran/8220); Z. Xiao, arXiv:2110.01751; F. Luca, Monatsh. Math. 146(3) (2005) 239–256 (bibliographic entry in GW) | Moving Subspace Theorem | gcd bounds for pairs of linear recurrences; Xiao extends this to non-simple recurrences. | Same as T12: ineffective. Listed so nobody looks for an effective c(e) bound here. | 4 | P (abstracts); Luca U |
| T14 | N. Hirata-Kohno, M. Kawashima, A. Poëls, Y. Washio, arXiv:2211.14399, Thm 1.1 p. 1; quotes Evertse, Invent. Math. 75 (1984) 561–584, Thm 1 (3·7^m·49^s) and Beukers–Schlickewei (256^{r+1}) | Padé approximation | λx + μy = 1 in S-units of a degree-m field (S includes the archimedean places, s = \|S\|) has at most (3.1 + 5·3.4^m)·45^s solutions. | Fix m and a finite prime set T, and let S = {∞,2,3} ∪ primes(m) ∪ T. Then the cells (k,l) where 2^k3^l·m+1 has **all** its prime factors in T number at most 20.1·45^{3+ω(m)+\|T\|} [PROVED from the cited theorem: −x + y = 1 with x = 2^k3^l·m]. This is an explicit form of APPROACHES C6. A covering only needs one T-factor per cell, so it gives no obstruction. | 8 | P (HKKPW), S (Evertse, B–S) |
| T15 | W. Banks, I. Shparlinski, arXiv:1605.07553 v2 (J. Anal. Math., doi 10.1007/s11854-019-0060-4), §1.1–1.2 | Postnikov plus Korobov, for character sums to moduli with small core | Short-character-sum and L-function bounds for q with a small core; an extended Siegel-zero-free region. The arXiv text says: "We do not improve the Linnik exponent … (see [Chang], [Iwaniec 1974] for the latest results)." A search snippet claiming "L < 2.1115" in the journal version could not be confirmed. | For A = 2^a3^b (core 6) the least prime ≡ 1 mod A is ≤ A^{L}, with L better than Xylouris' 5.2 by Iwaniec (Invent. Math. 23 (1974)) and Chang (U). So every A has some m ≤ A^{L−1} in the image of the map. This says nothing about a given m. | 7 | P (arXiv text); journal claim U; Iwaniec 1974 and Chang U |
| T16 | J. D. Lichtman, arXiv:2211.09641 (abstract) | Primes in APs to large moduli | Infinitely many p with p−1 free of prime factors > p^{0.2844}, improving Baker–Harman's p^{0.2961} (1998). | Concerns y-smooth parts with y = p^θ, not the {2,3}-part. **Not applicable** to "is every m a {2,3}-free part". | 7 | P (abstract) |
| T17 | J. Stadlmann, arXiv:2309.00425 (abstract); A. Mangerel, arXiv:2008.11163 (Forum Math. Sigma 9 (2021) e72) | Level of distribution to smooth moduli | Primes are equidistributed on average over x^δ-smooth (squarefree) moduli up to x^{1/2+1/40−ε}. | The moduli 2^a3^b ≤ x number only O((log x)²) and are not squarefree, so the average has nothing to act on (cf. D_almostall §6). **Not applicable.** | 5 | P (abstracts) |
| T18 | O. Järviniemi, arXiv:1912.02554 and 2106.09813 (abstracts) | Chebotarev/Kummer with GRH | Infinitely many p with prescribed index divisibilities for several groups W_i; orders of algebraic numbers (GRH). | Conditional density statements about generic p; nothing on the exceptional pool (small \|⟨2,3⟩ mod p\|). | 7 | P (abstracts) |
| T19 | P. Moree, "Artin's primitive root conjecture – a survey", arXiv:math/0412262 v2 (Integers 12A (2012) A13 per Pehlivan's bibliography), §"Higher rank Artin", pp. 36–37 | Survey | Cangelmi–Pappalardi: density (GRH) of p with ⟨g₁..g_r⟩ = F_p^×, constant A_r = ∏_q(1 − 1/(q^r(q−1))). Matthews: each g_i a primitive root (GRH). Pappalardi, Konyagin–Pomerance on generating sets. | Index-1 (full group) results only. Nothing on primes with \|⟨2,3⟩\| small, i.e. nothing on c(e). Closes the "two-generator Artin" search. | 7 | P |
| T20 | Searches with no hit (one or two each): image or fibres of p ↦ (p−1)/(2^a3^b); explicit EO constant; almost-primes in k2^n+1 or 2^a3^b+c; Maynard–Tao on exponential sequences; Murty–Rosen–Silverman "Variations on a theme of Romanoff" (venue not confirmed) | — | Nothing beyond APPROACHES A1–A2 and C9 and D_almostall §1. | Untried method 6 stays untried. The closest object is EO79 itself (the image has positive lower density). | 5 | negative search |

---------------------------------------------------------------------------------------------------------------------
## (c) Explicit fundamental lemma candidates

How Theorem A uses the lemma (D_almostall §10.6 and §11.6):
- First moment, κ = 1, lower sieve: E[R] ≥ (1 − η₁)μ.
- Pairs, κ = 2, upper sieve: E[R²] ≤ (1 + η₂)·pairs + (1 + η₁)μ.
- Paley–Zygmund then gives δ ≤ 1 − (1−η₁)²/((1+η₂)ρ). The stratified version uses the same per class.
- The level is D = x^{1−ε} and z = D^{1/s}. Remainders satisfy \|r_d\| ≤ 2^{ω(d)}, and their sum over d ≤ D is o(x/(log x)^{10}).
- Currently η₁ = e^{9−s}K₁^{10} and η₂ = e^{18−s}K₂^{10}, from "FI Lemma 6.3". That is really FI Lemma 6.8 (T4).

What a replacement must give: η₁(s), η₂(s) that are uniform over all pair problems with ρ(p) ∈ {1,2} for p ≥ w, with remainders only over squarefree d ≤ D, d | P(z). An ineffective x₀ is acceptable, since Theorem A is stated for x ≥ x₀.

### c.1 Ford–Halberstam / Ford notes (T1, T2): **can replace FI Lemma 6.8. Recommended.**

Quoted, Ford notes Thm 2.3 (p. 17): "Let A be a sieve problem and assume (g), (r) and (V). Partition the set of primes in [1,z] into P₁ ∪ ⋯ ∪ P_t … and let k₁,…,k_t be non-negative even integers. Then S(A,z) ≤ XV(z)e^E + R′, where E := Σ_{j=1}^t e^{L_j 1_{k_j>0}} L_j^{k_j+1}/(k_j+1)! and R′ := Σ_{d∈P(z), ω((d,P_j))≤k_j (1≤j≤t)} \|r_d\|", with L_j = log(1/V_j) and V_j = ∏_{p∈P_j}(1−g(p)).

Quoted, Thm 3.2 (p. 31), with P_j = {z_{j+1} < p ≤ z_j}: "S(A,z) ≥ XV(z)(1 − E) − R″, where R″ = Σ_{d∈P(z), d ≤ z₁^{k₁+1}z₂^{k₂}⋯z_t^{k_t}} \|r_d\|".

The same inequalities, with e^{L_j} kept for every j, are the Theorem on p. 7 of Ford–Halberstam.

Hypotheses: only (g) 0 ≤ g(p) < 1 and (r) the remainder definition. **No dimension condition and no K.** κ enters only through the size of L_j.

Matching Theorem A:
- **E is increasing in every L_j.** A pair with ρ(p) = 1 at p \| Δ therefore has E no larger than the worst case ρ ≡ 2, and the bound is uniform over pairs.
- The main term is the exact ∏(1 − ρ(p)/p), as D needs.
- Every d in R′ and R″ is ≤ z₁^{k₁+1}∏z_j^{k_j}. If the parameters keep this ≤ D, the remainder is the same O(Σ_{d≤D}2^{ω(d)}) that D already bounds.
- Stratified case: sieve only the primes in [w, z); g(p) = 0 below w contributes L = 0.

### c.2 Numbers [VERIFIED in the stated model; `scratchpad/L3scripts/fh_table.py`]

Model:
- Geometric partition z_j = z^{t_j}, t_j = K^{1−j}, for K in {1.5,…,6}, with up to 150 blocks.
- L_j = κ·log(t_j/t_{j+1}) = κ log K. This is the z → ∞ limit of L_j by Mertens, since every block endpoint tends to ∞ with x.
- Level constraint (k₁+1) + Σ_{j≥2}k_j t_j ≤ s.
- k_j are allocated greedily in steps of 2. Any feasible allocation is a valid sieve, so the values are upper bounds for the best E in this family.
- c = ε = 0.001, s = (r0+1)(1−ε)/(1+c) − 10⁻⁶ (D's convention), ρ = 1.028192 (D's rigorous upper value).

**Control (it fires):** with FI's η's the same script reproduces D's unstratified column exactly: r0 = 22 → 0.5511, 26 → 0.0479, 29 → 0.0285 (D: 0.551, 0.0479, 0.0285).

| r0 | s | η₁ = E(κ=1) | η₂ = e^{E(κ=2)}−1 | δ unstratified (Brun–Hooley) | δ unstratified (FI 6.8) |
|---|---|---|---|---|---|
| 13 | 13.97 | 3.9e-5 | 3.4e-2 | 0.0593 | 0.9999 |
| 15 | 15.97 | 1.1e-6 | 1.4e-2 | 0.0407 | 0.9992 |
| 17 | 17.96 | 3.2e-8 | 7.0e-3 | 0.0342 | 0.9944 |
| 19 | 19.96 | 3.3e-9 | 5.2e-4 | **0.0279** | 0.9600 |
| 22 | 22.95 | 1.9e-11 | 2.1e-4 | 0.0276 | 0.5511 |
| 25 | 25.95 | 8.3e-14 | 4.7e-6 | 0.0274 | 0.0811 |
| 29 | 29.94 | 7.8e-18 | 9.6e-7 | 0.0274 | 0.0285 |
| ∞ | | | | 1 − 1/ρ = 0.02742 | 0.02742 |

The table is not monotone in s (for example s = 15 → 16) because k_j moves in steps of 2. The stratified column (w = 31) could not be recomputed: `D_data/nu_w31.npz` is gitignored and absent. Since η no longer depends on K, it should approach D's limit of 0.57% at about the same r0 (≈ 19–20) [CONJECTURED until rerun]. Owner 5: rerun `D_r0table.py` with `e1 = E1(s)`, `e2 = expm1(E2(s))` from `fh_table.py`.

### c.3 Can it replace Lemma 6.8 in Theorem A?

**Yes, after one written step:** the x → ∞ limit of E for a partition whose bottom blocks have endpoints near the start of the sieve range.
- Ford's own proof of Thm 3.6 handles this. He takes t maximal and lets k_j grow with j; the deep blocks then cost Σk_j t_j → 0 of level and contribute Σ_j L^{k_j+1}e^L/(k_j+1)! → 0.
- For an explicit x₀, use explicit Mertens bounds (Rosser–Schoenfeld) for L_j on the fixed bottom blocks.
- Then Theorem A″ becomes "PROVED modulo floating-point sums". The citation for the sieve is an open primary source with a three-page elementary proof, so the lemma can also be checked in-house, or given to Aristotle.

### c.4 Other candidates

| candidate | explicit? | can it replace FI 6.8 in Theorem A? |
|---|---|---|
| FI Lemma 6.8 itself (T4, S) | yes: 1 ± e^{9κ−s}K^{10}, s ≥ 9κ+1 | It is what Theorem A uses. It stays S unless the book is read. Its K^{10} = 165 (unstratified, κ=2) is what forces r0 = 29. |
| Iwaniec 1980 Thm 1 (T3, P) | main terms F_κ(s), f_κ(s) explicit; error O(·)(log y)^{−1/3} | Yes in the x → ∞ limit, with η₂ = F₂(s) − 1 and η₁ = 1 − f₁(s). This needs a certified numerical solution of the κ = 2 Rosser system (β₂, A₂ from §5). It is more work than c.1 and gives smaller η at small s. |
| Iwaniec 1980 Thm 4 (T3) | no (Q(s) has an O(s)) | No. |
| IK Lemma 6.3 (T5, S) | no | No. |
| Tao Lemma 17 (T6, P) | no (O_κ(e^{−s})) | Not as stated. The proof could be made explicit, but c.1 already is. |
| Heath-Brown lectures (T7, P) | no; κ ≤ 1 | No. |
| HR Thm 2.5 | not found quoted in any open source | U; not needed. |
| Ford notes Thm 3.6 / Gorodetsky (T2, T9) | no | No (use Thms 2.3 and 3.2 instead). |
| Evertse's Leiden chapter, Lemma 10.2.2 (already cited in D §10.3) | no: O(e^{−κ/η}) | No. |

Not used: a full PDF of Iwaniec–Kowalski appears on a university library server (unina2.on-line.it). It is not an open-access publication, so I did not open it.

---------------------------------------------------------------------------------------------------------------------
## (d) Corrections to existing rows

1. **HUB.md N3 and open item 3; D_almostall §0, §10.3, §10.6, §11.5 (i), §11.6 (Theorem A″); LITERATURE.tex row 32 and §6 item 3.**
   - "Friedlander–Iwaniec, *Opera de Cribro*, Lemma 6.3 (error e^{9κ−s}K^{10})" → **Lemma 6.8**, per Matomäki–Teräväinen Lemma 9.1, Thorner–Zaman Lemma 6.2 and Grimmelt Lemma 2.4.
   - "Lemma 6.3" is Iwaniec–Kowalski's number, and IK 6.3 is not explicit (T5).
   - Upgrade the flag on the FI statement from U to S.
   - Add Ford–Halberstam as the open, explicit replacement (T1, T2, §(c)).
2. **D_almostall §11.4** says "only the fundamental-lemma range s ≳ 22 delivers relative errors below 10⁻²". That is an artefact of FI's K^{10}. With Brun–Hooley, η₂ < 10⁻² already at s ≈ 17 (κ = 2) in the limit model (§(c).2).
3. **LITERATURE.tex row 25, L_literature L14(d), L18.** "Hernández–Luca ('Common factors of shifted S-units')" is the wrong title. The paper GW cite is S. Hernández, F. Luca, "On the largest prime factor of (ab+1)(ac+1)(bc+1)", Bol. Soc. Mat. Mexicana (3) 9 (2003) 235–244 (S, from Grieve–Wang's bibliography).
4. **LITERATURE.tex row 28 (Pehlivan).** Lemma 8 is stated with no GRH hypothesis (P, p. 4; the GRH result there is Theorem 9). Change "lemma S" to "statement P, no proof in the paper; attributed to Matthews, Bull. LMS 14 (1982) 149–154 (S)".
5. **LITERATURE.tex row 27 (Akbary–Yazdani).**
   - The conjecture statement was re-read today: P.
   - Erdős's source is Arch. Math. (Basel) 27 (1976) 159–163.
   - Erdős–Murty is CRM Proc. Lecture Notes 19 (1999) 87–97 (S, from A–Y's bibliography). This also fixes the venue for row 29.
6. **APPROACHES.md C1 / LITERATURE row 31 (Linnik).** For moduli 2^a3^b (core 6), the relevant improvements of the Linnik exponent are for small-core moduli: Iwaniec 1974 and Chang, as named by Banks–Shparlinski (U). Banks–Shparlinski themselves say they do not improve the Linnik exponent. The bearing is unchanged.
7. **APPROACHES.md C6 (Evertse).** It can now be stated quantitatively, via Hirata-Kohno et al. Thm 1.1: at most 20.1·45^{3+ω(m)+\|T\|} cells have 2^k3^l·m+1 composed only of primes in T (T14). This is still not an obstruction.
8. **LITERATURE.tex §5 item 6** (untried method 6): mark it "searched 2026-11-03, no result on the image or fibres beyond EO79/Sun–Fang/Chen; adjacent results (T15, T16) are about different objects". It stays untried as a method. Item 2 (Maynard–Tao): no application to exponential sequences found; D_almostall §1 stands.
9. Nothing in this slice changes Y1–Y7, N1, N2, N4, N5 or C1–C3.

Sources opened today, all saved under `scratchpad/L3dl/`: arXiv 1803.02823, 1809.10008, 2301.07679, 1602.03140, 2604.12697, math/0209360, 2607.05707 (Friedlander 2026: a cancellation property of sieve weights in short intervals, not a fundamental lemma), 2410.07184 (Selberg upper bound only, not relevant), 2608.14190, 2304.04805, 1504.01550, math/0412262, 1505.06500, 1902.09109, 2211.14399, 1605.07553. Also the Ford–Halberstam PDF, Ford's 2023 notes, Evertse's Leiden chapter, Tao's Notes 4 (HTML), and Iwaniec's Acta Arith. 36 scan (matwbn, sheets 1–4 and 12 read).

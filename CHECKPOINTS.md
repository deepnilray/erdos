# CHECKPOINTS — master index of all research done for Deepnil Ray

Branch `claude/all-checkpoints` of `deepnilray/erdos`. Written 2026-11-10. This file lists every problem that has
already been worked on, what is established, where the files are, and the next attack. Read the entry for a problem
before touching it. If a problem has an entry here, RESUME from its checkpoint; do not redo it, and do not
re-derive results listed as PROVED or VERIFIED. Check the dead-idea lists before trying any approach.

Labels used throughout: PROVED (closed symbolically), VERIFIED (computation within a stated bound, with a control),
CONJECTURED (evidence only). Sources for each entry are named, because some entries come from earlier chat summaries
and personal notes rather than from files, and have not been re-verified in this branch.

## 0. How the work is laid out

| Folder in this branch | Problem | Origin branch |
|---|---|---|
| `erdos242/` | Erdős–Straus (Erdős #242) | `claude/erdos-straus` |
| `andrica/` | Andrica's conjecture, sums of large prime gaps | `claude/andrica-state` |
| `e203/` | Erdős #203 | `claude/open-conjecture-search-h6tgg3` |
| `e455/` | Erdős #455 | default branch `claude/nifty-allen-xcvku4` |
| `minmod/` | Fonollosa's minimum-modulus conjecture (arXiv:2607.08366) | `claude/fonollosa-min-modulus` |

The root `README.md` is the September triage log from the default branch (verdict EMPTY at that date).
Everything else below is listed with its location, which is sometimes Google Drive or an earlier chat, not this repo.

Working rules the user wants kept: every claim labelled PROVED/VERIFIED/CONJECTURED with bounds; every automated check
has a planted-failure control that fires; verdict first and worst news first; prior-art search on the mathematical
object before any derivation; forecast before computing; no numeric success probabilities; pre-send check before
anything leaves (citations and attributions verified against the primary source).

## 1. Erdős–Straus, Erdős #242 (4/n = 1/x + 1/y + 1/z) — folder `erdos242/`
Status 2026-11-08: OPEN. Source: files in this folder (`es_research_log.md`, `erdos_straus_family.pdf`).
- PROVED Theorem A: if p = mut − m − u with mt ≡ 1 (mod 4), w = (mt−1)/4, X = ut−1, then 4/p = 1/(uw) + 1/(pwX) + 1/(uwX).
- PROVED Proposition B: a prime p ≡ 1 (mod 4) lies in this family iff there is t ≡ 3 (mod 4) and a divisor a of pt+1 with 4 | a and a ≡ −1 (mod t).
- PROVED: u = 1 is Obláth's criterion; the divisor choice e = x² never works; no finite set of (t, m) pairs covers all primes (sub-agent derivation, spot-checked); for p ≡ 1 (mod 8), t = 3 works iff (3p+1)/4 has a prime factor ≡ 2 (mod 3).
- VERIFIED: every prime in the six open Mordell classes below 2·10^7 (39391 primes) is in the family (u up to 890, worst p = 5101441); independent t-search below 2·10^6 (4519 primes, t ≤ 367, worst p = 830041); random samples of 40 hard primes at each of 12, 15, 18 digits.
- NOT the same representation as Chamberland's p = qr − 4 s1 s2 (VERIFIED on primes below 400); whether the covering statements are equivalent is unknown.
- GAP: show that for every prime p ≡ 1 (mod 4) some t works, which needs sieve or primes-in-progressions control of the factorization of pt+1. Lean formalization of Theorem A not done (installer was denied by the permission system).
- Next attack: sieve over u/t for the factorization of pt+1; test equivalence with Chamberland's Prime Representation Conjecture.

## 2. Andrica's conjecture and sums of large prime gaps — folder `andrica/`
Status 2026-10-11: Andrica itself OPEN. Source: `andrica/STATE.md` (read), `andrica_gaps.tex/.pdf`, `andrica_master_log.md`.
- Main result (audited, recomputed from scratch, per STATE.md): sum of prime gaps ≥ x^{1/2} in [x, 2x] is ≪ x^{0.5575+ε}; Andrica failures up to X number ≪ X^{0.0575+ε}; Legendre exceptions ≪ N^{0.115+ε}. This improves Järviniemi's x^{0.57+ε} (arXiv:2212.10965, Theorem 1.1; Järviniemi's paper does not mention Andrica, so the Andrica count is a corollary).
- Total sieve loss at r = 0.0575: 0.99154810 (sieveZ, runN.sh, table `T400_0575M.txt`); r = 0.057 fails (partial 1.00221). Control: `sieve3 0.07 0 0 0.5` gives 0.99027345.
- Barrier theorem (Section 7, `beurling.tex`): a Beurling system with RH-quality behaviour violates Andrica, so RH-quality analytic input alone cannot prove Andrica. Conditional: a single-scale fourth-moment bound for ψ in intervals of length √X implies Andrica.
- Dead routes and exact obstructions: `andrica_master_log.md`. A 4 Nov 2025 withdrawn claim (Wang, arXiv:2510.17065) was checked in an earlier session: do not cite it as a result.
- Next: submit the paper; the exponent is likely improvable by further optimization in the Heath-Brown/Harman framework with the Guth–Maynard large-values input (arXiv:2405.20552).

## 3. Erdős #203 (m coprime to 6 with 2^k·3^l·m+1 always composite, k, l ≥ 1) — folder `e203/`
Status 2026-10-30: OPEN. Source: `e203/HUB.md` is the single source of truth (results table, withdrawn claims, run log, Aristotle prompt index). Read it in full before any work.
- Verdict recorded in `VERDICT.md`: NO is more likely (CONJECTURED).
- PROVED: no covering uses only primes with e_p ≤ 8·10^5 (B = 0.742445, exact rational); mixed certificates with e_p ≤ 8·10^5 are excluded; every covering needs at least 14082 primes with e_p > 8·10^5 (Theorem Z, B′ = 0.784180).
- VERIFIED: every m ≤ 10^10 coprime to 6 has a prime 2^k3^l·m+1 with k, l ≥ 1 (hardest m = 6257518159).
- PROVED conditionally: Theorem A (all but 2.0% of m have a cell with at most 22 prime factors), conditional on the explicit form of Friedlander–Iwaniec, Opera de Cribro, Lemma 6.3, which was never opened.
- Open items: read Opera de Cribro Lemma 6.3 to make Theorem A unconditional; write the #203 paper (.tex + PDF); a bound on c(e) = #{p : e_p = e} is the missing input for "no covering at any size".
- Withdrawn claims listed in HUB.md must not be reused.

## 4. Erdős #455 (convex chains of primes, q_n/n^2 → ∞) — folder `e455/`
Status (state 2026-09-28): OPEN. Source: `e455/PROGRESS.md` (read), scripts `kappa.c`, `cyc.py`, `quad_check.py`.
- PROVED: reduction R1 (suffices that the number of gaps d_k ≤ x is o(x)); cap C1 (for every y there is a y-rough convex quadratic chain, so fixed-prime arguments give at most liminf q_n/n² ≥ 1); constant or periodic curvature chains cannot stay below Cn² (Linnik–Vinogradov).
- VERIFIED: κ(5) = 30/21, κ(7) = 210/157, κ(11) ≈ 1.45; exact DP for N ≤ 1.024·10^6 with N/len² increasing.
- Dead ideas D1 to D22 are listed in `PROGRESS.md`. Open: show chains with arbitrary non-periodic curvature pay unbounded average curvature. Literature: Richter 1976 only gives liminf ≥ 0.352 (as recorded there).

## 4b. Fonollosa's minimum-modulus conjecture (unique multiset sums in Z_N) — folder `minmod/`
Status 2026-11-10: OPEN (verdict of the run: PARTIAL). Source: `minmod/minmod.tex/.pdf`, `minmod/NOTES.md` (candidate list, forecast, dead ideas), logs in `minmod/logs/`.
Statement (arXiv:2607.08366, Conjecture 1): a set A of n residues mod N is valid if the only size-n multiset from A with sum ΣA is A itself; conjecture: valid ⇒ N ≥ 2^n − 2^⌊log2 n⌋.
- PROVED: sign characterization (valid ⇔ every nonzero sum-zero relation vector has an entry ≥ 2 and an entry ≤ −2); heredity; affine invariance.
- PROVED: cyclic-order lemma (pair a, c; subsets S ≠ S' of the rest, |S'| ≥ |S|; if x_S' − x_S = i(a−c) then i ∉ [−1, |S'|−|S|+1]).
- PROVED: 1D bound N ≥ 5·2^(m−1) for m ≤ 3 (so N ≥ 5·2^(n−3) for n ≤ 5 with a unit difference); gap bound g_j ≥ 2n*_j + ascent; alternation criterion.
- NOT DONE: the independent adversarial check of the paper was cut off by a usage limit; only self-checks and the listed controls were run.
- PROVED: if some difference is a unit (e.g. N prime), N ≥ 2^(n−1) + n − 2; if moreover A contains 3a−2c, 4a−3c, 3c−2a or 4c−3a, N ≥ 5·2^(n−3).
- VERIFIED (exhaustive search `enum3.c`, all 2^(n−1) ≤ N < 2^n, n ≤ 8; controls in paper §5.1): valid n-sets exist exactly at N = 2^n − 2^k with 2^k ≤ n. So the conjecture holds for n = 8 (the author had certificates for n ≤ 7).
- VERIFIED: sporadic valid class {0,1,3,10} mod 15; AAD (all-anchor dissociated) sets have the same moduli for n ≤ 6 but exist at N = 120 for n = 7; 1D structure minimum 5·2^(m−1) for m ≤ 5.
- CONJECTURED: N < 2^n and valid ⇒ N | 2^n − 2^k with 2^k ≤ n; every 1D structure has N ≥ 5·2^(m−1).
- Dead ideas: ten, listed in `minmod/NOTES.md` (clique/LP bounds capped at 2^(n−1) by (Z_2)^(n−1); two-cube unions; virtual anchor; Parseval/cyclotomic identities; AAD reduction; parity induction; doubling the smallest element; halving along a generator).
- Next attack: prove the 1D bound via an LP-dual certificate; add the relation vectors with two entries ±2; extend the search to n = 9; Lean formalization of the proposition and lemma.

## 5. Work whose files are NOT in this repo
These come from memory notes and earlier chat summaries (not re-verified here). Locate the files before resuming.

### Google Drive (account deepnil.ray_ug2025@ashoka.edu.in), folder `projecteuclid` (folder id 1nc9GkzyQ16KYHUUf7NXSpwyn720j8hho)
Subfolders: `erd249`, `erd454`, `gilbearth`, `giuga`, `lehmar` (empty), `unfair0-1`, `rumoursequenceconjecture`, `corrected`, `best one`. Most contain Aristotle (Harmonic) Lean output archives (`*.tar.gz`) from 5 Aug 2026. Four Erdős formalizations (#287, #389, #699, #727) are in an Aristotle archive; per an earlier chat each has a faithful Lean statement and partial results with no `sorry`. These archives have not been opened in the current work.

### Erdős #249 (irrationality of Σ φ(n)/2^n)
Drive folder `erd249` (report `Erdoes249_Irrationality_Attempt.pdf`, Lean file `Main.lean`). Chat findings (Aug 2026): the Möbius–Lambert reformulation is already in OEIS A256936 (credited to Amiram Eldar, March 2026); the denominator-growth obstruction (Section 5.2, primitive prime divisors) appeared unpublished. Open.

### Erdős #39 (dense infinite Sidon sets) — memory note `/areas/erdos-39`
Open. Best known exponent √2−1 (Ruzsa 1998; Cilleruelo, Adv. Math. 255, 2014). Many dead ideas recorded (random digits, field towers capped at 1/3, Bruck's subplane theorem blocks exact planar towers). Live frontier: near-planar nested Sidon sets. Next: test whether control of near-collisions p1·p2 ≈ p3·p4 over structured prime subsets beats the random model.

### Erdős #1110 (representable sums of p^k q^l antichains) — earlier chat
Per chat summary: positive lower density proved by computer-assisted average-reward MDP certificates for the pairs (5,2), (7,2), (4,3), with exact 128-bit checks and controls; the pairs (9,2) and (5,3) are unresolved (finite lookahead exhausted). Files not located in this repo.

### Erdős–Rado sunflower conjecture
Open. Attack record dated 23 Sept 2026: shifting route via Mishra (arXiv:2606.02667), trace-class reduction for s = 3, 2-of-3 reformulation, retracted counterexample to a compression lemma. A later session found a gap in Fukuyama's claimed proof (arXiv:2212.13609v3), Case 3 of Lemma 2.1, and wrote a draft note showing an incompatibility between two lemmas (not a disproof of the conjecture); files not located.

### Unfair 0–1 polynomial conjecture (Letac, Green Problem 28)
Open. Drive folder `unfair0-1`, consolidated record `unfair_fractional_propagation` (not located in this repo).

### Gilbreath / SpikeBound
Computer-assisted proof of SpikeBound(4) with two independent certificates; c_4 ≤ 2 as a partial answer to an open question in Chase–Hunter–Tao (arXiv:2607.08712). Drive folder `gilbearth` (Lean file `Gilbreath.lean`, Aristotle archive). Output files `spikebound4-result.md`, `certificate_k4.py`, `planes_k4.json` were produced in a chat session and are not in this repo.

### Stanley's conjectures (Fibonacci-type and k-bonacci products)
Papers: Conjecture 4.2 (SSRN 7499163) and Conjecture 6.3 (SSRN 7502439) posted; Conjecture 5.1 paper drafted and submitted; the ω(n) paper ("The Ekhad–Zeilberger sequence ω(n) is not D-finite", OEIS A385082) finished; papers on Conjectures 5.4/5.5 and 6.2 drafted, not posted (as of Oct 2026). Zeilberger replied to an email with congratulations. Known soft spots for expert review: Section 3 local limit theorems and Section 7 weak convergence in the ω(n) paper.

### OEIS conjectures
Proofs of many OEIS recurrence and characterization conjectures, including a paper "Proofs of eighteen conjectures from the OEIS" (Sept 2026 chat) and Mathar-corpus proofs (A186185, A186184, others). Christoph Koutschan declined an arXiv endorsement, noting the results follow from standard methods (Zeilberger/creative telescoping; algebraic ⇒ D-finite ⇒ P-recursive). Two reference errors flagged by him (wrong title for arXiv:2303.02793; unsupported attribution to Fried) came from copying reference lists; always verify against primary sources.

### Matrix divisibility paper
"How Divisible Are the Powers of an Integer Matrix?", submission package for Linear and Multilinear Algebra (earlier AMM rejection on exposition grounds).

### Principia Math Fall 2026 competition
Owner of the Chebyshev product project (MathDB 377007), entered solo; wants all five stages at top quality and every open task finished. State not in this repo.

### Exploratory / literature items with no further file
Erdős #454 (Pomerance 1979 partial result, numerical check to n = 20000), #413 (open; Tao–Teräväinen and Lau, arXiv:2604.15042, for large k), Giuga and Lehmer folders on Drive (one Aristotle archive; Lehmer folder empty).

### Astronomy (separate from the math)
Repos `deepnilray/SearchChev` and `deepnilray/varwise` (VarWISE × Gaia × ZTF variable-star search); see the winter discovery plan in memory.

## 6. Known literature facts (verified in the sessions noted; recheck before citing)
- erdosproblems.com/242 listed as open with no AI results on 2026-11-08.
- Lonely runner conjecture proved for up to 13 runners as of April 2026 (Trakulthongchai–Sungkawichai, arXiv:2604.23906), building on Rosenfeld (arXiv:2512.01912); general case open.
- Guth–Maynard, arXiv:2405.20552 (zero-density estimate N(σ,T) ≤ T^{30(1−σ)/13+o(1)}).
- Bright–Loughran, arXiv:1908.02526: no Brauer–Manin obstruction for Erdős–Straus surfaces.

## 7. Suggested protocol for a new run
1. Read this file; if the chosen problem is listed, read its folder or note and continue from "Next attack".
2. If the problem is not listed, run the prior-art gate (search the mathematical object, read the primary source), forecast, then attack.
3. After each session append a dated entry to this file (status, new PROVED/VERIFIED/CONJECTURED items with bounds, dead ideas, next attack) and commit it, so no later run repeats the work.

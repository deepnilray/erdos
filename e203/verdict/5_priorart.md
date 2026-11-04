# Agent 5 — prior art, status, red team (Erdős #203), 2026-10-10

## 1. Status (primary sources fetched today)
- erdosproblems.com/203, exact wording: "Is there an integer m≥1 with (m,6)=1 such that none of 2^k3^ℓm+1 are prime,
  for any k,ℓ≥0?"  Source [ErGr80, p.27] = P. Erdős, R. L. Graham, *Old and new problems and results in combinatorial
  number theory*, Monographie No. 28 de L'Enseignement Mathématique, Genève 1980, 128 pp. (Zbl 434.10001 checked).
  The text of p.27 itself was not available online, so I could not read it.
- The page was last edited 20 Jan 2026. Comments 15, proof claims 0, proof expositions 0. Banner: "The ability to post new comments has been
  suspended." The page HTML shows no status colour (id=neutral). teorth/erdosproblems data/problems.yaml gives
  status **open** (last_update 2025-08-31). Formal Conjectures 203.lean has `@[category research open]`, with
  `answer(sorry) ↔ ∃ m, m.Coprime 6 ∧ ∀ k l, ¬(2^k*3^l*m+1).Prime`.
- Forum thread /forum/thread/203: all 15 posts are read (post ids 229…9048). The newest is veljjanoski, 15 Sep 2026.
  **There are no comments after 2026-09-27, no proof claim, and no claimed solution.** Other posts: AnimishSharma (21 Jun 2026)
  gives the density criterion and the exclusion lcm<5040 for p≤5e7. He also checks that 2·3²·78557+1=1414027 is prime, which I re-verified. Dogmachine and uona
  give heuristic sizes ≥1e10. emil467q found no m in [1e10,1e11]. Tao (19 Oct 2025) says LLMs found no references; on 29 Dec 2025 he
  notes that the q≡1 (4) variant has the trivial answer m=1. Woett cites the Filaseta–Finch–Kozek (FFK) conjecture and theorem. Bloom does housekeeping and split off #1113.
- History: the 2025-10-20 revision had a garbled remark ("probably no … Fermat primes"). That remark concerned the 1-D
  "covering not responsible" question. It now lives in #1113, which says Erdős–Graham thought **yes** (Sierpiński numbers
  without coverings exist), since otherwise there would be infinitely many Fermat primes.
- GitHub: veljjanoski/erdos203 (cloned). The last commit, 2026-09-28, regenerated the primes_full pools. Its status is "Not resolved".
  Neo7672/erdos-203-covering-search now returns **404 / not readable** (deleted or private). I could not re-verify it.
  The trureturing issue #9414 body was not retrievable (proxy, JS page).
- Web and arXiv searches found no paper on the 2-base {2,3} problem. **Not solved either way** [VERIFIED as of 2026-10-10].

## 2. Expert expectation
- No stated expectation by Erdős–Graham for #203 is recorded on the site, and I could not access p.27. Site reactions: Dogmachine says "looks
  difficult". uona's intuition is that m "shouldn't exist". Tao and Bloom made no mathematical prediction on #203.
- Related results (citations checked): FFK, *On powers associated with Sierpiński numbers, Riesel numbers and Polignac's
  conjecture*, J. Number Theory 128 (2008) 1916–1940, conjecture that every Sierpiński number is a perfect power or has a covering.
  A. S. Izotov, *A note on Sierpinski numbers*, Fibonacci Quart. 33(3) (1995) 206ff. #204 is solved NO (Adenwalla). #276 is
  "conjecturally solved" (Ismailescu–Son). #202 is solved.
- My assessment [CONJECTURED]: **NO is more probable, about 75–80%.**
  - Without a certificate, a prime-free 2-parameter family is heuristically impossible: the expected number of primes diverges, like
    Σ_{k,l} 1/(k+l).
  - Certificates (pure or mixed) are excluded for e_p ≤ 4e5 with a large margin (0.73 / 0.95), and the bound rises only about 0.015 per doubling.
  - The 2-D lattices do not nest.
  - YES remains possible only through primes of huge e_p, and Σ1/e_p does diverge. NO is far beyond current methods (it is the Sierpiński barrier), so the problem will likely stay open.

## 3. Red team (independent scripts in agents5/rt/, no repo code used)
- e_p and lattice: 20 random pool primes (4 above 1e8). I recomputed ord_p2, ord_p3 and e=lcm, built a generator h=2^s3^t with h^α=2,
  h^β=3 and ord h=e, and brute-tested the kernel. **20/20 OK.**
- Pool completeness: every prime 5≤p<2e6. **0 missing, 0 extra, 0 wrong e.** gcd(2^e−1,3^e−1) certificate for 6 values of e
  (including 360360 and 388080): the residual is 1 in every case.
- 6-core optimum: exhaustive search over (ℤ/144)² with arbitrary offsets gives **11080/20736 = 2770/5184** exactly.
- R3 (MIXED §4): brute-force reachable sets over all units M and every gcd(g,144) with 3|g. Light mass 0.0485017 (34
  primes) gives λ′=0.1040572 and **R3 = 250822656/3288415339**, the identical fraction, attained at g~3 (also at g~9).
- S = Σ_{5≤q≤4e5} q⁻²/(1−δ_q) = 0.1463795 matches.
- Capelli (Lang, Algebra, VI §9, Thm 9.1: X^n−a is irreducible if a∉K^p for all p|n and a∉−4K⁴ when 4|n). With a=−1/c,
  reducibility happens iff c∈ℚ^q for an odd q|d, or 4|d and c∈4ℚ⁴. This is correct. An independent sympy test (4320 cases, 87 reducible)
  gave 0 mismatches.
- Scope logic: "p | value" ⊇ "value = p", so the exclusion is conservative. m < max p is irrelevant for exclusion. The uncovered
  set is Nℤ²-periodic, so ℤ² vs ℕ² and the primes 2|value at k=0 and 3 on l=0 do not matter, because one can take k,l≥1.
  *Wording nit:* the theorem says k,l≥0 with p∤6. It should note this periodicity, or say k,l≥1. Alg(m) needs g = the maximal
  exponent. This is harmless because all q≥5 are summed unconditionally and both 3|g and 3∤g are bounded.
- Augmentation lemma: valid once primes with p|M (empty A_p) are dropped first.
- **No flaw found.** Unverified: the "x^{1/30}" claim attributed to Cangelmi–Pappalardi. The paper is L. Cangelmi, F. Pappalardi, "On the r-rank Artin conjecture
  II", J. Number Theory 75 (1999) 120–132, and its bibliographic data is correct, but I did not read its content. BBMST is correct: Invent. Math. 228 (2022) 377–414.
- Minor TARGET.md discrepancy: the site now says "last edited 20 January 2026". TARGET.md mentions only the 2025-10-20 history entry.

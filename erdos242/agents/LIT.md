# LIT agent report (2026-11-08). Labels: VERIFIED-SOURCE = I read the text (E-T PDF extracted via pypdf; arXiv abstract pages); UNVERIFIED-SOURCE = search snippet/summary/memory.

## 1. Elsholtz–Tao arXiv 1107.1010 (VERIFIED-SOURCE, full PDF text extracted)
- Defs: "Type I solution if n divides x but is coprime to y,z, and a Type II solution if n divides y,z but is coprime to x."
- Prop 1.6: "For any odd perfect square n, we have fI(n)=fII(n)=0." (Schinzel, Yamamoto; quadratic reciprocity.)
- Thm 1.1: sum_{n<=N} fI, fII << N log^3 N (and >>); sum_{p<=N} fI(p) in [N log^2 N, N log^2 N loglog N]; sum_{p<=N} fII(p) << N log^2 N (lower bound also; check text). Exceptional set: they cite Vaughan [82]: #{n<N: f(n)=0} <= N exp(-c log^{2/3} N). Not an everywhere statement.
- Prop 2.2/2.3 (Type I): equivalent: (i) exist a,b,e with e|a+b and 4ab | ne+1; (ii) 4abcd = na+nb+c, c coprime to n; (iii) ne+1=4ad(ce-a); (iv) **n = 4acd - f with f | 4a^2 d + 1, c coprime to n [credited to Nakayama, Tohoku Math J. 46]**; (v) ne=(4bcde-1)-4b^2 d.
- Prop 2.6/2.7 (Type II): (i) a,b,e, e|a+b, 4ab | n+e, (n+e)/4 coprime to n; (ii) 4abcd=a+b+nc; (iii) **n=(4acd-1)e-4a^2 d** with (n+e)/4 coprime to n [Rosati]; (iv) n=4ad(ce-a)-e. (This is Chamberland's form up to renaming.)
- Prop 1.9 (polynomial-solvable residue classes): Type I classes: n = -f mod 4ad, f|4a^2d+1; {n=-f mod 4ac}∩{n=-c/a mod f} (Yamamoto); {n=-f mod 4cd}∩{n^2=-4c^2 d mod f}; n=-1/e mod 4ab, e|a+b. Type II: -e mod 4ab; -4a^2d mod f with 4ad|f+1; -4a^2d-e mod 4ade. Only finitely many classes per solution => this is exactly "union of residue classes with growing moduli", no covering claim.
- Relation Type I <-> II: NOTHING found. Nothing gives "one exists when the other fails". Only (1.2) f>=3fI+3fII, and remark f(n)>>N log^6 N on average (Heath-Brown) so most composite solutions are neither type.
- PRIORITY: our Thm A / forms (a),(b),(c) are equivalent to the Nakayama/Yamamoto/Aigner families in E–T Prop 2.3 and 1.9 (n = 4acd - f, f|4a^2 d+1 <-> our k,l,t form with relabelling; I did NOT check the explicit variable dictionary—CONJECTURED identification, needs a 10-minute check). Treat the family as KNOWN (as a parametrisation); novelty can only be in Props C/D/E (Jacobi constraint, squares), the surface S_n viewpoint, and combined-coverage data. Note E–T's own Σ^I_n is a 3-dim variety mapping to S_n: xyz-type surface — cf. our (d).

## 2. Analogous "everywhere except explicit sparse set" results (ALL UNVERIFIED-SOURCE, from memory unless noted)
- Gauss–Legendre three squares: n is sum of 3 squares iff n != 4^a(8b+7). Technique: local conditions + class number one in genus (Hasse–Minkowski + indefinite/class-number-1 genus of x^2+y^2+z^2). Needs: single-class genus. Everywhere-statement because genus = class.
- Duke–Schulze-Pillot: ternary form, every sufficiently large n locally represented with bounded divisibility at anisotropic primes is represented, EXCEPT finitely many spinor-exceptional square classes t*m^2. Ineffective (Siegel/Duke). Hypothesis: primitive local rep + n large. Gives "all large n outside finite set of square-classes" – note: exceptions are square-class-shaped, reminiscent of our odd-square obstruction. For E–S the quadric/cubic is not a quadratic form, so does not apply directly.
- Sums of three cubes: Brauer–Manin obstruction mod 9 only; no everywhere theorem (open for 33, 42 resolved computationally only). Lesson: for cubic surfaces everywhere-statements are not known by any technique.
- Bright–Loughran, "Brauer–Manin obstruction for Erdős–Straus surfaces", arXiv:1908.02526, Bull. LMS 52 (2020) 746–761 (search-snippet): no BM obstruction to existence of natural-number solutions; obstruction to strong approximation exists at p-adic places. Consistent with BRIEF.
- Loughran–Mitankin arXiv 1807.10223 (Markoff-type, integral points; BM-explained failures density zero). Ghosh–Sarnak "Integral points on Markoff type cubic surfaces" (Invent. 2022, from memory): local-global holds for almost all n, but there are infinitely many failures not explained by BM; their numerics predict ~ N^{1/2} sparse set of failures. Colliot-Thélène–Wei–Xu "Brauer–Manin obstruction for Markoff surfaces" (Ann. Sc. Norm. Pisa 2020) – shows BM explains some failures. Relevance: genuinely says an integral-point everywhere-statement for xyz-type cubic surfaces is FALSE in the integral Markoff case (non-BM failures exist). Our S_n is different (ours have all positive integer args + only squares fail empirically), but this is a warning, and dead-idea D13 is consistent.
- Derenthal–Frei / Derenthal–Loughran: Manin-type asymptotics for rational points (and some integral points) on singular cubic surfaces; I found no paper on integral points on the A2+2A1 cubic in my searches (UNVERIFIED; a search suggested only 2A2+A1 (Le Boudec), E6 (Derenthal–Frei), not A2+2A1). Technique = universal torsor + divisor-sum counting; yields asymptotics in n (counting points of height <=B for fixed n via torsors are NOT what is needed) — gives density/average, never everywhere.
- Takeaway: an everywhere-statement needs either (a) class-number-one / genus=class phenomenon (quadratic forms), or (b) an explicit identity covering every class. For cubic surfaces S_n no known technique; hypothesis for (a) is a quadratic structure. Possible quadratic hook: for fixed t,k, (tk-1)(tl-1)=pt+1 is a divisor problem in Z[ ], i.e. norm form of split torus; for Type II, 4abcd=a+b+nc is a bilinear/Pell-like form. NOT verified to reduce to a ternary lattice.

## 3. 2024–2026 claims
- Bradford, "A Solution to the Straus-Erdős Conjecture", arXiv:2602.11774 (v1, 12 Feb 2026, math.NT, VERIFIED-SOURCE abstract page): abstract "outlines a solution"; no journal reference. Third-party audits (search snippets, UNVERIFIED-SOURCE, one from an AI-generated log page): identities valid, global covering step missing. erdosproblems.com forum: "claimed" by Bradford, problem still open (UNVERIFIED-SOURCE; direct fetch 403). I did NOT read the paper body.
- Mihnea–Dumitru (Bogdan), arXiv:2509.00128 (VERIFIED-SOURCE abstract): "empirical evidence ... improving computational bounds to 10^18 and ... evaluating f(p)". Computational only, preprint.
- Mballa, arXiv:2602.20036 v2 (VERIFIED-SOURCE abstract): unified parametric approach; density-one set of integers; n≡1 mod 4 via a divisor b≡3 mod 4 (this is Obláth/l=1 case); exceptions density zero. Not a proof; unrefereed.
- Cambridge Open Engage preprints "The Erdős–Straus Conjecture: Modulo 24 Obstructions and the Constant Residual Constraint" (two versions, 2026; UNVERIFIED-SOURCE snippet): claims an "absolute residual constant" bounds solutions / resolves mod-24 obstruction. Unrefereed, no endorsement found. Not read.
- Others from snippets (UNVERIFIED): Bello-Hernández et al arXiv:2606.10922 (divisor parametrisation, reproduces known types); Dyachenko arXiv:2511.07465 (reportedly flawed lattice step). Chamberland INTEGERS 26 A42 (refereed; PDF fetch failed here, rely on lead's reading).
- erdosproblems.com forum comment (snippet): a "full CRT coverage for n≡529 mod 840" argument was rebutted as only checking small n and appealing to periodicity.
- No accepted proof found as of this date.

## 4. Priority on our family (see §1)
Family = Nakayama (1939/Tohoku 46) n=4acd-f, f|4a^2d+1; Yamamoto (Kyushu) classes; Aigner/Rosati/Mordell variants, all catalogued in E–T Prop 2.3/1.9 and Mordell's book. Our (tk-1)(tl-1)=pt+1 and 'kl | p+k+l' are re-parametrisations. What I found NOT in E–T: Jacobi-symbol constraint (Prop C) beyond odd-square vanishing (Prop 1.6), the union-with-Type-II conjecture (C*), data on V. Honest statement: do not claim the family; claim Props C/D/E and C* only after checking against Mordell Ch. 26 / Yamamoto 1965 (not read).

## 5. Covering systems with growing moduli
Nothing found. E–T Prop 1.9 states each polynomial solution gives finitely many classes and the real covering would need infinitely many; Vaughan's N exp(-c log^{2/3}N) exceptional bound is the best sieve-type result. Forum thread: attempts at finite CRT covering rebutted. No literature on infinite-modulus coverings of non-squares for E–S.

## 6. Ranked leads
1. Elsholtz–Tao §2 Σ^I_n/Σ^II_n parametrisations (arXiv 1107.1010): both types are N-points of the same surface S_n; look for a birational correspondence/automorphism group action (our C*).
2. Bright–Loughran 1908.02526: confirms no BM obstruction; check whether their Brauer-group computation exhibits the odd-square obstruction as an algebraic (non-BM) failure of strong approximation.
3. Ghosh–Sarnak / Colliot-Thélène–Wei–Xu: framework for what "sparse exceptional set" looks like; warns non-BM failures exist.
4. Duke–Schulze-Pillot spinor exceptions: model for exceptional set = square classes.
5. Vaughan 1970 Mathematika 17: best exceptional-set bound; method may adapt to Type I∪Type II.
6. Chamberland INTEGERS 26 A42: exact Type II criterion enabling union attack.
7. Loughran–Mitankin 1807.10223: thin-set / BM counting.
8. Derenthal–Frei torsor method: only for asymptotics.
9. Mballa 2602.20036: shows 'b≡3 mod 4 divisor' route gives density 1 only.
10. Bradford 2602.11774: check if the global covering gap is the same as ours.

Not done: fetched Chamberland/Mordell/Yamamoto/Nakayama texts, Bradford body, erdosproblems forum (403), dictionary check of our variables vs Nakayama's. No computations run (no planted controls needed).

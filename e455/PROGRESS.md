# Erdős #455 — progress log

Target: primes q_1<q_2<... with q_{n+1}-q_n >= q_n-q_{n-1}  ==>  q_n/n^2 -> infinity.

## Literature status (checked 2026-09-27)
- Richter, Acta Arith. 30 (1976) 225-227 (read in full): liminf q_n/n^2 >= 1/S = 0.352 via run-length
  bound (a run of equal gaps d has < P(d) terms, P(d) = least prime not dividing d). Nothing more.
- erdosproblems.com/455: 0 comments, 0 proof claims. CoolRmal Lean repo: liminf > 0.864 (not the
  conjecture). trureturing #9775: liminf >= 0.543, states conjecture unproved. JSP PR #2627: closed as partial.
- No claimed full proof found. Problem OPEN.

## Standing results
- [PROVED] Reduction R1: it suffices to show U(x) := #{k : d_k <= x} = o(x); equivalently that
  every convex chain of primes of length n inside [1, Cn^2] is impossible for n >= n_0(C);
  equivalently the largest convex subset of the primes in [1,N] is o(sqrt N).
- [PROVED] Cap C1: for every y, q(t)=t^2+t+c (c by CRT with 1-4c a non-residue mod every odd p<=y)
  is y-rough, convex, curvature 2. So no argument using only primes <= y (fixed) plus run-length
  bounds gives more than liminf q_n/n^2 >= 1. Primes growing with n are necessary.
- [PROVED, standard] Chains with constant or periodic curvature (period pi << n^{1/2-eps}) cannot
  stay below Cn^2: the pi-step subsequence is an exact quadratic with discriminant O(n^2), and
  Linnik–Vinogradov gives a split prime << n^{1/2+eps}, so some term is divisible by it.
- [VERIFIED, value iteration] min mean curvature kappa(y) of y-rough chains (free AP loops removed):
  kappa(5)=30/21, kappa(7)=210/157, kappa(11)=1.45 (+-0.01). kappa(y) <= 2 for all y by C1.
- [VERIFIED, exact DP, N<=1.024e6] longest convex prime chain len(N): N/len^2 =
  0.77 (1e3), 1.01 (8e3), 1.30 (3.2e4), 1.67 (1.28e5), 2.02 (5.12e5), 2.20 (1.024e6). Increasing.

## Dead ideas (do not retry)
- D1 Fixed-y automaton / max-plus certificates: capped at liminf <= 1 by C1.
- D2 Plain large sieve on the chain: chain has ~sqrt(N) elements, the large sieve bound is ~N/log N; no contradiction.
- D3 Single-prime equidistribution via complete exponential sums (Kuzmin–Landau per h): quadratics with
  non-residue discriminant avoid 0 mod p, so one prime can never force a hit; errors ~Gauss sums exceed main term.
- D4 Gallagher larger sieve: quadratic chains occupy ~p/2 classes, which is exactly the extremal case; no gain.
- D5 Counting windows / upper-bound sieve on chain windows of growing length: sieve dimension = window
  length, fundamental-lemma range collapses to polylog primes; no gain.
- D6 Counting prime triples (q_{k-1},q_k,q_{k+1}) with small second difference: count of such triples
  is ~N·X/log^3 N, vastly more than the chain uses; linkage is lost.
- D7 Crossing-multiples argument for primes p > max gap: avoiding a multiple is exactly primality of
  the landing term; circular.

## Round 1 (2026-09-27): entropy of cheap y-rough chains
Idea tested: "rigidity" — for fixed mean curvature K, the exponential growth rate h(y,K) of the
number of y-rough convex chains (mod primorial, free loops removed) decays as y grows. If it reaches 0,
cheap chains are low-complexity, which is the regime where the periodic/quadratic kill (above) might extend.
Method: pressure P(s) = growth rate of sum over paths of exp(-s*cost); h(K) <= min_s P(s)+sK
(e455/press.c, Emax=40, 400–1200 iterations, averaged growth).
- [VERIFIED] h(y,K) upper bounds:
    y=5 : K=2 .472  K=3 .867  K=4 1.150  K=6 1.550
    y=7 : K=2 .452  K=3 .802  K=4 1.059  K=6 1.459
    y=11: K=2 .392  K=3 .732  K=4  .978  K=6 1.378
  Decrease from adding p=11 is about 0.07–0.08 for K>=3 (compare -log(1-1/11) = 0.095).
  Large-s slope reproduces kappa (y=5: -1.432, y=7: -1.333), which checks the code against kappa.c.
- [CONJECTURED] h(y,K) ≈ h_0(K) - c·sum_{p<=y} 1/p with c ≈ 0.8, so h(y,K) hits 0 at y ≈ exp(exp(O(K))).
- Not established: any proof of the decay; decay alone does not exclude a single chain.

Next step: extract near-minimal-cost paths at y=11 (K about 1.6–2, where h is smallest) and test whether
they are close to quadratic (curvature almost periodic). If yes, attack the lemma "low-entropy cheap
y-rough chains have almost-periodic curvature", which would reduce to the periodic kill above.

## Round 2 (2026-09-27): literature sweep II + structure of extremal chains
Literature (GitHub code/repo search "erdos_455", "erdos 455"): google-deepmind/formal-conjectures lists
erdos_455 as `research open` (only the Richter liminf variant marked solved); rjwalters/lean-genius stores the
conjecture as an opaque axiom (no proof); conjectures-io: 0 contributions; vibemathing repo: candidate-only,
no result. No claimed proof anywhere. Status unchanged: OPEN.

Step attacked: Step B of the plan ("cheap chains are almost periodic, hence killed by the periodic/LV lemma"),
tested on the true extremal objects.
- [VERIFIED, exact DP with backtracking, e455/chain2.c] longest convex chain of odd primes <= N:
    N=1.024e6: 683 (N/len^2=2.195)   N=2.048e6: 929 (2.373)   N=4.096e6: 1267 (2.552)
    N=1e7: 1896 (2.782)  [gap cap G=12000 and G=15000 give the same answer; max gap used 11632]
  Output chains re-checked independently (all prime, gaps nondecreasing). Chain for 1e7 saved in
  e455/optimal_chain_1e7.txt. N/len^2 grows roughly like 0.25 ln N - 1.3 over 1e4..1e7.
- [VERIFIED] structure of the optimal chains (second half, largest scale):
    mean curvature 5.65 (1e6), 6.48 (4e6), 6.94 (1e7) — growing;
    P(e=0) .206 -> .157 -> .147; P(e>=10) ~ .25; curvature autocorrelation at lags 1..6 all in [-0.12, 0.04];
    ~59% of gaps divisible by 6, ~17% by 30.
- DEAD D8: "extremal/cheap prime chains are near-quadratic or almost periodic, so reduce to Linnik–Vinogradov".
  The actual extremal chains have essentially uncorrelated curvature and no quadratic structure; their cost
  grows because they must dodge primes statistically, not because of an algebraic obstruction. A proof must
  therefore handle random-like (high-entropy) chains, and the periodic/LV lemma only covers a measure-zero corner.

Next step: find a deterministic lower bound on mean curvature for high-entropy chains. Candidate mechanism:
e_k >= g(x_k) with x_k = 2q_k - q_{k-1} (distance to the next prime). Attack: show that the reflection points
x_k of a convex prime chain cannot all lie within O(K) of a prime, using that x_k is determined by two chain primes
(pair-correlation / sieve on the pairs (q_{k-1}, q_k) with the triple condition).

## Round 3 (2026-09-27): cheap windows via reflection points
Step attacked: show a convex prime chain at scale X (gaps in [X,2X], terms <= A X^2, T ~ X/K steps)
cannot keep mean curvature <= K, by proving that windows of L consecutive steps with total curvature
<= 2KL do not exist once L = L(X) is large. (Reflection point x_k = 2q_k - q_{k-1}; e_k >= nextprime(x_k) - x_k.)
- [PROVED] Window structure: a window of L+1 consecutive terms is q_k + j d_k + E_j with
  0 <= E_j <= (sum of curvatures) * j, i.e. L+1 affine forms in (a,d) = (q_k,d_k) indexed by a curvature
  pattern; #patterns with total <= 2KL is <= binom((2K+1)L, L) <= e^{c(K)L}.
- [PROVED, reduction] If for L = C log X / log log X the number of pairs (a,d) in [1,AX^2] x [X,2X] making all
  L+1 forms prime is <= (C_0)^L * S * X^3/(log X)^{L+1} (summed over patterns with average singular series
  <= C_0^L), then no cheap window exists, hence mean curvature > K at scale X, hence U(x)=o(x) and #455 follows.
  (Count: X^3 e^{c(K)L} (C_0/log X)^L < 1 for C large.) This is a CONDITIONAL route: the hypothesis is a uniform
  Hardy–Littlewood-type upper bound for prime L-tuples with L ~ log X/log log X and constant exponential in L.
- DEAD D9: making that bound unconditional with sieve methods. Selberg/Ankeny–Onishi in dimension L give
  (C L/log X)^L instead of (C_0/log X)^L (dimension loss L!), and then X^3 e^{cL}(CL/log X)^L >= X^{-o(1)}·X^3
  for every choice of L (optimum L ~ log X/log log X gives only X^{-O(1/log log log X)}). Also dead for
  L = (log X)^{1/2} (needs L >= 4 log X/log log X). Literature check: uniform-in-k k-tuple upper bounds without
  k! (Kuperberg et al., arXiv 2210.09775) are proved only assuming Hardy–Littlewood. Fixed-length windows are
  NOT rare (count ~ X^3 (log X)^{-L} >> X), so some growth of L is unavoidable.

Next step: avoid per-window counting entirely. Candidate: use that the T/L windows of ONE chain are nested/linked
(consecutive windows share L terms), so the chain is a path in the de Bruijn-type graph of cheap windows; attack
the path-existence problem with an arithmetic invariant carried along the path (e.g. the discriminant-like
quantity Phi_a(k) = (d_k - a)^2 - 4 a q_k, which is constant on quadratic stretches and changes by
2 d_k (e_k - 2a) + e_k^2 - 2a e_k per step) combined with character sums in the Linnik–Vinogradov style.

## Round 4 (2026-09-27): arithmetic invariant along the path
Step attacked: carry an arithmetic invariant along the chain to force a hit mod some prime without counting.
- [PROVED] Identity: for any integer a >= 1 and every k, 4a q_k = (d_k - a)^2 - Phi_a(k) with
  Phi_a(k) := (d_k - a)^2 - 4a q_k, and Phi_a(k+1) - Phi_a(k) = 2 d_k (e_k - 2a) + e_k^2 - 2a e_k.
  Hence for p odd, p not dividing a: p | q_k  <=>  (d_k - a)^2 == Phi_a(k) (mod p). If Phi_a(k) is a
  non-residue mod p the step is automatically safe at p. Phi_a is constant exactly on stretches with e = 2a.
- [PROVED] Turning-point description: for p in [X,2X] the chain's gap crosses p; for |d_k - p| <= R the walk
  mod p is s* + sum of (d_j - p), a slowly varying quadratic-like path around s* = q_{k(p)} mod p. A hit at p
  occurring near the turning point is equivalent to q_k having a prime divisor within R of its own gap d_k.
- DEAD D10: Phi_a as a global invariant. Off the e = 2a stretches it jumps by ~2 d_k |e_k - 2a| ~ X per step,
  so modulo any p <= X it is effectively re-randomised every step; no character-sum (Linnik–Vinogradov/Burgess)
  argument applies beyond a single constant-curvature stretch, which is already covered by the periodic lemma.
- DEAD D11: turning-point forcing for p ~ gap. Near the turning point the chain visits O(R/e) residues out of p,
  so each prime p in [X,2X] contributes expected hits O(1/log X · local density); nothing is forced for any
  individual p, and summing over p reproduces the counting problem of D9.

Next step: test the weaker target limsup q_n/n^2 = infinity (implied by the conjecture), under the
all-scales hypothesis d_k <= K k for every k >= k_0, looking for a cross-scale obstruction: the same chain must
be cheap at scales X and X^2 simultaneously, and primes p ~ X act at scale X (as small primes relative to gaps
~X^2) and at scale ~p (turning points). Compute, for the exact extremal chains, whether scale-uniform cheapness
is harder than the liminf version (compare longest chains with d_k <= K k enforced for all k).

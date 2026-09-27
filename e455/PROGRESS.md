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

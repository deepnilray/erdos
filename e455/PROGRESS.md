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

## Round 5 (2026-09-27): all-scales version and a Brun–Titchmarsh reduction
- [VERIFIED, exact DP e455/allscale.c; N=6e6, gap cap 1e4 (C<=2.4), N=3e6 cap 6e3 (C=2)] n_C := largest n such
  that some convex prime chain q_1<...<q_n (any start, index from 1) has q_k <= C k^2 for EVERY k <= n:
      C=2.0: 495   2.1: 594   2.2: 704   2.3: 834   2.4: 987      (C<=1.5: no chain at all, since q_1 >= 2)
  Each maximal chain ends well below N (0.49e6 ... 2.34e6), so N is not binding. ln n_C ~ 1.7 C + 2.8, i.e.
  consistent with extremal chains obeying q_n ~ c n^2 ln n with c ~ 0.58 (compare Round 2 data).
- [PROVED, reduction R2] "Brun–Titchmarsh along chains" implies the conjecture: if for every convex chain at
  scale X (T ~ X/K steps) and every fixed E, #{k : [x_k, x_k+E] contains a prime} <= C(E+1) T/log X + o(T),
  where x_k = 2q_k - q_{k-1}, then mean curvature >= E(1 - C(E+1)/log X) -> infinity (take E = log X/(2C)).
  Steps with e_k = 0 are exactly those with x_k prime, so they are included.
- DEAD D12: proving R2's hypothesis with the Selberg sieve by establishing a level of distribution for the
  reflection points. (i) Large sieve: sum_{d<=D} d sum_a |A(d,a)-T/d|^2 <= (X^2+D^2) T, useless since T << X^2.
  (ii) Kuzmin–Landau/van der Corput for sum_k e(h q_k/d): phase differences h d_k/d are monotone but cross
  ~hX/d integers; summing over h gives deviation ~sqrt(XT) per modulus vs main term T/d, i.e. no level of
  distribution even for d ~ 1. (iii) Quadratic chains with non-residue discriminants have degenerate local
  densities (dimension ~0 if chi(p) = -1 for all p <= z), so any sieve route must also exclude Siegel-zero-like
  behaviour, which for exact quadratics is Linnik–Vinogradov but for general chains has no analogue.

Next step: look for a mechanism that uses the monotonicity of gaps across two DIFFERENT moduli simultaneously:
the pair (q_k mod p, d_k mod p) for p ~ sqrt(X) together with the exact integer d_k in [X,2X] (not just mod p).
Concretely: for p in (sqrt X, 2 sqrt X], d_k determines d_k mod p AND floor(d_k/p) (the "lap number"), which is
monotone in k. Test numerically on the exact 1e7 chain how hits/avoidance mod p correlate with lap changes.

## Round 6 (2026-09-27): lap structure for p ~ sqrt(X) — analysed, dead
Status re-check: erdosproblems.com/455 still OPEN, 0 comments, 0 proof claims, last edited 2025-10-07.
- [PROVED] For p in (lambda sqrt X, 2 lambda sqrt X], write d_k = u_k p + r_k. The lap number u_k is nondecreasing
  in k and takes ~sqrt(X)/lambda values; within one lap the step r_k mod p sweeps [0,p) with ~p/K steps and the
  walk mod p is quadratic-like (positions s_0 + sum r_i). Each sweep visits ~p/K residues.
- DEAD D13: per sweep, avoiding 0 mod p costs the chain at most one forbidden curvature value per step;
  aggregated over p in (P,2P] the forbidden fraction of curvature choices is ~log 2/log P, and aggregated over
  all p <= sqrt(Y) it becomes "x_k + e_k is prime" — i.e. exactly R2 / D9 / D12 again. No new leverage.

Assessment of the route map after 6 rounds: every mechanism tried reduces to one of two statements,
  (a) an unconditional upper bound for prime L-tuples uniform in L ~ log X/log log X without the L! loss, or
  (b) Brun–Titchmarsh along convex chains (R2),
neither of which is available; all other ideas collapsed to them (D8–D13).

## Round 7 (2026-09-27): direct attack on statement (b) (Brun–Titchmarsh along convex chains)
(b): for a convex prime chain at scale X (gaps in [X,2X], T ~ X/K steps) and fixed E,
     #{k : q_{k+1} - 2q_k + q_{k-1} <= E} <= C(E+1) T/log X + o(T).
- [PROVED] Graph form: vertices = prime pairs (a,b), b-a in [X,2X]; cheap edge (a,b)->(b,c) iff c prime in
  [2b-a, 2b-a+E]. (b) says every convex path of length T uses <= C(E+1)T/log X cheap edges.
- [PROVED] (b) is strictly stronger than what #455 needs: #455 only needs mean curvature -> infinity, while (b)
  also bounds the number of zero-curvature (3-AP) steps. A chain whose gaps are all multiples of 30 (runs of
  <= 3 equal gaps, jumps of 30) has mean curvature 7.5 and zero-step fraction 3/4; (b) with E=0 asserts such
  chains cannot exist at large X, which is an extra statement about 4-term prime APs along the chain.
  => the right target is the weighted form (b'): sum_k e_k >= omega(X) T, not a count of cheap steps.
- DEAD D14: (b) for E=0 via counting 3-APs of primes with difference in [X,2X]: there are ~Y X/log^3 Y of them
  (Y ~ X^2), far more than T; linkage lost (same obstruction as D6).
- DEAD D15: (b) via Green–Tao–Ziegler "linear equations in primes": asymptotics hold only for a FIXED system;
  fixed-length windows are not rare (D9), and the windows here are progressions of length ~ L sqrt(Y) at height Y,
  i.e. short intervals of exponent 1/2, below the 5/8 threshold of the known short-interval Gowers-uniformity
  results for primes (Matomäki–Radziwiłł–Shao–Tao–Teräväinen).
- DEAD D16: buying a cheap step by first paying for a good vertex: heuristically costs ~log^2 Y/(E+1) per cheap
  step (worse than greedy ~log Y), but turning this into a proof is again the adversarial-path existence problem.

Result of round 7: (b) not proved. (b) as stated is stronger than needed and should be replaced by (b').
Both (b) and (b') are statements about one adversarially chosen path; every available tool (sieve, large sieve,
exponential sums, GTZ counting, character sums) controls counts of configurations, and all such counts exceed the
chain length T. No step of the proof of #455 is closed by this round.

## Round 8 (2026-09-27): (b') — mean curvature -> infinity — via deterministic bounds and self-divisibility
(b') is equivalent to U(x) = o(x), i.e. to #455 itself (R1).
- Idea A: find a structured superset S of (part of) the chain with a deterministic sieve upper bound
  #primes(S) <= C|S|/log|S| (Brun–Titchmarsh for intervals/APs, Selberg bound for polynomial value sets) and
  |S| < T log T / C.
  DEAD D17: the tightest structured supersets available are windows {q_k + j d_k + E : 0 <= E <= K j^2},
  of size ~K w^3 for w chain terms; intervals/APs containing the chain have size >= T^2; polynomial value
  sets only fit exactly-quadratic stretches (already covered). No superset within a log factor of T exists
  for a chain with unstructured curvature.
- Idea B (self-divisibility): chain terms must avoid multiples of earlier chain primes; mod q_i the walk
  starts at 0. For exact quadratics q(t) = t^2+t+c this gives Pell-type equations
  (2j+1)^2 - l (2i+1)^2 = (1-l)(1-4c), which, when solvable, have infinitely many solutions (a second,
  algebraic way to kill quadratics besides Linnik–Vinogradov).  [PROVED for exact quadratics; conditional on
  solvability of the norm equation for some l.]
  DEAD D18 for general chains: multiples of chain primes are a subset of multiples of all primes, so this
  constraint is weaker than primality itself; for unstructured curvature a hit on l*q_i is a probability
  ~1/d event, nothing forces it.

State after 8 rounds: (b') not proved. Closed steps toward #455: none beyond the standing reductions and the
exact-quadratic/periodic cases. Open: (b') for chains with unstructured curvature.

## Round 9 (2026-09-27): inventory of open items and closing what can be closed
Status re-check: erdosproblems.com/455 OPEN, 0 proof claims. Nothing below is anyone else's proof
presented as mine; Richter (1976), CoolRmal (0.864) and trureturing (0.543) are theirs and are only cited.

### Open items and their status after this round
| item | statement | status |
|---|---|---|
| O1 | #455 under a uniform prime-tuple upper bound | CLOSED (conditional theorem below) |
| O2 | exact-quadratic / periodic-curvature chains | CLOSED for exact quadratics and AP runs; periodic case with small period reduces to O2' |
| O2' | Linnik–Vinogradov with an exceptional set of small primes | cited from the literature, not re-proved here |
| O3 | (b') mean curvature -> infinity for unstructured curvature | OPEN — this is #455 itself (R1); 18 routes dead (D1–D18) |

### O1 — [PROVED, conditional] Theorem C
Hypothesis U: there is an absolute C_0 such that for all large Y, every L <= 3 log Y/log log Y, and every
curvature pattern (e_1..e_{L-1}) of nonnegative even integers, the number of pairs (a,d) with a <= Y,
d <= Y^{1/2+o(1)} such that all L forms a + j d + E_j (E_j = sum_{i<j}(j-i)e_i) are prime is at most
C_0^L · Y^{3/2+o(1)} / (log Y)^L.
Theorem C: Hypothesis U implies q_n/n^2 -> infinity for every sequence of primes with nondecreasing gaps.
Proof. Suppose q_n <= C n^2 for infinitely many n; fix such a large n and put Y = C n^2, D = 2Cn.
For n/4 <= k <= n/2 we have d_k <= (q_n - q_k)/(n-k) <= D, so the total curvature over the n/4 steps of this
window is <= D. Cut the window into floor(n/(4L)) blocks of L consecutive steps; at least half of them have
curvature sum <= 2·4DL/n = 16CL. Each such block gives a pair (a,d) = (q_k, d_k) with a <= Y, d <= D and a
pattern with sum <= 16CL; there are at most binom(16CL+L, L) <= (e(16C+1))^L patterns, and distinct blocks
have distinct a. Hence, by U,
    n/(8L) <= (e(16C+1) C_0)^L · Y^{3/2+o(1)} / (log Y)^L.
With L = floor(3 log Y/log log Y) the right side is Y^{3/2+o(1)} · Y^{-3+o(1)} = Y^{-3/2+o(1)}, while the left
side is >= Y^{1/2-o(1)}. Contradiction for n large. So for every C, q_n > C n^2 for all large n.  QED
Remark: U is a uniform Hardy–Littlewood-type UPPER bound in dimension ~log Y/log log Y; unconditionally the
Selberg sieve gives (C L/log Y)^L instead of (C_0/log Y)^L, which is too weak (D9). U is not known.

### O2 — [PROVED] exact quadratic stretches and AP runs
(i) AP runs: L+1 primes > L in arithmetic progression with difference d force every prime <= L+1 to divide d
    (else the progression covers 0 mod that prime), so L+1 <= (1+o(1)) log d. (Richter's observation.)
(ii) Exact quadratics: if q_{k0+t} = Q(t) for 0 <= t <= M with 2Q(t) = A t^2 + B t + C' in Z[t], A > 0, then
    for every odd prime p > A with (Delta/p) != -1 (Delta = B^2 - 4AC') the polynomial has a root mod p, so
    p | Q(t) for some t in any p consecutive values; since Q(t) > p this contradicts primality once M >= p.
    If Delta is a square, 8A·Q(t) splits into two linear factors and Q(t) is composite for all t >= t_0(A,B,C').
    If Delta is not a square, a prime p with (Delta/p) = 1 and A < p << |Delta|^{1/4+eps} exists by
    Linnik–Vinogradov (Burgess + r(n) = sum_{d|n} chi(d) >= 0) provided the primes <= A may be excluded (O2');
    |Delta| << X^2 at scale X, so M >= X^{1/2+eps} is impossible.
(iii) Periodic curvature with period pi: the pi-step subsequence is an exact quadratic with A = pi·sigma
    (sigma = curvature per period), so (ii) applies to stretches of length >= pi·(pi X)^{1/2+eps}.

### O3 — OPEN
(b') for chains with unstructured curvature. Every tool tried controls counts of configurations among the
primes, and each such count exceeds the chain length; closing O3 unconditionally amounts to proving #455.

## Round 10 (2026-09-27): closing O2'
- O2' CLOSED by citation: P. Pollack, "Bounds for the first several prime character nonresidues",
  arXiv:1508.05035, Theorem (small residues): for eps, A > 0 and m > m_0(eps, A), every quadratic character
  chi mod m has at least (log m)^A primes l <= m^{1/4+eps} with chi(l) = 1. (Read in the arXiv source.)
- [PROVED] With this, O2(ii) needs no exceptional set: take chi = (Delta/.) as a character mod m = 4|Delta|
  (nonprincipal because Delta is not a square). For an odd prime l with chi(l) = 1: if l does not divide A, the
  polynomial A t^2 + B t + C' has two roots mod l; if l | A then l does not divide B (else l | Delta, so
  chi(l) = 0), and the polynomial is linear with a root mod l. Pollack gives >= 2 such primes, so an odd one
  with l << |Delta|^{1/4+eps} exists. Hence an exact quadratic stretch of primes Q(t), 0 <= t <= M, with
  Q(t) > l forces M < l << |Delta|^{1/4+eps}. At scale X (|Delta| << pi^2 X^2 for the pi-step subsequence)
  this bounds exact quadratic / periodic-curvature stretches by pi (pi X)^{1/2+eps}.
- O2 is now fully CLOSED (AP runs: Richter's argument; quadratic and periodic stretches: above).
- Remaining: O3 only (= #455 itself for unstructured curvature). Not closed.

## Round 11 (2026-09-28): O3 via a limiting (Furstenberg/adelic) object
Idea: take a chain with q_n <= C n^2 infinitely often, and pass to a limit of its windows to get a
shift-invariant measure mu on sequences (curvature e_k, state (q_k, d_k) in Zhat^2), with mean curvature <= 8C
and supported on states whose q-coordinate is a unit mod every prime. Then try to show no such mu exists.
- [PROVED] Existence of the limit object: the window measures (1/W) sum_{k in window} delta_{shift^k(e, (q,d) mod m)}
  are tight for each m (finitely many states), so a diagonal subsequence converges to a shift-invariant mu on
  E^Z x Zhat^2 with the stated properties (compactness of Zhat and of bounded-curvature pattern space after
  truncating the rare large curvatures, whose density is <= 8C/E).
- DEAD D19: such mu EXISTS unconditionally. Example: the quadratic chain q(t) = t^2 + t + c with c in Zhat chosen
  so that 1 - 4c is a non-residue at every odd prime (possible prime by prime), curvature constantly 2; its orbit
  measure is shift-invariant, mean curvature 2, and every state is a unit at every prime. So the profinite
  (non-archimedean) limit cannot contradict anything; the contradiction must use the archimedean size relation
  q_k ~ d_k^2 (anchoring) jointly with primes growing with the scale — exactly what the limit discards.
  This is the same obstruction as the Cap C1, now in structural form.

Status: O3 open. No step of #455 closed this round.

## Round 12 (2026-09-28): technique search
Searched for techniques that bound second differences / curvature of subsequences of primes.
- FOUND T1: J. Brüdern, C. Elsholtz, "Local oscillations in moderately dense sequences of primes",
  arXiv:1702.00289 (read in source). Theorem 2: if P is a delta-dense subset of the primes in a progression
  (#P ∩ [1,x] >= delta(x)·pi(x;q,a), delta^2 log x -> infinity), then
  sum_{N<n<=2N} |Delta_n|/p_n >= 1e-7 delta^3, where Delta_n = p_{n+2} - 2p_{n+1} + p_n.
  Method: Selberg-sieve upper bound (with Gallagher's singular-series average) for prime triples near
  3-progressions, plus the density hypothesis. This is exactly a lower bound on curvature for subsequences of
  primes — the right kind of statement — but it needs density delta >= (log x)^{-1/2+o(1)}.
  NOT APPLICABLE: a chain with q_n <= C n^2 has #chain ∩ [1,x] ~ sqrt(x/C), i.e. delta ~ x^{-1/2} log x.
  The near-3AP triple count (~ x·X/log^3 x) then exceeds the chain's T triples (this is D6 again).
- FOUND T2: Rényi (1950), Erdős–Rényi (1950): curvature of the full prime sequence ≍ log N, via the prime
  number theorem. Applies only to all primes / dense sets.
- T3 Piatetski-Shapiro sequences floor(n^c): convex sequences with prime asymptotics known for c < ~1.16;
  our chains live at c = 2, where even existence of primes in n^2+1 is open. Not applicable.
- DEAD D20 (container/tube version of D17): cover convex chains by tubes around piecewise-quadratic curves.
  To make a tube's prime count (sieve) smaller than its share of the chain, the tolerance must be < log N/C,
  which forces pieces of bounded length w = O(1) (curvature fluctuation over w steps is ~K w^{3/2}); tubes then
  degenerate to intervals shorter than log N around each term, for which no upper bound below 1 prime exists.
Result: no known technique covers sets of primes as sparse as x^{1/2}; the closest (T1) stops at density
(log x)^{-1/2}. O3 open.

## Round 13 (2026-09-28): independent attempts to push T1 (Brüdern–Elsholtz) below density (log x)^{-1/2}
- Attempt A: use many near-3APs per chain, (q_k, q_{k+j}, q_{k+2j}) for j <= J (second difference ~K j^2).
  DEAD D21: chain supplies T·J triples; the sieve count of prime triples (a, a+h, a+2h+e) with h <= 2JX,
  |e| <= K J^2 is ~ Y·JX·KJ^2/log^3 Y >> T·J for every J. Longer near-APs (r+1 points) multiply the count by
  (KJ^2)^{r-1}/log Y per point, never below the chain count.
- Attempt B: optimise the fundamental lemma for the window problem, using that L forms cover every nonzero
  class mod p for p <= L (factor prod_{p<=L} 1/p = e^{-(1+o(1))L}) and sieving only to z = L.
  DEAD D22: the fundamental lemma needs level D >= z^{c'L} = e^{c' L log L}; with D = Y^{3/2} this caps
  L at ~1.5 log Y/(c' log log Y), and the resulting bound Y^{3/2} e^{c(K)L} e^{-L} exceeds the chain's
  T/L ~ Y^{1/2} windows unless L >= log Y. Incompatible. (Whole-chain sieve: dimension T ~ sqrt Y forces z = O(1).)
O3 open.

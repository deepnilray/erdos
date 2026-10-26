# Erdős #203, agent C2: can the large-e_p tail be controlled without a bound on c(e)?

Labels: PROVED / VERIFIED (computation with a control that can fail) / CONJECTURED. Notation as in C_allE.md. c(e) = #{p : e_p = e}, lambda(L) = #{p : Lambda_p = L}. Scripts: `C2_mink.py` (log `C2_mink.log`), `C2_stage.py` (log `C2_stage.log`), run from `e203/`.

## 0. Verdict table

| idea | verdict |
|---|---|
| 1. Minkowski short vectors to bound c(e) | DEAD. Proved structure (Lemmas 1-3), but the only per-e bound it yields is c(e) <= min(e log 3/log e, psi(e)), the trivial one. Section 2 shows why no argument built from these constraints can do better. |
| 2. Lattice weights / Möbius over n using prod p <= 2^n - 1 | DEAD, PROVED: an explicit family c*(e) ~ phi(e) log 2/log e satisfies every inequality sum_{e|n} c(e) log(e+1) <= n log 2 (Prop. 4). |
| 3. Covering-specific cap on primes per stage | DEAD for the all-size theorem. Irredundance gives disjointness for equal lattices but no cap (Section 4). |
| New: clean sufficient hypothesis H_cls(eta), weaker than pointwise c(e), PROVED sufficient given C_allE section 4.2 | Section 5. Data satisfies it with room 10^2 to 10^3 for stages l >= 100. |
| Strongest unconditional statement | Unchanged: Theorem Z of C_allE (no covering with at most 10299 primes). Nothing here raises it. |

## 1. Structure (PROVED)

**Lemma 1 (Minkowski).** Lambda_p has index e = e_p in Z^2, so the box |i|,|j| <= sqrt(e) contains a nonzero lattice vector (area 4e). Euclid-reduced first vector u satisfies |u|^2 <= (2/sqrt 3) e. Hence p | 2^i 3^j - 1 (i,j >= 0), or p | 2^a - 3^b (mixed signs), and p < 6^{sqrt e}, equivalently e_p >= (log p/log 6)^2.
VERIFIED on all 100814 pool primes (`C2_mink.py`): shortest vector lies in Lambda_p (algebra) and p | 2^a 3^b - 1 (modular check) in 100814/100814 cases, sup-norm <= sqrt(e), Hermite bound, log p <= sqrt(e) log 6 all hold with 0 violations. Controls that can fail: replacing beta by beta+1 leaves the vector in the lattice in 0 of 100667 cases; an earlier version of the Hermite check used the sup-minimal vector and fired 3645 times, which is how I found it measured the wrong vector (fixed).

**Lemma 2 (uniqueness, from V 2.1).** For a primitive v and index e there is exactly one lattice Lambda(v,e) = Zv + eZw of index e containing v. So all primes p with e_p = e and p | N(v) share the lattice Lambda(v,e), and lambda(Lambda(v,e)) <= log N(v)/log(e+1) <= |v|_1 log 3/log(e+1).

**Lemma 3 (budget per vector).** For each primitive v: sum over e of lambda(Lambda(v,e)) log(e+1) <= log N(v) <= |v|_1 log 3 (the primes involved are distinct for distinct e, all divide N(v)). Summing over primitive v in the box of radius sqrt(E) gives #{p : e_p <= E} << E^{3/2}/log E, which is Pehlivan's Lemma 8 and L11. Nothing sharper follows.

**Data (VERIFIED).** The shortest-vector statistic L^2/e of the pool lattices is indistinguishable from that of random primitive forms of the same e: mean 0.5263 vs 0.5246, median 0.5249 vs 0.5226, 10% quantile 0.1077 vs 0.1040, 1% quantile 0.0123 vs 0.0100, max 1.1518 vs 1.1518. So the pool shows no hidden short-vector bias; there is no structure to exploit beyond the lattice count. Occupancy: sum over pool primes of 1/psi(e) = 1.73, i.e. a lattice of index e is occupied with probability about 0.12/psi(e); max c(e) = 4, 88.5% of occupied e have c = 1 (as in L21).

## 2. Why idea 1 cannot give c(e) << e^{1/2+o(1)} (PROVED statement about the constraint system)

Suppose one tries to bound c(e) using only the necessary conditions available from the lattice picture: (a) p > e, (b) each prime lies in Lambda(v,e) for a vector v of sup-norm <= sqrt(e), (c) the budget of Lemma 3 and the gcd-size inequality of Prop. 4.
* For a single index e, take every lattice of index e whose shortest vector has |v|_1 log 3 >= log(e+1) (all but O(log^2 e) of the psi(e) lattices) and put one prime on each, with sizes between e and 6^{sqrt e}. Condition (a)-(c) are satisfied, giving c(e) = psi(e)(1 - o(1)). The gcd-size inequality for n = e then caps this at e log 3/log e, but that is the trivial bound. So min(e log 3/log e, psi(e)) is the best these constraints can give for one e.
* Counting by pairs (p,v) instead of per e only yields the cumulative E^{3/2}/log E, and per-vector budgets give lambda(L) <= sqrt(e), which multiplied by the number of lattices is worse than trivial. The two partial bounds do not combine because the budget of a vector is shared across all e (Lemma 3), but the adversary can spend it all on one e.
So the answer to "does any version give c(e) << e^{1/2+o(1)}?" is **no**; the Minkowski vectors only give the lattice-count exponent 3/2 (E^{3/2} primes up to e <= E), the same as the one-base trivial count t^2/log t of Chang-Shparlinski. Being a statement about necessary conditions, this proves the method is stuck, not that such c(e) occur (CONJECTURED false: data says c(e) <= 4).

**Cumulative counts are not enough for any single stage.** Stage l contains all e = l^v e' with e' l-smooth, an infinite set of e up to exp(l^{o(1)}) ranges. The only sizes available are the pointwise trivial c(e) <= e/log e and the cumulative E^{3/2}; with either, sum over l-smooth e' of c(l e')/e' diverges (the smooth set has X^{alpha} elements below X and c(e)/e' >= l/log). PROVED by that one-line comparison; it reconfirms C_allE section 4.3.

## 3. Idea 2: Möbius over n (PROVED dead)

**Prop. 4.** Define c*(e) = floor( phi(e) log 2 / log(e+1) ) for e >= 2. Then for every n: sum_{e | n} c*(e) log(e+1) <= (n-1) log 2 < log(2^n - 1) = log g, the size of gcd(2^n-1, 3^n-1)'s bound. Proof: sum_{e|n} phi(e) = n and dropping e = 1. So every inequality coming from "prod_{p : e_p | n} p <= 2^n - 1", for all n simultaneously and in any Möbius-weighted combination, is satisfied by c* with c*(e) ~ e/log e. Hence the constraint system {gcd-size, p > e} gives no information beyond the trivial bound for **any** weighted sum with nonnegative weights over e (the maximum of sum w(e) c(e) is attained at c* up to a factor 1+o(1) wherever phi(e) ~ e). In particular weights w(e) = 1/e' over l-smooth e diverge. With the lattice constraint of Lemma 3 added the conclusion of Section 2 stands.
Sign-changing weights (true Möbius inversion c(e) = sum_{d|e} mu(e/d) W(d), W(n) = omega(g_n)) need an upper bound for W(n) and a lower bound for W(d) at the same time; the lower bound is unavailable (W(n) can be 0 for many n; Ailon-Rudnick conjecture, BCZ lower bound only for sparse n).

**Realised lattices.** "Weight lattices by the probability they are realised" has no proof counterpart: the sup over finite P in the distortion bound ranges over the occupied lattices, whose number is c(e) (up to lambda), and no unconditional bound on occupancy beyond Section 2 exists.

## 4. Idea 3: caps from irredundance (PROVED partial)

* Two primes with the same lattice and the same coset are redundant; with different cosets they are disjoint. So in a minimal certificate equal-lattice primes contribute disjoint cosets of one lattice: the union is a set of density lambda/e with no overlap among them. That removes no term from E[N_l], since both cosets are present in the first moment.
* Distinct lattices of index e: Lambda_p + Lambda_q has index c_pq | e and the pair intersection has density c_pq/e^2, at most 1/(2e) when the lattices differ. Constant factor only.
* Sun/Lettl: e_p <= 2^{k-1}, P^+(e_p) <= k, f(e_p) <= k-1 restrict which e occur but not their multiplicities (only n_P(e) <= k). C_allE section 3b already shows this gives no more than Theorem Z (K = 10299), and C's quadratic stage cost with n <= k is k^2(log k)^5/y, which needs y >> k^2, while stages l <= y still contain primes of every e_p > 8*10^5 that Theorem Z handles only linearly.
No cap on the number of large-e primes per stage follows. Dead for the unbounded case.

## 5. What would suffice (PROVED reduction, weaker than pointwise c(e))

By C_allE section 4.2 and the identity 1/lcm(a,b) = sum_{d | gcd(a,b)} phi(d)/(ab):
E[N_l^2] <= R sum_{d l-smooth} phi(d) Y_{d,l}^2, with Y_{d,l} = sum_{p in P, P^+(e_p) = l, d | e'_p} Lambda_p / e'_p (e' = e/l^{v_l(e)}).
**H_cls(eta).** For every prime l >= Q and every l-smooth d: Y_{d,l} <= l^{1/2 - eta}/d, with Y taken over all primes (not only those of a given P).
**Proposition 5 (PROVED, given the inequality quoted above).** H_cls(eta) implies sum_{l > Q} cost_l << sum_{l > Q} l^{-1-2 eta} log l, which tends to 0, so the quadratic tail converges (using sum_{d smooth} phi(d)/d^2 << log l). Pointwise bounds c(e) <= exp(c (log e)^theta), theta < 1/2, imply H_cls (C_allE section 4.3), but H_cls only constrains class sums, so it allows c(e) as large as e^{1/2} on a sparse set of e as long as the sums over divisibility classes obey it.
**Data against H_cls(eta) for d = 1 (VERIFIED, `C2_stage.py`, pool e <= 8*10^5, mu_l = Y_{1,l}).** max mu_l/sqrt(l) by stage range: l in [30,100): 0.43; [100,1000): 0.25; [10^3,10^4): 0.064; [10^4,10^5): 0.018; [10^5,10^7): 0.0066. Sum over all stages of (mu_l/l)^2 = 1.31, of which 1.28 comes from l in [5,30) (max mu/sqrt(l) = 1.83 at the smallest stages, where H_cls is not required) and the part l >= 1000 is 1.0*10^-4. The truncation at e <= 8*10^5 limits large stages to few e', so for l >= 10^4 this is not evidence about the infinite sum; it is consistent with H_cls and with the heuristic mu_l ~ 0.12 e^gamma log l.
H_cls is **not proved by any known result** (it contains Erdős's order conjecture in its smooth-e weighted form, L16).

## 6. Conclusion

1. No algebraic route found around c(e): the Minkowski/lattice/gcd-size constraint system admits adversarial c(e) of size ~ e/log e (Prop. 4, Section 2), so any proof must use arithmetic beyond size and lattice counting (Subspace Theorem type input, which is ineffective, or a new idea on common prime factors of 2^a 3^b - 1).
2. The tail hypothesis can be stated as H_cls(eta) on divisibility-class first moments over smooth sets; this is the correct minimal form of what is missing.
3. Strongest unconditional statement unchanged: Theorem Z (C_allE): every covering has at least ~10^4 primes with e_p > 8*10^5 (VERIFIED with float pool bound); conditional on H_dens/H_align (or H_cls with the pool constants) no covering exists.
4. Possible untried directions: (i) effective Subspace-type or Baker bounds for gcd(2^a 3^b - 1, 2^c 3^d - 1) restricted to small vectors would bound alignments c^< and lattice multiplicities lambda but not c(e); (ii) a certified pool beyond 1.6*10^6 doubles N_Z.

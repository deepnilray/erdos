# Open-conjecture attempt log

> **Erdős #203 (current).** No covering exists using only primes with e_p = |⟨2,3⟩ mod p| ≤ 2·10⁵, for any
> lcm (2D distortion method, certified pools; exact-rational proof up to 2·10⁴). See
> [`e203/DISTORTION.md`](e203/DISTORTION.md); earlier results in [`e203/RESULTS.md`](e203/RESULTS.md).

Goal given: pick an important, genuinely open conjecture (no proof or proof claim, not reduced to a
finite check) and prove it.

**Verdict: EMPTY.** No open conjecture was proved in this session. What follows is the triage, the
target chosen, and what was actually established, with every claim labelled.

## 1. Triage (source: erdosproblems.com, fetched 2026-09-27)

- 1,200 problems parsed; 581 marked OPEN; 444 of those have zero proof claims.
- Discarded after reading primary material:
  - **#385 / #463** (composite `m` near `n` with large least prime factor). I reduced #463 to
    counting prime pairs `a < q` with `aq` in `(n+K, n+a)`. Tao (blog, 2024-08-19) shows the
    mirror problem #385 needs a parity-barrier breakthrough that at least rules out Siegel zeros.
    Not attempted further.
  - **#993** (unimodality of tree independence sequences): proof claim for large forests filed
    2026-09-21; exhaustive check to n ≤ 32 already done by others. Skipped under the rules.
  - **#1181, #693, #1073, #1106, #1146** and others: each reduces to a known hard barrier (sieve
    dimension growing with n, short-interval smooth numbers, factorials mod p, S-unit bounds).
- **Chosen target: #455.** Let q₁ < q₂ < … be primes with q_{n+1} − q_n ≥ q_n − q_{n−1}. Must
  q_n / n² → ∞? It is OPEN. Known results are weaker constant bounds only: Richter 1976
  (liminf > 0.352) and a 2026 Lean formalisation (liminf > 0.864, repo `CoolRmal/erdos455-convex-primes`).
  Neither claims the conjecture.

## 2. What was established for #455

- **[PROVED] Reduction.** If q_n ≤ C n² for infinitely many n, then the first n/2 gaps are ≤ 2Cn,
  so the mean second difference ("curvature") over the steps n/4 to n/2 is ≤ 8C. A lower bound on
  the mean curvature that tends to infinity would therefore prove the conjecture.
- **[PROVED] Cap on every fixed-modulus method.** Fix y. Choose an odd c by the Chinese remainder
  theorem so that 1 − 4c is a quadratic non-residue modulo every odd prime p ≤ y. Then
  q(t) = t² + t + c is never divisible by any prime ≤ y. Its gaps 2t + 2 strictly increase, and its
  curvature is 2 at every step. Consequently no argument that uses only divisibility by primes
  ≤ y (fixed), together with run-length limits on equal gaps, can prove liminf q_n/n² > 1. Richter's
  method and the Lean max-plus certificate are both of this type, so they cannot go past 1.
  Proving q_n/n² → ∞ requires primes that grow with n.
- **[VERIFIED, t < 2·10⁵, y ∈ {7, 13, 29, 53}]** The CRT-chosen c gives terms with no prime factor
  ≤ y. **Control:** forcing 1 − 4c to be a residue mod 5 produces a multiple of 5 at t = 0, so the
  check can fail and does fire. (`e455/quad_check.py`)
- **[VERIFIED, value iteration]** Minimum mean curvature κ(y) of convex chains of y-rough numbers,
  modelled mod the primorial with free AP loops excluded (`e455/kappa.c`, `e455/cyc.py`):
  κ(5) = 1.4286 (exact cycle, 30/21), κ(7) = 1.3376 (exact cycle, 210/157), κ(11) ≈ 1.45
  (slope over T = 2400–3000, stable to ±0.01). By the cap above, κ(y) ≤ 2 for all y.
- **[PROVED, standard]** A chain that is exactly quadratic (constant curvature) cannot satisfy
  q_n = O(n²). Its discriminant is O(n²), so Linnik–Vinogradov/Burgess give a prime p ≪ n^{1/2+ε}
  that splits it, and then some term is divisible by p. Periodic curvature reduces to this case
  by passing to the subsequence at the period.

## 3. Not established

- The conjecture itself. The missing step is to show that chains with arbitrary, non-periodic
  curvature must pay unbounded average curvature to avoid primes in a range that grows with n
  (roughly polylog(n) < p < n^{1/2}). Upper-bound sieves lose too much here, because the sieve
  dimension grows with the window length. The large sieve and Gallagher's larger sieve are both
  sharp on quadratic chains, so they give no contradiction.

## Files

- `e455/kappa.c` — value iteration for κ(y).
- `e455/cyc.py` — extracts optimal cycles.
- `e455/quad_check.py` — checks the cap construction, with a planted control.

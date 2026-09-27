# Target: Erdős Problem #203 (two-base Sierpiński number)

**Verdict: VIABLE target, no progress yet.** This file records how the target was picked. It proves nothing
about #203.

## The problem (read from erdosproblems.com/203, fetched 2026-09-27)

> Is there an integer m ≥ 1 with (m, 6) = 1 such that none of 2^k·3^l·m + 1 is prime, for any k, l ≥ 0?

Source: [ErGr80, p. 27]. Status on the site: OPEN. There are 0 proof claims, 15 comments, and the only
history entry is dated 2025-10-20.

**Why a construction settles it outright.** Suppose we have a finite set of primes P, and for each p ∈ P a
residue class, such that every pair (k, l) ∈ ℤ² falls in at least one class. Then m is fixed by CRT (plus
m > max P, so that p never equals 2^k·3^l·m + 1). That m answers YES. Checking the certificate is finite:
it is a covering of a finite torus ℤ_N × ℤ_N.

## Structure

- [PROVED, standard] For p ∤ 6, the set {(k, l) : p | 2^k·3^l·m + 1} is empty or one coset of the lattice
  L_p = ker((k, l) ↦ 2^k·3^l mod p). Its index is e_p = |⟨2, 3⟩ mod p| = lcm(ord_p 2, ord_p 3), because
  (ℤ/p)^× is cyclic. So the problem is: cover ℤ² by one coset of each of finitely many lattices L_p.
- Setting l = 0 shows that any solution m is also a classical Sierpiński number.
- The density sum Σ 1/e_p is not the obstruction. Every prime p with p − 1 | N has e_p | N. For
  N = lcm(1..x) this gives Σ 1/e_p ≥ Σ_{5≤p≤x+1} 1/(p−1), which tends to ∞. Comment 1 on the forum computes
  Σ 1/e_p = 1.97 over the 442 primes with e_p ≤ 2000.
- The real obstruction is nesting. 1D Sierpiński coverings use chains of moduli 2 | 4 | 8 | … | 64. In 2D
  the lattices L_p are almost never nested: among e_p ≤ 2000, only 77 pairs are nested, each with index
  ratio ≥ 12 (veljjanoski, forum, 2026-09-15; not re-verified here).

## Prior art (object searched: the 2D covering problem, not just "#203")

| Who | What | Outcome |
|---|---|---|
| veljjanoski (github.com/veljjanoski/erdos203) | greedy + local search on ℤ_N² | 71.7% covered at N = 5040, 76.0% at N = 55440; perfect-power m gives no help |
| AnimishSharma (forum, 2026-06) | density-sum exclusion | no covering with lcm(e_p) < 5040 using p ≤ 5·10⁷ (computational, within that bound) |
| the-omega-institute/trureturing issue #9414 (opened 2026-09-22) | congruence-family obstructions | "No such integer m … has been obtained"; research suspended |
| emil467q (forum) | direct search | no m in [10¹⁰, 10¹¹] (heuristic range only; a covering m would be far larger) |
| Filaseta–Finch–Kozek | related: m with 2^k·m^i + 1 composite for 1 ≤ i ≤ l | not this problem |

## Forecast (written before any computation)

A covering probably exists: density is unbounded and nothing forbids it. But it needs moduli far beyond
N ≈ 5·10⁴. Chance that one session produces a verified m: low, about 10%. The plausible route is not a
flat search. It is to build nesting on purpose. For example, restrict to primes whose L_p contains a common
direction (k, l) = (J, −1)·t, so that each strip reduces to a 1D covering problem. Then stack 1D Sierpiński
coverings across strips and use algebraic factors (m a perfect power) to cover leftover cosets.

## Rejected candidates (every one read on the primary page)

| # | Question | Why rejected |
|---|---|---|
| 617 | balanced r-colouring of K_{r²+1} | 7 proof claims (Jul 2026) close r = 5, 6, 7, 8, 9; small cases exhausted |
| 7 | odd distinct covering system | decades of search; LCM must be divisible by 9 or 15 (BBMST22); $2000 unclaimed for 50+ years |
| 835 | χ(J(2k,k)) = k+1 | needs a large set of Steiner systems S(k−1, k, 2k) with k = p − 1 ≥ 10, and no Steiner t-design with t ≥ 6 is known explicitly |
| 364 / 366 | consecutive powerful triples / 2-full, 3-full pairs | none below 7.38·10²⁸ / 10²²; abc forbids infinitely many |
| 307 | (Σ_P 1/p)(Σ_Q 1/q) = 1 | forces Σ_{p∈P} 1/p = ∏Q/∏P exactly with \|P ∪ Q\| ≥ 60; heuristically no solutions |
| 647, 850, 672 | τ-gap example, Erdős–Woods triple, AP product a perfect power | large searches / k ≤ 34 ruled out / abc-type heuristics predict none |

## Risks (worst first)

1. A covering may need moduli so large that it can be neither searched nor verified. The problem is still
   open, but the attack is empty.
2. At least two other groups have been active since Sep 2026. The prior-art check must be re-run
   immediately before any claim.
3. A nonexistence proof would not come from this route. Only a YES answer does.

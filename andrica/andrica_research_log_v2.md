# Andrica's Conjecture: Research Attack Log (revised)

Labels: **PROVED** (closed symbolically), **VERIFIED** (computation with stated bound, or read in a primary source),
**HEURISTIC**, **UNPROVED**, **INVALID**.

## Target

For consecutive primes $p=p_n<q=p_{n+1}$,
$$\sqrt q-\sqrt p<1\iff q-p<2\sqrt p+1 .$$

**Status: open.**

---

## A. Established

**A1. Equivalence (PROVED).** $\sqrt q-\sqrt p<1\iff q<(\sqrt p+1)^2=p+2\sqrt p+1$.

**A2. Andrica implies Legendre (PROVED).** Suppose $(n^2,(n+1)^2)$ contained no prime. Let $p$ be the largest prime
below $n^2$ and $q$ the next prime, so $q>(n+1)^2$. Then $\sqrt q-\sqrt p>(n+1)-n=1$.

**A3. Exact counterexample structure (PROVED; corrects old §2).** Put $m=\lfloor\sqrt p\rfloor$. Suppose $q-p\ge2\sqrt p+1$.

- Every integer $N\in(p,p+2\sqrt p+1)$ is composite and satisfies $N<(\sqrt p+1)^2<(m+2)^2$.
- If $N$ has no prime factor $\le m$, all its prime factors are $\ge m+1$. Then $N$ is a product of two primes from
  $\{m+1,m+2,m+3\}$, since $(m+1)(m+4)>(m+2)^2$.
- So the only candidates are $(m+1)^2$ and $(m+1)(m+3)$. The product $(m+1)(m+2)$ would need two consecutive primes,
  which happens only for $m=1$.

Hence every integer in the gap window, **with at most two exceptions**, has a prime factor $\le m$. The old §2 named
only $(m+1)^2$, so it undercounted the exceptions.

**A4. Old §9 claim refuted (VERIFIED).** For $N=30030$, $M_N(286)=\sum_{d\mid N,\,d\le286}\mu(d)=-4$, so the claimed
bound $|M_N(t)|\le1$ is false.

**A5. Finite range (VERIFIED, primary source).** Visser (arXiv:1812.02762) uses the exhaustive table of maximal prime
gaps below $2^{64}$ to verify the strong form $\sqrt{p_{n+1}}-\sqrt{p_n}<\tfrac12$ for all $p<2^{64}\approx1.844\times10^{19}$,
apart from $p\in\{3,7,13,23,31,113\}$. Andrica itself therefore holds for all $p<2^{64}$.

**A6. Independent check (VERIFIED, bound $10^8$).**

- The maximum of $\sqrt{p_{n+1}}-\sqrt{p_n}$ over primes $\le10^8$ is $0.67087\ldots$, at $(7,11)$.
- No prime $p>1000$ in that range reaches $0.5$.
- Control: deleting the primes in $(5\times10^7,\,5.002\times10^7)$ to plant a violation produced $1.4156$, so the
  checker fired.

**A7. Heuristic count (HEURISTIC; old §4).** The expected number of $m$-rough integers in the window is
$\sim 2e^{-\gamma}m/\log m\to\infty$. This is a heuristic, not a proof.

---

## B. New barrier: residue coverings alone cannot prove Andrica

**B1. Long coverings exist (VERIFIED).** The fourteen primes $\le43$ cover all 89 consecutive integers starting at
$a=14478292443584$: each one is divisible by some prime $\le43$. This start value is OEIS A049300(14), and the
length is $j(43\#)-1$ from A048670.

- The run of length 90 from the same start is **not** covered, which confirms maximality at that start.
- Control: a random start in $[10^{12},10^{13})$ is not covered for 89 steps.

**B2. The comparison (VERIFIED).** For $m=43$, every window $(p,p+2\sqrt p+1)$ with $p\in(43^2,44^2)$ contains at
most **88** integers, fewer than the covered length **89**. So at $m=43$ the covering condition of A3 is satisfiable
by residues mod $43\#$. Using A048670, $m=43$ is the first prime $p_n$ with $j(p_n\#)-1\ge2p_n+3$. Coverage is not
monotone in $m$: for $m$ in $44,\dots,46$ the window can reach 94 integers while the primes $\le m$ stay the same.

**B3. All large $m$ (PROVED from a published bound).** Ford–Green–Konyagin–Maynard–Tao give
$j(x\#)\gg x\log x\,\frac{\log\log\log x}{\log\log x}$, which eventually exceeds $2x+3$. So for every sufficiently
large $m$ there are residue classes $a\bmod P_m$ with $a+1,\dots,a+2m+3$ all divisible by primes $\le m$.

**Consequence.** Any argument that uses only the residue data $\{p\bmod\ell:\ell\le m\}$ fails. This includes
inclusion–exclusion, Jacobsthal-type bounds, CRT counting, and Möbius manipulations with $N=P_m$. A proof must use the
**magnitude** constraint $m^2<p<(m+1)^2$, which is tiny compared with $P_m\approx e^{m}$. This explains, in one
statement, why old routes §3, §5 and §9 had to fail.

**B4. The magnitude reformulation (PROVED).** Andrica holds at scale $m$ if and only if no covered residue class
$a\bmod P_m$ has a prime representative $p\in(m^2,(m+1)^2)$. Here "covered" means the window $(a,a+2\sqrt a+1)$ is
covered up to the two exceptions of A3.

The least start of a *maximal* covered run for the first $n$ primes (A049300) grows very fast. For $n=14$ it is
$\approx1.45\times10^{13}$, against $m^2=1849$. This is suggestive only; A049300 records maximal runs, not runs of
length $2m+3$.

---

## C. Corrections to the previous log

- **Old §13: INVALID.** Baker–Harman–Pintz gives $g_n<p_n^{0.525}$ only for $n$ sufficiently large, with an
  ineffective threshold. It proves nothing for $p<2^{40}$, and for $p>2^{40}$ its interval is longer than Andrica's.
  The same flawed inference appears on Wikipedia. The real finite range is A5.
- **Old §6: UNPROVED as written.**
  - The bound $K\le m+O(m/\log m)$ on smooth composites has no derivation.
  - The formula for $H$ counts semiprimes in $(m^2,(m+1)^2)$; it should count them in the gap window
    $(p,p+2\sqrt p+1)$.
  - The decomposition idea itself is fine.
- **Old §12: clarified.** The exponent $0.525$ is asymptotic, with unspecified $n_0$.
- **Unchanged and still valid:** §7 (large prime factor does not imply prime), §8 (quantifier gap), §10 (the ratio
  bound does not imply Andrica), §11 (a bound of size $x/(\log x)^3$ cannot yield $\le1$).

---

## D. Where the problem sits

- **Under RH.** Explicit bounds give only $g_n<\tfrac{22}{25}\sqrt{p_n}\log p_n$ (Carneiro–Milinovich–Soundararajan).
  That is off by the factor $\log p_n$, and Visser (arXiv:1804.02500) states RH is insufficient for Andrica.
- **Unconditionally.** $\theta=0.525$, versus the needed $\tfrac12$ with an explicit constant.
- **Structurally (B).** Any proof must exploit $p\approx m^2$ against $P_m\approx e^m$, not just congruence
  information.

---

## E. Next attacks

1. **Magnitude-sensitive sieve.** Take $p<(m+1)^2$ and a small prime $\ell\le m^{1/2}$. The residues $p\bmod\ell$ and
   the size of $p$ are linked through $p=m^2+r$ with $0<r<2m+1$. Test whether a covering of length $2m+1$ is forced to
   place large primes $\ell\in(m/2,m]$ in positions incompatible with the smaller primes on such short, low
   windows. The first step is to compute, for $m\le10^4$, the minimum number of *uncovered* positions over all
   $p\in(m^2,(m+1)^2)$, with a planted-covering control.
2. **Quantify B4.** Bound the least start of a covered run of length $2m+3$ from below as a function of $m$,
   computationally first. It needs its own computation; A049300 does not give it.
3. **Keep the exceptions honest.** Any argument must handle the two exceptions of A3.

---

## Bottom line

**Not proved.**

- **Verified.** Andrica holds for all $p<2^{64}$.
- **New (B1–B4).** Pure residue-covering methods are provably insufficient: at $m=43$, and for every sufficiently large
  $m$, coverings long enough to create an Andrica counterexample exist modulo $P_m$. So a proof must use the size of
  $p$ relative to $m^2$.

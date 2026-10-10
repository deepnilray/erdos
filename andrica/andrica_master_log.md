# Andrica's Conjecture: Master Research Log

September 2026. This file is the single running record. Only steps that were checked go in. Labels: **PROVED**, **VERIFIED** (computation with its bound, or read in a primary source), **HEURISTIC**. Refuted material is listed in §9 so that it is never reused.

**Target.** For consecutive primes $p<q$: $\sqrt q-\sqrt p<1 \iff q-p<2\sqrt p+1$.

---

## 1. Exact reformulations (PROVED)

**1.1 First-occurrence form.** Let $F(n)$ be the least prime that begins a gap of at least $2n$. Then Andrica holds for all primes if and only if $F(n)\ge n^2-n+1$ for all $n$. Failure at $p$ with gap $2n$ means $2n\ge2\sqrt p+1$, which is equivalent to $p\le n^2-n$ (equality is impossible since $\sqrt p$ is irrational). Brute-force check: $F(1..20)=3,7,23,89,113,113,113,523,523,887,1129,1327\,(\times6),9551,15683,15683$, and all satisfy the bound. A planted violation was flagged.

**1.2 Square-straddling lemma.** If $k^2<p<q<(k+1)^2$, then $q-p<2k+1<2\sqrt p+1$. So Andrica can fail only at a gap that straddles a perfect square.

**1.3 Window structure.** Put $m=\lfloor\sqrt p\rfloor$ and let the window be $W=\{p+1,\dots,p+\lfloor2\sqrt p\rfloor\}$. Every $N\in W$ satisfies $N\le m^2+4m+1$. A composite $N\in W$ with a prime factor $q>m$ is either $(m+1)^2$ or of the form $aq$ with $2\le a\le m+2$. The product $(m+1)(m+3)=m^2+4m+3$ lies outside $W$.

**1.4 Large-cofactor bound.** For fixed $q>m$ the admissible $a$ lie in an interval of length $d/q<2$. Hence $A_{>m/C}=O_C(m/\log m)$. This is the same order as the prime margin, so it cannot be discarded.

**1.5 Odd-shift covering.** A counterexample makes $p+2j$ composite for $1\le j\le m$. Then modulo each odd prime $\ell\le m+1$ one nonzero class covers all of $j=1,\dots,m$.

---

## 2. Finite range (VERIFIED)

- **Literature.** The maximal-gap tables give Andrica for all $p<2^{64}$. Visser (arXiv:1812.02762) verifies the strong form $\sqrt{p_{n+1}}-\sqrt{p_n}<1/2$ there, apart from $p\in\{3,7,13,23,31,113\}$.
- **Own check.** Over primes $\le10^8$ the maximum of $\sqrt{p_{n+1}}-\sqrt{p_n}$ is $0.67087$, at $(7,11)$. No prime above 1000 reaches $0.5$. A planted gap was detected at $1.4156$.

---

## 3. Literature frontier (VERIFIED from primary sources)

| Result | Statement |
|---|---|
| Li, arXiv:2308.04458 | $[x-x^{0.52},x]$ contains primes for large $x$; ineffective |
| Guth–Maynard | asymptotic prime counts in intervals of length $x^{\theta}$ for $\theta>17/30$; large-values bound $R\le T^{o(1)}(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4})$ |
| Carneiro–Milinovich–Soundararajan, assuming RH | $g_n<\tfrac{22}{25}\sqrt{p_n}\log p_n$; RH is insufficient for Andrica (Visser) |
| Järviniemi | $\sum_{x\le p_n\le2x,\ g_n\ge\sqrt x}g_n\ll x^{0.57+\varepsilon}$ |
| Heath-Brown | the same sum is $\ll x^{3/5+\varepsilon}$; he conjectures it is bounded |
| Selberg, assuming RH | the same sum is $\ll x^{1/2}(\log x)^2$ |

---

## 4. Sieve-route analysis (Li's paper)

**4.1 Reproduced (VERIFIED).** Region-A loss over all of A is $0.240227$, and over $A\setminus A'$ it is $0.239221$. This matches Li's (10) and (15). A wrong-integrand control gave $0.386$.

**4.2 Loss structure.** At $\theta=0.52$ the total loss is $0.969975$, so the margin is $0.030$. The region-A loss is fixed at $0.478$ for every $\theta$. The region-C loss grows by $0.043$–$0.073$ per $0.001$ decrease in $\theta$.

**4.3 Extrapolations (HEURISTIC).**
- Li's method as written stops near $\theta\approx0.5196$.
- With region A fully recovered, it would stop near $\theta\approx0.511$–$0.513$.

**4.4 Mean-value Hölder barrier (PROVED within the integer-moment mean-value framework).**
- Integer-moment mean-value bounds reach $x^{1/2}$ for $\int|P_1P_2P_3|$ only in two splits: $(1,1)$, a Type-II split, or $(2,2,1)$ with one $\alpha_i\ge1-\theta$.
- These splits cover only $2.6\%$ of region A at $\theta=0.52$, $0.66\%$ at $0.51$, and $0.17\%$ at $0.505$.
- At the balanced point the deficit is $x^{0.073}$ at $\theta=0.52$ and $x^{1/12}$ at $\theta=1/2$.

**4.5 Large-values computation.**
- Symmetric level-set exponents for region A (the target is below 1):

| $\theta$ | Mean value + Huxley | Guth–Maynard |
|---|---|---|
| 0.52 | 1.0633 | 1.0467 |
| 0.50 | 1.0833 | 1.0667 |

- The worst case sits at $V\approx N^{0.70}$–$N^{0.75}$.
- Montgomery's large-values conjecture would suffice (a conditional statement).
- Joint large values through product polynomials give about 1.1, which is worse.

**4.6 Windows close (PROVED from the lemma statements).**
- Li's Type-II condition $|\alpha_1-\alpha_2|<2\theta-1$ and his Type-I level $2\theta-1$ both vanish at $\theta=1/2$.
- Järviniemi's Type-II range $A,B\ge x^{1/2-r}$, with $R=x^r$, collapses at $r=0$. Only the zeta-sum (fourth moment) range survives there.

---

## 5. General Type-II impossibility at scale $\sqrt x$ (PROVED)

**Lemma.** Take bilinear sums over $mn\in(x,x+h]$ with $m\sim M$, $n\sim N$, $MN\approx x$. If $M\ge h$, there are coefficients $a,b\in\{\pm1\}$ for which the short sum equals the pair count while the long-interval prediction is $o(\text{pair count})$.

*Proof.* For $m\ge h$ each $m$ has at most one partner $n(m)$. Take $b$ random and set $a_m=b_{n(m)}$. ∎

**Consequence.** A general Type-II asymptotic needs $M,N\le h$. With $MN=x$ and $h=\sqrt x$ only $M=N=\sqrt x$ remains, which is the boundary the lemma breaks. So no general bilinear input exists at the Andrica length.

**Check (VERIFIED).** At $x=10^{10}$, $h=\sqrt x$, with 69,322 short pairs: adversarial coefficients give 69,322 against a prediction of 9.1. Random coefficients give $-38$ against $-3.9$.

---

## 6. The reciprocal-curve object

**6.1 Definition.** $S(x)=\sum_{\sqrt x<m\le2\sqrt x}\mu(m)\,\mu(\lceil x/m\rceil)\,\mathbf 1[\{-x/m\}\le\sqrt x/m]$.

The condition $m\lceil x/m\rceil-x\le\sqrt x$ is the same as $\{-x/m\}\le\sqrt x/m$.

**6.2 Numerics (VERIFIED).** $S$ and its unrestricted version $U$ both show square-root cancellation.

| $x$ | $U$ | $U/\sqrt{\text{terms}}$ |
|---|---|---|
| $10^8$ | $-4$ | $-0.04$ |
| $10^9$ | $-41$ | $-0.23$ |
| $10^{10}$ | $252$ | $0.80$ |
| $10^{11}$ | $387$ | $0.69$ |

**6.3 Curve facts (PROVED).**
- $f(h)=(\sqrt{h^2+4p}-h)/2$ with $-1/2<f'<0$ and $f''>0$.
- $a_h=m_h-m_{h+d}$ takes $O(d)$ values, roughly between $0.28d$ and $0.5d$.
- The level sets of $a_h$ are Beatty-type sets governed by $\{f(h)\}$. They are not contiguous: 6 values fall into 46,226 runs.
- $K_h=m_h+n_h$ steps by $\pm1$.

**6.4 Fourier twists (VERIFIED at $x=10^{10}$).** $T_k=\sum\mu(m)\mu(\lceil x/m\rceil)e(kx/m)$ has $|T_k|/\sqrt M$ between $0.19$ and $1.20$ for $k\le1000$. This matches random-sign controls; the trivial bound is 316.

**6.5 Type I with the phase (VERIFIED).** $\sum_{d\le D}\big|\sum_u e(kx/du)\big|$ saves a factor of about 5 at $D=1000$, uniformly in $k$.

**6.6 Stationary set (PROVED).** Stationarity in the diagonal band means $c\approx kM/t$. For every $k$ it is reached at $t\asymp k$, so it is localized on a hyperbola in the $(t,c)$ plane.

**6.7 Function-field calibration (VERIFIED).** The $\mathbb F_q[t]$ analogue satisfies $|S|\le\sqrt{\#\text{terms}}$ for every case with $q\le7$, $n\le3$. Its mechanism is Carmon–Rudnick-type equidistribution, which needs the short interval to be a linear subspace. The integer condition is archimedean, $\{x/m\}\le\sqrt x/m$, so the mechanism has no direct integer analogue.

---

## 7. Literature audit of claimed proofs

**7.1 Furones, arXiv:1205.6365 ("A single proof to four conjectures"): REFUTED.**
- The main theorem claims a prime in $(n,n+\lceil\sqrt n\rceil]$ for every $n\ge2$.
- Counterexamples below 5000: $n=7,23,113,114,115$. For instance $(113,124]$ contains no prime, since the next prime is 127.
- The gap in the argument: it assumes the "worst case" distribution of multiples in a shifted interval equals their distribution in $[1,\lceil\sqrt n\rceil]$. Jacobsthal coverings show shifted intervals can be covered completely. Compare $j(43\#)-1=89$, attained at the start $14478292443584$ (OEIS A049300).

**7.2 Diouf, arXiv:1810.02191 (a conditional proof from a "Parity conjecture"): CIRCULAR (PROVED).**
- The "Parity conjecture" says $\lfloor m_i^2/p\rfloor$ is odd for every $m_i\in(p,m]$, where $m=(p+q)/2$.
- Write $m_i=p+j$. Then $\lfloor m_i^2/p\rfloor=p+2j+\lfloor j^2/p\rfloor$, which is odd exactly when $\lfloor j^2/p\rfloor$ is even.
- This holds for every $j<\sqrt p$ and first fails at $j=\lceil\sqrt p\rceil$ (for $p>6$).
- So the Parity conjecture for $(p,q)$ is equivalent to $m-p<\sqrt p$, that is, $q-p<2\sqrt p$. The hypothesis is the conclusion.
- Verified on all 17,983 consecutive prime pairs below $2\times10^5$. A control with $0.5\sqrt p$ disagreed 40 times.

**7.3 Still to check.** A ResearchGate "proof" by $p_n$-estimates with constants $\lambda=1.0001$ and $\mu=1.000000002$. The likely gap is that differencing Dusart-type bounds on $p_n$ gives errors of order $n\log\log n/\log n$, far above $\sqrt{p_n}$.

---

## 8. Current attack state

The reciprocal-curve correlation $S(x)$ (§6) is the live object. What is established about it:
- Its $k\ne0$ Fourier modes carry genuine curvature, and their stationary set is localized (§6.6).
- The Type-I parts save a power (§6.5).
- Fourier detection of $c=\lceil x/m\rceil$ frequency by frequency loses $M^{1/2}$: the large sieve gives $M^{3/2}$ against the trivial bound $M$. So the frequencies have to be summed coherently.

**Open step.** Cancellation in $\sum_{m\sim\sqrt x}\mu(m)\mu(\lceil x/m\rceil)$ for each single $x$.

---

## 9. Refuted or retracted (do not reuse)

- The sufficient condition "some edge has $\le L$ private vertices" (sunflower work). It is not relevant here and is kept out.
- The random-transversal barrier. Retracted.
- The $K_h$ steps in $\{0,1\}$, contiguous $a_h$ blocks, $a_h\approx d/2$. All disproved in §6.3.
- van der Corput on $F(h)$. It leads to 4-point Chowla, an even-order case that is open even with logarithmic averaging.
- "No stationary point for $k\gg1$". False: $t\asymp k$ is always stationary.
- The binomial-coefficient Legendre proof. Its key inequality fails at $n=14$, $\lambda=16$: $1.466\times10^{28}>6.067\times10^{21}$.
- Old log §13, the "$0.525\Rightarrow$ finite range" argument. BHP is ineffective.
- Old log §9, $|M_N(t)|\le1$. False: $M_N(286)=-4$ for $N=30030$.
- The square-crossing claim "upper offset < lower offset". It holds for only 1513 of 3160 crossings. The variant "upper offset $<k$" is Oppermann's conjecture.
- Complement counting $S+A<|W|-2$. It is circular: $A=|W|-S-\#\text{primes}-[\,(m+1)^2\in W\,]$.
- Friedlander–Iwaniec transfer. Those results are global, not per fibre.
- Stationary phase with a $\mu(m)$ weight. The weight is not smooth, so it cannot be applied.

---

## 10. Möbius-side analysis (added this round)

**10.1 Identity (PROVED, VERIFIED at $x=10^8+7$).** The hyperbola correlation is a short-interval sum of the balanced part of $\mu*\mu$:
$$U(x)=\sum_{\sqrt x<m\le2\sqrt x}\mu(m)\mu(\lceil x/m\rceil)=\sum_{x\le N<x+2\sqrt x}\ \sum_{\substack{m\mid N\\ \sqrt x<m\le2\sqrt x\\ m>N-x}}\mu(m)\mu(N/m).$$
*Proof.* $N=m\lceil x/m\rceil\in[x,x+m)$. Given $N$ and a divisor $m$, the pair arises exactly when $0\le N-x<m$. ∎

The numerical check gave $-3$ on both sides. A control that drops the condition $m>N-x$ gives $-8$, so the condition matters.

**10.2 Matomäki–Teräväinen, JEMS 25 (2023), arXiv:1911.09076 (VERIFIED from the primary text).**
- **Result.** $\sum_{x<n\le x+H}\mu(n)=o(H)$ for $H\ge x^{0.55+\varepsilon}$. This beats the prime exponent $7/12$.
- **Mechanism.** Ramaré's identity extracts a small prime $p\in(P,Q]$. Vinogradov–Korobov then gives a pointwise saving $|P(1+it)|\ll(\log x)^{-A}$. With that saving, Cauchy–Schwarz handles any subset product in $[x^{1-\theta},x^\theta]$ (their Lemma 4.3).
- **Unavailable for primes.** The authors state that $\Lambda$ has no small prime factor to extract.
- **Where it stops.** The binding case is five smooth polynomials of length $x^{1/5}$ (the 3/4-line large values). The authors also note that even under RH such results need $\theta>1/2$.
- **General multiplicative functions.** Their Proposition 2.1 covers multiplicative $f$ that are eventually periodic on primes and bounded by $\tau_\kappa$. This includes $\mu*\mu$, since $(\mu*\mu)(p)=-2$. So the *full* $\mu*\mu$ sum has cancellation at length $x^{0.55+\varepsilon}$.

**10.3 What $\theta=1/2$ requires in their scheme (PROVED at the level of exponents).**
- **Type-II window.** Lemma 4.3 needs a subset product in $[x^{1-\theta},x^\theta]$. At $\theta=1/2$ this is the single point $x^{1/2}$, the same collapse as §4.6 and §5.
- **Five-smooth configuration.** Take $N$ a partial sum of $\zeta$ of length $T^{2/5}$ and $T=x^{1/2}$. One needs $\int_{T_0}^{T}|N(\tfrac12+it)|^5\,dt\ll T(\log T)^{-A}$.
  - Mean value plus Hölder gives $T^{7/6}$.
  - Lindelöf ($|N|\ll T^{\varepsilon}$) gives only $T^{1+\varepsilon}$.
  - So this configuration needs a genuine logarithmic saving beyond Lindelöf.

**10.4 Status.**
- $U(x)$ is one piece of the Heath-Brown decomposition, restricted to balanced divisors, at length $\asymp\sqrt x$.
- Cancellation in $U$ is *sufficient* input for the asymptotic route. It is not *necessary* for Andrica, which only needs a positive lower bound for primes; a Harman-type sieve may discard pieces of the right sign.
- This keeps the lower-bound route open in principle. What it needs is to show the discarded pieces cannot exhaust the main term at length $2\sqrt x$.

---

## 11. Lower-bound route (added)

**11.1 Type I alone gives nothing (PROVED from standard linear-sieve theory).** For $\mathcal A=(x,x+H]$ with $H=\sqrt x$, Type-I information has level $D\le H x^{-\varepsilon}=x^{1/2-\varepsilon}$. Detecting primes needs sieving range $z=\sqrt x$, so $s=\log D/\log z<1$. The linear-sieve lower function satisfies $f(s)=0$ for $s\le2$, so the lower bound is $0$. This is the parity barrier in exact form.

**11.2 Consequence.** Any positive lower bound needs bilinear (Type-II) input. By §5 that input does not exist for general coefficients at this length. So a lower-bound proof must use specific coefficient structure, the same requirement as the asymptotic route. The lower-bound route removes no difficulty.

**11.3 Unified target.** Every route in this log needs arithmetic, non-generic bilinear cancellation at the balanced point $m,n\asymp\sqrt x$ inside a single interval of length $\asymp\sqrt x$.

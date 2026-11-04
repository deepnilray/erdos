# Function-field analogue of #203 (experiment, 2026-10-30)

Setting: base primes P=T, Q=T+1 in F_q[T]; m coprime to PQ; is P^k Q^l m + 1 reducible for all k,l?
Irreducible pi (not T, T+1): H_pi = <T,T+1> mod pi is cyclic of order e_pi, Lambda_pi has index e_pi, coset free by CRT on m.
Files: `ffpool.py` (all pi with e_pi | N, from the factors of T^N-1; lattice form by discrete log), `cover.py` (annealing for the fewest uncovered cells of (Z/N)^2).
Results (annealing, not exhaustive, so uncovered counts are upper bounds on the optimum):
- q=3: pool is exhausted at N=80 (22 primes, sum 1/e = 1.1375; N=160, 240 add nothing). Uncovered at N=40: 392/1600 (24.5%), N=80: 1079/6400 (16.9%), N=160: 4368/25600, N=240: 9828/57600 (the larger N use fewer iterations).
- q=2: sum 1/e is 0.82 at N=105 and 0.64 at N=1023; uncovered 4320/11025 at N=105.
- Multiplicities are large where the integer case has c(e)<=4: q=2, N=1023 has 90 primes with e=1023 (consistent with Silverman's deg gcd >= cn).
Verdict: PARTIAL / no mechanism found. No covering at these sizes; plateaus near the integer case (17-21% uncovered). The large multiplicities have not produced a covering at accessible N. No claim beyond the sizes searched.

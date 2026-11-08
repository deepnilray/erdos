# BACK.md - backward calculation (scope reduced mid-task)

## Task 2: structure of Type I exceptions V (the 27 non-squares in U_12e6.txt, VERIFIED listing) and Type II exception 4545
All 27 plus 4545: n = 1 mod 8, composite, never a square, n mod 24 in {1, 9}. Never n = 5 mod 12.
Factorisations (n: factorisation, mod 24, factorisation of (n+1)/2):
105=3.5.7 (9; 53); 465=3.5.31 (9; 233); 585=3^2.5.13 (9; 293); 801=3^2.89 (9; 401); 2641=19.139 (1; 1321); 2929=29.101 (1; 5.293);
2961=3^2.7.47 (9; 1481); 3705=3.5.13.19 (9; 17.109); 4785=3.5.11.29 (9; 2393); 4945=5.23.43 (1; 2473); 9529=13.733 (1; 5.953);
13041=3^4.7.23 (9; 6521); 13465=5.2693 (1; 6733); 14841=3^2.17.97 (9; 41.181); 18825=3.5^2.251 (9; 9413); 25305=3.5.7.241 (9; 12653);
35961=3.11987 (9; 17981); 60385=5.13.929 (1; 109.277); 111969=3^3.11.13.29 (9; 5.11197); 156961=7.17.1319 (1; 13.6037);
248521=7.13.2731 (1; 313.397); 698569=71.9839 (1; 5.69857); 1116801=3^3.7.19.311 (9; 558401); 1126945=5.257.877 (1; 37.97.157);
1243089=3^2.37.3733 (9; 5.124309); 1618521=3.539507 (9; 809261); 4809=3.7.229 (9; 5.13.37).
(Missing from the 4.8M-range list in BRIEF: 4809 is in my set; the brief's "29 non-squares to 2e7" has 2 members above 4.8M that I did NOT list; my partial rerun of es_U was killed at ~1.37M.)
Type II exception 4545 = 3^2.5.101, 4545 = 9 mod 24, 345 mod 840, distance 56 to 67^2... (4545-67^2=56); (n+1)/2=2273 prime = 1 mod 4.
Distance to nearest square is NOT small (5..899 relative to sqrt n up to 1272): "near a square" is NOT the characterisation (VERIFIED on the list).
Jacobi: (n/3) in {0,1} and (n/5) in {0,1} for ALL 28 (VERIFIED, trivially forced for 3 by below; for 5 an observed pattern, unproved). (n/7), (n/11) etc. take both signs.

### PROVED new facts (elementary)
P1. n = 5 mod 8 is Type I: (m,t,u)=(3,3,(n+3)/8).
P2. n = 2 mod 3, n = 1 mod 4 is Type I: n=3t-4 with t=(n+4)/3 = 3 mod 4 (m=3,u=1).
P3. (Obláth, l=1) if (n+1)/2 has a prime factor = 3 mod 4 then Type I: m=that factor q, u=1, t=(n+q+1)/q = 3 mod 4 automatically (n+1=2 mod 4).
Hence V is contained in {n = 1 mod 24 or 9 mod 24 : every prime factor of (n+1)/2 is 1 mod 4}. VERIFIED: all 28 satisfy it (the 'all primes 1 mod 4' column above).
This explains the mod 24 and the 3-adic observations; it is a density-zero residual condition (~ (log n)^(-1/2)).

### Computation (VERIFIED, with control)
For n=1 mod 8 non-square, n<60000, (n+1)/2 only 1 mod 4 primes: 2922 numbers. Least working m: m=3: 1688, 7: 794, 11: 142, 15: 125, 23: 46,... , >=40: 37, none: 17. The 17 'none' equal exactly the V elements <=35961 (agrees with es_U/U_12e6.txt). Several need m>=100 (9649:111, 11169:151, 47601:263, 54145:371). Control: swapping the condition t=3 mod 4 to t=1 mod 4 makes all 1003 (n<20000) fail; true version leaves 15. Script /tmp/cas.py.
Tested and rejected: V = near a square; V = 'n = c.k^2+small'.  Mild 3-enrichment: 18/28 of V divisible by 3 vs ~50% expected (weak, 28 data points).

## Task 1: best skeleton (Type I only is false, so via C*)
L1 (PROVED) P1-P3 reduce to: n=1 mod 24 or 9 mod 24 with (n+1)/2 a product of primes 1 mod 4 (so (n+1)/2 = sum of two squares, = 1 mod 4).
L2 (PROVED) Thm A + Chamberland Thm 1: Type I/II coverage criteria.
L3 (VERIFIED n<=2e7) every non-square residual n is Type I or Type II (C*).
L4 (CONJECTURED) the weakest link: for every non-square n in the L1 residual set with n large, some m=3 mod 4 and a | n+m, 4|a, a=-1 mod m, (a+1)/m = 3 mod 4. Equivalently the class of (n+1)/2 is sum-of-two-squares forces no obstruction. Tool: needs a bilinear/dispersion estimate for divisor pairs of n+m over m, or a lattice argument on (k,l); nothing known. For primes, (p+1)/2 being sum of two squares is itself a thin set, so a proof would be about integers of shape p = 1 mod 24 with p+1 = 2 * (norm form) - still open.

## Task 3 (short, CONJECTURAL)
If for every hard prime p one had a divisor of p+m in the class a = -1 (mod m) for some m <= C log^2 p (a quantitative, GRH-flavoured divisor-in-progression statement), the Type I family covers all large p. No such unconditional or GRH result was found; I did not write the conditional proof.

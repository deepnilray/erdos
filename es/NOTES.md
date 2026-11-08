# Erdős–Straus (4/n = 1/x+1/y+1/z) — baseline

Status: OPEN. Nothing here proves it; this is only a computational baseline.

- Reduction: it suffices to check primes n (a solution for n gives one for any multiple).
- `es2.c`: for each prime n, scans x upward from floor(n/4)+1; with a=4x-n, b=nx, solutions
  correspond to divisors d | b^2, d<=b, d ≡ -b (mod a), y=(b+d)/a, z=(b+b²/d)/a.
- Result: no counterexample for primes <= 2e7 (1,270,607 primes, ~2 s). The largest x-offset
  from n/4 ever needed is 26 (n=8803369), so the search window is tiny in practice.
- `verify.py`: independent exact-fraction check of the same search (primes <= 1e5 agree with C).
  The C code itself does not re-verify the fractions; the 2e7 run rests on the 1e5 cross-check.

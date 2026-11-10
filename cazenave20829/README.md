# Cazenave #20829 — SOLVED by disproof

The [paper](Cazenave_20829.pdf) proves that the conjectured gap of 2 fails at every order from 11 upward and that the optimal universal additive constant is 1. A separate exact computation verifies the original inequality on every connected unlabeled graph of orders 2 through 10. The mathematical arguments for the disproof and sharp constant are symbolic.

| File | Contents |
|---|---|
| [Cazenave_20829.tex](Cazenave_20829.tex) | LaTeX source of the paper |
| [TRIAGE.md](TRIAGE.md) and [FORECAST.md](FORECAST.md) | Fifteen-candidate screening and pre-computation forecast |
| [compute.py](compute.py) and [computations.log](computations.log) | Numerical discovery grid and full-matrix exact replay, with controls |
| [exact_scan.cpp](exact_scan.cpp), [run_small_orders.sh](run_small_orders.sh), and [small_orders.log](small_orders.log) | Exact enumeration and certificate check for orders 2 through 10 |
| [lean/Counterexample.lean](lean/Counterexample.lean) and [Lean verification log](lean/verification.log) | Kernel-checked disproof on the connected graph of order 11 |

The forecast was logged before the first computation. Its SHA-256 is `cbf5990cf2d59845c01f39bd41a8681674f482cacf8110343574e4c50d653a92`. Separate algebraic, combinatorial, and computational attacks produced independent proofs or certificates. A separate adversarial audit checked the paper's variational bounds, path extension, sharp limit, and small-order verifier logic.

## Reproduce

Run from this folder.

```sh
latexmk -pdf Cazenave_20829.tex
OPENBLAS_NUM_THREADS=1 python3 compute.py sweep
python3 compute.py exact
./run_small_orders.sh /path/to/geng
```

The sweep uses NumPy. The exact replay uses Python's standard library. The small-order run needs a C++17 compiler, GMP, `rg`, and nauty's `geng`. The recorded run used nauty 2.9.0 at [`3915d89`](https://github.com/lonnen/nauty/tree/3915d891af81630853ab485f2696828a31253cd9). The [upstream documentation](https://users.cecs.anu.edu.au/~bdm/nauty/) explains building `geng`. The driver checks the per-order enumeration counts and requires a fired mutation control.

## Lean reproduction

Use Lean and Mathlib v4.28.0. In the Mathlib checkout, run

```sh
lake exe cache get Mathlib.Analysis.Matrix.Spectrum Mathlib.Combinatorics.SimpleGraph.LapMatrix Mathlib.Data.Fin.VecNotation Mathlib.Tactic.NormNum Mathlib.Tactic.Ring Mathlib.Tactic.Positivity Mathlib.Tactic.FinCases Mathlib.Tactic.Linarith
```

From this folder, run `./lean/verify.sh /path/to/mathlib4`. It checks the graph's connectivity, identifies the exact quadratic forms with Mathlib's matrices, and proves the strict gap by applying the spectral theorem. A mutated square coefficient must be rejected. Lean covers the explicit disproof. The all-orders construction and the sharp infimum are established by the paper's symbolic arguments.

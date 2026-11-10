# Code for "Sums of large prime gaps, the Guth–Maynard estimate, and Andrica's conjecture"

Compile every program with `g++ -O2 -o NAME NAME.cpp`. All grids are 400 x 400 with cells of side
1/400; in every grid file, line `i` holds row `i`, and character `j` describes the cell
`[i/400,(i+1)/400] x [j/400,(j+1)/400]`: `1` = admissible (certified on the whole cell),
`0` = an uncertified point was found, `?` = node budget exhausted (treated as not admissible),
`-` = not computed.

## Programs

| file | role |
|------|------|
| `cover.cpp` | plain main grid in (a, c) = (log_x A, log_x C), routes rho_0, rho_X (Section 4) |
| `coverM.cpp` | main grid with the extended Cauchy–Schwarz routes rho_Q; run only on boundary cells |
| `coverZ.cpp` | zeta grid in (z, c) for F = ZBC (Section 4, Proposition 4.5) |
| `sieve3.cpp` | Järviniemi's sieve program with steps (b), (c), (d) of Section 5 |
| `sieveE.cpp` | `sieve3.cpp` plus step (e) (splitting W) |
| `sieveZ.cpp` | `sieveE.cpp` plus step (f) (zeta grid, main grid for groupings with a zeta factor) |
| `computation0.5_original.cpp` | Järviniemi's original program |
| `mk_cells.py` | boundary cells for `coverM`, and cell-wise OR of two grids |
| `verify_tab.py` | spot check of a main grid (3000 cells x 40 points, planted control) |
| `myspot.py` | independent 1500-point checker of both grids at r = 0.0575 (Controls (2)) |
| `tab400.sh`, `gridZ.sh`, `build_T400_0575M.sh` | grid builders |
| `run3.sh`, `run3p.sh`, `runE.sh`, `runN.sh` | loss runners over the nine ranges of log_x p |

Usage of the grid programs:

    ./cover  N r useGM i0 i1            # rows i0..i1-1; useGM=1 adds the Guth–Maynard bounds
    ./coverM N r useGM i0 i1            # same, with the flags below
    ./coverZ N r i0 i1                  # rows i0..i1-1 of the zeta grid (z = i/N)

Usage of the sieve programs (`DIRECT=1` turns on step (c), the direct test of two-variable sums):

    ./sieve3 r DIRECT P0 P1 [GRID]      # loss from log_x p in [P0, P1)

`./sieve3 0.07 0 0 0.5` (no grid, no flags) reproduces Järviniemi's total 0.99027345, with
0.28464871 for the range [0.43, 0.5).

## Flags used for each column of Table 1

| r | grid | grid command | loss command | total |
|---|------|--------------|--------------|-------|
| 0.061 | `T400_061.txt` | `tab400.sh 0.061 a`, `tab400.sh 0.061 b` (cover, useGM=1, no flags) | `run3.sh` / `run3p.sh`: `FULLPART=1 DECOMP=1 ./sieve3 r 1 P0 P1 T400_061.txt` | 0.91397 |
| 0.059 | `T400_059.txt` | as above | as above | 0.97161 |
| 0.0585 | `T400_0585.txt` | as above | as above | 0.99123 |
| 0.058 | `T400_058.txt` | as above | `runE.sh`: `WSPLIT=1 FULLPART=1 DECOMP=1 ./sieveE r 1 P0 P1 T400_058.txt` | 0.99738 |
| 0.0575 | `T400_0575M.txt`, `Z400_0575.txt` | `build_T400_0575M.sh`; `BUDGET=20000 gridZ.sh 400 0.0575 Z400_0575.txt` | `runN.sh 0.0575 T400_0575M.txt TAG 1` and `... 2`: `ZTAB=Z400_0575.txt ZNOZ=1 WSPLIT=1 FULLPART=1 DECOMP=1 ./sieveZ r 1 P0 P1 T400_0575M.txt` | 0.99155 (0.99154810) |

Meaning of the flags actually used:

* `cover`: none (`DBG` only prints diagnostics).
* `coverM`: `MCS=3` adds the routes rho_Q for Q = A^kA B^kB C^kC with 0 <= k <= 3;
  `BUDGET=20000` is the node budget per cell (default 8000); `CELLS=file` restricts the run to the
  listed cells (`i j` per line), all other cells being printed as `-`.
* `coverZ`: `BUDGET` (node budget per cell), set to 20000 by `gridZ.sh`.
* `sieve3`, `sieveE`, `sieveZ`: `FULLPART=1` tests all groupings (step (b)); `DECOMP=1` allows one
  Heath-Brown split (step (d)); `WSPLIT=1` splits W into two groups (step (e));
  `ZTAB=Z400_0575.txt` uses the zeta grid (step (f)); `ZNOZ=1` also tests groupings containing a
  zeta factor against the main grid (step (f), Remark 4.1).

Experimental flags, not used for any result: `coverM`: `HB`, `JUT`, `GM2`, `BOU`, `PRODK`,
`PRODW`, `HOLDK`, `J0`, `J1`, `DBG`; `coverZ`: `WMAX`, `NOZ12`, `NOZHUX`, `NOZPW`, `NOZHOLD`,
`PT`, `J0`, `J1`, `DBG`; `sieveE`/`sieveZ`: `WSPLIT2`, `WS2DEPTH`, `ZN` (zeta grid size, default
400), `DUMP` (diagnostic output).

## Main grid for r = 0.0575

`T400_0575.txt` is the plain grid (`cover 400 0.0575 1 0 400`). `cells_0575.txt` lists the
boundary cells: all cells that are not `1` in the plain grid, satisfy i + j <= N - 2, and have a
`1` within Chebyshev distance 2 (`python3 mk_cells.py cells T400_0575.txt cells_0575.txt`).
`coverM` is run on these cells with

    CELLS=cells_0575.txt MCS=3 BUDGET=20000 ./coverM 400 0.0575 1 0 400 > M.txt

and the cell-wise OR is formed with `python3 mk_cells.py or T400_0575.txt M.txt OUT`.
`build_T400_0575M.sh` performs these steps and then runs `mk_cells.py sub`, which checks that
every `1` cell of the shipped `T400_0575M.txt` (the grid used for Table 1) is `1` in the rebuilt
grid. The shipped grid was assembled in stages, partly with the default budget 8000, so the rebuilt
grid is a superset: all 85986 `1` cells of `T400_0575M.txt` are certified in it, and it certifies
226 further cells, which are not used (the published total 0.99154810 is computed with
`T400_0575M.txt`). Rows without such extra cells agree exactly, including the rows 15, 55, 158,
166, 199 and 201, which contain cells upgraded by `coverM`. The output of the `coverM` step
(about one hour on two cores) is shipped as `coverM_0575.txt`.

## Checks

    python3 verify_tab.py T400_<r>.txt r
    python3 myspot.py 1 100000 1500

The second command tests every certified cell with i + j < 399 of both r = 0.0575 grids (6186 in
the main grid, 15849 of the 15860 in the zeta grid) at 1500 points each, runs two control points,
and reports, for 100 random cells marked `0`, how many show a failing point (about 90).

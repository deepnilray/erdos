#!/usr/bin/env python3
"""Boundary cells for coverM, and cell-wise OR of two grids.

  python3 mk_cells.py cells PLAIN.txt OUT_CELLS.txt [N]
      OUT = all cells (i,j) with plain[i][j] != '1', i+j <= N-2, and some '1'
      within Chebyshev distance 2 in the plain grid.
  python3 mk_cells.py or PLAIN.txt COVERM_OUT.txt OUT_GRID.txt [N]
      OUT[i][j] = '1' if either grid has '1' at (i,j), else the plain entry.
  python3 mk_cells.py sub GRID_A.txt GRID_B.txt [N]
      checks that every '1' cell of GRID_A is '1' in GRID_B; prints the counts.
"""
import sys
def ld(f):
    d = {}
    for l in open(f):
        p = l.split()
        if len(p) == 2: d[int(p[0])] = p[1]
    return d
mode = sys.argv[1]
if mode == 'cells':
    plain, out = sys.argv[2], sys.argv[3]; N = int(sys.argv[4]) if len(sys.argv) > 4 else 400
    o = ld(plain)
    g = lambda i, j: o[i][j] if 0 <= i < N and 0 <= j < N else 'x'
    with open(out, 'w') as f:
        for i in range(N):
            for j in range(N):
                if o[i][j] != '1' and i + j <= N - 2 and any(g(i + a, j + b) == '1' for a in range(-2, 3) for b in range(-2, 3)):
                    f.write(f"{i} {j}\n")
elif mode == 'or':
    plain, cm, out = sys.argv[2], sys.argv[3], sys.argv[4]; N = int(sys.argv[5]) if len(sys.argv) > 5 else 400
    o = ld(plain); c = ld(cm)
    with open(out, 'w') as f:
        for i in range(N):
            ci = c.get(i, '-' * N)
            f.write(f"{i} " + ''.join('1' if (o[i][j] == '1' or ci[j] == '1') else o[i][j] for j in range(N)) + "\n")
elif mode == 'sub':
    A, B = ld(sys.argv[2]), ld(sys.argv[3]); N = int(sys.argv[4]) if len(sys.argv) > 4 else 400
    ones = [(i, j) for i in range(N) for j in range(N) if A[i][j] == '1']
    miss = [(i, j) for (i, j) in ones if B[i][j] != '1']
    extra = sum(1 for i in range(N) for j in range(N) if B[i][j] == '1' and A[i][j] != '1')
    print(f"{len(ones)} certified cells in {sys.argv[2]}; {len(miss)} not certified in {sys.argv[3]}; {extra} extra cells certified in {sys.argv[3]}")
    if miss: print("missing:", miss[:20]); sys.exit(1)
else:
    sys.exit(__doc__)

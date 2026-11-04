"""Exact max-coverage of G_S = Z^2 / cap_{p in S} L_p by one coset per prime (CP-SAT).

A full covering (coverage == |G_S|) yields m by CRT: m == -(2^k0 3^l0)^{-1} mod p for any cell
(k0,l0) in p's chosen coset.  Translation symmetry: the first prime's coset is fixed to 0."""
import sys, json, time
from ortools.sat.python import cp_model
from lattice import *

def cells_of(H):
    (a, _), (c, d) = H
    for k in range(a):
        for l in range(d):
            yield k, l

def solve(S, H, tlimit=300, workers=4, hint=None):
    cells = list(cells_of(H)); n = len(cells)
    m = cp_model.CpModel()
    X = {}
    for i, p in enumerate(S):
        X[i] = [m.NewBoolVar(f'x{i}_{c}') for c in range(p['e'])]
        m.AddExactlyOne(X[i])
    m.Add(X[0][0] == 1)
    Y = []
    for (k, l) in cells:
        y = m.NewBoolVar('')
        m.AddBoolOr([X[i][(p['alpha']*k + p['beta']*l) % p['e']] for i, p in enumerate(S)] + [y.Not()])
        Y.append(y)
    m.Maximize(sum(Y))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = tlimit; s.parameters.num_workers = workers
    t = time.time(); st = s.Solve(m)
    choice = [next(c for c in range(p['e']) if s.Value(X[i][c])) for i, p in enumerate(S)] if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None
    return dict(status=s.StatusName(st), best=s.ObjectiveValue(), bound=s.BestObjectiveBound(), n=n,
                time=time.time() - t, choice=choice)

if __name__ == '__main__':
    pool = {r['p']: r for r in load(sys.argv[1])}
    S = [pool[int(x)] for x in sys.argv[2].split(',')]
    H = [[1, 0], [0, 1]]
    for p in S: H = intersect(p, H)
    r = solve(S, H, tlimit=float(sys.argv[3]) if len(sys.argv) > 3 else 120)
    dens = sum(1 / p['e'] for p in S)
    print(f"|S|={len(S)} sum1/e={dens:.4f} |G_S|={r['n']} status={r['status']} "
          f"coverage={r['best']/r['n']:.4f} upper={r['bound']/r['n']:.4f} random={1-__import__('math').prod(1-1/p['e'] for p in S):.4f} t={r['time']:.0f}s")

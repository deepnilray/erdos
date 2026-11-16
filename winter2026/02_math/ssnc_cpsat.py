#!/usr/bin/env python3
"""CP-SAT search for SSNC counterexamples on n vertices, min outdegree >= delta, d+(0) = delta, N+(0) = {1..delta}.

Usage: ssnc_cpsat.py n delta [--slack k] [--lemma] [--time T] [--workers W]
  --lemma : add the redundant fixed-target capacity constraints of Brukhman (arXiv:2608.11530, Lemma 2.1):
            for each target x, if some source v cannot reach x in <= 2 steps then |P(x)| <= 2 q(x) - 1.
            These hold for the exact N2/U indicators of any genuine counterexample, so they cut nothing real.
  --slack k : planted-failure control (|N2(v)| <= d+(v) - 1 + k); models are re-checked by brute force.
"""
import argparse, itertools, time
from ortools.sat.python import cp_model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', type=int); ap.add_argument('delta', type=int)
    ap.add_argument('--slack', type=int, default=0)
    ap.add_argument('--lemma', action='store_true')
    ap.add_argument('--time', type=float, default=600)
    ap.add_argument('--workers', type=int, default=2)
    a = ap.parse_args()
    n, d = a.n, a.delta
    V = range(n)
    m = cp_model.CpModel()
    A = {(u, v): m.NewBoolVar(f'a{u}_{v}') for u in V for v in V if u != v}
    S = {(v, w): m.NewBoolVar(f's{v}_{w}') for v in V for w in V if v != w}
    for u, v in itertools.combinations(V, 2):
        m.AddBoolOr([A[u, v].Not(), A[v, u].Not()])
    out = {v: sum(A[v, w] for w in V if w != v) for v in V}
    for v in V:
        m.Add(out[v] >= d)
    m.Add(out[0] == d)
    for w in range(1, d + 1):
        m.Add(A[0, w] == 1)
    for v in V:
        for w in V:
            if w == v:
                continue
            m.AddBoolOr([A[v, w].Not(), S[v, w].Not()])
            for u in V:
                if u not in (v, w):
                    m.AddBoolOr([A[v, u].Not(), A[u, w].Not(), A[v, w], S[v, w]])
    for v in V:
        m.Add(sum(S[v, w] for w in V if w != v) <= out[v] - 1 + a.slack)
    if a.lemma:
        for x in V:
            indeg = sum(A[y, x] for y in V if y != x)
            q = (n - 1 - indeg) - d          # q(x) = |T(x)| - delta, T(x) = non-in-neighbours of x
            Uvx = []
            for v in V:
                if v == x:
                    continue
                u = m.NewBoolVar(f'u{v}_{x}')
                # u = 1 iff v -/-> x and x not in N2(v)  (exact when S is exact)
                m.Add(u + A[v, x] + S[v, x] >= 1)
                m.Add(u + A[v, x] <= 1); m.Add(u + S[v, x] <= 1)
                Uvx.append(u)
            p = sum(Uvx)
            m.Add(p <= 2 * q)
            for u in Uvx:
                m.Add(p <= 2 * q - 1).OnlyEnforceIf(u)
    sol = cp_model.CpSolver()
    sol.parameters.max_time_in_seconds = a.time
    sol.parameters.num_workers = a.workers
    t = time.time()
    st = sol.Solve(m)
    dt = time.time() - t
    name = sol.StatusName(st)
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        arc = [[u != v and sol.Value(A[u, v]) == 1 for v in V] for u in V]
        res = []
        for v in V:
            N1 = {w for w in V if arc[v][w]}
            N2 = {w for u in N1 for w in V if arc[u][w] and w not in N1 and w != v}
            res.append((len(N1), len(N2)))
        sey = [v for v, (x, y) in enumerate(res) if y >= x]
        print('model', res, 'Seymour', sey)
        assert min(x for x, _ in res) >= d
        if a.slack == 0:
            assert not sey
            print('!!! COUNTEREXAMPLE')
    print('RESULT', n, d, 'slack', a.slack, 'lemma', a.lemma, name, '%.1fs' % dt)


if __name__ == '__main__':
    main()

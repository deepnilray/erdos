#!/usr/bin/env python3
"""SAT search for counterexamples to Seymour's second neighbourhood conjecture (SSNC)
with n vertices and minimum outdegree >= delta, vertex 0 of outdegree exactly delta.

Usage: ssnc_sat.py n delta [--slack k] [--solver cd19] [--sb]
  --slack k : planted-failure control. The non-Seymour constraint |N2(v)| <= d+(v) - 1 is weakened to
              |N2(v)| <= d+(v) - 1 + k. With k >= 1 the instance must become SAT for suitable (n, delta)
              (Seymour-tight orientations exist, e.g. rotational tournaments), and every model is checked by an
              independent brute-force checker.
Exit summary line: RESULT n delta slack SAT/UNSAT time
"""
import sys, time, itertools, argparse
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


def build(n, delta, slack, sb, regular=False, zvertex=False, z2=None):
    pool = IDPool()
    A = lambda u, v: pool.id(('a', u, v))   # arc u -> v
    S = lambda v, w: pool.id(('s', v, w))   # w in N2(v) (forced true when a 2-path exists and v-/->w)
    cnf = CNF()
    V = range(n)
    for u, v in itertools.combinations(V, 2):
        cnf.append([-A(u, v), -A(v, u)])
    for v in V:
        outs = [A(v, w) for w in V if w != v]
        if v == 0 or regular:
            enc = CardEnc.equals(lits=outs, bound=delta, vpool=pool, encoding=EncType.seqcounter)
        else:
            enc = CardEnc.atleast(lits=outs, bound=delta, vpool=pool, encoding=EncType.seqcounter)
        cnf.extend(enc.clauses)
    for v in V:
        for w in V:
            if w == v:
                continue
            for u in V:
                if u in (v, w):
                    continue
                # a(v,u) & a(u,w) & -a(v,w) -> s(v,w)
                cnf.append([-A(v, u), -A(u, w), A(v, w), S(v, w)])
            # s(v,w) -> -a(v,w)  (exact second neighbourhood excludes N1)
            cnf.append([-S(v, w), -A(v, w)])
    # non-Seymour: |N2(v)| - d+(v) <= -1 + slack  <=>  sum s + sum(-a) <= (n-1) - 1 + slack
    for v in V:
        lits = [S(v, w) for w in V if w != v] + [-A(v, w) for w in V if w != v]
        enc = CardEnc.atmost(lits=lits, bound=n - 2 + slack, vpool=pool, encoding=EncType.seqcounter)
        cnf.extend(enc.clauses)
    if sb:
        # symmetry breaking (sound): vertex 0 has outdegree delta, relabel so N+(0) = {1..delta}
        for w in range(1, delta + 1):
            cnf.append([A(0, w)])
    if zvertex:
        # Theorem Z (LOG.md, PROVED): every counterexample with n = 2*delta+3 has a vertex z with no missing edge
        # and d+(z) = delta. Relabel it 0: 0 -> 1..delta, and every other vertex -> 0.
        assert n == 2 * delta + 3
        for w in range(delta + 1, n):
            cnf.append([A(w, 0)])
    if z2:
        # Theorem (LOG.md step 3, PROVED): a counterexample has a second vertex of outdegree delta adjacent to all
        # others. It is an out-neighbour of 0 (relabel it 1) or an in-neighbour of 0 (relabel it n-1).
        k = 1 if z2 == 'out' else n - 1
        for w in V:
            if w != k:
                cnf.append([A(k, w), A(w, k)])
        cnf.extend(CardEnc.atmost(lits=[A(k, w) for w in V if w != k], bound=delta, vpool=pool,
                                  encoding=EncType.seqcounter).clauses)
    return cnf, pool


def check_model(n, model, pool):
    pos = set(l for l in model if l > 0)
    arc = [[pool.id(('a', u, v)) in pos if u != v else False for v in range(n)] for u in range(n)]
    for u in range(n):
        for v in range(n):
            assert not (arc[u][v] and arc[v][u])
    res = []
    for v in range(n):
        N1 = {w for w in range(n) if arc[v][w]}
        N2 = {w for u in N1 for w in range(n) if arc[u][w] and w not in N1 and w != v}
        res.append((len(N1), len(N2)))
    return arc, res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', type=int)
    ap.add_argument('delta', type=int)
    ap.add_argument('--slack', type=int, default=0)
    ap.add_argument('--solver', default='cd19')
    ap.add_argument('--nosb', action='store_true')
    ap.add_argument('--zvertex', action='store_true')
    ap.add_argument('--z2', choices=['out', 'in'])
    ap.add_argument('--regular', action='store_true', help='all outdegrees exactly delta (the Z-empty tight case)')
    a = ap.parse_args()
    cnf, pool = build(a.n, a.delta, a.slack, not a.nosb, a.regular, a.zvertex, a.z2)
    t = time.time()
    with Solver(name=a.solver, bootstrap_with=cnf.clauses) as s:
        sat = s.solve()
        dt = time.time() - t
        if sat:
            arc, res = check_model(a.n, s.get_model(), pool)
            mind = min(d for d, _ in res)
            seymour = [v for v, (d1, d2) in enumerate(res) if d2 >= d1]
            print('model (d+,|N2|):', res, 'min outdeg', mind, 'Seymour vertices', seymour)
            assert mind >= a.delta
            if a.slack == 0:
                assert not seymour, 'checker disagrees with encoding'
                print('!!! COUNTEREXAMPLE FOUND')
    print('RESULT', a.n, a.delta, a.slack, 'SAT' if sat else 'UNSAT', '%.1fs' % dt,
          'vars', pool.top, 'clauses', len(cnf.clauses))


if __name__ == '__main__':
    main()

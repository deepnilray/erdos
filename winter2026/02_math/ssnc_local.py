#!/usr/bin/env python3
r"""Local-structure explorer for SSNC at a complete minimum-outdegree vertex (session 2, 2026-11-17).

Vertex 0 is complete (adjacent to all others) with outdegree exactly delta: 0 -> 1..delta, others -> 0.
All vertices have outdegree >= delta. The non-Seymour constraint |N2(v)| <= d+(v) - 1 (+ slack) is imposed only
on the vertices in the chosen set S; the question is whether a Seymour vertex is forced inside V \ S.

  S = 'zA'    : {0} and N+(0)
  S = 'zIn'   : {0} and N-(0)
  S = 'notA'  : every vertex except N+(0)
  S = 'notIn' : every vertex except N-(0)
  S = 'all'   : every vertex (the full counterexample question)
Options: --z2 out|in fixes a second complete vertex of outdegree delta (1 or n-1);
         --dense requires n = 2 delta + 3; --slack k is the planted-failure control.
Every SAT model is re-checked by an independent brute-force checker.
"""
import sys, time, itertools, argparse
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


def build(n, delta, Sset, slack, z2, freein=False, degon=None, nocomplete=False, cond=None):
    pool = IDPool()
    A = lambda u, v: pool.id(('a', u, v))
    S = lambda v, w: pool.id(('s', v, w))
    cnf = CNF()
    V = range(n)
    for u, v in itertools.combinations(V, 2):
        cnf.append([-A(u, v), -A(v, u)])
    for w in range(1, delta + 1):
        cnf.append([A(0, w)])
    if not nocomplete:
        for w in range(delta + 1, n):
            cnf.append([A(w, 0)])
    else:
        cnf.extend(CardEnc.atmost(lits=[A(0, w) for w in V if w != 0], bound=delta, vpool=pool, encoding=EncType.seqcounter).clauses)
    for v in V:
        outs = [A(v, w) for w in V if w != v]
        if v == 0 or (freein and v > delta):
            continue
        cnf.extend(CardEnc.atleast(lits=outs, bound=delta, vpool=pool, encoding=EncType.seqcounter).clauses)
    for v in Sset:
        for w in V:
            if w == v:
                continue
            for u in V:
                if u in (v, w):
                    continue
                cnf.append([-A(v, u), -A(u, w), A(v, w), S(v, w)])
            cnf.append([-S(v, w), -A(v, w)])
        lits = [S(v, w) for w in V if w != v] + [-A(v, w) for w in V if w != v]
        cls = CardEnc.atmost(lits=lits, bound=n - 2 + slack, vpool=pool, encoding=EncType.seqcounter).clauses
        if cond and v > delta:
            # non-Seymour required only if v in B = N2(0) (cond='B') or v in C = U(0) (cond='C'); exact s(0,v) below
            g = pool.id(('g', v))
            cnf.append([-g, S(0, v)] if cond == 'B' else [-g, -S(0, v)])
            cnf.append([g, -S(0, v)] if cond == 'B' else [g, S(0, v)])
            cls = [[-g] + c for c in cls]
        cnf.extend(cls)
    if cond:
        for v in range(delta + 1, n):
            cnf.append([-S(0, v)] + [A(w, v) for w in range(1, delta + 1)])
            for w in range(1, delta + 1):
                cnf.append([-A(w, v), S(0, v)])
    if degon:
        # exact s(0,v) for v in N-(0): s(0,v) <-> OR_{w in 1..delta} a(w,v)
        for v in range(delta + 1, n):
            cnf.append([-S(0, v)] + [A(w, v) for w in range(1, delta + 1)])
            for w in range(1, delta + 1):
                cnf.append([-A(w, v), S(0, v)])
            outs = [A(v, w) for w in V if w != v]
            sel = pool.id(('sel', v))
            cnf.append([-sel, S(0, v)] if degon == 'B' else [-sel, -S(0, v)])
            cnf.append([sel, -S(0, v)] if degon == 'B' else [sel, S(0, v)])
            for cl in CardEnc.atleast(lits=outs, bound=delta, vpool=pool, encoding=EncType.seqcounter).clauses:
                cnf.append([-sel] + cl)
    if z2:
        k = 1 if z2 == 'out' else n - 1
        for w in V:
            if w != k:
                cnf.append([A(k, w), A(w, k)])
        cnf.extend(CardEnc.atmost(lits=[A(k, w) for w in V if w != k], bound=delta, vpool=pool,
                                  encoding=EncType.seqcounter).clauses)
    return cnf, pool


def analyse(n, model, pool):
    pos = set(l for l in model if l > 0)
    arc = [[u != v and pool.id(('a', u, v)) in pos for v in range(n)] for u in range(n)]
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
    ap.add_argument('S', choices=['zA', 'zAB', 'zAC', 'A', 'zIn', 'notA', 'notIn', 'all'])
    ap.add_argument('--slack', type=int, default=0)
    ap.add_argument('--z2', choices=['out', 'in'])
    ap.add_argument('--freein', action='store_true', help='no outdegree lower bound on N-(0)')
    ap.add_argument('--nocomplete', action='store_true', help='drop: every vertex outside N+[0] -> 0')
    ap.add_argument('--degon', choices=['B', 'C'], help='with --freein: keep the outdegree bound only on B=N2(0) or C=U(0)')
    a = ap.parse_args()
    n, d = a.n, a.delta
    Aset = set(range(1, d + 1)); In = set(range(d + 1, n))
    Sset = {'zA': {0} | Aset, 'zAB': set(range(n)), 'zAC': set(range(n)), 'A': set(Aset), 'zIn': {0} | In, 'notA': {0} | In, 'notIn': {0} | Aset,
            'all': set(range(n))}[a.S]
    if a.S == 'notA':
        Sset = set(range(n)) - Aset
    if a.S == 'notIn':
        Sset = set(range(n)) - In
    cnf, pool = build(n, d, Sset, a.slack, a.z2, a.freein, a.degon, a.nocomplete, {'zAB': 'B', 'zAC': 'C'}.get(a.S))
    t = time.time()
    with Solver(name='cd19', bootstrap_with=cnf.clauses) as s:
        sat = s.solve(); dt = time.time() - t
        if sat:
            arc, res = analyse(n, s.get_model(), pool)
            assert min(res[v][0] for v in range(n) if not (a.freein and v > d)) >= d and res[0][0] == d
            assert a.nocomplete or all(arc[0][w] or arc[w][0] for w in range(1, n))
            if a.S in ('zAB', 'zAC'):
                N2z = {v for v in range(d + 1, n) if any(arc[w][v] for w in range(1, d + 1))}
                Sset = {0} | Aset | (N2z if a.S == 'zAB' else In - N2z)
            bad = [v for v in Sset if res[v][1] > res[v][0] - 1 + a.slack]
            assert not bad, 'checker disagrees with encoding'
            sey = [v for v, (x, y) in enumerate(res) if y >= x]
            print('model (d+,|N2|):', res)
            print('Seymour vertices:', sey)
            print('arcs:', [(u, v) for u in range(n) for v in range(n) if arc[u][v]])
    print('RESULT', n, d, a.S, 'slack', a.slack, 'z2', a.z2, 'SAT' if sat else 'UNSAT', '%.1fs' % dt)


if __name__ == '__main__':
    main()

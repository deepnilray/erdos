#!/usr/bin/env python3
"""Numerical guard for the algebra in LOG.md (claims I1, I2, I3), on random oriented graphs with n = 2*delta + 3.

I1 (identity):  sum_x (p_x - 2 q_x + 1) = sum_v (d+(v) - 1 - |N2(v)|)       [needs only n = 2 delta + 3]
I2:             q_x = deg_M(x) + (d+(x) - delta)                            [M = missing (non-adjacent) pairs]
I3 (refined fixed-target lemma): for p = |P(x)| > 0,
                p (2 q_x - 1 - p) / 2 >= J_P + m_P + r_x
    J_P = sum_{v in P}(d+(v) - delta), m_P = non-adjacent pairs inside P,
    r_x = #{(v,t): v in P, t in T(x) minus P, v -/-> t}.
Planted failure: the same test of I1 with "+1" replaced by "+0" and I3 with an extra "+1" on the right must FAIL.
"""
import random, itertools, sys

def rand_graph(n, delta, rng):
    # random oriented graph with min outdegree >= delta: random tournament-ish, then delete arcs keeping d+ >= delta
    while True:
        arc = [[False]*n for _ in range(n)]
        for u, v in itertools.combinations(range(n), 2):
            if rng.random() < 0.5: arc[u][v] = True
            else: arc[v][u] = True
        arcs = [(u, v) for u in range(n) for v in range(n) if arc[u][v]]
        rng.shuffle(arcs)
        k = rng.randint(0, n)
        for (u, v) in arcs:
            if k == 0: break
            if sum(arc[u]) > delta:
                arc[u][v] = False; k -= 1
        if min(sum(r) for r in arc) == delta:
            return arc

def stats(arc, delta, plant):
    n = len(arc); V = range(n)
    N1 = [{w for w in V if arc[v][w]} for v in V]
    N2 = [{w for u in N1[v] for w in V if arc[u][w] and w not in N1[v] and w != v} for v in V]
    U = [set(V) - {v} - N1[v] - N2[v] for v in V]
    T = [{y for y in V if y != x and not arc[y][x]} for x in V]
    q = [len(T[x]) - delta for x in V]
    P = [{v for v in V if x in U[v]} for x in V]
    lhs = sum(len(P[x]) - 2*q[x] + (0 if plant else 1) for x in V)
    rhs = sum(len(N1[v]) - 1 - len(N2[v]) for v in V)
    ok1 = lhs == rhs
    ok2 = all(q[x] == sum(1 for y in V if y != x and not arc[x][y] and not arc[y][x]) + len(N1[x]) - delta for x in V)
    ok3 = True
    for x in V:
        p = len(P[x])
        if p == 0: continue
        J = sum(len(N1[v]) - delta for v in P[x])
        mP = sum(1 for a, b in itertools.combinations(P[x], 2) if not arc[a][b] and not arc[b][a])
        r = sum(1 for v in P[x] for t in T[x] - P[x] if not arc[v][t])
        assert all(N1[v] <= T[x] for v in P[x])
        if not (p*(2*q[x]-1-p) >= 2*(J+mP+r) + (2 if plant else 0)):
            ok3 = False
    return ok1, ok2, ok3

rng = random.Random(20261117)
for plant in (False, True):
    fails = [0, 0, 0]; N = 0
    for delta in range(1, 6):
        for _ in range(300):
            arc = rand_graph(2*delta+3, delta, rng)
            r = stats(arc, delta, plant); N += 1
            for i in range(3): fails[i] += (not r[i])
    print('planted' if plant else 'real   ', 'graphs', N, 'failures I1,I2,I3 =', fails)

# Lemma 3 (tight => covered) and Lemma 4 (<= 1 covered target per source), any oriented graph.
# Planted failure: the false claim "no source has a covered target" must be refuted on some graphs.
def lemmas34(arc, delta):
    n = len(arc); V = range(n)
    N1 = [{w for w in V if arc[v][w]} for v in V]
    N2 = [{w for u in N1[v] for w in V if arc[u][w] and w not in N1[v] and w != v} for v in V]
    R = [{v} | N1[v] | N2[v] for v in V]
    U = [set(V) - R[v] for v in V]
    T = [{y for y in V if y != x and not arc[y][x]} for x in V]
    P = [{v for v in V if x in U[v]} for x in V]
    tight_checked = bad3 = bad4 = covered_any = 0
    for x in V:
        if P[x] and 2*(len(T[x]) - delta) - 1 - len(P[x]) == 0:
            for v in P[x]:
                tight_checked += 1
                bad3 += not (T[x] <= R[v])
    for v in V:
        c = sum(1 for x in U[v] if T[x] <= R[v])
        bad4 += c > 1; covered_any += c > 0
    return tight_checked, bad3, bad4, covered_any

tot = [0, 0, 0, 0]
for delta in range(1, 6):
    for _ in range(300):
        r = lemmas34(rand_graph(2*delta+3, delta, rng), delta)
        tot = [a + b for a, b in zip(tot, r)]
print('Lemma3: tight (x,v) pairs checked', tot[0], 'violations', tot[1], '| Lemma4 violations', tot[2],
      '| planted claim "no covered target" refuted at', tot[3], 'sources')

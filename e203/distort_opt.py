"""Incremental optimiser for the distortion bound: per-stage term blocks; changing delta_k
recomputes only stage k and the stages whose terms involve coordinate k.  Uses the same cost
formula as distort_fast.costs (checked equal at the end)."""
import sys, json, numpy as np, scipy.sparse as sp
import distort_fast as D

def split(B):
    """per-stage (S1,w1,S2,w2) blocks and affected-stage lists."""
    S1, s1, w1 = B['T1']; S2, s2, w2 = B['T2']
    blocks = []; affected = [set() for _ in B['ells']]
    for s in range(B['nst']):
        r1 = np.where(s1 == s)[0]; r2 = np.where(s2 == s)[0]
        b = (S1[r1], w1[r1], S2[r2], w2[r2]); blocks.append(b)
        for q in set(b[0].indices) | set(b[2].indices): affected[q].add(s)
    for s, l in enumerate(B['stage_ells']): affected[B['idx'][l]].add(s)
    return blocks, [sorted(a) for a in affected]

def stage_cost(B, blocks, s, dvec, L):
    S1, w1, S2, w2 = blocks[s]
    m1 = float(w1 @ np.exp(S1 @ L)); m2 = float(w2 @ np.exp(S2 @ L))
    d = dvec[B['idx'][B['stage_ells'][s]]]; A = B['Acap'][s]
    if A <= d: return 0.0
    best = m1
    if d > 0:
        x = min(2 * d, A)
        if x > d: best = min(best, m2 * (x - d) / x ** 2)
        t = D.TS[D.TS >= 2 * d]
        if len(t): best = min(best, float(np.min((1 - 2 * d / t) * m1 + d / t ** 2 * m2)))
    return best / (1 - d)

def optimise(B, sweeps=3, grid=np.array([0.0] + [x / 100 for x in range(1, 96)])):
    blocks, affected = split(B)
    dvec = np.zeros(len(B['ells'])); L = -np.log1p(-dvec)
    cost = np.array([stage_cost(B, blocks, s, dvec, L) for s in range(B['nst'])])
    order = [B['idx'][l] for l in B['stage_ells']]
    for sw in range(sweeps):
        for k in order:
            aff = affected[k]; base = cost[aff].sum(); best = (0.0, dvec[k])
            for g in grid:
                old = dvec[k]; dvec[k] = g; L[k] = -np.log1p(-g)
                delta_sum = sum(stage_cost(B, blocks, s, dvec, L) for s in aff) - base
                if delta_sum < best[0] - 1e-15: best = (delta_sum, g)
                dvec[k] = old; L[k] = -np.log1p(-old)
            dvec[k] = best[1]; L[k] = -np.log1p(-best[1])
            for s in aff: cost[s] = stage_cost(B, blocks, s, dvec, L)
        print(f'  sweep {sw}: bound {cost.sum():.5f}', file=sys.stderr, flush=True)
    return dvec, cost

if __name__ == '__main__':
    pool = [json.loads(l) for l in open(sys.argv[1])]
    if len(sys.argv) > 2: pool = [p for p in pool if p['e'] <= int(float(sys.argv[2]))]
    B = D.build(pool)
    print(f"{sys.argv[1]} (e<={sys.argv[2] if len(sys.argv)>2 else 'all'}): {len(pool)} primes, "
          f"sum1/e={sum(1/p['e'] for p in pool):.4f}, stages {B['nst']}", flush=True)
    dvec, cost = optimise(B, sweeps=int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    chk = D.costs(B, dvec)[0].sum()
    print(f"DISTORTION BOUND = {cost.sum():.6f} (independent full recompute {chk:.6f}) -> "
          f"{'NO COVERING POSSIBLE' if chk < 1 else 'inconclusive'}", flush=True)
    for s in range(min(10, B['nst'])):
        l = B['stage_ells'][s]; print(f"   stage {l}: delta {dvec[B['idx'][l]]:.2f} cost {cost[s]:.4f}")
    print(f"   stages > {B['stage_ells'][min(10,B['nst'])-1]}: cost {cost[10:].sum():.4f}")
    np.save(sys.argv[1] + f".E{sys.argv[2] if len(sys.argv)>2 else 'all'}.delta.npy", dvec)

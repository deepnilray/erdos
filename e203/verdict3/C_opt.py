"""C_opt.py -- joint optimisation of the delta-vector for Theorem Z (objective N = smallest N with s(N) B'(delta) + N rho_max(delta) >= 1).
Variables: delta_q for the 78 primes 5<=q<=400 (in [0,0.6]) and one cap Cbig for all q>400 (their delta = min(run value, Cbig)).
B' via distort_fast.costs on the pickled build; rho_max via the sparse incidence sets of C_rhoset.py (same bound as C_size.py).
usage: python3 verdict3/C_opt.py [sweeps]   -> writes verdict3/C_opt_best.npz (full 15279-vector) and prints N."""
import sys, pickle, math, numpy as np
sys.path.insert(0, '.')
import distort_fast as D
E0 = 800000; OPT = 0.578318; LAM0 = 0.04850936; RMAX = 2.614450284594; LIM = 64 * E0
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv0 = z['dv'].copy(); idx = {l: i for i, l in enumerate(ells)}
Bp = pickle.load(open('verdict3/B_E800000.pkl', 'rb'))
R = pickle.load(open('/tmp/C_rhoset.pkl', 'rb')); qs = R['qs']
Ae, AS, Bme, BS = R['Ae'], R['AS'], R['Bme'], R['BS']
from math import gcd
RT = {1: 1.0}                                   # cyclic-type price r(gcd(e,144)) (C_allE.md sec 3d); OLD=1 restores RMAX
for _l in open('coupled_full_E200000.txt'):
    _k, _R = _l.split()[:2]; _a, _c, _d = map(int, _k.split(','))
    if gcd(gcd(_a, _c), _d) == 1: RT[_a * _d] = max(RT.get(_a * _d, 0.0), float(_R))
import os
rfun = (lambda e: RMAX if (e % 2 == 0 or e % 3 == 0) else 1.0) if os.environ.get('OLD') else (lambda e: RT[gcd(int(e), 144)])
RMX = RMAX if os.environ.get('OLD') else max(RT.values())
rA = np.array([rfun(e) for e in Ae]); lnA = np.log(Ae) - np.log(rA); rB = np.array([rfun(e) for e in Bme])
big = np.array([i for i, l in enumerate(ells) if l > 400]); qi = np.array([idx[q] for q in qs])
def full(dq, cb):
    d = dv0.copy(); d[big] = np.minimum(dv0[big], cb); d[qi] = dq; return d
def rho_max(dq, cb):
    Lq = -np.log1p(-dq); gmax = 1 / (1 - np.max(np.minimum(dv0[big], cb)))
    smooth = float(np.max(np.exp(AS @ Lq - lnA)))
    x = BS @ Lq
    large = max(float(np.max(rB * np.exp(x + w * math.log(gmax)) / np.maximum(Bme * 401 ** w, E0 + 1))) for w in (1, 2, 3, 4))
    large = max(large, RMX * (gmax / 401) ** 5, RMX * 16 / LIM)
    return max(smooth, large), smooth, large
def Nof(B1, c):
    ok = lambda N: (1 - OPT - LAM0) / (1 - OPT - LAM0 - N / E0) * B1 + N * c >= 1
    if B1 >= 1: return 0
    lo, hi = 0.0, E0 * (1 - OPT - LAM0) * 0.999
    if not ok(hi): return hi
    for _ in range(60):
        mid = (lo + hi) / 2
        if ok(mid): hi = mid
        else: lo = mid
    return hi
def evaluate(dq, cb):
    B1 = D.costs(Bp, full(dq, cb))[0].sum(); c = rho_max(dq, cb)
    return Nof(B1, c[0]), B1, c
if __name__ == '__main__':
    sweeps = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    dq = np.minimum(dv0[qi], 0.28); cb = 0.28
    N, B1, c = evaluate(dq, cb); print('start (cap .28): N=%.1f B\'=%.6f rho=%.4e (smooth %.4e large %.4e)' % ((N, B1) + (c[0], c[1], c[2])), flush=True)
    steps = [0.04, 0.02, 0.01, 0.005][:sweeps + 1]
    for sw in range(sweeps + 1):
        st = steps[sw]; imp = 0
        for k in list(range(len(qs))) + [-1]:
            for sgn in (+1, -1):
                while True:
                    dq2 = dq.copy(); cb2 = cb
                    if k >= 0: dq2[k] = min(max(dq[k] + sgn * st, 0.0), 0.6)
                    else: cb2 = min(max(cb + sgn * st, 0.0), 0.6)
                    if (k >= 0 and dq2[k] == dq[k]) or (k < 0 and cb2 == cb): break
                    N2, B2, c2 = evaluate(dq2, cb2)
                    if N2 > N + 1e-9: dq, cb, N, B1, c = dq2, cb2, N2, B2, c2; imp += 1
                    else: break
        print('sweep %d step %.3f: N=%.1f B\'=%.6f rho=%.4e  Cbig=%.3f  improvements %d' % (sw, st, N, B1, c[0], cb, imp), flush=True)
        np.savez('verdict3/C_opt_best.npz', dv=full(dq, cb), dq=dq, cb=cb, N=N, B1=B1, rho=c[0])
    print('dq =', np.round(dq, 3).tolist())

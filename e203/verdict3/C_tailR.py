"""C_tailR.py -- Theorem C' with hypotheses on WEIGHTED STAGE-RANGE sums (V_check.md 8.2 repair).
Per stage l a FIXED majorant is chosen from the model (kappa=1): either 'lin' (cost = cfin + RSTAR*Y1/(1-d)) or a moment majorant
cost = (a*m1 + b*m2)/(1-d) with (a,b) one of: (1,0); quadratic (0,(x-d)/x^2), x=min(2d,A); tangent (1-2d/t, d/t^2).  Then the stage cost is
LINEAR in the tail functionals Y1_l^> and X_l := cross_l + Q_l^>, with cross_l <= 2 sqrt(S2data_l Q_l^>) (theta-Cauchy-Schwarz).
Hypotheses, for each range R in RANGES (weights w_l, v_l printed to C_tailR_weights.npz):
   H_L^R(kL):  sum_{l in R} w_l Y1_l^>  <= kL * sum_{l in R} w_l Y1mod_l ,      w_l = RSTAR*(a + b/l)/(1-d)  (lin: RSTAR/(1-d))
   H_Q^R(kQ):  sum_{l in R} v_l Q_l^>   <= kQ^2 * sum_{l in R} v_l Qmod_l ,     v_l = TH*RSTAR*b/(1-d)
and sum_R v (2 sqrt(S Q) + Q) <= 2 sqrt(sum v S) sqrt(sum v Q) + sum v Q (Cauchy-Schwarz over l).
usage: python3 verdict3/C_tailR.py PIECES.npz kL kQ [eps] [choose_kQ]"""
import sys, numpy as np
z = np.load(sys.argv[1]); P = z['P']; RSTAR = float(z['RSTAR'])
kL, kQ = float(sys.argv[2]), float(sys.argv[3]); EPS = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0; kC = float(sys.argv[5]) if len(sys.argv) > 5 else kQ
TH = 1 + EPS; A = 1.0
RANGES = [(5, 7), (7, 12), (12, 30), (30, 100), (100, 1000), (1000, 10**4), (10**4, 10**5), (10**5, 10**9)]
TS = np.linspace(0, 1, 801)[1:]
L, d, cfin, M1F, M2F, Y1, S, Qm = P.T
def options(i):
    di = d[i]; o = [(1.0, 0.0)]
    if di > 0:
        x = min(2 * di, A)
        if x > di: o.append((0.0, (x - di) / x ** 2))
        for t in TS[TS >= 2 * di]: o.append((1 - 2 * di / t, di / t ** 2))
    return o
w = np.zeros(len(L)); v = np.zeros(len(L)); fixed = np.zeros(len(L))
for i in range(len(L)):
    li, di = L[i], d[i]
    # model values at the choice point (kL=1? use kC for the quadratic part so the choice is made where the theorem is applied)
    m1 = M1F[i] + RSTAR * Y1[i]; m2 = M2F[i] + TH * RSTAR * (2 * kC * np.sqrt(S[i] * Qm[i]) + kC ** 2 * Qm[i]) + RSTAR * Y1[i] / li
    best = (cfin[i] + RSTAR * Y1[i] / (1 - di), 'lin', None)
    for a, b in options(i):
        c = (a * m1 + b * m2) / (1 - di)
        if c < best[0]: best = (c, 'mom', (a, b))
    if best[1] == 'lin': fixed[i] = cfin[i]; w[i] = RSTAR / (1 - di)
    else:
        a, b = best[2]; fixed[i] = (a * M1F[i] + b * M2F[i]) / (1 - di); w[i] = RSTAR * (a + b / li) / (1 - di); v[i] = TH * RSTAR * b / (1 - di)
import os
KLR = [float(x) for x in os.environ['KLR'].split(',')] if os.environ.get('KLR') else None      # per-range kappa_L
KQ2R = [float(x) for x in os.environ['KQ2R'].split(',')] if os.environ.get('KQ2R') else None   # per-range kappa_Q^2
tot = 0.0; rows = []
for ri, (lo, hi) in enumerate(RANGES):
    if KLR: kL = KLR[ri]
    if KQ2R: kQ = KQ2R[ri] ** 0.5
    m = (L >= lo) & (L < hi)
    if not m.any(): continue
    lin = kL * (w[m] * Y1[m]).sum(); vQ = kQ ** 2 * (v[m] * Qm[m]).sum(); vS = (v[m] * S[m]).sum()
    t = fixed[m].sum() + lin + 2 * np.sqrt(vS * vQ) + vQ
    rows.append((lo, hi, t)); tot += t
ext = 4e-5 * max(kL, kQ ** 2)       # (with per-range kappas: those of the last range)       # stages beyond the computed range, scaled
print('kL=%.2f kQ=%.2f eps=%.2f (choice at kQ=%.2f): total %.4f (+ tail beyond computed stages %.1e)' % (kL, kQ, EPS, kC, tot + ext, ext))
print('   by range:', ' '.join('[%g,%g):%.4f' % r for r in rows))
np.savez('verdict3/C_tailR_weights.npz', L=L, w=w, v=v, fixed=fixed)

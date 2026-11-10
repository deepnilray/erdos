"""a4/kappa_fit.py -- 4_tail.md section 7. Fits total(kL,kQ) = A + B*kL + X*kQ + Q*kQ^2 to the UNIFORM-kappa totals logged in
verdict3/C_tailR.log (run-delta profile; majorant re-chosen at each kQ), holds one point out as a check, and extrapolates to the kappa
implied by a pointwise multiplicity bound n(e) <= s for e > E0:  kappa = s / tau,  tau = C0/ln(E0) (n_hat = kappa*tau*e/phi(e) >= kappa*tau).
This is an extrapolation of logged numbers, not a rerun (pieces file C_tailpieces_L1000.npz is gitignored and absent)."""
import numpy as np, math, re
rows = []
for line in open('verdict3/C_tailR.log'):
    m = re.match(r'kL=([\d.]+) kQ=([\d.]+) eps=0.00 \(choice at kQ=([\d.]+)\): total ([\d.]+)', line)
    if m and abs(float(m.group(2)) - float(m.group(3))) < 1e-9: rows.append(tuple(map(float, (m.group(1), m.group(2), m.group(4)))))
print("uniform rows:", rows)
hold = [r for r in rows if r[:2] == (1.0, 1.34)]; fit = [r for r in rows if r[:2] != (1.0, 1.34)]
M = np.array([[1, kl, kq, kq * kq] for kl, kq, _ in fit]); y = np.array([t for _, _, t in fit])
coef, *_ = np.linalg.lstsq(M, y, rcond=None); A, B, X, Q = coef
print("A,B,X,Q =", coef.round(5), " max fit residual", np.abs(M @ coef - y).max().round(5))
for kl, kq, t in hold: print(f"held-out ({kl},{kq}): logged {t}, fit {A + B*kl + X*kq + Q*kq*kq:.4f}")
# control: a planted wrong row must show a large residual
Mc = np.vstack([M, [1, 1.0, 1.34, 1.34**2]]); yc = np.append(y, 1.05)
cc, *_ = np.linalg.lstsq(Mc, yc, rcond=None); print("control (planted total 1.05 at (1,1.34)): max residual", np.abs(Mc @ cc - yc).max().round(4))
kstar = (-(B + X) + math.sqrt((B + X) ** 2 + 4 * Q * (1 - A))) / (2 * Q)
print(f"uniform kappa at which the fitted total reaches 1: {kstar:.3f}")
tau = 0.813 / math.log(8e5)
for s in (1, 2, 4):
    for k in (s / tau, s / (2.5 * tau)):
        print(f"s={s}: kappa={k:.2f}  fitted total {A + (B + X) * k + Q * k * k:.2f}")

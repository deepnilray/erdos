"""
Pilot: does the Lyman-alpha primordial-magnetic-field (PMF) hint (B_1Mpc ~ 0.2 nG, n_B = -2.9; Pavicevic et al. 2025,
arXiv:2501.06299) survive the strong-lensing measurement of the small-scale matter power spectrum (Gilman et al. 2022,
arXiv:2112.03293)?

PMF-induced linear power: Ralegankar, Pavicevic & Viel 2024 (arXiv:2402.14079), Eq. Delta_b:
  Delta^2_b(k) = 1e-4 xi_b(a)^2 (k/Mpc^-1)^(2 n_B + 10) (B_1Mpc/nG)^4 G_nB exp(-2 k^2 lambda_D^2)
  lambda_D = (0.1 kappa B_1Mpc)^(2/(n_B+5)) Mpc   (their Eqs. B_B1mpc, lamkap; Pavicevic Eq. 1)
  kappa = (G_nB / (1.14 eta))^(1/4); eta = 0.1 -> kappa_-2.9 = 0.88 (value used by Pavicevic); G_-2.9 = 1.14 eta kappa^4.
The matter growth factor xi_m(a) is obtained here by integrating the paper's two-fluid equations (matter era, source switched
on at recombination); control: xi_b(a = 0.01) must come out near 2.5 as stated in the paper.
LCDM linear power from CAMB (Planck-like). Ratio evaluated at z = 30 (matter era, after both modes grow as a).
Lensing: log10(P/P_LCDM) = 0.0 +0.4/-0.4 (k=10), 0.1 +0.7/-0.6 (k=25), 0.2 +1.0/-0.9 (k=50 Mpc^-1), 68% (Gilman+22 abstract).
"""
import numpy as np, camb
from scipy.integrate import solve_ivp

Om, Ob = 0.308, 0.0482
fb, fc = Ob / Om, 1 - Ob / Om
def rhs(x, y):  # x = ln a; y = (db, db', dc, dc'); source s = 1 (constant in matter era)
    db, dbp, dc, dcp = y; grav = 1.5 * (fb * db + fc * dc)
    return [dbp, -0.5 * dbp + grav + 1.0, dcp, -0.5 * dcp + grav]
arec = 1 / 1100.
sol = solve_ivp(rhs, [np.log(arec), np.log(1 / 31.)], [0, 0, 0, 0], dense_output=True, rtol=1e-8)
def xi(a):
    db, _, dc, _ = sol.sol(np.log(a)); return db, dc, fb * db + fc * dc
xb01, xc01, xm01 = xi(0.01)
print(f"control: xi_b(0.01) = {xb01:.2f} (paper: ~2.5); xi_DM(0.01) = {xc01:.2f}; xi_m(0.01) = {xm01:.2f}")
a_eval = 1 / 31.
xb, xc, xm = xi(a_eval)
print(f"xi_m(z=30) = {xm:.1f}")

def delta2_pmf(k, B, nB=-2.9, kappa=0.88, eta=0.1):
    G = 1.14 * eta * kappa ** 4
    lamD = (0.1 * kappa * B) ** (2 / (nB + 5))
    return 1e-4 * xm ** 2 * k ** (2 * nB + 10) * B ** 4 * G * np.exp(-2 * k ** 2 * lamD ** 2), lamD

pars = camb.CAMBparams(); pars.set_cosmology(H0=67.8, ombh2=Ob * 0.678 ** 2, omch2=(Om - Ob) * 0.678 ** 2)
pars.InitPower.set_params(ns=0.961, As=2.1e-9); pars.set_matter_power(redshifts=[30.], kmax=300.)
res = camb.get_results(pars)
kh, z, pk = res.get_matter_power_spectrum(minkh=1e-2, maxkh=200, npoints=600)
k = kh * 0.678; P = pk[0] / 0.678 ** 3            # Mpc^-1, Mpc^3
D2l = k ** 3 * P / (2 * np.pi ** 2)
lens = {10: (0.0, 0.4, 0.4), 25: (0.1, 0.7, 0.6), 50: (0.2, 1.0, 0.9)}
print("\nB_1Mpc(nG)  k_peak(Mpc^-1)  log10(P_tot/P_LCDM) at k=10, 25, 50  |  pull vs lensing (sigma, one-sided, 68% widths)")
for B in (0.05, 0.1, 0.15, 0.2, 0.3, 0.5):
    d2, lamD = delta2_pmf(k, B); kpk = k[np.argmax(d2)]
    row, pulls = [], []
    for kk, (mu, up, lo) in lens.items():
        r = np.log10(1 + np.interp(kk, k, d2) / np.interp(kk, k, D2l)); row.append(r)
        pulls.append((r - mu) / up if r > mu else (r - mu) / lo)
    print(f"  {B:5.2f}      {kpk:7.1f}        " + "  ".join(f"{r:6.2f}" for r in row) + "   |  " + "  ".join(f"{p:+.1f}" for p in pulls))
# control: B -> 0 gives zero boost
print("\ncontrol B=1e-4:", np.log10(1 + np.interp(25, k, delta2_pmf(k, 1e-4)[0]) / np.interp(25, k, D2l)))

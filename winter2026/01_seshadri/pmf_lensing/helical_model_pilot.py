"""
Pilot (order of magnitude): is the helical inflationary magnetogenesis model of Sharma, Subramanian & Seshadri 2018
(PRD 97, 083503; arXiv:1802.04847) already constrained by the small-scale matter power that primordial magnetic fields (PMFs)
induce, given the Lyman-alpha forest bound/hint (Pavicevic et al. 2025, arXiv:2501.06299) and JWST (arXiv:2604.24835)?

Method
- PMF-sourced baryon power: the general integral of Ralegankar, Pavicevic & Viel 2024 (arXiv:2402.14079, Eq. Pb_int), evaluated
  numerically for an arbitrary magnetic spectrum P_B(q). It is the NON-helical kernel; the helical part of the Lorentz-force
  power is NOT included (that is the open calculation). Treat results as indicative only.
- Absolute normalisation is calibrated on the paper's closed-form power-law result (Eq. Delta_b, with G_nB from kappa and eta);
  two independent calibrations (n_B = -2.9 and -2.5) must agree: that is the control.
- Model spectrum today: d rho_B / d ln k  ~ k^4 below k_c and ~ k^(-2/3) above (k^4 as generated in 1802.04847; Kolmogorov-like
  tail assumed), k_c = 2 pi / L_c, normalised to the total field B_0. (B_0, L_c) are the maximal values of Table 1 of
  1802.04847 (with nonlinear helical decay), at reheating temperatures 5 MeV, 150 MeV, 100 GeV, 1000 GeV.
- Damping exp(-k^2 lambda_D^2), lambda_D = 0.1 kappa (B_0/nG) Mpc, kappa = 0.88 (as used by Pavicevic et al.).
- Matter growth xi_m(z=30) from the two-fluid equations (see pmf_vs_lensing.py); LCDM from CAMB at z = 30.
- Reference: power-law models n_B = -2.9 with B_1Mpc = 0.2 nG (Ly-a hint), 0.3 nG (Ly-a 3-sigma bound), 0.5 nG (excluded).
"""
import numpy as np, camb
from scipy.special import gamma
from scipy.integrate import solve_ivp

Om, Ob = 0.308, 0.0482; fb, fc = Ob / Om, 1 - Ob / Om
def rhs(x, y):
    db, dbp, dc, dcp = y; g = 1.5 * (fb * db + fc * dc); return [dbp, -0.5 * dbp + g + 1, dcp, -0.5 * dcp + g]
sol = solve_ivp(rhs, [np.log(1 / 1100), np.log(1 / 31)], [0, 0, 0, 0], rtol=1e-8)
xb, xc = sol.y[0, -1], sol.y[2, -1]; xm = fb * xb + fc * xc
XB01 = 2.5  # paper's xi_b(0.01), used only inside the calibration constant

def bracket(x, y): return 1 + 2 * x**2 + 4 * x**2 * y**4 - 4 * x**2 * y**2 - 4 * x * y**3 + y**2

def I_of_k(k, PB, nx=500, nu=200):
    """J(k) = int d^3q/(2pi)^3 PB(q) PB(|k-q|)/|k-q|^2 * [bracket]  (bracket in units of k^2), in (x=q/k, u=|k-q|/k)."""
    x = np.logspace(-4, 3, nx); tot = np.zeros_like(x)
    for i, xi in enumerate(x):
        lo = max(abs(1 - xi), 1e-7); u = np.logspace(np.log10(lo), np.log10(1 + xi), nu)
        y = np.clip((1 + xi**2 - u**2) / (2 * xi), -1, 1)
        f = PB(k * xi) * PB(k * u) / (k * u) ** 2 * k**2 * bracket(xi, y) * (2 * np.pi * k**3 * xi * u) / (2 * np.pi) ** 3
        tot[i] = np.trapezoid(f * u, np.log(u))
    return np.trapezoid(tot * x, np.log(x))

def powerlaw_PB(B1, nB):
    A = B1**2 * 4 * np.pi**2 / gamma((nB + 3) / 2)   # Mpc units, lambda = 1 Mpc
    return lambda q: A * q**nB

# calibration: Delta_b = C * xi^2 * k^7 * J(k), with C fixed by the closed form at k = 1, B1 = 1
def G_of(kappa, eta): return 1.14 * eta * kappa**4
Cs = []
for nB, kap, eta in ((-2.5, 1.07, 0.3), (-2.0, 1.36, 0.3)):   # n_B=-2.9 is too IR-sensitive for this grid (see note)
    J = I_of_k(1.0, powerlaw_PB(1.0, nB)); Cs.append(1e-4 * G_of(kap, eta) / J)
print("calibration constants (must agree): %.3e  %.3e  ratio %.2f" % (Cs[0], Cs[1], Cs[0] / Cs[1]))
C = Cs[0]
# note: for n_B = -2.9 the integrand ~ x^-0.9 near x -> 0 converges too slowly for this grid (numeric G = 0.043 vs 0.069
# from the paper), so the reference n_B = -2.9 models below use the paper's closed form instead of the numerical integral.

pars = camb.CAMBparams(); pars.set_cosmology(H0=67.8, ombh2=Ob * 0.678**2, omch2=(Om - Ob) * 0.678**2)
pars.InitPower.set_params(ns=0.961, As=2.1e-9); pars.set_matter_power(redshifts=[30.], kmax=400.)
kh, _, pk = camb.get_results(pars).get_matter_power_spectrum(minkh=1e-2, maxkh=300, npoints=500)
kl = kh * 0.678; D2l = kl**3 * pk[0] / 0.678**3 / (2 * np.pi**2)
ks = np.array([3, 5, 10, 20, 30, 50, 80])

def delta2_m(PB, lamD):
    PBd = lambda q: PB(q) * np.exp(-q**2 * lamD**2)
    return np.array([C * xm**2 * k**7 * I_of_k(k, PBd) for k in ks])
# C was calibrated against Delta_b with xi = 1 in front, so C * xm^2 * k^7 * J is the matter power with growth xi_m.

def report(name, d2):
    r = np.log10(1 + d2 / np.interp(ks, kl, D2l))
    print(f"{name:34s} " + " ".join(f"{v:6.2f}" for v in r))

print("\nlog10(P_total / P_LCDM) at k [Mpc^-1] =", " ".join(f"{k:6d}" for k in ks))
for B1 in (0.2, 0.3, 0.5):
    lamD = (0.1 * 0.88 * B1) ** (2 / (-2.9 + 5))
    d2 = 1e-4 * (xm / XB01 * 2.5) ** 2 * ks ** (2 * -2.9 + 10) * B1 ** 4 * G_of(0.88, 0.1) * np.exp(-2 * ks ** 2 * lamD ** 2)
    report(f"ref n_B=-2.9, B_1Mpc={B1} nG", d2)

table = {"5 MeV": (6.41, 1.62), "150 MeV": (0.990, 0.58), "100 GeV": (0.0392, 0.068), "1000 GeV": (0.00712, 0.032)}
for eps in (1.0, 1e-2):
    for name, (B0, Lc) in table.items():
        B = B0 * np.sqrt(eps); kc = 2 * np.pi / Lc
        shape = lambda q: np.where(q < kc, (q / kc) ** 4, (q / kc) ** (-2 / 3))   # d rho/d ln k
        lnq = np.linspace(np.log(kc) - 12, np.log(kc) + 12, 4000)
        norm = B**2 / np.trapezoid(shape(np.exp(lnq)), lnq)
        PB = lambda q, norm=norm: norm * shape(q) * 2 * np.pi**2 / q**3   # B^2 = int dlnk k^3 PB/(2pi^2)
        lamD = 0.1 * 0.88 * B
        report(f"SSS18 T_r={name}, eps={eps:g} (B={B:.3g} nG)", delta2_m(PB, lamD))
print("\ncontrol: xi_m(z=30) =", round(xm, 2))

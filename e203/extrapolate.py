"""HEURISTIC extrapolation of the merged-{2,3} distortion bound to E = infinity.
Model (fitted on the certified pool e <= 2e5): #{p : e_p = e} has mean kappa (e/phi(e))/log e,
kappa = 0.815 (largest fitted value), directions uniform.  For stage ell the missing mass is
   T_ell = sum_{e > E, P+(e) = ell} nbar(e)/e ~ kappa * mu / ell * Int_{t0}^inf rho(t/log ell)/(log ell + t) dt,
t0 = max(0, log(E/ell)), mu = mean of n/phi(n) = 315 zeta(3)/(2 pi^4) ~ 1.9436 (rho = Dickman).
Existing stages scale T by their empirical mean weight (Lam*r); cross terms by their empirical
overlap factor gamma = cross(m2) / (m1^2 - sum w^2).  Each stage's delta is re-optimised locally."""
import sys, json, math, numpy as np
from sympy import factorint, primerange
import distort23 as D23, distort_fast as D

SAFETY = {5: 1.7}; SAFETY_DEFAULT = 1.3
KAPPA, MU = 0.815, 315 * 1.2020569031595942 / (2 * math.pi ** 4)

def dickman(umax=40, h=1e-3):
    n = int(umax / h) + 1; r = np.ones(n); u = np.arange(n) * h
    k1 = int(1 / h)
    for i in range(k1 + 1, n):             # rho'(u) = -rho(u-1)/u, trapezoid
        r[i] = r[i - 1] - h * 0.5 * (r[i - k1] / u[i] + r[i - 1 - k1] / u[i - 1])
    return lambda x: np.interp(x, u, r, right=0.0)
RHO = dickman()

def tail_mass(ell, E):
    L = math.log(ell); t0 = max(0.0, math.log(E / ell))
    t = np.linspace(t0, t0 + 40 * L, 4000)
    f = RHO(t / L) / (L + t)
    return KAPPA * MU / ell * float(np.trapezoid(f, t)) * (1 + 1 / ell)   # (1 + 1/ell): ell^2 | e

def stage_cost(m1, m2, A=1.0):
    best = m1
    for d in np.linspace(0.01, 0.95, 95):
        c = [m1]
        x = min(2 * d, A)
        if x > d: c.append(m2 * (x - d) / x ** 2)
        t = np.linspace(2 * d, 2 * d + 1, 400); c.append(np.min((1 - 2 * d / t) * m1 + d / t ** 2 * m2))
        best = min(best, min(c) / (1 - d))
    return best

# ---- exact discrete tail for small stages -------------------------------------------------
from sympy import primerange as _pr
def smooth_tail_exact(ell, E, cap):
    """sum over e in (E, cap], P+(e) = ell, of kappa (e/phi(e)) / (e log e)."""
    ps = list(_pr(2, ell + 1)); tot = 0.0
    def dfs(i, e, ratio, has_ell):
        nonlocal tot
        if e > E and has_ell: tot += KAPPA * ratio / (e * math.log(e))
        for j in range(i, len(ps)):
            p = ps[j]; x = e * p
            if x > cap: break
            r = ratio * p / (p - 1) if e % p else ratio
            dfs(j, x, r, has_ell or p == ell)
    dfs(0, 1, 1.0, False)
    return tot

def tail_mass_best(ell, E, exact_upto=97, E2=None):
    if E2 is not None:
        if ell > exact_upto: return tail_mass(ell, E) - tail_mass(ell, E2)
        return smooth_tail_exact(ell, E, E2)
    if ell > exact_upto: return tail_mass(ell, E)
    cap = 10 ** 11 if ell <= 23 else (10 ** 9 if ell <= 53 else 10 ** 8)
    rem = tail_mass(ell, max(E, cap)) * (1.5 if ell <= 53 else 1.3)   # Dickman remainder, inflated
    return smooth_tail_exact(ell, E, cap) + rem


if __name__ == '__main__':
    pool = [json.loads(l) for l in open(sys.argv[1])]; E = int(float(sys.argv[2]))
    heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]; a_h = float(sys.argv[3]); Lmax = int(float(sys.argv[4]))
    E2 = int(float(sys.argv[6])) if len(sys.argv) > 6 else None
    sub = [p for p in pool if p['e'] <= E]
    light = sum(1 / p['e'] for p in sub if max(factorint(p['e'])) <= 3 and p['p'] not in heavy)
    # first-stage light tail: 3-smooth e > E
    def e_over_phi(e): return (2.0 if e % 2 == 0 else 1.0) * (1.5 if e % 3 == 0 else 1.0)
    light_tail = sum(KAPPA * e_over_phi(e) / math.log(e) / e
                     for e in (2 ** i * 3 ** j for i in range(100) for j in range(64)) if E < e < 1e30)
    B = D23.build(sub, heavy, a_h + light + light_tail)
    dv = np.load(sys.argv[5]); c, m1, m2 = D.costs(B, dv)
    S1, s1, w1 = B['T1']
    base = D.costs(B, dv)[0].sum()
    raw = np.bincount(s1, w1, minlength=B['nst'])            # sum of r/e (no Lambda)
    sumw2 = np.bincount(s1, w1 ** 2, minlength=B['nst'])
    gam_all = []
    tot = 0.0; rows = []
    for i, l in enumerate(B['stage_ells']):
        wbar = m1[i] / raw[i] if raw[i] > 0 else 1.0
        denom = m1[i] ** 2 - (sumw2[i] * wbar ** 2)
        S2, s2, w2 = B['T2']; dr = B['diag_rows']
        diag = float((w2[dr] * np.exp(S2[dr] @ (-np.log1p(-dv))))[s2[dr] == i].sum())
        g = max(0.0, (m2[i] - diag) / denom) if denom > 1e-12 else 1.0
        gam_all.append(g)
        dm1 = wbar * SAFETY.get(l, SAFETY_DEFAULT) * tail_mass_best(l, E, E2=E2)
        M1 = m1[i] + dm1; M2 = m2[i] + dm1 / l + g * (2 * m1[i] * dm1 + dm1 ** 2)
        cst = stage_cost(M1, M2); tot += cst; rows.append((l, m1[i], dm1, c[i], cst))
    g_med = float(np.median(gam_all)); wbar_g = float(np.median([r[1] / max(1e-12, raw[i]) for i, r in enumerate(rows)]))
    new = 0.0; present = set(B['stage_ells'])
    for l in primerange(5, Lmax):
        if l in present: continue
        if E2 is not None and l > E2: continue
        dm1 = wbar_g * SAFETY_DEFAULT * tail_mass_best(l, E, E2=E2); new += stage_cost(dm1, dm1 / l + g_med * dm1 ** 2)
    beyond = 2.0 * wbar_g ** 2 * (KAPPA * MU) ** 2 / (Lmax * math.log(Lmax))   # sum_{ell>Lmax} ~ C/ell^2
    print(f"E={E}: rigorous bound at E = {base:.4f};  HEURISTIC limit: existing stages {tot:.4f} + new stages "
          f"<= {Lmax:.0e}: {new:.4f} + beyond ~{beyond:.4f}  =>  B_heur(inf) ~ {tot + new + beyond:.4f}")
    print('  largest heuristic increments:', sorted(((round(r[4] - r[3], 4), r[0]) for r in rows), reverse=True)[:8])


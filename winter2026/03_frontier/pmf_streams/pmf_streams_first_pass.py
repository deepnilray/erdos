"""
First-pass estimate: what do Gaia stellar-stream subhalo measurements say about a
primordial magnetic field (PMF)?

Inputs taken from two published papers (both read in full text on 2026-11-16):
  [S20] Sanati et al. 2020, arXiv:2005.05401, Eq. (12) + Table 2:
        ratio of PMF halo mass function to LCDM, (c-1) exp(-(log10 M - u)^2 / 2 s^2) + 1,
        fitted to dark-matter-only simulations for n_B = -2.9 and B_lambda = 0.05, 0.10, 0.20, 0.50 nG.
  [B21] Banik et al. 2021, arXiv:1911.02663, Eqs. (2.2)-(2.4):
        posterior of r = log10(n_sub / n_sub,CDM) from the GD-1 + Pal 5 streams in two mass bins.

Everything else here (interpolation in B, priors, forecast) is a modelling choice of this script
and is labelled as such.  Status of the output: VERIFIED numerics on a CONJECTURED model chain
(see README, section "What is assumed").
"""
import numpy as np, json

# ---------- [S20] Table 2, n_B = -2.9 -------------------------------------------------
S20 = {0.05: (3.00, 5.30, 0.80), 0.10: (4.50, 6.17, 0.70), 0.20: (4.06, 7.08, 0.70), 0.50: (3.86, 8.45, 0.67)}
_lB = np.log10(sorted(S20)); _c = [S20[b][0] for b in sorted(S20)]
_u = [S20[b][1] for b in sorted(S20)]; _s = [S20[b][2] for b in sorted(S20)]

def cus(B):
    """(c,u,s) at field B [nG]: linear interpolation in log10 B; u extrapolated linearly outside the grid
    (magnetic Jeans mass scales as a power of B), c and s held at the edge values. MODELLING CHOICE."""
    lb = np.log10(B)
    u = np.interp(lb, _lB, _u)
    if lb < _lB[0]:  u = _u[0] + (lb-_lB[0])*(_u[1]-_u[0])/(_lB[1]-_lB[0])
    if lb > _lB[-1]: u = _u[-1] + (lb-_lB[-1])*(_u[-1]-_u[-2])/(_lB[-1]-_lB[-2])
    return np.interp(lb, _lB, _c), u, np.interp(lb, _lB, _s)

def ratio(M, B):
    c, u, s = cus(B)
    return (c-1)*np.exp(-(np.log10(M)-u)**2/(2*s*s)) + 1

def bin_boost(lo, hi, B, alpha=-1.9, n=4000):
    """number-weighted mean of the ratio over a mass bin, CDM weight dN/dM ~ M^alpha ([B21] Eq. 2.1)."""
    lm = np.linspace(lo, hi, n); M = 10**lm
    w = M**(alpha+1)                      # dN/dlogM
    return np.trapezoid(w*ratio(M, B), lm)/np.trapezoid(w, lm)

# ---------- [B21] Eqs. (2.2)-(2.4) ----------------------------------------------------
def lnp_78(r):  return -np.abs(r+0.5)**2.5/(2*0.5**2)
def lnp_89(r):  return np.where(r < -0.7, -(r+0.7)**2/(2*0.3**2), -(r+0.7)**2/(2*0.6**2))

def lnlike(B, lf, lc0=0.0, use_field=True):
    b1 = bin_boost(7, 8, B) if use_field else 1.0
    b2 = bin_boost(8, 9, B) if use_field else 1.0
    return lnp_78(lc0+lf+np.log10(b1)) + lnp_89(lc0+lf+np.log10(b2))

def posterior_B(Bgrid, f_lo, f_hi, sig_c0=0.2):
    """marginalise over survival fraction (log-uniform in [f_lo,f_hi]) and CDM normalisation
    (log-normal, sig_c0 dex; [B21] find c0 ~ 1.6 from classical satellites, we centre on that)."""
    lfs = np.linspace(np.log10(f_lo), np.log10(f_hi), 241)
    lcs = np.log10(1.6) + np.linspace(-3, 3, 61)*sig_c0
    wc = np.exp(-0.5*((lcs-np.log10(1.6))/sig_c0)**2)
    post = []
    for B in Bgrid:
        b1, b2 = np.log10(bin_boost(7, 8, B)), np.log10(bin_boost(8, 9, B))
        L = 0.0
        for lc, w in zip(lcs, wc):
            L += w*np.trapezoid(np.exp(lnp_78(lc+lfs+b1)+lnp_89(lc+lfs+b2)), lfs)
        post.append(L/(lfs[-1]-lfs[0]))
    post = np.array(post); return post/post.max()

def upper95(Bgrid, post):
    lb = np.log10(Bgrid); cdf = np.cumsum(post); cdf /= cdf[-1]
    return 10**np.interp(0.95, cdf, lb)

if __name__ == "__main__":
    out = {}
    print("bin-averaged subhalo boost over LCDM (n_B=-2.9):")
    print(" B[nG]  peak log10M   [1e5,1e6] [1e6,1e7] [1e7,1e8] [1e8,1e9]")
    rows = []
    for B in (0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 1.0):
        bb = [bin_boost(a, a+1, B) for a in (5, 6, 7, 8)]
        rows.append((B, cus(B)[1], *bb))
        print(f" {B:5.2f}   {cus(B)[1]:6.2f}      " + "    ".join(f"{x:5.2f}" for x in bb))
    out["boost_table"] = rows

    # control 1 (must reproduce the input): B -> tiny field gives boost -> 1 in the stream bins
    assert abs(bin_boost(7, 8, 0.005)-1) < 1e-3 and abs(bin_boost(8, 9, 0.005)-1) < 1e-3
    # control 2 (planted failure that MUST fire): a x30 boost in both bins must be strongly disfavoured
    planted = (lnp_78(np.log10(0.22*30)) + lnp_89(np.log10(0.22*30))) - (lnp_78(np.log10(0.22)) + lnp_89(np.log10(0.22)))
    assert planted < -5, planted
    print(f"\ncontrols: zero-field limit OK; planted x30 boost gives delta lnL = {planted:.1f} (fires)")

    Bgrid = 10**np.linspace(np.log10(0.02), np.log10(2.0), 121)
    for name, (flo, fhi) in {"wide f_survive prior [1e-4,0.5] (as in B21)": (1e-4, 0.5),
                             "simulation-motivated f_survive in [0.1,0.5]": (0.1, 0.5),
                             "fixed f_survive = 0.22 (B21 best fit)": (0.2199, 0.2201)}.items():
        post = posterior_B(Bgrid, flo, fhi)
        ul = upper95(Bgrid, post)
        out[name] = {"B95_nG": float(ul), "post_at_0.05": float(np.interp(np.log10(0.05), np.log10(Bgrid), post)),
                     "post_min": float(post.min()), "B_at_min": float(Bgrid[post.argmin()])}
        excl = Bgrid[post < 0.05]
        out[name]["excluded_window_nG"] = [float(excl.min()), float(excl.max())] if len(excl) else None
        print(f"\n{name}\n   relative posterior at 0.05 nG: {out[name]['post_at_0.05']:.2f}"
              f"   | lowest relative posterior {post.min():.3f} at B={Bgrid[post.argmin()]:.2f} nG"
              f"   | field values with relative posterior < 0.05: {out[name]['excluded_window_nG']}")

    # ---------- forecast: add a measured [1e6,1e7] bin and a [1e5,1e6] bin -----------------
    print("\nFORECAST (hypothetical future data consistent with LCDM, f_survive in [0.1,0.5]):")
    for sig in (0.5, 0.3, 0.2, 0.15, 0.1):
        lfs = np.linspace(-1, np.log10(0.5), 121); post = []
        for B in Bgrid:
            b = [np.log10(bin_boost(a, a+1, B)) for a in (5, 6, 7, 8)]
            L = np.trapezoid(np.exp(sum(-(lfs+bi-np.log10(0.22))**2/(2*sig*sig) for bi in b)), lfs)
            post.append(L)
        post = np.array(post)/max(post)
        excl = Bgrid[post < 0.05]; win = [float(excl.min()), float(excl.max())] if len(excl) else None
        print(f"   four decade bins 1e5-1e9 each measured to {sig:.2f} dex: field values with relative posterior < 0.05: {win}"
              f"   (relative posterior at 0.05 nG: {np.interp(np.log10(0.05), np.log10(Bgrid), post):.3f})")
        out[f"forecast_sig{sig}"] = win
    json.dump(out, open("first_pass_results.json", "w"), indent=1)

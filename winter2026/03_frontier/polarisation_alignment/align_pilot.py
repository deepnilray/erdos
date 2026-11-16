"""
PILOT: coordinate-invariant test for large-scale alignment of intrinsic (Faraday-derotated)
radio polarisation angles, on the sources of the Van Eck et al. (2023) consolidated RM catalogue
v1.2.0 (github.com/CIRADA-Tools/RMTable) that carry a derotated angle.

Statistic (Jain, Narain & Sarala 2004 style): for source i with n_v nearest neighbours k,
   d_i = | (1/n_v) sum_k exp(2 i psi_k->i) |,   S_D = mean_i d_i,
where psi_k->i is the angle of k parallel-transported along the great circle to i.
Significance: shuffle angles among positions (keeps the sky footprint, destroys any real alignment).

Usage: python3 align_pilot.py /path/to/consolidated_catalog_ver1.2.0.fits
"""
import sys, numpy as np, json, collections
from astropy.table import Table
rng = np.random.default_rng(20261116)

def unit(ra, dec):
    ra, dec = np.radians(ra), np.radians(dec)
    return np.c_[np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)]

def bearing(ra1, dec1, ra2, dec2):
    """position angle (N through E) at point 1 of the great circle towards point 2; radians."""
    ra1, dec1, ra2, dec2 = map(np.radians, (ra1, dec1, ra2, dec2)); dl = ra2-ra1
    return np.arctan2(np.sin(dl)*np.cos(dec2), np.cos(dec1)*np.sin(dec2)-np.sin(dec1)*np.cos(dec2)*np.cos(dl))

def neighbours(ra, dec, nv):
    X = unit(ra, dec); C = X @ X.T; np.fill_diagonal(C, -2)
    return np.argsort(-C, axis=1)[:, :nv]

def transport_phases(ra, dec, nb):
    """phase factor exp(2i*(bearing(i->k) - bearing(k->i))) for every (i, neighbour k)."""
    i = np.arange(len(ra))[:, None]
    return np.exp(2j*(bearing(ra[i], dec[i], ra[nb], dec[nb]) - bearing(ra[nb], dec[nb], ra[i], dec[i])))

def S_D(psi, nb, ph):
    return np.abs((np.exp(2j*psi)[nb]*ph).mean(axis=1)).mean()

def test(ra, dec, psi, nv, nshuf=2000):
    nb = neighbours(ra, dec, nv); ph = transport_phases(ra, dec, nb)
    s = S_D(psi, nb, ph); sh = np.array([S_D(rng.permutation(psi), nb, ph) for _ in range(nshuf)])
    return s, sh.mean(), sh.std(), (1+(sh >= s).sum())/(nshuf+1)

if __name__ == "__main__":
    t = Table.read(sys.argv[1])
    psi = np.radians(np.array(t['derot_polangle'], float)); ok = np.isfinite(psi)
    ra, dec, b = (np.array(t[c], float) for c in ('ra', 'dec', 'b'))
    cat = np.array([str(x).strip() for x in t['catalog_name']])
    typ = np.array([str(x).strip() for x in t['type']])
    ok &= (np.abs(b) > 20) & ~np.isin(typ, ['Pulsar', 'SNR', 'HII'])
    ra, dec, psi, cat = ra[ok], dec[ok], psi[ok] % np.pi, cat[ok]
    # remove duplicates between compilations: keep first of any pair closer than 2 arcmin
    X = unit(ra, dec); keep = np.ones(len(ra), bool)
    C = X @ X.T
    for i in range(len(ra)):
        if keep[i]:
            dup = np.where(C[i, i+1:] > np.cos(np.radians(2/60)))[0] + i + 1; keep[dup] = False
    print(f"sources with derotated angle, |b|>20, non-Galactic type: {ok.sum()}  -> after 2' de-duplication: {keep.sum()}")
    ra, dec, psi, cat = ra[keep], dec[keep], psi[keep], cat[keep]
    print("by catalogue:", dict(collections.Counter(cat).most_common(8)))
    res = {}
    def block(name, m):
        print(f"\n== {name}: N = {m.sum()}")
        for nv in (5, 10, 20, 40, 80):
            if m.sum() <= nv+5: continue
            s, mu, sd, p = test(ra[m], dec[m], psi[m], nv)
            print(f"   n_v={nv:3d}  S_D={s:.4f}  shuffled {mu:.4f} +- {sd:.4f}  z={(s-mu)/sd:+.2f}  p={p:.4f}")
            res[f"{name}|nv{nv}"] = dict(S=float(s), mu=float(mu), sd=float(sd), p=float(p), N=int(m.sum()))
    possum = cat == '10.3847/1538-3881/ad2fc8'
    block("ALL", np.ones(len(ra), bool)); block("old compilations (no POSSUM pilot)", ~possum); block("POSSUM pilot only", possum)
    # ---- controls -------------------------------------------------------------------------
    m = ~possum; r, d = ra[m], dec[m]
    # negative control: random angles must give p not small
    s, mu, sd, p = test(r, d, rng.uniform(0, np.pi, m.sum()), 20, 1000)
    print(f"\ncontrol A (random angles): z={(s-mu)/sd:+.2f} p={p:.3f}  [must NOT be significant]")
    # planted signal that MUST fire: in a 30-deg cap give 50% of sources a common *transported* direction
    X = unit(r, d); c0 = X[np.argmax(X @ X.mean(0))]; cap = (X @ c0) > np.cos(np.radians(30))
    psi_p = rng.uniform(0, np.pi, m.sum()); idx = np.where(cap)[0]; i0 = idx[0]
    sel = idx[rng.random(len(idx)) < 0.5]
    psi_p[sel] = (1.0 + bearing(r[sel], d[sel], r[i0], d[i0]) - bearing(r[i0], d[i0], r[sel], d[sel]) + rng.normal(0, 0.2, len(sel))) % np.pi
    s, mu, sd, p = test(r, d, psi_p, 20, 1000)
    print(f"control B (planted alignment in a 30-deg cap, {len(sel)} sources): z={(s-mu)/sd:+.2f} p={p:.4f}  [MUST be significant]")
    res["control_random_p"] = float(p)
    json.dump(res, open("pilot_results.json", "w"), indent=1)

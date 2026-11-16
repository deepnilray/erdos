"""Diagnostics for the pilot signal: is it trivial? (per-catalogue angle distributions, same-source
components, catalogue-footprint effects). Usage: python3 align_diagnostics.py catalogue.fits"""
import sys, numpy as np, collections
from astropy.table import Table
import align_pilot as ap
rng = np.random.default_rng(7)
t = Table.read(sys.argv[1])
psi = np.radians(np.array(t['derot_polangle'], float)); ok = np.isfinite(psi)
ra, dec, b = (np.array(t[c], float) for c in ('ra', 'dec', 'b'))
cat = np.array([str(x).strip() for x in t['catalog_name']]); typ = np.array([str(x).strip() for x in t['type']])
ok &= (np.abs(b) > 20) & ~np.isin(typ, ['Pulsar', 'SNR', 'HII'])
ra, dec, psi, cat = ra[ok], dec[ok], psi[ok] % np.pi, cat[ok]

def dedupe(ra, dec, arcmin):
    X = ap.unit(ra, dec); C = X @ X.T; keep = np.ones(len(ra), bool)
    for i in range(len(ra)):
        if keep[i]: keep[np.where(C[i, i+1:] > np.cos(np.radians(arcmin/60)))[0]+i+1] = False
    return keep

print("1) angle histograms per catalogue (6 bins of 30 deg), and exact-value pile-ups")
for c, n in collections.Counter(cat).most_common(8):
    a = np.degrees(psi[cat == c]); h = np.histogram(a, bins=6, range=(0, 180))[0]
    vals, cnt = np.unique(np.round(a, 3), return_counts=True)
    X = ap.unit(ra[cat == c], dec[cat == c]); ext = np.degrees(np.arccos(np.clip((X @ X.mean(0)/np.linalg.norm(X.mean(0))).min(), -1, 1)))
    print(f"   {c[:22]:22s} N={n:4d} hist={h} most-repeated value {vals[cnt.argmax()]:.1f} x{cnt.max()}  sky radius ~{ext:.0f} deg")

def run(name, m, nv=20, within=None, nshuf=2000):
    r, d, p = ra[m], dec[m], psi[m]
    nb = ap.neighbours(r, d, nv); ph = ap.transport_phases(r, d, nb)
    s = ap.S_D(p, nb, ph)
    if within is None: sh = [ap.S_D(rng.permutation(p), nb, ph) for _ in range(nshuf)]
    else:
        g = within[m]; sh = []
        for _ in range(nshuf):
            q = p.copy()
            for u in np.unique(g):
                j = np.where(g == u)[0]; q[j] = q[rng.permutation(j)]
            sh.append(ap.S_D(q, nb, ph))
    sh = np.array(sh)
    print(f"   {name:58s} N={m.sum():5d} z={(s-sh.mean())/sh.std():+.2f} p={(1+(sh>=s).sum())/(nshuf+1):.4f}")

print("\n2) n_v=20 tests")
for am in (2, 10, 60):
    k = dedupe(ra, dec, am); idx = np.where(k)[0]; m = np.zeros(len(ra), bool); m[idx] = True
    run(f"all, one source per {am}' (global shuffle)", m)
    run(f"all, one source per {am}' (shuffle WITHIN catalogue)", m, within=cat)
k = dedupe(ra, dec, 60); base = np.zeros(len(ra), bool); base[np.where(k)[0]] = True
for c, n in collections.Counter(cat).most_common(5):
    m = base & (cat == c)
    if m.sum() > 60: run(f"only {c[:22]}, one per 60'", m)
old = base & np.isin(cat, ['1980A&AS...39..379T', '1981ApJS...45...97S'])
run("TI80 + SN81 only, one per 60' (global shuffle)", old)
run("TI80 + SN81 only, one per 60' (shuffle within catalogue)", old, within=cat)

"""
Periodicity-first search for new variable stars in ZTF DR24 (public), one sky region at a time.

  python3 -I period_search.py RA DEC RADIUS_DEG OUTDIR

1. IRSA TAP: ztf_objects_dr24 objects with real excess scatter, in r AND g, that are star-like, with
   >= 250 good r epochs, median r 14.5-19.5, chisq > 3, von Neumann ratio < 1.5 (smooth, correlated variation).
2. Drop anything within 3" of a catalogued variable (VSX, ZTF Chen+2020, ATLAS, Gaia DR3 vari classifications,
   Gaia DR3 vari_summary): xknown.py.
3. Light curves by object ID, r and g (bad nights removed). Lomb-Scargle in each band, 1/1500 to 50 per day.
4. Keep a star only if:
   - the r periodogram peak is strong (power >= 0.25, FAP < 1e-10);
   - it is not a sampling alias (|f - k| > 0.01 per day for k = 1..3; P not within 2 % of 29.53 d or 365.25 d or their halves);
   - g gives the same period (or 2x / 0.5x, as for eclipsing binaries) within 0.5 %;
   - no Gaia DR3 neighbour within 6" that is brighter than the target + 1.5 mag (blend).
5. Writes vetted.csv and a phase-plot PNG for each survivor.
"""
import sys, os, io, json, time, numpy as np, pandas as pd, requests, pyvo, subprocess
from astropy.timeseries import LombScargle
from astropy.coordinates import SkyCoord; import astropy.units as u
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
IRSA = pyvo.dal.TAPService("https://irsa.ipac.caltech.edu/TAP")
LCURL = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"

def query(ra, dec, r, band, cuts):
    q = (f"SELECT oid, ra, dec, filtercode, ngoodobs, medianmag, magrms, medmagerr, chisq, vonneumannratio, refsharp, refchi "
         f"FROM ztf_objects_dr24 WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},{r}))=1 AND filtercode='{band}' {cuts}")
    for att in range(3):
        try: return IRSA.run_sync(q, maxrec=500000).to_table().to_pandas()
        except Exception as e: print("TAP retry", e); time.sleep(20)
    raise RuntimeError("TAP failed")

def get_lc(oid):
    for att in range(3):
        try:
            q = requests.get(LCURL, params=dict(ID=str(int(oid)), FORMAT="csv"), timeout=120)
            lc = pd.read_csv(io.StringIO(q.text)); return lc
        except Exception as e: time.sleep(5)
    return None

def clean(lc):
    lc = lc[lc.catflags == 0].copy()
    lc["night"] = np.floor(lc.mjd - 0.3).astype(int)
    g = lc.groupby("night")
    sc = g.mag.transform(lambda x: 1.4826 * np.median(np.abs(x - np.median(x))) if len(x) >= 5 else 0.0)
    return lc[~((g.mag.transform("size") >= 5) & (sc > 4 * g.magerr.transform("median")))]

def ls_peak(lc):
    ls = LombScargle(lc.mjd, lc.mag, lc.magerr)
    f, p = ls.autopower(minimum_frequency=1 / 1500, maximum_frequency=50, samples_per_peak=8, method="fast")
    k = np.argmax(p); return float(1 / f[k]), float(p[k]), float(ls.false_alarm_probability(p[k])), f, p

def alias(P):
    f = 1 / P
    if any(abs(f - k) < 0.01 for k in (1, 2, 3)): return True
    for A in (29.53, 365.25, 29.53 / 2, 365.25 / 2):
        if abs(P / A - 1) < 0.02: return True
    return P > 1000

def same_period(P1, P2):
    for m in (1, 2, 0.5):
        if abs(P1 * m / P2 - 1) < 0.005: return True
    return False

def gaia_blend(ra, dec, rmag):
    g = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
    t = g.run_sync(f"SELECT ra, dec, phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},{6/3600}))").to_table()
    if len(t) == 0: return False, None
    c = SkyCoord(ra * u.deg, dec * u.deg); s = SkyCoord(np.array(t["ra"]) * u.deg, np.array(t["dec"]) * u.deg).separation(c).arcsec
    gm = np.array(t["phot_g_mean_mag"], float); own = np.argmin(s)
    others = [(si, gi) for i, (si, gi) in enumerate(zip(s, gm)) if i != own]
    blend = any(np.isfinite(gi) and gi < gm[own] + 1.5 for si, gi in others)
    return blend, float(gm[own])

def main():
    ra, dec, r = map(float, sys.argv[1:4]); out = sys.argv[4]; os.makedirs(out, exist_ok=True)
    cuts = ("AND ngoodobs>=250 AND medianmag BETWEEN 14.5 AND 19.5 AND chisq > 3 AND vonneumannratio < 1.5 "
            "AND refsharp BETWEEN -0.25 AND 0.25 AND refchi < 2")
    rr = query(ra, dec, r, "zr", cuts); print("r-band candidates", len(rr), flush=True)
    rr = rr.sort_values("chisq", ascending=False).drop_duplicates(subset=None)
    # one entry per sky position (overlapping fields give duplicate oids)
    c = SkyCoord(rr.ra.values * u.deg, rr.dec.values * u.deg); keep = np.ones(len(rr), bool)
    idx, s2, _ = c.match_to_catalog_sky(c, nthneighbor=2)
    for i, (j, s) in enumerate(zip(idx, s2.arcsec)):
        if s < 2 and keep[j] and rr.ngoodobs.values[j] >= rr.ngoodobs.values[i] and j != i: keep[i] = False
    rr = rr[keep]; p = os.path.join(out, "cands.csv"); rr.to_csv(p, index=False); print("unique positions", len(rr), flush=True)
    subprocess.run([sys.executable, "-I", os.path.join(HERE, "xknown.py"), p, os.path.join(out, "cands_x.csv")], check=True)
    cx = pd.read_csv(os.path.join(out, "cands_x.csv")); un = cx[~cx.known_any]; print("not catalogued:", len(un), "of", len(cx), flush=True)
    # g-band partner oids
    gg = query(ra, dec, r, "zg", "AND ngoodobs>=80")
    gc = SkyCoord(gg.ra.values * u.deg, gg.dec.values * u.deg)
    rows = []
    for _, o in un.iterrows():
        lc = get_lc(o.oid)
        if lc is None or len(lc) < 100: continue
        lc = clean(lc)
        P, pw, fap, f, pp = ls_peak(lc)
        row = dict(oid=int(o.oid), ra=o.ra, dec=o.dec, rmag=o.medianmag, P_r=P, power_r=pw, fap_r=fap, alias=alias(P))
        if pw < 0.25 or fap > 1e-10 or row["alias"]: rows.append(row); continue
        j, sg, _ = SkyCoord(o.ra * u.deg, o.dec * u.deg).match_to_catalog_sky(gc)
        if sg.arcsec[0] < 1.5:
            lg = get_lc(gg.oid.values[int(j)])
            if lg is not None and len(lg) > 60:
                lg = clean(lg); Pg, pwg, fapg, _, _ = ls_peak(lg)
                row.update(P_g=Pg, power_g=pwg, fap_g=fapg, period_agrees=same_period(P, Pg), gmr=float(np.median(lg.mag) - np.median(lc.mag)))
        try: row["blend"], row["gaia_G"] = gaia_blend(o.ra, o.dec, o.medianmag)
        except Exception as e: row["blend"] = None
        rows.append(row)
        # phase plot (fold at P and 2P: eclipsing binaries often peak at half the orbital period)
        fig, axs = plt.subplots(1, 3, figsize=(15, 3.6))
        for ax, PP, tt in ((axs[0], None, "light curve"), (axs[1], P, f"P = {P:.6f} d"), (axs[2], 2 * P, f"2P = {2*P:.6f} d")):
            for L, col in ((lc, "r"),) + (((lg, "g"),) if "P_g" in row else ()):
                x = L.mjd if PP is None else ((L.mjd - L.mjd.min()) / PP) % 1
                ax.plot(x, L.mag, ".", ms=2, color=col, alpha=0.6)
            ax.invert_yaxis(); ax.set_title(tt, fontsize=9)
        fig.suptitle(f"ZTF {int(o.oid)} RA {o.ra:.5f} Dec {o.dec:.5f} r {o.medianmag:.2f} LS {pw:.2f} g-agree {row.get('period_agrees')}", fontsize=9)
        plt.tight_layout(); plt.savefig(os.path.join(out, f"{int(o.oid)}.png"), dpi=70); plt.close()
        print(row, flush=True)
    R = pd.DataFrame(rows); R.to_csv(os.path.join(out, "all_lc.csv"), index=False)
    if len(R) and "period_agrees" in R:
        V = R[(R.power_r >= 0.25) & (R.fap_r < 1e-10) & ~R.alias & (R.period_agrees == True) & (R.blend == False)]
        V.to_csv(os.path.join(out, "vetted.csv"), index=False); print("VETTED:", len(V)); print(V.to_string())

if __name__ == "__main__":
    main()

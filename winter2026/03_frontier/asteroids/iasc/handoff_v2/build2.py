"""Build PS1 DR2 validation sets: 4 same-filter exposures 8-40 min apart, ecliptic fields away from the Milky Way, interior crops (>=97% valid),
each with >=3 known asteroids (SkyBoT, V<21.5) inside the crop. Writes sets/<name>/*.fits (IASC-like layout) and sets/<name>/known.json."""
import json, os, sys, requests, numpy as np, time
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
BASE = "https://ps1images.stsci.edu"; LIST = BASE + "/cgi-bin/ps1filenames.py"; NX, NY = 2434, 2423; TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 50
rng = np.random.default_rng(11); os.makedirs("sets", exist_ok=True)
import pickle
cands = []
if os.path.exists("cands.pkl"): cands = pickle.load(open("cands.pkl","rb"))
for lam in ([] if cands else  range(0, 360, 8)):
    for beta in (-5, 0, 5):
        c = SkyCoord(lon=lam * u.deg, lat=beta * u.deg, frame="geocentrictrueecliptic").icrs
        if abs(c.dec.deg) > 32 or abs(c.galactic.b.deg) < 12: continue
        try: txt = requests.get(LIST, params=dict(ra=c.ra.deg, dec=c.dec.deg, type="warp", format="fits"), timeout=60).text
        except Exception: continue
        g = {}
        for l in txt.splitlines()[1:]:
            r = l.split()
            if len(r) < 10 or r[9] != "0": continue
            g.setdefault((r[4], int(float(r[5])), r[0], r[1]), {})[round(float(r[5]), 4)] = r
        pts = []
        for (flt, d, pc, sc), ex in g.items():
            ms = sorted(ex)
            if len(ms) != 4: continue
            gp = np.diff(ms) * 1440
            if gp.min() < 8 or gp.max() > 40: continue
            pts.append(dict(lam=lam, beta=beta, ra=c.ra.deg, dec=c.dec.deg, filter=flt, mjds=ms, files=[ex[m][7] for m in ms]))
        rng.shuffle(pts); cands += pts[:3]
pickle.dump(cands, open("cands.pkl","wb")); print("candidates", len(cands), flush=True); rng.shuffle(cands)
built = 0
def geom_ok(cd):
    try:
        rr = requests.get(BASE + cd["files"][0], timeout=300); rr.raise_for_status(); open("/tmp/g0.fits", "wb").write(rr.content)
        h = fits.open("/tmp/g0.fits"); hd = h[1].header
        w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]; w.wcs.crval = [hd["CRVAL1"], hd["CRVAL2"]]; w.wcs.crpix = [hd["CRPIX1"], hd["CRPIX2"]]
        w.wcs.cd = np.array([[hd["CDELT1"] * hd["PC001001"], 0], [0, hd["CDELT2"] * hd["PC002002"]]]); w.wcs.set()
        d = np.array(h[1].data, dtype=np.float32); x0 = (d.shape[1] - NX) // 2; y0 = (d.shape[0] - NY) // 2
        if np.isfinite(d[y0:y0 + NY, x0:x0 + NX]).mean() < 0.65: return False
        cc = w.pixel_to_world(x0 + NX / 2, y0 + NY / 2); cd["ra"], cd["dec"] = float(cc.ra.deg), float(cc.dec.deg); return True
    except Exception: return False
for ci, cd in enumerate(cands):
    if built >= TARGET: break
    if not geom_ok(cd): continue
    tmid = Time(np.mean(cd["mjds"]), format="mjd").jd
    try:
        r = requests.get("https://ssp.imcce.fr/webservices/skybot/api/conesearch.php", params={"-ep": tmid, "-ra": cd["ra"], "-dec": cd["dec"], "-rd": 0.07, "-mime": "text", "-output": "obs", "-observer": "F51", "-objFilter": "111", "-from": "ps1val2"}, timeout=60).text
    except Exception: continue
    known = []
    for l in r.splitlines():
        if l.startswith("#") or "|" not in l: continue
        f = [x.strip() for x in l.split("|")]
        try:
            c = SkyCoord(f[2], f[3], unit=("hourangle", "deg")); V = float(f[5])
            if V < 22.5: known.append(dict(num=f[0], name=f[1], ra=c.ra.deg, dec=c.dec.deg, V=V, err=float(f[6]), dra_h=float(f[8]), ddec_h=float(f[9])))
        except Exception: pass
    print("  cand", ci, "geom ok, known V<22.5:", len(known), flush=True)
    if len(known) < 2: continue
    name = f"P{built:02d}_{cd['filter']}_{int(cd['mjds'][0])}_L{cd['lam']}B{cd['beta']}"; sd = f"sets/{name}"; os.makedirs(sd, exist_ok=True)
    ok = True; outs = []
    for fi, fn in enumerate(cd["files"]):
        try:
            tmp = f"/tmp/w2_{fi}.fits"; rr = requests.get(BASE + fn, timeout=300); rr.raise_for_status(); open(tmp, "wb").write(rr.content)
            h = fits.open(tmp); hd = h[1].header; d = np.array(h[1].data, dtype=np.float32)
        except Exception as e: ok = False; break
        w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]; w.wcs.crval = [hd["CRVAL1"], hd["CRVAL2"]]; w.wcs.crpix = [hd["CRPIX1"], hd["CRPIX2"]]
        w.wcs.cd = np.array([[hd["CDELT1"] * hd["PC001001"], 0], [0, hd["CDELT2"] * hd["PC002002"]]]); w.wcs.set()
        x0 = (d.shape[1] - NX) // 2; y0 = (d.shape[0] - NY) // 2
        c = d[y0:y0 + NY, x0:x0 + NX].copy()
        if np.isfinite(c).mean() < 0.60: ok = False; break
        c = np.where(np.isfinite(c), c + 1000.0, 0.0).astype(np.float32)
        oh = fits.Header(); oh["DATE-OBS"] = Time(hd["MJD-OBS"], format="mjd").utc.isot; oh["EXPTIME"] = hd["EXPTIME"]
        oh["CTYPE1"] = "RA---TAN"; oh["CTYPE2"] = "DEC--TAN"; oh["CRVAL1"] = hd["CRVAL1"]; oh["CRVAL2"] = hd["CRVAL2"]
        oh["CRPIX1"] = hd["CRPIX1"] - x0; oh["CRPIX2"] = hd["CRPIX2"] - y0; oh["CDELT1"] = -abs(hd["CDELT1"]); oh["CDELT2"] = abs(hd["CDELT2"]); oh["CROTA2"] = 0.0; oh["GAIN"] = hd.get("CELL.GAIN", 1.0); oh["PS1SRC"] = fn
        outs.append((f"{sd}/{fi}_{os.path.basename(fn)}", c, oh)); os.remove(tmp)
    if not ok:
        import shutil; shutil.rmtree(sd, ignore_errors=True); continue
    for p, c, oh in outs: fits.PrimaryHDU(c, oh).writeto(p, overwrite=True)
    json.dump(dict(cand=cd, known=known, tmid_jd=tmid), open(f"{sd}/known.json", "w")); built += 1
    print(f"built {name}  known V<22.5: {len(known)}   ({built}/{TARGET}, cand {ci}/{len(cands)})", flush=True)
print("done", built)

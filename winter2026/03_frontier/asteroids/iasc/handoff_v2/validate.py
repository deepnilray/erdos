import sys, os, glob, json, numpy as np, pandas as pd, time
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
import iasc_hunt as H
from tracker import Params, build_D, find_tracklets
CONFIGS = {"base": Params(), "sens": Params(NSIG=2.0, SNR_MIN=3.0)}
if len(sys.argv) > 2: CONFIGS = {k: v for k, v in CONFIGS.items() if k in sys.argv[2].split(",")}
def run_set(sd):
    meta = json.load(open(f"{sd}/known.json")); ims = H.load(sd); n = len(ims)
    h0 = ims[0]["hdr"]; w0 = H.clean_wcs(h0); ny, nx = ims[0]["data"].shape; cen = w0.pixel_to_world(nx / 2, ny / 2); rad = 0.75 * np.hypot(nx, ny) * abs(h0["CDELT1"])
    gaia = H.gaia_stars(cen.ra.deg, cen.dec.deg, rad); cache = []
    for im in ims:
        det = H.detect(im); w, q = H.refine_wcs(im, det, gaia); cache.append(dict(w=w, zp=q["zp"], q=q))
    T = np.array([im["t"].mjd for im in ims]) * 1440.0; tmid = np.mean([im["t"].jd for im in ims])
    out = []
    for cname, P in CONFIGS.items():
        D = build_D([im["data"] for im in ims], ims, cache, P); trk = find_tracklets(D, T, P)
        pos = []
        for tr in trk:
            ks = sorted(tr["members"]); c0 = D[ks[0]]["sky"][tr["members"][ks[0]]]; c1 = D[ks[-1]]["sky"][tr["members"][ks[-1]]]
            f = (np.mean(T) - T[ks[0]]) / (T[ks[-1]] - T[ks[0]]); pos.append(SkyCoord(c0.ra + f * (c1.ra - c0.ra), c0.dec + f * (c1.dec - c0.dec)))
        used = set(); rec = {}
        for ki, k in enumerate(meta["known"]):
            ko = SkyCoord(k["ra"] * u.deg, k["dec"] * u.deg); xy = cache[0]["w"].world_to_pixel(ko)
            on = 60 < xy[0] < nx - 60 and 60 < xy[1] < ny - 60
            best = min(((p.separation(ko).arcsec, i) for i, p in enumerate(pos)), default=(1e9, -1))
            tol = max(10.0, 3 * k["err"]); hit = best[0] < tol
            if hit: used.add(best[1])
            out.append(dict(set=os.path.basename(sd), config=cname, name=k["name"], V=k["V"], on_chip=bool(on), recovered=int(hit and on), ntrk=len(trk)))
        out.append(dict(set=os.path.basename(sd), config=cname, name="__summary__", V=np.nan, on_chip=True, recovered=-1, ntrk=len(trk), unmatched=len(trk) - len(used), n_det=int(np.mean([len(d["x"]) for d in D]))))
    return out
if __name__ == "__main__":
    sets = sorted(glob.glob(sys.argv[1] + "/P*")); allr = []
    for sd in sets:
        t = time.time()
        try: allr += run_set(sd)
        except Exception as e: print("FAIL", sd, repr(e)[:150], flush=True); continue
        print("ok", os.path.basename(sd), round(time.time() - t), "s", flush=True)
        pd.DataFrame(allr).to_csv("validation_rows.csv", index=False)

"""Build the labelled IASC-style training database from the real practice set.

Real images are kept; synthetic moving objects with known truth (mag, rate, PA, path) are injected at random,
trailed by the real 45 s exposure, with Moffat PSFs matched to each image's measured FWHM and Poisson shot noise.
Scramble trials (rotate non-stationary detections of images 1..3) give chance-alignment false tracklets.

Outputs (OUT dir): iasc_train.db (SQLite), injections.csv, tracklets_features.csv, trials_meta.json
Usage: python build_db.py <fits_folder> <out> [N_INJ_TRIALS] [N_SCRAMBLE] [SEED]
"""
import sys, os, json, pickle, sqlite3, time, csv
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
import iasc_hunt as H
from tracker import Params, build_D, find_tracklets

PIX = None


def load_cache(folder, out):
    path = os.path.join(out, "cache.pkl")
    ims = H.load(folder)
    if os.path.exists(path):
        return ims, pickle.load(open(path, "rb"))
    h0 = ims[0]["hdr"]; w0 = H.clean_wcs(h0); ny, nx = ims[0]["data"].shape
    cen = w0.pixel_to_world(nx / 2, ny / 2); rad = 0.75 * np.hypot(nx, ny) * abs(h0["CDELT1"])
    gaia = H.gaia_stars(cen.ra.deg, cen.dec.deg, rad)
    cache = []
    for im in ims:
        det = H.detect(im); w, q = H.refine_wcs(im, det, gaia); cache.append(dict(w=w, zp=q["zp"], q=q))
    pk = dict(cache=cache, cen_ra=cen.ra.deg, cen_dec=cen.dec.deg)
    pickle.dump(pk, open(path, "wb")); return ims, pk


def moffat_stamp(fwhm, beta, half, dx, dy):
    """flux-normalised Moffat evaluated on a (2*half+1)^2 grid centred on the integer pixel, source at sub-pixel offset (dx,dy)."""
    alpha = fwhm / (2 * np.sqrt(2 ** (1 / beta) - 1))
    yy, xx = np.mgrid[-half:half + 1, -half:half + 1].astype(float)
    r2 = (xx - dx) ** 2 + (yy - dy) ** 2
    return (beta - 1) / (np.pi * alpha ** 2) * (1 + r2 / alpha ** 2) ** (-beta)


def inject(arr, x, y, trail_dx, trail_dy, flux, fwhm, gain, rng, beta=2.5):
    """add one trailed source centred at (x,y) (pixel, 0-based) whose motion during the exposure is (trail_dx, trail_dy) pixels."""
    L = float(np.hypot(trail_dx, trail_dy)); ns = int(min(max(np.ceil(L / 0.5) + 1, 1), 80))
    half = int(np.ceil(3 * fwhm + L / 2 + 3)); ny, nx = arr.shape
    xc, yc = int(round(x)), int(round(y))
    if xc - half < 0 or yc - half < 0 or xc + half >= nx or yc + half >= ny: return False
    stamp = np.zeros((2 * half + 1, 2 * half + 1))
    for s in np.linspace(-0.5, 0.5, ns):
        stamp += moffat_stamp(fwhm, beta, half, x - xc + s * trail_dx, y - yc + s * trail_dy)
    stamp *= flux / ns
    noisy = stamp + rng.normal(0, 1, stamp.shape) * np.sqrt(np.clip(stamp, 0, None) / gain)
    arr[yc - half:yc + half + 1, xc - half:xc + half + 1] += noisy
    return True


def make_trial(ims, pk, rng, nsrc, region, mag_rng=(19.0, 24.0), rate_rng=(0.05, 15.0)):
    """returns list of modified arrays and truth rows. region: 'train' (x < nx/2) or 'test' (x >= nx/2) in image 0 pixels."""
    n = len(ims); ny, nx = ims[0]["data"].shape
    arrs = [im["data"].copy() for im in ims]
    t_min = np.array([im["t"].mjd for im in ims]) * 1440.0
    texp = np.array([im["hdr"].get("EXPTIME", 45.0) for im in ims]) / 60.0
    gain = ims[0]["hdr"].get("GAIN", 1.0)
    truth, placed = [], []
    tries = 0
    while len(truth) < nsrc and tries < 500:
        tries += 1
        m = rng.uniform(*mag_rng); rate = float(np.exp(rng.uniform(np.log(rate_rng[0]), np.log(rate_rng[1])))); pa = rng.uniform(0, 360)
        xs = rng.uniform(120, nx / 2 - 20) if region == "train" else rng.uniform(nx / 2 + 20, nx - 120)
        ys = rng.uniform(120, ny - 120)
        if any(np.hypot(xs - px, ys - py) < 150 for px, py in placed): continue
        sky0 = pk["cache"][0]["w"].pixel_to_world(xs, ys)
        e, nn = rate * np.sin(np.radians(pa)), rate * np.cos(np.radians(pa))     # arcsec/min east, north
        rows, ok = [], True
        for k in range(n):
            dtm = t_min[k] - t_min[0]
            sk = SkyCoord(sky0.ra + e * dtm * u.arcsec / np.cos(sky0.dec.radian), sky0.dec + nn * dtm * u.arcsec)
            xk, yk = pk["cache"][k]["w"].world_to_pixel(sk); xk, yk = float(xk), float(yk)
            # trail across the exposure: sky displacement over texp minutes, mapped through the local WCS
            sk2 = SkyCoord(sk.ra + e * texp[k] * u.arcsec / np.cos(sk.dec.radian), sk.dec + nn * texp[k] * u.arcsec)
            x2, y2 = pk["cache"][k]["w"].world_to_pixel(sk2)
            if not (60 < xk < nx - 60 and 60 < yk < ny - 60): ok = False; break
            rows.append((k, sk.ra.deg, sk.dec.deg, xk, yk, float(x2) - xk, float(y2) - yk))
        if not ok: continue
        # avoid injecting on a cell gap (the tracker masks those on purpose); record gaps instead of silently losing the source
        if "gap0" not in pk: pk["gap0"] = H.gap_mask(np.ascontiguousarray(ims[0]["data"]))
        gapm = pk["gap0"]
        if gapm[int(round(rows[0][4])), int(round(rows[0][3]))]: continue
        placed.append((xs, ys))
        sid = len(truth)
        for (k, ra, dec, xk, yk, tdx, tdy) in rows:
            zp = pk["cache"][k]["zp"]; flux = 10 ** (-0.4 * (m - zp))
            fwhm = float(np.sqrt(ims[k]["hdr"]["FWHM_MAJ"] * ims[k]["hdr"]["FWHM_MIN"]))
            inject(arrs[k], xk, yk, tdx, tdy, flux, fwhm, gain, rng)
        truth.append(dict(src=sid, mag=m, rate=rate, pa=pa, path=[(r[0], r[1], r[2]) for r in rows], x0=xs, y0=ys))
    return arrs, truth


def match_truth(tr, truth, ims_t, tol=1.5):
    """index of the injected source that this tracklet follows (>=3 members within tol arcsec), else -1."""
    best, bi = 0, -1
    for ti, tt in enumerate(truth):
        hit = 0
        for k, idx in tr["members_sky"].items():
            _, ra, dec = tt["path"][k]
            if SkyCoord(ra * u.deg, dec * u.deg).separation(idx).arcsec < tol: hit += 1
        if hit > best: best, bi = hit, ti
    return bi if best >= 3 else -1


def run(folder, out, n_inj=100, n_scr=100, seed=1, nsrc=6):
    os.makedirs(out, exist_ok=True)
    ims, pk = load_cache(folder, out)
    cen = SkyCoord(pk["cen_ra"] * u.deg, pk["cen_dec"] * u.deg)
    P0 = Params(); T = np.array([im["t"].mjd for im in ims]) * 1440.0
    # baseline (no injection): real tracklets present in the images
    D0 = build_D([im["data"] for im in ims], ims, pk["cache"], P0); base = find_tracklets(D0, T, P0)
    base_sky = [b["sky_first"] for b in base]
    print("baseline tracklets:", len(base), [(round(b["rate"], 3), round(b["mag"], 2)) for b in base])
    rows_inj, rows_trk = [], []
    t0 = time.time()
    meta = dict(seed=seed, n_inj=n_inj, n_scr=n_scr, nsrc=nsrc, P=P0.__dict__, baseline=[dict(rate=b["rate"], mag=b["mag"], ra=b["ra0"], dec=b["dec0"]) for b in base])
    for trial in range(n_inj):
        region = "train" if trial < int(0.7 * n_inj) else "test"
        rng = np.random.default_rng(seed * 100000 + trial)
        arrs, truth = make_trial(ims, pk, rng, nsrc, region)
        D = build_D(arrs, ims, pk["cache"], P0); trk = find_tracklets(D, T, P0)
        for tr in trk:
            tr["members_sky"] = {k: D[k]["sky"][v] for k, v in tr["members"].items()}
        used = set()
        for tr in trk:
            ti = match_truth(tr, truth, ims)
            isbase = any(tr["sky_first"].separation(bs).arcsec < 3 for bs in base_sky)
            label = 1 if ti >= 0 else (-1 if isbase else 0)
            if ti >= 0: used.add(ti)
            rows_trk.append(dict(source=f"inj{trial}", split=region, label=label, truth_src=ti, **{k: tr[k] for k in ("n", "rate", "pa", "resid", "mag", "ptp_mag", "snr_min", "snr_med", "elong_med", "a_med", "a_ptp", "peak_med")}))
        for tt in truth:
            rows_inj.append(dict(trial=trial, split=region, src=tt["src"], mag=round(tt["mag"], 3), rate=round(tt["rate"], 4), pa=round(tt["pa"], 2),
                                 x0=round(tt["x0"], 1), y0=round(tt["y0"], 1), recovered=int(tt["src"] in used)))
        if trial % 10 == 0: print(f"inj trial {trial}/{n_inj}  {time.time() - t0:.0f}s  recovered so far {sum(r['recovered'] for r in rows_inj)}/{len(rows_inj)}", flush=True)
    for s in range(n_scr):
        trk = find_tracklets(D0, T, P0, scramble_seed=seed * 1000 + s, cen=cen)
        for tr in trk:
            rows_trk.append(dict(source=f"scr{s}", split="scramble", label=0, truth_src=-1, **{k: tr[k] for k in ("n", "rate", "pa", "resid", "mag", "ptp_mag", "snr_min", "snr_med", "elong_med", "a_med", "a_ptp", "peak_med")}))
    print("scramble trials done; false tracklets:", sum(r["source"].startswith("scr") for r in rows_trk))
    for name, rows in (("injections", rows_inj), ("tracklets_features", rows_trk)):
        with open(os.path.join(out, name + ".csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    json.dump(meta, open(os.path.join(out, "trials_meta.json"), "w"), indent=1)
    db = sqlite3.connect(os.path.join(out, "iasc_train.db"))
    import pandas as pd
    pd.DataFrame(rows_inj).to_sql("injections", db, if_exists="replace", index=False)
    pd.DataFrame(rows_trk).to_sql("tracklets", db, if_exists="replace", index=False); db.close()
    print("done", time.time() - t0, "s")


if __name__ == "__main__":
    a = sys.argv
    run(a[1], a[2], int(a[3]) if len(a) > 3 else 100, int(a[4]) if len(a) > 4 else 100, int(a[5]) if len(a) > 5 else 1)

"""
IASC / Pan-STARRS image-set moving-object finder.

Input: one IASC image set (a folder with 4 FITS images of the same field, taken ~15 min apart).
Steps
 1. Detect sources in each image (sep), background-subtracted, threshold NSIG.
 2. Astrometry: refine each image's header WCS against Gaia DR3 (affine + TAN refit on matched stars), report RMS.
 3. Photometry: zero point from Gaia G of matched stars (w band ~ G for this purpose; stated approximation).
 4. Remove stationary sources (detected at the same sky position, within MATCH_ARCSEC, in >= 2 other images).
 5. Link the rest into tracklets: one detection per image (>= 3 of 4 images), positions linear in time,
    rate between MIN_RATE and MAX_RATE arcsec/min, consistent magnitude, fit RMS < MAX_RESID arcsec.
 6. Known objects: SkyBoT cone search at the set's mid-time for observatory F51 (Pan-STARRS 1), matched to tracklets.
 7. Outputs: tracklets.csv (all), MPCReport.txt (laid out like Astrometrica's IASC report: header, 80-column lines, '----- end -----';
    check against Astrometrica before pasting into the IASC team page), cutout PNGs, summary.json.

Usage: python iasc_hunt.py <folder_with_fits> <outdir> [--team ABC]
"""
import sys, os, glob, json, argparse, numpy as np, requests, io
from astropy.io import fits
from astropy.wcs import WCS
from astropy.wcs.utils import fit_wcs_from_points
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
import sep

NSIG, MATCH_ARCSEC, MIN_RATE, MAX_RATE, MAX_RESID = 2.5, 1.0, 0.03, 20.0, 0.6   # rates in arcsec/min

def load(folder):
    ims = []
    for f in sorted(glob.glob(os.path.join(folder, "*.fits")) + glob.glob(os.path.join(folder, "*.fit"))):
        h = fits.getheader(f); d = fits.getdata(f).astype(np.float64)
        t = Time(h["DATE-OBS"], scale="utc") + (h.get("EXPTIME", 0) / 2) * u.s    # mid-exposure
        ims.append(dict(file=os.path.basename(f), hdr=h, data=d, t=t))
    return sorted(ims, key=lambda x: x["t"].jd)

def clean_wcs(h, flip=False):
    """Plain TAN WCS from CRVAL/CRPIX/CDELT/CROTA2 only (PS1 IASC headers carry extra keys that make astropy's PC singular).
    flip=True mirrors the x axis (parity test; the right one is chosen by Gaia match count)."""
    w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.crval = [h["CRVAL1"], h["CRVAL2"]]; w.wcs.crpix = [h["CRPIX1"], h["CRPIX2"]]
    c1, c2 = h["CDELT1"] * (-1 if flip else 1), h["CDELT2"]; r = np.radians(h.get("CROTA2", 0.0))
    w.wcs.cd = np.array([[c1 * np.cos(r), -c2 * np.sin(r)], [c1 * np.sin(r), c2 * np.cos(r)]]); w.wcs.set(); return w

def gap_mask(d):
    """PS1 IASC chips fill cell gaps / dead cells with a constant value: flag pixels whose neighbours are identical."""
    from scipy import ndimage
    flat = np.zeros(d.shape, bool)
    eq_r = d[:, 1:] == d[:, :-1]; eq_d = d[1:, :] == d[:-1, :]
    flat[:-1, :-1] = eq_r[:-1, :] & eq_d[:, :-1]
    flat = ndimage.binary_opening(flat, structure=np.ones((3, 3)))     # real flat runs, not single coincidences
    return flat | (d <= 0) | ~np.isfinite(d)

def detect(im):
    d = np.ascontiguousarray(im["data"]); mask = gap_mask(d)
    from scipy import ndimage
    near_gap = ndimage.binary_dilation(mask, iterations=8)
    bkg = sep.Background(d, mask=mask, bw=64, bh=64); sub = d - bkg.back()
    obj = sep.extract(sub, NSIG, err=bkg.globalrms, mask=mask, minarea=5, deblend_cont=0.01)
    flux, ferr, _ = sep.sum_circle(sub, obj["x"], obj["y"], 5.0, err=bkg.globalrms, mask=mask)
    xi = np.clip(np.round(obj["x"]).astype(int), 0, d.shape[1] - 1); yi = np.clip(np.round(obj["y"]).astype(int), 0, d.shape[0] - 1)
    ok = (flux > 0) & (obj["flag"] < 4) & (obj["a"] < 8)
    o = obj[ok]; return dict(x=o["x"], y=o["y"], flux=flux[ok], ferr=ferr[ok], a=o["a"], b=o["b"], peak=o["peak"], rms=bkg.globalrms, sub=sub,
                             gap=near_gap[yi, xi][ok])

def gaia_stars(ra, dec, rad_deg, gmax=20.5):
    import pyvo
    g = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
    q = (f"SELECT ra, dec, pmra, pmdec, phot_g_mean_mag AS g, bp_rp FROM gaiadr3.gaia_source WHERE phot_g_mean_mag < {gmax} AND "
         f"1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},{rad_deg}))")
    return g.run_sync(q, maxrec=200000).to_table()

def refine_wcs(im, det, gaia):
    dt = (im["t"].jyear - 2016.0)
    pm_ok = np.isfinite(np.array(gaia["pmra"], float))
    gra = np.array(gaia["ra"], float) + np.where(pm_ok, np.array(gaia["pmra"], float), 0) * dt / 3.6e6 / np.cos(np.radians(np.array(gaia["dec"], float)))
    gde = np.array(gaia["dec"], float) + np.where(pm_ok, np.array(gaia["pmdec"], float), 0) * dt / 3.6e6
    gsc = SkyCoord(gra * u.deg, gde * u.deg)
    bright = np.argsort(-det["flux"])[:1500]
    # choose header parity/rotation variant with most Gaia matches after removing a global offset
    best = None
    for flip in (False, True):
        for sgn in (1, -1):
            hh = dict(im["hdr"]); hh["CROTA2"] = sgn * im["hdr"].get("CROTA2", 0.0); wt = clean_wcs(hh, flip)
            sky = wt.pixel_to_world(det["x"][bright[:400]], det["y"][bright[:400]])
            idx, s2, _ = sky.match_to_catalog_sky(gsc)
            nm = int((s2.arcsec < 15).sum())
            if best is None or nm > best[0]: best = (nm, wt, flip, sgn)
    w = best[1]
    for it, tol in enumerate((12.0, 4.0, 1.5, 1.0)):
        sky = w.pixel_to_world(det["x"][bright], det["y"][bright])
        idx, sep2d, _ = sky.match_to_catalog_sky(gsc)
        if it == 0:   # remove a global offset first (header WCS can be off by several arcsec)
            dra = np.median(((gsc[idx].ra - sky.ra) * np.cos(sky.dec.radian)).to(u.arcsec).value[sep2d.arcsec < tol])
            dde = np.median((gsc[idx].dec - sky.dec).to(u.arcsec).value[sep2d.arcsec < tol])
            sky = SkyCoord(sky.ra + dra * u.arcsec / np.cos(sky.dec.radian), sky.dec + dde * u.arcsec)
            idx, sep2d, _ = sky.match_to_catalog_sky(gsc)
        m = sep2d.arcsec < tol
        if m.sum() < 20: break
        w = fit_wcs_from_points((det["x"][bright][m], det["y"][bright][m]), gsc[idx[m]], projection="TAN", sip_degree=3)
    sky = w.pixel_to_world(det["x"], det["y"]); idx, sep2d, _ = sky.match_to_catalog_sky(gsc)
    m = sep2d.arcsec < 1.0
    resid = sep2d.arcsec[m]
    g = np.array(gaia["g"], float)[idx[m]]; x = np.array(np.ma.filled(gaia["bp_rp"], np.nan), float)[idx[m]]
    gr = -0.02275 + 0.3961 * x - 0.1243 * x ** 2 - 0.01396 * x ** 3 + 0.003775 * x ** 4      # Riello et al. 2021, G - R_Cousins
    ok = np.isfinite(gr) & (x > 0.5) & (x < 2.0) & (g > 14) & (g < 20)
    rmag = g - gr
    zp = np.median(rmag[ok] + 2.5 * np.log10(det["flux"][m][ok])) if ok.sum() > 10 else np.nan
    return w, dict(parity_flip=best[2], rot_sign=best[3], n_match=int(m.sum()), rms_arcsec=float(np.sqrt(np.mean(resid ** 2))) if m.sum() else np.nan, zp=float(zp))

def skybot(ra, dec, t_jd, rad_deg):
    url = "https://ssp.imcce.fr/webservices/skybot/api/conesearch.php"
    p = {"-ep": t_jd, "-ra": ra, "-dec": dec, "-rd": rad_deg, "-mime": "text", "-output": "obs", "-observer": "F51", "-objFilter": "111", "-from": "IASCpipeline"}
    r = requests.get(url, params=p, timeout=120); rows = []
    for line in r.text.splitlines():
        if line.startswith("#") or "|" not in line: continue
        f = [x.strip() for x in line.split("|")]
        try:
            c = SkyCoord(f[2], f[3], unit=(u.hourangle, u.deg))
            rows.append(dict(num=f[0], name=f[1], ra=c.ra.deg, dec=c.dec.deg, cls=f[4], V=float(f[5]), err_arcsec=float(f[6]),
                             dra_arcsec_h=float(f[8]), ddec_arcsec_h=float(f[9])))
        except Exception: pass
    return rows, r.text[:300]

B62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def pack_number(n):
    n = int(n)
    if n < 100000: return f"{n:05d}"
    if n < 620000: return B62[n // 10000] + f"{n % 10000:04d}"
    m = n - 620000; out = ""
    for _ in range(4): out = B62[m % 62] + out; m //= 62
    return "~" + out

def pack_provisional(desig):
    """'2018 LT' -> 'K18L00T'; '2006 CX81' -> 'K06C81X' (MPC packed provisional designation)."""
    yr, rest = desig.split()[:2]; cent = {"18": "I", "19": "J", "20": "K"}[yr[:2]]
    half, second, num = rest[0], rest[1], int(rest[2:] or 0)
    cyc = f"{num:02d}" if num < 100 else B62[num // 10] + str(num % 10)
    return cent + yr[2:] + half + cyc + second

def mpc_line(t, c, mag, tmp=None, number=None, prov=None, band="R", code="F51"):
    """80-column MPC1992 line laid out exactly as Astrometrica writes it in IASC reports:
    cols 1-5 packed number | 6-12 packed provisional or temporary designation | 13-14 blank | 15 'C' |
    16-32 'YYYY MM DD.dddddd' | 33-44 'HH MM SS.sss' | 45-56 'sDD MM SS.ss' | 57-65 blank | 66-71 'mm.m B' | 72-77 blank | 78-80 code"""
    d = t.datetime; frac = (d.hour + (d.minute + (d.second + d.microsecond / 1e6) / 60) / 60) / 24
    date = f"{d.year:04d} {d.month:02d} {d.day + frac:09.6f}"
    ra = c.ra.to_string(unit=u.hourangle, sep=" ", precision=3, pad=True)
    de = c.dec.to_string(unit=u.deg, sep=" ", precision=2, alwayssign=True, pad=True)
    num = pack_number(number) if number else ""
    des = tmp if tmp else (pack_provisional(prov) if prov and not number else "")
    m = f"{mag:4.1f} {band}" if np.isfinite(mag) else ""
    line = f"{num:>5s}{des:<7s}  C{date}{ra}{de}{'':9s}{m:<6s}{'':6s}{code}"
    assert len(line) == 80, (len(line), line); return line

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("out"); ap.add_argument("--team", default="XXX")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    ims = load(a.folder); n = len(ims); print("images:", n, [im["file"] for im in ims])
    h0 = ims[0]["hdr"]; w0 = clean_wcs(h0); ny, nx = ims[0]["data"].shape
    cen = w0.pixel_to_world(nx / 2, ny / 2); rad = 0.75 * np.hypot(nx, ny) * abs(h0["CDELT1"])
    gaia = gaia_stars(cen.ra.deg, cen.dec.deg, rad); print("gaia stars:", len(gaia))
    D, info = [], []
    for im in ims:
        det = detect(im); w, q = refine_wcs(im, det, gaia); sky = w.pixel_to_world(det["x"], det["y"])
        mag = q["zp"] - 2.5 * np.log10(det["flux"])
        D.append(dict(sky=sky, mag=mag, snr=det["flux"] / det["ferr"], x=det["x"], y=det["y"], w=w, sub=det["sub"], gap=det["gap"], ab=det["a"] / det["b"]))
        info.append(dict(file=im["file"], mjd=im["t"].mjd, n_det=len(det["x"]), **q)); print(info[-1])
    # stationary flag: matched within MATCH_ARCSEC in >= 2 other images
    stat = []
    for i in range(n):
        cnt = np.zeros(len(D[i]["sky"]), int)
        for j in range(n):
            if i == j: continue
            _, s, _ = D[i]["sky"].match_to_catalog_sky(D[j]["sky"]); cnt += (s.arcsec < MATCH_ARCSEC)
        stat.append(cnt >= 2)
    mov = [np.where(~stat[i] & (D[i]["snr"] > 4) & ~D[i]["gap"])[0] for i in range(n)]
    print("non-stationary detections per image:", [len(m) for m in mov])
    T = np.array([im["t"].mjd for im in ims]) * 1440.0    # minutes
    # linking: seed pairs from first and last usable images, predict the middle ones
    tracks = []
    for (i0, i1) in [(0, n - 1), (0, n - 2), (1, n - 1)]:
        if i1 <= i0: continue
        dtm = T[i1] - T[i0]
        A = D[i0]["sky"][mov[i0]]; B = D[i1]["sky"][mov[i1]]
        if len(A) == 0 or len(B) == 0: continue
        # astropy: B.search_around_sky(A, r) -> (idx into A, idx into B, sep, dist)
        jA, jB, sab, _ = B.search_around_sky(A, MAX_RATE * dtm * u.arcsec)
        for ka, kb, s in zip(jA, jB, sab.arcsec):
            pa, pb = A[ka], B[kb]; rate = s / dtm
            if rate < MIN_RATE: continue
            members = {i0: mov[i0][ka], i1: mov[i1][kb]}
            off_ra = (pb.ra - pa.ra).to(u.arcsec).value * np.cos(pa.dec.radian); off_de = (pb.dec - pa.dec).to(u.arcsec).value
            for k in range(n):
                if k in members: continue
                f = (T[k] - T[i0]) / dtm
                pred = SkyCoord(pa.ra + f * off_ra * u.arcsec / np.cos(pa.dec.radian), pa.dec + f * off_de * u.arcsec)
                cand = D[k]["sky"][mov[k]]
                if len(cand) == 0: continue
                idx, s2, _ = pred.match_to_catalog_sky(cand)
                if s2.arcsec < 1.2: members[k] = mov[k][idx]
            ok = False
            while len(members) >= 3:
                ks = sorted(members); t = np.array([T[k] for k in ks])
                ra = np.array([D[k]["sky"][members[k]].ra.deg for k in ks]); de = np.array([D[k]["sky"][members[k]].dec.deg for k in ks])
                mg = np.array([D[k]["mag"][members[k]] for k in ks])
                x = (ra - ra.mean()) * 3600 * np.cos(np.radians(de.mean())); y = (de - de.mean()) * 3600
                px, py = np.polyfit(t - t.mean(), x, 1), np.polyfit(t - t.mean(), y, 1)
                res = np.hypot(x - np.polyval(px, t - t.mean()), y - np.polyval(py, t - t.mean()))
                if res.max() <= MAX_RESID and np.ptp(mg) <= 1.2: ok = True; break
                if len(members) == 3: break
                # drop the worst point (by position residual, or by magnitude deviation), never a seed
                bad = np.argsort(-(res / MAX_RESID + np.abs(mg - np.median(mg)) / 0.6))
                drop = next((ks[b] for b in bad if ks[b] not in (i0, i1)), None)
                if drop is None: break
                members.pop(drop)
            if not ok: continue
            tracks.append(dict(members={int(k): int(v) for k, v in members.items()}, n=len(ks), rate=float(np.hypot(px[0], py[0])),
                               pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), mag=float(np.median(mg)),
                               ra0=float(ra[0]), dec0=float(de[0])))
    # de-duplicate (same detections)
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted((k, v) for k, v in tr["members"].items()))
        if any((k, v) in seen for k, v in key): continue
        seen.update(key); uniq.append(tr)
    print("tracklets:", len(uniq))
    # known objects
    tmid = Time(np.mean([im["t"].jd for im in ims]), format="jd")
    known, raw = skybot(cen.ra.deg, cen.dec.deg, tmid.jd, rad)
    print("SkyBoT known objects in field:", len(known))
    for tr in uniq:
        k0 = sorted(tr["members"])[0]; k1 = sorted(tr["members"])[-1]
        c = D[k0]["sky"][tr["members"][k0]]; c1 = D[k1]["sky"][tr["members"][k1]]
        # position at tmid by linear interpolation
        f = (tmid.mjd * 1440 - T[k0]) / (T[k1] - T[k0])
        pm = SkyCoord(c.ra + f * (c1.ra - c.ra), c.dec + f * (c1.dec - c.dec))
        best = None
        for kobj in known:
            s = pm.separation(SkyCoord(kobj["ra"] * u.deg, kobj["dec"] * u.deg)).arcsec
            if best is None or s < best[0]: best = (s, kobj)
        tr["known"] = best[1]["name"] if best and best[0] < max(10.0, 3 * best[1]["err_arcsec"]) else ""
        tr["known_sep"] = float(best[0]) if best else np.nan
        tr["known_V"] = best[1]["V"] if best and tr["known"] else np.nan
    # which known objects (bright enough) were missed
    recovered = {tr["known"] for tr in uniq if tr["known"]}
    for kobj in known: kobj["recovered"] = kobj["name"] in recovered
    # outputs
    import csv
    with open(os.path.join(a.out, "tracklets.csv"), "w", newline="") as fh:
        wr = csv.writer(fh); wr.writerow(["id", "n_images", "rate_arcsec_min", "pa_deg", "max_resid_arcsec", "mag_w", "ra_first", "dec_first", "known", "known_sep_arcsec", "known_V"])
        for i, tr in enumerate(uniq): wr.writerow([f"T{i:03d}", tr["n"], f"{tr['rate']:.3f}", f"{tr['pa']:.1f}", f"{tr['resid']:.2f}", f"{tr['mag']:.2f}", f"{tr['ra0']:.6f}", f"{tr['dec0']:.6f}", tr["known"], f"{tr['known_sep']:.1f}", tr["known_V"]])
    with open(os.path.join(a.out, "known_in_field.csv"), "w", newline="") as fh:
        wr = csv.writer(fh); wr.writerow(["name", "num", "class", "V", "ra", "dec", "pos_err_arcsec", "recovered"])
        for kobj in sorted(known, key=lambda z: z["V"]): wr.writerow([kobj["name"], kobj["num"], kobj["cls"], kobj["V"], f"{kobj['ra']:.6f}", f"{kobj['dec']:.6f}", kobj["err_arcsec"], kobj["recovered"]])
    unknown = [tr for tr in uniq if not tr["known"]]
    obs = []
    for tr in uniq:
        if tr["known"]:
            kobj = next(k for k in known if k["name"] == tr["known"])
            numbered = kobj["num"] not in ("-", "")
            ident = dict(number=kobj["num"] if numbered else None, prov=None if numbered else kobj["name"])
        else:
            ident = dict(tmp=f"{a.team[:3].upper()}{unknown.index(tr) + 1:04d}")
        tr["ident"] = ident
        for k in sorted(tr["members"]):
            i = tr["members"][k]; obs.append(mpc_line(ims[k]["t"], D[k]["sky"][i], D[k]["mag"][i], **ident))
    now = Time.now().datetime
    head = ["COD F51", "OBS J. Bulger, T. Lowe, A. Schultz, M. Willman", "MEA T. Vorobjov, PS1 Science Consortium",
            "TEL 1.8-m f/4.4 Ritchey-Chretien + CCD", f"ACK MPCReport file updated {now:%Y.%m.%d %H:%M:%S}", "NET Gaia DR3"]
    body = obs if obs else ["No moving objects detected"]
    with open(os.path.join(a.out, "MPCReport.txt"), "w", newline="\r\n") as fh:
        fh.write("\n".join(head + body + ["----- end -----"]) + "\n")
    # cutouts for every tracklet
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        for i, tr in enumerate(uniq):
            fig, axs = plt.subplots(1, n, figsize=(2.2 * n, 2.4))
            for k in range(n):
                ax = axs[k]; ax.set_xticks([]); ax.set_yticks([])
                kk = k if k in tr["members"] else sorted(tr["members"])[0]
                c = D[kk]["sky"][tr["members"][kk]] if k in tr["members"] else None
                if c is None:
                    ax.set_title(f"img{k} -", fontsize=7); continue
                x, y = D[k]["w"].world_to_pixel(c); x, y = int(round(float(x))), int(round(float(y)))
                cut = D[k]["sub"][max(0, y - 25):y + 26, max(0, x - 25):x + 26]
                ax.imshow(cut, origin="lower", cmap="gray", vmin=-2 * np.std(cut), vmax=6 * np.std(cut)); ax.set_title(f"img{k}", fontsize=7)
            fig.suptitle(f"T{i:03d} {tr['known'] or 'UNKNOWN'} rate {tr['rate']:.2f}\"/min w {tr['mag']:.1f}", fontsize=8)
            plt.tight_layout(); plt.savefig(os.path.join(a.out, f"T{i:03d}.png"), dpi=80); plt.close()
    except Exception as e: print("plot error", e)
    summ = dict(images=info, n_tracklets=len(uniq), n_unknown=len(unknown), n_known_in_field=len(known),
                known_recovered=sum(k["recovered"] for k in known), skybot_head=raw[:200])
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1, default=str); print(json.dumps({k: v for k, v in summ.items() if k != "images"}, indent=1))

if __name__ == "__main__":
    main()

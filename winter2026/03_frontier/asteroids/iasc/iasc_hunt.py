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

# Tunable parameters. Values tuned on PS1 DR2 warp sets (bench.py, train half; see BENCH.md); original values in comments.
NSIG, MATCH_ARCSEC, MIN_RATE, MAX_RATE, MAX_RESID = 2.5, 1.3, 0.1, 20.0, 0.4   # rates in arcsec/min (orig 2.5, 1.0, 0.03, 20, 0.6)
LINK_TOL = 1.2       # arcsec: a middle-image detection must lie this close to the seed-pair prediction (orig 1.2)
MAG_SPREAD = 0.8     # max peak-to-peak magnitude along a tracklet (orig 1.2)
MIN_SNR = 4.0        # aperture S/N for a non-stationary detection to be linked (orig 4)
STAT_MIN = 1         # stationary = matched within MATCH_ARCSEC in >= STAT_MIN other images, capped at n-1 (orig 2)
GAP_DILATE = 8       # px: detections this close to masked pixels (cell gaps, chip edges) are not linked (orig 8)
MINAREA = 5          # sep minimum area (px) (orig 5)
NOISY_FACTOR = 1.5   # mask regions whose local background RMS exceeds this x the median (noisy PS1 cells); None = off (orig: off)
ID_VFRAC, ID_VMIN = 0.25, 0.1   # identification: tracklet velocity within max(ID_VMIN "/min, ID_VFRAC x |v|) of SkyBoT's
WARP_MJD_SCALE = "tai"   # PS1 DR2 warp MJD-OBS time scale (measured on known asteroids, see BENCH.md)
AP_RADIUS = 5.0      # px: photometry aperture radius (PS1: 5 px = 1.25")
STAT_DT_MIN = 0.0    # min: only images at least this far apart in time are used for the stationary test (0 = all; PS1 unchanged)
MIN_NFRAC = None     # tracklets need >= max(3, ceil(MIN_NFRAC * n)) images (None = 3, the PS1 rule)
OBSCODE = "F51"      # MPC observatory code used for SkyBoT and the report
BAND = "R"           # photometric band of the zero point
ZTF_BADBITS = 6141   # ZTF mskimg bits treated as bad: 0 track, 2-10 (low/high resp., noisy, ghosts, spike, saturated, dead, NaN), 12 halo
                     # (bits 1 and 11 only mark detected sources and are NOT bad)
# ZTF (1.01"/px, ~2" FWHM, 30 s, 6-12+ images over ~2 h). Scaled from the PS1 values: apertures/dilation by pixel scale,
# position tolerances by the ~2x larger centroid errors, and a minimum fraction of images instead of a fixed 3.
ZTF_PARAMS = dict(AP_RADIUS=2.5, MINAREA=3, GAP_DILATE=3, MATCH_ARCSEC=1.5, LINK_TOL=2.0, MAX_RESID=1.0, MAG_SPREAD=1.5,
                  MAX_RATE=10.0, STAT_DT_MIN=30.0, MIN_NFRAC=0.5, OBSCODE="I41")

def use_params(d):
    """Set module-level tunables (used for the ZTF style; PS1 styles keep the defaults above)."""
    g = globals()
    for k, v in d.items():
        assert k in g, k
        g[k] = v

def header_style(h):
    """'iasc' = IASC PS1 chip (CDELT + CROTA2, extra keys that make astropy's PC singular);
    'warp' = PS1 DR2 skycell warp/cutout (CDELT + PC001001-style or PCi_j/CDi_j, no CROTA2);
    'ztf'  = ZTF science image (quadrant or IBE cutout; CD + TPV distortion, SHUTOPEN/SHUTCLSD, FIELDID/RCID)."""
    if str(h.get("ORIGIN", "")).startswith("Zwicky") or ("FIELDID" in h and "SHUTOPEN" in h): return "ztf"
    if "CROTA2" in h: return "iasc"
    if str(h.get("PSFORMAT", "")).strip().upper() == "SKYCELL": return "warp"
    if any(k in h for k in ("CD1_1", "PC1_1", "PC001001")): return "warp"
    return "iasc"

def obs_mid_time(h):
    """Mid-exposure time. IASC chips: DATE-OBS (UTC start). PS1 DR2 warps: MJD-OBS (start, scale WARP_MJD_SCALE)."""
    half = (h.get("EXPTIME", 0) / 2) * u.s
    if header_style(h) == "ztf":
        # ZTF: SHUTOPEN/SHUTCLSD are UTC shutter times; OBSMJD is the exposure start (~0.2-0.8 s before SHUTOPEN, measured on headers)
        if "SHUTOPEN" in h and "SHUTCLSD" in h:
            t0, t1 = Time(h["SHUTOPEN"], scale="utc"), Time(h["SHUTCLSD"], scale="utc"); return t0 + (t1 - t0) / 2
        return Time(float(h["OBSMJD"]), format="mjd", scale="utc") + half
    if "DATE-OBS" in h: return Time(h["DATE-OBS"], scale="utc") + half
    return (Time(float(h["MJD-OBS"]), format="mjd", scale=WARP_MJD_SCALE) + half).utc

def load(folder):
    ims = []
    for f in sorted(glob.glob(os.path.join(folder, "*.fits")) + glob.glob(os.path.join(folder, "*.fit"))):
        h = fits.getheader(f); d = fits.getdata(f).astype(np.float64)
        if "BSOFTEN" in h and "BOFFSET" in h:      # PS1 asinh-compressed image -> linear flux (PS1 DR2 docs)
            d = h["BOFFSET"] + h["BSOFTEN"] * 2 * np.sinh(d * np.log(10) / 2.5)
        t = obs_mid_time(h).utc; st = header_style(h); extra = None
        if st == "ztf":
            # bad pixels from the matching mskimg (stored as <folder>/mask/<same file name>), plus saturation from the header
            mf = os.path.join(folder, "mask", os.path.basename(f))
            extra = np.zeros(d.shape, bool)
            if os.path.exists(mf):
                m = fits.getdata(mf).astype(np.int32)
                if m.shape == d.shape: extra |= (m & ZTF_BADBITS) != 0
            if "SATURATE" in h:
                from scipy import ndimage
                extra |= ndimage.binary_dilation(d >= 0.9 * float(h["SATURATE"]), iterations=2)
        ims.append(dict(file=os.path.basename(f), hdr=h, data=d, t=t, style=st, mask=extra))
    return sorted(ims, key=lambda x: x["t"].jd)

def clean_wcs(h, flip=False, style="iasc"):
    """Plain TAN WCS (no distortion) from the header.
    iasc: CRVAL/CRPIX/CDELT/CROTA2 only (PS1 IASC headers carry extra keys that make astropy's PC singular).
    warp: CRVAL/CRPIX and CDi_j, or CDELTi * PCi_j (also the old PC00i00j spelling PS1 warps use).
    flip=True mirrors the x axis (parity test; the right one is chosen by Gaia match count)."""
    w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.crval = [h["CRVAL1"], h["CRVAL2"]]; w.wcs.crpix = [h["CRPIX1"], h["CRPIX2"]]
    if style == "iasc":
        c1, c2 = h["CDELT1"] * (-1 if flip else 1), h["CDELT2"]; r = np.radians(h.get("CROTA2", 0.0))
        w.wcs.cd = np.array([[c1 * np.cos(r), -c2 * np.sin(r)], [c1 * np.sin(r), c2 * np.cos(r)]])
    else:
        if "CD1_1" in h:
            cd = np.array([[h["CD1_1"], h.get("CD1_2", 0.0)], [h.get("CD2_1", 0.0), h["CD2_2"]]], float)
        else:
            pc = np.eye(2)
            for i in (1, 2):
                for j in (1, 2):
                    for key in (f"PC{i}_{j}", f"PC{i:03d}{j:03d}"):
                        if key in h: pc[i - 1, j - 1] = h[key]
            cd = np.diag([h["CDELT1"], h["CDELT2"]]) @ pc
        if flip: cd[:, 0] *= -1
        w.wcs.cd = cd
    w.wcs.set(); return w

def pixel_scale_deg(h, style):
    if style == "iasc": return abs(h["CDELT1"])
    return float(np.sqrt(abs(np.linalg.det(clean_wcs(h, style=style).wcs.cd))))

def gap_mask(d, style="iasc", extra=None):
    """PS1 IASC chips fill cell gaps / dead cells with a constant value: flag pixels whose neighbours are identical.
    Warps are sky-subtracted (half the pixels are <= 0) and mark no-data with NaN, so d <= 0 is only used for IASC chips.
    extra: an additional boolean bad-pixel mask (ZTF: mskimg bits + saturation), OR-ed in."""
    if extra is not None: return gap_mask(d, style) | extra
    from scipy import ndimage
    flat = np.zeros(d.shape, bool)
    eq_r = d[:, 1:] == d[:, :-1]; eq_d = d[1:, :] == d[:-1, :]
    flat[:-1, :-1] = eq_r[:-1, :] & eq_d[:, :-1]
    flat = ndimage.binary_opening(flat, structure=np.ones((3, 3)))     # real flat runs, not single coincidences
    bad = flat | ~np.isfinite(d)
    return bad | (d <= 0) if style == "iasc" else bad

def detect(im):
    d = np.ascontiguousarray(im["data"]); mask = gap_mask(d, im.get("style", "iasc"), im.get("mask"))
    if not np.isfinite(d).all(): d = np.ascontiguousarray(np.where(np.isfinite(d), d, 0.0))
    from scipy import ndimage
    near_gap = ndimage.binary_dilation(mask, iterations=GAP_DILATE) if GAP_DILATE > 0 else mask
    bkg = sep.Background(d, mask=mask, bw=64, bh=64); sub = d - bkg.back()
    if NOISY_FACTOR:
        rmap = bkg.rms(); noisy = rmap > NOISY_FACTOR * np.median(rmap[~mask]) if (~mask).any() else np.zeros_like(mask)
        if noisy.any():
            mask = mask | noisy; near_gap = near_gap | ndimage.binary_dilation(noisy, iterations=max(GAP_DILATE, 1))
    obj = sep.extract(sub, NSIG, err=bkg.globalrms, mask=mask, minarea=MINAREA, deblend_cont=0.01)
    flux, ferr, _ = sep.sum_circle(sub, obj["x"], obj["y"], AP_RADIUS, err=bkg.globalrms, mask=mask)
    xi = np.clip(np.round(obj["x"]).astype(int), 0, d.shape[1] - 1); yi = np.clip(np.round(obj["y"]).astype(int), 0, d.shape[0] - 1)
    ok = (flux > 0) & (obj["flag"] < 4) & (obj["a"] < 8)
    o = obj[ok]; return dict(x=o["x"], y=o["y"], flux=flux[ok], ferr=ferr[ok], a=o["a"], b=o["b"], peak=o["peak"], rms=bkg.globalrms, sub=sub,
                             gap=near_gap[yi, xi][ok], good_area_px=int((~mask).sum()))

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
    style = im.get("style", "iasc")
    for flip in (False, True):
        for sgn in ((1, -1) if style == "iasc" else (1,)):
            hh = dict(im["hdr"])
            if style == "iasc": hh["CROTA2"] = sgn * im["hdr"].get("CROTA2", 0.0)
            wt = clean_wcs(hh, flip, style)
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
    if style == "ztf":   # ZTF r/g/i ~ SDSS r/g/i (Riello et al. 2021, Table C.2, G - SDSS)
        f = str(im["hdr"].get("FILTER", "ZTF_r")).strip()[-1:]
        gr = {"r": -0.12879 + 0.24662 * x - 0.027464 * x ** 2 - 0.049465 * x ** 3,
              "g": 0.13518 - 0.46245 * x - 0.25171 * x ** 2 + 0.021349 * x ** 3,
              "i": -0.29676 + 0.64728 * x - 0.10141 * x ** 2}.get(f, gr)
    ok = np.isfinite(gr) & (x > 0.5) & (x < 2.0) & (g > 14) & (g < 20)
    rmag = g - gr
    zp = np.median(rmag[ok] + 2.5 * np.log10(det["flux"][m][ok])) if ok.sum() > 10 else np.nan
    return w, dict(parity_flip=best[2], rot_sign=best[3], n_match=int(m.sum()), rms_arcsec=float(np.sqrt(np.mean(resid ** 2))) if m.sum() else np.nan, zp=float(zp))

def skybot(ra, dec, t_jd, rad_deg, observer=None):
    url = "https://ssp.imcce.fr/webservices/skybot/api/conesearch.php"
    p = {"-ep": t_jd, "-ra": ra, "-dec": dec, "-rd": rad_deg, "-mime": "text", "-output": "obs", "-observer": observer or OBSCODE, "-objFilter": "111", "-from": "IASCpipeline"}
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

def image_stats(im, det, w, q, mask_area_px, scale_arcsec):
    """Domain-shift diagnostics: FWHM (2 x half-light radius of bright isolated stars), background RMS, 5-sigma limiting magnitude
    (naive: pixel RMS x sqrt(aperture area); empirical: scatter of random 5 px apertures, which includes resampling-correlated noise),
    detection density (S/N > 5 per arcmin^2)."""
    sub = det["sub"]; ok = (det["flux"] / det["ferr"] > 30) & (det["flux"] / det["ferr"] < 500) & ~det["gap"] & (det["a"] / det["b"] < 1.3)
    fwhm = np.nan
    if ok.sum() >= 5:
        r50, fl = sep.flux_radius(sub, det["x"][ok], det["y"][ok], np.full(ok.sum(), 15.0), 0.5, subpix=5)
        fwhm = float(2 * np.median(r50[fl == 0]) * scale_arcsec) if (fl == 0).sum() >= 5 else np.nan
    rng = np.random.default_rng(0); ny, nx = sub.shape
    xs, ys = rng.uniform(20, nx - 20, 3000), rng.uniform(20, ny - 20, 3000)
    finite = np.isfinite(im["data"])
    keep = finite[ys.astype(int), xs.astype(int)]
    f, _, _ = sep.sum_circle(sub, xs[keep], ys[keep], AP_RADIUS)
    f = f[np.isfinite(f)]; emp = 1.4826 * np.median(np.abs(f - np.median(f))) if len(f) > 100 else np.nan
    naive = det["rms"] * np.sqrt(np.pi * AP_RADIUS ** 2)
    area_arcmin2 = mask_area_px * scale_arcsec ** 2 / 3600
    return dict(fwhm_arcsec=fwhm, bkg_rms=float(det["rms"]), ap_noise_ratio=float(emp / naive) if np.isfinite(emp) else np.nan,
                lim5_naive=float(q["zp"] - 2.5 * np.log10(5 * naive)), lim5_emp=float(q["zp"] - 2.5 * np.log10(5 * emp)) if emp > 0 else np.nan,
                dens_snr5_arcmin2=float(((det["flux"] / det["ferr"]) > 5).sum() / area_arcmin2), area_arcmin2=float(area_arcmin2))

def measure(folder, gaia_fn=None, verbose=True):
    """Stage 1: load, detect, Gaia WCS refit and zero point for every image of a set."""
    ims = load(folder); n = len(ims)
    if ims and ims[0]["style"] == "ztf": use_params(ZTF_PARAMS)
    if verbose: print("images:", n, [im["file"] for im in ims])
    h0 = ims[0]["hdr"]; st = ims[0]["style"]; w0 = clean_wcs(h0, style=st); ny, nx = ims[0]["data"].shape
    scale = pixel_scale_deg(h0, st)
    cen = w0.pixel_to_world(nx / 2, ny / 2); rad = 0.75 * np.hypot(nx, ny) * scale
    gaia = (gaia_fn or gaia_stars)(cen.ra.deg, cen.dec.deg, rad)
    if verbose: print("gaia stars:", len(gaia))
    D, info = [], []
    for im in ims:
        det = detect(im); w, q = refine_wcs(im, det, gaia); sky = w.pixel_to_world(det["x"], det["y"])
        mag = q["zp"] - 2.5 * np.log10(det["flux"])
        D.append(dict(sky=sky, mag=mag, snr=det["flux"] / det["ferr"], x=det["x"], y=det["y"], w=w, sub=det["sub"], gap=det["gap"], ab=det["a"] / det["b"]))
        try: stats = image_stats(im, det, w, q, det["good_area_px"], scale * 3600)
        except Exception as e: stats = dict(stats_error=str(e))
        info.append(dict(file=im["file"], mjd=im["t"].mjd, n_det=len(det["x"]), style=im["style"], **q, **stats))
        if verbose: print(info[-1])
    return ims, D, info, cen, rad

def _tangent(sky, ra0, de0):
    """Gnomonic projection about (ra0, de0) in arcsec (xi east, eta north)."""
    ra, de = np.radians(sky.ra.deg), np.radians(sky.dec.deg); a0, d0 = np.radians(ra0), np.radians(de0)
    cosc = np.sin(d0) * np.sin(de) + np.cos(d0) * np.cos(de) * np.cos(ra - a0)
    xi = np.cos(de) * np.sin(ra - a0) / cosc; eta = (np.cos(d0) * np.sin(de) - np.sin(d0) * np.cos(de) * np.cos(ra - a0)) / cosc
    return np.column_stack([xi, eta]) * 206264.80624709636

LAST_DIAG = {}     # stationary flags / linkable indices of the last find_tracklets call (bench diagnostics)

def find_tracklets(D, T, verbose=True):
    """Stage 2: drop stationary sources, link the rest into >= 3-image linear tracklets. T = image mid-times in minutes.
    Same algorithm as the original per-pair loop, vectorised in a common tangent plane (KD-trees)."""
    from scipy.spatial import cKDTree
    n = len(D)
    ra0, de0 = float(np.median(D[0]["sky"].ra.deg)), float(np.median(D[0]["sky"].dec.deg))
    P = [_tangent(d["sky"], ra0, de0) if len(d["sky"]) else np.zeros((0, 2)) for d in D]
    trees = [cKDTree(p) for p in P]
    # stationary flag: matched within MATCH_ARCSEC in >= STAT_MIN other images
    # (STAT_DT_MIN > 0, ZTF: only images far enough apart in time count, so a slow mover in closely spaced images is not "stationary")
    stat = []
    for i in range(n):
        cnt = np.zeros(len(P[i]), int); n_far = 0
        for j in range(n):
            if i == j: continue
            if STAT_DT_MIN > 0 and abs(T[j] - T[i]) < STAT_DT_MIN: continue
            n_far += 1
            if len(P[j]) == 0 or len(P[i]) == 0: continue
            dd, _ = trees[j].query(P[i], k=1); cnt += (dd < MATCH_ARCSEC)
        stat.append(cnt >= min(STAT_MIN, n_far) if n_far else np.zeros(len(P[i]), bool))
    mov = [np.where(~stat[i] & (D[i]["snr"] > MIN_SNR) & ~D[i]["gap"])[0] for i in range(n)]
    if verbose: print("non-stationary detections per image:", [len(m) for m in mov])
    LAST_DIAG.clear(); LAST_DIAG.update(stat=stat, mov=mov)
    Pm = [P[i][mov[i]] for i in range(n)]; Tm = [cKDTree(p) if len(p) else None for p in Pm]
    tracks = []
    nmin = max(3, int(np.ceil(MIN_NFRAC * n))) if MIN_NFRAC else 3
    seeds = [(0, n - 1), (0, n - 2), (1, n - 1)]
    if n > 4:   # many images (ZTF): seed from every pair at least half the set apart, so objects missing from the first or
                # last images (passing a star, edge, shallower twilight frames) can still be linked
        seeds = [(i, j) for i in range(n) for j in range(n - 1, i, -1) if j - i >= n // 2]
    for (i0, i1) in seeds:
        if i1 <= i0 or Tm[i0] is None or Tm[i1] is None: continue
        dtm = T[i1] - T[i0]
        sm = Tm[i0].sparse_distance_matrix(Tm[i1], MAX_RATE * dtm, output_type="ndarray")
        ka, kb, s = sm["i"], sm["j"], sm["v"]
        keep = s / dtm >= MIN_RATE; ka, kb = ka[keep], kb[keep]
        if len(ka) == 0: continue
        A, B = Pm[i0][ka], Pm[i1][kb]
        hits = {}
        for k in range(n):
            if k in (i0, i1) or Tm[k] is None: continue
            f = (T[k] - T[i0]) / dtm; pred = A + f * (B - A)
            dd, ii = Tm[k].query(pred, k=1); hits[k] = np.where(dd < LINK_TOL, ii, -1)
        nmem = 2 + sum((h >= 0).astype(int) for h in hits.values()) if hits else np.full(len(ka), 2)
        for p in np.where(nmem >= nmin)[0]:
            members = {i0: mov[i0][ka[p]], i1: mov[i1][kb[p]]}
            for k, h in hits.items():
                if h[p] >= 0: members[k] = mov[k][h[p]]
            ok = False
            while len(members) >= nmin:
                ks = sorted(members); t = np.array([T[k] for k in ks])
                ra = np.array([D[k]["sky"][members[k]].ra.deg for k in ks]); de = np.array([D[k]["sky"][members[k]].dec.deg for k in ks])
                mg = np.array([D[k]["mag"][members[k]] for k in ks])
                x = (ra - ra.mean()) * 3600 * np.cos(np.radians(de.mean())); y = (de - de.mean()) * 3600     # original fit frame
                px, py = np.polyfit(t - t.mean(), x, 1), np.polyfit(t - t.mean(), y, 1)
                res = np.hypot(x - np.polyval(px, t - t.mean()), y - np.polyval(py, t - t.mean()))
                if res.max() <= MAX_RESID and np.ptp(mg) <= MAG_SPREAD: ok = True; break
                if len(members) == nmin: break
                # drop the worst point (by position residual, or by magnitude deviation), never a seed
                bad = np.argsort(-(res / MAX_RESID + np.abs(mg - np.median(mg)) / (MAG_SPREAD / 2)))
                drop = next((ks[b] for b in bad if ks[b] not in (i0, i1)), None)
                if drop is None: break
                members.pop(drop)
            if not ok: continue
            c0 = D[ks[0]]["sky"][members[ks[0]]]
            tracks.append(dict(members={int(k): int(v) for k, v in members.items()}, n=len(ks), rate=float(np.hypot(px[0], py[0])),
                               pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), mag=float(np.median(mg)),
                               ra0=float(c0.ra.deg), dec0=float(c0.dec.deg), vx=float(px[0]), vy=float(py[0])))
    # de-duplicate (same detections)
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted((k, v) for k, v in tr["members"].items()))
        if any((k, v) in seen for k, v in key): continue
        seen.update(key); uniq.append(tr)
    if verbose: print("tracklets:", len(uniq))
    return uniq

def identify(uniq, D, T, tmid_mjd, known):
    """Match tracklets (position interpolated to tmid) to SkyBoT objects; sets tr['known'] and kobj['recovered']."""
    for tr in uniq:
        k0 = sorted(tr["members"])[0]; k1 = sorted(tr["members"])[-1]
        c = D[k0]["sky"][tr["members"][k0]]; c1 = D[k1]["sky"][tr["members"][k1]]
        f = (tmid_mjd * 1440 - T[k0]) / (T[k1] - T[k0])      # position at tmid by linear interpolation
        pm = SkyCoord(c.ra + f * (c1.ra - c.ra), c.dec + f * (c1.dec - c.dec))
        best = None
        for kobj in known:
            if ID_VFRAC is not None and "vx" in tr:    # motion must agree too (a fast false tracklet can pass near a known object)
                kv = np.hypot(kobj["dra_arcsec_h"], kobj["ddec_arcsec_h"]) / 60
                dv = np.hypot(tr["vx"] - kobj["dra_arcsec_h"] / 60, tr["vy"] - kobj["ddec_arcsec_h"] / 60)
                if dv > max(ID_VMIN, ID_VFRAC * kv): continue
            s = pm.separation(SkyCoord(kobj["ra"] * u.deg, kobj["dec"] * u.deg)).arcsec
            if best is None or s < best[0]: best = (s, kobj)
        tr["known"] = best[1]["name"] if best and best[0] < max(10.0, 3 * best[1]["err_arcsec"]) else ""
        tr["known_sep"] = float(best[0]) if best else np.nan
        tr["known_V"] = best[1]["V"] if best and tr["known"] else np.nan
    recovered = {tr["known"] for tr in uniq if tr["known"]}
    for kobj in known: kobj["recovered"] = kobj["name"] in recovered
    return uniq

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("out"); ap.add_argument("--team", default="XXX")
    ap.add_argument("--sensitive", action="store_true",
                    help="2.0-sigma detection, S/N >= 3 (from the parallel handoff, measured there on 40 PS1 sets: V 20.5-21.5 recovery 5/17 -> 7/17, about 2x the false tracklets)")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    if a.sensitive:
        global NSIG, MIN_SNR
        NSIG, MIN_SNR = 2.0, 3.0
    ims, D, info, cen, rad = measure(a.folder); n = len(ims)
    T = np.array([im["t"].mjd for im in ims]) * 1440.0    # minutes
    uniq = find_tracklets(D, T)
    # known objects
    tmid = Time(np.mean([im["t"].jd for im in ims]), format="jd")
    known, raw = skybot(cen.ra.deg, cen.dec.deg, tmid.jd, rad)
    print("SkyBoT known objects in field:", len(known))
    identify(uniq, D, T, tmid.mjd, known)
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
    ztf = ims[0]["style"] == "ztf"
    band = str(ims[0]["hdr"].get("FILTER", "ZTF_r")).strip()[-1:] if ztf else "R"
    with open(os.path.join(a.out, "detections.csv"), "w", newline="") as fh:     # per-image positions of every tracklet
        wr = csv.writer(fh); wr.writerow(["id", "image", "utc", "ra", "dec", "mag", "known"])
        for i, tr in enumerate(uniq):
            for k in sorted(tr["members"]):
                c = D[k]["sky"][tr["members"][k]]
                wr.writerow([f"T{i:03d}", ims[k]["file"], ims[k]["t"].isot, f"{c.ra.deg:.7f}", f"{c.dec.deg:.7f}", f"{D[k]['mag'][tr['members'][k]]:.2f}", tr["known"]])
    for tr in uniq:
        if tr["known"]:
            kobj = next(k for k in known if k["name"] == tr["known"])
            numbered = kobj["num"] not in ("-", "")
            ident = dict(number=kobj["num"] if numbered else None, prov=None if numbered else kobj["name"])
        else:
            ident = dict(tmp=f"{a.team[:3].upper()}{unknown.index(tr) + 1:04d}")
        tr["ident"] = ident
        for k in sorted(tr["members"]):
            i = tr["members"][k]
            obs.append(mpc_line(ims[k]["t"], D[k]["sky"][i], D[k]["mag"][i], band=band, code=OBSCODE, **ident) if ztf else
                       mpc_line(ims[k]["t"], D[k]["sky"][i], D[k]["mag"][i], **ident))
    now = Time.now().datetime
    head = ["COD F51", "OBS J. Bulger, T. Lowe, A. Schultz, M. Willman", "MEA T. Vorobjov, PS1 Science Consortium",
            "TEL 1.8-m f/4.4 Ritchey-Chretien + CCD", f"ACK MPCReport file updated {now:%Y.%m.%d %H:%M:%S}", "NET Gaia DR3"]
    if ztf:   # archival ZTF data: positions for checking only, NOT a submission
        head = [f"COD {OBSCODE}", "COM Archival ZTF public science images (IRSA); remeasured positions for checking only - not for submission",
                "TEL 1.2-m Schmidt + CCD (ZTF)", f"ACK file written {now:%Y.%m.%d %H:%M:%S}", "NET Gaia DR3"]
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

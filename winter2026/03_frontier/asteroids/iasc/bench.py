"""
Benchmark iasc_hunt.py on public Pan-STARRS1 DR2 single-epoch warp images, with known asteroids (SkyBoT, observer F51)
as ground truth.

Subcommands (run with python3 -I; downloads go to --root, one directory per set, never into the repo):
  select   sample ecliptic positions (|beta| < 10 deg), list PS1 DR2 warps, keep nights with >= 3 warps of one skycell
           within MAX_SPAN_H hours (>= MIN_GAP_MIN apart); fetch low-resolution coverage previews and choose a
           2400 px window with the largest pixel coverage common to all images.        -> <root>/sets.json
  fetch    download the 2400 x 2400 px cutouts (fitscut.cgi) for every selected set.   -> <root>/<set>/*.fits
  measure  run iasc_hunt stage 1 (detection + Gaia WCS + photometry) per set, cached per NSIG/gap parameters;
           cache SkyBoT ground truth per set.                                           -> <root>/cache/
  evaluate run stage 2 (stationary removal, linking, identification) with a parameter set and score it.
  tune     grid search over linking/detection parameters on the TRAIN sets, then score held-out TEST sets.
  report   write the CSVs and the recovery-vs-magnitude PNG used in BENCH.md.

Ground truth = SkyBoT objects at the set mid-time whose predicted positions (linear motion from the SkyBoT rates)
fall on finite pixels in >= 3 images (that is the requirement the pipeline itself has).
"""
import sys, os, json, time, math, argparse, hashlib, pickle, random, csv, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))     # -I drops the script dir; we want iasc_hunt from here only
import numpy as np, requests
from concurrent.futures import ThreadPoolExecutor

PS1 = "https://ps1images.stsci.edu"
UA = {"User-Agent": "ps1-asteroid-bench/0.1 (research benchmark; low request rate)"}
MAX_SPAN_H, MIN_GAP_MIN, CUT_PX, PREV_PX, PREV_OUT = 1.5, 8.0, 2400, 6400, 256
MIN_COVER = 0.80        # min fraction of the 2400 px window covered by all images of the set

def get(url, params=None, timeout=300, tries=4, stream=False):
    for k in range(tries):
        try:
            r = requests.get(url, params=params, timeout=timeout, headers=UA, stream=stream)
            if r.status_code == 200: return r
        except requests.RequestException: pass
        time.sleep(3 * (k + 1))
    raise RuntimeError(f"GET failed: {url} {params}")

# ----------------------------------------------------------------------------------------------- select
def ecliptic_points(n, seed):
    from astropy.coordinates import SkyCoord, GeocentricTrueEcliptic
    import astropy.units as u
    rng = np.random.default_rng(seed); out = []
    while len(out) < n:
        lam, beta = rng.uniform(0, 360), rng.uniform(-10, 10)
        c = SkyCoord(lam * u.deg, beta * u.deg, frame=GeocentricTrueEcliptic(equinox="J2000")).icrs
        g = c.galactic
        if c.dec.deg < -25 or abs(g.b.deg) < 12: continue    # PS1 3pi limit; skip the crowded Galactic plane (runtime)
        out.append((round(c.ra.deg, 4), round(c.dec.deg, 4), round(beta, 2)))
    return out

def list_warps(ra, dec):
    r = get(f"{PS1}/cgi-bin/ps1filenames.py", dict(ra=ra, dec=dec, filters="grizy", type="warp"), timeout=120)
    rows = []
    for line in r.text.splitlines()[1:]:
        f = line.split()
        if len(f) < 10: continue
        rows.append(dict(projcell=int(f[0]), subcell=int(f[1]), filter=f[4], mjd=float(f[5]), filename=f[7], badflag=int(f[9])))
    return rows

def night_sets(rows):
    """Group warps by skycell and night; per night choose the best window of 3-4 images within MAX_SPAN_H, spaced
    >= MIN_GAP_MIN (back-to-back exposures < 1 min apart look stationary and are dropped). Same filter preferred."""
    from collections import defaultdict
    g = defaultdict(list)
    for r in rows:
        if r["badflag"] == 0: g[(r["projcell"], r["subcell"], int(math.floor(r["mjd"])))].append(r)
    out = []
    for key, rs in g.items():
        rs = sorted(rs, key=lambda z: z["mjd"])
        best = None
        for filt in sorted({r["filter"] for r in rs}) + ["mixed"]:
            cand = [r for r in rs if filt == "mixed" or r["filter"] == filt]
            keep = []
            for r in cand:
                if not keep or (r["mjd"] - keep[-1]["mjd"]) * 1440 >= MIN_GAP_MIN: keep.append(r)
            for i in range(len(keep)):
                win = [r for r in keep[i:] if (r["mjd"] - keep[i]["mjd"]) * 24 <= MAX_SPAN_H]
                if len(win) < 3: continue
                if len(win) > 4: win = [win[j] for j in np.linspace(0, len(win) - 1, 4).round().astype(int)]
                score = (len(win), filt != "mixed")
                if best is None or score > best[0]: best = (score, win, filt)
        if best: out.append(dict(projcell=key[0], subcell=key[1], night=key[2], filter=best[2], images=best[1]))
    return out

def skycell_center(filename):
    """CRPIX/CRVAL of the full warp (compressed header, first 2880*20 bytes) -> sky position of the skycell centre."""
    from astropy.io import fits
    from astropy.wcs import WCS
    r = requests.get(PS1 + filename, headers={**UA, "Range": "bytes=0-80639"}, timeout=120)
    txt = r.content.decode("ascii", "replace"); cards = [txt[i:i + 80] for i in range(0, len(txt), 80)]
    ext = [c for c in cards[cards.index(next(c for c in cards if c.startswith("XTENSION"))):]]
    h = fits.Header()
    for c in ext:
        if c.startswith("END "): break
        try: h.append(fits.Card.fromstring(c))
        except Exception: pass
    nx, ny = h["ZNAXIS1"], h["ZNAXIS2"]
    w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]; w.wcs.crval = [h["CRVAL1"], h["CRVAL2"]]; w.wcs.crpix = [h["CRPIX1"], h["CRPIX2"]]
    w.wcs.cd = np.array([[h["CDELT1"] * h.get("PC001001", 1.0), h["CDELT1"] * h.get("PC001002", 0.0)],
                         [h["CDELT2"] * h.get("PC002001", 0.0), h["CDELT2"] * h.get("PC002002", 1.0)]]); w.wcs.set()
    c = w.pixel_to_world((nx - 1) / 2, (ny - 1) / 2); return float(c.ra.deg), float(c.dec.deg)

def preview(filename, ra, dec):
    from astropy.io import fits
    r = get(f"{PS1}/cgi-bin/fitscut.cgi", dict(red=filename, ra=ra, dec=dec, size=PREV_PX, output_size=PREV_OUT, format="fits"))
    import io
    with fits.open(io.BytesIO(r.content)) as f: return f[0].header.copy(), np.isfinite(f[0].data)

def choose_window(masks, hdr):
    """Largest common coverage window of CUT_PX px (in preview pixels) -> (fraction, ra, dec)."""
    from astropy.wcs import WCS
    common = np.logical_and.reduce(masks).astype(float); k = int(round(CUT_PX * PREV_OUT / PREV_PX))
    S = np.pad(common.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    best = (-1, 0, 0)
    for y in range(0, common.shape[0] - k + 1, 2):
        for x in range(0, common.shape[1] - k + 1, 2):
            s = S[y + k, x + k] - S[y, x + k] - S[y + k, x] + S[y, x]
            if s > best[0]: best = (s, x, y)
    frac = best[0] / k ** 2; cx, cy = best[1] + k / 2 - 0.5, best[2] + k / 2 - 0.5
    hh = hdr.copy()
    for key in list(hh.keys()):
        if key.startswith("PC0"): hh.remove(key)
    w = WCS(naxis=2); w.wcs.ctype = ["RA---TAN", "DEC--TAN"]; w.wcs.crval = [hdr["CRVAL1"], hdr["CRVAL2"]]; w.wcs.crpix = [hdr["CRPIX1"], hdr["CRPIX2"]]
    w.wcs.cd = np.array([[hdr["CDELT1"] * hdr.get("PC001001", 1.0), hdr["CDELT1"] * hdr.get("PC001002", 0.0)],
                         [hdr["CDELT2"] * hdr.get("PC002001", 0.0), hdr["CDELT2"] * hdr.get("PC002002", 1.0)]]); w.wcs.set()
    c = w.pixel_to_world(cx, cy); return float(frac), float(c.ra.deg), float(c.dec.deg)

def cmd_select(a):
    os.makedirs(a.root, exist_ok=True); path = os.path.join(a.root, "sets.json")
    sets = json.load(open(path)) if os.path.exists(path) else []
    have = {s["id"] for s in sets}; seen_cells = {(s["projcell"], s["subcell"]) for s in sets}
    pts = ecliptic_points(a.npoints, a.seed)
    with ThreadPoolExecutor(2) as ex: listings = list(ex.map(lambda p: (p, list_warps(p[0], p[1])), pts))
    cands = []
    for p, rows in listings:
        ns = night_sets(rows)
        for s in ns:
            s["beta"] = p[2]; s["qra"], s["qdec"] = p[0], p[1]
        # one set per skycell (independent fields), prefer 4 images, same filter
        ns.sort(key=lambda s: (-len(s["images"]), s["filter"] == "mixed"))
        if ns: cands.append(ns[0])
    print("positions:", len(pts), "with a usable night:", len(cands))
    random.Random(a.seed).shuffle(cands)
    for s in cands:
        if len(sets) >= a.nsets: break
        if (s["projcell"], s["subcell"]) in seen_cells: continue
        sid = f"sc{s['projcell']}_{s['subcell']:03d}_{s['night']}"
        if sid in have: continue
        try:
            ra, dec = skycell_center(s["images"][0]["filename"])
            pv = [preview(im["filename"], ra, dec) for im in s["images"]]
            masks = [m for _, m in pv]
            # with 4 images, drop one if that raises common coverage a lot (still >= 3)
            frac, cra, cdec = choose_window(masks, pv[0][0]); imgs = s["images"]
            if len(imgs) == 4 and frac < MIN_COVER:
                alt = max(((choose_window([m for j, m in enumerate(masks) if j != d], pv[0][0]), d) for d in range(4)), key=lambda z: z[0][0])
                if alt[0][0] >= MIN_COVER: (frac, cra, cdec), imgs = alt[0], [im for j, im in enumerate(imgs) if j != alt[1]]
            print(sid, s["filter"], len(imgs), f"cover {frac:.2f}", flush=True)
            if frac < MIN_COVER: continue
            filt = imgs[0]["filter"] if len({im["filter"] for im in imgs}) == 1 else "mixed"
            sets.append(dict(id=sid, projcell=s["projcell"], subcell=s["subcell"], night=s["night"], filter=filt, beta=s["beta"],
                             ra=cra, dec=cdec, cover=frac, images=imgs))
            seen_cells.add((s["projcell"], s["subcell"]))
            json.dump(sets, open(path, "w"), indent=1)
        except Exception as e: print("skip", sid, e)
    json.dump(sets, open(path, "w"), indent=1); print("sets:", len(sets))

# ----------------------------------------------------------------------------------------------- fetch
def cmd_fetch(a):
    sets = json.load(open(os.path.join(a.root, "sets.json")))
    jobs = []
    for s in sets:
        d = os.path.join(a.root, s["id"]); os.makedirs(d, exist_ok=True)
        for im in s["images"]:
            out = os.path.join(d, os.path.basename(im["filename"]))
            if not os.path.exists(out): jobs.append((im["filename"], s["ra"], s["dec"], out))
    def one(j):
        fn, ra, dec, out = j
        r = get(f"{PS1}/cgi-bin/fitscut.cgi", dict(red=fn, ra=ra, dec=dec, size=CUT_PX, format="fits"))
        if not r.content.startswith(b"SIMPLE"): raise RuntimeError("not FITS: " + fn)
        open(out + ".part", "wb").write(r.content); os.replace(out + ".part", out); return out
    print("to download:", len(jobs))
    with ThreadPoolExecutor(3) as ex:
        for k, o in enumerate(ex.map(one, jobs)):
            if k % 20 == 0: print(k, o, flush=True)

# ----------------------------------------------------------------------------------------------- measure
def pkey(p):
    return hashlib.md5(json.dumps(p, sort_keys=True).encode()).hexdigest()[:10]

def gaia_cached(cachedir):
    import iasc_hunt as H
    def f(ra, dec, rad):
        p = os.path.join(cachedir, "gaia.pkl")
        if os.path.exists(p): return pickle.load(open(p, "rb"))
        t = H.gaia_stars(ra, dec, rad); pickle.dump(t, open(p, "wb")); return t
    return f

DET_KEYS = ("NSIG", "GAP_DILATE", "MINAREA")

def measure_set(root, s, det_params):
    import iasc_hunt as H
    det_params = det_key(det_params)
    for k, v in dict(DEFAULT_DET, **det_params).items(): setattr(H, k, v)
    cd = os.path.join(root, "cache", s["id"]); os.makedirs(cd, exist_ok=True)
    out = os.path.join(cd, f"m_{pkey(det_params)}.pkl")
    if os.path.exists(out): return out
    ims, D, info, cen, rad = H.measure(os.path.join(root, s["id"]), gaia_fn=gaia_cached(cd), verbose=False)
    for d in D: d.pop("sub", None)
    meta = [dict(file=im["file"], t_mjd=im["t"].mjd, shape=im["data"].shape, finite=np.isfinite(im["data"]) & (im["data"] != 0)) for im in ims]
    pickle.dump(dict(D=D, info=info, cen=(cen.ra.deg, cen.dec.deg), rad=rad, meta=meta), open(out, "wb"))
    return out

def skybot_cached(root, s, cen, rad, tmid_jd):
    import iasc_hunt as H
    p = os.path.join(root, "cache", s["id"], "skybot.json")
    if os.path.exists(p): return json.load(open(p))
    rows, raw = H.skybot(cen[0], cen[1], tmid_jd, rad)
    json.dump(dict(rows=rows, head=raw), open(p, "w")); return dict(rows=rows, head=raw)

def cmd_measure(a):
    sets = json.load(open(os.path.join(a.root, "sets.json")))
    det = json.loads(a.det) if a.det else {}
    ids = set(a.only.split(",")) if a.only else None
    for s in sets:
        if ids and s["id"] not in ids: continue
        t0 = time.time()
        try:
            p = measure_set(a.root, s, det); m = pickle.load(open(p, "rb"))
            tmid = np.mean([x["t_mjd"] for x in m["meta"]]) + 2400000.5
            skybot_cached(a.root, s, m["cen"], m["rad"], tmid)
            print(s["id"], "ok", f"{time.time() - t0:.0f}s", [i["n_det"] for i in m["info"]], flush=True)
        except Exception as e: print(s["id"], "FAILED", repr(e)[:300], flush=True)

# ----------------------------------------------------------------------------------------------- evaluate
def truth_for_set(m, sky):
    """Known objects whose linearly-propagated SkyBoT position lands on finite pixels of >= 3 images (WCS of each image)."""
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    tmid = np.mean([x["t_mjd"] for x in m["meta"]]); out = []
    for o in sky["rows"]:
        on = []; pos = []
        for d, mt in zip(m["D"], m["meta"]):
            dt_h = (mt["t_mjd"] - tmid) * 24
            dec = o["dec"] + o["ddec_arcsec_h"] * dt_h / 3600; ra = o["ra"] + o["dra_arcsec_h"] * dt_h / 3600 / np.cos(np.radians(o["dec"]))
            x, y = d["w"].world_to_pixel(SkyCoord(ra * u.deg, dec * u.deg)); x, y = float(x), float(y)
            ny, nx = mt["shape"]; xi, yi = int(round(x)), int(round(y))
            ok = 5 <= xi < nx - 5 and 5 <= yi < ny - 5 and bool(mt["finite"][yi, xi])
            on.append(ok); pos.append((ra, dec, x, y))
        if sum(on) >= 3:
            out.append(dict(o, on=on, pos=pos, rate=float(np.hypot(o["dra_arcsec_h"], o["ddec_arcsec_h"]) / 60)))
    return out

def diagnose(m, o, H):
    """Why was a known object missed? Per image: nearest detection to the SkyBoT prediction, then the first cut it fails."""
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    from scipy import ndimage
    stat, mov = H.LAST_DIAG["stat"], H.LAST_DIAG["mov"]
    r = max(1.5, 3 * o["err_arcsec"]); per = []; pts = []
    for k, (d, mt) in enumerate(zip(m["D"], m["meta"])):
        if not o["on"][k]: per.append("off_image"); continue
        ra, dec, x, y = o["pos"][k]
        if len(d["sky"]) == 0: per.append("undetected"); continue
        idx, s2, _ = SkyCoord(ra * u.deg, dec * u.deg).match_to_catalog_sky(d["sky"]); idx = int(np.ravel(idx)[0]); s2 = float(np.ravel(s2.arcsec)[0])
        if s2 > r:
            xi, yi = int(round(x)), int(round(y)); fin = mt["finite"]
            y0, y1, x0, x1 = max(0, yi - 10), yi + 11, max(0, xi - 10), xi + 11
            per.append("gap" if not fin[y0:y1, x0:x1].all() else "undetected"); continue
        if stat[k][idx]: per.append("stationary_blend")
        elif d["gap"][idx]: per.append("gap")
        elif d["snr"][idx] <= H.MIN_SNR: per.append("low_snr")
        else: per.append("linkable"); pts.append((k, idx))
    out = dict(per_image="|".join(per), n_linkable=len(pts))
    if o["err_arcsec"] > 10: out["why"] = "poor_ephemeris"; return out
    if len(pts) >= 3:
        T = np.array([mt["t_mjd"] for mt in m["meta"]]) * 1440
        t = np.array([T[k] for k, _ in pts]); sk = [m["D"][k]["sky"][i] for k, i in pts]
        ra = np.array([c.ra.deg for c in sk]); de = np.array([c.dec.deg for c in sk]); mg = np.array([m["D"][k]["mag"][i] for k, i in pts])
        x = (ra - ra.mean()) * 3600 * np.cos(np.radians(de.mean())); y = (de - de.mean()) * 3600
        px, py = np.polyfit(t - t.mean(), x, 1), np.polyfit(t - t.mean(), y, 1)
        res = np.hypot(x - np.polyval(px, t - t.mean()), y - np.polyval(py, t - t.mean()))
        f = (t - t[0]) / (t[-1] - t[0]); pe = np.hypot(x - (x[0] + f * (x[-1] - x[0])), y - (y[0] + f * (y[-1] - y[0])))
        out.update(fit_resid=float(res.max()), mag_ptp=float(np.ptp(mg)), pred_err=float(pe.max()))
        if pe.max() >= H.LINK_TOL: out["why"] = "link_tol"
        elif res.max() > H.MAX_RESID: out["why"] = "max_resid"
        elif np.ptp(mg) > H.MAG_SPREAD: out["why"] = "mag_spread"
        else: out["why"] = "linker_other"
        return out
    bad = [p for p in per if p not in ("linkable",)]
    from collections import Counter
    c = Counter(bad); out["why"] = c.most_common(1)[0][0] if c else "unknown"
    if out["why"] == "off_image": out["why"] = "image_missing"
    return out

def evaluate_set(m, sky, link_params, s=None, diag=True):
    """Run stage 2 with link_params on cached measurements; return per-object truth rows + tracklet rows."""
    import iasc_hunt as H
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    for k, v in link_params.items(): setattr(H, k, v)
    T = np.array([x["t_mjd"] for x in m["meta"]]) * 1440.0
    uniq = H.find_tracklets(m["D"], T, verbose=False)
    tmid_mjd = np.mean([x["t_mjd"] for x in m["meta"]])
    H.identify(uniq, m["D"], T, tmid_mjd, sky["rows"])
    truth = truth_for_set(m, sky)
    trows = []
    for tr in uniq:
        trows.append(dict(set=s["id"] if s else "", n=tr["n"], rate=tr["rate"], mag=tr["mag"], resid=tr["resid"], known=tr["known"],
                          known_sep=tr["known_sep"]))
    rec = {tr["known"]: tr for tr in uniq if tr["known"]}
    orows = []
    for o in truth:
        lim5 = float(np.nanmedian([i.get("lim5_emp", np.nan) for i in m["info"]]))
        tr = rec.get(o["name"]); row = dict(set=s["id"] if s else "", filter=s["filter"] if s else "", lim5=lim5, name=o["name"], num=o["num"], cls=o["cls"], V=o["V"], rate=o["rate"],
                                            n_on=sum(o["on"]), pos_err=o["err_arcsec"], recovered=tr is not None)
        if tr is not None:
            oc, al, ct = [], [], []
            vx, vy = o["dra_arcsec_h"], o["ddec_arcsec_h"]; vn = np.hypot(vx, vy) or 1.0
            for k, i in tr["members"].items():
                c = m["D"][k]["sky"][i]; ra, dec = o["pos"][k][0], o["pos"][k][1]
                oc.append(float(c.separation(SkyCoord(ra * u.deg, dec * u.deg)).arcsec))
                de = (c.ra.deg - ra) * 3600 * np.cos(np.radians(dec)); dn = (c.dec.deg - dec) * 3600
                al.append((de * vx + dn * vy) / vn); ct.append((-de * vy + dn * vx) / vn)
            meas = [[m["meta"][k]["t_mjd"], float(m["D"][k]["sky"][i].ra.deg), float(m["D"][k]["sky"][i].dec.deg), o["pos"][k][0], o["pos"][k][1]]
                    for k, i in sorted(tr["members"].items())]
            row.update(meas=json.dumps(meas))
            row.update(oc_med=float(np.median(oc)), oc_max=float(np.max(oc)), oc_along=float(np.median(al)), oc_cross=float(np.median(ct)),
                       dt_s=float(np.median(al) / (vn / 3600)), n_det=tr["n"], mag_meas=tr["mag"])
        elif diag:
            row.update(diagnose(m, o, H))
        orows.append(row)
    n_unknown = sum(1 for tr in uniq if not tr["known"])
    return orows, trows, n_unknown

def load_cached(root, s, det_params):
    cd = os.path.join(root, "cache", s["id"])
    p = os.path.join(cd, f"m_{pkey(det_params)}.pkl")
    sk = os.path.join(cd, "skybot.json")
    if not (os.path.exists(p) and os.path.exists(sk)): return None, None
    return pickle.load(open(p, "rb")), json.load(open(sk))

def split(sets):
    """Deterministic train/test split: sets sorted by md5(id), first half train, second half test."""
    h = sorted(sets, key=lambda s: hashlib.md5(s["id"].encode()).hexdigest()); k = len(h) // 2
    ids_tr = {s["id"] for s in h[:k]}
    return [s for s in sets if s["id"] in ids_tr], [s for s in sets if s["id"] not in ids_tr]

DEFAULT_DET = dict(NSIG=2.5, GAP_DILATE=8, MINAREA=5, NOISY_FACTOR=None)
DEFAULT_LINK = dict(MIN_RATE=0.03, MATCH_ARCSEC=1.0, LINK_TOL=1.2, MAX_RESID=0.6, MAG_SPREAD=1.2, MIN_SNR=4.0, STAT_MIN=2)

def det_key(det):
    """Cache key: only the parameters that differ from the defaults ({} = original pipeline defaults)."""
    return {k: v for k, v in det.items() if DEFAULT_DET.get(k) != v}

def score(root, sets, det_params, link_params, diag=True, measure_missing=False):
    import iasc_hunt as H
    for k, v in DEFAULT_DET.items(): setattr(H, k, v)
    for k, v in det_params.items(): setattr(H, k, v)
    O, Tr, nu, nsets = [], [], [], 0
    for s in sets:
        m, sky = load_cached(root, s, det_key(det_params))
        if m is None and measure_missing:
            try: measure_set(root, s, det_key(det_params)); m, sky = load_cached(root, s, det_key(det_params))
            except Exception as e: print("measure failed", s["id"], e)
        if m is None: continue
        o, t, n_unk = evaluate_set(m, sky, dict(DEFAULT_LINK, **link_params), s, diag); O += o; Tr += t; nu.append(n_unk); nsets += 1
    return O, Tr, nu, nsets

def summarize(O, nu, vlim=21.5):
    b = [o for o in O if o["V"] < vlim]
    return dict(n_sets=len(nu), n_truth=len(b), n_rec=sum(o["recovered"] for o in b), frac=(sum(o["recovered"] for o in b) / len(b)) if b else np.nan,
                n_truth_all=len(O), n_rec_all=sum(o["recovered"] for o in O),
                fp_per_set=float(np.mean(nu)) if nu else np.nan, fp_total=int(np.sum(nu)) if nu else 0)

GRID = dict(NOISY_FACTOR=[None, 1.5], NSIG=[2.0, 2.5, 3.0], GAP_DILATE=[3, 8], MIN_RATE=[0.03, 0.06, 0.1, 0.15], MATCH_ARCSEC=[0.5, 0.7, 1.0, 1.3], LINK_TOL=[0.8, 1.2, 1.6, 2.0, 2.5],
            MAX_RESID=[0.4, 0.6, 0.8, 1.0], MAG_SPREAD=[0.8, 1.2, 1.6, 2.0], MIN_SNR=[3.0, 4.0, 5.0], STAT_MIN=[1, 2])

def cmd_tune(a):
    """Coordinate descent on TRAIN sets: maximise recovered known objects (all V) subject to false (unidentified) tracklets per set
    <= the default configuration's; ties -> fewer false tracklets. Every evaluation is logged to <out>/tune_log.csv."""
    sets = json.load(open(os.path.join(a.root, "sets.json"))); train, test = split(sets)
    cur = dict(DEFAULT_DET, **DEFAULT_LINK); cur.update(json.loads(a.start) if a.start else {}); log = []; memo = {}
    def ev(cfg):
        key = json.dumps(cfg, sort_keys=True)
        if key in memo: return memo[key]
        det = {k: cfg[k] for k in DEFAULT_DET}; link = {k: cfg[k] for k in DEFAULT_LINK}
        O, Tr, nu, ns = score(a.root, train, det, link, diag=False, measure_missing=True)
        r = summarize(O, nu); memo[key] = r; log.append(dict(cfg, **r)); print(json.dumps(dict(cfg, **r)), flush=True)
        write_csv(os.path.join(a.out, "tune_log.csv"), log); return r
    os.makedirs(a.out, exist_ok=True)
    base = ev(cur); fp_cap = base["fp_per_set"] + 1e-9
    def better(r, b):
        if r["fp_per_set"] > fp_cap: return False
        return (r["n_rec_all"], -r["fp_total"]) > (b["n_rec_all"], -b["fp_total"])
    best = base
    for rnd in range(a.rounds):
        changed = False
        for p in a.order.split(","):
            for v in GRID[p]:
                if v == cur[p]: continue
                c = dict(cur, **{p: v}); r = ev(c)
                if better(r, best): best, cur, changed = r, c, True
        if not changed: break
    json.dump(dict(best_cfg=cur, best_train=best, default_train=base, fp_cap=fp_cap), open(os.path.join(a.out, "tune_best.json"), "w"), indent=1)
    print("BEST", json.dumps(cur), json.dumps(best))

def cmd_evaluate(a):
    sets = json.load(open(os.path.join(a.root, "sets.json")))
    det = dict(DEFAULT_DET, **(json.loads(a.det) if a.det else {})); link = dict(DEFAULT_LINK, **(json.loads(a.link) if a.link else {}))
    tr, te = split(sets); use = {"train": tr, "test": te, "all": sets}[a.which]
    O, Tr, nu, ns = score(a.root, use, det, link, measure_missing=a.measure)
    print(json.dumps(dict(det=det, link=link, which=a.which, **summarize(O, nu)), default=float))
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        write_csv(os.path.join(a.out, "objects.csv"), O); write_csv(os.path.join(a.out, "tracklets.csv"), Tr)

def cmd_horizons(a):
    """Spot-check: measured positions and SkyBoT predictions of recovered objects against JPL Horizons (location F51)."""
    from astroquery.jplhorizons import Horizons
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    rows = [r for r in csv.DictReader(open(a.objects)) if r["recovered"] == "True" and r["num"] not in ("-", "")]
    rows = sorted(rows, key=lambda r: float(r["V"]))
    random.Random(0).shuffle(rows); rows = rows[:a.n]; out = []
    for r in rows:
        meas = json.loads(r["meas"]); jd = [x[0] + 2400000.5 for x in meas]
        try:
            eph = Horizons(id=r["num"], id_type="smallbody", location="F51", epochs=jd).ephemerides(extra_precision=True)
        except Exception as e: print("horizons fail", r["name"], e); continue
        for x, e in zip(meas, eph):
            h = SkyCoord(float(e["RA"]) * u.deg, float(e["DEC"]) * u.deg)
            oc = h.separation(SkyCoord(x[1] * u.deg, x[2] * u.deg)).arcsec; sk = h.separation(SkyCoord(x[3] * u.deg, x[4] * u.deg)).arcsec
            out.append(dict(set=r["set"], name=r["name"], num=r["num"], V=r["V"], t_mjd=x[0], oc_horizons=oc, skybot_minus_horizons=sk,
                            sigma_ra_3=float(e["RA_3sigma"]), sigma_dec_3=float(e["DEC_3sigma"])))
        print(r["name"], [f"{o['oc_horizons']:.3f}" for o in out if o["name"] == r["name"]], flush=True)
        time.sleep(1)
    write_csv(a.out, out)
    print("median O-C vs Horizons:", np.median([o["oc_horizons"] for o in out]), " median |SkyBoT-Horizons|:", np.median([o["skybot_minus_horizons"] for o in out]))

def binned(O, key, edges):
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        b = [o for o in O if lo <= o[key] < hi]; k = sum(o["recovered"] for o in b); n = len(b)
        # Wilson 68% interval
        if n:
            z = 1.0; p = k / n; c = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
        out.append(dict(lo=lo, hi=hi, n=n, rec=k, frac=k / n if n else np.nan, lo68=c - h if n else np.nan, hi68=c + h if n else np.nan))
    return out

def cmd_report(a):
    """Score default and tuned configurations on TRAIN and held-out TEST sets; write CSVs + PNG into --out (small files, committed)."""
    from collections import Counter
    sets = json.load(open(os.path.join(a.root, "sets.json"))); train, test = split(sets)
    best = json.load(open(a.best))["best_cfg"]
    cfgs = {"default": dict(DEFAULT_DET, **DEFAULT_LINK), "tuned": best}
    os.makedirs(a.out, exist_ok=True); summ = {}; per = {}
    for cname, cfg in cfgs.items():
        det = {k: cfg[k] for k in DEFAULT_DET}; link = {k: cfg[k] for k in DEFAULT_LINK}
        for wname, ws in (("train", train), ("test", test)):
            O, Tr, nu, ns = score(a.root, ws, det, link, diag=True, measure_missing=True)
            for o in O: o["config"] = cname; o["split"] = wname
            per[(cname, wname)] = O
            rec = [o for o in O if o["recovered"]]
            miss = [o for o in O if not o["recovered"] and o["V"] < 21]
            summ[f"{cname}_{wname}"] = dict(cfg=cfg, **summarize(O, nu), frac_V_lt_21=summarize(O, nu, 21.0)["frac"],
                                            median_oc_skybot=float(np.median([o["oc_med"] for o in rec])) if rec else np.nan,
                                            fp_tracklets_per_set_median=float(np.median(nu)) if nu else np.nan,
                                            miss_V_lt_21=dict(Counter(o.get("why", "?") for o in miss)),
                                            by_V=binned(O, "V", list(np.arange(17.0, 23.51, 0.5))),
                                            by_rate=binned(O, "rate", [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.2, 5, 100]),
                                            by_V_minus_lim5=binned([dict(o, dl=o["V"] - o["lim5"]) for o in O], "dl", list(np.arange(-3.0, 2.01, 0.5))))
            write_csv(os.path.join(a.out, f"objects_{cname}_{wname}.csv"), [{k: v for k, v in o.items() if k != "meas"} for o in O])
            write_csv(os.path.join(a.out, f"tracklets_{cname}_{wname}.csv"), Tr)
            print(cname, wname, json.dumps({k: v for k, v in summ[f"{cname}_{wname}"].items() if not k.startswith("by_")}, default=float), flush=True)
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1, default=float)
    # per-set table (sets, filter, depth, image count) and image-quality stats for the domain-shift section
    rows = []
    for s in sets:
        m, _ = load_cached(a.root, s, {})
        if m is None: continue
        for i in m["info"]:
            rows.append(dict(set=s["id"], split="test" if s in test else "train", filter=s["filter"], n_images=len(s["images"]), beta=s["beta"],
                             **{k: i.get(k) for k in ("file", "n_det", "n_match", "rms_arcsec", "zp", "fwhm_arcsec", "bkg_rms", "ap_noise_ratio",
                                                       "lim5_naive", "lim5_emp", "dens_snr5_arcmin2")}))
    write_csv(os.path.join(a.out, "image_stats.csv"), rows)
    plot(summ, os.path.join(a.out, "recovery_vs_mag.png"))

def plot(summ, path):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    col = {"default": "#2a78d6", "tuned": "#eb6834"}; ink, ink2 = "#0b0b0b", "#52514e"
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2), facecolor="#fcfcfb")
    for ax, key, xl in ((axs[0], "by_V", "predicted V (SkyBoT), 0.5 mag bins"), (axs[1], "by_V_minus_lim5", "V minus set 5-sigma limit (R-equiv.), 0.5 mag bins")):
        ax.set_facecolor("#fcfcfb")
        for j, c in enumerate(("default", "tuned")):
            b = [x for x in summ[f"{c}_test"][key] if x["n"] > 0]
            x = np.array([(x_["lo"] + x_["hi"]) / 2 for x_ in b]) + (j - 0.5) * 0.08
            y = np.array([x_["frac"] for x_ in b]); lo = y - np.array([x_["lo68"] for x_ in b]); hi = np.array([x_["hi68"] for x_ in b]) - y
            ax.errorbar(x, y, yerr=[lo, hi], color=col[c], lw=2, marker="o", ms=6, capsize=0, elinewidth=1.2,
                        label=f"{c} (held-out sets)", markeredgecolor="#fcfcfb", markeredgewidth=1.5)
            if c == "tuned":
                for xx, x_ in zip(x, b): ax.annotate(str(x_["n"]), (xx, 1.04), ha="center", fontsize=7, color=ink2)
        ax.set_ylim(-0.03, 1.09); ax.set_xlabel(xl, color=ink2); ax.grid(axis="y", color="#e4e3df", lw=0.8)
        for sp in ("top", "right"): ax.spines[sp].set_visible(False)
        for sp in ("left", "bottom"): ax.spines[sp].set_color("#b5b4ad")
        ax.tick_params(colors=ink2)
    axs[0].set_ylabel("fraction of known objects recovered", color=ink2)
    axs[0].legend(frameon=False, loc="lower left", fontsize=8); axs[0].set_title("Recovery vs magnitude (numbers = objects per bin)", fontsize=10, color=ink, loc="left")
    axs[1].set_title("Recovery vs depth-normalised magnitude", fontsize=10, color=ink, loc="left")
    plt.tight_layout(); plt.savefig(path, dpi=110, facecolor="#fcfcfb"); plt.close()

def write_csv(path, rows):
    keys = []
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, keys); w.writeheader(); [w.writerow(r) for r in rows]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("select"); p.add_argument("--root", required=True); p.add_argument("--npoints", type=int, default=150)
    p.add_argument("--nsets", type=int, default=60); p.add_argument("--seed", type=int, default=1)
    p = sp.add_parser("fetch"); p.add_argument("--root", required=True)
    p = sp.add_parser("measure"); p.add_argument("--root", required=True); p.add_argument("--det", default=""); p.add_argument("--only", default="")
    p = sp.add_parser("evaluate"); p.add_argument("--root", required=True); p.add_argument("--det", default=""); p.add_argument("--link", default="")
    p.add_argument("--which", default="all", choices=["train", "test", "all"]); p.add_argument("--out", default=""); p.add_argument("--measure", action="store_true")
    p = sp.add_parser("tune"); p.add_argument("--root", required=True); p.add_argument("--out", required=True); p.add_argument("--rounds", type=int, default=2); p.add_argument("--start", default="")
    p.add_argument("--order", default="MIN_RATE,MATCH_ARCSEC,LINK_TOL,MAX_RESID,MAG_SPREAD,MIN_SNR,STAT_MIN,NSIG,GAP_DILATE")
    p = sp.add_parser("report"); p.add_argument("--root", required=True); p.add_argument("--best", required=True); p.add_argument("--out", required=True)
    p = sp.add_parser("horizons"); p.add_argument("--objects", required=True); p.add_argument("--out", required=True); p.add_argument("--n", type=int, default=12)
    a = ap.parse_args()
    dict(select=cmd_select, fetch=cmd_fetch, measure=cmd_measure, evaluate=cmd_evaluate, tune=cmd_tune, report=cmd_report, horizons=cmd_horizons)[a.cmd](a)

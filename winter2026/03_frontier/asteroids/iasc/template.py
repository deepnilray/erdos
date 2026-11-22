"""
Static-sky template from the PS1 DR2 3pi deep stacks (g, r, i), for removing stars from IASC / PS1 frames.

build(w_ref, shape, cachedir) -> dict(g=, r=, i=) arrays on the reference pixel grid (NaN where no stack coverage).
model_for(frame, mask, T) -> best static model of one frame: frame ~ a*g + b*r + c*i, after Gaussian PSF matching
                              of whichever image is sharper, fitted on star pixels. Returns (model, info).

The stacks are 860-2040 s deep against 45 s IASC frames, so the template adds almost no noise.
"""
import os, numpy as np, requests
from scipy import ndimage
from astropy.io import fits
import iasc_hunt as H

PS1 = "https://ps1images.stsci.edu"
FILTERS = ("g", "r", "i")

def _stack_files(ra, dec):
    r = requests.get(f"{PS1}/cgi-bin/ps1filenames.py", params=dict(ra=ra, dec=dec, filters="".join(FILTERS), type="stack"), timeout=120)
    rows = [l.split() for l in r.text.strip().splitlines()[1:]]
    return {(row[4], row[7]) for row in rows if len(row) >= 8}

def build(w_ref, shape, cachedir, size_px=None):
    """Reproject every PS1 stack skycell touching the frame onto the reference grid; average where cells overlap."""
    os.makedirs(cachedir, exist_ok=True)
    ny, nx = shape
    pts = [(nx / 2, ny / 2), (0, 0), (nx, 0), (0, ny), (nx, ny), (nx / 2, 0), (nx / 2, ny), (0, ny / 2), (nx, ny / 2)]
    files = set()
    for x, y in pts:
        c = w_ref.pixel_to_world(x, y); files |= _stack_files(c.ra.deg, c.dec.deg)
    cen = w_ref.pixel_to_world(nx / 2, ny / 2)
    scale = float(np.sqrt(abs(np.linalg.det(w_ref.pixel_scale_matrix)))) * 3600
    size = size_px or int(np.hypot(nx, ny) * scale / 0.25) + 200
    out = {f: np.zeros(shape, np.float64) for f in FILTERS}; cnt = {f: np.zeros(shape, np.float64) for f in FILTERS}
    from synth import coord_map
    from astropy.time import Time
    gaia = H.gaia_stars(cen.ra.deg, cen.dec.deg, 0.75 * np.hypot(nx, ny) * scale / 3600)
    wcs_cell = {}       # one Gaia-refitted WCS per skycell (from its r stack, else any filter): all filters share the grid
    def cell_of(fn): return os.path.basename(fn).split(".stk.")[0]
    def refit(path, h, d):
        im = dict(hdr=h, data=d, t=Time(2012.0, format="jyear"), style="warp", file=os.path.basename(path))
        det = H.detect(im); w, q = H.refine_wcs(im, det, gaia)
        return w, q
    for f, fn in sorted(files, key=lambda z: (z[0] != "r", z[1])):
        path = os.path.join(cachedir, os.path.basename(fn).replace(".fits", f"_{cen.ra.deg:.4f}_{cen.dec.deg:.4f}.fits"))
        if not os.path.exists(path):
            r = requests.get(f"{PS1}/cgi-bin/fitscut.cgi", params=dict(red=fn, ra=cen.ra.deg, dec=cen.dec.deg, size=size, format="fits"), timeout=600)
            if not r.content.startswith(b"SIMPLE"): continue
            open(path + ".part", "wb").write(r.content); os.replace(path + ".part", path)
        h = fits.getheader(path); d = fits.getdata(path).astype(np.float64)
        good = np.isfinite(d)
        if cell_of(fn) not in wcs_cell:
            try: wcs_cell[cell_of(fn)] = refit(path, h, np.where(good, d, np.nan))
            except Exception: wcs_cell[cell_of(fn)] = (H.clean_wcs(h, style="warp"), dict(rms_arcsec=np.nan))
        ws = wcs_cell[cell_of(fn)][0]
        if good.sum() < 1000: continue
        import sep
        dd = np.ascontiguousarray(np.where(good, d, 0.0)); bk = sep.Background(dd, mask=~good, bw=128, bh=128)
        d = np.where(good, dd - bk.back(), np.nan)
        ys, xs = coord_map(w_ref, ws, shape)
        v = ndimage.map_coordinates(np.where(good, d, 0.0), [ys, xs], order=1, cval=0.0)
        g = ndimage.map_coordinates(good.astype(np.float32), [ys, xs], order=0, cval=0.0) > 0.5
        out[f][g] += v[g]; cnt[f][g] += 1
    T = {}
    for f in FILTERS:
        with np.errstate(invalid="ignore", divide="ignore"):
            T[f] = np.where(cnt[f] > 0, out[f] / np.maximum(cnt[f], 1), np.nan)
    return T

def model_for(frame, mask, T, sat=None):
    """Least-squares static model of a background-subtracted frame on the reference grid."""
    have = [f for f in FILTERS if f in T and np.isfinite(T[f]).mean() > 0.2]
    if not have: return None, dict(ok=False)
    cov = np.all([np.isfinite(T[f]) for f in have], axis=0) & ~mask
    if cov.mean() < 0.2: return None, dict(ok=False)
    Tz = {f: np.where(np.isfinite(T[f]), T[f], 0.0) for f in have}
    s_f = 1.4826 * np.median(np.abs(frame[cov]))
    ref = sum(Tz[f] for f in have)
    s_t = 1.4826 * np.median(np.abs(ref[cov]))
    stars = cov & (ref > 20 * s_t)
    if sat is not None: stars &= frame < sat
    stars &= ndimage.binary_erosion(cov, iterations=8)
    if stars.sum() < 200: return None, dict(ok=False, n_star_px=int(stars.sum()))
    best = None
    for st in (0.0, 0.6, 1.0, 1.4, 1.8, 2.2):          # template blur (px)
        for sf in (0.0, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6):   # frame blur (px): only one of the two is non-zero
            if st > 0 and sf > 0: continue
            Tb = {f: ndimage.gaussian_filter(Tz[f], st) if st else Tz[f] for f in have}
            Fb = ndimage.gaussian_filter(frame, sf) if sf else frame
            X = np.column_stack([Tb[f][stars] for f in have]); y = Fb[stars]
            coef, *_ = np.linalg.lstsq(X, y, rcond=None)
            if np.any(coef < 0):            # colour fit unstable: one scale on the summed template
                X1 = X.sum(axis=1, keepdims=True); c1, *_ = np.linalg.lstsq(X1, y, rcond=None); coef = np.repeat(c1, len(have))
            res = y - X @ coef; chi = float(np.mean(res ** 2)) / float(np.mean(y ** 2))   # fraction of star flux left
            if best is None or chi < best[0]: best = (chi, st, sf, coef)
    chi, st, sf, coef = best
    model = sum(c * (ndimage.gaussian_filter(Tz[f], st) if st else Tz[f]) for c, f in zip(coef, have))
    model = np.where(cov, model, np.nan)
    return model, dict(ok=True, tmpl_blur=st, frame_blur=sf, coef=[float(c) for c in coef], filters=have,
                       star_resid_frac=float(np.sqrt(chi)), cover=float(cov.mean()))


def _basis(sigmas=(0.8, 1.6, 2.6), deg=2, half=10):
    """Alard-Lupton style kernel basis: Gaussians x monomials u^i v^j (i + j <= deg)."""
    yy, xx = np.mgrid[-half:half + 1, -half:half + 1].astype(float)
    B = []
    for s in sigmas:
        g = np.exp(-(xx ** 2 + yy ** 2) / (2 * s * s))
        for i in range(deg + 1):
            for j in range(deg + 1 - i):
                k = g * xx ** i * yy ** j
                if i == 0 and j == 0: k = k / k.sum()
                else: k = k - (k.sum() / g.sum()) * g if (i % 2 == 0 and j % 2 == 0) else k   # even terms: zero net flux
                B.append(k)
    return B

def kernel_match(frame, mask, T, sat=None):
    """Convolve the (sharper) frame with a fitted kernel K so that K * frame matches the deep template sum(g,r,i).
    Returns (K*frame, template_sum, info); difference = first - second (template units), NaN where uncovered."""
    from scipy.signal import fftconvolve
    have = [f for f in FILTERS if f in T and np.isfinite(T[f]).mean() > 0.2]
    if not have: return None, None, dict(ok=False)
    cov = np.all([np.isfinite(T[f]) for f in have], axis=0) & ~mask
    if cov.mean() < 0.2: return None, None, dict(ok=False)
    Ts = sum(np.where(np.isfinite(T[f]), T[f], 0.0) for f in have)
    F = np.where(mask, 0.0, frame)
    s_t = 1.4826 * np.median(np.abs(Ts[cov]))
    # fit region: boxes around unsaturated, isolated-ish stars bright in the template
    pk = (Ts > 30 * s_t) & (Ts == ndimage.maximum_filter(Ts, size=9)) & ndimage.binary_erosion(cov, iterations=14)
    if sat is not None: pk &= ndimage.maximum_filter(F, size=5) < 0.5 * sat
    ys, xs = np.nonzero(pk)
    if len(xs) < 15: return None, None, dict(ok=False, n_stars=int(len(xs)))
    order = np.argsort(-Ts[ys, xs]); ys, xs = ys[order][5:205], xs[order][5:205]     # skip the 5 brightest
    sel = np.zeros_like(cov)
    for y, x in zip(ys, xs): sel[y - 7:y + 8, x - 7:x + 8] = True
    sel &= cov
    B = _basis()
    conv = [fftconvolve(F, k, mode="same") for k in B]
    X = np.column_stack([c[sel] for c in conv] + [np.ones(sel.sum())]); y = Ts[sel]
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    KF = sum(c * cv for c, cv in zip(coef[:-1], conv)) + coef[-1]
    res = (KF - Ts)[sel]
    info = dict(ok=True, n_stars=int(len(xs)), star_resid_frac=float(np.sqrt(np.mean(res ** 2) / np.mean(y ** 2))),
                cover=float(cov.mean()), flux_scale=float(sum(coef[i] for i in range(len(B)) if abs(B[i].sum() - 1) < 1e-6)))
    return np.where(cov, KF, np.nan), np.where(cov, Ts, np.nan), info


def kernel_match2(frame, mask, T, sat=None, frame_sigma=2.0):
    """Colour-aware matching: blur the frame by frame_sigma so it is broader than the stack, then fit
    G*frame ~ sum_f K_f * T_f + bg, one Alard-Lupton kernel per filter (the w band ~ a linear mix of g, r, i).
    Returns (G*frame, model, info) on the reference grid; difference = first - second."""
    from scipy.signal import fftconvolve
    have = [f for f in FILTERS if f in T and np.isfinite(T[f]).mean() > 0.2]
    if not have: return None, None, dict(ok=False)
    cov = np.all([np.isfinite(T[f]) for f in have], axis=0) & ~mask
    if cov.mean() < 0.2: return None, None, dict(ok=False)
    Tz = {f: np.where(np.isfinite(T[f]), T[f], 0.0) for f in have}
    F = ndimage.gaussian_filter(np.where(mask, 0.0, frame), frame_sigma)
    Ts = sum(Tz.values()); s_t = 1.4826 * np.median(np.abs(Ts[cov]))
    pk = (Ts > 30 * s_t) & (Ts == ndimage.maximum_filter(Ts, size=9)) & ndimage.binary_erosion(cov, iterations=14)
    if sat is not None: pk &= ndimage.maximum_filter(np.where(mask, 0.0, frame), size=5) < 0.5 * sat
    ys, xs = np.nonzero(pk)
    if len(xs) < 20: return None, None, dict(ok=False, n_stars=int(len(xs)))
    order = np.argsort(-Ts[ys, xs]); ys, xs = ys[order][5:305], xs[order][5:305]
    sel = np.zeros_like(cov)
    for y, x in zip(ys, xs): sel[y - 8:y + 9, x - 8:x + 9] = True
    sel &= cov
    B = _basis(sigmas=(0.5, 1.0, 1.8), deg=2, half=9)
    conv = [(f, fftconvolve(Tz[f], k, mode="same")) for f in have for k in B]
    X = np.column_stack([c[sel] for _, c in conv] + [np.ones(sel.sum())]); y = F[sel]
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    model = sum(c * cv for c, (_, cv) in zip(coef[:-1], conv)) + coef[-1]
    res = (F - model)[sel]
    info = dict(ok=True, n_stars=int(len(xs)), star_resid_frac=float(np.sqrt(np.mean(res ** 2) / np.mean(y ** 2))), cover=float(cov.mean()))
    return np.where(cov, F, np.nan), np.where(cov, model, np.nan), info

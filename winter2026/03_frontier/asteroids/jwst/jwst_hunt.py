"""
Moving-object (asteroid) search in JWST NIRCam calibrated exposures (*_cal.fits) of one field and detector.

At NIRCam depth a main-belt asteroid moving ~30"/h trails ~30 px (LW, 0.063"/px) in a ~4-min exposure, so:
 1. align all exposures of the set onto exposure 0's pixel grid (header WCS, bilinear), masking DQ DO_NOT_USE;
 2. remove everything static with the per-pixel median of the aligned exposures (stars, galaxies);
 3. find trails in each residual with a matched line-filter bank (fast.detect_trails: lengths x angles);
 4. link trails across >= 3 exposures: motion linear in time, and trail length/angle consistent with
    rate x exposure time and the motion direction;
 5. a scrambled-time control (exposure times permuted) gives the false-link rate.

Usage: python3 -I jwst_hunt.py <dir_with_cal_files> <outdir> [--min-exp 3]
Separate from the IASC pipeline: it only imports fast.py's filter bank, read-only.
"""
import sys, os, glob, json, argparse, numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from astropy.time import Time
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy import ndimage
from scipy.spatial import cKDTree
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "iasc"))
import fast as F

RATE_MIN, RATE_MAX = 3.0, 300.0      # arcsec/hour (main belt near quadrature ~ 15-60"/h; NEOs faster)
THR = 6.0                             # trail-filter S/N per exposure
CLIP = 5.0                            # residuals clipped at +-CLIP sigma before the line filters
LEN_TOL, ANG_TOL = 0.5, 20.0
PRED_TOL = 1.0                        # arcsec
MAX_RESID = 0.6                       # arcsec

def load(d):
    ims = []
    for f in sorted(glob.glob(os.path.join(d, "**", "*_cal.fits"), recursive=True)):
        h0 = fits.getheader(f, 0); h1 = fits.getheader(f, 1)
        sci = fits.getdata(f, "SCI").astype(np.float32); dq = fits.getdata(f, "DQ")
        bad = (dq & 1).astype(bool) | ~np.isfinite(sci)
        t0 = Time(h0["EXPSTART"], format="mjd", scale="utc"); t1 = Time(h0["EXPEND"], format="mjd", scale="utc")
        ims.append(dict(file=os.path.basename(f), sci=sci, bad=bad, w=WCS(h1), tmid=t0 + (t1 - t0) / 2,
                        texp=float(h0.get("EFFEXPTM", (t1 - t0).sec)), filt=h0.get("FILTER"), pupil=h0.get("PUPIL"),
                        pixar=float(h1.get("PIXAR_SR", np.nan))))
    return sorted(ims, key=lambda z: z["tmid"].mjd)

def group_sets(ims, gap_min=60.0, min_exp=3):
    """Consecutive exposures (gaps < gap_min minutes, same filter) form one set."""
    sets, cur = [], []
    for im in ims:
        if cur and ((im["tmid"] - cur[-1]["tmid"]).to(u.min).value > gap_min or im["filt"] != cur[-1]["filt"]):
            sets.append(cur); cur = []
        cur.append(im)
    if cur: sets.append(cur)
    return [s for s in sets if len(s) >= min_exp]

B = 2      # work on 2x2-binned exposures (memory; LW 0.126"/px, still ~3 px per PSF FWHM)

def binimg(a, b=B):
    ny, nx = a.shape[0] // b * b, a.shape[1] // b * b
    return a[:ny, :nx].reshape(ny // b, b, nx // b, b).mean(axis=(1, 3))

def coord_map(w_from, w_to, shape, origin, step=32):
    """For each pixel of the binned reference grid: its position in the binned grid of the image with WCS w_to."""
    ny, nx = shape
    gy, gx = np.arange(0, ny + step, step), np.arange(0, nx + step, step)
    GX, GY = np.meshgrid(gx, gy)
    sky = w_from.pixel_to_world((GX.ravel() - origin[0]) * B + (B - 1) / 2, (GY.ravel() - origin[1]) * B + (B - 1) / 2)
    xk, yk = w_to.world_to_pixel(sky)
    xk = (np.asarray(xk).reshape(GX.shape) - (B - 1) / 2) / B; yk = (np.asarray(yk).reshape(GX.shape) - (B - 1) / 2) / B
    yy, xx = np.mgrid[0:ny, 0:nx].astype(np.float32)
    return ndimage.map_coordinates(yk, [yy / step, xx / step], order=1), ndimage.map_coordinates(xk, [yy / step, xx / step], order=1)

def to_sky(w0, x, y, origin):
    """binned reference-grid pixel -> sky"""
    return w0.pixel_to_world((np.asarray(x) - origin[0]) * B + (B - 1) / 2, (np.asarray(y) - origin[1]) * B + (B - 1) / 2)

def residuals(S):
    """Align a set on exposure 0's (binned, padded) grid, subtract the per-pixel median, normalise to unit noise."""
    w0 = S[0]["w"]; ny0, nx0 = S[0]["sci"].shape
    ext = 0
    for im in S[1:]:
        x, y = w0.world_to_pixel(im["w"].pixel_to_world(nx0 / 2, ny0 / 2)); ext = max(ext, abs(float(x) - nx0 / 2), abs(float(y) - ny0 / 2))
    pad = int(ext / B) + 8; shape = (ny0 // B + 2 * pad, nx0 // B + 2 * pad); origin = (pad, pad)
    A = np.full((len(S),) + shape, np.nan, np.float32)
    for k, im in enumerate(S):
        ys, xs = coord_map(w0, im["w"], shape, origin)
        sb = binimg(np.where(im["bad"], 0.0, im["sci"]).astype(np.float32)); mb = binimg(im["bad"].astype(np.float32)) > 0.25
        a = ndimage.map_coordinates(sb, [ys, xs], order=1, cval=np.nan)
        m = ndimage.map_coordinates(mb.astype(np.float32), [ys, xs], order=0, cval=1.0) > 0.5
        A[k] = np.where(m | ~np.isfinite(a), np.nan, a)
    M = ~np.isfinite(A)
    nvalid = (~M).sum(axis=0)
    med = np.nanmedian(A, axis=0)
    s_med = 1.4826 * np.nanmedian(np.abs(med - np.nanmedian(med)))
    core = ndimage.binary_dilation(np.nan_to_num(med) > 200 * s_med, iterations=4)
    R = []
    for k in range(len(S)):
        r = A[k] - med
        r[(nvalid < 3) | M[k] | ~np.isfinite(r)] = 0.0
        bg = ndimage.median_filter(r[::8, ::8], size=9); r = r - np.kron(bg, np.ones((8, 8)))[:r.shape[0], :r.shape[1]]
        # NIRCam 1/f striping: remove row and column medians of the residual (the grid is ~aligned with exposure 0's rows)
        good = r != 0
        for ax_ in (1, 0):
            rr = np.where(good, r, np.nan); med_line = np.nanmedian(rr, axis=ax_); med_line = np.nan_to_num(med_line)
            r = r - (med_line[:, None] if ax_ == 1 else med_line[None, :]); r[~good] = 0.0
        s = 1.4826 * np.median(np.abs(r[r != 0])); R.append((r / s).astype(np.float32))
    RM = [M[k] | (nvalid < 3) | core for k in range(len(S))]
    del A
    return R, RM, w0, origin

def detections(S, verbose=True):
    R, RM, w0, origin = residuals(S)
    n = len(S)
    pix = float(np.sqrt(abs(np.linalg.det(w0.pixel_scale_matrix)))) * 3600 * B
    texp_h = np.median([im["texp"] for im in S]) / 3600.0
    Lmin, Lmax = max(RATE_MIN * texp_h / pix, 3.0), RATE_MAX * texp_h / pix
    lengths = np.unique(np.round(np.geomspace(Lmin, Lmax, 7)))
    angles = np.arange(0, 180, 10.0)
    psf_sig = 1.0                              # binned px (NIRCam PSF FWHM ~2 native px)
    det = []
    for k in range(n):
        # winsorise: residual star cores / dipoles are single-pixel-heavy, a trail is many moderate pixels
        d = F.detect_trails(np.clip(R[k], -CLIP, CLIP), RM[k], psf_sig, lengths, angles, thr=THR, binf=1)
        d["sky"] = to_sky(w0, d["x"], d["y"], origin); det.append(d)
    if verbose: print("trail detections per exposure:", [len(d["x"]) for d in det])
    c0 = w0.pixel_to_world(S[0]["sci"].shape[1] / 2, S[0]["sci"].shape[0] / 2)
    from iasc_hunt import _tangent
    P = [_tangent(d["sky"], c0.ra.deg, c0.dec.deg) if len(d["x"]) else np.zeros((0, 2)) for d in det]
    pas = []
    for k in range(n):
        if len(det[k]["x"]) == 0: pas.append(np.zeros(0)); continue
        t = np.radians(det[k]["theta"])
        p2 = _tangent(to_sky(w0, det[k]["x"] + 5 * np.cos(t), det[k]["y"] + 5 * np.sin(t), origin), c0.ra.deg, c0.dec.deg)
        dv = p2 - P[k]; pas.append(np.degrees(np.arctan2(dv[:, 0], dv[:, 1])) % 180)
    return dict(det=det, P=P, pas=pas, pix=pix, texp_h=texp_h, R=R, RM=RM, origin=origin, w0=w0)

def link(S, DD, scramble=None):
    det, P, pas, pix, texp_h = DD["det"], DD["P"], DD["pas"], DD["pix"], DD["texp_h"]
    n = len(S); T = np.array([im["tmid"].mjd for im in S]) * 24.0     # hours
    if scramble is not None: T = T[scramble]
    trees = [cKDTree(p) if len(p) else None for p in P]
    order = np.argsort(T); tracks = []
    seeds = [(order[0], order[-1]), (order[0], order[-2]), (order[1], order[-1])]
    for i0, i1 in seeds:
        if trees[i0] is None or trees[i1] is None: continue
        dt = T[i1] - T[i0]
        if dt <= 0: continue
        for a, lst in enumerate(trees[i1].query_ball_point(P[i0], r=RATE_MAX * dt)):
            for b in lst:
                v = (P[i1][b] - P[i0][a]) / dt; rate = float(np.hypot(*v))
                if rate < RATE_MIN: continue
                pa = float(np.degrees(np.arctan2(v[0], v[1])) % 180); Lexp = rate * texp_h / pix
                ok = True
                for k, idx in ((i0, a), (i1, b)):
                    if abs(det[k]["L"][idx] - Lexp) > LEN_TOL * Lexp + 3: ok = False
                    dpa = abs(pas[k][idx] - pa) % 180; dpa = min(dpa, 180 - dpa)
                    if Lexp > 8 and dpa > ANG_TOL: ok = False
                if not ok: continue
                mem = {int(i0): a, int(i1): b}
                for k in range(n):
                    if k in mem or trees[k] is None: continue
                    d2, j = trees[k].query(P[i0][a] + v * (T[k] - T[i0]))
                    if d2 < PRED_TOL: mem[k] = int(j)
                if len(mem) < 3: continue
                ks = sorted(mem, key=lambda z: T[z]); t = np.array([T[k] for k in ks]); xy = np.array([P[k][mem[k]] for k in ks])
                px = np.polyfit(t - t.mean(), xy[:, 0], 1); py = np.polyfit(t - t.mean(), xy[:, 1], 1)
                res = np.hypot(xy[:, 0] - np.polyval(px, t - t.mean()), xy[:, 1] - np.polyval(py, t - t.mean()))
                if res.max() > MAX_RESID: continue
                sn = [float(det[k]["snr"][mem[k]]) for k in ks]
                tracks.append(dict(members={int(k): int(mem[k]) for k in ks}, n=len(ks), rate_arcsec_h=float(np.hypot(px[0], py[0])),
                                   pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), snr_med=float(np.median(sn)),
                                   pos=[(S[k]["tmid"].isot, float(det[k]["sky"][mem[k]].ra.deg), float(det[k]["sky"][mem[k]].dec.deg)) for k in ks]))
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted(tr["members"].items()))
        if any(m in seen for m in key): continue
        seen.update(key); uniq.append(tr)
    return uniq

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("out"); ap.add_argument("--min-exp", type=int, default=3)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    ims = load(a.dir); sets = group_sets(ims, min_exp=a.min_exp)
    print("exposures", len(ims), "sets", [len(s) for s in sets], flush=True)
    summary = []
    for si, S in enumerate(sets):
        DD = detections(S); tr = link(S, DD)
        rng = np.random.default_rng(si); scr = []
        for rep in range(3):
            perm = rng.permutation(len(S))
            if np.all(perm == np.arange(len(S))): perm = perm[::-1]
            scr.append(len(link(S, DD, scramble=perm)))
        print(f"set {si}: {len(S)} exp {S[0]['filt']} {S[0]['tmid'].isot}: tracklets {len(tr)}, scrambled {scr}")
        summary.append(dict(set=si, n_exp=len(S), filt=S[0]["filt"], t0=S[0]["tmid"].isot, files=[im["file"] for im in S],
                            tracklets=tr, scrambled_counts=scr))
    json.dump(summary, open(os.path.join(a.out, "tracklets.json"), "w"), indent=1)

if __name__ == "__main__":
    main()

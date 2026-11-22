"""
Fast-mover (trailed) search for 3-4 image sets: the NEO regime, > ~1.25"/min.

A fast mover smears into a trail during the exposure (rate x EXPTIME), so its peak S/N drops and a point-source
detector loses it. Here each image is filtered with a bank of line kernels (PSF-wide segments of several lengths and
angles); a detection carries its trail length and angle. Linking then requires the motion between images to agree
with the trail itself (length = rate x exposure, direction = position angle): a strong constraint that keeps chance
alignments rare.

detect_trails(im_sub, mask, psf_sigma_px, lengths_px, angles_deg, thr) -> detections (x, y, L, theta, snr)
find_fast(D, ims, T_min, scale_arcsec) -> tracklets in the same dict form as iasc_hunt.find_tracklets
"""
import numpy as np
from scipy import ndimage
from scipy.signal import fftconvolve
from scipy.spatial import cKDTree

THR = 5.5                  # trail-filter S/N threshold per image (each filter output normalised by its own MAD)
SNR_RATIO = 0.4            # weakest image's S/N >= this x median (constant brightness)
MIN_RATE_FAST = 1.0        # "/min (below this the point-source linker and synth cover it)
MAX_RATE_FAST = 15.0
LEN_TOL = 0.45             # fractional agreement of trail length with rate x exposure
ANG_TOL = 20.0             # deg agreement of trail angle with motion direction (mod 180)
PRED_TOL = 2.0             # arcsec: predicted vs detected position in the other images
MAX_RESID = 1.0            # arcsec, linear fit

def line_kernel(L, theta_deg, sigma):
    half = int(np.ceil(L / 2 + 3 * sigma)) + 1
    yy, xx = np.mgrid[-half:half + 1, -half:half + 1].astype(float)
    t = np.radians(theta_deg); ux, uy = np.cos(t), np.sin(t)
    along = xx * ux + yy * uy; perp = -xx * uy + yy * ux
    a = np.clip(np.abs(along) - L / 2, 0, None)
    k = np.exp(-(perp ** 2 + a ** 2) / (2 * sigma * sigma))
    return k / np.sqrt((k ** 2).sum())        # unit-norm: filtered/noise = matched-filter S/N for white noise

def detect_trails(sub, mask, psf_sigma, lengths, angles, thr=THR, binf=2):
    """Matched line-filter bank on a 2x-binned image. Returns arrays x, y (unbinned px), L (px), theta (deg), snr."""
    img = np.where(mask, 0.0, sub)
    ny, nx = img.shape; ny2, nx2 = ny // binf * binf, nx // binf * binf
    b = img[:ny2, :nx2].reshape(ny2 // binf, binf, nx2 // binf, binf).sum(axis=(1, 3))
    mb = mask[:ny2, :nx2].reshape(ny2 // binf, binf, nx2 // binf, binf).any(axis=(1, 3))
    noise = 1.4826 * np.median(np.abs(b[~mb] - np.median(b[~mb])))
    best = np.full(b.shape, -np.inf, np.float32); bL = np.zeros(b.shape, np.float32); bT = np.zeros(b.shape, np.float32)
    s = max(psf_sigma / binf, 0.7)
    for L in lengths:
        for th in angles:
            k = line_kernel(L / binf, th, s)
            f = fftconvolve(b, k, mode="same"); fv = f[~mb]
            f = f / (1.4826 * np.median(np.abs(fv - np.median(fv))))
            upd = f > best; best[upd] = f[upd]; bL[upd] = L; bT[upd] = th
    best[ndimage.binary_dilation(mb, iterations=4)] = -np.inf
    loc = (best == ndimage.maximum_filter(best, size=7)) & (best > thr)
    yy, xx = np.nonzero(loc)
    return dict(x=(xx + 0.5) * binf - 0.5, y=(yy + 0.5) * binf - 0.5, L=bL[yy, xx], theta=bT[yy, xx], snr=best[yy, xx])

def find_fast(P, texp_min, verbose=True):
    """P: synth.prepare() output. Trail detection runs on its static-subtracted residuals (median of the aligned
    images removed, stars / gaps / clutter masked), all on image 0's pixel grid, so stars cannot fake trails."""
    from iasc_hunt import _tangent
    R, RM, T, w0 = P["R"], P["Rmask"], P["T"], P["w0"]
    n = len(R); scale = P["scale"] / 2.0 if False else float(np.sqrt(abs(np.linalg.det(w0.pixel_scale_matrix)))) * 3600
    clut = np.kron(P["masked"], np.ones((2, 2), bool))[:R[0].shape[0], :R[0].shape[1]]
    if clut.shape != R[0].shape:
        c2 = np.zeros(R[0].shape, bool); c2[:clut.shape[0], :clut.shape[1]] = clut; clut = c2
    Lmin = max(MIN_RATE_FAST * texp_min / scale, 3.0); Lmax = MAX_RATE_FAST * texp_min / scale
    lengths = np.unique(np.round(np.geomspace(Lmin, Lmax, 6)))
    angles = np.arange(0, 180, 12.0)
    det = []
    for k in range(n):
        dt = detect_trails(R[k], RM[k] | clut, P["psf_sigma_px"], lengths, angles)
        dt["sky"] = w0.pixel_to_world(dt["x"], dt["y"]); det.append(dt)
    if verbose: print("fast: trail detections per image", [len(d["x"]) for d in det])
    ra0, de0 = P["cen"].ra.deg, P["cen"].dec.deg
    Pp = [_tangent(d["sky"], ra0, de0) if len(d["x"]) else np.zeros((0, 2)) for d in det]
    pas = []
    for k in range(n):
        if len(det[k]["x"]) == 0: pas.append(np.zeros(0)); continue
        t = np.radians(det[k]["theta"]); p2 = _tangent(w0.pixel_to_world(det[k]["x"] + 5 * np.cos(t), det[k]["y"] + 5 * np.sin(t)), ra0, de0)
        dv = p2 - Pp[k]; pas.append(np.degrees(np.arctan2(dv[:, 0], dv[:, 1])) % 180)
    tracks = []
    for i0, i1 in [(0, n - 1), (0, n - 2), (1, n - 1)]:
        if i1 <= i0 or len(Pp[i0]) == 0 or len(Pp[i1]) == 0: continue
        dtm = T[i1] - T[i0]
        pairs = cKDTree(Pp[i1]).query_ball_point(Pp[i0], r=MAX_RATE_FAST * dtm)
        for a, lst in enumerate(pairs):
            for b in lst:
                v = (Pp[i1][b] - Pp[i0][a]) / dtm; rate = float(np.hypot(*v))
                if rate < MIN_RATE_FAST: continue
                pa = float(np.degrees(np.arctan2(v[0], v[1])) % 180); Lexp = rate * texp_min / scale
                ok = True
                for k, idx in ((i0, a), (i1, b)):
                    if abs(det[k]["L"][idx] - Lexp) > LEN_TOL * Lexp + 2: ok = False
                    dpa = abs(pas[k][idx] - pa) % 180; dpa = min(dpa, 180 - dpa)
                    if dpa > ANG_TOL and Lexp > 6: ok = False
                if not ok: continue
                members = {i0: a, i1: b}
                for k in range(n):
                    if k in members or len(Pp[k]) == 0: continue
                    d2, j = cKDTree(Pp[k]).query(Pp[i0][a] + v * (T[k] - T[i0]))
                    if d2 < PRED_TOL: members[k] = j
                if len(members) < 3: continue
                ks = sorted(members); t = np.array([T[k] for k in ks]); xy = np.array([Pp[k][members[k]] for k in ks])
                sn = np.array([det[k]["snr"][members[k]] for k in ks])
                if sn.min() < SNR_RATIO * np.median(sn): continue
                px = np.polyfit(t - t.mean(), xy[:, 0], 1); py = np.polyfit(t - t.mean(), xy[:, 1], 1)
                res = np.hypot(xy[:, 0] - np.polyval(px, t - t.mean()), xy[:, 1] - np.polyval(py, t - t.mean()))
                if res.max() > MAX_RESID: continue
                tracks.append(dict(members={int(k): int(members[k]) for k in ks}, n=len(ks), rate=float(np.hypot(px[0], py[0])),
                                   pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), snr=float(np.median(sn)),
                                   sky=[det[k]["sky"][members[k]] for k in ks], images=ks))
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted(tr["members"].items()))
        if any(m in seen for m in key): continue
        seen.update(key); uniq.append(tr)
    return uniq, det

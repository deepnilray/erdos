"""
Synthetic tracking (shift-and-stack) for 3-4 image PS1 sets: finds movers too faint to detect in single images.

Why: iasc_hunt.py detects in each image and links (like Astrometrica blinking or PS1's own MOPS). Anything it can find,
MOPS has usually already reported. Stacking the images along each trial motion adds the signal coherently, so the
search goes deeper than any single image (~0.75 mag for 4 images in the ideal case, less after the trials penalty).

Steps
 1. iasc_hunt.measure(): per-image background subtraction and Gaia WCS refit.
 2. Resample every image onto image 0's pixel grid (WCS-to-WCS map, bilinear).
 3. Remove everything static: subtract the per-pixel median of the aligned images, mask gaps / noisy cells / bright stars.
 4. Matched filter (Gaussian PSF), normalise each image to unit noise, decimate x2.
 5. For every trial velocity (grid fine enough that the worst position error is <= 1 binned px), sum the shifted images.
    Keep the per-pixel maximum (score) and the velocity that gave it.
 6. Candidates = local maxima above SCORE_MIN. Each must also show positive signal in >= n-1 individual images,
    with no single image carrying more than MAX_FRAC of the total (rejects one-image artefacts).
 7. Control: the same search with the image order scrambled. Real movers cannot stack then, so the scrambled count
    measures the false-alarm rate at the same threshold.

Usage: python3 -I synth.py <set_folder> <out_json> [--truth skybot] [--scramble]
"""
import sys, os, json, argparse, time, numpy as np
from scipy import ndimage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iasc_hunt as H
import astropy.units as u
from astropy.coordinates import SkyCoord

RATE_MIN, RATE_MAX = 0.1, 1.25       # arcsec/min searched
BIN = 2
REPORT_MIN = 10.0                     # candidates listed for human review (bench: ~2 noise hits per set at this level)
SCORE_MIN = 5.0                       # robust stack S/N threshold (sum of all but the brightest image / sqrt(n-1))
MAX_FRAC = 0.45                       # max fraction of the stacked signal from one image
MIN_RATIO = 0.4                       # every image's signal >= this x the median image signal (constant-brightness test)
CLUTTER_BOX, CLUTTER_NEG = 41, 30     # binned px box; > CLUTTER_NEG pixels below -4 sigma (all images) = artefact region
CLUTTER_OVERRIDE = 30.0               # a peak this strong is kept even inside a clutter region: a bright SLOW mover overlaps
                                      # itself between images, biases the median and leaves negatives, so it flags its own region
                                      # (injection test on the IASC practice chip, 2026-11-22)
                                      # (star halos, ghosts, galaxies leave negative AND positive residuals; a mover leaves ~none negative)
STAR_MASK_SNR = 30                    # mask cores of bright static sources (residuals there are not Gaussian)
PSF_FWHM = 1.3                        # arcsec, matched-filter FWHM (PS1); None = median header SEEING x PIXSCALE (ZTF)
# Many-image sets (ZTF, n > 4). The 3-4 image rules above do not scale:
#  - score: sum minus the brightest image costs a second pass per velocity; with n >= 6 a per-image clip at ZCLIP does the same job
#    (one image can add at most ZCLIP/sqrt(n) to the score) in one pass.
#  - "every image >= 2 sigma" and ">= 0.4 x median": at stack S/N 10 over 12 images the per-image S/N is ~3, so about 15 % of images
#    of a REAL mover fall below 2 by chance; replaced by: >= POS_FRAC of the unmasked images positive, both time halves
#    significant on their own (>= HALF_MIN), and no image above MAX_FRAC_MANY of the total.
#  - time origin at the mean time, so the velocity grid's worst position error is half the PS1 value.
#  - scrambled control: a random permutation with ~zero correlation to the true order (reversing the order, as for n = 3,
#    is just v -> -v when the spacing is even, so real movers still stack).
ZTF_SYNTH = dict(BIN=1, PSF_FWHM=None)
ZCLIP, POS_FRAC, HALF_MIN, MAX_FRAC_MANY = 5.0, 0.75, 3.0, 0.3
#  - the clipped stack saturates at ZCLIP*sqrt(n) for bright movers (flat plateaus -> many tied local maxima), so each candidate's
#    reported score is the unclipped robust score (sum minus max over sqrt(n-1), as for PS1) at its velocity, and candidates
#    within NMS_PX of a higher-scoring one are dropped; a known object absorbs every candidate within MATCH_R_MANY arcsec.
NMS_PX, MATCH_R_MANY = 10, 6.0
#  - constant brightness over time: the mean signal of each time third must be >= THIRD_FRAC x the overall mean (rejects partial
#    alignments, e.g. a mover faster than RATE_MAX, or a different velocity, that lines up in only part of the set)
THIRD_FRAC = 0.35
#  - and the per-image scatter must look like noise plus seeing changes: std <= max(STD_ABS, STD_REL x mean)
STD_ABS, STD_REL = 1.8, 0.65

def many(n): return n > 4

def coord_map(w_from, w_to, shape, step=64):
    """Pixel coords in image k (w_to) of every pixel of the reference grid (w_from)."""
    ny, nx = shape
    gy, gx = np.arange(0, ny + step, step), np.arange(0, nx + step, step)
    GX, GY = np.meshgrid(gx, gy)
    xk, yk = w_to.world_to_pixel(w_from.pixel_to_world(GX.ravel(), GY.ravel()))
    xk, yk = np.asarray(xk).reshape(GX.shape), np.asarray(yk).reshape(GX.shape)
    yy, xx = np.mgrid[0:ny, 0:nx].astype(np.float32)
    fy, fx = yy / step, xx / step
    return ndimage.map_coordinates(yk, [fy, fx], order=1), ndimage.map_coordinates(xk, [fy, fx], order=1)

def prepare(folder):
    ims, D, info, cen, rad = H.measure(folder, verbose=False)
    n = len(ims); shape = ims[0]["data"].shape; w0 = D[0]["w"]
    if ims[0]["style"] == "ztf": globals().update(ZTF_SYNTH)
    A, M = [], []
    for k in range(n):
        d = ims[k]["data"]; mk = H.gap_mask(d, ims[k]["style"], ims[k].get("mask")) | ~np.isfinite(D[k]["sub"])
        sub = np.where(mk, 0.0, D[k]["sub"]).astype(np.float32)
        if k == 0: a, m = sub, mk
        else:
            yk, xk = coord_map(w0, D[k]["w"], shape)
            a = ndimage.map_coordinates(sub, [yk, xk], order=1, cval=0.0).astype(np.float32)
            m = ndimage.map_coordinates(mk.astype(np.float32), [yk, xk], order=0, cval=1.0) > 0.5
        A.append(a); M.append(m)
    A = np.array(A); M = np.array(M)
    stack = np.where(M, np.nan, A)
    med = np.nanmedian(stack, axis=0); med = np.where(np.isfinite(med), med, 0)
    bad = M.any(axis=0) if n <= 3 else (M.sum(axis=0) >= 2)
    # bright static sources: residuals near their cores are dominated by PSF/seeing changes, not noise
    rms0 = 1.4826 * np.nanmedian(np.abs(med - np.nanmedian(med)))
    lo = np.nanmin(stack, axis=0); lo = np.where(np.isfinite(lo), lo, 0)     # static = bright in EVERY image (a mover is not)
    star = ndimage.binary_dilation(lo > STAR_MASK_SNR * rms0, iterations=6)
    Z = []
    pix = H.pixel_scale_deg(ims[0]["hdr"], ims[0]["style"]) * 3600
    fwhm = PSF_FWHM if PSF_FWHM else float(np.median([im["hdr"].get("SEEING", 2.0) * im["hdr"].get("PIXSCALE", pix) for im in ims]))
    psf_sig = fwhm / 2.355 / pix    # PS1: ~1.3" FWHM in px
    for k in range(n):
        r = A[k] - med; r[M[k] | bad | star] = 0
        s = 1.4826 * np.median(np.abs(r[r != 0])); r /= s
        f = ndimage.gaussian_filter(r, psf_sig)
        f /= 1.4826 * np.median(np.abs(f[r != 0]))
        f[M[k] | bad | star] = 0
        Z.append(f[::BIN, ::BIN].astype(np.float32))
    Z = np.array(Z)
    neg = sum(ndimage.uniform_filter((z < -4).astype(np.float32), CLUTTER_BOX) * CLUTTER_BOX ** 2 for z in Z)
    clutter = neg > CLUTTER_NEG * (n / 4 if many(n) else 1)    # negative pixels add up over images: scale the cut with n
    T = np.array([im["t"].mjd for im in ims]) * 1440.0
    Tref = T.mean() if many(n) else T[0]
    return dict(ims=ims, D=D, Z=Z, T=T - Tref, tref_jd=Tref / 1440.0 + 2400000.5, w0=w0, cen=cen, rad=rad, clutter_frac=float(clutter.mean()), psf_fwhm=fwhm,
                scale=H.pixel_scale_deg(ims[0]["hdr"], ims[0]["style"]) * 3600 * BIN, masked=clutter)

def search(P, order=None):
    Z, T = P["Z"], P["T"].copy()
    if order is not None: T = T[order]          # scrambled control: wrong time for each image
    n, ny, nx = Z.shape; span = T.max() - T.min()
    vmax = RATE_MAX / P["scale"]; vmin = RATE_MIN / P["scale"]; dv = 2.0 / span
    g = np.arange(-vmax, vmax + dv / 2, dv)
    best = np.full((ny, nx), -np.inf, np.float32); bidx = np.zeros((ny, nx), np.int32)
    V = [(vx, vy) for vx in g for vy in g if vmin <= np.hypot(vx, vy) <= vmax]
    pad = int(np.ceil(vmax * span)) + 2
    Zp = np.zeros((n, ny + 2 * pad, nx + 2 * pad), np.float32); Zp[:, pad:pad + ny, pad:pad + nx] = Z
    if many(n):
        np.minimum(Zp, ZCLIP, out=Zp); S = np.empty((ny, nx), np.float32); tmp = np.empty((ny, nx), bool)
        for i, (vx, vy) in enumerate(V):
            S[:] = 0
            for k in range(n):
                sx, sy = int(round(vx * T[k])), int(round(vy * T[k]))
                S += Zp[k, pad + sy:pad + sy + ny, pad + sx:pad + sx + nx]
            np.greater(S, best, out=tmp); best[tmp] = S[tmp]; bidx[tmp] = i
        best /= np.sqrt(n)
        return best, bidx, V
    for i, (vx, vy) in enumerate(V):
        S = np.zeros((ny, nx), np.float32); Mx = np.full((ny, nx), -np.inf, np.float32)
        for k in range(n):
            sx, sy = int(round(vx * T[k])), int(round(vy * T[k]))
            z = Zp[k, pad + sy:pad + sy + ny, pad + sx:pad + sx + nx]; S += z; np.maximum(Mx, z, out=Mx)
        S -= Mx            # robust score: drop the brightest image, so one-image artefacts cannot drive the stack
        upd = S > best; best[upd] = S[upd]; bidx[upd] = i
    best /= np.sqrt(n - 1)
    return best, bidx, V

def candidates(P, best, bidx, V, order=None):
    Z, T = P["Z"], P["T"].copy()
    if order is not None: T = T[order]
    n, ny, nx = Z.shape
    loc = (best == ndimage.maximum_filter(best, size=9)) & (best > SCORE_MIN) & (~P["masked"] | (best >= CLUTTER_OVERRIDE))
    out = []
    for y, x in zip(*np.nonzero(loc)):
        vx, vy = V[bidx[y, x]]
        vals = []
        for k in range(n):
            xx, yy = int(round(x + vx * T[k])), int(round(y + vy * T[k]))
            vals.append(float(Z[k, yy, xx]) if 0 <= yy < ny and 0 <= xx < nx else 0.0)
        vals = np.array(vals); good = vals[vals != 0.0]          # exactly 0 = masked in that image
        if many(n):
            half = n // 2; v_ord = vals[np.argsort(T)]      # halves in the time order the search assumed (scrambled for the control)
            h1, h2 = v_ord[:half][v_ord[:half] != 0], v_ord[half:][v_ord[half:] != 0]
            if (len(good) < max(3, int(np.ceil(0.5 * n))) or (good > 0).mean() < POS_FRAC or len(h1) < 2 or len(h2) < 2
                    or h1.sum() / np.sqrt(len(h1)) < HALF_MIN or h2.sum() / np.sqrt(len(h2)) < HALF_MIN or good.max() / good.sum() > MAX_FRAC_MANY): continue
            thirds = [v[v != 0] for v in np.array_split(v_ord, 3)]
            if any(len(th) == 0 or th.mean() < THIRD_FRAC * good.mean() for th in thirds): continue
            if good.std() > max(STD_ABS, STD_REL * good.mean()): continue
        elif len(good) < 3 or good.min() < 2.0 or good.min() < MIN_RATIO * np.median(good) or good.max() / good.sum() > MAX_FRAC: continue
        sky = P["w0"].pixel_to_world(x * BIN, y * BIN)
        rate = np.hypot(vx, vy) * P["scale"]
        score = float(best[y, x])
        if many(n): score = float((good.sum() - good.max()) / np.sqrt(len(good) - 1))   # unclipped robust score (see NMS_PX note)
        out.append(dict(x=int(x * BIN), y=int(y * BIN), ra=sky.ra.deg, dec=sky.dec.deg, score=score, score_stack=float(best[y, x]),
                        rate=float(rate), vx=float(vx), vy=float(vy), per_image=[round(v, 2) for v in vals]))
    if many(n):   # non-maximum suppression by the robust score
        keep = []
        for c in sorted(out, key=lambda c: -c["score"]):
            if all(np.hypot(c["x"] - k["x"], c["y"] - k["y"]) > NMS_PX for k in keep): keep.append(c)
        out = keep
    return out

def match_truth(P, cands, known):
    """known: SkyBoT rows at mid-time. Move each to image-0 time with its catalogue rates and match."""
    t0 = P.get("tref_jd", P["ims"][0]["t"].jd); tm = np.mean([im["t"].jd for im in P["ims"]])
    dt_h = (t0 - tm) * 24
    res = []
    for k in known:
        ra = k["ra"] + k["dra_arcsec_h"] * dt_h / 3600 / np.cos(np.radians(k["dec"])); de = k["dec"] + k["ddec_arcsec_h"] * dt_h / 3600
        x, y = P["w0"].world_to_pixel(SkyCoord(ra * u.deg, de * u.deg))
        ny, nx = P["ims"][0]["data"].shape
        if not (0 <= x < nx and 0 <= y < ny): continue
        rate = np.hypot(k["dra_arcsec_h"], k["ddec_arcsec_h"]) / 60
        hit = None
        for c in cands:
            if many(len(P["ims"])):
                if np.hypot(c["x"] - x, c["y"] - y) * P["scale"] / BIN < MATCH_R_MANY and abs(c["rate"] - rate) < 0.15:
                    c["known"] = k["name"]; hit = c if hit is None or c["score"] > hit["score"] else hit
                continue
            if np.hypot(c["x"] - x, c["y"] - y) * P["scale"] / BIN < 2.5 and abs(c["rate"] - rate) < 0.15: hit = c; c["known"] = k["name"]; break
        res.append(dict(name=k["name"], V=k["V"], rate=float(rate), x=float(x), y=float(y), found=hit is not None,
                        score=hit["score"] if hit else None, masked=bool(P["masked"][int(y) // BIN, int(x) // BIN])))
    return res

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("out")
    ap.add_argument("--no-truth", action="store_true")
    ap.add_argument("--maps", default=None, help="npz cache of the two search maps (re-running the candidate stage skips the search)")
    a = ap.parse_args()
    t = time.time(); P = prepare(a.folder); n = len(P["ims"])
    cache = np.load(a.maps) if a.maps and os.path.exists(a.maps) else None
    if cache is not None: best, bidx, V = cache["best"], cache["bidx"], [tuple(v) for v in cache["V"]]
    else: best, bidx, V = search(P)
    C = candidates(P, best, bidx, V)
    # scrambled control: reverse the time order (and swap the middle pair) so no linear motion stacks
    order = np.array([n - 1 - k for k in range(n)]);
    if n == 4: order = np.array([2, 3, 0, 1])
    if many(n):   # random permutation least correlated with the true order (seeded, reproducible)
        rng = np.random.default_rng(1); best_o = None
        for _ in range(2000):
            o = rng.permutation(n); c = abs(np.corrcoef(P["T"][o], P["T"])[0, 1])
            if best_o is None or c < best_o[0]: best_o = (c, o)
        order = best_o[1]
    if cache is not None: bs, bis, Vs = cache["bs"], cache["bis"], [tuple(v) for v in cache["Vs"]]
    else: bs, bis, Vs = search(P, order)
    if a.maps and cache is None: np.savez_compressed(a.maps, best=best, bidx=bidx, V=np.array(V), bs=bs, bis=bis, Vs=np.array(Vs))
    Cs = candidates(P, bs, bis, Vs, order)
    truth = []
    if not a.no_truth:
        tm = np.mean([im["t"].jd for im in P["ims"]])
        known, _ = H.skybot(P["cen"].ra.deg, P["cen"].dec.deg, tm, P["rad"])
        truth = match_truth(P, C, known)
    res = dict(folder=a.folder, n_images=n, clutter_frac=P["clutter_frac"], n_velocities=len(V), seconds=round(time.time() - t, 1),
               psf_fwhm=P.get("psf_fwhm"), bin=BIN, scramble_order=[int(k) for k in order], tref_jd=P.get("tref_jd"),
               n_cand=len(C), n_cand_scrambled=len(Cs), cands=C, scrambled=Cs, truth=truth)
    # per-image predicted positions + cutouts for every unidentified candidate above REPORT_MIN (to check in Astrometrica)
    outdir = os.path.splitext(a.out)[0] + "_cutouts"; os.makedirs(outdir, exist_ok=True)
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    review = sorted([c for c in C if c["score"] >= REPORT_MIN and not c.get("known")], key=lambda c: -c["score"])
    for j, c in enumerate(review):
        c["id"] = f"S{j:03d}"; c["positions"] = []
        fig, axs = plt.subplots(1, n, figsize=(2.2 * n, 2.4))
        for k in range(n):
            xr, yr = c["x"] + c["vx"] * BIN * P["T"][k], c["y"] + c["vy"] * BIN * P["T"][k]      # image-0 pixel frame
            sky = P["w0"].pixel_to_world(xr, yr); xk, yk = P["D"][k]["w"].world_to_pixel(sky)
            c["positions"].append(dict(image=P["ims"][k]["file"], utc=P["ims"][k]["t"].isot, ra=sky.ra.deg, dec=sky.dec.deg, x=float(xk), y=float(yk)))
            xi, yi = int(round(float(xk))), int(round(float(yk))); cut = P["D"][k]["sub"][max(0, yi - 20):yi + 21, max(0, xi - 20):xi + 21]
            axs[k].imshow(cut, origin="lower", cmap="gray", vmin=-2 * np.std(cut), vmax=5 * np.std(cut)); axs[k].set_xticks([]); axs[k].set_yticks([])
            axs[k].set_title(f"img{k}", fontsize=7)
        fig.suptitle(f"{c['id']} stack S/N {c['score']:.1f} rate {c['rate']:.2f}\"/min", fontsize=8)
        plt.tight_layout(); plt.savefig(os.path.join(outdir, f"{c['id']}.png"), dpi=80); plt.close()
    res["review"] = [c["id"] for c in review]
    json.dump(res, open(a.out, "w"), indent=1, default=float)
    print(json.dumps({k: v for k, v in res.items() if k not in ("cands", "scrambled")}, indent=1, default=float))

if __name__ == "__main__":
    main()

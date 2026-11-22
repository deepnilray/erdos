"""Refactor of iasc_hunt.py main(): detection + linking as callable functions with tunable parameters.
Logic is identical to iasc_hunt.py at default parameters (verified on the practice set)."""
import numpy as np
from dataclasses import dataclass, asdict
from astropy.coordinates import SkyCoord
import astropy.units as u
import iasc_hunt as H


@dataclass
class Params:
    NSIG: float = 2.5
    MATCH_ARCSEC: float = 1.0
    MIN_RATE: float = 0.03
    MAX_RATE: float = 20.0
    MAX_RESID: float = 0.6
    SNR_MIN: float = 4.0
    PRED_TOL: float = 1.2
    MAG_PTP: float = 1.2
    MINAREA: int = 5
    MATCHED: bool = False   # matched-filter detection with a Gaussian kernel of the image FWHM


def detect2(im, P):
    """same as iasc_hunt.detect but with tunable minarea and optional matched-filter (Gaussian, per-image FWHM) detection."""
    import sep
    from scipy import ndimage
    d = np.ascontiguousarray(im["data"]); mask = H.gap_mask(d); near_gap = ndimage.binary_dilation(mask, iterations=8)
    bkg = sep.Background(d, mask=mask, bw=64, bh=64); sub = d - bkg.back()
    kw = {}
    if P.MATCHED:
        fw = float(np.sqrt(im["hdr"]["FWHM_MAJ"] * im["hdr"]["FWHM_MIN"])); sg = fw / 2.355; hh = int(np.ceil(3 * sg))
        yy, xx = np.mgrid[-hh:hh + 1, -hh:hh + 1]; ker = np.exp(-(xx ** 2 + yy ** 2) / (2 * sg ** 2)); kw = dict(filter_kernel=ker, filter_type="matched")
    obj = sep.extract(sub, P.NSIG, err=bkg.globalrms, mask=mask, minarea=P.MINAREA, deblend_cont=0.01, **kw)
    flux, ferr, _ = sep.sum_circle(sub, obj["x"], obj["y"], 5.0, err=bkg.globalrms, mask=mask)
    xi = np.clip(np.round(obj["x"]).astype(int), 0, d.shape[1] - 1); yi = np.clip(np.round(obj["y"]).astype(int), 0, d.shape[0] - 1)
    ok = (flux > 0) & (obj["flag"] < 4) & (obj["a"] < 8)
    o = obj[ok]; return dict(x=o["x"], y=o["y"], flux=flux[ok], ferr=ferr[ok], a=o["a"], b=o["b"], peak=o["peak"], rms=bkg.globalrms, sub=sub, gap=near_gap[yi, xi][ok])


def build_D(arrays, ims, cache, P):
    """arrays: list of float image arrays (possibly with injections); ims: loaded image dicts (header, time);
    cache: per-image dict(w=refined WCS, zp=zeropoint)."""
    H.NSIG = P.NSIG
    D = []
    for k, (arr, im) in enumerate(zip(arrays, ims)):
        im2 = dict(im); im2["data"] = arr
        det = detect2(im2, P) if (P.MATCHED or P.MINAREA != 5) else H.detect(im2)
        w, zp = cache[k]["w"], cache[k]["zp"]
        sky = w.pixel_to_world(det["x"], det["y"]); mag = zp - 2.5 * np.log10(det["flux"])
        D.append(dict(sky=sky, mag=mag, snr=det["flux"] / det["ferr"], x=det["x"], y=det["y"], w=w,
                      gap=det["gap"], ab=det["a"] / det["b"], a=det["a"], peak=det["peak"], flux=det["flux"]))
    return D


def _rotate(sky, cen, ang_deg):
    pa = cen.position_angle(sky); sep = cen.separation(sky)
    return cen.directional_offset_by(pa + ang_deg * u.deg, sep)


def find_tracklets_slow(D, T, P, scramble_seed=None, cen=None):
    """D from build_D; T: mid-times in minutes. scramble_seed: rotate non-stationary detections of images 1.. about cen
    by random angles (destroys real motion; any tracklet found is a chance alignment)."""
    n = len(D)
    stat = []
    for i in range(n):
        cnt = np.zeros(len(D[i]["sky"]), int)
        for j in range(n):
            if i == j: continue
            _, s, _ = D[i]["sky"].match_to_catalog_sky(D[j]["sky"]); cnt += (s.arcsec < P.MATCH_ARCSEC)
        stat.append(cnt >= 2)
    mov = [np.where(~stat[i] & (D[i]["snr"] > P.SNR_MIN) & ~D[i]["gap"])[0] for i in range(n)]
    S = [D[i]["sky"] for i in range(n)]
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        S = [S[0]] + [_rotate(S[i], cen, rng.uniform(15, 345)) for i in range(1, n)]
    tracks = []
    for (i0, i1) in [(0, n - 1), (0, n - 2), (1, n - 1)]:
        if i1 <= i0: continue
        dtm = T[i1] - T[i0]
        A = S[i0][mov[i0]]; B = S[i1][mov[i1]]
        if len(A) == 0 or len(B) == 0: continue
        jA, jB, sab, _ = B.search_around_sky(A, P.MAX_RATE * dtm * u.arcsec)
        for ka, kb, s in zip(jA, jB, sab.arcsec):
            pa, pb = A[ka], B[kb]; rate = s / dtm
            if rate < P.MIN_RATE: continue
            members = {i0: mov[i0][ka], i1: mov[i1][kb]}
            off_ra = (pb.ra - pa.ra).to(u.arcsec).value * np.cos(pa.dec.radian); off_de = (pb.dec - pa.dec).to(u.arcsec).value
            for k in range(n):
                if k in members: continue
                f = (T[k] - T[i0]) / dtm
                pred = SkyCoord(pa.ra + f * off_ra * u.arcsec / np.cos(pa.dec.radian), pa.dec + f * off_de * u.arcsec)
                cand = S[k][mov[k]]
                if len(cand) == 0: continue
                idx, s2, _ = pred.match_to_catalog_sky(cand)
                if s2.arcsec < P.PRED_TOL: members[k] = mov[k][idx]
            ok = False
            while len(members) >= 3:
                ks = sorted(members); t = np.array([T[k] for k in ks])
                ra = np.array([S[k][members[k]].ra.deg for k in ks]); de = np.array([S[k][members[k]].dec.deg for k in ks])
                mg = np.array([D[k]["mag"][members[k]] for k in ks])
                x = (ra - ra.mean()) * 3600 * np.cos(np.radians(de.mean())); y = (de - de.mean()) * 3600
                px, py = np.polyfit(t - t.mean(), x, 1), np.polyfit(t - t.mean(), y, 1)
                res = np.hypot(x - np.polyval(px, t - t.mean()), y - np.polyval(py, t - t.mean()))
                if res.max() <= P.MAX_RESID and np.ptp(mg) <= P.MAG_PTP: ok = True; break
                if len(members) == 3: break
                bad = np.argsort(-(res / P.MAX_RESID + np.abs(mg - np.median(mg)) / 0.6))
                drop = next((ks[b] for b in bad if ks[b] not in (i0, i1)), None)
                if drop is None: break
                members.pop(drop)
            if not ok: continue
            tracks.append(dict(members={int(k): int(v) for k, v in members.items()}, n=len(ks), rate=float(np.hypot(px[0], py[0])),
                               pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), mag=float(np.median(mg)),
                               ptp_mag=float(np.ptp(mg)), ra0=float(ra[0]), dec0=float(de[0])))
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted((k, v) for k, v in tr["members"].items()))
        if any((k, v) in seen for k, v in key): continue
        seen.update(key); uniq.append(tr)
    for tr in uniq:   # per-tracklet features for the classifier
        ks = sorted(tr["members"])
        snr = np.array([D[k]["snr"][tr["members"][k]] for k in ks]); ab = np.array([D[k]["ab"][tr["members"][k]] for k in ks])
        aa = np.array([D[k]["a"][tr["members"][k]] for k in ks]); pk = np.array([D[k]["peak"][tr["members"][k]] for k in ks])
        tr.update(snr_min=float(snr.min()), snr_med=float(np.median(snr)), elong_med=float(np.median(ab)), a_med=float(np.median(aa)),
                  a_ptp=float(np.ptp(aa)), peak_med=float(np.median(pk)), sky_first=S[ks[0]][tr["members"][ks[0]]])
    return uniq


def find_tracklets(D, T, P, scramble_seed=None, cen=None):
    """Vectorised version of find_tracklets_slow (KD-trees in the local tangent plane); same logic and acceptance rules."""
    from scipy.spatial import cKDTree
    n = len(D)
    stat = []
    for i in range(n):
        cnt = np.zeros(len(D[i]["sky"]), int)
        for j in range(n):
            if i == j: continue
            _, s, _ = D[i]["sky"].match_to_catalog_sky(D[j]["sky"]); cnt += (s.arcsec < P.MATCH_ARCSEC)
        stat.append(cnt >= 2)
    mov = [np.where(~stat[i] & (D[i]["snr"] > P.SNR_MIN) & ~D[i]["gap"])[0] for i in range(n)]
    S = [D[i]["sky"] for i in range(n)]
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        S = [S[0]] + [_rotate(S[i], cen, rng.uniform(15, 345)) for i in range(1, n)]
    ra_ref = float(np.mean([np.mean(S[i].ra.deg) for i in range(n)])); de_ref = float(np.mean([np.mean(S[i].dec.deg) for i in range(n)]))
    cosd = np.cos(np.radians(de_ref))
    XY = [np.column_stack([((S[i].ra.deg - ra_ref + 180) % 360 - 180) * cosd * 3600.0, (S[i].dec.deg - de_ref) * 3600.0]) for i in range(n)]
    tracks = []
    for (i0, i1) in [(0, n - 1), (0, n - 2), (1, n - 1)]:
        if i1 <= i0: continue
        dtm = T[i1] - T[i0]
        if len(mov[i0]) == 0 or len(mov[i1]) == 0: continue
        A = XY[i0][mov[i0]]; B = XY[i1][mov[i1]]
        tB = cKDTree(B); lists = tA = None
        pairs = tB.query_ball_point(A, r=P.MAX_RATE * dtm)
        ka = np.concatenate([np.full(len(l), a) for a, l in enumerate(pairs)]) if len(pairs) else np.array([], int)
        kb = np.concatenate([np.array(l, int) for l in pairs]) if len(pairs) else np.array([], int)
        if len(ka) == 0: continue
        dist = np.hypot(*(B[kb] - A[ka]).T); keep = dist / dtm >= P.MIN_RATE; ka, kb, dist = ka[keep], kb[keep], dist[keep]
        if len(ka) == 0: continue
        # third/fourth members by prediction
        cand = {}
        for k in range(n):
            if k in (i0, i1): continue
            if len(mov[k]) == 0: continue
            f = (T[k] - T[i0]) / dtm; pred = A[ka] + f * (B[kb] - A[ka])
            dd, ii = cKDTree(XY[k][mov[k]]).query(pred); hit = dd < P.PRED_TOL
            cand[k] = (hit, ii)
        nhit = sum((cand[k][0].astype(int) for k in cand), np.zeros(len(ka), int)) if cand else np.zeros(len(ka), int)
        for q in np.where(nhit + 2 >= 3)[0]:
            members = {i0: mov[i0][ka[q]], i1: mov[i1][kb[q]]}
            for k in cand:
                if cand[k][0][q]: members[k] = mov[k][cand[k][1][q]]
            ok = False
            while len(members) >= 3:
                ks = sorted(members); t = np.array([T[k] for k in ks])
                xs = np.array([XY[k][members[k]][0] for k in ks]); ys = np.array([XY[k][members[k]][1] for k in ks])
                mg = np.array([D[k]["mag"][members[k]] for k in ks])
                px, py = np.polyfit(t - t.mean(), xs, 1), np.polyfit(t - t.mean(), ys, 1)
                res = np.hypot(xs - np.polyval(px, t - t.mean()), ys - np.polyval(py, t - t.mean()))
                if res.max() <= P.MAX_RESID and np.ptp(mg) <= P.MAG_PTP: ok = True; break
                if len(members) == 3: break
                bad = np.argsort(-(res / P.MAX_RESID + np.abs(mg - np.median(mg)) / 0.6))
                drop = next((ks[b] for b in bad if ks[b] not in (i0, i1)), None)
                if drop is None: break
                members.pop(drop)
            if not ok: continue
            c0 = S[ks[0]][members[ks[0]]]
            tracks.append(dict(members={int(k): int(v) for k, v in members.items()}, n=len(ks), rate=float(np.hypot(px[0], py[0])),
                               pa=float(np.degrees(np.arctan2(px[0], py[0])) % 360), resid=float(res.max()), mag=float(np.median(mg)),
                               ptp_mag=float(np.ptp(mg)), ra0=float(c0.ra.deg), dec0=float(c0.dec.deg)))
    uniq, seen = [], set()
    for tr in sorted(tracks, key=lambda z: (-z["n"], z["resid"])):
        key = tuple(sorted((k, v) for k, v in tr["members"].items()))
        if any((k, v) in seen for k, v in key): continue
        seen.update(key); uniq.append(tr)
    for tr in uniq:
        ks = sorted(tr["members"])
        snr = np.array([D[k]["snr"][tr["members"][k]] for k in ks]); ab = np.array([D[k]["ab"][tr["members"][k]] for k in ks])
        aa = np.array([D[k]["a"][tr["members"][k]] for k in ks]); pk = np.array([D[k]["peak"][tr["members"][k]] for k in ks])
        tr.update(snr_min=float(snr.min()), snr_med=float(np.median(snr)), elong_med=float(np.median(ab)), a_med=float(np.median(aa)),
                  a_ptp=float(np.ptp(aa)), peak_med=float(np.median(pk)), sky_first=S[ks[0]][tr["members"][ks[0]]])
    return uniq

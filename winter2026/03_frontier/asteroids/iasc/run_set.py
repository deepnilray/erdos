"""
One command for an IASC image set: every search, one folder of results.

    python3 -I run_set.py <folder_with_fits> <outdir> --team ABC

Runs
 1. iasc_hunt.py: single-image detect + link, SkyBoT identification. Writes MPCReport.txt (Astrometrica IASC layout),
    with known objects under their MPC designations and new tracklets as ABC0001...
 2. synth.py: shift-and-stack for faint movers (0.1-1.25"/min).
 3. fast.py: trailed search for fast movers (1-15"/min, the NEO regime).
 4. Candidates from 2 and 3 that the linker did not already report:
    - PSF-fitted positions in every image;
    - a SkyBoT check;
    - a NEO-likeness flag;
    - cutouts;
    - MPC lines in the same layout, numbered after the linker's (ABC0002, ...).
    They go in candidates_MPC.txt, NOT in MPCReport.txt: confirm each in Astrometrica first, then add its lines.
Writes summary.txt in plain English.
"""
import sys, os, json, csv, argparse, subprocess, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iasc_hunt as H, synth as S, fast as F
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
from scipy.optimize import least_squares

HERE = os.path.dirname(os.path.abspath(__file__))

def psf_fit(img, x0, y0, half=8, sigma0=2.0):
    """Elliptical Gaussian + background fit in a box around (x0, y0). Returns (x, y, flux, ok)."""
    xi, yi = int(round(x0)), int(round(y0)); ny, nx = img.shape
    if xi - half < 0 or yi - half < 0 or xi + half >= nx or yi + half >= ny: return x0, y0, np.nan, False
    cut = img[yi - half:yi + half + 1, xi - half:xi + half + 1].astype(float)
    if not np.isfinite(cut).all(): return x0, y0, np.nan, False
    yy, xx = np.mgrid[-half:half + 1, -half:half + 1].astype(float)
    def model(p):
        A, dx, dy, sa, sb, th, b = p
        c, s = np.cos(th), np.sin(th); u_ = (xx - dx) * c + (yy - dy) * s; v_ = -(xx - dx) * s + (yy - dy) * c
        return A * np.exp(-0.5 * ((u_ / sa) ** 2 + (v_ / sb) ** 2)) + b
    p0 = [max(cut.max() - np.median(cut), 1e-3), x0 - xi, y0 - yi, sigma0, sigma0, 0.0, np.median(cut)]
    try:
        r = least_squares(lambda p: (model(p) - cut).ravel(), p0,
                          bounds=([0, -4, -4, 0.8, 0.8, -np.pi, -np.inf], [np.inf, 4, 4, 15, 15, np.pi, np.inf]))
        A, dx, dy, sa, sb, th, b = r.x
        ok = r.success and A > 0 and abs(dx) < 3.5 and abs(dy) < 3.5
        return xi + dx, yi + dy, 2 * np.pi * A * sa * sb, ok
    except Exception:
        return x0, y0, np.nan, False

def neo_flag(rate, pa_deg, elong=None):
    """Heuristic, not digest2: near opposition main-belt asteroids move west (PA ~ 240-300 deg) at < ~1"/min."""
    if rate > 1.5: return "possible NEO (fast)"
    if not (200 <= pa_deg % 360 <= 340): return "possible NEO (unusual direction)"
    return ""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("out"); ap.add_argument("--team", default="XXX")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); team = a.team[:3].upper()
    # 1. linker + report
    lk_out = os.path.join(a.out, "linker")
    subprocess.run([sys.executable, "-I", os.path.join(HERE, "iasc_hunt.py"), a.folder, lk_out, "--team", team], check=True)
    import shutil; shutil.copyfile(os.path.join(lk_out, "MPCReport.txt"), os.path.join(a.out, "MPCReport.txt"))   # byte-exact (CRLF)
    lk = list(csv.DictReader(open(os.path.join(lk_out, "tracklets.csv"))))
    n_lk_unknown = sum(1 for t in lk if not t["known"])
    lk_pos = [SkyCoord(float(t["ra_first"]) * u.deg, float(t["dec_first"]) * u.deg) for t in lk]
    # 2-3. synth + fast
    P = S.prepare(a.folder); ims, D, T = P["ims"], P["D"], P["T"]; n = len(ims)
    best, bidx, V = S.search(P); C = S.candidates(P, best, bidx, V)
    ft, _ = F.find_fast(P, ims[0]["hdr"].get("EXPTIME", 45.0) / 60.0, verbose=False)
    tm = np.mean([im["t"].jd for im in ims]); known, _ = H.skybot(P["cen"].ra.deg, P["cen"].dec.deg, tm, P["rad"])
    cands = []
    for c in C:
        if c["score"] < S.REPORT_MIN: continue
        pos = []
        for k in range(n):
            xr, yr = c["x"] + c["vx"] * S.BIN * P["T"][k], c["y"] + c["vy"] * S.BIN * P["T"][k]
            pos.append(P["w0"].pixel_to_world(xr, yr))
        cands.append(dict(src="stack", score=c["score"], rate=c["rate"], pred=pos))
    for tr in ft:
        # predicted positions in all images from the linear fit through the members
        ks = tr["images"]; t = np.array([T[k] for k in ks])
        ra = np.array([s.ra.deg for s in tr["sky"]]); de = np.array([s.dec.deg for s in tr["sky"]])
        pr, pd = np.polyfit(t, ra, 1), np.polyfit(t, de, 1)
        cands.append(dict(src="fast", score=tr["snr"], rate=tr["rate"], pred=[SkyCoord(np.polyval(pr, T[k]) * u.deg, np.polyval(pd, T[k]) * u.deg) for k in range(n)]))
    # drop duplicates of linker tracklets (first-image position within 3") and of each other
    keep = []
    for c in sorted(cands, key=lambda z: -z["score"]):
        p0 = c["pred"][0]
        if any(p0.separation(q).arcsec < 3 for q in lk_pos): continue
        if any(p0.separation(k["pred"][0]).arcsec < 3 for k in keep): continue
        keep.append(c)
    # 4. PSF positions, known check, MPC lines
    rows, lines = [], []
    for j, c in enumerate(keep):
        meas = []
        for k in range(n):
            x, y = D[k]["w"].world_to_pixel(c["pred"][k]); xf, yf, fl, ok = psf_fit(np.nan_to_num(D[k]["sub"]), float(x), float(y))
            sky = D[k]["w"].pixel_to_world(xf, yf) if ok else c["pred"][k]
            meas.append(dict(sky=sky, ok=ok, flux=fl))
        kn = ""
        for kobj in known:
            kp = SkyCoord(kobj["ra"] * u.deg, kobj["dec"] * u.deg)
            dt_h = (ims[0]["t"].jd - tm) * 24
            kp0 = SkyCoord((kobj["ra"] + kobj["dra_arcsec_h"] * dt_h / 3600 / np.cos(np.radians(kobj["dec"]))) * u.deg, (kobj["dec"] + kobj["ddec_arcsec_h"] * dt_h / 3600) * u.deg)
            if meas[0]["sky"].separation(kp0).arcsec < max(10, 3 * kobj["err_arcsec"]): kn = kobj["name"]; break
        s0, s1 = meas[0]["sky"], meas[-1]["sky"]
        pa = float(s0.position_angle(s1).deg)
        tmp = f"{team}{n_lk_unknown + j + 1:04d}"
        flag = neo_flag(c["rate"], pa)
        rows.append(dict(id=tmp, method=c["src"], score=round(c["score"], 1), rate_arcsec_min=round(c["rate"], 3), pa_deg=round(pa, 1),
                         psf_fits_ok=sum(m["ok"] for m in meas), known=kn, neo_flag=flag,
                         ra_first=round(s0.ra.deg, 6), dec_first=round(s0.dec.deg, 6)))
        for k, m in enumerate(meas):
            if not m["ok"]: continue
            mag = np.nan
            if np.isfinite(m["flux"]) and m["flux"] > 0: mag = D[k]["zp"] - 2.5 * np.log10(m["flux"])
            lines.append(H.mpc_line(ims[k]["t"], m["sky"], mag, tmp=tmp))
    with open(os.path.join(a.out, "candidates_review.csv"), "w", newline="") as fh:
        if rows:
            wr = csv.DictWriter(fh, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
    with open(os.path.join(a.out, "candidates_MPC.txt"), "w", newline="\r\n") as fh:
        fh.write("\n".join(lines) + ("\n" if lines else ""))
    # cutouts
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        for r_, c in zip(rows, keep):
            fig, axs = plt.subplots(1, n, figsize=(2.2 * n, 2.4))
            for k in range(n):
                x, y = D[k]["w"].world_to_pixel(c["pred"][k]); xi, yi = int(round(float(x))), int(round(float(y)))
                cut = np.nan_to_num(D[k]["sub"])[max(0, yi - 20):yi + 21, max(0, xi - 20):xi + 21]
                axs[k].imshow(cut, origin="lower", cmap="gray", vmin=-2 * np.std(cut), vmax=5 * np.std(cut)); axs[k].set_xticks([]); axs[k].set_yticks([])
                axs[k].set_title(f"img{k}", fontsize=7)
            fig.suptitle(f"{r_['id']} ({r_['method']}) S/N {r_['score']} rate {r_['rate_arcsec_min']}\"/min {r_['known'] or ''} {r_['neo_flag']}", fontsize=8)
            plt.tight_layout(); plt.savefig(os.path.join(a.out, f"{r_['id']}.png"), dpi=80); plt.close()
    except Exception as e: print("plot error", e)
    # summary
    kn_lk = [t for t in lk if t["known"]]; un_lk = [t for t in lk if not t["known"]]
    txt = [f"Image set: {a.folder} ({n} images)",
           f"MPCReport.txt: {len(kn_lk)} known asteroid(s) ({', '.join(t['known'] for t in kn_lk) or '-'}), {len(un_lk)} unidentified tracklet(s) as {team}0001...",
           f"candidates_review.csv: {len(rows)} faint/fast candidate(s) from stacking and the trail search, not in the report yet.",
           "For each candidate: open its PNG, then mark the object in Astrometrica on every image. If it is real, add its",
           "lines from candidates_MPC.txt (or Astrometrica's own measurement) to the report before submitting.",
           "Known objects SkyBoT lists on the chip: " + (", ".join(f"{k['name']} V{k['V']}" for k in known) or "none")]
    open(os.path.join(a.out, "summary.txt"), "w").write("\n".join(txt) + "\n"); print("\n".join(txt))

if __name__ == "__main__":
    main()

"""
Review cutouts for unidentified ZTF candidates (synth.py review list): each image smoothed with the PSF, the co-moving stack
along the candidate's motion, and the static stack at the mid-time position (a static source would show there instead).
Usage: python3 -I ztf_review.py <root> <outdir> <set> <synth.json> [ids...]
"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iasc_hunt as H
from scipy import ndimage
from astropy.coordinates import SkyCoord
import astropy.units as u

def main():
    root, outdir, setn, sj = sys.argv[1:5]; ids = sys.argv[5:]
    os.makedirs(outdir, exist_ok=True)
    R = json.load(open(sj)); C = [c for c in R["cands"] if c.get("id") and (not ids or c["id"] in ids)]
    if not C: return
    ims, D, info, cen, rad = H.measure(os.path.join(root, setn), verbose=False)
    n = len(ims); hw = 12
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    for c in C:
        cuts, stat = [], []
        mid = SkyCoord(c["ra"] * u.deg, c["dec"] * u.deg)
        for k, p in enumerate(c["positions"]):
            sub = ndimage.gaussian_filter(np.nan_to_num(D[k]["sub"]), 0.75)
            def cut(x, y):
                xi, yi = int(round(float(x))), int(round(float(y)))
                a = sub[yi - hw:yi + hw + 1, xi - hw:xi + hw + 1]
                return a if a.shape == (2 * hw + 1, 2 * hw + 1) else np.zeros((2 * hw + 1, 2 * hw + 1))
            cuts.append(cut(p["x"], p["y"])); xs, ys = D[k]["w"].world_to_pixel(mid); stat.append(cut(xs, ys))
        s = np.std(np.concatenate([q.ravel() for q in cuts]))
        fig, axs = plt.subplots(1, n + 2, figsize=(1.25 * (n + 2), 1.7))
        for k in range(n):
            axs[k].imshow(cuts[k], origin="lower", cmap="gray", vmin=-2 * s, vmax=5 * s); axs[k].set_title(f"{k} {c['per_image'][k]:.1f}", fontsize=6)
        for j, (img, t) in enumerate(((np.mean(cuts, 0), "co-moving"), (np.mean(stat, 0), "static"))):
            ss = np.std(np.mean(cuts, 0)); axs[n + j].imshow(img, origin="lower", cmap="gray", vmin=-2 * ss, vmax=6 * ss); axs[n + j].set_title(t, fontsize=6)
        for a in axs: a.set_xticks([]); a.set_yticks([])
        fig.suptitle(f"{setn}_{c['id']}  S/N {c['score']:.1f}  {c['rate']:.2f}\"/min  RA {c['ra']:.5f} Dec {c['dec']:.5f}  (25\" boxes)", fontsize=7)
        plt.tight_layout(); plt.savefig(os.path.join(outdir, f"{setn}_{c['id']}.png"), dpi=72); plt.close()
        print("wrote", f"{setn}_{c['id']}.png")

if __name__ == "__main__":
    main()

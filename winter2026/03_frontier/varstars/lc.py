"""Fetch ZTF light curves (all filters) for unknown candidates, run Lomb-Scargle, plot. Usage: lc.py x.csv outdir"""
import sys, os, io, numpy as np, pandas as pd, requests
from astropy.timeseries import LombScargle
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
d = pd.read_csv(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
d = d[~d.known_any]
res = []
for _, r in d.iterrows():
    try:
        q = requests.get("https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves",
                         params=dict(ID=str(int(r.oid)), FORMAT="csv"), timeout=120)
        lc = pd.read_csv(io.StringIO(q.text)); lc.to_csv(os.path.join(out, f"{int(r.oid)}_lc.csv"), index=False)
    except Exception as e: print("lc fail", r.oid, e); continue
    if len(lc) == 0: continue
    row = dict(oid=r.oid, ra=r.ra, dec=r.dec, medmag=r.medianmag)
    lc = lc[(lc.catflags == 0)].copy()
    # drop bad nights: a night whose internal scatter is far above its errors (one night of poor photometry can fake a variable)
    lc["night"] = np.floor(lc.mjd - 0.3).astype(int)
    g_ = lc.groupby("night")
    sc = g_.mag.transform(lambda x: 1.4826 * np.median(np.abs(x - np.median(x))) if len(x) >= 5 else 0.0)
    er = g_.magerr.transform("median")
    lc = lc[~((g_.mag.transform("size") >= 5) & (sc > 4 * er))]
    # night-level variability: nightly medians must vary, across many nights
    nm = lc.groupby(["filtercode", "night"]).agg(m=("mag", "median"), e=("magerr", "median"), k=("mag", "size")).reset_index()
    for f in ("zg", "zr"):
        q_ = nm[nm.filtercode == f]
        if len(q_) >= 20:
            row[f"nights_{f}"] = len(q_); row[f"namp_{f}"] = float(np.percentile(q_.m, 95) - np.percentile(q_.m, 5))
            row[f"nchi_{f}"] = float(np.mean(((q_.m - np.median(q_.m)) / q_.e) ** 2))
    fig, axs = plt.subplots(1, 3, figsize=(15, 3.6))
    best = None
    for f, col in (("zg", "g"), ("zr", "r"), ("zi", "m")):
        s = lc[lc.filtercode == f]
        if len(s) < 30: continue
        axs[0].errorbar(s.mjd, s.mag, s.magerr, fmt=".", ms=2, color=col, alpha=0.5, label=f)
        row[f"n_{f}"] = len(s); row[f"amp_{f}"] = float(np.percentile(s.mag, 95) - np.percentile(s.mag, 5))
        row[f"chi_{f}"] = float(np.mean(((s.mag - np.median(s.mag)) / s.magerr) ** 2))
        if f == "zr" or (best is None and f == "zg"):
            ls = LombScargle(s.mjd, s.mag, s.magerr); fr, pw = ls.autopower(minimum_frequency=1 / 1500, maximum_frequency=50, samples_per_peak=5, method="fast")
            k = np.argmax(pw); P = 1 / fr[k]; fap = float(ls.false_alarm_probability(pw[k]))
            best = (f, P, float(pw[k]), fap)
            nb = len(pw) // 4000 + 1; m_ = len(pw) // nb * nb
            axs[1].plot(1 / fr[:m_].reshape(-1, nb)[:, 0], pw[:m_].reshape(-1, nb).max(axis=1), lw=0.5); axs[1].set_xscale("log"); axs[1].set_xlabel("period (d)")
    if best:
        f, P, pw, fap = best; row.update(band=f, period_d=P, ls_power=pw, fap=fap)
        for ff, col in (("zg", "g"), ("zr", "r")):
            s = lc[lc.filtercode == ff]
            if len(s) >= 30:
                ph = (s.mjd / P) % 1; axs[2].plot(np.r_[ph, ph + 1], np.r_[s.mag, s.mag], ".", ms=2, color=col)
        axs[2].set_title(f"P = {P:.5f} d (power {pw:.2f})")
    for a in (axs[0], axs[2]): a.invert_yaxis()
    axs[0].legend(fontsize=7); fig.suptitle(f"ZTF oid {r.oid}  RA {r.ra:.5f} Dec {r.dec:.5f}  r~{r.medianmag:.2f}", fontsize=9)
    plt.tight_layout(); plt.savefig(os.path.join(out, f"{r.oid}.png"), dpi=70); plt.close()
    res.append(row); print(row, flush=True)
pd.DataFrame(res).to_csv(os.path.join(out, "lc_summary.csv"), index=False)

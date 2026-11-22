"""Threshold tuning on TRAIN-region injections (x < nx/2), faint end only (mag 21-23.5), then fixed-config evaluation on TEST region.
Usage: python tune.py <fits_folder> <cache.pkl dir> <config_name> <region> <n_trials> <seed>"""
import sys, os, json, pickle, numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
import iasc_hunt as H
from tracker import Params, build_D, find_tracklets
import build_db as B

CONFIGS = {
    "base": Params(),
    "snr3": Params(SNR_MIN=3.0),
    "n2snr35": Params(NSIG=2.0, SNR_MIN=3.5),
    "n2snr3": Params(NSIG=2.0, SNR_MIN=3.0),
    "mf4": Params(NSIG=4.0, SNR_MIN=3.0, MINAREA=3, MATCHED=True),
    "mf3": Params(NSIG=3.0, SNR_MIN=3.0, MINAREA=3, MATCHED=True),
    "ma3": Params(MINAREA=3),
    "ma3n22": Params(NSIG=2.2, MINAREA=3, SNR_MIN=3.5),
    "n2snr3_gap": Params(NSIG=2.0, SNR_MIN=3.0, MAX_RESID=0.8, PRED_TOL=1.5),
}


def main():
    folder, cdir, cname, region, ntr, seed = sys.argv[1:7]; ntr = int(ntr); seed = int(seed)
    P = CONFIGS[cname]
    ims = H.load(folder); pk = pickle.load(open(os.path.join(cdir, "cache.pkl"), "rb"))
    cen = SkyCoord(pk["cen_ra"] * u.deg, pk["cen_dec"] * u.deg); T = np.array([im["t"].mjd for im in ims]) * 1440.0
    D0 = build_D([im["data"] for im in ims], ims, pk["cache"], P); base = find_tracklets(D0, T, P)
    base_sky = [b["sky_first"] for b in base]
    rec, tot, rows, fp_inj = 0, 0, [], 0
    for trial in range(ntr):
        rng = np.random.default_rng(seed * 100000 + trial)
        arrs, truth = B.make_trial(ims, pk, rng, 6, region, mag_rng=(21.0, 23.5))
        D = build_D(arrs, ims, pk["cache"], P); trk = find_tracklets(D, T, P)
        for tr in trk: tr["members_sky"] = {k: D[k]["sky"][v] for k, v in tr["members"].items()}
        used = set()
        for tr in trk:
            ti = B.match_truth(tr, truth, ims)
            if ti >= 0: used.add(ti)
            elif not any(tr["sky_first"].separation(bs).arcsec < 3 for bs in base_sky): fp_inj += 1
        for tt in truth: rows.append((tt["mag"], tt["rate"], int(tt["src"] in used)))
    arr = np.array(rows); nscr = 100
    fp_scr = sum(len(find_tracklets(D0, T, P, scramble_seed=seed * 1000 + s, cen=cen)) for s in range(nscr))
    res = dict(config=cname, params=P.__dict__, region=region, n_sources=len(arr), recall=float(arr[:, 2].mean()),
               recall_by_mag={f"{a}-{b}": float(arr[(arr[:, 0] >= a) & (arr[:, 0] < b), 2].mean()) for a, b in [(21, 22), (22, 22.5), (22.5, 23), (23, 23.5)]},
               false_tracklets_per_scramble_set=fp_scr / nscr, false_tracklets_in_injection_runs_per_set=fp_inj / ntr, n_baseline_tracklets=len(base))
    print(json.dumps(res)); open(f"tune_{cname}_{region}.json", "w").write(json.dumps(res, indent=1))


if __name__ == "__main__": main()

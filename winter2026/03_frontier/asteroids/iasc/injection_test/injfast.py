import sys, os, json, shutil, numpy as np, time
sys.path.insert(0, '/home/claude/erdos/winter2026/03_frontier/asteroids/iasc'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iasc_hunt as H, fast as F, synth as S, hand_build_db as B
from astropy.io import fits
from astropy.coordinates import SkyCoord; import astropy.units as u
SRC, OUT, NTR, SEED = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
os.makedirs(OUT, exist_ok=True); ims, pk = B.load_cache(SRC, OUT); rng = np.random.default_rng(SEED)
def run(folder):
    P = S.prepare(folder); D = P["D"]; T = P["T"]
    lt = H.find_tracklets(D, T, verbose=False)
    ft, det = F.find_fast(P, 0.75, verbose=False)
    return D, lt, ft
if NTR == 0:   # the real practice set, no injections: fast false alarms
    D, lt, ft = run(SRC); print('practice set: fast tracklets', len(ft), [(round(t['rate'],2), round(t['snr'],1)) for t in ft]); sys.exit()
for t in range(NTR):
    arrs, truth = B.make_trial(ims, pk, rng, 6, "train" if t % 2 == 0 else "test", mag_rng=(19.0, 22.5), rate_rng=(1.25, 15.0))
    d = os.path.join(OUT, f"trial_{SEED}_{t}"); os.makedirs(d, exist_ok=True)
    for im, a in zip(ims, arrs): fits.writeto(os.path.join(d, im["file"]), np.clip(np.round(a), 0, 65535).astype(np.uint16), im["hdr"], overwrite=True)
    t0 = time.time(); D, lt, ft = run(d)
    used = set()
    for tt in truth:
        path = {k: SkyCoord(ra * u.deg, dec * u.deg) for k, ra, dec in tt["path"]}
        lk = any(sum(D[k]["sky"][i].separation(path[k]).arcsec < 1.5 for k, i in tr["members"].items()) >= 3 for tr in lt)
        fk = False
        for j, tr in enumerate(ft):
            if sum(s.separation(path[k]).arcsec < 2.5 for k, s in zip(tr["images"], tr["sky"])) >= 3: fk = True; used.add(j)
        open(os.path.join(OUT, f"res_{SEED}.jsonl"), "a").write(json.dumps(dict(trial=t, mag=tt["mag"], rate=tt["rate"], linker=bool(lk), fast=bool(fk))) + "\n")
    open(os.path.join(OUT, f"fa_{SEED}.jsonl"), "a").write(json.dumps(dict(trial=t, fast_false=len(ft) - len(used), secs=round(time.time() - t0))) + "\n")
    shutil.rmtree(d); print("trial", t, "done", round(time.time() - t0), "s", flush=True)

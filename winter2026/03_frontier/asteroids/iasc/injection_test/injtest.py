"""Injection test on the real IASC practice chip: linker (iasc_hunt.find_tracklets) vs synth.py, same injected sets.
Injection code = the other session's build_db.make_trial (Moffat PSF per image FWHM, trailed, Poisson noise)."""
import sys, os, json, shutil, numpy as np
sys.path.insert(0, '/home/claude/erdos/winter2026/03_frontier/asteroids/iasc'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iasc_hunt as H, synth as S, hand_build_db as B
from astropy.io import fits
from astropy.coordinates import SkyCoord; import astropy.units as u
SRC = sys.argv[1]; OUT = sys.argv[2]; NTR = int(sys.argv[3]); SEED = int(sys.argv[4])
os.makedirs(OUT, exist_ok=True)
ims, pk = B.load_cache(SRC, OUT)
rng = np.random.default_rng(SEED); rows = []
res_path = os.path.join(OUT, f"results_{SEED}.jsonl")
for t in range(NTR):
    arrs, truth = B.make_trial(ims, pk, rng, 6, "train" if t % 2 == 0 else "test")
    d = os.path.join(OUT, f"trial_{SEED}_{t}"); os.makedirs(d, exist_ok=True)
    for im, a in zip(ims, arrs):
        fits.writeto(os.path.join(d, im["file"]), np.clip(np.round(a), 0, 65535).astype(np.uint16), im["hdr"], overwrite=True)
    P = S.prepare(d); D = P["D"]; T = P["T"]
    tracks = H.find_tracklets(D, T, verbose=False)
    best, bidx, V = S.search(P); C = S.candidates(P, best, bidx, V)
    for tt in truth:
        path = {k: SkyCoord(ra * u.deg, dec * u.deg) for k, ra, dec in tt["path"]}
        lk = False
        for tr in tracks:
            hit = sum(D[k]["sky"][i].separation(path[k]).arcsec < 1.5 for k, i in tr["members"].items())
            if hit >= 3: lk = True; break
        sc = 0.0
        for c in C:
            if SkyCoord(c["ra"] * u.deg, c["dec"] * u.deg).separation(path[0]).arcsec < 2.5 and abs(c["rate"] - tt["rate"]) < max(0.15, 0.2 * tt["rate"]):
                sc = max(sc, c["score"])
        rows.append(dict(seed=SEED, trial=t, mag=tt["mag"], rate=tt["rate"], linker=lk, synth_score=sc))
        open(res_path, "a").write(json.dumps(rows[-1]) + "\n")
    # unmatched synth candidates above 10 = false alarms (excluding the 2 real objects)
    real = [SkyCoord(3.1075984 * u.deg, -10.7306536 * u.deg), SkyCoord(3.0415608 * u.deg, -10.7813501 * u.deg)]
    nfa = 0
    for c in C:
        if c["score"] < 10: continue
        cs = SkyCoord(c["ra"] * u.deg, c["dec"] * u.deg)
        if any(cs.separation(SkyCoord(ra * u.deg, dec * u.deg)).arcsec < 3 for tt in truth for k, ra, dec in tt["path"][:1]): continue
        if any(cs.separation(r).arcsec < 30 for r in real): continue
        nfa += 1
    open(os.path.join(OUT, f"fa_{SEED}.jsonl"), "a").write(json.dumps(dict(trial=t, synth_fa10=nfa, n_tracks=len(tracks))) + "\n")
    shutil.rmtree(d); print("trial", t, "done", flush=True)

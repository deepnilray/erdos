"""End-to-end check of run_set.py on injected sets: is each injected mover reported, and how good are the positions?"""
import sys, os, json, shutil, subprocess, numpy as np
sys.path.insert(0, '/home/claude/erdos/winter2026/03_frontier/asteroids/iasc'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_build_db as B
from astropy.io import fits
from astropy.coordinates import SkyCoord; from astropy.time import Time; import astropy.units as u
SRC, OUT, NTR, SEED = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
os.makedirs(OUT, exist_ok=True); ims, pk = B.load_cache(SRC, OUT); rng = np.random.default_rng(SEED)
def parse(path):
    out = []
    if not os.path.exists(path): return out
    for l in open(path).read().splitlines():
        if len(l) != 80 or l[14] != 'C': continue
        y, m, d = int(l[15:19]), int(l[20:22]), float(l[23:32])
        c = SkyCoord(l[32:44], l[44:56], unit=(u.hourangle, u.deg))
        out.append((l[5:12].strip(), Time(f"{y:04d}-{m:02d}-01T00:00:00", scale='utc') + (d - 1) * u.day, c))
    return out
for t in range(NTR):
    arrs, truth = B.make_trial(ims, pk, rng, 6, "train" if t % 2 == 0 else "test", mag_rng=(19.5, 22.3), rate_rng=(0.1, 10.0))
    d = os.path.join(OUT, f"set_{SEED}_{t}"); os.makedirs(d, exist_ok=True)
    for im, a in zip(ims, arrs): fits.writeto(os.path.join(d, im["file"]), np.clip(np.round(a), 0, 65535).astype(np.uint16), im["hdr"], overwrite=True)
    o = os.path.join(OUT, f"rs_{SEED}_{t}")
    subprocess.run([sys.executable, "-I", "/home/claude/erdos/winter2026/03_frontier/asteroids/iasc/run_set.py", d, o, "--team", "TST"], capture_output=True)
    lines = [("report",) + x for x in parse(os.path.join(o, "MPCReport.txt"))] + [("cand",) + x for x in parse(os.path.join(o, "candidates_MPC.txt"))]
    for tt in truth:
        path = [SkyCoord(ra * u.deg, dec * u.deg) for k, ra, dec in tt["path"]]
        best = None
        for src, des, tm, c in lines:
            k = int(np.argmin([abs((tm - im["t"]).sec) for im in ims]))
            if abs((tm - ims[k]["t"]).sec) > 5: continue
            s = c.separation(path[k]).arcsec
            if s < 2.0:
                best = best or dict(src=src, des=des, oc=[])
                if des == best["des"]: best["oc"].append(s)
        open(os.path.join(OUT, f"e2e_{SEED}.jsonl"), "a").write(json.dumps(dict(trial=t, mag=tt["mag"], rate=tt["rate"], found=best is not None,
            src=best["src"] if best else None, n_lines=len(best["oc"]) if best else 0, oc_med=float(np.median(best["oc"])) if best else None)) + "\n")
    shutil.rmtree(d); print("trial", t, "done", flush=True)

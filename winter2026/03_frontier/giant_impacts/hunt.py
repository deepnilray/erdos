"""
Giant-impact afterglow hunt on raw NEOWISE single-exposure photometry (runs in GitHub Actions).
Pool: FGK members of young open clusters (Hunt & Reffert 2023, VizieR J/A+A/673/A114), ages 15-500 Myr, plus validation
objects with known collisions (ASASSN-21qj; NGC 2547-ID8), whose positions come from their 2MASS designations.
Detector: per 6-month visit medians; sustained (>=2 consecutive visits) brightening in W2 that exceeds W1 (reddening),
measured against the early-mission baseline. Resumable: state lives in results/ and is carried between runs.
"""
import os, sys, json, time, re, traceback, numpy as np, pyvo
from astropy.table import Table
from concurrent.futures import ThreadPoolExecutor, as_completed
OUT = "results"; os.makedirs(OUT, exist_ok=True)
L = open(f"{OUT}/hunt_log.txt", "a")
def log(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(map(str, a)); print(s, flush=True); L.write(s + "\n"); L.flush()
IRSA = "https://irsa.ipac.caltech.edu/TAP"; VIZ = os.environ.get("VIZ_TAP", "https://tapvizier.cds.unistra.fr/TAPVizieR/tap")
BUDGET = float(os.environ.get("BUDGET_MIN", "300")) * 60; T0 = time.time()
VALID = {"ASASSN-21qj": (123.847042, -38.989833), "NGC2547-ID8": (122.260417, -48.971444)}

def pick(cols, *pats):
    for p in pats:
        for c in cols:
            if re.fullmatch(p, c, re.I): return c
    return None

def build_pool():
    path = f"{OUT}/pool.csv"
    if os.path.exists(path): return Table.read(path, format="csv")
    try:
        if os.environ.get("USE_CLUSTERS") != "1": raise RuntimeError("cluster pool disabled (VizieR unreachable from Actions on 2026-11-17)")
        return _pool_clusters(path)
    except Exception as e:
        log("cluster pool unavailable:", repr(e)[:200], "-> Gaia DR3 nearby main-sequence pool")
    gaia = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
    q = ("SELECT source_id, ra, dec, phot_g_mean_mag AS gmag, bp_rp AS bprp, parallax AS plx FROM gaiadr3.gaia_source "
         "WHERE parallax > 4 AND parallax_over_error > 10 AND phot_g_mean_mag BETWEEN 8 AND 15 "
         "AND bp_rp BETWEEN 0.55 AND 2.2 AND ruwe < 1.4")
    log("gaia pool query:", q)
    from astropy.table import vstack
    parts = []
    for r0 in range(0, 360, 5):          # synchronous queries in 5-degree RA strips (async jobs fail via pyvo here)
        qq = q + f" AND ra >= {r0} AND ra < {r0 + 5}"
        for attempt in range(3):
            try:
                p = gaia.run_sync(qq, maxrec=200000).to_table(); parts.append(p); break
            except Exception as e:
                log("strip", r0, "failed:", repr(e)[:300]); time.sleep(10)
    t = vstack(parts); log("gaia pool rows:", len(t), "from", len(parts), "strips")
    absg = np.array(t["gmag"], float) + 5 * np.log10(np.array(t["plx"], float) / 100.0)
    x = np.array(t["bprp"], float); ms = (absg > 2.2 * x + 0.2) & (absg < 2.9 * x + 3.6)
    t = t[ms]; t = t[np.argsort(-np.array(t["plx"], float))]; log("after main-sequence cut:", len(t))
    t["prob"] = 1.0; t["cluster"] = "field"; t["logage"] = np.nan
    return _finish_pool(t, path)

def _finish_pool(t, path):
    t = Table({k: t[k] for k in ("source_id", "ra", "dec", "gmag", "bprp", "plx", "prob", "cluster", "logage")})
    t["cluster"] = t["cluster"].astype("U40")
    for name, (r, d) in VALID.items():
        t.add_row({"source_id": -1, "ra": r, "dec": d, "gmag": np.nan, "bprp": np.nan, "plx": np.nan, "prob": 1.0, "cluster": "VALID:" + name, "logage": np.nan})
    t["uid"] = np.arange(len(t)); t.write(path, format="csv", overwrite=True); return t

def _pool_clusters(path):
    viz = pyvo.dal.TAPService(VIZ)
    tabs = viz.run_sync("SELECT table_name FROM TAP_SCHEMA.tables WHERE table_name LIKE 'J/A+A/673/A114%'").to_table()
    names = [str(x) for x in tabs["table_name"]]; log("Hunt&Reffert tables:", names)
    def cols(t): return [str(x) for x in viz.run_sync(f"SELECT column_name FROM TAP_SCHEMA.columns WHERE table_name='{t}'").to_table()["column_name"]]
    ct = [n for n in names if n.endswith("clusters")][0]; mt = [n for n in names if n.endswith("members")][0]
    cc, mc = cols(ct), cols(mt); log("cluster cols:", cc); log("member cols:", mc)
    age = pick(cc, "logAge50", "logAge", "logAge16", ".*logage.*"); ckey = pick(cc, "ID", "Name"); mkey = pick(mc, "ID", "Name")
    ra, de = pick(mc, "RA_ICRS", "RAdeg", "_RA"), pick(mc, "DE_ICRS", "DEdeg", "_DE")
    g, bprp, prob = pick(mc, "Gmag", "phot_g_mean_mag"), pick(mc, "BP-RP", "BPRP", "bp_rp"), pick(mc, "Prob", "Pmemb", "proba")
    plx = pick(mc, "Plx", "parallax"); src = pick(mc, "GaiaDR3", "Source", "source_id")
    log("chosen:", dict(age=age, ckey=ckey, mkey=mkey, ra=ra, de=de, g=g, bprp=bprp, prob=prob, plx=plx, src=src))
    q = (f'SELECT m."{src}" AS source_id, m."{ra}" AS ra, m."{de}" AS dec, m."{g}" AS gmag, m."{bprp}" AS bprp, '
         f'm."{plx}" AS plx, m."{prob}" AS prob, c."{ckey}" AS cluster, c."{age}" AS logage '
         f'FROM "{mt}" AS m JOIN "{ct}" AS c ON m."{mkey}" = c."{ckey}" '
         f'WHERE c."{age}" BETWEEN 7.18 AND 8.70 AND m."{prob}" > 0.7 AND m."{g}" < 16.5 '
         f'AND m."{bprp}" BETWEEN 0.55 AND 2.2 AND m."{plx}" > 0.5')
    log("pool query:", q)
    t = viz.run_async(q, maxrec=2000000).to_table(); log("pool from clusters:", len(t))
    # main-sequence cut in absolute G (rough FGK/early-M band), removes giants
    absg = np.array(t["gmag"], float) + 5 * np.log10(np.array(t["plx"], float) / 100.0)
    x = np.array(t["bprp"], float); ms = (absg > 2.2 * x + 0.2) & (absg < 2.9 * x + 3.6)
    t = t[ms]; log("after main-sequence cut:", len(t))
    return _finish_pool(t, path)

GOODQ = ("n.qual_frame > 0 AND n.qi_fact > 0.9 AND n.saa_sep > 5 AND n.moon_masked = '00' "
         "AND n.w1snr > 3 AND n.w2snr > 3 AND n.nb = 1")

def fetch_chunk(sub):
    svc = pyvo.dal.TAPService(IRSA)
    up = Table({"uid": np.array(sub["uid"], int), "ra": np.array(sub["ra"], float), "dec": np.array(sub["dec"], float)})
    q = ("SELECT u.uid, n.mjd, n.w1mpro, n.w1sigmpro, n.w2mpro, n.w2sigmpro, n.cc_flags FROM TAP_UPLOAD.pos AS u, "
         "neowiser_p1bs_psd AS n WHERE CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', u.ra, u.dec, 0.000833)) = 1 AND " + GOODQ)
    for attempt in range(3):
        try:
            return svc.run_async(q, uploads={"pos": up}, maxrec=5000000).to_table()
        except Exception as e:
            log("chunk retry", attempt, repr(e)[:200]); time.sleep(20 * (attempt + 1))
    return None

def visits(m, v1, e1, v2, e2):
    o = np.argsort(m); m, v1, v2 = m[o], v1[o], v2[o]
    cuts = np.where(np.diff(m) > 30)[0] + 1; out = []
    for s in np.split(np.arange(len(m)), cuts):
        if len(s) < 5: continue
        a, b = v1[s], v2[s]
        out.append((np.median(m[s]), np.median(a), max(1.25 * np.median(np.abs(a - np.median(a))) / np.sqrt(len(s)), 0.005),
                    np.median(b), max(1.25 * np.median(np.abs(b - np.median(b))) / np.sqrt(len(s)), 0.005), len(s)))
    return np.array(out)

def score(V):
    """returns dict of detector quantities; brightening is positive."""
    if len(V) < 6: return None
    base = V[:3]; b1, b2 = np.median(base[:, 1]), np.median(base[:, 3])
    sc1 = max(np.std(base[:, 1]), np.median(base[:, 2]), 0.01); sc2 = max(np.std(base[:, 3]), np.median(base[:, 4]), 0.01)
    # robust whole-curve scatter (catches ordinary variables): MAD of visit-to-visit differences
    d2 = np.diff(V[:, 3]); jit = max(1.48 * np.median(np.abs(d2)) / np.sqrt(2), 0.01)
    D1, D2 = b1 - V[:, 1], b2 - V[:, 3]
    best = dict(dW2=0.0, dW1=0.0, start=np.nan, nvis=0)
    for i in range(3, len(V) - 1):
        w2 = min(D2[i], D2[i + 1]); w1 = min(D1[i], D1[i + 1])
        if w2 > best["dW2"]:
            j = i
            while j + 1 < len(V) and D2[j + 1] > 0.5 * w2: j += 1
            best = dict(dW2=float(w2), dW1=float(w1), start=float(V[i, 0]), nvis=int(j - i + 1))
    s = best["dW2"] / np.hypot(sc2, jit)
    return dict(score=float(s), base_w1=float(b1), base_w2=float(b2), base_w1w2=float(b1 - b2), jitter=float(jit),
                redden=float(best["dW2"] - best["dW1"]), n_visits=int(len(V)), **best)

def main():
    pool = build_pool(); done_path = f"{OUT}/scores.csv"
    done = set()
    if os.path.exists(done_path):
        for line in open(done_path).read().splitlines()[1:]: done.add(int(line.split(",")[0]))
    else:
        open(done_path, "w").write("uid,score,dW2,dW1,redden,start,nvis,n_visits,base_w1,base_w2,base_w1w2,jitter\n")
    todo = [i for i in np.array(pool["uid"], int) if i not in done]
    # validation objects first
    vfirst = [int(u) for u, c in zip(pool["uid"], pool["cluster"]) if str(c).startswith("VALID:")]
    todo = vfirst + [u for u in todo if u not in vfirst]
    log(f"pool {len(pool)}, done {len(done)}, to do {len(todo)}")
    CH = 250; chunks = [todo[i:i + CH] for i in range(0, len(todo), CH)]
    lcdir = f"{OUT}/lc"; os.makedirs(lcdir, exist_ok=True)
    def work(ch):
        sub = pool[np.isin(np.array(pool["uid"], int), ch)]
        t = fetch_chunk(sub); return ch, t
    nproc = 0
    with ThreadPoolExecutor(4) as ex:
        futs = []
        for ch in chunks:
            if time.time() - T0 > BUDGET: break
            futs.append(ex.submit(work, ch))
            if len(futs) >= 8:
                for f in as_completed(futs[:4]): pass
            # harvest finished
            for f in [f for f in futs if f.done()]:
                futs.remove(f); nproc += harvest(f.result(), done_path, lcdir)
            if time.time() - T0 > BUDGET: break
        for f in as_completed(futs): nproc += harvest(f.result(), done_path, lcdir)
    log("processed this run:", nproc)
    summarize(pool)

def harvest(res, done_path, lcdir):
    ch, t = res
    if t is None: log("chunk failed, will retry next run"); return 0
    uid = np.array(t["uid"], int); m = np.array(t["mjd"], float)
    w1, e1, w2, e2 = (np.array(t[c], float) for c in ("w1mpro", "w1sigmpro", "w2mpro", "w2sigmpro"))
    cc = np.array([str(x) for x in t["cc_flags"]]); ok = np.array([c[:2] in ("00", "0") or c == "0000" for c in cc]) & np.isfinite(w1 + w2)
    rows = []
    for u in ch:
        s = (uid == u) & ok; r = None
        if s.sum() >= 30:
            V = visits(m[s], w1[s], e1[s], w2[s], e2[s]); r = score(V)
            if r and (r["score"] > 8 or u in VALIDU): np.savetxt(f"{lcdir}/{u}.txt", V, fmt="%.5f", header="mjd w1 e1 w2 e2 n")
        if r is None: r = dict(score=np.nan, dW2=np.nan, dW1=np.nan, redden=np.nan, start=np.nan, nvis=0, n_visits=0, base_w1=np.nan, base_w2=np.nan, base_w1w2=np.nan, jitter=np.nan)
        rows.append(f"{u},{r['score']:.3f},{r['dW2']:.4f},{r['dW1']:.4f},{r['redden']:.4f},{r['start']:.1f},{r['nvis']},{r['n_visits']},{r['base_w1']:.3f},{r['base_w2']:.3f},{r['base_w1w2']:.3f},{r['jitter']:.4f}")
    with open(done_path, "a") as fh: fh.write("\n".join(rows) + "\n")
    return len(ch)

def summarize(pool):
    import pandas as pd
    s = pd.read_csv(f"{OUT}/scores.csv"); p = pool.to_pandas(); d = s.merge(p, on="uid", how="left")
    log("scored:", len(d), "| with light curve:", int(np.isfinite(d.score).sum()))
    for name in VALID:
        v = d[d.cluster == "VALID:" + name]
        log(f"VALIDATION {name}:", v[["score", "dW2", "dW1", "redden", "start", "nvis", "n_visits"]].to_dict("records"))
        if len(v) and np.isfinite(v.score.iloc[0]):
            rank = int((d.score > v.score.iloc[0]).sum()) + 1; log(f"   rank of {name} among all scored: {rank}")
    good = d[np.isfinite(d.score)]
    for thr in (5, 8, 12, 20, 40): log(f"score > {thr}: {(good.score > thr).sum()}  (and reddening dW2-dW1>0.05: {((good.score > thr) & (good.redden > 0.05)).sum()})")
    cand = good[(good.score > 8) & (good.redden > 0.05) & (good.nvis >= 2)].sort_values("score", ascending=False)
    cand.to_csv(f"{OUT}/candidates.csv", index=False); log("candidates written:", len(cand))
    log(cand.head(40)[["uid", "cluster", "logage", "gmag", "bprp", "ra", "dec", "score", "dW2", "dW1", "start", "nvis", "base_w1w2"]].to_string())
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        os.makedirs(f"{OUT}/plots", exist_ok=True)
        show = list(cand.uid.head(40)) + [int(u) for u in d[d.cluster.astype(str).str.startswith("VALID:")].uid]
        for u in show:
            f = f"{OUT}/lc/{u}.txt"
            if not os.path.exists(f): continue
            V = np.loadtxt(f, ndmin=2); r = d[d.uid == u].iloc[0]
            plt.figure(figsize=(6, 3.2))
            plt.errorbar(V[:, 0], V[:, 1], V[:, 2], fmt="o", ms=3, label="W1"); plt.errorbar(V[:, 0], V[:, 3], V[:, 4], fmt="s", ms=3, label="W2")
            plt.gca().invert_yaxis(); plt.xlabel("MJD"); plt.ylabel("mag"); plt.legend(fontsize=7)
            plt.title(f"uid {u} {r.cluster} score {r.score:.1f} ra {r.ra:.4f} dec {r.dec:.4f}", fontsize=7); plt.tight_layout()
            plt.savefig(f"{OUT}/plots/{u}.png", dpi=90); plt.close()
    except Exception: traceback.print_exc(file=L)

VALIDU = set()
if __name__ == "__main__":
    try:
        pool = build_pool(); VALIDU.update(int(u) for u, c in zip(pool["uid"], pool["cluster"]) if str(c).startswith("VALID:"))
        main()
    except Exception: traceback.print_exc(file=L); traceback.print_exc()

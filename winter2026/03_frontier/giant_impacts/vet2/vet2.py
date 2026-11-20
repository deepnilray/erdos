"""
vet2: automated vetting stage for the giant-impact infrared transient search. Every target gets the same checks that were
done by hand in LOG.md (2026-11-17 .. 2026-11-20), with explicit, recorded kill rules. Runs in GitHub Actions
(.github/workflows/giant_impacts_vet2.yml, results on branch impacts-vet2) and locally (ASAS-SN Sky Patrol needs port 9006).

Target list (env TARGETS):
  near : detector-1 (D1) candidates from the shard branches impacts-live-0..3 (score > 8, redden > 0.05, nvis >= 2),
         with ra/dec from hunt.build_pool() (POOL=near), plus ../blindspot/d2_excess_variability_near.csv (detector 2, D2)
  far  : the same D1 cuts on impacts-far-0..3, plus the D2 selection computed on the far pool (baseline W1-W2 more than
         0.10 mag and z > 5 above the BP-RP locus, W1 > 8, visit jitter > 3x the median at that W2), pool from
         hunt.build_pool() under POOL=far
  list : LIST_CSV, a CSV with columns ra,dec,name
Controls always added: ASASSN-21qj (must pass every check and be found in SIMBAD), J060000 (2019 optical dip must show in
ASAS-SN), V836 Tau = Gaia DR3 3420008412568724736 (must be flagged young).

Per target: refetched NEOWISE light curve (hunt.visits / hunt.score, score reproduced against the stored one); centroid of
every visit against a proper-motion trend and the jump at the event onset; field control (same-epoch step of every NEOWISE
neighbour within 12 arcmin with W2 8.5-12.5); AllWISE 2010 colours and Class I/II-like colour cuts; Gaia DR3 neighbours,
RUWE, ipd_frac_multi_peak, NSS tables, GSP-Phot, H-alpha pseudo-EW, variability class, position on the M_G vs BP-RP sequence;
SIMBAD (IDIA mirror) object types and reference counts; ASAS-SN light curve normalised per camera; dust temperature from the
W1/W2 excess-flux ratio. Kill rules and flags are in verdict().

Robustness: every HTTP request has a timeout (requests.Session.request is patched), every query is retried and cached on disk
(CACHE dir, successful results only), output is rewritten after every target, and an exception in one check or one target is
recorded in that target's `errors` field and never stops the run.
"""
import os, sys, json, time, hashlib, pickle, threading, traceback, io, math, re
import numpy as np, pandas as pd, requests

HERE = os.path.dirname(os.path.abspath(__file__)); GI = os.path.dirname(HERE)
MODE = os.environ.get("TARGETS", "near").strip().lower()
OUT = os.path.abspath(os.environ.get("OUT", os.path.join(HERE, "out", MODE)))
CACHE = os.path.abspath(os.environ.get("CACHE", os.path.join(HERE, "cache")))
NET_TIMEOUT = float(os.environ.get("NET_TIMEOUT", "300"))
DEADLINE = float(os.environ.get("VET2_DEADLINE_MIN", "200")) * 60
DO_ASASSN = os.environ.get("ASASSN", "1") == "1"
NMAX = int(os.environ.get("NMAX", "200"))
THREADS = int(os.environ.get("THREADS", "6"))
T0 = time.time()
for d in (OUT, CACHE, f"{OUT}/plots", f"{OUT}/field", f"{OUT}/lc"): os.makedirs(d, exist_ok=True)

# ------------------------------------------------------------------ every HTTP call times out (pyvo, skypatrol, requests)
_orig_request = requests.Session.request
def _timed_request(self, method, url, **k):
    k.setdefault("timeout", NET_TIMEOUT); return _orig_request(self, method, url, **k)
requests.Session.request = _timed_request
import pyvo  # noqa: E402
from astropy.table import Table  # noqa: E402

LOGF = open(f"{OUT}/vet2_log.txt", "a"); _LL = threading.Lock()
def log(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(map(str, a))
    with _LL: print(s, flush=True); LOGF.write(s + "\n"); LOGF.flush()

IRSA = "https://irsa.ipac.caltech.edu/TAP"
GAIA = "https://gea.esac.esa.int/tap-server/tap"
SIMBAD = os.environ.get("SIMBAD_TAP", "https://simbad.idia.ac.za/simbad/sim-tap")
ZP = {"W1": 309.54, "W2": 171.787}; LAM = {"W1": 3.35e-6, "W2": 4.60e-6}

YOUNG_TYPES = {"Y*O", "Y*?", "TT*", "TT?", "Or*", "Ae*", "Ae?", "pr*", "pr?", "YSO", "TTS", "Y*O?", "FU*"}
CV_TYPES = {"CV*", "NL*", "DN*", "No*", "XB*", "LXB", "HXB", "CV"}
EB_TYPES = {"EB*", "EB", "Al*", "bL*", "WU*"}                       # confirmed eclipsing binaries; '?' variants are notes only
SB_TYPES = {"SB*", "El*", "**"}                                      # other binaries: flags, not kills
GAL_TYPES = {"G", "GiG", "GiC", "GiP", "BiC", "IG", "PaG", "SBG", "H2G", "EmG", "AGN", "QSO", "Sy1", "Sy2", "SyG", "BLL",
             "Bla", "LIN", "rG", "LSB", "bCG", "GrG", "CGG", "ClG", "SCG"}
GAL_Q = {"G?", "Q?", "AG?", "Bz?", "BL?", "C?G", "Gr?", "Sy?", "rG?"}
CAND_Q = {"CV?", "EB?", "No?", "XB?", "SB?"}

CONTROLS = [dict(name="ASASSN-21qj", ra=123.847042, dec=-38.989833, det="D1", expect="survive; SIMBAD counterpart"),
            dict(name="J060000", ra=90.00308, dec=-31.00781, det="D1", expect="survive; optical dip in ASAS-SN"),
            dict(name="V836 Tau", ra=75.77750987, dec=25.38870272, det="D2", gaia_id=3420008412568724736, expect="flagged young")]

# ------------------------------------------------------------------ cache, retry, TAP
def _key(*parts): return hashlib.sha1(json.dumps(parts, default=str, sort_keys=True).encode()).hexdigest()
def cached(key, fn):
    p = os.path.join(CACHE, key + ".pkl")
    if os.path.exists(p):
        try: return pickle.load(open(p, "rb"))
        except Exception: pass
    v = fn()
    try:
        tmp = p + f".{threading.get_ident()}"; pickle.dump(v, open(tmp, "wb")); os.replace(tmp, p)
    except Exception: pass
    return v

def retry(fn, tries=3, wait=8, what=""):
    err = None
    for k in range(tries):
        try: return fn()
        except Exception as e:
            err = e; log(f"  retry {k + 1}/{tries} {what}: {repr(e)[:160]}"); time.sleep(wait * (k + 1))
    raise RuntimeError(f"{what}: {repr(err)[:300]}")

def tap(url, q, uploads=None, maxrec=500000, tries=3, wait=8):
    up_sig = None
    if uploads: up_sig = {k: [list(map(str, v[c])) for c in v.colnames] for k, v in uploads.items()}
    def run():
        svc = pyvo.dal.TAPService(url)
        return svc.run_sync(q, uploads=uploads, maxrec=maxrec).to_table().to_pandas()
    return cached(_key("tap", url, q, up_sig, maxrec), lambda: retry(run, tries, wait, what=url.split("/")[2]))

def cone(ra, dec, r_arcsec, racol="ra", deccol="dec"):
    return f"CONTAINS(POINT('ICRS', {racol}, {deccol}), CIRCLE('ICRS', {ra}, {dec}, {r_arcsec / 3600.0})) = 1"

def offs(ra, dec, ra0, dec0):
    """tangent-plane-ish offsets in arcsec (small fields)"""
    return ((np.asarray(ra, float) - ra0 + 540) % 360 - 180) * np.cos(np.radians(dec0)) * 3600, (np.asarray(dec, float) - dec0) * 3600

def fnum(x, f="%.3f"):
    if x is None: return "n/a"
    try:
        x = float(x)
        return "nan" if not np.isfinite(x) else f % x
    except Exception: return str(x)

# ------------------------------------------------------------------ hunt.py (imported read-only; run in a work dir per pool)
def import_hunt(pool):
    work = os.path.join(HERE, "work", pool); os.makedirs(work, exist_ok=True); os.chdir(work)
    os.environ["POOL"] = pool
    sys.path.insert(0, GI)
    import hunt  # noqa
    return hunt

def merge_scores(dirs):
    parts = []
    for p in dirs:
        f = os.path.join(p, "scores.csv")
        if os.path.exists(f):
            try: parts.append(pd.read_csv(f)); log("read", f, len(parts[-1]))
            except Exception as e: log("unreadable", f, repr(e)[:100])
        else: log("MISSING", f)
    if not parts: return pd.DataFrame(columns=["uid", "score"])
    s = pd.concat(parts, ignore_index=True)
    s["fin"] = np.isfinite(s.score); s = s.sort_values("fin").drop_duplicates("uid", keep="last").drop(columns="fin")
    log("merged unique uids", len(s)); return s

def d1_cut(d): return d[(d.score > 8) & (d.redden > 0.05) & (d.nvis >= 2)].sort_values("score", ascending=False)

def d2_select(d):
    """detector-2 'excess + variability' selection exactly as vet/vet.py and LOG.md (2026-11-20 blind-spot entry)"""
    field = d[np.isfinite(d.score) & (d.cluster.astype(str) == "field")]
    f2 = field[np.isfinite(field.base_w1w2) & np.isfinite(field.bprp) & (field.base_w1 > 8)].copy()
    edges = np.arange(0.55, 2.2501, 0.05); mids, med, sig = [], [], []
    for a, b in zip(edges[:-1], edges[1:]):
        x = f2.base_w1w2[(f2.bprp >= a) & (f2.bprp < b)]
        if len(x) >= 50: mids.append((a + b) / 2); m = np.median(x); med.append(m); sig.append(max(1.4826 * np.median(np.abs(x - m)), 0.01))
    if len(mids) < 2: log("D2: too few scored stars for a locus", len(f2)); return f2.iloc[:0]
    f2["exc"] = f2.base_w1w2 - np.interp(f2.bprp, mids, med); f2["z"] = f2.exc / np.interp(f2.bprp, mids, sig)
    jb = np.arange(4.0, 15.01, 0.5); jmid, jmed = [], []
    for a, b in zip(jb[:-1], jb[1:]):
        x = f2.jitter[(f2.base_w2 >= a) & (f2.base_w2 < b)]
        if len(x) >= 50: jmid.append((a + b) / 2); jmed.append(np.median(x))
    if len(jmid) < 2: log("D2: too few stars for the jitter reference"); return f2.iloc[:0]
    f2["jr"] = f2.jitter / np.interp(f2.base_w2, jmid, jmed)
    pd.DataFrame(dict(bprp=mids, locus_w1w2=med, sigma=sig)).to_csv(f"{OUT}/d2_locus.csv", index=False)
    A = f2[(f2.exc > 0.10) & (f2.z > 5)]; log("D2 stage A (excess):", len(A), "of", len(f2), "| with jitter > 3x:", int((A.jr > 3).sum()))
    return A[A.jr > 3].sort_values("z", ascending=False)

def build_targets():
    T = []
    if MODE in ("near", "far"):
        pool_name = MODE
        dirs = os.environ.get("SHARD_DIRS", " ".join(f"/tmp/{'s' if MODE == 'near' else 'f'}{i}" for i in range(4))).split()
        s = merge_scores(dirs)
        try:
            hunt = import_hunt(pool_name)
            pool = hunt.build_pool().to_pandas(); log("pool", pool_name, len(pool))
            d = s.merge(pool, on="uid", how="left")
        except Exception as e:
            log("POOL FAILED", repr(e)[:300]); d = s.assign(ra=np.nan, dec=np.nan, bprp=np.nan, source_id=np.nan, cluster="?")
        c1 = d1_cut(d[np.isfinite(d.score)]); log("D1 candidates:", len(c1))
        for x in c1.itertuples():
            if not np.isfinite(x.ra): log("D1 uid without position (pool mismatch):", x.uid); continue
            T.append(dict(name=f"uid{x.uid}", det="D1", label="D1", uid=int(x.uid), ra=x.ra, dec=x.dec,
                          gaia_id=int(x.source_id) if np.isfinite(x.source_id) and x.source_id > 0 else None,
                          score_stored=x.score, cluster=str(x.cluster)))
        if MODE == "near":
            d2 = pd.read_csv(os.path.join(GI, "blindspot", "d2_excess_variability_near.csv"))
        else:
            d2 = d2_select(d) if "base_w1w2" in d else pd.DataFrame()
            d2.to_csv(f"{OUT}/d2_far_selection.csv", index=False)
        for x in d2.itertuples():
            T.append(dict(name=f"uid{x.uid}", det="D2", label="D2", uid=int(x.uid), ra=x.ra, dec=x.dec,
                          gaia_id=int(x.source_id) if np.isfinite(x.source_id) else None, score_stored=x.score,
                          d2_exc=x.exc, d2_z=x.z, d2_jr=x.jr, cluster="field"))
    elif MODE == "list":
        L = pd.read_csv(os.environ.get("LIST_CSV", os.path.join(HERE, "list.csv")))
        for x in L.itertuples():
            T.append(dict(name=str(x.name), det="LIST", label="LIST", ra=float(x.ra), dec=float(x.dec)))
    else: raise SystemExit(f"unknown TARGETS={MODE}")
    T = T[:NMAX]
    # controls; merge with a target at the same position (within 3")
    for c in CONTROLS:
        hit = None
        for t in T:
            dx, dy = offs(t["ra"], t["dec"], c["ra"], c["dec"])
            if math.hypot(float(dx), float(dy)) < 3: hit = t; break
        if hit is not None:
            hit["label"] = "CONTROL+" + hit["label"]; hit["control"] = c["name"]; hit["expect"] = c["expect"]
            hit["name"] = f"{c['name']} ({hit['name']})"
            if c.get("gaia_id"): hit["gaia_id"] = c["gaia_id"]
        else:
            T.append(dict(name=c["name"], det=c["det"], label="CONTROL", control=c["name"], expect=c["expect"], ra=c["ra"],
                          dec=c["dec"], gaia_id=c.get("gaia_id")))
    # de-duplicate D1/D2 overlaps
    out, seen = [], []
    for t in T:
        dup = [u for u in seen if math.hypot(*map(float, offs(t["ra"], t["dec"], u["ra"], u["dec"]))) < 2]
        if dup:
            u = dup[0]; u["label"] = u["label"] + "+" + t["label"]
            if t["det"] == "D2": u["det"] = "D2" if u["det"] == "D2" else u["det"]
            for k, v in t.items(): u.setdefault(k, v)
            continue
        seen.append(t); out.append(t)
    log("targets:", len(out)); return out

# ------------------------------------------------------------------ NEOWISE
NEOCOLS = "n.mjd, n.ra, n.dec, n.w1mpro, n.w1sigmpro, n.w2mpro, n.w2sigmpro, n.w1rchi2, n.w2rchi2, n.cc_flags"
def neowise_batch(T, goodq):
    """raw single-exposure photometry for all targets: synchronous upload joins of <= 60 targets (IRSA works best so)"""
    raw = {}
    for i in range(0, len(T), 60):
        sub = T[i:i + 60]
        up = Table({"objid": np.arange(i, i + len(sub)), "tra": np.array([t["ra"] for t in sub], float),
                    "tdec": np.array([t["dec"] for t in sub], float)})
        q = (f"SELECT t.objid, {NEOCOLS} FROM TAP_UPLOAD.targets AS t, neowiser_p1bs_psd AS n WHERE "
             "CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', t.tra, t.tdec, 0.000833)) = 1 AND " + goodq)
        try:
            r = tap(IRSA, q, uploads={"targets": up}, maxrec=3000000, tries=2, wait=30)
            for j, t in enumerate(sub): raw[t["name"]] = r[r.objid == i + j].drop(columns="objid").reset_index(drop=True)
            log("NEOWISE upload join", i, "->", len(r), "rows")
        except Exception as e: log("NEOWISE upload join failed, per-target cones later:", repr(e)[:200])
    return raw

def neowise_cone(t, goodq):
    q = (f"SELECT {NEOCOLS} FROM neowiser_p1bs_psd AS n WHERE "
         f"CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', {t['ra']}, {t['dec']}, 0.000833)) = 1 AND " + goodq)
    return tap(IRSA, q, maxrec=50000)

def visit_groups(raw):
    """identical to hunt.visits: sort by mjd, split at gaps > 30 d, keep groups with >= 5 points"""
    m = raw.mjd.to_numpy(float); o = np.argsort(m); raw = raw.iloc[o].reset_index(drop=True); m = m[o]
    cuts = np.where(np.diff(m) > 30)[0] + 1
    return raw, [s for s in np.split(np.arange(len(m)), cuts) if len(s) >= 5]

def onset_index(V, sc):
    """visit index k of the first visit after the infrared onset"""
    n = len(V)
    if n < 2: return None
    if sc and sc.get("dW2", 0) > 0.03 and n >= 5:
        b2 = np.median(V[:3, 3]); D2 = b2 - V[:, 3]; h = 0.5 * sc["dW2"]
        for i in range(3, n):
            if D2[i] > h and (i == n - 1 or D2[i + 1] > h): return i
    st = V[:-1, 3] - V[1:, 3]  # brightening between consecutive visits
    return int(np.argmax(st)) + 1

# ------------------------------------------------------------------ field control
def field_control(t, r, raw, groups, k):
    if k is None or k < 1 or k > len(groups) - 1: r["missing"].append("field control (no onset bracket)"); return
    idx = list(range(max(k - 2, 0), k)) + list(range(k, min(k + 2, len(groups))))
    wins = [(raw.mjd.iloc[groups[i]].min() - 2, raw.mjd.iloc[groups[i]].max() + 2, i >= k) for i in idx]
    m0, m1 = wins[0][0], wins[-1][1]
    cond = (f"n.mjd BETWEEN {m0:.4f} AND {m1:.4f} AND n.w2mpro BETWEEN 8.5 AND 12.5 AND n.w1snr > 10 AND n.nb = 1 AND n.qual_frame > 0 "
            "AND n.qi_fact > 0.9 AND n.saa_sep > 5 AND n.moon_masked = '00'")
    f = None
    try:
        # neighbours = AllWISE sources within 12' with W2 8.3-12.7; their NEOWISE detections come from synchronous upload joins of
        # <= 60 positions (a 12' NEOWISE cone over all epochs regularly exceeds 3-5 minutes at IRSA)
        aw = tap(IRSA, "SELECT ra, dec, w2mpro FROM allwise_p3as_psd WHERE " + cone(t["ra"], t["dec"], 720) + " AND w2mpro BETWEEN 8.3 AND 12.7")
        ax, ay = offs(aw.ra, aw.dec, t["ra"], t["dec"]); aw = aw.assign(sep=np.hypot(ax, ay))
        aw = aw[aw.sep > 3].sort_values("sep").head(int(os.environ.get("FIELD_MAX", "240"))).reset_index(drop=True)
        parts = []
        for i in range(0, len(aw), 60):
            up = Table({"aid": np.arange(i, min(i + 60, len(aw))), "ara": aw.ra.values[i:i + 60].astype(float), "adec": aw.dec.values[i:i + 60].astype(float)})
            q = ("SELECT t.aid, n.mjd, n.ra, n.dec, n.w1mpro, n.w2mpro, n.cc_flags FROM TAP_UPLOAD.a AS t, neowiser_p1bs_psd AS n WHERE "
                 "CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', t.ara, t.adec, 0.000556)) = 1 AND " + cond)
            parts.append(tap(IRSA, q, uploads={"a": up}, maxrec=2000000, tries=3, wait=20))
        f = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=["aid", "mjd", "ra", "dec", "w1mpro", "w2mpro", "cc_flags"])
        f = f.rename(columns={"aid": "key"}); src = f"AllWISE anchors + upload joins ({len(aw)} anchors)"
    except Exception as e:
        r["errors"].append(f"field upload joins: {repr(e)[:150]}; falling back to a 12' cone")
    if f is None:
        q = ("SELECT n.mjd, n.ra, n.dec, n.w1mpro, n.w2mpro, n.cc_flags FROM neowiser_p1bs_psd AS n WHERE "
             f"CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', {t['ra']}, {t['dec']}, 0.2)) = 1 AND " + cond)
        f = tap(IRSA, q, maxrec=2000000, tries=2, wait=20)
        fx, fy = offs(f.ra, f.dec, t["ra"], t["dec"])
        f["key"] = (np.round(fx / 3).astype(int) * 100000 + np.round(fy / 3).astype(int)); src = "12' cone, 3-arcsec grid"
    f = f[f.cc_flags.astype(str).str[:2] == "00"].reset_index(drop=True)
    side = np.full(len(f), -1)
    for a, b, after in wins: side[((f.mjd >= a) & (f.mjd <= b)).to_numpy()] = int(after)
    f = f[side >= 0].assign(after=side[side >= 0])
    fx, fy = offs(f.ra, f.dec, t["ra"], t["dec"]); f = f.assign(fx=fx, fy=fy); tgt_anchor = set()
    rows = []
    for kk, g in f.groupby("key"):
        if kk in tgt_anchor or np.hypot(g.fx.median(), g.fy.median()) < 3: continue
        a, b = g[g.after == 0], g[g.after == 1]
        if len(a) >= 4 and len(b) >= 4:
            rows.append((g.ra.median(), g.dec.median(), g.w2mpro.median(), a.w2mpro.median() - b.w2mpro.median(), a.w1mpro.median() - b.w1mpro.median()))
    nb = pd.DataFrame(rows, columns=["ra", "dec", "w2", "dW2_step", "dW1_step"])
    nb.round(4).to_csv(f"{OUT}/field/{safe(t['name'])}.csv", index=False)
    # the target's own step from its raw points in the same windows (same definition)
    tb = np.concatenate([groups[i] for i in idx if i < k]); ta = np.concatenate([groups[i] for i in idx if i >= k])
    tstep = float(np.median(raw.w2mpro.iloc[tb]) - np.median(raw.w2mpro.iloc[ta]))
    r.update(fc_target_step=tstep, fc_target_step_w1=float(np.median(raw.w1mpro.iloc[tb]) - np.median(raw.w1mpro.iloc[ta])),
             fc_n=len(nb), fc_mjd0=m0, fc_mjd1=m1, fc_ident=src)
    if len(nb) < 5: r["missing"].append(f"field control (only {len(nb)} neighbours)"); return
    med = float(nb.dW2_step.median()); sig = max(1.4826 * float(np.median(np.abs(nb.dW2_step - med))), 0.005)
    r.update(fc_median=med, fc_sigma=sig, fc_max=float(nb.dW2_step.max()), fc_min=float(nb.dW2_step.min()),
             fc_z=(tstep - med) / sig, fc_rank=int((nb.dW2_step >= tstep).sum()) + 1)

# ------------------------------------------------------------------ centroid
def centroid(t, r, raw, groups, k, V, gaia_nb):
    tt, X, Y, EX, EY = [], [], [], [], []
    for s in groups:
        g = raw.iloc[s]; dx, dy = offs(g.ra, g.dec, t["ra"], t["dec"])
        tt.append(np.median(g.mjd)); X.append(np.median(dx)); Y.append(np.median(dy))
        EX.append(max(1.25 * np.median(np.abs(dx - np.median(dx))) / np.sqrt(len(s)), 0.01))
        EY.append(max(1.25 * np.median(np.abs(dy - np.median(dy))) / np.sqrt(len(s)), 0.01))
    tt, X, Y, EX, EY = map(np.array, (tt, X, Y, EX, EY)); x = (tt - tt.mean()) / 365.25
    def fit(A, y, e):
        w = 1 / e ** 2; cov = np.linalg.inv(A.T @ (A * w[:, None])); b = cov @ (A.T @ (w * y))
        chi = np.sum(w * (y - A @ b) ** 2) / max(len(y) - A.shape[1], 1); return b, cov * max(chi, 1.0), y - A @ b
    A1 = np.c_[np.ones_like(x), x]
    bx, _, rx = fit(A1, X, EX); by, _, ry = fit(A1, Y, EY)
    r["cen_tmjd"] = list(np.round(tt, 2)); r["cen_dx"] = list(np.round(rx, 4)); r["cen_dy"] = list(np.round(ry, 4))
    r["cen_ex"] = list(np.round(EX, 4)); r["cen_ey"] = list(np.round(EY, 4))
    r["pm_ra_wise"], r["pm_dec_wise"] = float(bx[1]), float(by[1])
    r["cen_rms"] = float(np.sqrt(np.mean(rx ** 2 + ry ** 2)))
    if k is None or k < 1 or k > len(tt) - 1 or len(tt) < 4: r["missing"].append("centroid jump (no onset bracket)"); return
    H = (tt >= tt[k] - 1).astype(float); A2 = np.c_[np.ones_like(x), x, H]
    cx, Cx, _ = fit(A2, X, EX); cy, Cy, _ = fit(A2, Y, EY)
    jx, jy, sx, sy = cx[2], cy[2], math.sqrt(Cx[2, 2]), math.sqrt(Cy[2, 2]); J = math.hypot(jx, jy)
    sj = math.sqrt((jx * sx) ** 2 + (jy * sy) ** 2) / J if J > 0 else max(sx, sy)
    pa = math.degrees(math.atan2(jx, jy)) % 360
    lo, hi = max(k - 1, 1), min(k + 1, len(tt) - 1)
    jumps = [math.hypot(rx[i] - rx[i - 1], ry[i] - ry[i - 1]) for i in range(lo, hi + 1)]
    r.update(cen_jump=J, cen_jump_err=sj, cen_jump_sig=J / sj, cen_jump_pa=pa, cen_max_consec_jump=float(max(jumps)))
    # direction to Gaia neighbours (within 10") and the shift expected if that neighbour had made the whole brightening
    dW2 = r.get("fc_target_step", r.get("dW2", np.nan))
    frac = 1 - 10 ** (-0.4 * dW2) if np.isfinite(dW2) and dW2 > 0 else np.nan
    toward, away, expect = [], [], []
    for nb in gaia_nb:
        d = abs((nb["pa"] - pa + 180) % 360 - 180)
        expect.append(f'{nb["sep"]:.1f}" G{nb["g"]:.1f}: {nb["sep"] * frac:.2f}"' if np.isfinite(frac) else "")
        if d < 45: toward.append(f'{nb["sep"]:.1f}" PA{nb["pa"]:.0f} G{nb["g"]:.1f} (angle {d:.0f} deg)')
        if d > 135 and nb["sep"] < 8: away.append(f'{nb["sep"]:.1f}" PA{nb["pa"]:.0f} G{nb["g"]:.1f}')
    r["cen_toward_nb"] = "; ".join(toward); r["cen_away_nb"] = "; ".join(away); r["cen_expected_shift_if_nb"] = "; ".join(e for e in expect if e)

# ------------------------------------------------------------------ AllWISE
def allwise(t, r):
    a = tap(IRSA, "SELECT designation, ra, dec, w1mpro, w1sigmpro, w1snr, w2mpro, w2sigmpro, w2snr, w3mpro, w3sigmpro, w3snr, "
            "w4mpro, w4sigmpro, w4snr, cc_flags, ext_flg, ph_qual FROM allwise_p3as_psd WHERE " + cone(t["ra"], t["dec"], 6))
    r["aw_n6"] = len(a)
    if not len(a): r["missing"].append("AllWISE (no source within 6\")"); return
    dx, dy = offs(a.ra, a.dec, t["ra"], t["dec"]); a = a.assign(sep=np.hypot(dx, dy)).sort_values("sep"); x = a.iloc[0]
    r.update(aw_name=str(x.designation).strip(), aw_sep=float(x.sep), aw_w1=float(x.w1mpro), aw_w2=float(x.w2mpro),
             aw_w3=float(x.w3mpro), aw_w4=float(x.w4mpro), aw_w3snr=float(x.w3snr), aw_w4snr=float(x.w4snr),
             aw_w1w2=float(x.w1mpro - x.w2mpro), aw_w2w3=float(x.w2mpro - x.w3mpro), aw_w3w4=float(x.w3mpro - x.w4mpro),
             aw_ext=int(x.ext_flg), aw_phq=str(x.ph_qual), aw_ccf=str(x.cc_flags))
    w12, w23, s3 = r["aw_w1w2"], r["aw_w2w3"], r["aw_w3snr"]
    if not (np.isfinite(s3) and s3 >= 5): cls = "W3 S/N < 5: no W2-W3 class" + ("; W1-W2 > 0.25" if w12 > 0.25 else "")
    elif w12 > 1.0 and w23 > 2.0: cls = "Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)"
    elif w12 > 0.25 and w23 > 1.0: cls = "Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)"
    elif w23 > 1.0: cls = "W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)"
    elif w23 > 0.5: cls = "weak W3 excess (0.5 < W2-W3 < 1.0)"
    else: cls = "photosphere-like (W2-W3 < 0.5)"
    r["aw_class"] = cls

# ------------------------------------------------------------------ Gaia DR3
_REF = {}
def gaia_reference():
    if "seq" in _REF: return _REF["seq"]
    g = tap(GAIA, "SELECT phot_g_mean_mag + 5*LOG10(parallax/100) AS mg, bp_rp FROM gaiadr3.gaia_source WHERE random_index < 40000000 "
            "AND parallax > 4 AND parallax_over_error > 20 AND ruwe < 1.4 AND bp_rp IS NOT NULL", maxrec=300000)
    e = np.arange(-0.2, 4.01, 0.1); mids, med, sig = [], [], []
    for a, b in zip(e[:-1], e[1:]):
        x = g.mg[(g.bp_rp >= a) & (g.bp_rp < b)]
        if len(x) >= 30: mids.append((a + b) / 2); m = np.median(x); med.append(m); sig.append(1.4826 * np.median(np.abs(x - m)))
    _REF["seq"] = (np.array(mids), np.array(med), np.array(sig), len(g)); return _REF["seq"]

def gaia(t, r):
    g = tap(GAIA, "SELECT source_id, ra, dec, phot_g_mean_mag AS g, bp_rp, parallax, parallax_error, pmra, pmdec, ruwe, "
            "ipd_frac_multi_peak, non_single_star, phot_variable_flag FROM gaiadr3.gaia_source WHERE " + cone(t["ra"], t["dec"], 10))
    dx, dy = offs(g.ra, g.dec, t["ra"], t["dec"]); g = g.assign(sep=np.hypot(dx, dy), pa=np.degrees(np.arctan2(dx, dy)) % 360).sort_values("sep")
    me = None
    if t.get("gaia_id") is not None and (g.source_id == t["gaia_id"]).any(): me = g[g.source_id == t["gaia_id"]].iloc[0]
    elif len(g) and g.sep.iloc[0] < 2.5: me = g.iloc[0]
    if me is None: r["missing"].append("Gaia counterpart"); r["gaia_nb_list"] = ""; return []
    r.update(gaia_id=int(me.source_id), gmag=float(me.g), bprp=float(me.bp_rp), plx=float(me.parallax), ruwe=float(me.ruwe),
             ipd_multi=float(me.ipd_frac_multi_peak), nss_flag=int(me.non_single_star), gaia_varflag=str(me.phot_variable_flag),
             gaia_sep=float(me.sep))
    nb = g[g.source_id != me.source_id]
    lst = [dict(sep=float(s.sep), pa=float(s.pa), g=float(s.g), dG=float(s.g - me.g)) for s in nb.itertuples()]
    r["gaia_n_nb10"] = len(lst)
    r["gaia_nb_list"] = "; ".join(f'{n["sep"]:.1f}" PA{n["pa"]:.0f} G{n["g"]:.2f} dG{n["dG"]:+.2f}' for n in lst)
    in6 = [n for n in lst if n["sep"] < 6 and np.isfinite(n["dG"])]
    r["gaia_nb6_min_dG"] = min([n["dG"] for n in in6], default=np.nan)
    sid = int(me.source_id)
    ap = tap(GAIA, f"SELECT teff_gspphot, logg_gspphot, mh_gspphot, ew_espels_halpha, ew_espels_halpha_flag, classprob_dsc_combmod_star "
             f"FROM gaiadr3.astrophysical_parameters WHERE source_id = {sid}")
    if len(ap):
        a = ap.iloc[0]; r.update(teff=float(a.teff_gspphot), logg=float(a.logg_gspphot), mh=float(a.mh_gspphot),
                                 ha_pew=float(a.ew_espels_halpha), ha_flag=str(a.ew_espels_halpha_flag))
    v = tap(GAIA, f"SELECT best_class_name, best_class_score FROM gaiadr3.vari_classifier_result WHERE source_id = {sid}")
    r["gaia_varclass"] = ";".join(f"{a.best_class_name}({a.best_class_score:.2f})" for a in v.itertuples())
    nss = []
    for tab in ("nss_two_body_orbit", "nss_acceleration_astro", "nss_non_linear_spectro", "nss_vim_fl"):
        n = tap(GAIA, f"SELECT COUNT(*) AS n FROM gaiadr3.{tab} WHERE source_id = {sid}")
        if int(n.n.iloc[0]) > 0: nss.append(tab)
    r["gaia_nss"] = ",".join(nss)
    for tab, col in (("qso_candidates", "gaia_qso_cand"), ("galaxy_candidates", "gaia_gal_cand")):
        n = tap(GAIA, f"SELECT COUNT(*) AS n FROM gaiadr3.{tab} WHERE source_id = {sid}"); r[col] = bool(int(n.n.iloc[0]))
    if np.isfinite(r["plx"]) and r["plx"] > 0 and np.isfinite(r["bprp"]):
        mids, med, sig, nref = gaia_reference(); r["abs_g"] = r["gmag"] + 5 * math.log10(r["plx"] / 100)
        r["seq_dMG"] = r["abs_g"] - float(np.interp(r["bprp"], mids, med)); r["seq_sigma"] = float(np.interp(r["bprp"], mids, sig))
        r["seq_note"] = ("above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)"
                         if r["seq_dMG"] < -0.75 else "below the sequence" if r["seq_dMG"] > 0.75 else "on the sequence")
    return lst

# ------------------------------------------------------------------ SIMBAD (IDIA mirror; no correlated subqueries)
def simbad_batch(T):
    up = Table({"idx": np.arange(len(T)), "tra": np.array([t["ra"] for t in T], float), "tdec": np.array([t["dec"] for t in T], float)})
    jn = "FROM TAP_UPLOAD.t AS t JOIN basic AS b ON CONTAINS(POINT('ICRS', b.ra, b.dec), CIRCLE('ICRS', t.tra, t.tdec, 10./3600)) = 1"
    b = tap(SIMBAD, "SELECT t.idx, b.oid, b.main_id, b.otype, DISTANCE(POINT('ICRS', b.ra, b.dec), POINT('ICRS', t.tra, t.tdec))*3600 AS sep " + jn,
            uploads={"t": up}, tries=4, wait=15)
    o = tap(SIMBAD, "SELECT t.idx, b.oid, o.otype AS anytype " + jn + " JOIN otypes AS o ON o.oidref = b.oid", uploads={"t": up}, tries=4, wait=15)
    oids = sorted(set(int(x) for x in b.oid))
    nref = {}
    for i in range(0, len(oids), 200):
        ids = ",".join(map(str, oids[i:i + 200]))
        n = tap(SIMBAD, f"SELECT b.oid, COUNT(h.oidbibref) AS nref FROM basic AS b JOIN has_ref AS h ON h.oidref = b.oid WHERE b.oid IN ({ids}) GROUP BY b.oid", tries=4, wait=15)
        nref.update({int(a): int(c) for a, c in zip(n.oid, n.nref)})
    res = {}
    for i, t in enumerate(T):
        bi = b[b.idx == i].sort_values("sep"); objs = []
        for x in bi.itertuples():
            types = sorted({str(y).strip() for y in o[(o.idx == i) & (o.oid == x.oid)].anytype} | {str(x.otype).strip()})
            objs.append(dict(main_id=str(x.main_id).strip(), otype=str(x.otype).strip(), types=types, sep=float(x.sep), nref=nref.get(int(x.oid), 0)))
        res[t["name"]] = objs
    log("SIMBAD batch:", len(b), "objects for", len(T), "targets")
    return res

def simbad_apply(t, r, objs):
    r["simbad_n10"] = len(objs)
    r["simbad"] = "; ".join(f'{o["main_id"]} [{o["otype"]}; {",".join(o["types"])}] {o["sep"]:.2f}" refs={o["nref"]}' for o in objs)
    c = [o for o in objs if o["sep"] < 3]
    r["simbad_found"] = bool(c)
    if c: r.update(simbad_main=c[0]["main_id"], simbad_otype=c[0]["otype"], simbad_types=",".join(c[0]["types"]), simbad_nref=c[0]["nref"])
    r["_simbad_objs"] = objs

# ------------------------------------------------------------------ ASAS-SN Sky Patrol, per-camera normalisation
_SP = {"fails": 0}
def _with_timeout(fn, sec):
    from concurrent.futures import ThreadPoolExecutor
    ex = ThreadPoolExecutor(1); f = ex.submit(fn)
    try: return f.result(timeout=sec)
    finally: ex.shutdown(wait=False)

def asassn_fetch(t):
    """one fresh SkyPatrolClient per target: the client keeps per-query state (self.index), so a shared client used from
    several threads mixes up catalogues and light curves (seen in run 44748576117)"""
    def run():
        if _SP["fails"] >= 6: raise RuntimeError("Sky Patrol skipped after 6 consecutive failures")
        try:
            from pyasassn.client import SkyPatrolClient
            def go():
                c = SkyPatrolClient(verbose=False)
                lc = c.cone_search(ra_deg=t["ra"], dec_deg=t["dec"], radius=10, units="arcsec", download=True, catalog="master_list")
                if lc is None: return pd.DataFrame(), pd.DataFrame()
                return lc.data.copy(), lc.catalog_info.copy()
            data, cat = _with_timeout(go, 300)
        except Exception:
            _SP["fails"] += 1; raise
        _SP["fails"] = 0
        if len(cat):
            dx, dy = offs(cat.ra_deg, cat.dec_deg, t["ra"], t["dec"])
            if np.min(np.hypot(dx, dy)) > 10: raise RuntimeError(f"Sky Patrol returned a source {np.min(np.hypot(dx, dy)):.0f}\" away (mixed-up query)")
        return data, cat
    return cached(_key("asassn-v2", round(t["ra"], 6), round(t["dec"], 6)), lambda: retry(run, 2, 20, what="asas-sn"))

def asassn(t, r, t_on):
    data, cat = asassn_fetch(t)
    if not len(data): r["missing"].append("ASAS-SN (no source)"); return None
    dx, dy = offs(cat.ra_deg, cat.dec_deg, t["ra"], t["dec"]); cat = cat.assign(sep=np.hypot(dx, dy)).sort_values("sep")
    sid = cat.asas_sn_id.iloc[0]; r["asn_id"] = str(sid); r["asn_sep"] = float(cat.sep.iloc[0]); r["asn_n_sources10"] = len(cat)
    d = data[data.asas_sn_id == sid].copy()
    d["mjd"] = d.jd.astype(float) - 2400000.5
    good = np.isfinite(d.mag.astype(float)) & (d.mag_err.astype(float) < 0.15) & (d.mag_err.astype(float) > 0)
    if "quality" in d: good &= d.quality.astype(str) == "G"
    if "limit" in d: good &= d.mag.astype(float) < d.limit.astype(float)
    d = d[good].copy(); d["mag"] = d.mag.astype(float)
    if "phot_filter" not in d: d["phot_filter"] = "?"
    cams = []; d["nmag"] = np.nan; BIN = 120.0; t0 = d.mjd.min() if len(d) else 0
    for cam, g in d.groupby("camera"):
        if len(g) < 20: continue
        m0 = g.mag.median(); d.loc[g.index, "nmag"] = g.mag - m0
        g = g.assign(b=np.floor((g.mjd - t0) / BIN))
        bins = g.groupby("b").agg(t=("mjd", "median"), m=("mag", "median"), n=("mag", "size")); bins = bins[bins.n >= 5]
        row = dict(camera=str(cam), filt=str(g.phot_filter.iloc[0]), n=len(g), t_first=g.mjd.min(), t_last=g.mjd.max(), med=m0)
        if t_on is not None and np.isfinite(t_on):
            bef = bins[(bins.t < t_on) & (bins.t > t_on - 730)]; aft = bins[(bins.t >= t_on) & (bins.t < t_on + 730)]
            if len(bef) and len(aft):
                sc = 1.4826 * np.median(np.abs(bins.m - bins.m.median())) if len(bins) >= 3 else np.nan
                row.update(delta=float(aft.m.median() - bef.m.median()), nbef=len(bef), naft=len(aft), season_scatter=float(sc))
        cams.append(row)
    d = d[np.isfinite(d.nmag)]
    r["asn_npts"] = len(d); r["asn_cameras"] = "; ".join(f'{c["camera"]}({c["filt"]},{c["n"]}' + (f', d={c["delta"]:+.3f}' if "delta" in c else "") + ")" for c in cams)
    deltas = [c["delta"] for c in cams if "delta" in c]
    if deltas:
        r.update(asn_onset_delta=float(np.median(deltas)), asn_onset_ncam=len(deltas), asn_onset_nbright=int(sum(x < -0.01 for x in deltas)),
                 asn_onset_ndim=int(sum(x > 0.01 for x in deltas)), asn_onset_deltas=",".join(f"{x:+.3f}" for x in deltas))
    else: r["missing"].append("ASAS-SN change at onset (no camera spans the onset)")
    if len(d) >= 20:
        b = d.assign(b=np.floor((d.mjd - t0) / BIN)).groupby("b").agg(t=("mjd", "median"), m=("nmag", "median"), n=("nmag", "size"))
        b = b[b.n >= 10]
        if len(b):
            j = b.m.idxmax(); r.update(asn_max_dim=float(b.m.max() - b.m.median()), asn_max_dim_mjd=float(b.t[j]),
                                       asn_season_rms=float(1.4826 * np.median(np.abs(b.m - b.m.median()))))
    pd.DataFrame(cams).to_csv(f"{OUT}/lc/{safe(t['name'])}_asassn_cameras.csv", index=False)
    d[["mjd", "camera", "phot_filter", "mag", "mag_err", "nmag"]].to_csv(f"{OUT}/lc/{safe(t['name'])}_asassn.csv", index=False)
    return d

# ------------------------------------------------------------------ dust temperature from the W1/W2 excess-flux ratio
def bb_ratio(T):
    h, c, k = 6.62607015e-34, 2.99792458e8, 1.380649e-23
    n1, n2 = c / LAM["W1"], c / LAM["W2"]
    return (n1 ** 3 / np.expm1(h * n1 / (k * T))) / (n2 ** 3 / np.expm1(h * n2 / (k * T)))
TG = np.logspace(np.log10(150), np.log10(8000), 600); RG = bb_ratio(TG)
def ratio_to_T(R):
    R = np.asarray(R, float); out = np.interp(R, RG, TG, left=np.nan, right=np.nan)
    out[R <= RG[0]] = TG[0]; out[R >= RG[-1]] = TG[-1]; return out

def dust_T(r, V, k):
    if k is None or k < 1: return
    bef, aft = V[:k], V[k:k + 2]
    def F(m, band): return ZP[band] * 10 ** (-0.4 * m)
    b1, b2, a1, a2 = np.median(bef[:, 1]), np.median(bef[:, 3]), np.median(aft[:, 1]), np.median(aft[:, 3])
    e = lambda x: np.sqrt(np.sum(x ** 2)) / len(x)
    eb1, eb2, ea1, ea2 = e(bef[:, 2]), e(bef[:, 4]), e(aft[:, 2]), e(aft[:, 4])
    dF1, dF2 = F(a1, "W1") - F(b1, "W1"), F(a2, "W2") - F(b2, "W2")
    r.update(exc_mJy_W1=dF1 * 1e3, exc_mJy_W2=dF2 * 1e3)
    if dF2 <= 0: r["dust_T_note"] = "no W2 excess flux after onset"; return
    rng = np.random.default_rng(1); N = 2000
    s1 = F(a1 + rng.normal(0, max(ea1, 0.005), N), "W1") - F(b1 + rng.normal(0, max(eb1, 0.005), N), "W1")
    s2 = F(a2 + rng.normal(0, max(ea2, 0.005), N), "W2") - F(b2 + rng.normal(0, max(eb2, 0.005), N), "W2")
    Ts = ratio_to_T(np.where(s2 > 0, s1 / np.where(s2 > 0, s2, 1), np.nan)); Ts = Ts[np.isfinite(Ts)]
    r["dust_ratio"] = dF1 / dF2; r["dust_T"] = float(ratio_to_T([dF1 / dF2])[0])
    if len(Ts) > 100: r["dust_T_lo"], r["dust_T_hi"] = map(float, np.percentile(Ts, [16, 84]))
    if r["dust_T"] <= TG[0] * 1.01: r["dust_T_note"] = f"W1 excess <= 0: colder than ~{TG[0]:.0f} K (upper limit)"
    if r["dust_T"] >= TG[-1] * 0.99: r["dust_T_note"] = "ratio bluer than an 8000 K blackbody (not dust-like)"

# ------------------------------------------------------------------ verdict
def verdict(r):
    kills, flags, young = [], [], []
    det, lab = r.get("det"), r.get("label", "")
    step_target = det in ("D1", "LIST")
    if step_target and np.isfinite(r.get("fc_z", np.nan)) and r["fc_z"] < 5:
        kills.append(f"field control: target step {r['fc_target_step']:+.3f} mag vs neighbours median {r['fc_median']:+.3f}, robust sigma "
                     f"{r['fc_sigma']:.3f}, max {r['fc_max']:+.3f} (N={r['fc_n']}): z = {r['fc_z']:.1f} < 5")
    if r.get("cen_jump_sig", 0) > 3 and r.get("cen_toward_nb"):
        kills.append(f"centroid jump {r['cen_jump']:.3f}\" ({r['cen_jump_sig']:.1f} sigma) at the onset toward a neighbour: {r['cen_toward_nb']}")
    elif r.get("cen_jump_sig", 0) > 3:
        why = (f"away from the neighbour(s) {r['cen_away_nb']}, as expected when the target itself brightens in a blended WISE PSF"
               if r.get("cen_away_nb") else "not toward a Gaia neighbour")
        flags.append(f"centroid jump {r['cen_jump']:.3f}\" ({r['cen_jump_sig']:.1f} sigma, PA {r['cen_jump_pa']:.0f}) {why}")
    if np.isfinite(r.get("gaia_nb6_min_dG", np.nan)) and r["gaia_nb6_min_dG"] < 3:
        kills.append(f"blend: Gaia neighbour within 6\" only {r['gaia_nb6_min_dG']:.2f} mag fainter in G ({r['gaia_nb_list']})")
    w1 = r.get("base_w1", np.nan)
    if not np.isfinite(w1): w1 = r.get("aw_w1", np.nan)
    if np.isfinite(w1) and w1 < 8: kills.append(f"W1 saturation: baseline W1 {w1:.2f} < 8")
    objs = r.get("_simbad_objs", [])
    near5 = [o for o in objs if o["sep"] < 5]; cp = [o for o in objs if o["sep"] < 3]
    yt = sorted({ty for o in near5 for ty in o["types"]} & YOUNG_TYPES)
    if yt: young.append(f"SIMBAD young-star types {','.join(yt)} ({'; '.join(o['main_id'] for o in near5 if set(o['types']) & YOUNG_TYPES)})")
    if "YSO" in str(r.get("gaia_varclass", "")): young.append(f"Gaia DR3 variability class {r['gaia_varclass']}")
    ct = sorted({ty for o in cp for ty in o["types"]})
    if set(ct) & CV_TYPES: kills.append(f"cataclysmic variable / X-ray binary in SIMBAD ({','.join(sorted(set(ct) & CV_TYPES))}, {cp[0]['main_id']})")
    if set(ct) & SB_TYPES: flags.append(f"binary type in SIMBAD ({','.join(sorted(set(ct) & SB_TYPES))}, {cp[0]['main_id']})")
    if set(ct) & EB_TYPES: kills.append(f"eclipsing binary in SIMBAD ({','.join(sorted(set(ct) & EB_TYPES))}, {cp[0]['main_id']})")
    gal = [o for o in objs if o["sep"] < 6 and set(o["types"]) & GAL_TYPES]
    if gal: kills.append("galaxy/QSO within 6\" in SIMBAD: " + "; ".join(f'{o["main_id"]} [{",".join(sorted(set(o["types"]) & GAL_TYPES))}] {o["sep"]:.1f}"' for o in gal))
    if r.get("gaia_qso_cand"): flags.append("in the Gaia DR3 QSO candidate table (low purity)")
    if r.get("gaia_gal_cand"): flags.append("in the Gaia DR3 galaxy candidate table (low purity)")
    q = sorted(set(ct) & (CAND_Q | GAL_Q))
    if q: flags.append(f"SIMBAD candidate type(s) {','.join(q)} ({cp[0]['main_id']}): uncertain, not a kill")
    if r.get("aw_ext", 0) == 1: flags.append("AllWISE ext_flg = 1 (extended or 2MASS XSC association)")
    if r.get("ruwe", 0) > 1.4: flags.append(f"Gaia RUWE {r['ruwe']:.2f} > 1.4 (possible unresolved companion)")
    if r.get("gaia_nss"): flags.append(f"Gaia DR3 NSS solution: {r['gaia_nss']}")
    if r.get("ipd_multi", 0) > 10: flags.append(f"Gaia ipd_frac_multi_peak {r['ipd_multi']:.0f}% (resolved double?)")
    if r.get("seq_dMG", 0) < -0.75: flags.append(f"{-r['seq_dMG']:.2f} mag above the main sequence at its colour")
    if r.get("aw_class", "").startswith("Class"): flags.append(f"AllWISE 2010 {r['aw_class']}")
    # optical brightening together with the infrared rise
    if step_target or det == "D2":
        dlt = r.get("asn_onset_delta", np.nan); nc = r.get("asn_onset_ncam", 0)
        if np.isfinite(dlt) and dlt < -0.015 and nc >= 2 and r.get("asn_onset_nbright", 0) >= 2 and r.get("asn_onset_ndim", 0) == 0:
            flags.append(f"not plain dust: optical brightening {dlt:+.3f} mag (per-camera {r.get('asn_onset_deltas')}) together with the infrared rise")
        elif np.isfinite(dlt) and nc == 1 and dlt < -0.03:
            flags.append(f"possible optical brightening at onset ({dlt:+.3f} mag, one camera only)")
        if np.isfinite(dlt) and dlt > 0.05 and r.get("asn_onset_nbright", 0) == 0:
            flags.append(f"optical dimming {dlt:+.3f} mag after the infrared onset (debris transit signature)")
    if np.isfinite(r.get("asn_max_dim", np.nan)) and r["asn_max_dim"] > 0.1:
        flags.append(f"largest seasonal optical dimming {r['asn_max_dim']:.2f} mag (MJD {r['asn_max_dim_mjd']:.0f})")
    if r.get("score_reproduced") is False: flags.append(f"stored score {r['score_stored']:.2f} not reproduced on refetch ({r.get('score_refetch', np.nan):.2f})")
    if young and det != "D2": kills.append("young star (" + "; ".join(young) + "): disk variability expected, not an afterglow candidate")
    cat = "KILLED" if kills else "YOUNG" if young else "SURVIVOR"
    return cat, kills, flags, young

# ------------------------------------------------------------------ per target
def safe(s): return re.sub(r"[^A-Za-z0-9_.+-]+", "_", s)[:60]

def vet_one(t, ctx):
    r = dict(t); r["errors"] = []; r["missing"] = []
    if time.time() - T0 > DEADLINE: r["errors"].append("SKIPPED: deadline"); return finish(r)
    def step(name, fn):
        try: return fn()
        except Exception as e:
            r["errors"].append(f"{name}: {repr(e)[:200]}"); r["missing"].append(name); log(" ", t["name"], name, "FAILED", repr(e)[:150]); return None
    gaia_nb = step("gaia", lambda: gaia(t, r)) or []
    step("allwise", lambda: allwise(t, r))
    if ctx["simbad"] is not None: simbad_apply(t, r, ctx["simbad"].get(t["name"], []))
    else:
        objs = step("simbad", lambda: simbad_batch([t])[t["name"]])
        if objs is not None: simbad_apply(t, r, objs)
    raw = ctx["neo"].get(t["name"])
    if raw is None: raw = step("neowise", lambda: neowise_cone(t, ctx["goodq"]))
    V = groups = k = None; rawg = None
    if raw is not None:
        cc = raw.cc_flags.astype(str); ok = cc.map(lambda c: c[:2] in ("00", "0") or c == "0000") & np.isfinite(raw.w1mpro + raw.w2mpro)
        rawg = raw[ok].reset_index(drop=True); r["npts"] = len(rawg)
        if len(rawg) >= 10:
            rawg, groups = visit_groups(rawg)
            V = ctx["hunt_visits"](*(rawg[c].to_numpy(float) for c in ("mjd", "w1mpro", "w1sigmpro", "w2mpro", "w2sigmpro")))
            if len(V) != len(groups): r["errors"].append("visit grouping differs from hunt.visits"); groups = None
    if V is not None and len(V) >= 2:
        np.savetxt(f"{OUT}/lc/{safe(t['name'])}_visits.txt", V, fmt="%.5f", header="mjd w1 e1 w2 e2 n")
        sc = ctx["hunt_score"](V) if len(rawg) >= 30 else None
        if sc:
            r.update(score_refetch=sc["score"], dW2=sc["dW2"], dW1=sc["dW1"], redden=sc["redden"], nvis=sc["nvis"], base_w1=sc["base_w1"],
                     base_w2=sc["base_w2"], base_w1w2=sc["base_w1w2"], jitter=sc["jitter"], start=sc["start"])
        r["n_visits"] = len(V)
        if np.isfinite(r.get("score_stored", np.nan)) and sc:
            r["score_reproduced"] = bool(abs(sc["score"] - r["score_stored"]) <= max(0.5, 0.1 * abs(r["score_stored"])))
        k = onset_index(V, sc)
        if k is not None:
            r["onset_k"] = k; r["onset_mjd"] = float((V[k - 1, 0] + V[k, 0]) / 2); r["onset_before_mjd"] = float(V[k - 1, 0]); r["onset_after_mjd"] = float(V[k, 0])
            r["onset_dW2_visits"] = float(np.median(V[max(k - 2, 0):k, 3]) - np.median(V[k:k + 2, 3]))
        if groups is not None:
            step("field control", lambda: field_control(t, r, rawg, groups, k))
            step("centroid", lambda: centroid(t, r, rawg, groups, k, V, gaia_nb))
        step("dust T", lambda: dust_T(r, V, k))
    else: r["missing"].append("NEOWISE light curve")
    asn = None
    if DO_ASASSN: asn = step("asas-sn", lambda: asassn(t, r, r.get("onset_mjd")))
    else: r["missing"].append("ASAS-SN (disabled)")
    try: r["category"] = verdict(r)[0]
    except Exception: pass
    try: plot(r, V, rawg, asn)
    except Exception as e: r["errors"].append(f"plot: {repr(e)[:150]}")
    return finish(r)

def finish(r):
    try: cat, kills, flags, young = verdict(r)
    except Exception as e: cat, kills, flags, young = "ERROR", [], [f"verdict failed: {repr(e)[:150]}"], []
    r.update(category=cat, kill_reasons=" | ".join(kills), flags=" | ".join(flags), young_reasons=" | ".join(young), young=bool(young))
    r["errors"] = " || ".join(r["errors"])[:800]; r["missing"] = "; ".join(dict.fromkeys(r["missing"]))
    r.pop("_simbad_objs", None)
    log("vetted", r["name"], r["label"], "->", cat, "| kills:", r["kill_reasons"][:160], "| missing:", r["missing"][:120])
    return r

# ------------------------------------------------------------------ plot
def plot(r, V, raw, asn):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(5, 1, figsize=(7.5, 11), sharex=True, gridspec_kw=dict(height_ratios=[2, 2, 1.2, 2, 1.5]))
    ton = r.get("onset_mjd")
    if V is not None and len(V):
        if raw is not None and len(raw) < 20000:
            ax[0].plot(raw.mjd, raw.w1mpro, ".", c="C0", ms=1, alpha=0.25); ax[1].plot(raw.mjd, raw.w2mpro, ".", c="C1", ms=1, alpha=0.25)
        ax[0].errorbar(V[:, 0], V[:, 1], V[:, 2], fmt="o", c="C0", ms=3, label="W1 visit median")
        ax[1].errorbar(V[:, 0], V[:, 3], V[:, 4], fmt="s", c="C1", ms=3, label="W2 visit median")
        ax[2].errorbar(V[:, 0], V[:, 1] - V[:, 3], np.hypot(V[:, 2], V[:, 4]), fmt="ko", ms=3)
        for a, c in ((ax[0], 1), (ax[1], 3)):
            lo, hi = np.min(V[:, c]), np.max(V[:, c]); pad = max(0.05, 0.25 * (hi - lo)); a.set_ylim(hi + pad, lo - pad)
    if np.isfinite(r.get("aw_w1", np.nan)):
        ax[0].plot([55350], [r["aw_w1"]], "C0*", ms=9, label="AllWISE 2010"); ax[1].plot([55350], [r["aw_w2"]], "C1*", ms=9)
        ax[2].plot([55350], [r["aw_w1w2"]], "k*", ms=9)
    ax[0].set_ylabel("W1"); ax[1].set_ylabel("W2"); ax[2].set_ylabel("W1-W2"); ax[0].legend(fontsize=6); ax[1].legend(fontsize=6)
    if asn is not None and len(asn):
        for i, (cam, g) in enumerate(asn.groupby("camera")):
            gb = g.assign(b=np.floor(g.mjd / 60)).groupby("b").agg(t=("mjd", "median"), m=("nmag", "median"), n=("nmag", "size"))
            gb = gb[gb.n >= 3]
            ax[3].plot(g.mjd, g.nmag, ".", ms=1, alpha=0.25, c=f"C{i % 10}")
            ax[3].plot(gb.t, gb.m, "-o", ms=2, lw=0.8, c=f"C{i % 10}", label=f"{cam} ({g.phot_filter.iloc[0]})")
        lo, hi = np.nanpercentile(asn.nmag, [1, 99]); ax[3].set_ylim(hi + 0.05, lo - 0.05); ax[3].legend(fontsize=5, ncol=4)
    else: ax[3].text(0.5, 0.5, "no ASAS-SN data", transform=ax[3].transAxes, ha="center")
    ax[3].set_ylabel("ASAS-SN mag\n- camera median")
    if r.get("cen_tmjd"):
        tt = np.array(r["cen_tmjd"])
        ax[4].errorbar(tt, r["cen_dx"], r["cen_ex"], fmt="o", ms=3, label="dRA cos(dec) resid.")
        ax[4].errorbar(tt, r["cen_dy"], r["cen_ey"], fmt="s", ms=3, label="dDec resid.")
        ax[4].axhline(0, c="0.6", lw=0.5); ax[4].legend(fontsize=6)
    ax[4].set_ylabel("centroid\n(arcsec)"); ax[4].set_xlabel("MJD")
    if ton:
        for a in ax: a.axvline(ton, c="r", lw=0.8, ls="--")
    ax[0].set_title(f"{r['name']} [{r['label']}] {r.get('category', '')}  ra {r['ra']:.5f} dec {r['dec']:.5f}\n"
                    f"score {fnum(r.get('score_refetch'), '%.1f')}  field z {fnum(r.get('fc_z'), '%.1f')}  "
                    f"centroid jump {fnum(r.get('cen_jump_sig'), '%.1f')} sig  T {fnum(r.get('dust_T'), '%.0f')} K", fontsize=8)
    plt.tight_layout(); fn = f"{OUT}/plots/{safe(r['name'])}.png"; plt.savefig(fn, dpi=90); plt.close(); r["plot"] = os.path.relpath(fn, OUT)

# ------------------------------------------------------------------ outputs
COLS = ["category", "name", "label", "det", "control", "uid", "ra", "dec", "gaia_id", "gmag", "bprp", "plx", "ruwe", "ipd_multi", "nss_flag",
        "gaia_nss", "teff", "logg", "mh", "ha_pew", "gaia_varclass", "gaia_qso_cand", "gaia_gal_cand", "abs_g", "seq_dMG", "seq_note",
        "gaia_n_nb10", "gaia_nb6_min_dG", "gaia_nb_list", "score_stored", "score_refetch", "score_reproduced", "dW2", "dW1", "redden", "nvis",
        "n_visits", "npts", "base_w1", "base_w2", "base_w1w2", "d2_exc", "d2_z", "d2_jr", "onset_mjd", "onset_before_mjd", "onset_after_mjd",
        "onset_dW2_visits", "fc_target_step", "fc_target_step_w1", "fc_median", "fc_sigma", "fc_max", "fc_min", "fc_n", "fc_rank", "fc_z", "fc_ident",
        "cen_jump", "cen_jump_err", "cen_jump_sig", "cen_jump_pa", "cen_max_consec_jump", "cen_rms", "cen_toward_nb", "cen_away_nb", "cen_expected_shift_if_nb",
        "aw_name", "aw_sep", "aw_w1", "aw_w2", "aw_w3", "aw_w4", "aw_w1w2", "aw_w2w3", "aw_w3snr", "aw_w3w4", "aw_w4snr", "aw_ext", "aw_phq",
        "aw_ccf", "aw_class", "simbad_found", "simbad_main", "simbad_otype", "simbad_types", "simbad_nref", "simbad_n10", "simbad",
        "asn_id", "asn_sep", "asn_n_sources10", "asn_npts", "asn_cameras", "asn_onset_delta", "asn_onset_deltas", "asn_onset_ncam",
        "asn_onset_nbright", "asn_onset_ndim", "asn_max_dim", "asn_max_dim_mjd", "asn_season_rms", "exc_mJy_W1", "exc_mJy_W2", "dust_ratio",
        "dust_T", "dust_T_lo", "dust_T_hi", "dust_T_note", "young", "young_reasons", "kill_reasons", "flags", "missing", "errors", "plot"]

def control_checks(R):
    out = []
    for c in CONTROLS:
        x = [r for r in R if r.get("control") == c["name"]]
        if not x: out.append((c["name"], "NOT RUN", "")); continue
        r = x[0]
        if c["name"] == "ASASSN-21qj":
            ok = r["category"] == "SURVIVOR" and r.get("simbad_found") is True and np.isfinite(r.get("fc_z", np.nan)) and np.isfinite(r.get("cen_jump_sig", np.nan))
            why = f"category {r['category']}, SIMBAD {r.get('simbad_main')} ({r.get('simbad_nref')} refs), field z {fnum(r.get('fc_z'), '%.1f')}, missing: {r.get('missing') or 'none'}"
        elif c["name"] == "J060000":
            ok = r["category"] == "SURVIVOR" and r.get("asn_max_dim", 0) > 0.2
            why = f"category {r['category']}, largest ASAS-SN seasonal dimming {fnum(r.get('asn_max_dim'), '%.2f')} mag at MJD {fnum(r.get('asn_max_dim_mjd'), '%.0f')}"
        else:
            ok = bool(r.get("young")); why = f"young: {r.get('young_reasons')}"
        out.append((c["name"], "PASS" if ok else "FAIL", why))
    return out

def rank_key(r):
    cat = {"SURVIVOR": 0, "YOUNG": 1, "KILLED": 2}.get(r["category"], 3)
    z = r.get("fc_z", np.nan); s = r.get("score_refetch", np.nan)
    z = float(z) if z is not None and np.isfinite(z) else -1e9; s = float(s) if s is not None and np.isfinite(s) else -1e9
    return (cat, 1 if r.get("flags") else 0, -z, -s)

_WL = threading.Lock()
def write_outputs(R, final=False):
    with _WL:
        df = pd.DataFrame(R)
        for c in COLS:
            if c not in df: df[c] = np.nan
        df = df[COLS + [c for c in df.columns if c not in COLS and not c.startswith("cen_") or c in ("cen_tmjd",)]]
        R2 = sorted(R, key=rank_key); df = df.set_index("name").loc[[r["name"] for r in R2]].reset_index()
        df.drop(columns=[c for c in ("cen_tmjd",) if c in df]).to_csv(f"{OUT}/vet2_table.csv", index=False)
        with open(f"{OUT}/vet2_report.md", "w") as fh:
            fh.write(f"# vet2 report: {MODE} target list ({'final' if final else 'PARTIAL, run in progress'})\n\n")
            fh.write(f"Generated {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}; {len(R)} targets; machine-generated, the plots in plots/ "
                     "still need a look by eye.\n\n")
            fh.write("Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia "
                     "neighbour within 6\" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart "
                     "within 3\"); SIMBAD galaxy/QSO within 6\"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5\" or Gaia "
                     "variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not "
                     "kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 "
                     "mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.\n\n")
            fh.write("## Controls\n\n| Control | Result | Detail |\n|---|---|---|\n")
            for n, ok, why in control_checks(R): fh.write(f"| {n} | {ok} | {why} |\n")
            counts = pd.Series([r["category"] for r in R]).value_counts().to_dict()
            fh.write(f"\nCounts: {counts}\n\n")
            for cat, title in (("SURVIVOR", "Survivors"), ("YOUNG", "Known/likely young stars (detector 2)"), ("KILLED", "Killed"), ("ERROR", "Errors")):
                sub = [r for r in R2 if r["category"] == cat]
                if not sub: continue
                fh.write(f"## {title} ({len(sub)})\n\n")
                for r in sub: fh.write(entry(r))
    return df

def entry(r):
    g = lambda k, f="%.3f": fnum(r.get(k), f)
    s = f"### {r['name']}  [{r['label']}]  {r['category']}\n"
    s += f"- position {r['ra']:.5f} {r['dec']:+.5f}; Gaia DR3 {r.get('gaia_id', '?')}; G {g('gmag', '%.2f')}, BP-RP {g('bprp', '%.2f')}, plx {g('plx', '%.2f')} mas; plot `{r.get('plot', '')}`\n"
    if r.get("kill_reasons"): s += f"- **KILL:** {r['kill_reasons']}\n"
    if r.get("young_reasons"): s += f"- **young:** {r['young_reasons']}\n"
    if r.get("flags"): s += f"- flags: {r['flags']}\n"
    s += (f"- NEOWISE: score refetch {g('score_refetch', '%.2f')} (stored {g('score_stored', '%.2f')}, reproduced {r.get('score_reproduced', 'n/a')}); "
          f"dW2 {g('dW2')}, dW1 {g('dW1')}, {r.get('n_visits', '?')} visits, {r.get('npts', '?')} points; baseline W1 {g('base_w1', '%.2f')}, W1-W2 {g('base_w1w2')}; "
          f"onset between MJD {g('onset_before_mjd', '%.0f')} and {g('onset_after_mjd', '%.0f')}\n")
    if r.get("det") == "D2" and np.isfinite(r.get("d2_exc", np.nan)): s += f"- detector 2: excess {g('d2_exc')} mag, z {g('d2_z', '%.1f')}, jitter ratio {g('d2_jr', '%.1f')}\n"
    s += (f"- field control: target step {g('fc_target_step', '%+.3f')} (W1 {g('fc_target_step_w1', '%+.3f')}); neighbours N={r.get('fc_n', '?')}, median "
          f"{g('fc_median', '%+.3f')}, robust sigma {g('fc_sigma')}, max {g('fc_max', '%+.3f')}; z = {g('fc_z', '%.1f')}\n")
    s += (f"- centroid: jump at onset {g('cen_jump')}\" +- {g('cen_jump_err')} ({g('cen_jump_sig', '%.1f')} sigma, PA {g('cen_jump_pa', '%.0f')}); largest "
          f"consecutive-visit jump {g('cen_max_consec_jump')}\"; rms {g('cen_rms')}\"; toward neighbour: {r.get('cen_toward_nb') or 'none'}; "
          f"expected shift if a neighbour were the source: {r.get('cen_expected_shift_if_nb') or 'n/a'}\n")
    s += (f"- AllWISE 2010: W1-W2 {g('aw_w1w2')}, W2-W3 {g('aw_w2w3')} (W3 S/N {g('aw_w3snr', '%.1f')}), W3-W4 {g('aw_w3w4')} (W4 S/N {g('aw_w4snr', '%.1f')}), "
          f"ext_flg {r.get('aw_ext', '?')}, ph_qual {r.get('aw_phq', '?')}: {r.get('aw_class', 'n/a')}\n")
    s += (f"- Gaia: RUWE {g('ruwe', '%.2f')}, ipd_frac_multi_peak {g('ipd_multi', '%.0f')}, NSS {r.get('gaia_nss') or 'none'}, Teff {g('teff', '%.0f')} K, "
          f"logg {g('logg', '%.2f')}, H-alpha pEW {g('ha_pew', '%.3f')} nm, varclass {r.get('gaia_varclass') or 'none'}; M_G {g('abs_g', '%.2f')}, "
          f"{g('seq_dMG', '%+.2f')} mag vs sequence ({r.get('seq_note', 'n/a')}); neighbours within 10\": {r.get('gaia_nb_list') or 'none'}\n")
    s += f"- SIMBAD (10\"): {r.get('simbad') or 'no object'}\n"
    s += (f"- ASAS-SN: {r.get('asn_npts', 0)} points, cameras {r.get('asn_cameras', 'n/a')}; change at onset (after-before, per-camera median) "
          f"{g('asn_onset_delta', '%+.3f')} mag; largest seasonal dimming {g('asn_max_dim', '%.2f')} mag at MJD {g('asn_max_dim_mjd', '%.0f')}\n")
    s += (f"- dust: excess flux W1 {g('exc_mJy_W1', '%.2f')} mJy, W2 {g('exc_mJy_W2', '%.2f')} mJy, T = {g('dust_T', '%.0f')} K "
          f"(16-84%: {g('dust_T_lo', '%.0f')}-{g('dust_T_hi', '%.0f')}) {r.get('dust_T_note') or ''}\n")
    if r.get("missing"): s += f"- checks missing: {r['missing']}\n"
    if r.get("errors"): s += f"- errors: {r['errors'][:400]}\n"
    return s + "\n"

def main():
    log(f"vet2 start: TARGETS={MODE} OUT={OUT} CACHE={CACHE} ASASSN={DO_ASASSN}")
    T = build_targets()
    hunt = sys.modules.get("hunt") or import_hunt("near" if MODE != "far" else "far")
    json.dump(T, open(f"{OUT}/targets.json", "w"), indent=1, default=str)
    ctx = dict(goodq=hunt.GOODQ, hunt_visits=hunt.visits, hunt_score=hunt.score)
    try: ctx["simbad"] = simbad_batch(T)
    except Exception as e: log("SIMBAD batch failed; per-target cones:", repr(e)[:200]); ctx["simbad"] = None
    try: ctx["neo"] = neowise_batch(T, hunt.GOODQ)
    except Exception as e: log("NEOWISE batch failed:", repr(e)[:200]); ctx["neo"] = {}
    try: gaia_reference()
    except Exception as e: log("Gaia reference sequence failed:", repr(e)[:200])
    R = []
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(THREADS) as ex:
        futs = {ex.submit(vet_one, t, ctx): t for t in T}
        for f in as_completed(futs):
            t = futs[f]
            try: r = f.result()
            except Exception as e:
                r = finish(dict(t, errors=[f"target failed: {repr(e)[:300]}"], missing=["all"]))
            R.append(r)
            with open(f"{OUT}/vet2_partial.jsonl", "a") as fh: fh.write(json.dumps({k: v for k, v in r.items() if not k.startswith("cen_") or k == "cen_jump"}, default=str) + "\n")
            try: write_outputs(R)
            except Exception: log("write_outputs failed:", traceback.format_exc()[-300:])
    write_outputs(R, final=True)
    summ = dict(mode=MODE, n_targets=len(R), counts=pd.Series([r["category"] for r in R]).value_counts().to_dict(),
                controls=control_checks(R), minutes=round((time.time() - T0) / 60, 1))
    json.dump(summ, open(f"{OUT}/summary.json", "w"), indent=1, default=str); log(json.dumps(summ, default=str))

if __name__ == "__main__":
    try: main()
    except Exception: log("FATAL", traceback.format_exc())

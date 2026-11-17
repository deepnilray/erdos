"""
Vetting + second detector for the giant-impact afterglow hunt (runs in GitHub Actions; results go to branch impacts-vet).

Inputs: the four shard branches impacts-live-0..3 cloned to $SHARD_DIRS (space separated), each holding scores.csv.
Steps
 1. Merge shard scores (deduplicate by uid), rebuild the identical Gaia DR3 pool with hunt.build_pool(), rank detector-1
    candidates (score > 8, W2 brightening exceeding W1 by > 0.05 mag, >= 2 consecutive visits) plus the top sub-threshold
    field stars (exercise targets for the vetting pipeline, not candidates).
 2. Detector 2 (events that began before 2015): W1-W2 of the 2014-2015 baseline relative to the main-sequence locus
    (running median in Gaia BP-RP, robust sigma), stage A = excess > 0.10 mag and z > 5, unsaturated (W1 > 8);
    stage B = decay over the mission (W2 fading slope or W1-W2 decline, > 3 sigma) or AllWISE 2010 W1-W2 above the NEOWISE
    baseline by > 0.1 mag. Must-recover validation object: NGC 2547-ID8.
 3. Vet every target: Gaia DR3 neighbours within 6" (blend), W1 < 8 (saturation), Gaia DR3 variability class / QSO
    candidate table, SIMBAD object types within 6", VSX entries within 6", AllWISE 2010 colours, refetched NEOWISE light
    curve (score re-computed as a uid-mapping control), plot per target.
"""
import os, sys, json, time, traceback, numpy as np, pandas as pd, pyvo, requests
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
os.chdir(HERE)
import hunt  # noqa: E402  (pool builder, visit binning and detector-1 score are reused verbatim)
OUT = "out"; os.makedirs(f"{OUT}/plots", exist_ok=True)
LG = open(f"{OUT}/vet_log.txt", "w")
def log(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(map(str, a)); print(s, flush=True); LG.write(s + "\n"); LG.flush()

class TSession(requests.Session):
    """every HTTP call gets a timeout, so one hung archive cannot stall the whole job"""
    def request(self, *a, **k): k.setdefault("timeout", 90); return super().request(*a, **k)
SES = TSession()
def TAPS(u): return pyvo.dal.TAPService(u, session=SES)
GAIA = TAPS("https://gea.esac.esa.int/tap-server/tap")
IRSA = TAPS("https://irsa.ipac.caltech.edu/TAP")
SIMBAD_URLS = ["https://simbad.cds.unistra.fr/simbad/sim-tap", "https://simbad.harvard.edu/simbad/sim-tap"]
VIZ_URLS = ["https://tapvizier.cds.unistra.fr/TAPVizieR/tap"]
YSO_TYPES = {"Y*O", "Y*?", "TT*", "TT?", "Or*", "Ae*", "Ae?", "HH", "YSO", "TTS", "pr*", "pr?", "Y*O?", "FU*", "outflow?", "of?"}
VAR_KILL = {"Mi*", "Mi?", "LP*", "LP?", "C*", "C*?", "AB*", "AB?", "RG*", "RG?", "s*r", "EB*", "EB?", "SB*", "CV*", "Be*", "Em*"}
EXTRAGAL = {"QSO", "Q?", "AGN", "AG?", "G", "G?", "Sy1", "Sy2", "SyG", "BLL", "Bla", "LIN", "GiG", "GiC", "rG", "IG"}
NVET_NEAR = int(os.environ.get("NVET_NEAR", "15")); NVET_D2 = int(os.environ.get("NVET_D2", "40"))

def tap(svc, q, tries=3, maxrec=50000):
    for k in range(tries):
        try: return svc.run_sync(q, maxrec=maxrec).to_table().to_pandas()
        except Exception as e:
            err = repr(e)[:200]; time.sleep(4 * (k + 1))
    raise RuntimeError(err)

_svc_ok, _dead = {}, {}
def tap_any(urls, q, key):
    """first reachable mirror wins; a mirror that fails twice is not tried again in this job (unreachable CDS hosts
    would otherwise cost minutes per target). Returns (df, url) or raises."""
    errs = []
    order = ([_svc_ok[key]] if key in _svc_ok else []) + [u for u in urls if u != _svc_ok.get(key)]
    for u in order:
        if _dead.get(u, 0) >= 2: errs.append(f"{u}: skipped (failed twice)"); continue
        try:
            df = tap(TAPS(u), q, tries=1); _svc_ok[key] = u; _dead[u] = 0; return df, u
        except Exception as e: errs.append(f"{u}: {e}"); _dead[u] = _dead.get(u, 0) + 1
    raise RuntimeError(" | ".join(errs)[:400])

def cone(ra, dec, r): return f"CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra}, {dec}, {r / 3600.0})) = 1"

# ---------------------------------------------------------------- 1. merge
def merge_scores():
    parts = []
    for p in os.environ["SHARD_DIRS"].split():
        f = os.path.join(p, "scores.csv")
        if os.path.exists(f): parts.append(pd.read_csv(f)); log("read", f, len(parts[-1]))
        else: log("MISSING", f)
    s = pd.concat(parts, ignore_index=True)
    s["fin"] = np.isfinite(s.score); s = s.sort_values("fin").drop_duplicates("uid", keep="last").drop(columns="fin")
    log("merged rows", sum(map(len, parts)), "-> unique uids", len(s)); return s

# ---------------------------------------------------------------- light curve + metrics
def neowise_lc(ra, dec):
    q = ("SELECT mjd, w1mpro, w1sigmpro, w2mpro, w2sigmpro, cc_flags FROM neowiser_p1bs_psd AS n WHERE "
         f"CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', {ra}, {dec}, 0.000833)) = 1 AND " + hunt.GOODQ)
    t = tap(IRSA, q, maxrec=20000)
    cc = t.cc_flags.astype(str); ok = cc.map(lambda c: c[:2] in ("00", "0") or c == "0000") & np.isfinite(t.w1mpro + t.w2mpro)
    t = t[ok]
    if len(t) < 30: return None, len(t)
    return hunt.visits(*(t[c].to_numpy(float) for c in ("mjd", "w1mpro", "w1sigmpro", "w2mpro", "w2sigmpro"))), len(t)

def slope(t, y, e):
    """weighted linear slope in mag/yr with errors inflated by the residual scatter (intrinsic variability counts as noise)"""
    x = (t - t.mean()) / 365.25; w = 1 / np.maximum(e, 0.005) ** 2
    A = np.vstack([np.ones_like(x), x]).T; W = np.diag(w)
    cov = np.linalg.inv(A.T @ W @ A); b = cov @ A.T @ W @ y
    chi = np.sum(w * (y - A @ b) ** 2) / max(len(y) - 2, 1)
    return float(b[1]), float(np.sqrt(cov[1, 1] * max(chi, 1.0)))

# ---------------------------------------------------------------- per-target vetting
T0 = time.time(); DEADLINE = float(os.environ.get("VET_DEADLINE_MIN", "85")) * 60
def vet_one(row):
    r = dict(uid=int(row.uid), label=row.label, ra=float(row.ra), dec=float(row.dec)); errs = []
    if time.time() - T0 > DEADLINE: r["errors"] = "SKIPPED: job deadline reached"; return r
    # Gaia neighbours within 6"
    try:
        g = tap(GAIA, "SELECT source_id, ra, dec, phot_g_mean_mag AS g, bp_rp, parallax, ruwe, phot_variable_flag, "
                f"DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {r['ra']}, {r['dec']})) * 3600 AS sep FROM gaiadr3.gaia_source WHERE "
                + cone(r["ra"], r["dec"], 6)).sort_values("sep")
        if len(g):
            me = g.iloc[0]; r.update(gaia_id=int(me.source_id), gmag=float(me.g), bprp=float(me.bp_rp) if np.isfinite(me.bp_rp) else np.nan,
                                    plx=float(me.parallax), ruwe=float(me.ruwe) if np.isfinite(me.ruwe) else np.nan, varflag=str(me.phot_variable_flag), self_sep=float(me.sep))
            nb = g.iloc[1:]
            r["n_nb6"] = len(nb); r["nb_list"] = "; ".join(f'{s.sep:.1f}" G={s.g:.2f}' for s in nb.itertuples())
            r["nb_min_dG"] = float((nb.g - me.g).min()) if len(nb) else np.nan
        else: r["n_nb6"] = 0
    except Exception as e: errs.append(f"gaia:{e}")
    if r.get("gaia_id"):
        try:
            v = tap(GAIA, f"SELECT classifier_name, best_class_name, best_class_score FROM gaiadr3.vari_classifier_result WHERE source_id = {r['gaia_id']}")
            r["gaia_varclass"] = ";".join(f"{a.best_class_name}({a.best_class_score:.2f})" for a in v.itertuples()) if len(v) else ""
            qq = tap(GAIA, f"SELECT source_id FROM gaiadr3.qso_candidates WHERE source_id = {r['gaia_id']}"); r["gaia_qso_cand"] = bool(len(qq))
        except Exception as e: errs.append(f"gaiavari:{e}")
    # SIMBAD within 6"
    try:
        s, url = tap_any(SIMBAD_URLS, "SELECT b.main_id, b.otype, o.otype AS anytype, DISTANCE(POINT('ICRS', b.ra, b.dec), "
                         f"POINT('ICRS', {r['ra']}, {r['dec']})) * 3600 AS sep FROM basic AS b JOIN otypes AS o ON o.oidref = b.oid "
                         f"WHERE CONTAINS(POINT('ICRS', b.ra, b.dec), CIRCLE('ICRS', {r['ra']}, {r['dec']}, {6 / 3600})) = 1", "simbad")
        r["simbad"] = "; ".join(sorted({f"{m.strip()}[{o}] {d:.1f}\"" for m, o, d in zip(s.main_id, s.otype, s.sep)}))
        r["simbad_types"] = ",".join(sorted({str(x).strip() for x in pd.concat([s.otype, s.anytype])}))
    except Exception as e: errs.append(f"simbad:{e}"); r["simbad"] = "UNREACHABLE"
    # VSX within 6": VizieR B/vsx, then the AAVSO VSX API
    try:
        v, url = tap_any(VIZ_URLS, f'SELECT "Name", "Type", "max", "min", "Period" FROM "B/vsx/vsx" WHERE '
                         f"CONTAINS(POINT('ICRS', RAJ2000, DEJ2000), CIRCLE('ICRS', {r['ra']}, {r['dec']}, {6 / 3600})) = 1", "viz")
        r["vsx"] = "; ".join(f"{a.Name}[{a.Type}] P={a.Period}" for a in v.itertuples()) if len(v) else ""
    except Exception as e:
        try:
            j = requests.get("https://www.aavso.org/vsx/index.php", params=dict(view="api.list", ra=r["ra"], dec=r["dec"], radius=6 / 3600, format="json"), timeout=60).json()
            items = (j.get("VSXObjects") or {}).get("VSXObject", []) if isinstance(j, dict) else []
            if isinstance(items, dict): items = [items]
            r["vsx"] = "; ".join(f"{o.get('Name')}[{o.get('VariabilityType')}] P={o.get('Period')}" for o in items)
        except Exception as e2: errs.append(f"vsx:{e} / aavso:{e2}"); r["vsx"] = "UNREACHABLE"
    # AllWISE 2010
    try:
        a = tap(IRSA, "SELECT designation, w1mpro, w1sigmpro, w2mpro, w2sigmpro, w3mpro, w3sigmpro, w4mpro, w4sigmpro, cc_flags, ext_flg, ph_qual, "
                f"DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {r['ra']}, {r['dec']})) * 3600 AS sep FROM allwise_p3as_psd WHERE " + cone(r["ra"], r["dec"], 6)).sort_values("sep")
        r["allwise_n6"] = len(a)
        if len(a):
            x = a.iloc[0]
            r.update(aw_name=str(x.designation).strip(), aw_sep=float(x.sep), aw_w1=float(x.w1mpro), aw_w2=float(x.w2mpro), aw_w3=float(x.w3mpro), aw_w4=float(x.w4mpro),
                     aw_w1w2=float(x.w1mpro - x.w2mpro), aw_w2w3=float(x.w2mpro - x.w3mpro), aw_ccf=str(x.cc_flags), aw_phq=str(x.ph_qual), aw_ext=int(x.ext_flg))
    except Exception as e: errs.append(f"allwise:{e}")
    # NEOWISE refetch, detector-1 score recomputed, detector-2 decay metrics, plot
    try:
        V, npts = neowise_lc(r["ra"], r["dec"]); r["npts"] = npts
        if V is not None and len(V) >= 3:
            np.savetxt(f"{OUT}/plots/{r['uid']}_lc.txt", V, fmt="%.5f", header="mjd w1 e1 w2 e2 n")
            sc = hunt.score(V); r["score_refetch"] = sc["score"] if sc else np.nan
            col = V[:, 1] - V[:, 3]; ecol = np.hypot(V[:, 2], V[:, 4])
            r["w2_slope"], r["w2_slope_err"] = slope(V[:, 0], V[:, 3], V[:, 4])
            r["col_slope"], r["col_slope_err"] = slope(V[:, 0], col, ecol)
            r["neo_w1w2_first"], r["neo_w1w2_last"] = float(np.median(col[:3])), float(np.median(col[-3:]))
            plot(r, V)
    except Exception as e: errs.append(f"neowise:{e}")
    r["errors"] = " || ".join(errs)[:600]
    with open(f"{OUT}/vet_partial.jsonl", "a") as fh: fh.write(json.dumps(r, default=str) + "\n")
    log("vetted", r["uid"], r["label"], "errors:", r["errors"][:200]); return r

def plot(r, V):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    f, ax = plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True, gridspec_kw=dict(height_ratios=[2, 1]))
    ax[0].errorbar(V[:, 0], V[:, 1], V[:, 2], fmt="o", ms=3, label="W1 (NEOWISE visit median)")
    ax[0].errorbar(V[:, 0], V[:, 3], V[:, 4], fmt="s", ms=3, label="W2")
    if np.isfinite(r.get("aw_w1", np.nan)):
        ax[0].plot([55350], [r["aw_w1"]], "C0*", ms=10, label="AllWISE W1 (2010, epoch approx.)"); ax[0].plot([55350], [r["aw_w2"]], "C1*", ms=10)
        ax[1].plot([55350], [r["aw_w1w2"]], "k*", ms=10)
    ax[0].invert_yaxis(); ax[0].set_ylabel("mag"); ax[0].legend(fontsize=6)
    ax[1].errorbar(V[:, 0], V[:, 1] - V[:, 3], np.hypot(V[:, 2], V[:, 4]), fmt="ko", ms=3); ax[1].set_ylabel("W1-W2"); ax[1].set_xlabel("MJD")
    ax[0].set_title(f"{r['label']} uid {r['uid']}  ra {r['ra']:.5f} dec {r['dec']:.5f}  score(refetch) {r.get('score_refetch', np.nan):.1f}", fontsize=7)
    plt.tight_layout(); plt.savefig(f"{OUT}/plots/{r['uid']}.png", dpi=100); plt.close()

def verdict(r, det):
    kills, notes = [], []
    if np.isfinite(r.get("base_w1", np.nan)) and r["base_w1"] < 8: kills.append(f"W1 saturation (baseline W1 {r['base_w1']:.2f} < 8)")
    if r.get("n_nb6", 0) and np.isfinite(r.get("nb_min_dG", np.nan)) and r["nb_min_dG"] < 3:
        kills.append(f"blend: Gaia neighbour within 6\" only {r['nb_min_dG']:.1f} mag fainter in G ({r['nb_list']})")
    elif r.get("n_nb6", 0): notes.append(f"faint Gaia neighbours within 6\": {r['nb_list']}")
    t = set(str(r.get("simbad_types", "")).split(",")) - {""}
    if t & YSO_TYPES: kills.append(f"YSO in SIMBAD ({','.join(sorted(t & YSO_TYPES))})")
    if t & VAR_KILL: kills.append(f"known variable class in SIMBAD ({','.join(sorted(t & VAR_KILL))})")
    if t & EXTRAGAL: kills.append(f"extragalactic object within 6\" in SIMBAD ({','.join(sorted(t & EXTRAGAL))})")
    vsx = str(r.get("vsx", ""))
    if vsx and vsx != "UNREACHABLE": notes.append(f"VSX: {vsx}")
    if "YSO" in str(r.get("gaia_varclass", "")): kills.append("Gaia DR3 variability classifier: YSO")
    if r.get("gaia_qso_cand"): kills.append("in Gaia DR3 QSO candidate table")
    pre = r.get("aw_excess", np.nan)
    if det == 1 and np.isfinite(pre) and pre > 0.1 and r.get("aw_w1", 0) > 8:
        kills.append(f"pre-existing IR excess in AllWISE 2010 (W1-W2 {pre:.2f} above the main-sequence locus)")
    if np.isfinite(r.get("score_refetch", np.nan)) and np.isfinite(r.get("score", np.nan)) and r["score"] > 1 and abs(r["score_refetch"] - r["score"]) > 0.3 * r["score"]:
        notes.append(f"score not reproduced on refetch ({r['score']:.1f} stored vs {r['score_refetch']:.1f})")
    if r.get("simbad") == "UNREACHABLE" or r.get("vsx") == "UNREACHABLE": notes.append("literature check incomplete (SIMBAD or VSX unreachable)")
    return kills, notes

def main():
    s = merge_scores()
    pool = hunt.build_pool().to_pandas(); log("pool rows", len(pool))
    d = s.merge(pool, on="uid", how="left"); good = d[np.isfinite(d.score)]
    summ = dict(n_pool=len(pool), n_scored=len(d), n_with_lc=len(good), frac_done=len(d) / len(pool))
    for thr in (5, 8, 12, 20): summ[f"n_score_gt_{thr}"] = int((good.score > thr).sum())
    for name in hunt.VALID:
        v = d[d.cluster == "VALID:" + name]
        if len(v): summ[f"valid_{name}"] = dict(score=float(v.score.iloc[0]), dW2=float(v.dW2.iloc[0]), dW1=float(v.dW1.iloc[0]), start=float(v.start.iloc[0]),
                                                rank=int((good.score > v.score.iloc[0]).sum()) + 1)
    field = good[good.cluster == "field"]
    summ["field_max_score"] = float(field.score.max())
    c1 = good[(good.score > 8) & (good.redden > 0.05) & (good.nvis >= 2)].sort_values("score", ascending=False)
    c1.to_csv(f"{OUT}/candidates_det1.csv", index=False); summ["n_cand_det1"] = len(c1); summ["n_cand_det1_field"] = int((c1.cluster == "field").sum())
    near = field[~field.uid.isin(c1.uid)].sort_values("score", ascending=False).head(NVET_NEAR)
    # ---------------- detector 2, stage A
    f2 = field[np.isfinite(field.base_w1w2) & np.isfinite(field.bprp) & (field.base_w1 > 8)].copy()
    edges = np.arange(0.55, 2.2501, 0.05); mids, med, sig = [], [], []
    for a, b in zip(edges[:-1], edges[1:]):
        x = f2.base_w1w2[(f2.bprp >= a) & (f2.bprp < b)]
        if len(x) >= 50: mids.append((a + b) / 2); m = np.median(x); med.append(m); sig.append(max(1.4826 * np.median(np.abs(x - m)), 0.01))
    mids, med, sig = map(np.array, (mids, med, sig))
    pd.DataFrame(dict(bprp=mids, locus_w1w2=med, sigma=sig)).to_csv(f"{OUT}/ms_locus_w1w2.csv", index=False)
    loc = lambda c: np.interp(c, mids, med); sg = lambda c: np.interp(c, mids, sig)
    f2["excess_locus"] = f2.base_w1w2 - loc(f2.bprp); f2["z_excess"] = f2.excess_locus / sg(f2.bprp)
    # variability of the 6-month visit medians relative to stars of the same W2 brightness (EDDs such as ID8 vary
    # recurrently rather than decay, arXiv:2610.10130), used by the detector-2 "excess + variability" variant
    jb = np.arange(4.0, 15.01, 0.5); jmid, jmed = [], []
    for a, b in zip(jb[:-1], jb[1:]):
        x = f2.jitter[(f2.base_w2 >= a) & (f2.base_w2 < b)]
        if len(x) >= 50: jmid.append((a + b) / 2); jmed.append(np.median(x))
    jit_ref = lambda w2: np.interp(w2, jmid, jmed)
    pd.DataFrame(dict(w2=jmid, median_jitter=jmed)).to_csv(f"{OUT}/jitter_ref.csv", index=False)
    f2["jit_ratio"] = f2.jitter / jit_ref(f2.base_w2)
    A = f2[(f2.excess_locus > 0.10) & (f2.z_excess > 5)].sort_values("z_excess", ascending=False)
    summ["n_det2_var_pass_all"] = int((A.jit_ratio > 3).sum())
    A.to_csv(f"{OUT}/det2_stageA.csv", index=False); summ["n_det2_stageA"] = len(A); summ["n_det2_input"] = len(f2)
    log("detector 2 stage A:", len(A), "of", len(f2))
    # ---------------- targets
    T = []
    for lab, df in (("DET1", c1), ("NEAR", near), ("DET2A", A.head(NVET_D2)), ("DET2A", A[A.jit_ratio > 3].head(NVET_D2))):
        for x in df.itertuples(): T.append(dict(uid=x.uid, ra=x.ra, dec=x.dec, label=lab))
    for x in d[d.cluster.astype(str).str.startswith("VALID:")].itertuples(): T.append(dict(uid=x.uid, ra=x.ra, dec=x.dec, label=x.cluster))
    T = pd.DataFrame(T).drop_duplicates("uid"); log("targets to vet:", len(T))
    with ThreadPoolExecutor(6) as ex: R = list(ex.map(lambda row: vet_one(row), [r for r in T.itertuples()]))
    R = pd.DataFrame(R).merge(d[["uid", "score", "dW2", "dW1", "redden", "start", "nvis", "n_visits", "base_w1", "base_w2", "base_w1w2", "jitter"]], on="uid", how="left")
    R = R.merge(f2[["uid", "excess_locus", "z_excess", "jit_ratio"]], on="uid", how="left")
    # validation objects are not in the field locus table: compute their excess from their own Gaia colour
    for i in R.index[R.label.str.startswith("VALID:")]:
        if np.isfinite(R.at[i, "bprp"]):
            R.at[i, "excess_locus"] = R.at[i, "base_w1w2"] - loc(R.at[i, "bprp"]); R.at[i, "z_excess"] = R.at[i, "excess_locus"] / sg(R.at[i, "bprp"])
        if np.isfinite(R.at[i, "base_w2"]): R.at[i, "jit_ratio"] = R.at[i, "jitter"] / jit_ref(R.at[i, "base_w2"])
    R["aw_excess"] = R.aw_w1w2 - loc(R.bprp)
    # detector 2 stage B (decay)
    R["w2_fade_sig"] = R.w2_slope / R.w2_slope_err; R["col_decline_sig"] = -R.col_slope / R.col_slope_err
    R["aw_minus_neo_w1w2"] = R.aw_w1w2 - R.base_w1w2
    R["det2_pass"] = (R.excess_locus > 0.10) & (R.z_excess > 5) & (((R.w2_fade_sig > 3) & (R.w2_slope > 0.01)) | ((R.col_decline_sig > 3) & (R.col_slope < -0.005)) | (R.aw_minus_neo_w1w2 > 0.1))
    R["det2_var_pass"] = (R.excess_locus > 0.10) & (R.z_excess > 5) & (R.jit_ratio > 3)
    K, N = [], []
    for r in R.to_dict("records"):
        det = 2 if r["label"] == "DET2A" or r["label"] == "VALID:NGC2547-ID8" else 1
        k, n = verdict(r, det); K.append(" | ".join(k)); N.append(" | ".join(n))
    R["kill"] = K; R["notes"] = N
    R.to_csv(f"{OUT}/vet_table.csv", index=False)
    for name in hunt.VALID:
        v = R[R.label == "VALID:" + name]
        if len(v): summ[f"vet_{name}"] = {k: (None if isinstance(x, float) and not np.isfinite(x) else x) for k, x in v.iloc[0][["score", "score_refetch", "excess_locus", "z_excess", "w2_slope", "w2_fade_sig", "col_slope", "col_decline_sig", "aw_w1w2", "aw_minus_neo_w1w2", "det2_pass", "jit_ratio", "det2_var_pass", "simbad", "vsx", "kill"]].to_dict().items()}
    summ["n_det2_pass_vetted"] = int(R[R.label == "DET2A"].det2_pass.sum()); summ["n_det2_var_pass_vetted"] = int(R[R.label == "DET2A"].det2_var_pass.sum())
    summ["services"] = _svc_ok
    json.dump(summ, open(f"{OUT}/summary.json", "w"), indent=1, default=str); log(json.dumps(summ, indent=1, default=str))
    cols = ["label", "uid", "ra", "dec", "gmag", "bprp", "score", "score_refetch", "dW2", "dW1", "start", "base_w1", "excess_locus", "z_excess", "w2_slope", "w2_fade_sig", "col_slope", "col_decline_sig", "aw_w1w2", "det2_pass", "jit_ratio", "det2_var_pass", "n_nb6", "nb_min_dG", "simbad", "vsx", "gaia_varclass", "kill", "notes", "errors"]
    with open(f"{OUT}/vet_report.md", "w") as fh:
        fh.write("# Vetting report (machine generated; by-eye check of plots/ still required)\n\n```\n" + json.dumps(summ, indent=1, default=str) + "\n```\n\n")
        for r in R[[c for c in cols if c in R.columns]].to_dict("records"):
            fh.write(f"## {r['label']} uid {r['uid']}\n" + "\n".join(f"- {k}: {v}" for k, v in r.items()) + "\n\n")

if __name__ == "__main__":
    try: main()
    except Exception: traceback.print_exc(file=LG); traceback.print_exc(); sys.exit(1)

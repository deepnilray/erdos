"""
Injection-recovery test of the giant-impact hunt detector D1 (hunt.visits + hunt.score + candidate cuts).

Stages (run from a scratch working directory; hunt.py opens results/hunt_log.txt in the cwd at import):
  python completeness.py sample    # random Gaia DR3 sample from the near-pool definition (random RA strips)
  python completeness.py fetch     # NEOWISE single exposures with hunt.GOODQ, IRSA run_sync upload joins of <= 60
  python completeness.py control   # ASASSN-21qj positive control (real light curve, no injection)
  python completeness.py inject    # false-positive run on the untouched sample + injection trials -> trials.csv.gz
  python completeness.py report    # tables, 50%/90% amplitudes, plot
Only real NEOWISE photometry is used; synthetic signals are added on top of it for this test only.
"""
import os, sys, time, json, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
WORK = os.environ.get("WORK", os.getcwd()); os.makedirs(WORK, exist_ok=True); os.chdir(WORK)
import hunt                                   # noqa: E402  (imported after chdir on purpose)
from astropy.table import Table, vstack      # noqa: E402
import pyvo                                   # noqa: E402

SEED = 20261120
NSAMP = int(os.environ.get("NSAMP", "2000"))
AMPS = [0.03, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.50]
SHAPES = ["step", "decay1yr", "decay3yr", "ramp"]
K_ONSET = int(os.environ.get("K_ONSET", "2"))          # independent (onset, T, ramp length) draws per star, amp and shape
MJD_LO, MJD_HI = 56700.0, 60300.0
ZP1, ZP2 = 309.540, 171.787                           # WISE Vega zero points (Jy), Wright et al. 2010 / Jarrett et al. 2011
LAM1, LAM2 = 3.35e-6, 4.60e-6                         # isophotal wavelengths (m) given in the task

def cand(r):
    return r is not None and r["score"] > 8 and r["redden"] > 0.05 and r["nvis"] >= 2

def bb_ratio(T):
    """F_nu(W1)/F_nu(W2) of a blackbody at temperature T (no colour correction)."""
    h, c, k = 6.62607015e-34, 2.99792458e8, 1.380649e-23
    nu1, nu2 = c / LAM1, c / LAM2
    return (nu1 ** 3 / np.expm1(h * nu1 / (k * T))) / (nu2 ** 3 / np.expm1(h * nu2 / (k * T)))

# ---------------------------------------------------------------- stage 1: sample
def stage_sample():
    rng = np.random.default_rng(SEED)
    gaia = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
    q = ("SELECT source_id, ra, dec, phot_g_mean_mag AS gmag, bp_rp AS bprp, parallax AS plx FROM gaiadr3.gaia_source "
         "WHERE parallax > 4 AND parallax_over_error > 10 AND phot_g_mean_mag BETWEEN 8 AND 15 "
         "AND bp_rp BETWEEN 0.55 AND 2.2 AND ruwe < 1.4")              # identical to hunt.build_pool POOL=near
    W = 0.05; starts = np.sort(rng.choice(np.arange(0, 360, W), 90, replace=False))   # 90 random 0.05-deg RA strips, all Dec
    parts = []
    for r0 in starts:
        for a in range(4):
            try:
                parts.append(gaia.run_sync(q + f" AND ra >= {r0:.2f} AND ra < {r0 + W:.2f}", maxrec=100000).to_table()); break
            except Exception as e:
                print("strip", r0, "failed", repr(e)[:120], flush=True); time.sleep(10)
    t = vstack(parts)
    absg = np.array(t["gmag"], float) + 5 * np.log10(np.array(t["plx"], float) / 100.0)
    x = np.array(t["bprp"], float); t = t[(absg > 2.2 * x + 0.2) & (absg < 2.9 * x + 3.6)]   # hunt's main-sequence band
    print("strips", len(parts), "main-sequence stars in strips", len(t))
    df = t.to_pandas(); df = df.iloc[rng.permutation(len(df))[:NSAMP]].reset_index(drop=True)
    df["uid"] = np.arange(len(df))
    df.to_csv(f"{HERE}/sample.csv", index=False); print("sample written:", len(df))
    json.dump({"strip_width_deg": W, "strip_starts": [float(s) for s in starts], "pool_in_strips": len(t)}, open(f"{HERE}/sample_strips.json", "w"))

# ---------------------------------------------------------------- stage 2: fetch
QUP = ("SELECT t.objid, n.mjd, n.w1mpro, n.w1sigmpro, n.w2mpro, n.w2sigmpro, n.cc_flags FROM TAP_UPLOAD.targets AS t, "
       "neowiser_p1bs_psd AS n WHERE CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', t.tra, t.tdec, 0.000833)) = 1 AND " + hunt.GOODQ)

def fetch_one(svc, sub):
    up = Table({"objid": np.array(sub["uid"], int), "tra": np.array(sub["ra"], float), "tdec": np.array(sub["dec"], float)})
    r = svc.run_sync(QUP, uploads={"targets": up}, maxrec=2000000).to_table(); r.rename_column("objid", "uid"); return r

def stage_fetch():
    import requests
    s = pd.read_csv(f"{HERE}/sample.csv"); os.makedirs("raw", exist_ok=True)
    sess = requests.Session(); sess.request = _timeout(sess.request, 300)
    svc = pyvo.dal.TAPService(hunt.IRSA, session=sess)
    CH = 60
    for k in range(0, len(s), CH):
        out = f"raw/chunk_{k // CH:03d}.csv"
        if os.path.exists(out): continue
        sub = s.iloc[k:k + CH]
        for a in range(5):
            try:
                t0 = time.time(); r = fetch_one(svc, sub); r.write(out, format="csv", overwrite=True)
                print(f"chunk {k // CH} rows {len(r)} {time.time() - t0:.0f}s", flush=True); break
            except Exception as e:
                print(f"chunk {k // CH} attempt {a + 1} failed: {repr(e)[:150]}", flush=True); time.sleep(20 * (a + 1))

def _timeout(f, t):
    def g(*a, **kw):
        kw.setdefault("timeout", t); return f(*a, **kw)
    return g

def load_exposures():
    """per-star arrays after the hunt's harvest() filters: cc_flags clean, finite W1+W2, >= 30 exposures."""
    import glob
    t = pd.concat([pd.read_csv(f, dtype={"cc_flags": str}, keep_default_na=False, na_values=[""]) for f in sorted(glob.glob("raw/chunk_*.csv"))])
    cc = t["cc_flags"].astype(str).values
    ok = np.array([c[:2] in ("00", "0") or c == "0000" for c in cc], dtype=bool)   # copied verbatim from hunt.harvest
    w1 = t["w1mpro"].astype(float).values; w2 = t["w2mpro"].astype(float).values
    ok &= np.isfinite(w1 + w2)
    t = t[ok]; stars = {}
    for u, g in t.groupby("uid"):
        if len(g) < 30: continue                                                    # hunt.harvest: s.sum() >= 30
        stars[int(u)] = tuple(g[c].astype(float).values for c in ("mjd", "w1mpro", "w1sigmpro", "w2mpro", "w2sigmpro"))
    return stars

# ---------------------------------------------------------------- stage 3: control
def stage_control():
    svc = pyvo.dal.TAPService(hunt.IRSA); ra, de = hunt.VALID["ASASSN-21qj"]
    q = ("SELECT mjd, w1mpro, w1sigmpro, w2mpro, w2sigmpro, cc_flags FROM neowiser_p1bs_psd AS n WHERE "
         f"CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', {ra}, {de}, 0.000833)) = 1 AND " + hunt.GOODQ)
    t = svc.run_sync(q, maxrec=20000).to_table()
    cc = np.array([str(x) for x in t["cc_flags"]]); w1, e1, w2, e2 = (np.array(t[c], float) for c in ("w1mpro", "w1sigmpro", "w2mpro", "w2sigmpro"))
    ok = np.array([c[:2] in ("00", "0") or c == "0000" for c in cc], dtype=bool) & np.isfinite(w1 + w2)
    m = np.array(t["mjd"], float)
    V = hunt.visits(m[ok], w1[ok], e1[ok], w2[ok], e2[ok]); r = hunt.score(V)
    r["n_exposures"] = int(ok.sum()); r["candidate"] = bool(cand(r))
    print(json.dumps(r, indent=1)); json.dump(r, open(f"{HERE}/control_asassn21qj.json", "w"), indent=1)

# ---------------------------------------------------------------- stage 4: inject
def profile(shape, t, t0, ramp):
    dt = t - t0; p = np.zeros_like(t); on = dt >= 0
    if shape == "step": p[on] = 1.0
    elif shape == "decay1yr": p[on] = np.exp(-dt[on] / 365.25)
    elif shape == "decay3yr": p[on] = np.exp(-dt[on] / (3 * 365.25))
    elif shape == "ramp": p[on] = np.minimum(dt[on] / ramp, 1.0)
    return p

def inject(m, w1, w2, amp, shape, t0, T, ramp):
    """add excess flux to every exposure. amp = peak W2 brightening of the quiescent star (mag). W1 excess flux density
    = W2 excess flux density x blackbody ratio B_nu(3.35um)/B_nu(4.60um) at T, converted with the Vega zero points."""
    F1 = ZP1 * 10 ** (-0.4 * w1); F2 = ZP2 * 10 ** (-0.4 * w2)
    q2 = ZP2 * 10 ** (-0.4 * np.median(w2)); q2 = q2 * (10 ** (0.4 * amp) - 1)       # excess W2 flux (Jy) at peak
    p = profile(shape, m, t0, ramp)
    X2 = q2 * p; X1 = X2 * bb_ratio(T)
    return -2.5 * np.log10((F1 + X1) / ZP1), -2.5 * np.log10((F2 + X2) / ZP2)

def stage_inject():
    stars = load_exposures(); s = pd.read_csv(f"{HERE}/sample.csv").set_index("uid")
    rng = np.random.default_rng(SEED + 1)
    rows, base, fp = [], [], []
    roundtrip_bad = 0
    for u, (m, w1, e1, w2, e2) in stars.items():
        V = hunt.visits(m, w1, e1, w2, e2); r0 = hunt.score(V)
        if r0 is None: continue                                                       # < 6 visits: dropped
        # round-trip control: zero-amplitude injection must reproduce the untouched score
        a1, a2 = inject(m, w1, w2, 0.0, "step", MJD_LO, 1000.0, 365.0)
        rz = hunt.score(hunt.visits(m, a1, e1, a2, e2)); roundtrip_bad += abs(rz["score"] - r0["score"]) > 1e-6
        base.append(dict(uid=u, gmag=s.loc[u, "gmag"], bprp=s.loc[u, "bprp"], ra=s.loc[u, "ra"], dec=s.loc[u, "dec"], n_exp=len(m),
                         **{k: r0[k] for k in ("score", "dW2", "dW1", "redden", "nvis", "n_visits", "base_w1", "base_w2", "jitter", "start")},
                         candidate=cand(r0)))
        sc2 = max(np.std(V[:3, 3]), np.median(V[:3, 4]), 0.01); noise = np.hypot(sc2, r0["jitter"])
        for shape in SHAPES:
            for amp in AMPS:
                for k in range(K_ONSET):
                    t0 = rng.uniform(MJD_LO, MJD_HI); T = rng.uniform(600, 1300); ramp = rng.uniform(365.25, 730.5)
                    i1, i2 = inject(m, w1, w2, amp, shape, t0, T, ramp)
                    r = hunt.score(hunt.visits(m, i1, e1, i2, e2))
                    rows.append((u, shape, amp, round(t0, 1), round(T, 0), round(ramp, 0) if shape == "ramp" else np.nan,
                                 round(r0["base_w2"], 3), round(r0["jitter"], 4), round(noise, 4), r0["n_visits"],
                                 round(r["score"], 2), round(r["dW2"], 4), round(r["dW1"], 4), round(r["redden"], 4), r["nvis"],
                                 r["start"], int(cand(r)), int(cand(r0))))
    cols = ["uid", "shape", "amp_w2", "onset_mjd", "T_dust", "ramp_days", "base_w2", "jitter", "noise", "n_visits",
            "score", "dW2", "dW1", "redden", "nvis", "start", "recovered", "untouched_candidate"]
    pd.DataFrame(rows, columns=cols).to_csv(f"{HERE}/trials.csv.gz", index=False)
    b = pd.DataFrame(base); b.to_csv(f"{HERE}/untouched_scores.csv", index=False)
    info = dict(stars_with_exposures=len(stars), stars_ge6_visits=len(b), untouched_candidates=int(b.candidate.sum()),
                untouched_score_gt8=int((b.score > 8).sum()), roundtrip_mismatches=int(roundtrip_bad), trials=len(rows))
    print(info); json.dump(info, open(f"{HERE}/run_info.json", "w"), indent=1)

# ---------------------------------------------------------------- stage 5: report
def stage_report():
    d = pd.read_csv(f"{HERE}/trials.csv.gz"); d = d[d.untouched_candidate == 0]
    info = json.load(open(f"{HERE}/run_info.json"))
    out = {}
    out["by_amp_shape"] = d.pivot_table(index="amp_w2", columns="shape", values="recovered", aggfunc="mean")[SHAPES]
    ok_on = (d.onset_mjd > 57250) & (d.onset_mjd < 59700)
    out["by_amp_shape_onset_57250_59700"] = d[ok_on].pivot_table(index="amp_w2", columns="shape", values="recovered", aggfunc="mean")[SHAPES]
    d["onset_bin"] = pd.cut(d.onset_mjd, np.arange(56700, 60301, 400))
    out["by_onset_amp_step"] = d[d["shape"] == "step"].pivot_table(index="onset_bin", columns="amp_w2", values="recovered", aggfunc="mean", observed=True)
    d["w2_bin"] = pd.cut(d.base_w2, [0, 8, 9, 10, 11, 12, 13, 20])
    out["by_w2mag_amp_step_midonset"] = d[(d["shape"] == "step") & ok_on].pivot_table(index="w2_bin", columns="amp_w2", values="recovered", aggfunc="mean", observed=True)
    d["noise_bin"] = pd.cut(d.noise, [0, 0.01415, 0.02, 0.03, 1.0])     # 0.01414 = floor hypot(0.01, 0.01)
    out["by_noise_amp_step_midonset"] = d[(d["shape"] == "step") & ok_on].pivot_table(index="noise_bin", columns="amp_w2", values="recovered", aggfunc="mean", observed=True)
    d["nvis_bin"] = pd.cut(d.n_visits, [5, 10, 15, 19, 40])
    out["by_nvisits_amp_step_midonset"] = d[(d["shape"] == "step") & ok_on].pivot_table(index="nvis_bin", columns="amp_w2", values="recovered", aggfunc="mean", observed=True)
    out["stars_per_nvis_bin"] = d.drop_duplicates("uid").groupby("nvis_bin", observed=True).uid.count().to_frame("stars")
    d["T_bin"] = pd.cut(d.T_dust, [600, 775, 950, 1125, 1300])
    out["by_T_amp_step_midonset"] = d[(d["shape"] == "step") & ok_on].pivot_table(index="T_bin", columns="amp_w2", values="recovered", aggfunc="mean", observed=True)
    def thresh(tab):
        res = {}
        for sh in tab.columns:
            y = tab[sh].values; x = np.log(tab.index.values); r = {}
            for lev in (0.5, 0.9):
                i = np.where(y >= lev)[0]
                if not len(i): r[lev] = None; continue
                i = i[0]
                r[lev] = float(tab.index.values[0]) if i == 0 else float(np.exp(np.interp(lev, [y[i - 1], y[i]], [x[i - 1], x[i]])))
            res[sh] = r
        return res
    th_all = thresh(out["by_amp_shape"]); th_mid = thresh(out["by_amp_shape_onset_57250_59700"])
    early = d[d.onset_mjd < 57248]; mid = d[(d.onset_mjd > 58000) & (d.onset_mjd < 59300)]
    ctrl = dict(early_onset_recovery_by_amp=early.groupby("amp_w2").recovered.mean().round(3).to_dict(),
                mid_onset_ge03_recovery_by_shape=mid[mid.amp_w2 >= 0.3].groupby("shape").recovered.mean().round(3).to_dict(),
                n_trials_used=len(d))
    with open(f"{HERE}/tables.txt", "w") as fh:
        fh.write(json.dumps(info) + "\n\n")
        for k, v in out.items(): fh.write(f"== {k}\n{v.round(3).to_string()}\n\n")
        fh.write("== thresholds (all onsets)\n" + json.dumps(th_all) + "\n== thresholds (onset 57250-59700)\n" + json.dumps(th_mid) + "\n")
        fh.write("== controls\n" + json.dumps(ctrl) + "\n")
        fh.write("== trials per cell (amp x shape)\n" + d.pivot_table(index="amp_w2", columns="shape", values="recovered", aggfunc="count").to_string() + "\n")
    print(open(f"{HERE}/tables.txt").read())
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, matplotlib.ticker
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    col = dict(step="#2a6fdb", decay1yr="#d9534f", decay3yr="#e0a030", ramp="#3a9d5d")
    for sh in SHAPES:
        ax[0].plot(AMPS, out["by_amp_shape"][sh].values, "o-", color=col[sh], label=f"{sh} (all onsets)")
        ax[0].plot(AMPS, out["by_amp_shape_onset_57250_59700"][sh].values, "s--", color=col[sh], alpha=.6, ms=4, label=f"{sh} (onset 57250-59700)")
    ax[0].set_xscale("log"); ax[0].set_xticks(AMPS); ax[0].set_xticklabels([str(a) for a in AMPS], fontsize=7); ax[0].xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax[0].set_xlabel("injected peak W2 brightening (mag)"); ax[0].set_ylabel("recovered fraction (score>8, redden>0.05, nvis>=2)")
    ax[0].axhline(.5, color="grey", lw=.5); ax[0].axhline(.9, color="grey", lw=.5); ax[0].legend(fontsize=6.5); ax[0].set_ylim(-.02, 1.02)
    ax[0].set_title(f"D1 completeness, {info['stars_ge6_visits']} real NEOWISE light curves", fontsize=9)
    st = d[d["shape"] == "step"]; centers = np.arange(56700, 60300, 200) + 100
    for amp in (0.1, 0.12, 0.15, 0.2, 0.5):
        e = st[st.amp_w2 == amp]; y = [e[(e.onset_mjd >= c - 100) & (e.onset_mjd < c + 100)].recovered.mean() for c in centers]
        ax[1].plot(centers, y, "o-", ms=3, label=f"step {amp} mag")
    ax[1].axvline(57248, color="k", ls=":", lw=1); ax[1].text(57270, .5, "first 1.5 yr\n(baseline)", fontsize=7)
    ax[1].set_xlabel("onset MJD"); ax[1].set_ylabel("recovered fraction"); ax[1].legend(fontsize=7); ax[1].set_ylim(-.02, 1.02)
    ax[1].set_title("step-plateau recovery vs onset epoch", fontsize=9)
    plt.tight_layout(); plt.savefig(f"{HERE}/completeness.png", dpi=110)
    json.dump(dict(thresholds_all=th_all, thresholds_mid=th_mid, controls=ctrl), open(f"{HERE}/summary.json", "w"), indent=1)

if __name__ == "__main__":
    dict(sample=stage_sample, fetch=stage_fetch, control=stage_control, inject=stage_inject, report=stage_report)[sys.argv[1]]()

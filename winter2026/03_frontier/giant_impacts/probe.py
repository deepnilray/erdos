"""Archive probe for the giant-impact search (runs in GitHub Actions)."""
import os, json, traceback, pyvo, numpy as np
OUT = "results"; os.makedirs(OUT, exist_ok=True); L = open(f"{OUT}/probe_log.txt", "w")
def log(*a): s = " ".join(map(str, a)); print(s); L.write(s + "\n"); L.flush()
IRSA = pyvo.dal.TAPService("https://irsa.ipac.caltech.edu/TAP"); GAIA = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
RA, DEC = 123.847042, -38.989833   # ASASSN-21qj = 2MASS J08152329-3859234
def q(svc, s, n=100000):
    try: t = svc.run_sync(s, maxrec=n).to_table(); return t
    except Exception as e: log("QUERY FAILED:", s[:200], repr(e)); return None
t = q(IRSA, "SELECT table_name, description FROM TAP_SCHEMA.tables WHERE lower(table_name) LIKE '%varwise%' OR lower(table_name) LIKE '%neowise%' OR lower(table_name) LIKE '%untimely%' OR lower(table_name) LIKE '%allwise_p3as_psd%'")
for r in t: log("TABLE", r["table_name"], "|", str(r["description"])[:120])
for tab in [str(r["table_name"]) for r in t if "varwise" in str(r["table_name"]).lower()]:
    c = q(IRSA, f"SELECT column_name, datatype, description FROM TAP_SCHEMA.columns WHERE table_name='{tab}'")
    log(f"\nCOLUMNS of {tab}:"); [log("   ", r["column_name"], r["datatype"], "|", str(r["description"])[:140]) for r in c]
    n = q(IRSA, f"SELECT COUNT(*) AS n FROM {tab}"); log("rows", n["n"][0] if n is not None else "?")
    h = q(IRSA, f"SELECT * FROM {tab} WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',{RA},{DEC},0.003))=1")
    log("ASASSN-21qj in", tab, ":", None if h is None else len(h)); 
    if h is not None and len(h): log(dict(zip(h.colnames, [str(h[c][0]) for c in h.colnames])))
c = q(IRSA, "SELECT column_name FROM TAP_SCHEMA.columns WHERE table_name='neowiser_p1bs_psd'"); log("\nneowiser_p1bs_psd columns:", [r[0] for r in c] if c is not None else None)
lc = q(IRSA, f"SELECT mjd, w1mpro, w1sigmpro, w2mpro, w2sigmpro, qual_frame, cc_flags, nb, na, moon_masked, saa_sep, qi_fact, sso_flg FROM neowiser_p1bs_psd WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',{RA},{DEC},0.000833))=1")
if lc is not None:
    lc.write(f"{OUT}/asassn21qj_neowise.csv", format="csv", overwrite=True); log("NEOWISE single exposures for ASASSN-21qj:", len(lc))
    m = np.array(lc["mjd"]); w1 = np.array(lc["w1mpro"], float); w2 = np.array(lc["w2mpro"], float)
    order = np.argsort(m); m, w1, w2 = m[order], w1[order], w2[order]; br = np.where(np.diff(m) > 30)[0] + 1
    for seg in np.split(np.arange(len(m)), br): log(f"   visit mjd {np.median(m[seg]):.0f} n={len(seg)} W1={np.nanmedian(w1[seg]):.3f} W2={np.nanmedian(w2[seg]):.3f}")
g = q(GAIA, f"SELECT source_id, phot_g_mean_mag, bp_rp, parallax, parallax_over_error, ruwe, teff_gspphot, logg_gspphot, phot_variable_flag FROM gaiadr3.gaia_source WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',{RA},{DEC},0.0015))=1")
log("\nGaia DR3 within 5.4 arcsec:"); 
if g is not None: [log("   ", dict(zip(g.colnames, [str(r[c]) for c in g.colnames]))) for r in g]
a = q(IRSA, f"SELECT designation, w1mpro, w2mpro, w3mpro, w4mpro, ph_qual, cc_flags FROM allwise_p3as_psd WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',{RA},{DEC},0.001))=1")
log("AllWISE:", None if a is None else [dict(zip(a.colnames, [str(r[c]) for c in a.colnames])) for r in a])

"""
Runs in GitHub Actions (the Claude sandbox cannot reach CSIRO). Downloads SPICE-RACS DR1, records the schema, and runs the
polarisation-angle coherence test with controls. Writes everything to results/ which the workflow pushes to branch
askap-results. Every step logs what it did, so a failed run still tells the next session what to fix.
"""
import os, sys, re, json, glob, time, traceback, collections
import numpy as np, requests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "polarisation_alignment"))
import align_pilot as ap

OUT = "results"; os.makedirs(OUT, exist_ok=True)
LOG = open(os.path.join(OUT, "run_log.txt"), "w")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()

DOIS = ["10.25919/w37t-nw98", "10.25919/z9jj-8m66", "10.25919/abwc-f513"]   # cut, full (two DOIs seen for the full deposit)
H = {"Accept": "application/json", "User-Agent": "deepnilray-research/1.0"}

def collection_id(doi):
    r = requests.get("https://doi.org/" + doi, allow_redirects=True, timeout=60)
    log("DOI", doi, "->", r.url, r.status_code)
    m = re.search(r"csiro(?::|%3A)(\d+)", r.url, re.I) or re.search(r"collections?/(\d+)", r.url)
    return m.group(1) if m else None

def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)

def list_files(cid):
    for url in (f"https://data.csiro.au/dap/ws/v2/collections/{cid}/data",
                f"https://data.csiro.au/dap/ws/v2/collections/{cid}/data?fileOnly=true"):
        try:
            r = requests.get(url, headers=H, timeout=120); log("GET", url, r.status_code, len(r.content))
            if r.ok:
                j = r.json(); json.dump(j, open(os.path.join(OUT, f"dap_listing_{cid}.json"), "w"), indent=1)
                files = []
                for d in walk(j):
                    name = d.get("filename") or d.get("name")
                    href = (d.get("link") or {}).get("href") if isinstance(d.get("link"), dict) else d.get("link") or d.get("href")
                    if name and href: files.append((name, href, d.get("fileSize") or d.get("size")))
                log("listing top-level keys:", list(j.keys()) if isinstance(j, dict) else type(j), "| parsed files:", len(files))
                if files: return files
        except Exception as e:
            log("listing error", url, repr(e))
    return []

def fetch_casda():
    """SPICE-RACS DR1 files live in a linked CASDA collection; look for catalogue tables on the CASDA TAP service."""
    import pyvo
    svc = pyvo.dal.TAPService("https://casda.csiro.au/casda_vo_tools/tap")
    q = ("SELECT table_name, description FROM TAP_SCHEMA.tables WHERE lower(table_name) LIKE '%spice%' "
         "OR lower(description) LIKE '%spice%' OR (lower(description) LIKE '%polari%' AND lower(description) LIKE '%racs%')")
    tabs = svc.search(q).to_table(); log("CASDA tables matching SPICE/RACS-polarisation:"); 
    for r in tabs: log("   ", r["table_name"], "|", str(r["description"])[:160])
    names = [str(r["table_name"]) for r in tabs]
    names.sort(key=lambda n: (1 if "sources" in n.lower() else 0, 0 if "cut" in n.lower() else 1, [-int(x) for x in re.findall(r"_v(\d+)", n)] or [0], n))
    for n in names:
        try:
            cnt = svc.search(f"SELECT COUNT(*) AS n FROM {n}").to_table()["n"][0]; log("table", n, "rows", cnt)
            if cnt < 1000 or cnt > 400000: continue
            t = svc.search(f"SELECT * FROM {n}", maxrec=500000).to_table()
            os.makedirs("data", exist_ok=True); path = os.path.join("data", n.replace(".", "_") + ".fits")
            t.write(path, overwrite=True); log("saved", path, len(t), "rows"); return path
        except Exception as e:
            log("casda table error", n, repr(e))
    return None

def fetch_catalogue():
    try:
        p = fetch_casda()
        if p: return p
    except Exception as e:
        log("CASDA error", repr(e)); traceback.print_exc(file=LOG)
    for doi in DOIS:
        try:
            cid = collection_id(doi)
            if not cid: continue
            files = list_files(cid)
            log(f"collection {cid}: {len(files)} files; catalogue-like:")
            cands = [f for f in files if re.search(r"(cat|corrected).*\.(xml|vot|fits|csv)$", f[0], re.I)
                     and not re.search(r"spectr|cube|fdf", f[0], re.I)]
            for f in cands[:30]: log("   ", f)
            cands.sort(key=lambda f: (0 if "cut" in f[0].lower() else 1, f[0]))
            for name, href, size in cands:
                path = os.path.join("data", name); os.makedirs("data", exist_ok=True)
                log("downloading", name, href)
                with requests.get(href, stream=True, timeout=600, headers={"User-Agent": H["User-Agent"]}) as r:
                    r.raise_for_status()
                    with open(path, "wb") as fh:
                        for chunk in r.iter_content(1 << 20): fh.write(chunk)
                log("got", path, os.path.getsize(path), "bytes")
                return path
        except Exception as e:
            log("fetch error for", doi, repr(e)); traceback.print_exc(file=LOG)
    return None

def pick(cols, *pats):
    for p in pats:
        for c in cols:
            if re.fullmatch(p, c, re.I): return c
    return None

def main():
    path = fetch_catalogue()
    if not path: log("NO CATALOGUE DOWNLOADED; see listings above"); return
    from astropy.table import Table
    t = Table.read(path)
    cols = t.colnames
    log("rows", len(t)); log("columns", cols)
    with open(os.path.join(OUT, "schema.txt"), "w") as fh:
        for c in cols: fh.write(f"{c}\t{t[c].dtype}\t{getattr(t[c],'unit','')}\t{t[c][0] if len(t) else ''}\n")
    ra = pick(cols, "ra", "ra_deg", "ra_j2000", ".*_ra$", "ra.*")
    de = pick(cols, "dec", "dec_deg", "dec_j2000", ".*_dec$", "dec.*")
    rm = pick(cols, "rm", "rm_fit", "faraday_depth", "phi_peak", "rm_clean")
    pa0 = pick(cols, "derot_polangle", "polangle_0", "psi_0", "chi_0", "polangle0", "pa_0", ".*derot.*", ".*intrinsic.*angle.*")
    fp = pick(cols, "fracpol", "frac_pol", "fractional_pol.*", "p_frac")
    fld = pick(cols, "tile_id", "field", "field_name", "tile", "sbid", "beam_id", ".*tile.*", ".*field.*")
    log("chosen columns:", dict(ra=ra, dec=de, rm=rm, angle=pa0, fracpol=fp, field=fld))
    if not (ra and de and pa0): log("cannot find required columns; stop"); return
    RA, DE = np.array(t[ra], float), np.array(t[de], float)
    PSI = np.array(t[pa0], float); unit = str(getattr(t[pa0], "unit", "") or "")
    if "rad" in unit or np.nanmax(np.abs(PSI)) <= 3.2: PSI = np.degrees(PSI)
    PSI = np.radians(PSI % 180.0)
    RM = np.array(t[rm], float) if rm else np.full(len(t), np.nan)
    FP = np.array(t[fp], float) if fp else np.full(len(t), np.nan)
    if fp and np.nanmedian(FP) > 1.5: FP = FP / 100.0
    FLD = np.array([str(x) for x in t[fld]]) if fld else np.array(["all"] * len(t))
    from astropy.coordinates import SkyCoord; import astropy.units as u
    b = SkyCoord(RA*u.deg, DE*u.deg).galactic.b.deg
    base = np.isfinite(RA) & np.isfinite(DE) & np.isfinite(PSI)
    log("finite rows", base.sum(), "| |b|>20:", (base & (abs(b) > 20)).sum())
    rng = np.random.default_rng(20261117); results = {}

    def dedupe(idx, arcmin):
        X = ap.unit(RA[idx], DE[idx]); keep = np.ones(len(idx), bool); cth = np.cos(np.radians(arcmin/60))
        for i in range(len(idx)):
            if keep[i]: keep[np.where(X[i+1:] @ X[i] > cth)[0] + i + 1] = False
        return idx[keep]

    def stat(idx, nv, nshuf=1000, within=False, psi=None):
        psi = PSI[idx] if psi is None else psi
        nb = ap.neighbours(RA[idx], DE[idx], nv); ph = ap.transport_phases(RA[idx], DE[idx], nb)
        s = ap.S_D(psi, nb, ph); sh = []
        g = FLD[idx]; groups = [np.where(g == k)[0] for k in np.unique(g)]
        for _ in range(nshuf):
            if within:
                q = psi.copy()
                for j in groups: q[j] = q[rng.permutation(j)]
            else: q = rng.permutation(psi)
            sh.append(ap.S_D(q, nb, ph))
        sh = np.array(sh); return dict(N=len(idx), S=float(s), mu=float(sh.mean()), sd=float(sh.std()),
                                       z=float((s-sh.mean())/sh.std()), p=float((1+(sh >= s).sum())/(nshuf+1)))

    samples = {"|b|>20": base & (abs(b) > 20),
               "|b|>20, |RM|>20": base & (abs(b) > 20) & (np.abs(RM) > 20),
               "|b|>20, fracpol>0.03": base & (abs(b) > 20) & (FP > 0.03),
               "|b|>20, |RM|>20, fracpol>0.03": base & (abs(b) > 20) & (np.abs(RM) > 20) & (FP > 0.03)}
    for name, m in samples.items():
        for am in (2, 10, 60):
            idx = dedupe(np.where(m)[0], am)
            if len(idx) < 100: log(f"{name}, one per {am}': N={len(idx)} too small"); continue
            for nv in (10, 20, 40, 80):
                for within in (False, True):
                    r = stat(idx, nv, within=within); key = f"{name}|{am}arcmin|nv{nv}|{'within' if within else 'global'}"
                    results[key] = r
                    log(f"{key:60s} N={r['N']:5d} z={r['z']:+.2f} p={r['p']:.4f}")
    # controls on the main sample
    idx = dedupe(np.where(samples["|b|>20"])[0], 10)
    r = stat(idx, 20, psi=rng.uniform(0, np.pi, len(idx))); results["control_random"] = r
    log(f"CONTROL random angles: z={r['z']:+.2f} p={r['p']:.3f} (must not be significant)")
    X = ap.unit(RA[idx], DE[idx])
    for f_al in (0.05, 0.1, 0.2, 0.3, 0.5):
        psi_p = rng.uniform(0, np.pi, len(idx)); c0 = X[rng.integers(len(idx))]
        cap = np.where(X @ c0 > np.cos(np.radians(10)))[0]; sel = cap[rng.random(len(cap)) < f_al]
        i0 = cap[0] if len(cap) else 0
        psi_p[sel] = (1.0 + ap.bearing(RA[idx][sel], DE[idx][sel], RA[idx][i0], DE[idx][i0])
                      - ap.bearing(RA[idx][i0], DE[idx][i0], RA[idx][sel], DE[idx][sel]) + rng.normal(0, 0.2, len(sel))) % np.pi
        r = stat(idx, 20, psi=psi_p); results[f"planted_f{f_al}"] = dict(r, n_planted=int(len(sel)))
        log(f"PLANTED fraction {f_al} in a 10-deg cap ({len(sel)} sources): z={r['z']:+.2f} p={r['p']:.4f}")
    json.dump(results, open(os.path.join(OUT, "askap_results.json"), "w"), indent=1)
    log("DONE")

if __name__ == "__main__":
    try: main()
    except Exception: traceback.print_exc(file=LOG); traceback.print_exc()

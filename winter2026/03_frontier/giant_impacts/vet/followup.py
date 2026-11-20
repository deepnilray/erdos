"""Follow-up for giant-impact candidates, run in GitHub Actions (archives unreachable from the sandbox):
ASAS-SN Sky Patrol optical light curves and SIMBAD (astroquery) for each target. Outputs to followup/."""
import os, json, traceback
os.makedirs("followup", exist_ok=True)
T = {"G5792808347020475136": (220.96632, -76.19612), "G5808318474663998464": (252.21435, -69.41863),
     "J060000": (90.00308, -31.00781), "ASASSN-21qj": (123.847042, -38.989833)}
log = open("followup/followup_log.txt", "w")
def p(*a): s = " ".join(map(str, a)); print(s, flush=True); log.write(s + "\n"); log.flush()
try:
    from pyasassn.client import SkyPatrolClient
    c = SkyPatrolClient()
    for n, (ra, de) in T.items():
        try:
            r = c.cone_search(ra_deg=ra, dec_deg=de, radius=8, units="arcsec", download=True, catalog="master_list")
            p(n, "asas-sn sources:", len(r.catalog_info) if hasattr(r, "catalog_info") else "?")
            r.catalog_info.to_csv(f"followup/{n}_asassn_catalog.csv", index=False)
            r.data.to_csv(f"followup/{n}_asassn_lc.csv", index=False); p(n, "asas-sn rows:", len(r.data))
        except Exception as e: p(n, "ASAS-SN ERR", repr(e)[:300])
except Exception: p("ASAS-SN client failed:", traceback.format_exc()[-400:])
try:
    from astroquery.simbad import Simbad
    import astropy.units as u
    from astropy.coordinates import SkyCoord
    s = Simbad(); s.add_votable_fields("otype", "sp", "otypes")
    for n, (ra, de) in T.items():
        try:
            t = s.query_region(SkyCoord(ra, de, unit="deg"), radius=20 * u.arcsec)
            p(n, "SIMBAD:", "none" if t is None else len(t))
            if t is not None: t.write(f"followup/{n}_simbad.csv", format="csv", overwrite=True); p(t)
        except Exception as e: p(n, "SIMBAD ERR", repr(e)[:300])
except Exception: p("SIMBAD failed:", traceback.format_exc()[-400:])

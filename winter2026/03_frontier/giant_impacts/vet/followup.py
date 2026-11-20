"""Follow-up in GitHub Actions (CDS Strasbourg is down; uses the IDIA SIMBAD mirror listed in the CDS outage notice).
1. SIMBAD object types within 5 arcsec for every star in blindspot/d2_excess_variability_near.csv (detector 2 output) and the
   candidates, plus the control ASASSN-21qj (must be found). 2. ASAS-SN Sky Patrol light curves for the candidates (kept from v1)."""
import os, traceback, pandas as pd, numpy as np, pyvo, requests
from astropy.table import Table
os.makedirs("followup", exist_ok=True)
log = open("followup/followup_log.txt", "w")
def p(*a): s = " ".join(map(str, a)); print(s, flush=True); log.write(s + "\n"); log.flush()
class TS(requests.Session):
    def request(self, *a, **k): k.setdefault("timeout", 300); return super().request(*a, **k)
d2 = pd.read_csv("../blindspot/d2_excess_variability_near.csv")
T = pd.DataFrame({"uid": list(d2.uid) + [-1, -2, -3, -4], "ra": list(d2.ra) + [123.847042, 220.96632, 252.21435, 90.00308],
                  "dec": list(d2.dec) + [-38.989833, -76.19612, -69.41863, -31.00781]})
up = Table({"objid": T.uid.values.astype(int), "tra": T.ra.values, "tdec": T.dec.values})
q = ("SELECT t.objid, b.main_id, b.otype, b.sp_type, DISTANCE(POINT('ICRS',b.ra,b.dec),POINT('ICRS',t.tra,t.tdec))*3600 AS sep "
     "FROM TAP_UPLOAD.t AS t JOIN basic AS b "
     "ON CONTAINS(POINT('ICRS',b.ra,b.dec),CIRCLE('ICRS',t.tra,t.tdec,5./3600))=1")
for url in ("https://simbad.idia.ac.za/simbad/sim-tap", "https://simbad.harvard.edu/simbad/sim-tap", "https://simbad.cds.unistra.fr/simbad/sim-tap"):
    try:
        r = pyvo.dal.TAPService(url, session=TS()).run_sync(q, uploads={"t": up}).to_table().to_pandas()
        r.to_csv("followup/d2_simbad.csv", index=False); p("SIMBAD OK via", url, "rows", len(r))
        p("control ASASSN-21qj found:", bool((r.objid == -1).any()))
        try:
            o = pyvo.dal.TAPService(url, session=TS()).run_sync(
                "SELECT t.objid, o.otype FROM TAP_UPLOAD.t AS t JOIN basic AS b ON CONTAINS(POINT('ICRS',b.ra,b.dec),CIRCLE('ICRS',t.tra,t.tdec,5./3600))=1 "
                "JOIN otypes AS o ON o.oidref = b.oid", uploads={"t": up}).to_table().to_pandas()
            o.to_csv("followup/d2_simbad_alltypes.csv", index=False); p("all otypes rows", len(o))
        except Exception as e: p("otypes ERR", repr(e)[:200])
        break
    except Exception as e: p("SIMBAD ERR", url, repr(e)[:200])

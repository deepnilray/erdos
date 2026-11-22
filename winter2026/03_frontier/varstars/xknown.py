"""Cross-match candidate variables against known-variable catalogues. Usage: xknown.py cands.csv out.csv"""
import sys, numpy as np, pandas as pd, pyvo
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord; import astropy.units as u
from astropy.table import Table
CATS = {"VSX": "B/vsx/vsx", "ZTF_Chen2020": "J/ApJS/249/18/table2", "ASASSN_var": "II/366/catalog", "ATLAS_var": "J/AJ/156/241/table4",
        "Gaia_DR3_vari": "I/358/vclassre", "WISE_var": "J/ApJS/265/42/table1"}
R = 3.0
d = pd.read_csv(sys.argv[1]); c = SkyCoord(d.ra.values * u.deg, d.dec.values * u.deg)
cen = SkyCoord(np.median(d.ra) * u.deg, np.median(d.dec) * u.deg); rad = cen.separation(c).max().deg + 0.01
import requests
def viz(cat, ra, dec, rad):
    for server in ("vizier.cfa.harvard.edu", "vizier.idia.ac.za"):
        try:
            r = requests.get(f"https://{server}/viz-bin/asu-tsv", params={"-source": cat, "-c": f"{ra} {dec}", "-c.rd": rad,
                             "-out.max": "unlimited", "-out.add": "_RAJ2000,_DEJ2000", "-oc.form": "d"}, timeout=300)
            lines = [l for l in r.text.splitlines() if l and not l.startswith("#")]
            if len(lines) < 3: return [], [], []
            hdr = lines[0].split("\t"); rows = [l.split("\t") for l in lines[3:] if not l.startswith("---")]
            ir, idc = hdr.index("_RAJ2000"), hdr.index("_DEJ2000")
            lab = next((k for k in range(len(hdr)) if k not in (ir, idc)), 0)
            ra_ = [float(x[ir]) for x in rows if len(x) > max(ir, idc) and x[ir].strip()]
            de_ = [float(x[idc]) for x in rows if len(x) > max(ir, idc) and x[ir].strip()]
            lb = [x[lab].strip() for x in rows if len(x) > max(ir, idc) and x[ir].strip()]
            return ra_, de_, lb
        except Exception as e:
            print(cat, server, "failed", repr(e)[:80])
    raise RuntimeError("all mirrors failed")
for name, cat in CATS.items():
    try:
        ra_, de_, lb = viz(cat, cen.ra.deg, cen.dec.deg, rad)
        if not ra_: d[name] = ""; print(name, 0); continue
        kc = SkyCoord(np.array(ra_) * u.deg, np.array(de_) * u.deg); idx, s2, _ = c.match_to_catalog_sky(kc)
        d[name] = [lb[i] if s < R else "" for i, s in zip(idx, s2.arcsec)]
        print(name, len(ra_), "rows in area;", (s2.arcsec < R).sum(), "candidates matched", flush=True)
    except Exception as e: print(name, "ERROR", repr(e)[:120]); d[name] = "ERROR"
# Gaia DR3 vari_summary via ESA TAP (authoritative)
try:
    g = pyvo.dal.TAPService("https://gea.esac.esa.int/tap-server/tap")
    q = (f"SELECT s.source_id, s.ra, s.dec, v.in_vari_classification_result FROM gaiadr3.gaia_source AS s JOIN gaiadr3.vari_summary AS v "
         f"ON s.source_id=v.source_id WHERE 1=CONTAINS(POINT('ICRS',s.ra,s.dec),CIRCLE('ICRS',{cen.ra.deg},{cen.dec.deg},{rad}))")
    t = g.run_sync(q, maxrec=500000).to_table()
    kc = SkyCoord(np.array(t["ra"]) * u.deg, np.array(t["dec"]) * u.deg); idx, s2, _ = c.match_to_catalog_sky(kc)
    d["GaiaDR3_vari_summary"] = [str(t["source_id"][i]) if s < R else "" for i, s in zip(idx, s2.arcsec)]
    print("Gaia vari_summary", len(t), (s2.arcsec < R).sum())
except Exception as e: print("Gaia ERROR", e)
known_cols = [k for k in d.columns if k in CATS or k == "GaiaDR3_vari_summary"]
d["known_any"] = d[known_cols].fillna("").astype(str).apply(lambda r: any(x not in ("", "nan", "--", "ERROR") for x in r), axis=1)
d["xmatch_complete"] = ~(d[known_cols].astype(str) == "ERROR").any(axis=1)
d.to_csv(sys.argv[2], index=False); print("unknown:", (~d.known_any).sum(), "of", len(d))

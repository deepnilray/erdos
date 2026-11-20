"""
Run this on your own PC (the cloud sandbox and GitHub Actions cannot reach SIMBAD/VizieR at CDS).
It checks the giant-impact candidates against SIMBAD and against EVERY VizieR catalogue with a source within 5 arcsec,
and writes everything to impact_check_results.txt.

    pip install astroquery astropy
    python run_on_my_pc.py

Then send me impact_check_results.txt (or paste it).
"""
from astroquery.simbad import Simbad
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
import astropy.units as u

TARGETS = {
    "candidate 1  Gaia DR3 5792808347020475136": (220.96632, -76.19612),
    "candidate 2  Gaia DR3 5808318474663998464": (252.21435, -69.41863),
    "J060000      Gaia DR3 2891196718939580672": (90.00308, -31.00781),
    "CONTROL ASASSN-21qj (must show up)": (123.847042, -38.989833),
}
out = open("impact_check_results.txt", "w", encoding="utf-8")
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n")

sim = Simbad(); sim.add_votable_fields("otype", "sp_type", "otypes")
viz = Vizier(columns=["*"], row_limit=3)
for name, (ra, dec) in TARGETS.items():
    c = SkyCoord(ra, dec, unit="deg")
    p("=" * 100); p(name, f"RA {ra} Dec {dec}")
    try:
        t = sim.query_region(c, radius=20 * u.arcsec)
        if t is None or len(t) == 0: p("SIMBAD: nothing within 20 arcsec")
        else: p("SIMBAD:"); p(t)
    except Exception as e: p("SIMBAD ERROR:", repr(e))
    try:
        res = viz.query_region(c, radius=5 * u.arcsec, catalog=None)   # every catalogue with a match
        p(f"VizieR: {len(res)} tables with a source within 5 arcsec")
        for key in res.keys():
            title = res[key].meta.get("description", "")
            p(f"  {key:35s} {title[:100]}")
    except Exception as e: p("VizieR ERROR:", repr(e))
out.close()
print("\nWrote impact_check_results.txt")

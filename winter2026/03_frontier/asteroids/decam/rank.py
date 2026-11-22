import pandas as pd, numpy as np
from astropy.coordinates import SkyCoord, GeocentricTrueEcliptic; import astropy.units as u
d = pd.read_parquet("decam_ecliptic.parquet")
d["t"] = pd.to_datetime(d.dateobs_center, utc=True, format="ISO8601"); d["rel"] = pd.to_datetime(d.release_date)
d = d[d.rel <= "2026-11-22"]
ec = SkyCoord(d.ra_center.values * u.deg, d.dec_center.values * u.deg).transform_to(GeocentricTrueEcliptic())
d["beta"] = ec.lat.deg; d = d[np.abs(d.beta) < 10]
d["band"] = d.ifilter.fillna("?").astype(str).str[0]
d["px"] = (d.ra_center * np.cos(np.radians(d.dec_center)) / 0.3).round().astype(int); d["py"] = (d.dec_center / 0.3).round().astype(int)
g = d.groupby(["proposal", "px", "py", "caldat"]).agg(n=("t", "size"), t0=("t", "min"), t1=("t", "max"), exp=("exposure", "median"),
        bands=("band", lambda b: "".join(sorted(set(b)))), ra=("ra_center", "median"), dec=("dec_center", "median"), beta=("beta", "median")).reset_index()
g["span_min"] = (g.t1 - g.t0).dt.total_seconds() / 60
q = g[(g.n >= 3) & (g.span_min >= 20)].copy()
q["date"] = pd.to_datetime(q.caldat)
res = []
for (p, x, y), s in q.groupby(["proposal", "px", "py"]):
    dates = np.sort(s.date.values.astype("datetime64[D]").astype(int))
    # longest run of qualifying nights each <= 7 days from the previous
    best, run = 1, 1
    for i in range(1, len(dates)):
        run = run + 1 if dates[i] - dates[i - 1] <= 7 else 1; best = max(best, run)
    res.append(dict(proposal=p, ra=s.ra.median(), dec=s.dec.median(), beta=s.beta.median(), nights=len(s), linked_nights=best,
                    exp_per_night=int(s.n.median()), exptime=float(s.exp.median()), span_min=float(s.span_min.median()), bands="".join(sorted(set("".join(s.bands)))),
                    first=str(s.date.min().date()), last=str(s.date.max().date())))
R = pd.DataFrame(res)
P = R[R.linked_nights >= 2].groupby("proposal").agg(fields=("ra", "size"), max_linked=("linked_nights", "max"), med_linked=("linked_nights", "median"),
        exp_per_night=("exp_per_night", "median"), exptime=("exptime", "median"), span_min=("span_min", "median"), bands=("bands", "first"),
        first=("first", "min"), last=("last", "max"), beta=("beta", "median")).reset_index()
P["score"] = P.fields * P.med_linked * np.minimum(P.exptime, 300) / 100
P = P.sort_values("score", ascending=False)
R.to_csv("pointings.csv", index=False); P.to_csv("programs.csv", index=False)
print(len(d), "public ecliptic exposures;", len(R), "pointings with a 3+-exposure night;", len(P), "programs with >=2 linked nights")
print(P.head(30).to_string())

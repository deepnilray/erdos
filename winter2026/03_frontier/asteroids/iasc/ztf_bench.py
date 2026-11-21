"""
Run iasc_hunt.py (detect + link) and synth.py (shift-and-stack) on public ZTF science-image sets and score them against
known asteroids (SkyBoT at the set mid-time, observer I41).

Set layout (one directory per set, downloads never in the repo):
  <root>/<set>/ztf_..._sciimg.fits         IBE cutouts of one field/CCD/quadrant/filter, one night
  <root>/<set>/mask/ztf_..._sciimg.fits    the matching _mskimg cutout, saved under the SCIENCE file name
  <root>/sets.json                          set list written by the selection step (see ZTF.md)

Subcommands (python3 -I):
  link     --root R --out O [--only Z1,Z2]  stage 1 + linking + truth; per set: objects.csv, tracklets.csv, detections.csv,
                                            cutouts of unidentified tracklets, measure cache (pickle) in <root>/cache
  synth    --root R --out O [--only ...]    runs synth.py per set (json + review cutouts)
  report   --out O                          joins both, writes recovery tables / noise / candidates (summary.json, *.csv)
  horizons --out O --n 25                   O-C of linker positions of numbered recovered objects vs JPL Horizons (I41)

Truth: SkyBoT objects whose linearly propagated position lands on good (unmasked) pixels in >= the linker's minimum
number of images, max(3, ceil(MIN_NFRAC * n)).
"""
import sys, os, json, time, argparse, pickle, csv, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import iasc_hunt as H

HERE = os.path.dirname(os.path.abspath(__file__))

def sets_in(root, only):
    S = json.load(open(os.path.join(root, "sets.json")))
    return [s for s in S if not only or s["label"] in only.split(",")]

def measure_cached(root, s):
    cd = os.path.join(root, "cache", s["label"]); os.makedirs(cd, exist_ok=True)
    p = os.path.join(cd, "measure.pkl")
    if os.path.exists(p):
        H.use_params(H.ZTF_PARAMS); return pickle.load(open(p, "rb"))
    def gaia(ra, dec, rad):
        g = os.path.join(cd, "gaia.pkl")
        if os.path.exists(g): return pickle.load(open(g, "rb"))
        t = H.gaia_stars(ra, dec, rad); pickle.dump(t, open(g, "wb")); return t
    ims, D, info, cen, rad = H.measure(os.path.join(root, s["label"]), gaia_fn=gaia, verbose=False)
    meta = []
    for im in ims:
        good = ~H.gap_mask(im["data"], im["style"], im.get("mask"))
        meta.append(dict(file=im["file"], t_mjd=im["t"].mjd, isot=im["t"].isot, shape=im["data"].shape, finite=good,
                         seeing=float(im["hdr"].get("SEEING", np.nan)), maglim_hdr=float(im["hdr"].get("MAGLIM", np.nan)),
                         magzp_hdr=float(im["hdr"].get("MAGZP", np.nan))))
    subs = [d.pop("sub") for d in D]
    m = dict(D=D, info=info, cen=(cen.ra.deg, cen.dec.deg), rad=rad, meta=meta)
    pickle.dump(m, open(p, "wb"))
    for d, sb in zip(D, subs): d["sub"] = sb
    return m

def skybot_cached(root, s, m):
    p = os.path.join(root, "cache", s["label"], "skybot.json")
    if os.path.exists(p): return json.load(open(p))
    tmid = np.mean([x["t_mjd"] for x in m["meta"]]) + 2400000.5
    rows, raw = H.skybot(m["cen"][0], m["cen"][1], tmid, m["rad"], observer="I41")
    out = dict(rows=rows, head=raw, tmid_jd=tmid); json.dump(out, open(p, "w")); return out

def truth(m, sky, nmin):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    tmid = np.mean([x["t_mjd"] for x in m["meta"]]); out = []
    for o in sky["rows"]:
        on, pos = [], []
        for d, mt in zip(m["D"], m["meta"]):
            dt_h = (mt["t_mjd"] - tmid) * 24
            dec = o["dec"] + o["ddec_arcsec_h"] * dt_h / 3600; ra = o["ra"] + o["dra_arcsec_h"] * dt_h / 3600 / np.cos(np.radians(o["dec"]))
            x, y = d["w"].world_to_pixel(SkyCoord(ra * u.deg, dec * u.deg)); x, y = float(x), float(y)
            ny, nx = mt["shape"]; xi, yi = int(round(x)), int(round(y))
            on.append(bool(5 <= xi < nx - 5 and 5 <= yi < ny - 5 and mt["finite"][yi, xi])); pos.append((ra, dec, x, y))
        if sum(on) >= nmin:
            out.append(dict(o, on=on, pos=pos, rate=float(np.hypot(o["dra_arcsec_h"], o["ddec_arcsec_h"]) / 60)))
    return out

def plot_tracklet(path, title, D, members, n):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    k0 = sorted(members)[0]; k1 = sorted(members)[-1]
    c0, c1 = D[k0]["sky"][members[k0]], D[k1]["sky"][members[k1]]
    fig, axs = plt.subplots(1, n, figsize=(1.5 * n, 1.9))
    for k in range(n):
        ax = axs[k]; ax.set_xticks([]); ax.set_yticks([])
        if k in members: c = D[k]["sky"][members[k]]
        else:   # interpolate where the tracklet should be
            from astropy.coordinates import SkyCoord
            T = [D[j]["t_min"] for j in range(n)]; f = (T[k] - T[k0]) / (T[k1] - T[k0])
            c = SkyCoord(c0.ra + f * (c1.ra - c0.ra), c0.dec + f * (c1.dec - c0.dec))
        x, y = D[k]["w"].world_to_pixel(c); x, y = int(round(float(x))), int(round(float(y)))
        cut = D[k]["sub"][max(0, y - 15):y + 16, max(0, x - 15):x + 16]
        if cut.size: ax.imshow(cut, origin="lower", cmap="gray", vmin=-2 * np.std(cut), vmax=6 * np.std(cut))
        ax.set_title(f"{k}{'' if k in members else ' (pred)'}", fontsize=6)
    fig.suptitle(title, fontsize=7); plt.tight_layout(); plt.savefig(path, dpi=70); plt.close()

def cmd_link(a):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    for s in sets_in(a.root, a.only):
        t0 = time.time(); od = os.path.join(a.out, s["label"]); os.makedirs(od, exist_ok=True)
        m = measure_cached(a.root, s); sky = skybot_cached(a.root, s, m); n = len(m["D"])
        H.use_params(H.ZTF_PARAMS)
        nmin = max(3, int(np.ceil(H.MIN_NFRAC * n)))
        T = np.array([x["t_mjd"] for x in m["meta"]]) * 1440.0
        uniq = H.find_tracklets(m["D"], T, verbose=False)
        tmid = np.mean([x["t_mjd"] for x in m["meta"]])
        H.identify(uniq, m["D"], T, tmid, sky["rows"])
        tru = truth(m, sky, nmin); rec = {tr["known"]: tr for tr in uniq if tr["known"]}
        lim5 = float(np.nanmedian([i.get("lim5_emp", np.nan) for i in m["info"]]))
        rows = []
        for o in tru:
            tr = rec.get(o["name"])
            row = dict(set=s["label"], name=o["name"], num=o["num"], cls=o["cls"], V=o["V"], rate=o["rate"], n_on=sum(o["on"]),
                       pos_err=o["err_arcsec"], lim5=lim5, recovered=tr is not None, ra_mid=o["ra"], dec_mid=o["dec"])
            if tr is not None:
                oc = []; meas = []
                for k, i in sorted(tr["members"].items()):
                    c = m["D"][k]["sky"][i]; ra, dec = o["pos"][k][0], o["pos"][k][1]
                    oc.append(float(c.separation(SkyCoord(ra * u.deg, dec * u.deg)).arcsec))
                    meas.append([m["meta"][k]["t_mjd"], float(c.ra.deg), float(c.dec.deg), ra, dec, float(m["D"][k]["mag"][i])])
                row.update(n_det=tr["n"], mag_meas=tr["mag"], oc_skybot_med=float(np.median(oc)), meas=json.dumps(meas))
            else:
                row.update(H_diag(m, o))
            rows.append(row)
        write_csv(os.path.join(od, "objects.csv"), rows)
        trows = []
        for j, tr in enumerate(uniq):
            k0 = sorted(tr["members"])[0]; k1 = sorted(tr["members"])[-1]
            c0, c1 = m["D"][k0]["sky"][tr["members"][k0]], m["D"][k1]["sky"][tr["members"][k1]]
            f = (tmid * 1440 - T[k0]) / (T[k1] - T[k0])
            ram, dem = c0.ra.deg + f * (c1.ra.deg - c0.ra.deg), c0.dec.deg + f * (c1.dec.deg - c0.dec.deg)
            trows.append(dict(set=s["label"], id=f"{s['label']}_T{j:03d}", n=tr["n"], n_images=n, rate=tr["rate"], pa=tr["pa"], resid=tr["resid"],
                              mag=tr["mag"], ra_mid=ram, dec_mid=dem, known=tr["known"], known_sep=tr["known_sep"], known_V=tr["known_V"],
                              members=json.dumps(tr["members"])))
            if not tr["known"]:
                for k in range(n): m["D"][k]["t_min"] = T[k]
                if "sub" not in m["D"][0]: m_sub(a.root, s, m)
                plot_tracklet(os.path.join(od, f"{s['label']}_T{j:03d}.png"), f"{s['label']}_T{j:03d} UNIDENTIFIED rate {tr['rate']:.2f}\"/min r {tr['mag']:.1f} n={tr['n']}/{n}",
                              m["D"], tr["members"], n)
        write_csv(os.path.join(od, "tracklets.csv"), trows)
        json.dump(dict(set=s["label"], n_images=n, nmin=nmin, lim5=lim5, info=m["info"], n_tracklets=len(uniq),
                       n_unknown=sum(1 for t in uniq if not t["known"]), n_truth=len(tru), n_rec=sum(r["recovered"] for r in rows),
                       n_skybot=len(sky["rows"]), tmid_jd=sky.get("tmid_jd"), seconds=round(time.time() - t0, 1)),
                  open(os.path.join(od, "link_summary.json"), "w"), indent=1, default=float)
        print(s["label"], f"n={n} truth={len(tru)} rec={sum(r['recovered'] for r in rows)} tracklets={len(uniq)} "
              f"unknown={sum(1 for t in uniq if not t['known'])} lim5={lim5:.2f} {time.time() - t0:.0f}s", flush=True)

def m_sub(root, s, m):
    """Re-create background-subtracted images (dropped from the pickle) for cutouts."""
    ims = H.load(os.path.join(root, s["label"]))
    for im, d in zip(ims, m["D"]): d["sub"] = H.detect(im)["sub"]

def H_diag(m, o):
    import bench
    try: return bench.diagnose(m, o, H)
    except Exception as e: return dict(why=f"diag_error {e}")

def cmd_synth(a):
    for s in sets_in(a.root, a.only):
        od = os.path.join(a.out, s["label"]); os.makedirs(od, exist_ok=True)
        out = os.path.join(od, "synth.json")
        if os.path.exists(out) and not a.force: print(s["label"], "synth cached"); continue
        t0 = time.time()
        r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "synth.py"), os.path.join(a.root, s["label"]), out,
                            "--maps", os.path.join(a.root, "cache", s["label"], "synth_maps.npz")], capture_output=True, text=True)
        open(os.path.join(od, "synth.log"), "w").write(r.stdout + r.stderr)
        print(s["label"], "synth rc", r.returncode, f"{time.time() - t0:.0f}s", flush=True)

def wilson(k, n):
    if not n: return (np.nan, np.nan)
    z = 1.0; p = k / n; c = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (c - h, c + h)

def cmd_report(a):
    import synth as SY
    sets = sorted(d for d in os.listdir(a.out) if os.path.exists(os.path.join(a.out, d, "objects.csv")))
    O, per_set, cands = [], [], []
    for sname in sets:
        od = os.path.join(a.out, sname)
        objs = list(csv.DictReader(open(os.path.join(od, "objects.csv"))))
        trk = list(csv.DictReader(open(os.path.join(od, "tracklets.csv")))) if os.path.getsize(os.path.join(od, "tracklets.csv")) else []
        ls = json.load(open(os.path.join(od, "link_summary.json")))
        sj = os.path.join(od, "synth.json"); sy = json.load(open(sj)) if os.path.exists(sj) else None
        found_s = {t["name"]: t for t in (sy["truth"] if sy else []) if t["found"]}
        for o in objs:
            o["V"] = float(o["V"]); o["rate"] = float(o["rate"]); o["recovered"] = o["recovered"] == "True"
            o["synth"] = o["name"] in found_s if sy else None
            o["synth_score"] = found_s[o["name"]]["score"] if o["name"] in found_s else None
            O.append(o)
        rev = [c for c in (sy["cands"] if sy else []) if c["score"] >= SY.REPORT_MIN and not c.get("known")]
        scr = [c for c in (sy["scrambled"] if sy else []) if c["score"] >= SY.REPORT_MIN]
        unk = [t for t in trk if not t["known"]]
        per_set.append(dict(set=sname, n_images=ls["n_images"], lim5=round(ls["lim5"], 2), n_truth=ls["n_truth"], link_rec=ls["n_rec"],
                            synth_rec=sum(o["synth"] for o in objs if o["synth"]) if sy else None, link_unknown=len(unk),
                            synth_review=len(rev), synth_scrambled_review=len(scr),
                            synth_cand=sy["n_cand"] if sy else None, synth_cand_scrambled=sy["n_cand_scrambled"] if sy else None,
                            synth_seconds=sy["seconds"] if sy else None, n_vel=sy["n_velocities"] if sy else None))
        for t in unk:
            cands.append(dict(set=sname, id=t["id"], method="link", ra=float(t["ra_mid"]), dec=float(t["dec_mid"]), tmid_jd=ls["tmid_jd"],
                              rate=float(t["rate"]), pa=float(t["pa"]), mag=float(t["mag"]), n=f"{t['n']}/{t['n_images']}", score=None))
        for c in rev:
            cands.append(dict(set=sname, id=f"{sname}_{c['id']}", method="synth", ra=c["ra"], dec=c["dec"], tmid_jd=sy.get("tref_jd") or ls["tmid_jd"],
                              rate=c["rate"], pa=float(np.degrees(np.arctan2(-c["vx"], c["vy"])) % 360), mag=None, n=None, score=c["score"],
                              per_image=c["per_image"]))
    edges = [14, 17, 18, 19, 19.5, 20, 20.5, 21, 21.5, 22, 25]
    tab = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        b = [o for o in O if lo <= o["V"] < hi]; n = len(b)
        kl = sum(o["recovered"] for o in b); ks = sum(bool(o["synth"]) for o in b); ku = sum(o["recovered"] or bool(o["synth"]) for o in b)
        tab.append(dict(V=f"{lo}-{hi}", n=n, link=kl, synth=ks, either=ku, link_frac=round(kl / n, 2) if n else None,
                        synth_frac=round(ks / n, 2) if n else None, either_frac=round(ku / n, 2) if n else None))
    whys = {}
    for o in O:
        if not o["recovered"] and o["V"] < 20.5: whys[o.get("why", "?")] = whys.get(o.get("why", "?"), 0) + 1
    oc = [json.loads(o["meas"]) for o in O if o["recovered"] and o.get("meas")]
    summ = dict(sets=per_set, by_V=tab, link_miss_why_V_lt_20_5=whys, n_truth=len(O))
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1, default=float)
    write_csv(os.path.join(a.out, "objects_all.csv"), O); write_csv(os.path.join(a.out, "candidates.csv"), cands)
    print(json.dumps(summ, indent=1, default=float))

def cmd_horizons(a):
    from astroquery.jplhorizons import Horizons
    from astropy.coordinates import SkyCoord
    import astropy.units as u, random
    rows = [r for r in csv.DictReader(open(os.path.join(a.out, "objects_all.csv"))) if r["recovered"] == "True" and r["num"] not in ("-", "") and r.get("meas")]
    random.Random(0).shuffle(rows); rows = rows[:a.n]; out = []
    for r in rows:
        meas = json.loads(r["meas"]); jd = [x[0] + 2400000.5 for x in meas]
        try: eph = Horizons(id=r["num"], id_type="smallbody", location="I41", epochs=jd).ephemerides(extra_precision=True)
        except Exception as e: print("horizons fail", r["name"], e); continue
        for x, e in zip(meas, eph):
            h = SkyCoord(float(e["RA"]) * u.deg, float(e["DEC"]) * u.deg); c = SkyCoord(x[1] * u.deg, x[2] * u.deg)
            dra = (x[1] - float(e["RA"])) * 3600 * np.cos(np.radians(x[2])); dde = (x[2] - float(e["DEC"])) * 3600
            vx, vy = float(e["RA_rate"]), float(e["DEC_rate"]); vn = np.hypot(vx, vy) or 1
            out.append(dict(set=r["set"], name=r["name"], num=r["num"], V=r["V"], t_mjd=x[0], oc=h.separation(c).arcsec,
                            along=(dra * vx + dde * vy) / vn, cross=(-dra * vy + dde * vx) / vn,
                            skybot_minus_horizons=h.separation(SkyCoord(x[3] * u.deg, x[4] * u.deg)).arcsec, mag_meas=x[5], V_horizons=float(e["V"])))
        print(r["set"], r["name"], f"median O-C {np.median([o['oc'] for o in out if o['name'] == r['name']]):.3f}", flush=True)
        time.sleep(1)
    write_csv(os.path.join(a.out, "horizons_check.csv"), out)
    print("positions", len(out), "objects", len(set(o["name"] for o in out)), "median O-C", np.median([o["oc"] for o in out]),
          "median along", np.median([o["along"] for o in out]), "median cross", np.median([o["cross"] for o in out]),
          "median |SkyBoT-Horizons|", np.median([o["skybot_minus_horizons"] for o in out]))

def mpcheck(ra, dec, jd, radius=5, code="I41"):
    """MPC MPChecker (orbit catalogue, not the isolated tracklet file). Returns parsed rows and the raw object lines."""
    import requests, re, html
    from astropy.time import Time
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    t = Time(jd, format="jd").datetime; day = t.day + (t.hour + (t.minute + t.second / 60) / 60) / 24
    c = SkyCoord(ra * u.deg, dec * u.deg)
    data = dict(year=t.year, month=f"{t.month:02d}", day=f"{day:.3f}", which="pos", ra=c.ra.to_string(unit=u.hourangle, sep=" ", precision=1, pad=True),
                decl=c.dec.to_string(unit=u.deg, sep=" ", precision=0, alwayssign=True, pad=True), TextArea="", radius=radius, limit="24.0",
                oc=code, sort="d", mot="h", tmot="s", pdes="u", needed="f", ps="n", type="p")
    r = requests.post("https://minorplanetcenter.net/cgi-bin/mpcheck.cgi", data=data, timeout=120)
    txt = html.unescape(re.sub(r"<[^>]+>", "", r.text)); rows = []
    for line in txt.splitlines():
        m = re.match(r"^\s*(\(\d+\)\s+\S+(?:\s\S+)?|\d{4} [A-Z]{2}\d*|\S+)\s+(\d\d \d\d \d\d\.\d)\s+([+-]\d\d \d\d \d\d)\s+(\d+\.\d|\s*)\s+([\d.]+[EW])\s+([\d.]+[NS])\s+(\d+[+-])\s+(\d+[+-])", line)
        if not m: continue
        oc = SkyCoord(m.group(2), m.group(3), unit=(u.hourangle, u.deg))
        mra = float(m.group(7)[:-1]) * (1 if m.group(7)[-1] == "+" else -1); mde = float(m.group(8)[:-1]) * (1 if m.group(8)[-1] == "+" else -1)
        rows.append(dict(name=m.group(1).strip(), sep_arcsec=float(c.separation(oc).arcsec), V=m.group(4).strip(),
                         rate_arcsec_min=float(np.hypot(mra, mde) / 60), line=line.strip()))
    none = "No known minor planets" in txt or ("were found" not in txt and not rows)
    return dict(rows=sorted(rows, key=lambda x: x["sep_arcsec"]), none_found=none, head=txt[txt.find("The following"):][:200] if "The following" in txt else txt[:300])

def cmd_mpcheck(a):
    C = list(csv.DictReader(open(os.path.join(a.out, "candidates.csv"))))
    out = []
    for c in C:
        if a.ids and c["id"] not in a.ids.split(","): continue
        r = mpcheck(float(c["ra"]), float(c["dec"]), float(c["tmid_jd"]))
        near = r["rows"][0] if r["rows"] else None
        out.append(dict(id=c["id"], method=c["method"], ra=c["ra"], dec=c["dec"], tmid_jd=c["tmid_jd"], rate=c["rate"], n_listed=len(r["rows"]),
                        nearest=near["name"] if near else "", nearest_sep_arcsec=round(near["sep_arcsec"], 1) if near else "",
                        nearest_V=near["V"] if near else "", nearest_rate=round(near["rate_arcsec_min"], 3) if near else "", head=r["head"][:150]))
        print(out[-1], flush=True); time.sleep(3)
    write_csv(os.path.join(a.out, "mpcheck.csv"), out)

def write_csv(path, rows):
    keys = []
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); [w.writerow(r) for r in rows]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for c in ("link", "synth"):
        p = sp.add_parser(c); p.add_argument("--root", required=True); p.add_argument("--out", required=True); p.add_argument("--only", default="")
        p.add_argument("--force", action="store_true")
    p = sp.add_parser("report"); p.add_argument("--out", required=True)
    p = sp.add_parser("horizons"); p.add_argument("--out", required=True); p.add_argument("--n", type=int, default=25)
    p = sp.add_parser("mpcheck"); p.add_argument("--out", required=True); p.add_argument("--ids", default="")
    a = ap.parse_args(); dict(link=cmd_link, synth=cmd_synth, report=cmd_report, horizons=cmd_horizons, mpcheck=cmd_mpcheck)[a.cmd](a)

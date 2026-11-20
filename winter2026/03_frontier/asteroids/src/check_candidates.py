"""Step 4: independent known-object checks for unmatched tracklets.

For each candidate (tracklet with no SkyBoT match), at the tracklet mid-time:
  * JPL sb_ident (two-pass, n-body), FOV half-width 0.03 deg, obs code W84
  * MPC MPChecker (minorplanetcenter.net/cgi-bin/mpcheck.cgi), radius 2', V<=25.5
Both report every catalogued object near the predicted position; a candidate is
'identified' if an object lies within max(10", 3x its stated uncertainty) and
moves at a consistent rate.
usage: python check_candidates.py TAG [--min-n 4]
"""
import os, re, json, argparse, time
import numpy as np, pandas as pd, requests
from astropy.time import Time
from tap import sb_ident, CACHE, _key

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def sexa_ra(ra):
    h = ra / 15
    hh = int(h); mm = int((h - hh) * 60); ss = ((h - hh) * 60 - mm) * 60
    return f'{hh:02d}-{mm:02d}-{ss:05.2f}', f'{hh:02d} {mm:02d} {ss:05.2f}'


def sexa_dec(dec):
    s = 'M' if dec < 0 else ''
    sg = '-' if dec < 0 else '+'
    d = abs(dec)
    dd = int(d); mm = int((d - dd) * 60); ss = ((d - dd) * 60 - mm) * 60
    return f'{s}{dd:02d}-{mm:02d}-{ss:04.1f}', f'{sg}{dd:02d} {mm:02d} {ss:04.1f}'


def mid_state(d):
    """RA, Dec, mid time and rates (deg/day) from the tracklet detections."""
    t = d.tmid.values
    tm = t.mean()
    A = np.vstack([np.ones_like(t), t - tm]).T
    cosd = np.cos(np.radians(d.dec.mean()))
    cr, *_ = np.linalg.lstsq(A, d.ra.values, rcond=None)
    cd, *_ = np.linalg.lstsq(A, d.dec.values, rcond=None)
    return cr[0], cd[0], tm, cr[1] * cosd, cd[1]


def jpl_check(ra, dec, mjd):
    p = {'mpc-code': 'W84', 'obs-time': f'{mjd + 2400000.5:.5f}',
         'fov-ra-center': sexa_ra(ra)[0], 'fov-dec-center': sexa_dec(dec)[0],
         'fov-ra-hwidth': '0.03', 'fov-dec-hwidth': '0.03', 'two-pass': 'true',
         'suppress-first-pass': 'true', 'mag-required': 'false'}
    js = json.loads(sb_ident(p))
    rows = []
    for r in js.get('data_second_pass', []) or []:
        rows.append(dict(name=r[0], dra_arcsec=float(r[3]), ddec_arcsec=float(r[4]),
                         sep=float(r[5]), V=r[6], rate_ra=r[7], rate_dec=r[8]))
    return rows, js.get('n_second_pass', 0)


def mpc_check(ra, dec, mjd):
    t = Time(mjd, format='mjd')
    y, mo = t.datetime.year, t.datetime.month
    day = t.datetime.day + (t.mjd % 1)
    data = dict(year=str(y), month=f'{mo:02d}', day=f'{day:.2f}', which='pos',
                ra=sexa_ra(ra)[1], decl=sexa_dec(dec)[1], TextArea='', radius='2',
                limit='25.5', oc='W84', sort='d', mot='h', tmot='s', pdes='u',
                needed='f', ps='n', type='p')
    fn = os.path.join(CACHE, 'mpcheck_' + _key(sorted(data.items())) + '.html')
    if os.path.exists(fn):
        txt = open(fn).read()
    else:
        txt = None
        for i in range(3):
            try:
                r = requests.post('https://minorplanetcenter.net/cgi-bin/mpcheck.cgi',
                                  data=data, timeout=90)
                if r.status_code == 200:
                    txt = r.text
                    break
            except Exception as e:
                print('mpcheck error', e)
            time.sleep(5)
        if txt is None:
            return None, 'unreachable'
        open(fn, 'w').write(txt)
        time.sleep(2)
    if 'No known minor planets' in txt:
        return [], 'none'
    pre = re.findall(r'<pre>(.*?)</pre>', txt, re.S | re.I)
    rows = []
    for block in pre:
        for line in block.splitlines():
            # object lines: designation, RA, Dec, V, offsets ...
            m = re.match(r'\s*(.{24})\s+(\d\d \d\d [\d.]+)\s+([+-]\d\d \d\d [\d.]+)\s+([\d.]+)?\s+([\d.]+[EW])\s+([\d.]+[NS])\s+(\d+)([+-])\s+(\d+)([+-])', line)
            if m:
                ew = float(m.group(5)[:-1]) * (1 if m.group(5)[-1] == 'E' else -1)
                ns = float(m.group(6)[:-1]) * (1 if m.group(6)[-1] == 'N' else -1)
                rows.append(dict(name=re.sub('<[^>]+>', '', m.group(1)).strip(),
                                 V=m.group(4), off_E_arcmin=ew, off_N_arcmin=ns,
                                 sep=60 * np.hypot(ew, ns), line=line.strip(),
                                 mot_ra=float(m.group(7)) * (1 if m.group(8) == '+' else -1),
                                 mot_dec=float(m.group(9)) * (1 if m.group(10) == '+' else -1)))
    return rows, 'ok'


def main(tag, top, jpl, tiers='AB'):
    c = pd.read_csv(os.path.join(DATA, f'{tag}_candidates.csv'))
    dd = pd.read_csv(os.path.join(DATA, f'{tag}_dets_classified.csv'))
    c = c[c.tier.isin(list(tiers))]
    # one tracklet per candidate object (earliest night), best-ranked first
    order = c.drop_duplicates('cand_id').cand_id.values[:top]
    cand = c[c.cand_id.isin(order)].sort_values('night').drop_duplicates('cand_id')
    out = []
    g = {k: v for k, v in dd.groupby('tracklet')}
    for r in cand.itertuples():
        d = g[r.tracklet]
        ra, dec, tm, vra, vdec = mid_state(d)
        if jpl:
            try:
                jrows, nj = jpl_check(ra, dec, tm)
            except Exception as e:
                print('JPL failed', e)
                jrows, nj = [], 'timeout'
        else:
            jrows, nj = [], 'not run'
        jbest = min(jrows, key=lambda x: x['sep']) if jrows else None
        mrows, mstat = mpc_check(ra, dec, tm)
        mbest = min(mrows, key=lambda x: x['sep']) if mrows else None
        # identification: within 30" (MPChecker prints offsets to 0.1') AND motion
        # within 3"/h in both coordinates of the tracklet's rate
        vr, vd = vra * 3600 / 24, vdec * 3600 / 24
        ident = [x['name'] for x in (mrows or []) if x['sep'] <= 30 and
                 abs(x['mot_ra'] - vr) < 3 and abs(x['mot_dec'] - vd) < 3]
        # weaker: within the 2' search radius with motion within 2"/h (a catalogued
        # object with a poor orbit, e.g. a short arc, can be off by arcminutes)
        poss = [x['name'] for x in (mrows or []) if abs(x['mot_ra'] - vr) < 2 and
                abs(x['mot_dec'] - vd) < 2 and x['name'] not in ident]
        out.append(dict(cand_id=r.cand_id, tier=r.tier, tracklet=r.tracklet, ra_mid=ra, dec_mid=dec, mjd_mid=tm,
                        rate_ra_degday=vra, rate_dec_degday=vdec,
                        jpl_n=nj, jpl_nearest=jbest['name'] if jbest else None,
                        jpl_sep_arcsec=jbest['sep'] if jbest else np.nan,
                        mpc_status=mstat, mpc_n=len(mrows) if mrows else 0,
                        mpc_nearest=mbest['name'] if mbest else None,
                        mpc_sep_arcsec=mbest['sep'] if mbest else np.nan,
                        mpc_nearest_motion=(mbest['mot_ra'], mbest['mot_dec']) if mbest else None,
                        cand_motion=(round(vr, 1), round(vd, 1)),
                        mpc_identified=';'.join(ident) if ident else None,
                        mpc_possible=';'.join(poss) if poss else None))
        print(out[-1], flush=True)
    res = pd.DataFrame(out)
    res.to_csv(os.path.join(DATA, f'{tag}_candidate_checks.csv'), index=False)
    print('checked', len(res))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('tag')
    ap.add_argument('--top', type=int, default=40)
    ap.add_argument('--jpl', action='store_true')
    ap.add_argument('--tiers', default='AB')
    a = ap.parse_args()
    main(a.tag, a.top, a.jpl, a.tiers)

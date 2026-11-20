"""Cached, retrying helpers for NOIRLab Data Lab TAP, SkyBoT and JPL sb_ident."""
import hashlib, io, os, time
import requests
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '..', 'cache')
os.makedirs(CACHE, exist_ok=True)
TAP = 'https://datalab.noirlab.edu/tap/sync'


def _key(*parts):
    return hashlib.sha1('|'.join(map(str, parts)).encode()).hexdigest()[:20]


def _get(url, params=None, data=None, timeout=100, tries=4):
    last = None
    for i in range(tries):
        try:
            if data is not None:
                r = requests.post(url, data=data, timeout=timeout)
            else:
                r = requests.get(url, params=params, timeout=timeout)
            if r.status_code == 200:
                return r.text
            last = f'HTTP {r.status_code}: {r.text[:300]}'
        except Exception as e:  # network error
            last = repr(e)
        time.sleep(3 * (i + 1))
    raise RuntimeError(f'request failed after {tries} tries: {last}')


def tap(query, timeout=110):
    """Run an ADQL query on Data Lab TAP, cache CSV by query hash."""
    fn = os.path.join(CACHE, 'tap_' + _key(query) + '.csv')
    if os.path.exists(fn):
        return pd.read_csv(fn)
    txt = _get(TAP, data=dict(REQUEST='doQuery', LANG='ADQL', FORMAT='csv',
                              QUERY=query), timeout=timeout)
    if txt.lstrip().startswith('<'):
        raise RuntimeError('TAP error: ' + txt[:500])
    with open(fn, 'w') as f:
        f.write(txt)
    return pd.read_csv(io.StringIO(txt))


SKYBOT = 'https://ssp.imcce.fr/webservices/skybot/api/conesearch.php'


def skybot(jd, ra, dec, rad_deg, loc='W84'):
    """SkyBoT cone search. Returns DataFrame of known objects (may be empty)."""
    p = {'-ep': f'{jd:.6f}', '-ra': f'{ra:.5f}', '-dec': f'{dec:.5f}',
         '-rd': f'{rad_deg:.4f}', '-mime': 'text', '-output': 'all',
         '-loc': loc, '-filter': '0', '-objFilter': '111', '-refsys': 'EQJ2000',
         '-from': 'erdos-student-pipeline'}
    fn = os.path.join(CACHE, 'skybot_' + _key(sorted(p.items())) + '.txt')
    if os.path.exists(fn):
        txt = open(fn).read()
    else:
        txt = _get(SKYBOT, params=p, timeout=90)
        with open(fn, 'w') as f:
            f.write(txt)
    lines = [l for l in txt.splitlines() if l.strip()]
    hdr = None
    for l in lines:
        if l.startswith('# Num'):
            hdr = [h.strip() for h in l.lstrip('#').split('|')]
    if hdr is None:
        if not txt.startswith('# Flag: 0'):
            raise RuntimeError('unexpected SkyBoT reply: ' + txt[:300])
        return pd.DataFrame()
    rows = [[c.strip() for c in l.split('|')] for l in lines if not l.startswith('#')]
    df = pd.DataFrame(rows, columns=hdr)
    df['ra'] = [15 * (float(h) + float(m) / 60 + float(s) / 3600)
                for h, m, s in (x.split() for x in df['RA(h)'])]
    def dec(x):
        d, m, s = x.split()
        sg = -1 if d.startswith('-') else 1
        return sg * (abs(float(d)) + float(m) / 60 + float(s) / 3600)
    df['dec'] = [dec(x) for x in df['DE(deg)']]
    for c in ['Mv', 'Err(arcsec)', 'dRA(arcsec/h)', 'dDEC(arcsec/h)', 'Dg(ua)', 'Dh(ua)']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df


SBIDENT = 'https://ssd-api.jpl.nasa.gov/sb_ident.api'


def sb_ident(params):
    fn = os.path.join(CACHE, 'sbident_' + _key(sorted(params.items())) + '.json')
    if os.path.exists(fn):
        return open(fn).read()
    txt = _get(SBIDENT, params=params, timeout=600, tries=2)
    with open(fn, 'w') as f:
        f.write(txt)
    return txt

"""Image cutouts for top candidates from the NOIRLab Astro Data Archive.

For each candidate: 4 detections spread over the night. The exact instcal file NSC
measured is located with adv_search (archive_filename), the CCD's HDU index from
the archive header service, and that single HDU is downloaded (cached). Panels are
centred on each detection (the mover stays centred, stars move between panels);
a last panel shows the FIRST detection's sky position at the LAST epoch, which
must be empty if the source moved.
usage: python cutouts.py REGION CAND_ID [CAND_ID ...]
"""
import os, sys, json, io
import numpy as np, pandas as pd, requests
from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
PLOTS = os.path.join(HERE, '..', 'plots')
HDUC = os.path.join(HERE, '..', 'cache', 'hdu')
os.makedirs(HDUC, exist_ok=True)
API = 'https://astroarchive.noirlab.edu/api'


def find_md5(expname):
    """Map an NSC exposure name to the archive md5 of the same instcal file.
    Searches by calendar date (fast, indexed) and matches the file basename."""
    fn = os.path.join(HDUC, expname + '.md5')
    if os.path.exists(fn):
        return open(fn).read().strip()
    yymmdd = expname.split('_')[1]
    from datetime import date, timedelta
    d0 = date(2000 + int(yymmdd[:2]), int(yymmdd[2:4]), int(yymmdd[4:6]))
    body = {"outfields": ["md5sum", "archive_filename", "proc_type", "prod_type"],
            "search": [["caldat", str(d0 - timedelta(days=1)), str(d0)],
                       ["instrument", "decam"], ["proc_type", "instcal"],
                       ["prod_type", "image"]]}
    r = requests.post(f'{API}/adv_search/find/?limit=20000', json=body, timeout=120)
    rows = [x for x in r.json()[1:] if os.path.basename(x['archive_filename']).startswith(expname)]
    md5 = rows[0]['md5sum']
    open(fn, 'w').write(md5)
    return md5


def hdu_index(md5, ccdnum):
    fn = os.path.join(HDUC, md5 + '.hdr.json')
    if not os.path.exists(fn):
        r = requests.get(f'{API}/header/{md5}/?format=json', timeout=120)
        open(fn, 'w').write(r.text)
    h = json.load(open(fn))
    for i, x in enumerate(h):
        if x.get('CCDNUM') == ccdnum:
            return i
    raise KeyError(ccdnum)


def get_hdu(expname, ccdnum):
    fn = os.path.join(HDUC, f'{expname}_{ccdnum}.fits')
    if not os.path.exists(fn):
        md5 = find_md5(expname)
        k = hdu_index(md5, ccdnum)
        r = requests.get(f'{API}/retrieve/{md5}/?hdus=0,{k}', timeout=300)
        r.raise_for_status()
        open(fn, 'wb').write(r.content)
    hl = fits.open(fn)
    for h in hl:
        if h.data is not None and h.data.ndim == 2:
            return h.data.astype(float), h.header
    raise ValueError('no image HDU')


def panel(ax, data, hdr, ra, dec, size=24, title='', mark=True):
    w = WCS(hdr)
    c = SkyCoord(ra * u.deg, dec * u.deg)
    cut = Cutout2D(data, c, size * u.arcsec, wcs=w, mode='partial', fill_value=np.nan)
    im = cut.data
    med = np.nanmedian(im)
    mad = np.nanmedian(np.abs(im - med)) * 1.4826
    ax.imshow(im, origin='lower', cmap='gray_r', vmin=med - 2 * mad, vmax=med + 8 * mad,
              interpolation='nearest')
    if mark:
        x, y = cut.wcs.world_to_pixel(c)
        ax.add_patch(plt.Circle((x, y), 2.0 / 0.263, fill=False, color='#eb6834', lw=1.2))
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=8)


def main(reg, cids):
    det = pd.read_csv(os.path.join(DATA, f'{reg}_candidate_detections.csv'))
    for cid in cids:
        d = det[det.cand_id == cid].sort_values('tmid')
        first_night = d.tracklet.iloc[0]
        dn = d[d.tracklet == first_night]
        idx = np.linspace(0, len(dn) - 1, 4).astype(int)
        rows = dn.iloc[idx]
        fig, axs = plt.subplots(1, 5, figsize=(11, 2.6))
        for ax, r in zip(axs[:4], rows.itertuples()):
            try:
                data, hdr = get_hdu(r.exposure, int(r.ccdnum))
                panel(ax, data, hdr, r.ra, r.dec,
                      title=f'MJD {r.tmid:.4f}\n{r.filter} {r.mag_auto:.2f}')
            except Exception as e:
                ax.set_title(f'failed: {e}'[:40], fontsize=7)
                print('cutout failed', cid, r.exposure, e, flush=True)
        r0, rl = rows.iloc[0], rows.iloc[-1]
        try:
            data, hdr = get_hdu(rl.exposure, int(rl.ccdnum))
            panel(axs[4], data, hdr, r0.ra, r0.dec,
                  title=f'first position\nat MJD {rl.tmid:.4f}')
        except Exception as e:
            axs[4].set_title('ref failed', fontsize=7)
            print('ref failed', e)
        fig.suptitle(f'{cid} ({first_night}): 24" cutouts centred on each detection; '
                     'last panel = first position at last epoch', fontsize=9)
        fig.tight_layout()
        fig.savefig(os.path.join(PLOTS, f'cutout_{cid}.png'), dpi=110)
        plt.close(fig)
        print('saved', cid, flush=True)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])

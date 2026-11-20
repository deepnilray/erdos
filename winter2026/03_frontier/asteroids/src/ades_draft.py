"""Write an ADES (version 2022) PSV *draft* for one candidate. NOT FOR SUBMISSION.

Purpose: show exactly what a report would contain. Observers/measurers/submitter
fields are placeholders; archival DECam data must go through the MPC's SARC DECam
contact first (see PRIORART.md), and positions should be re-measured from the images
rather than copied from the NSC catalogue before any real report.
obsTime = NSC exposure start + exptime/2 (UTC). Astrometry is NSC DR2 (calibrated
to Gaia DR2 -> astCat Gaia2). rmsRA is the NSC raerr (arcsec, already on the sky).
usage: python ades_draft.py REGION CAND_ID [max_rows_per_night]
"""
import os, sys
import numpy as np, pandas as pd
from astropy.time import Time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def main(reg, cid, per_night=4):
    d = pd.read_csv(os.path.join(DATA, f'{reg}_candidate_detections.csv'))
    d = d[d.cand_id == cid].sort_values('tmid')
    rows = []
    for tr, g in d.groupby('tracklet'):
        g = g.iloc[np.linspace(0, len(g) - 1, min(per_night, len(g))).astype(int)]
        rows.append(g)
    d = pd.concat(rows).sort_values('tmid')
    trk = cid.replace('-', '')[-7:]
    hdr = [
        '# version=2022',
        '# DRAFT ONLY - NOT SUBMITTED - placeholders must be replaced; see README',
        '# observatory',
        '! mpcCode W84',
        '# submitter',
        '! name PLACEHOLDER (submitter)',
        '# observers',
        '! name PLACEHOLDER (original observers of NOAO program 2014A-0496)',
        '# measurers',
        '! name PLACEHOLDER (measurer)',
        '# telescope',
        '! aperture 4.0',
        '! design Reflector',
        '! detector CCD',
        '# comment',
        '! line Positions from NOIRLab Source Catalog DR2 (archival DECam), not re-measured',
    ]
    cols = ['permID', 'provID', 'trkSub', 'mode', 'stn', 'obsTime', 'ra', 'dec',
            'rmsRA', 'rmsDec', 'astCat', 'mag', 'rmsMag', 'band', 'photCat']
    lines = ['|'.join(cols)]
    for r in d.itertuples():
        t = Time(r.tmid, format='mjd', scale='utc').isot[:22] + 'Z'
        lines.append('|'.join(['', '', trk, 'CCD', 'W84', t, f'{r.ra:.6f}', f'{r.dec:+.6f}',
                               f'{r.raerr:.3f}', f'{r.decerr:.3f}', 'Gaia2', f'{r.mag_auto:.2f}',
                               f'{r.magerr_auto:.2f}', r.filter, 'Gaia2']))
    fn = os.path.join(DATA, f'ADES_DRAFT_NOT_SUBMITTED_{cid}.psv')
    open(fn, 'w').write('\n'.join(hdr + lines) + '\n')
    print(fn)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 4)

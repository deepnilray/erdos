import lightkurve as lk, numpy as np, matplotlib, warnings; matplotlib.use('Agg'); import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import sys
n, c = sys.argv[1], sys.argv[2]
r = lk.search_lightcurve(c, radius=10, author=['QLP', 'SPOC', 'TESS-SPOC'])
seen = {}; lcs = []
for row in r:
    s = row.mission[0]
    if s in seen: continue
    try:
        lc = row.download(quality_bitmask='hard')
        col = 'sap_flux' if 'QLP' in row.author[0] else 'pdcsap_flux'
        if col not in lc.colnames: col = 'flux'
        lc = lc.select_flux(col).remove_nans().normalize()
        seen[s] = row.author[0]; lcs.append((s, row.author[0], lc))
        f = lc.flux.value; print(n, s, row.author[0], len(f), 'rms %.4f' % np.nanstd(f), 'min %.4f' % np.nanmin(f), '1st pct %.4f' % np.nanpercentile(f, 1), flush=True)
    except Exception as e: print(n, s, 'ERR', repr(e)[:120], flush=True)
fig, ax = plt.subplots(len(lcs), 1, figsize=(10, 1.8 * len(lcs)), squeeze=False)
for i, (s, a, lc) in enumerate(lcs):
    ax[i, 0].plot(lc.time.value, lc.flux.value, 'k.', ms=1); ax[i, 0].set_ylabel(f'{s[-9:]}\n{a}', fontsize=7)
    lo, hi = np.nanpercentile(lc.flux.value, [0.2, 99.8]); ax[i, 0].set_ylim(lo - 0.01, hi + 0.01)
ax[0, 0].set_title(n + ' TESS normalised flux'); plt.tight_layout(); plt.savefig(f'{n}_tess.png', dpi=90)

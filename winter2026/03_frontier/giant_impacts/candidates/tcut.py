import lightkurve as lk, numpy as np, warnings, sys, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
n, c = sys.argv[1], sys.argv[2]; sectors = [int(s) for s in sys.argv[3].split(',')]
out = []
for s in sectors:
    try:
        tpf = lk.search_tesscut(c, sector=s).download(cutout_size=11, quality_bitmask='hard')
        im = np.nanmedian(tpf.flux.value, axis=0); cy, cx = np.array(im.shape) // 2
        ap = np.zeros(im.shape, bool); ap[cy - 1:cy + 2, cx - 1:cx + 2] = True
        bk = im < np.nanpercentile(im, 40); bk[cy - 3:cy + 4, cx - 3:cx + 4] = False
        f = tpf.flux.value; bkg = np.nanmedian(f[:, bk], axis=1)
        flux = np.nansum(f[:, ap], axis=1) - ap.sum() * bkg
        t = tpf.time.value; ok = np.isfinite(flux) & (flux > 0)
        t, flux, bkg = t[ok], flux[ok], bkg[ok]; flux = flux / np.nanmedian(flux)
        # 6-hour bins
        edges = np.arange(t.min(), t.max() + 0.25, 0.25); idx = np.digitize(t, edges)
        tb = np.array([t[idx == i].mean() for i in np.unique(idx)]); fb = np.array([np.median(flux[idx == i]) for i in np.unique(idx)])
        bb = np.array([np.median(bkg[idx == i]) for i in np.unique(idx)])
        out.append((s, t, flux, tb, fb, bb))
        print(n, 'sector', s, 'N', len(t), 'binned min %.3f, 1st pct %.3f, rms(binned) %.4f' % (fb.min(), np.percentile(fb, 1), np.std(fb)), flush=True)
    except Exception as e: print(n, 'sector', s, 'ERR', repr(e)[:150], flush=True)
fig, ax = plt.subplots(len(out), 1, figsize=(10, 2.0 * len(out)), squeeze=False)
for i, (s, t, flux, tb, fb, bb) in enumerate(out):
    a = ax[i, 0]; a.plot(t, flux, '.', c='0.8', ms=1); a.plot(tb, fb, 'k.-', ms=3, lw=0.5); a.set_ylabel(f'S{s}', fontsize=8)
    a2 = a.twinx(); a2.plot(tb, bb, 'r-', lw=0.6, alpha=0.6); a2.set_yticks([])
    a.set_ylim(np.percentile(fb, 0.5) - 0.03, np.percentile(fb, 99.5) + 0.03)
ax[0, 0].set_title(f'{n}: TESScut 3x3 aperture, background-subtracted (black: 6-h bins; red: background)'); plt.tight_layout(); plt.savefig(f'{n}_tesscut.png', dpi=90)

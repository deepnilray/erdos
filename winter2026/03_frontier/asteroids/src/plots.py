"""Figures for the README. usage: python plots.py REGION"""
import os, sys
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
PLOTS = os.path.join(HERE, '..', 'plots')
os.makedirs(PLOTS, exist_ok=True)
BLUE, ORANGE, AQUA, GREY, INK, INK2 = '#2a78d6', '#eb6834', '#1baf7a', '#b5b3ad', '#0b0b0b', '#52514e'
plt.rcParams.update({'font.size': 10, 'axes.edgecolor': INK2, 'axes.labelcolor': INK,
                     'xtick.color': INK2, 'ytick.color': INK2, 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.grid': True, 'grid.color': '#e6e5e0',
                     'grid.linewidth': 0.6, 'figure.facecolor': '#fcfcfb',
                     'axes.facecolor': '#fcfcfb', 'savefig.facecolor': '#fcfcfb'})


def main(reg):
    tr = pd.read_csv(os.path.join(DATA, f'{reg}_tracklets_classified.csv'))
    dd = pd.read_csv(os.path.join(DATA, f'{reg}_dets_classified.csv'))
    g = pd.read_csv(os.path.join(DATA, f'{reg}_control.csv'))
    known = tr.known.notna()

    # 1. sky map of detections in tracklets
    fig, ax = plt.subplots(figsize=(6.5, 6))
    kn = dd.tracklet.isin(tr.tracklet[known])
    good = dd.tracklet.isin(tr.tracklet[~known & (tr.n >= 5)])
    ax.scatter(dd.ra[kn], dd.dec[kn], s=1, c=BLUE, lw=0, label='matched to a known object')
    ax.scatter(dd.ra[good], dd.dec[good], s=4, c=ORANGE, lw=0,
               label='unmatched, >= 5 detections')
    ax.invert_xaxis()
    ax.set_xlabel('RA (deg)'); ax.set_ylabel('Dec (deg)')
    ax.set_title(f'{reg}: detections in single-night tracklets', loc='left')
    ax.legend(loc='lower left', markerscale=5, frameon=False)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTS, f'{reg}_skymap.png'), dpi=130)
    plt.close(fig)

    # 2. recovery fraction vs V
    bins = np.arange(16, 25.5, 0.5)
    c = pd.cut(g.mv, bins)
    s = g.groupby(c, observed=False).recovered.agg(['size', 'sum'])
    mid = bins[:-1] + 0.25
    frac = np.where(s['size'] > 0, s['sum'] / s['size'].clip(lower=1), np.nan)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.5, 5.5), sharex=True,
                                 gridspec_kw=dict(height_ratios=[2, 1]))
    a1.plot(mid, frac, '-o', color=BLUE, lw=2, ms=5)
    a1.set_ylabel('fraction recovered'); a1.set_ylim(0, 1.05)
    a1.set_title(f'{reg}: recovery of SkyBoT-predicted known objects (per night)', loc='left')
    dep = g.depth.median()
    a1.axvline(dep, color=INK2, lw=1, ls='--')
    a1.text(dep - 0.1, 0.08, f'median depth95 {dep:.1f}', ha='right', color=INK2, fontsize=9)
    a2.bar(mid, s['size'], width=0.42, color=GREY, label='expected on chips')
    a2.bar(mid, s['sum'], width=0.42, color=BLUE, label='recovered')
    a2.set_xlabel('predicted V (SkyBoT)'); a2.set_ylabel('objects')
    a2.legend(frameon=False, fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTS, f'{reg}_recovery.png'), dpi=130)
    plt.close(fig)

    # 3. rate vs magnitude
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.scatter(tr.mag[known], tr.rate[known], s=6, c=BLUE, lw=0, label='known')
    u = ~known & (tr.n >= 5)
    ax.scatter(tr.mag[u], tr.rate[u], s=14, c=ORANGE, lw=0, label='unmatched, n >= 5')
    ax.set_yscale('log'); ax.set_xlabel('median magaut (main filter)')
    ax.set_ylabel('rate (deg/day)')
    ax.set_title(f'{reg}: tracklet rate vs magnitude', loc='left')
    ax.legend(frameon=False)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTS, f'{reg}_rate_mag.png'), dpi=130)
    plt.close(fig)

    # 4. false tracklets vs n
    rot = [pd.read_csv(os.path.join(DATA, f'{reg}_rotate{s}_tracklets.csv'))
           for s in (1, 2, 3) if os.path.exists(os.path.join(DATA, f'{reg}_rotate{s}_tracklets.csv'))]
    if rot:
        nb = [3, 4, 5, 6, 8, 12, 20, 40, 400]
        lab = ['3', '4', '5', '6-7', '8-11', '12-19', '20-39', '40+']
        raw = pd.read_csv(os.path.join(DATA, f'{reg}_tracklets.csv'))
        real = pd.cut(raw.n, nb, right=False).value_counts().sort_index().values
        tcl = [pd.read_csv(os.path.join(DATA, f'{reg}_tclean{s}_tracklets.csv'))
               for s in (1, 2, 3) if os.path.exists(os.path.join(DATA, f'{reg}_tclean{s}_tracklets.csv'))]
        fake = np.mean([pd.cut(r.n, nb, right=False).value_counts().sort_index().values
                        for r in rot], axis=0)
        x = np.arange(len(lab))
        fig, ax = plt.subplots(figsize=(6.5, 4))
        ax.bar(x - 0.27, real, 0.26, color=BLUE, label='real data (before fragment merging)')
        ax.bar(x, fake, 0.26, color=ORANGE, label='each exposure rotated (mean of 3)')
        if tcl:
            tc = np.mean([pd.cut(r.n, nb, right=False).value_counts().sort_index().values
                          for r in tcl], axis=0)
            ax.bar(x + 0.27, tc, 0.26, color=AQUA,
                   label='movers removed, times shuffled (mean of 3)')
        ax.set_xticks(x); ax.set_xticklabels(lab); ax.set_yscale('symlog', linthresh=1)
        ax.set_xlabel('detections per tracklet'); ax.set_ylabel('tracklets')
        ax.set_title(f'{reg}: real vs scrambled tracklets', loc='left')
        ax.legend(frameon=False, fontsize=8)
        fig.tight_layout(); fig.savefig(os.path.join(PLOTS, f'{reg}_false_rate.png'), dpi=130)
        plt.close(fig)


if __name__ == '__main__':
    main(sys.argv[1])

"""Injection-recovery and false-positive test for flash.py on Gaia-like cadence and noise.
Cadence: visits every ~20-60 d over 66 months (DR4 span 2014.6-2020.0), each visit 2-4 transits
106 min apart (the two fields of view).  Noise: per-transit G errors for G = 13/15/17, plus a 0.5 mmag floor.
Nuisance: half the stars carry rotation (P 1-40 d, semi-amp 0.5-5 mmag), so the null is not white."""
import numpy as np, json, sys
from flash import score_lc
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
NOISE = {13: 0.0015, 15: 0.0030, 17: 0.0080}
def cadence():
    t, x = [], 56870.0 + rng.uniform(0, 30)
    while x < 58850:
        for j in range(rng.choice([2, 2, 2, 4])): t.append(x + j*0.0736)
        x += rng.uniform(20, 60)
    return np.array(t)
def star(G, flash=None):
    t = cadence(); s = np.hypot(NOISE[G], 0.0005)
    f = np.ones_like(t)
    if rng.random() < 0.5:
        P = rng.uniform(1, 40); f += rng.uniform(0.0005, 0.005)*np.sin(2*np.pi*t/P + rng.uniform(0, 6.3))
    if flash:
        A, tau = flash; t0 = rng.uniform(t.min()+300, t.max()-200)
        f += np.where(t >= t0, A*np.exp(-(t-t0)/tau), 0)
    mag = -2.5*np.log10(f) + 14 + rng.normal(0, s, len(t))
    return t, mag, np.full(len(t), s)
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 600
null = {G: sorted(score_lc(*star(G))['score'] for _ in range(N0)) for G in NOISE}
thr = {G: max(30.0, 1.2*null[G][-1]) for G in NOISE}          # above every null trial, floor 30
res = {}
for G in NOISE:
    for A in (0.005, 0.01, 0.02, 0.05, 0.1):
        for tau in (3, 30, 300, 2000):
            hit = sum(score_lc(*star(G, (A, tau)))['score'] > thr[G] for _ in range(40))
            res[f"G{G}_A{A}_tau{tau}"] = hit/40
json.dump(dict(n_null=N0, null_max={G: null[G][-1] for G in NOISE}, threshold=thr, recovery=res),
          open('inject_summary.json', 'w'), indent=1)
for G in NOISE:
    print(f"G={G} null max {null[G][-1]:.1f} thr {thr[G]:.1f}")
    for tau in (3, 30, 300, 2000):
        print("  tau", tau, [res[f'G{G}_A{A}_tau{tau}'] for A in (0.005, 0.01, 0.02, 0.05, 0.1)])

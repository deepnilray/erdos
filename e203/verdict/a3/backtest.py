import numpy as np, math, itertools
series = {
 "L4''(coupled)": {20000: 0.633429, 200000: 0.715690, 400000: 0.730584},
 "L4'":           {2000: 0.570147, 20000: 0.734931, 100000: 0.808684, 200000: 0.867666, 400000: 0.885439},
 "old a*=.5955":  {2000: 0.570, 20000: 0.769, 50000: 0.817, 100000: 0.846, 200000: 0.868},
}
import sys
if len(sys.argv) > 1: series["L4''(coupled)"][800000] = float(sys.argv[1])
shapes = {
 'loglog (diverges)': lambda E: math.log(math.log(E)),
 '-1/logE (conv)':    lambda E: -1 / math.log(E),
 '-1/log^2E (conv)':  lambda E: -1 / math.log(E) ** 2,
 '-E^-0.25 (conv)':   lambda E: -E ** -0.25,
 '-E^-0.5 (conv)':    lambda E: -E ** -0.5,
}
for name, s in series.items():
    Es = sorted(s); print(f"== {name}: {[(E, s[E]) for E in Es]}")
    for sh, g in shapes.items():
        res = []
        for i in range(len(Es) - 2):
            for j in range(i + 1, len(Es) - 1):
                if Es[i] < 20000 and name != "L4'": continue
                E1, E2 = Es[i], Es[j]
                b = (s[E2] - s[E1]) / (g(E2) - g(E1)); a = s[E1] - b * g(E1)
                for k in range(j + 1, len(Es)):
                    pred = a + b * g(Es[k]); res.append((E1, E2, Es[k], pred, s[Es[k]], pred - s[Es[k]]))
                lim = a if 'conv' in sh else float('inf')
        errs = [r[5] for r in res]
        last = res[-1] if res else None
        print(f"   {sh:20s} back-test errors (fit on 2 pts, predict later): " + ", ".join(f"{r[0]:g},{r[1]:g}->{r[2]:g}: {r[5]:+.4f}" for r in res))

"""Soundness controls for distort2 (exact stage 2 + forced overlaps) on GENUINE coverings that
use stage 2, plus a planted bug (treat every overlap with stage 2 as forced) that must fire."""
import itertools, math, numpy as np
import distort2 as D2, distort_opt as O, distort_fast as D
from control_distort import covers, find_offsets, P
fams = {
 '1D {0(2),0(3),1(4),5(6),7(12)} along k': [P(i, d, 1, 0) for i, d in enumerate([2, 3, 4, 6, 12])],
 '1D same along (1,3)':                    [P(i, d, 1, 3) for i, d in enumerate([2, 3, 4, 6, 12])],
 '2D: k even  +  (k odd, l = c mod 3)':    [P(0, 2, 1, 0)] + [P(i, 6, 3, 4) for i in (1, 2, 3)],
 '2D: k+l even + (k+l odd, k = c mod 3)':  [P(0, 2, 1, 1)] + [P(i, 6, 3 + 4, 3) for i in (1, 2, 3)],
 '2D: e=4 line + e=4 + lines mod 3':       [P(0, 4, 1, 0), P(1, 4, 1, 0)] + [P(i, 12, 3 * 1 + 4 * 0, 4 * 1) for i in (2, 3, 4, 5, 6, 7)],
}
def bound(fam, bug=False):
    if bug:
        orig = D2.img
        D2.img = lambda p, H: p['e']            # planted bug: pretend every stage-2 overlap is forced
    try:
        B = D2.build(fam)
    finally:
        if bug: D2.img = orig
    if B is None: return float('inf')
    if B['nst'] == 0: return 0.0
    dv, c = O.optimise(B, sweeps=3); return D.costs(B, dv)[0].sum()
ok = True; fired = False
for name, fam in fams.items():
    offs = find_offsets(fam); assert offs is not None, name
    U = bound(fam); W = bound(fam, bug=True)
    ok &= U >= 1 - 1e-9; fired |= W < 1 - 1e-9
    print(f"{name:42s} covering {offs}: bound {U:.4f} {'OK' if U >= 1-1e-9 else 'UNSOUND!'}; planted-bug {W:.4f} {'FIRES' if W < 1-1e-9 else '-'}")
print('SOUNDNESS', 'PASS' if ok else 'FAIL', '| planted bug detected:', fired)

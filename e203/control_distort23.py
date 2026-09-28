"""Soundness controls for the merged {2,3} first stage, on GENUINE coverings whose {2,3}-part does not
cover and a stage >= 5 must finish.  alpha* = exact max coverage of the first-stage members (brute
force over offsets).  Planted bug: using alpha* = true alpha minus 0.2 (understating the removed
mass) must be caught."""
import itertools, math, numpy as np
import distort23 as D23, distort_opt as O, distort_fast as D
from control_distort import covers, P
from sympy import factorint

def maxcov(fam):
    if not fam: return 0.0
    N = math.lcm(*[f['e'] for f in fam]); best = 0
    k, l = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
    vals = [(f['alpha'] * k + f['beta'] * l) % f['e'] for f in fam]
    for offs in itertools.product([0], *[range(f['e']) for f in fam[1:]]):
        cov = vals[0] == offs[0]
        for v, c in zip(vals[1:], offs[1:]): cov |= v == c
        best = max(best, cov.mean())
    return best

# (family, explicit offsets); psi = 5k+6l mod 10 encodes (k mod 2, l mod 5); offsets c with c odd.
fams = {
 'k even + (k odd, l = c mod 5)':         ([P(0, 2, 1, 0)] + [P(i, 10, 5, 6) for i in range(1, 6)], [0, 1, 7, 3, 9, 5]),
 '1D {0(2),0(3),1(4),5(6)} + 7(12)&c(5)': ([P(i, d, 1, 0) for i, d in enumerate([2, 3, 4, 6])] + [P(10 + c, 60, 1, 0) for c in range(5)],
                                           [0, 0, 1, 5] + [x for x in range(60) if x % 12 == 7]),
 '2D: k even, l even, + (k,l odd; mod 5)': ([P(0, 2, 1, 0), P(1, 2, 0, 1)] + [P(10 + c, 10, 5, 5 + 6) for c in range(5)],
                                           [0, 0] + [x for x in range(10) if (5 + 5 + 6) % 2 == x % 2]),
 'k+l even + (k+l odd, (k-l) mod 5)':     ([P(0, 2, 1, 1)] + [P(10 + c, 10, 5 + 6, 5 - 6) for c in range(5)], [0, 1, 3, 5, 7, 9]),
}
def bound(fam, bug=False):
    first = [f for f in fam if max(factorint(f['e'])) <= 3]
    a = maxcov(first) - (0.2 if bug else 0.0)
    if a >= 1: return float('inf')
    B = D23.build(fam, [f['p'] for f in first], a)
    if B['nst'] == 0: return 0.0
    dv, c = O.optimise(B, sweeps=3); return D.costs(B, dv)[0].sum()
ok = True; fired = False
for name, (fam, offs) in fams.items():
    assert covers(fam, offs), name + ' is NOT a covering'
    U = bound(fam); W = bound(fam, bug=True)
    ok &= U >= 1 - 1e-9; fired |= W < 1 - 1e-9
    print(f"{name:40s} covering {offs}: bound {U:.4f} {'OK' if U >= 1-1e-9 else 'UNSOUND!'}; planted-bug {W:.4f} {'FIRES' if W < 1-1e-9 else '-'}")
print('SOUNDNESS', 'PASS' if ok else 'FAIL', '| planted bug detected:', fired)

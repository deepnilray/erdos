"""Controls for the distortion bound.
Soundness: on GENUINE coverings of Z^2 (synthetic psi data, verified to cover by brute force),
the optimised bound must be >= 1.  Planted failure: dropping the diagonal term of m2 (a plausible
bug) must drive the bound below 1 on some genuine covering -- i.e. the control can fire."""
import itertools, math, numpy as np
import distort_fast as D

def P(tag, e, a, b): return dict(p=tag, e=e, alpha=a % e, beta=b % e)

def covers(fam, offs):
    N = math.lcm(*[f['e'] for f in fam])
    return all(any((f['alpha'] * k + f['beta'] * l - c) % f['e'] == 0 for f, c in zip(fam, offs))
               for k in range(N) for l in range(N))

def find_offsets(fam):
    for offs in itertools.product(*[range(f['e']) for f in fam]):
        if covers(fam, offs): return offs
    return None

# genuine coverings (verified below):
fams = {
 'three mod-2 lines':  [P(1, 2, 1, 0), P(2, 2, 0, 1), P(3, 2, 1, 1)],
 'two parallel mod-2': [P(1, 2, 1, 0), P(2, 2, 1, 0)],
 '1D covering {2,3,4,6,12} along k': [P(i, d, 1, 0) for i, d in enumerate([2, 3, 4, 6, 12])],
 '1D covering along k+2l': [P(i, d, 1, 2) for i, d in enumerate([2, 3, 4, 6, 12])],
 'mod-3 parallel class': [P(i, 3, 1, 1) for i in range(3)],
 '4 lines of F_3^2 through 0 + extra': [P(1, 3, 1, 0), P(2, 3, 0, 1), P(3, 3, 1, 1), P(4, 3, 1, 2), P(5, 3, 1, 0), P(6, 3, 0, 1)],
}
def bound(fam, drop_diag=False):
    B = D.build(fam)
    if drop_diag:                       # planted bug: remove all diagonal terms of m2
        S2, s2, w2 = B['T2']; n1 = len(B['T1'][1])
        w2 = w2.copy(); w2[:n1] = 0.0; B['T2'] = (S2, s2, w2)   # first n1 rows of T2 are diagonal
    dvec, U = D.optimise(B, sweeps=3, verbose=False)
    return U
ok = True; fired = False
for name, fam in fams.items():
    offs = find_offsets(fam)
    assert offs is not None, name + ' is not a covering'
    U = bound(fam); W = bound(fam, drop_diag=True)
    ok &= U >= 1 - 1e-9; fired |= W < 1 - 1e-9
    print(f"{name:38s} genuine covering (offsets {offs}); bound {U:.4f} {'OK >=1' if U >= 1-1e-9 else 'UNSOUND!'}"
          f";  planted-bug bound {W:.4f} {'FIRES' if W < 1-1e-9 else '-'}")
print('SOUNDNESS', 'PASS' if ok else 'FAIL', '| planted bug detected:', fired)

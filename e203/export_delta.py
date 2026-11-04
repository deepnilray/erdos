"""Export a delta vector (npy, indexed by distort23.build's ells) to an ell -> delta JSON."""
import sys, json, numpy as np, distort23 as D23
from sympy import factorint
pool = [p for p in (json.loads(l) for l in open(sys.argv[1])) if p['e'] <= int(float(sys.argv[2]))]
heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]
ells = sorted({q for p in pool for q in factorint(p['e'])} - {2, 3})
dv = np.load(sys.argv[3]); assert len(dv) == len(ells)
json.dump({str(l): float(dv[i]) for i, l in enumerate(ells)}, open(sys.argv[4], 'w')); print('wrote', sys.argv[4])

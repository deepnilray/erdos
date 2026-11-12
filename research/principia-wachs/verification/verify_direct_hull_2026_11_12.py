"""Independent numerical convex hull of ORIGINAL Wachs one-line vectors.
No product geometry used to generate points. SciPy/Qhull is floating point;
this is a diagnostic, not a proof.
"""
from itertools import permutations
import numpy as np
from scipy.spatial import ConvexHull

def direct_wachs(m):
    # Enumerate original permutations and filter the definition, rather than
    # using the claimed block parametrization.
    for w in permutations(range(1,2*m+1)):
        pos = {v:i for i,v in enumerate(w)}
        if all(abs(pos[2*j-1]-pos[2*j])==1 for j in range(1,m+1)):
            yield w

for m in (2,3):
    W=np.array(list(direct_wachs(m)), dtype=float)
    # Eliminate the final original coordinate using sum x_i = m(2m+1).
    # This is a bijective affine projection on the ambient sum hyperplane.
    X=W[:,:-1]
    hull=ConvexHull(X)
    # Each hull simplex is a triangulation of a facet. Merge normalized
    # hyperplanes, retaining tolerance to accommodate floating-point noise.
    planes=set()
    for eq in hull.equations:
        v=eq / np.linalg.norm(eq[:-1])
        planes.add(tuple(np.round(v,8)))
    expected=2*m+(2**m-2)
    assert len(W)==2**m*np.math.factorial(m) if hasattr(np,'math') else len(W)==2**m*__import__('math').factorial(m)
    assert len(planes)==expected, (m,len(planes),expected)
    assert len(hull.vertices)==len(W)
    print(f'm={m}: {len(W)} directly enumerated vertices, affine dimension {X.shape[1]}, {len(planes)} hull facets; PASS')

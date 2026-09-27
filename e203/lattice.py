"""Exact lattice arithmetic for the 2D covering problem.

psi_p(k,l) = alpha*k + beta*l (mod e);  L_p = ker psi_p;  killed set of p = one coset of L_p.
A lattice is stored by an integer basis matrix B (columns b1, b2); index = |det B|.
"""
import math, json

def egcd(a, b):
    if b == 0: return (abs(a), 1 if a >= 0 else -1, 0)
    g, x, y = egcd(b, a % b); return g, y, x - (a // b) * y

def kernel_basis(a, b, e):
    """Basis of {z in Z^2 : a z1 + b z2 == 0 mod e}."""
    a %= e; b %= e
    if a == 0 and b == 0: return [[1, 0], [0, 1]]
    g = math.gcd(a, b); h = math.gcd(g, e)
    _, x0, y0 = egcd(a // g, b // g)            # (a/g) x0 + (b/g) y0 = 1
    v1 = (b // g, -(a // g)); v2 = ((e // h) * x0, (e // h) * y0)
    return [[v1[0], v2[0]], [v1[1], v2[1]]]     # columns

def matmul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def det(B): return B[0][0]*B[1][1] - B[0][1]*B[1][0]

def hnf(B):
    """Column-style lower-triangular HNF of a full-rank 2x2 integer basis: [[a,0],[c,d]], 0<=c<d."""
    (p, q), (r, s) = B            # columns (p,r), (q,s)
    g, x, y = egcd(p, q)          # combine columns so that first row becomes (g, 0)
    c1 = (g, x*r + y*s)           # x*col1 + y*col2
    c2 = (0, (-q//g)*r + (p//g)*s)
    d = abs(c2[1]); c = c1[1] % d if d else c1[1]
    return [[g, 0], [c, d]]

def restrict(p, B):
    """psi_p composed with basis B: linear form on coordinates z."""
    a = (p['alpha']*B[0][0] + p['beta']*B[1][0]) % p['e']
    b = (p['alpha']*B[0][1] + p['beta']*B[1][1]) % p['e']
    return a, b

def image_size(p, B):
    """|psi_p(L)| where L has basis B  (= [L : L cap L_p])."""
    a, b = restrict(p, B); return p['e'] // math.gcd(math.gcd(a, b), p['e'])

def intersect(p, B):
    a, b = restrict(p, B); return hnf(matmul(B, kernel_basis(a, b, p['e'])))

def load(path): return [json.loads(l) for l in open(path)]

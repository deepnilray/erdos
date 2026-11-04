"""Exact forced-overlap factor for the merged {2,3} stage.
For a coset A with lattice L_A, the heavy {2,3} sets read only x mod 144, and uniform measure on A pushes
forward to uniform measure on the image of L_A in (Z/144)^2.  minU(A) = min over heavy offsets of the
covered fraction of that image (exact branch and bound, minunion.c), so
    P_23(A) <= u(A) (1 - minU(A)) / (1 - alpha*).
Results are cached by the image subgroup (canonical HNF of L_A + 144 Z^2)."""
import json, subprocess, functools
import lattice as LT
M = 144
HEAVY = None
def set_heavy(H):
    global HEAVY; HEAVY = H; minU_img.cache_clear()
@functools.lru_cache(maxsize=None)
def minU_img(g1, g2):
    inp = f"{M} {g1[0]} {g1[1]} {g2[0]} {g2[1]} {len(HEAVY)} " + " ".join(f"{h['alpha']} {h['beta']} {h['e']}" for h in HEAVY)
    a, n = subprocess.run(['./minunion'], input=inp, capture_output=True, text=True, check=True).stdout.split()
    return int(a) / int(n)
def minU(H):
    g1 = (H[0][0] % M, H[1][0] % M); g2 = (H[0][1] % M, H[1][1] % M)
    return minU_img(g1, g2)

def canon(H):
    """canonical HNF [[a,0],[c,d]] (0<=c<d) of the lattice L + M Z^2, L with basis columns H."""
    import math
    cols = [[H[0][0], H[1][0]], [H[0][1], H[1][1]], [M, 0], [0, M]]
    # combine columns so that exactly one has nonzero first coordinate
    piv = None; rest = []
    for v in cols:
        if piv is None: piv = v; continue
        a, b = piv[0], v[0]
        if b == 0: rest.append(v); continue
        g, x, y = LT.egcd(a, b)
        new_piv = [x * piv[0] + y * v[0], x * piv[1] + y * v[1]]
        other = [(-b // g) * piv[0] + (a // g) * v[0], (-b // g) * piv[1] + (a // g) * v[1]]
        piv = new_piv; rest.append(other)
    d = 0
    for v in rest: d = math.gcd(d, v[1])
    a = abs(piv[0]); c = piv[1] * (1 if piv[0] > 0 else -1)
    return (a, c % d, d)

def gens_from_canon(k):
    a, c, d = k; return (a, c), (0, d)

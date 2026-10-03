"""Residue constraint for m = M^g (D1 generalised).
Killed set of p: {psi_p = c}, h^c = -1/m.  As M ranges over F_p^x, the admissible offsets are
   c == c0 (mod o),   o = e / gcd(e, n/d),  n = p-1, d = gcd(g, n),
   c0 = 0 if n/d even;  c0 = o/2 if n/d odd and o even;  NO admissible c if n/d odd and o odd
(then p is useless unless p | M, which empties A_p).  Derivation: h^c in -F^{x d} iff (-1)^{n/d} h^{c n/d} = 1."""
import math
def admissible(p, e, g):
    n = p - 1; d = math.gcd(g, n); o = e // math.gcd(e, n // d)
    if (n // d) % 2 == 0: return (o, 0)
    if o % 2 == 0: return (o, o // 2)
    return None
if __name__ == '__main__':
    from sympy import primerange, n_order, primitive_root
    bad = 0; tot = 0; useless = 0
    for p in primerange(5, 1500):
        e = math.lcm(n_order(2, p), n_order(3, p)); n = p - 1
        r = primitive_root(p); h = pow(r, n // e, p)
        logh = {pow(h, c, p): c for c in range(e)}
        for g in [2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 24, 60, 420, 840]:
            brute = sorted({logh[(-pow(pow(u, g, p), -1, p)) % p] for u in range(1, p) if (-pow(pow(u, g, p), -1, p)) % p in logh})
            a = admissible(p, e, g)
            pred = [] if a is None else [c for c in range(e) if c % a[0] == a[1]]
            tot += 1; useless += a is None
            if brute != pred: bad += 1; print('MISMATCH', p, e, g, brute[:10], pred[:10])
    print('checked', tot, '(p,g) pairs, useless', useless, 'mismatches', bad)
    # planted failure: ignore the (-1)^{n/d} sign -> must mismatch somewhere
    def broken(p, e, g):
        n = p - 1; d = math.gcd(g, n); return (e // math.gcd(e, n // d), 0)
    mm = 0
    for p in primerange(5, 200):
        e = math.lcm(n_order(2, p), n_order(3, p)); h = pow(primitive_root(p), (p-1)//e, p)
        logh = {pow(h, c, p): c for c in range(e)}
        for g in [2, 4, 8]:
            brute = sorted({logh[x] for u in range(1, p) for x in [(-pow(pow(u, g, p), -1, p)) % p] if x in logh})
            o, c0 = broken(p, e, g); mm += brute != [c for c in range(e) if c % o == c0]
    print('planted control mismatches (must be > 0):', mm)

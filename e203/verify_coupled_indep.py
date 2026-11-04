"""Second, independent exact solver for the 1908 coupled prices R(A) (DISTORTION.md, L4'').
Runs myratio.c (integer-exact branch and bound, __int128 comparisons, heavy forms from heavy_forms.txt)
on every type in coupled_full_E200000.txt and compares R as exact rationals.  Resumable; 4 workers.
  gcc -O2 -o myratio myratio.c && python3 verify_coupled_indep.py"""
import os, subprocess
from fractions import Fraction as F
from concurrent.futures import ThreadPoolExecutor
cert = {l.split()[0]: tuple(map(int, l.split()[2:6])) for l in open('coupled_full_E200000.txt')}
out = 'myratio_all_E200000.txt'
done = {l.split()[0] for l in open(out)} if os.path.exists(out) else set()
def R(a, nA, g, nG): return (1 - F(a, nA)) / (1 - F(g, nG) - F(485, 10000))
def run(k):
    r = subprocess.run(['./myratio', *k.split(',')], capture_output=True, text=True, check=True).stdout.split()
    with open(out, 'a') as fh: fh.write(f"{k} {' '.join(r)}\n")
with ThreadPoolExecutor(4) as ex: list(ex.map(run, [k for k in cert if k not in done]))
mine = {l.split()[0]: tuple(map(int, l.split()[1:5])) for l in open(out)}
eq = sum(R(*mine[k]) == R(*cert[k]) for k in cert); hi = sum(R(*mine[k]) > R(*cert[k]) for k in cert)
print(f"types {len(cert)}; identical rational R: {eq}; independent solver LARGER (repo missed max): {hi}")

"""Coupled exact worst-case ratio R(A) (maxratio.c) for every canonical type, heaviest first, 4 workers.
Appends 'key R' lines to coupled_E{E}.txt as results arrive (resumable)."""
import sys, json, subprocess, os
from concurrent.futures import ThreadPoolExecutor
import rtypes as R
E = sys.argv[1]; types = json.load(open(f'types_E{E}.json'))
pool = {json.loads(l)['p']: json.loads(l) for l in open('poolE200000.jsonl')}
H = [pool[p] for p in [5, 7, 13, 17, 19, 37, 73, 97, 577]]
done = set()
out = f'coupled_full_E{E}.txt'   # lines: key R bestA nA bestG nG (lambda = 485/10000)
if os.path.exists(out): done = {l.split()[0] for l in open(out)}
todo = [k for k in types if k not in done]
tail = f"485 10000 {len(H)} " + " ".join(f"{h['alpha']} {h['beta']} {h['e']}" for h in H)
def run(k):
    a, c, d = map(int, k.split(','))
    r = subprocess.run(['./maxratio'], input=f"144 {a} {c} 0 {d} " + tail, capture_output=True, text=True).stdout.split()
    with open(out, 'a') as fh: fh.write(f"{k} {' '.join(r)}\n")
with ThreadPoolExecutor(4) as ex: list(ex.map(run, todo))
print('all types done')

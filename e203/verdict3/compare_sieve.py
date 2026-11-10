import sys, json
N = int(sys.argv[2]); pool = {}
for l in open('poolE800000.jsonl'):
    r = json.loads(l)
    if r['p'] < N: pool[r['p']] = r['e']
sv = {}
for l in open(sys.argv[1]):
    p, e = map(int, l.split()); sv[p] = e
print('pool primes <N:', len(pool), ' sieve primes <N with e<=8e5:', len(sv))
miss = [p for p in sv if p not in pool]; extra = [p for p in pool if p not in sv]; wrong = [p for p in pool if p in sv and pool[p] != sv[p]]
print('in sieve not pool:', len(miss), miss[:5], ' in pool not sieve:', len(extra), extra[:5], ' wrong e:', len(wrong))
# restricted to the new range
new = {p: e for p, e in sv.items() if e > 400000}; poolnew = {p: e for p, e in pool.items() if e > 400000}
print('range (4e5,8e5]: sieve', len(new), 'pool', len(poolnew), 'equal:', new == poolnew)

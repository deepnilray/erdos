"""Core-refined rigorous coverage bound.

coverage <= OPT(core)  +  sum_{i not in core} w_i * prod_{j in J_i} (1 - w_j)

OPT(core) is an exact optimum (CP-SAT, certified OPTIMAL; cross-checked by brute force on a
6-prime core).  Core members that are jointly independent of the rest of the core ("free"
members, e.g. 23 with e=11) are folded in exactly:  OPT <- OPT + w (1 - OPT).
J_i ranges over ALL earlier primes (core included) with {i} u J_i jointly independent."""
import sys, json
from exclude import compatible
def bound2(pool, core_opt, core, free, beam=64):
    pool = sorted(pool, key=lambda r: r['e'])
    by_p = {r['p']: r for r in pool}
    opt = core_opt
    for p in free: opt += (1 - opt) / by_p[p]['e']
    head = [by_p[p] for p in core + free]
    rest = [r for r in pool if r['p'] not in set(core + free)]
    order = head + rest; total = opt
    for i in range(len(head), len(order)):
        r = order[i]; earlier = sorted(order[:i], key=lambda s: s['e'])[:beam]
        best_f = 1.0
        for seed in range(len(earlier) + 1):
            T, f = [r], 1.0
            for s in earlier[seed:seed+1] + earlier:
                if s in T: continue
                if compatible(T, s): T.append(s); f *= 1 - 1 / s['e']
            best_f = min(best_f, f)
        total += best_f / r['e']
    return total
if __name__ == '__main__':
    core_opt = float(sys.argv[1]); core = [int(x) for x in sys.argv[2].split(',')]
    free = [int(x) for x in sys.argv[3].split(',')] if sys.argv[3] != '-' else []
    for path in sys.argv[4:]:
        pool = [json.loads(l) for l in open(path)]
        U = bound2(pool, core_opt, core, free)
        print(f"{path}: primes={len(pool)} sum1/e={sum(1/r['e'] for r in pool):.4f} coverage <= {U:.4f} "
              f"-> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}", flush=True)

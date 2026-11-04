"""Task 1: statistics of n(e), sum 1/e_p, index distribution, Artin-type prediction, large G(e)."""
import json, math, sys
import numpy as np
from sympy import factorint, primerange

pool = [json.loads(l) for l in open(sys.argv[1])]
EMAX = 800000
e = np.array([p['e'] for p in pool]); P = np.array([p['p'] for p in pool], dtype=np.int64)
idx = (P - 1) // e
n = np.bincount(e, minlength=EMAX + 1)

# phi and smallest-prime-factor sieve
phi = np.arange(EMAX + 1, dtype=np.float64)
for q in primerange(2, EMAX + 1):
    phi[q::q] *= (1 - 1 / q)
ratio = np.zeros(EMAX + 1); ratio[1:] = np.arange(1, EMAX + 1) / phi[1:]

print("== cumulative sum 1/e_p and count ==")
cum = np.cumsum(n / np.maximum(np.arange(EMAX + 1), 1))
for E in [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 400000, 800000]:
    print(f"E={E:7d}  #primes={int(n[:E+1].sum()):6d}  S(E)=sum1/e={cum[E]:.4f}  loglogE={math.log(math.log(E)):.4f}")

# fit S(E) = A + c*loglog E on E in [1e4, 8e5]
Es = np.array([10**x for x in np.arange(3.5, 5.91, 0.1)]).astype(int)
X = np.log(np.log(Es)); Y = cum[Es]
c, A = np.polyfit(X, Y, 1)
print(f"fit S(E) ~ {A:.4f} + {c:.4f} loglogE on [3e3,8e5]; resid max {np.max(np.abs(Y-(A+c*X))):.4f}")
Es2 = Es[Es >= 20000]; c2, A2 = np.polyfit(np.log(np.log(Es2)), cum[Es2], 1)
print(f"fit on [2e4,8e5]: S ~ {A2:.4f} + {c2:.4f} loglogE")
# alternative: S ~ A + c log E (would mean n(e) ~ const) - check increments per doubling
print("increments per doubling and per unit of loglog:")
for E in [25000, 50000, 100000, 200000, 400000, 800000]:
    d = cum[E] - cum[E // 2]; dl = math.log(math.log(E) / math.log(E / 2))
    print(f"  ({E//2},{E}]: dS={d:.4f}  dS/d(loglog)={d/dl:.4f}")

print("== kappa: n(e) ~ kappa*(e/phi(e))/log e ==")
for lo, hi in [(1000, 10000), (10000, 50000), (50000, 100000), (100000, 200000), (200000, 400000), (400000, 600000), (600000, 800000)]:
    r = np.arange(lo, hi + 1)
    pred = (ratio[r] / np.log(r)).sum()
    print(f"  e in ({lo},{hi}]: count {int(n[lo+1:hi+1].sum())}  kappa={n[lo+1:hi+1].sum()/pred:.4f}")

print("== index distribution i=(p-1)/e ==")
for lo, hi in [(0, 400000), (400000, 800000)]:
    m = (e > lo) & (e <= hi); ii = idx[m]; N = m.sum()
    s = "  ".join(f"i={k}:{(ii==k).mean():.3f}" for k in range(1, 9))
    print(f"  e in ({lo},{hi}] N={N}: {s}  i>=10:{(ii>=10).mean():.3f}  i>=100:{(ii>=100).mean():.4f} max i={ii.max()}")
    # tail exponent: P(i>=k) ~ k^-a
    ks = np.array([2, 4, 8, 16, 32, 64]); tail = np.array([(ii >= k).mean() for k in ks])
    a = -np.polyfit(np.log(ks), np.log(tail), 1)[0]
    print(f"     P(i>=k) for k={list(ks)}: {np.round(tail,4).tolist()}  -> tail exponent ~ {a:.2f} (1/i^2 density gives 1)")

print("== Artin/Kummer heuristic prediction of n(e) ==")
# P(index exactly i | p = i e + 1 prime) = sum_{d|e sqfree} mu(d) c(id)/(id)^2, c = Kummer degeneracy of <2,3>
def c_k(m):
    a = (m % 8 == 0); b = (m % 12 == 0)
    return 4 if (a and b) else (2 if (a or b) else 1)
IMAX = 3000
FI = {i: (factorint(i) if i > 1 else {}) for i in range(1, IMAX + 1)}
def pred_n(E0):
    f = factorint(E0); qs = list(f)
    sq = [1]
    for q in qs: sq = sq + [-d if d > 0 else d for d in []]  # placeholder
    # squarefree divisors with mobius
    divs = [(1, 1)]
    for q in qs: divs = divs + [(d * q, -mu) for d, mu in divs]
    tot = 0.0
    for i in range(1, IMAX + 1):
        M = i * E0
        if M % 2: continue
        fi = FI[i]
        corr = 1.0
        for q in set(qs) | set(fi): corr *= q / (q - 1)
        pr = corr / math.log(M + 1)
        fprob = sum(mu * c_k(i * d) / (i * d) ** 2 for d, mu in divs)
        tot += pr * fprob
    return tot
rng = np.random.default_rng(1)
for lo, hi in [(10000, 50000), (100000, 200000), (400000, 800000)]:
    sample = rng.integers(lo + 1, hi + 1, size=300)
    pr = np.array([pred_n(int(x)) for x in sample]); ac = n[sample]
    print(f"  e in ({lo},{hi}]: sample 300 e: mean actual n={ac.mean():.4f} mean predicted={pr.mean():.4f}  ratio={ac.mean()/pr.mean():.3f}")
    # parity split
    ev = sample % 2 == 0
    print(f"     even e: actual {ac[ev].mean():.4f} pred {pr[ev].mean():.4f};  odd e: actual {ac[~ev].mean():.4f} pred {pr[~ev].mean():.4f}")

print("== large G(e): L(e) = sum_{e_p | e} log p  (= log G(e) up to prime-power multiplicity) ==")
L = np.zeros(EMAX + 1)
lp = np.log(P.astype(np.float64))
for ee, l in zip(e, lp):
    L[ee::ee] += l
r = np.arange(1, EMAX + 1)
Lr = L[1:]
# normalise by e: log G(e) is at most e log 2
top = np.argsort(-Lr / r)[:15]
print("  top L(e)/e:", [(int(r[k]), round(float(Lr[k] / r[k]), 3)) for k in top])
top2 = np.argsort(-Lr)[:12]
print("  top L(e) absolute:", [(int(r[k]), round(float(Lr[k]), 1), dict(factorint(int(r[k])))) for k in top2])
# 'new part' log of primes with e_p == e exactly
Lnew = np.zeros(EMAX + 1)
for ee, l in zip(e, lp): Lnew[ee] += l
for lo, hi in [(1000, 10000), (100000, 200000), (400000, 800000)]:
    s = Lnew[lo + 1:hi + 1]
    print(f"  e in ({lo},{hi}]: mean log(new part)={s.mean():.2f}, mean/log e={s.mean()/math.log(hi):.3f}, max={s.max():.1f} at e={lo+1+int(np.argmax(s))} ({dict(factorint(lo+1+int(np.argmax(s))))})")
# largest n(e)
top3 = np.argsort(-n)[:10]
print("  largest n(e):", [(int(k), int(n[k]), dict(factorint(int(k)))) for k in top3])
np.save('n_e.npy', n)

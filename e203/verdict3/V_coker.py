# Independent brute force: for primitive forms (ap,bp mod a),(aq,bq mod b), density of A_p∩A_q (any offsets)
# must be <= c/(a*b), c = gcd(ap*bq-bp*aq, a, b)   [claim L2 in DISTORTION.md]; and equal for consistent offsets.
import random, math, itertools
random.seed(7)
bad=0; tested=0; tight=0
def prim(a,b,n): return math.gcd(math.gcd(a,b),n)==1
for trial in range(4000):
    a=random.choice([2,3,4,6,8,9,12,16,18,24,36]); b=random.choice([2,3,4,6,8,9,12,16,18,24,36])
    ap,bp=random.randrange(a),random.randrange(a); aq,bq=random.randrange(b),random.randrange(b)
    if not(prim(ap,bp,a) and prim(aq,bq,b)): continue
    # surjectivity onto Z/a, Z/b guaranteed by primitivity
    N=math.lcm(a,b)
    D=ap*bq-bp*aq; c=math.gcd(math.gcd(D,a),b)
    from collections import Counter
    cnt=Counter(((ap*k+bp*l)%a,(aq*k+bq*l)%b) for k in range(N) for l in range(N))
    mx=max(cnt.values())/N**2
    tested+=1
    if mx>c/(a*b)+1e-15: bad+=1; print("VIOLATION",a,b,ap,bp,aq,bq,mx,c/(a*b))
    if abs(mx-c/(a*b))<1e-15: tight+=1
print("tested",tested,"violations",bad,"tight",tight)
# planted failure: replace c by gcd(D,a,b)/2-ish (drop a factor) must fail sometimes
fails=0
for trial in range(2000):
    a=random.choice([4,6,8,12]); b=a
    ap,bp=random.randrange(a),random.randrange(a); 
    if not prim(ap,bp,a): continue
    aq,bq=ap,bp  # identical forms: intersection density 1/a, c=a
    N=a
    from collections import Counter
    cnt=Counter(((ap*k+bp*l)%a,(aq*k+bq*l)%b) for k in range(N) for l in range(N))
    mx=max(cnt.values())/N**2
    cwrong=1  # "alignment ignored"
    if mx>cwrong/(a*b)+1e-15: fails+=1
print("planted (ignore alignment) fires",fails)

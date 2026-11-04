# (1)-(2): cyclic-type prices by index from coupled_full_E200000.txt, own parsing; check Z^2/(Lam+144Z^2) = Z/gcd(e,144) on pool sample.
import math, json, random
from fractions import Fraction as F
LIGHT=F(4850936,10**8)  # approx light mass at 8e5 (float log value); CORR applied separately
r={}
for l in open('coupled_full_E200000.txt'):
    k,_,a,nA,g,nG=l.split(); A,c,d=map(int,k.split(','))
    R=(1-F(int(a),int(nA)))/(1-F(int(g),int(nG))-F(485,10000))
    if math.gcd(math.gcd(A,c),d)==1:
        n=A*d; r[n]=max(r.get(n,F(0)),R)
r[1]=F(1)
print({n:round(float(v),4) for n,v in sorted(r.items())})
# counts per index vs n*prod(1+1/q)
cnt={}
for l in open('coupled_full_E200000.txt'):
    A,c,d=map(int,l.split()[0].split(','))
    if math.gcd(math.gcd(A,c),d)==1: cnt[A*d]=cnt.get(A*d,0)+1
psi=lambda n: n*math.prod(1+F(1,q) for q in (2,3) if n%q==0)
print("all cyclic types present:",all(cnt.get(n,0)==psi(n) for n in r if n>1))
bad=[(g,float(r[2*g]/r[g])) for g in r if 2*g in r and r[2*g]/r[g]>=2]+[(g,float(r[3*g]/r[g])) for g in r if 3*g in r and r[3*g]/r[g]>=3]
print("max r(2g)/r(g)=%.3f max r(3g)/r(g)=%.3f violations %s"%(max(float(r[2*g]/r[g]) for g in r if 2*g in r),max(float(r[3*g]/r[g]) for g in r if 3*g in r),bad))
# DFS also needs monotone 'non-increasing ratio' for powers: r(g*q)/r(g) < q for every g|144 (checked above for q=2,3)
# cyclic quotient check on pool: image of Lam_p in (Z/144)^2 has index gcd(e,144)
pool=[json.loads(l) for l in open('poolE800000.jsonl')]
random.seed(4); ok=0; S=random.sample(pool,3000)
for p in S:
    a,b,e=p['alpha'],p['beta'],p['e']; g=math.gcd(e,144)
    # psi mod g on (Z/144)^2 is well defined (g|144) and onto -> kernel index g; and Lam+144Z^2 = ker(psi mod g)
    vals={(a*k+b*l)%g for k in range(g) for l in range(g)}
    ok+= len(vals)==g
print("pool sample: psi mod gcd(e,144) onto in",ok,"/",len(S))
print("CORR=(1-OPT-0.0485)/(1-OPT-light) =",float((1-F(578318,10**6)-F(485,10000))/(1-F(578318,10**6)-LIGHT)))
json.dump({str(n):float(v) for n,v in r.items()},open('verdict3/V_rcyc.json','w'))

from sympy import factorint
def sqfree(n): return all(e==1 for e in factorint(abs(n)).values())
def fundamental(D):
    if D==1: return True
    if D%4==1: return sqfree(D)
    if D%4==0:
        d=D//4
        return d%4 in (2,3) and sqfree(d)
    return False
out=set()
for a in range(0,30):
    for b in range(0,20):
        n=2**a*3**b
        for D in (n,-n):
            if fundamental(D): out.add(n)
print(sorted(out))

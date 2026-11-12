from math import comb, factorial

def stirling2(n,k):
    s=[[0]*(n+1) for _ in range(n+1)]
    s[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            s[i][j]=j*s[i-1][j]+s[i-1][j-1]
    return s[n][k]

def eulerian(n):
    a=[1]
    for r in range(2,n+1):
        b=[0]*r
        for j in range(r):
            b[j]=(j+1)*(a[j] if j<len(a) else 0)+(r-j)*(a[j-1] if j else 0)
        a=b
    return a

def check(m):
    d=2*m-1
    f=[0]*(d+1)
    for r in range(m):
        permfaces=factorial(m-r)*stirling2(m,m-r)
        for s in range(m+1):
            f[r+s]+=permfaces*comb(m,s)*2**(m-s)
    h=[0]*(d+1)
    for k, fk in enumerate(f):
        for j in range(k+1):
            h[j]+=fk*comb(k,j)*(-1)**(k-j)
    predicted=[0]*(d+1)
    for j,aj in enumerate(eulerian(m)):
        for s in range(m+1):
            predicted[j+s]+=aj*comb(m,s)
    assert h==predicted,(m,h,predicted)
    assert sum(h)==2**m*factorial(m)
    assert h==h[::-1]
    return f,h

if __name__=='__main__':
    for m in range(1,8):
        f,h=check(m)
        print(f'm={m}: f={f}; h={h}; PASS')

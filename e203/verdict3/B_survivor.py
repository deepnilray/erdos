import sys, gmpy2
m=int(sys.argv[1])
S=sorted((2**k*3**l,k,l) for k in range(1,200) for l in range(1,130) if 2**k*3**l<2**220)
for s,k,l in S:
    n=s*m+1
    if gmpy2.is_prime(n,40):
        print("m",m,"k",k,"l",l,"log2 s",round(gmpy2.log2(s),2),"digits",len(str(n)),"BPSW+40 MR PRP"); 
        if n<2**64: print("proved (<2^64)")
        break

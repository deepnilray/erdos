# D_delta.py w Wup M Cw K1 K2 : exceptional-density bound delta_w(s) = sum_r mu(r) * min(1, 1-(1-eta1)^2/((1+eta2)*ratio_r)),
# ratio_r <= Cw*(Wup + M*(1/nu_r - 1)), eta1=e^{9-s}K1^10, eta2=e^{18-s}K2^10.  nu distribution from D_data/nu_w{w}.npz.
import numpy as np, sys, math
w=int(sys.argv[1]); Wup,M,Cw,K1,K2=map(float,sys.argv[2:7])
z=np.load(f'D_data/nu_w{w}.npz'); nu=z['nu']; mu=z['mu']; s_=mu>0; nu=nu[s_]; mu=mu[s_]
for s in (24,25,26,27,28,30,35,50):
    e1=math.exp(9-s)*K1**10; e2=math.exp(18-s)*K2**10
    with np.errstate(divide='ignore'):
        ratio=Cw*(Wup+M*(1/nu-1))
        phi=np.where(nu>0,np.clip(1-(1-e1)**2/((1+e2)*ratio),0,1),1.0)
    print(f"w={w} s={s} r0={math.floor(s*1.001/0.999+1e-9)} delta<= {np.sum(mu*phi):.5f}   (mean ratio {np.sum(mu*ratio):.5f})")

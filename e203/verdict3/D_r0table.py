# D_r0table.py: for each r0, take s = (r0+1)*(1-eps)/(1+c) - 1e-6 (largest s with Omega <= r0; c=eps=0.001) and report delta bounds
# unstratified (rho<=1.028192, K1=1.033859,K2=1.141244) and stratified w=31 (D_delta inputs).
import numpy as np, math
c=eps=0.001
z=np.load('D_data/nu_w31.npz'); nu=z['nu']; mu=z['mu']; m=mu>0; nu=nu[m]; mu=mu[m]
Wup,M,Cw,K1s,K2s=1.0093865,3.4152e-3,0.9925180,1.0361162,1.0748174
rho,K1,K2=1.028192,1.25,5/3
print("r0   s       unstrat   strat(w=31)")
for r0 in range(19,36):
    s=(r0+1)*(1-eps)/(1+c)-1e-6
    if s<19: continue
    e1=math.exp(9-s)*K1**10; e2=math.exp(18-s)*K2**10
    du=min(1,1-(1-e1)**2/((1+e2)*rho))
    e1s=math.exp(9-s)*K1s**10; e2s=math.exp(18-s)*K2s**10
    ratio=Cw*(Wup+M*(1/nu-1)); ds=np.sum(mu*np.clip(1-(1-e1s)**2/((1+e2s)*ratio),0,1))
    print(f"{r0:3d} {s:7.3f}  {du:.5f}   {ds:.5f}")

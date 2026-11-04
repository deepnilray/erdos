# a5_delta_control.py: feed D's own inputs (FI eta's with K1s=1.0361162, K2s=1.0748174; D's W,M,C for w=31) through a5's exact-bin
# machinery. Must reproduce D_r0table.log's stratified column from above (binning at lower edges can only raise it) and close to it.
import pickle, math
from fractions import Fraction
NB=pickle.load(open('/home/user/erdos/e203/verdict3/D_data/a5_nubins_BW64.pkl','rb'))
Wup,M,Cw,K1s,K2s=1.0093865,3.4152e-3,0.9925180,1.0361162,1.0748174
D_ref={22:0.01995,23:0.01102,26:0.00599,29:0.00574}
for r0 in (22,23,26,29):
    s=(r0+1)*0.999/1.001-1e-6; e1=math.exp(9-s)*K1s**10; e2=math.exp(18-s)*K2s**10
    tot=0.0
    for b,wn in enumerate(NB['binw']):
        if not wn: continue
        nu=b*NB['BW']/NB['Hs']; ratio=Cw*(Wup+M*(1/nu-1))
        tot+=wn/NB['DEN']*min(1,max(0,1-(1-e1)**2/((1+e2)*ratio)))
    print(r0, "a5 bins: %.5f   D: %.5f   (a5 >= D: %s)"%(tot,D_ref[r0],tot>=D_ref[r0]-5e-6))

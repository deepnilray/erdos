// Min mean curvature of convex chains of y-rough numbers, modelled mod P = primorial(y).
// State (s,d): s = current term mod P (must be unit), d = current gap mod P (even).
// Step: choose even e>=0 (curvature); d'=d+e, s'=s+d'. Need s' unit.
// Free loops (d==0 mod P, e==0) are forbidden (they correspond to APs, killed by primes > y).
// Value iteration: f_T(v) = min_e [ e + f_{T-1}(v') ]; kappa ~ (min f_T - min f_{T-K})/K.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  int y=atoi(argv[1]); int Emax=atoi(argv[2]); int T=atoi(argv[3]);
  int primes[]={2,3,5,7,11,13,17,19,23};
  long P=1; for(int i=0;i<9&&primes[i]<=y;i++)P*=primes[i];
  char*unit=malloc(P); for(long i=0;i<P;i++)unit[i]=(gcd(i,P)==1);
  long H=P/2; // d even: index d/2
  long V=P*H;
  float*f=malloc(sizeof(float)*V),*g=malloc(sizeof(float)*V);
  const float INF=1e30f;
  for(long s=0;s<P;s++)for(long h=0;h<H;h++)f[s*H+h]=unit[s]?0:INF;
  float prev[4096];
  for(int t=1;t<=T;t++){
    float mn=INF;
    for(long s=0;s<P;s++){
      if(!unit[s]){for(long h=0;h<H;h++)g[s*H+h]=INF;continue;}
      for(long h=0;h<H;h++){
        long d=2*h; float best=INF;
        for(int e=0;e<=Emax;e+=2){
          if(e==0 && d==0) continue;
          long d2=(d+e)%P; long s2=(s+d2)%P;
          if(!unit[s2]) continue;
          float c=e+f[s2*H+d2/2];
          if(c<best)best=c;
        }
        g[s*H+h]=best; if(best<mn)mn=best;
      }
    }
    float*tmp=f;f=g;g=tmp;
    prev[t%4096]=mn;
    if(t%(T/10)==0 && t>=T/5){ int K=T/5; printf("T=%d minf=%.1f  slope(last %d)=%.5f\n",t,mn,K,(mn-prev[(t-K)%4096])/K); fflush(stdout);}
  }
  return 0;
}

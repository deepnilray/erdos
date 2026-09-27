// Pressure P(s) of y-rough convex chain automaton mod P(y): growth rate of sum over paths of exp(-s*cost).
// State (s mod P unit, d mod P even). Edge: even e in [0,Emax], not (d==0 && e==0); d'=d+e, s'=s+d' unit.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  int y=atoi(argv[1]); int Emax=atoi(argv[2]); int iters=atoi(argv[3]);
  int pr[]={2,3,5,7,11,13}; long P=1; for(int i=0;i<6&&pr[i]<=y;i++)P*=pr[i];
  char*u=malloc(P); for(long i=0;i<P;i++)u[i]=gcd(i,P)==1;
  long H=P/2,V=P*H; double*v=malloc(8*V),*w=malloc(8*V);
  for(int si=4;si<argc;si++){
    double s=atof(argv[si]); double lam=0; double logacc=0; int cnt=0;
    for(long i=0;i<V;i++) v[i]=u[i/H]?1:0;
    for(int it=0;it<iters;it++){
      double tot=0;
      for(long a=0;a<P;a++){ if(!u[a]){for(long h=0;h<H;h++)w[a*H+h]=0;continue;}
        for(long h=0;h<H;h++){ long d=2*h; double acc=0;
          for(int e=0;e<=Emax;e+=2){ if(e==0&&d==0)continue; long d2=(d+e)%P, a2=(a+d2)%P; if(!u[a2])continue; acc+=exp(-s*e)*v[a2*H+d2/2]; }
          w[a*H+h]=acc; tot+=acc; } }
      double norm=0; for(long i=0;i<V;i++) norm+=v[i];
      lam=tot/norm; if(it>=iters/2){logacc+=log(lam);cnt++;} for(long i=0;i<V;i++) v[i]=w[i]/lam;
    }
    // mean cost at s: -dP/ds via finite diff done outside
    printf("y=%d s=%.3f P(s)=%.6f\n",y,s,logacc/cnt); fflush(stdout);
  }
}

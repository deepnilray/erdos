// ell(n) = least prime q, gcd(q,n)=1, with Jacobi (q/n) = -1.  For n = 1 mod 8 non-square up to N.
// Reads uncovered set from U file; prints ell for U non-squares, and the maximum ell over all covered n (and where).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int jac(ll a, ll n){ // n odd positive
 int r=1; a%=n; while(a){ while(a%2==0){a/=2; ll m=n%8; if(m==3||m==5) r=-r;} ll t=a;a=n;n=t; if(a%4==3&&n%4==3) r=-r; a%=n;} return n==1?r:0; }
int main(int c,char**v){ ll N=atoll(v[1]);
 char*isU=calloc(N+1,1); FILE*f=fopen(v[2],"r"); ll x; while(fscanf(f,"%lld",&x)==1) if(x<=N) isU[x]=1; fclose(f);
 int P[64],np=0; for(int q=2;np<64;q++){ int ok=1; for(int i=0;i<np;i++) if(q%P[i]==0) ok=0; if(ok) P[np++]=q; }
 ll bestn[64]={0}; int hist[64]={0};
 for(ll n=9;n<=N;n+=8){ ll s=(ll)sqrt((double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; if(s*s==n) continue;
  int ell=-1; for(int i=0;i<np;i++){ if(n%P[i]==0) continue; if(jac(P[i],n)==-1){ell=P[i];break;} }
  if(ell<0) ell=1000;
  if(isU[n]) printf("U non-square n=%lld ell=%d  n^(1/4)=%.1f  log^2 n=%.0f\n",n,ell,pow((double)n,0.25),log((double)n)*log((double)n));
  else { int idx=0; while(idx<np&&P[idx]!=ell) idx++; if(idx<np){ hist[idx]++; if(n>bestn[idx]) bestn[idx]=n; } }
 }
 printf("covered non-squares: ell distribution (ell:count:largest n)\n"); for(int i=0;i<np;i++) if(hist[i]) printf("%d:%d:%lld  ",P[i],hist[i],bestn[i]); printf("\n"); return 0; }

// Mean/low-tail of R(n) for primes vs composite non-squares, n in hard classes mod 840, window [LO,HI).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static ll R(ll n){ ll r=0; for(ll m=3;m<=(n+1)/2+1;m+=4){ ll M=n+m; for(ll t=3;;t+=4){ ll a=m*t-1; if(a>M)break; if(M%a==0) r++; } } return r; }
static int isp(ll n){ if(n<2) return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
int main(int c,char**v){ ll LO=atoll(v[1]),HI=atoll(v[2]); int hard[6]={1,121,169,289,361,529};
 ll cp=0,cc=0,sp=0,sc=0,lowp=0,lowc=0,zc=0,zp=0;
 for(ll n=LO;n<HI;n++){ int ok=0; for(int k=0;k<6;k++) if(n%840==hard[k]) ok=1; if(!ok) continue;
  ll s=(ll)sqrt((double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; if(s*s==n) continue;
  ll r=R(n); if(isp(n)){cp++;sp+=r; if(r<=3) lowp++; if(r==0) zp++;} else {cc++;sc+=r; if(r<=3) lowc++; if(r==0) zc++;} }
 printf("window [%lld,%lld) hard classes, non-squares: primes n=%lld meanR=%.2f frac(R<=3)=%.4f zeros=%lld | composites n=%lld meanR=%.2f frac(R<=3)=%.4f zeros=%lld\n",LO,HI,cp,(double)sp/cp,(double)lowp/cp,zp,cc,(double)sc/cc,(double)lowc/cc,zc); return 0; }

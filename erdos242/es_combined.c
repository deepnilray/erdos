// Combined coverage of n = 1 mod 4, 5<=n<=N by FAMILY (Type I) and CHAMBERLAND (Type II, q<=4N+1).
// controls: odd squares must be missed by both (Elsholtz-Tao); 'bogus' drops the s_i | (q+1)/4 rule -> squares must get Type II reps.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll;
static int *spf;
int main(int c,char**v){ ll N=atoll(v[1]); int bogus=c>2; ll QC=4*N+1; ll H=(QC+1)/4+2;
 char*fam=calloc(N+1,1),*ch=calloc(N+1,1);
 for(ll m=3;m<=N;m+=4) for(ll t=3;m*t-1-m<=N;t+=4){ ll a=m*t-1; for(ll n=a-m;n<=N;n+=a) if(n>=5&&n%4==1) fam[n]=1; }
 spf=calloc(H+1,sizeof(int)); for(ll i=2;i<=H;i++) if(!spf[i]) for(ll j=i;j<=H;j+=i) if(!spf[j]) spf[j]=i;
 ll *D=malloc(sizeof(ll)*200000);
 for(ll q=3;q<=QC;q+=4){ ll h=(q+1)/4; int nd=0;
  if(bogus){ for(ll d=1;d<=h&&d<=60;d++) D[nd++]=d; }
  else { D[nd++]=1; ll x=h; while(x>1){ ll p=spf[x]; int e=0; while(x%p==0){x/=p;e++;} int cur=nd; ll pw=1; for(int k=1;k<=e;k++){ pw*=p; for(int i=0;i<cur;i++) D[nd++]=D[i]*pw; } } }
  for(int i=0;i<nd;i++) for(int j=i;j<nd;j++){ ll rho=(4*D[i]*D[j])%q; ll n0=(q-rho)%q; if(n0<5) n0+=q; for(ll n=n0;n<=N;n+=q) if(n%4==1) ch[n]=1; } }
 ll nf=0,nc=0,nb=0,sqf=0,sqc=0,nsq=0; 
 printf("MODE %s N=%lld q<=%lld\n",bogus?"BOGUS":"MAIN",N,QC);
 for(ll n=5;n<=N;n+=4){ ll s=(ll)sqrt((double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; int sq=(s*s==n);
  if(sq){nsq++; sqf+=fam[n]; sqc+=ch[n];}
  if(!fam[n]) nf++; if(!ch[n]) nc++; if(!fam[n]&&!ch[n]) nb++;
  if(!sq && !ch[n]) printf("non-square missed by Type II: %lld (family hit=%d)\n",n,fam[n]);
  if(!sq && !fam[n] && !ch[n]) printf("NON-SQUARE MISSED BY BOTH: %lld\n",n); }
 printf("odd squares=%lld | with family rep=%lld | with Type II rep=%lld\n",nsq,sqf,sqc);
 printf("missing family=%lld missing Type II=%lld missing both=%lld  (squares=%lld)\n",nf,nc,nb,nsq); return 0; }

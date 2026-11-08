// R(p) = #{(m,t,u): m=t=3 mod 4, u>=1, p = m*u*t - m - u} for hard primes p (classes mod 840), exhaustive to N.
// Equivalent: pairs (m,t) with a=m*t-1 | p+m. Prints min R per decade and the argmin.  usage: ./es_count N [control]
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(int c,char**v){ ll N=atoll(v[1]); int control=c>2;
 char*s=calloc(N+1,1); for(ll i=2;i*i<=N;i++) if(!s[i]) for(ll j=i*i;j<=N;j+=i) s[j]=1;
 int hard[6]={1,121,169,289,361,529};
 ll lo=10; 
 while(lo<N){ ll hi=lo*10; if(hi>N+1) hi=N+1; ll minR=1LL<<60,arg=0,cnt=0; double sum=0;
  for(ll p=lo;p<hi;p++){ if(s[p]||p<2) continue; int ok=0; for(int k=0;k<6;k++) if(p%840==hard[k]) ok=1;
   if(control){ ok = (p%4==3 && p>3); }   // control: p=3 mod 4 must give R=0 for every prime
   if(!ok) continue;
   ll R=0;
   for(ll m=3;m<=(p+1)/2+1;m+=4){ ll M=p+m; for(ll t=3;;t+=4){ ll a=m*t-1; if(a>M) break; if(M%a==0) R++; } }
   cnt++; sum+=R; if(R<minR){minR=R;arg=p;} }
  if(cnt) printf("%s p in [%lld,%lld): primes=%lld  mean R=%.1f  min R=%lld at p=%lld\n",control?"CONTROL":"MAIN",lo,hi,cnt,sum/cnt,minR,arg);
  lo=hi; }
 return 0; }

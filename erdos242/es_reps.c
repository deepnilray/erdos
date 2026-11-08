// Dump ALL family reps (m,t,u): p = m*u*t - m - u, m=t=3 mod 4, u>=1, for primes p=1 mod 4 (hard classes only unless 'all').
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(int c,char**v){ ll N=atoll(v[1]); int all=c>2;
 char*s=calloc(N+1,1); for(ll i=2;i*i<=N;i++) if(!s[i]) for(ll j=i*i;j<=N;j+=i) s[j]=1;
 int hard[6]={1,121,169,289,361,529};
 for(ll p=5;p<=N;p++){ if(s[p]||p%4!=1) continue; int ok=all; for(int k=0;k<6;k++) if(p%840==hard[k]) ok=1; if(!ok) continue;
  for(ll m=3;m<=(p+1)/2+1;m+=4){ ll M=p+m; for(ll t=3;;t+=4){ ll a=m*t-1; if(a>M) break; if(M%a==0) printf("%lld %lld %lld %lld\n",p,m,t,M/a); } } }
 return 0; }

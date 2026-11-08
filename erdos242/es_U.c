// U = { n = 1 mod 4, 5<=n<=N : no (m,t,u) with n = m*u*t - m - u, m=t=3 mod 4, u>=1 }.
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
int main(int c,char**v){ ll N=atoll(v[1]);
 for(ll n=5;n<=N;n+=4){ int hit=0;
  for(ll m=3;m<=(n+1)/2+1 && !hit;m+=4){ ll M=n+m; for(ll t=3;;t+=4){ ll a=m*t-1; if(a>M) break; if(M%a==0){hit=1;break;} } }
  if(!hit) printf("%lld\n",n); }
 return 0; }

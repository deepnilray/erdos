// Integral points (x,y,z>=1) of S_n : xyz - x - y = n, classified by residues mod 4.
// GOOD classes (each gives a Type I or Type II solution):  z=0 | x=0 | y=0 | xz=1 | yz=1  (mod 4).   'wide' adds z=2 (planted failure).
// For each n = 1 mod 4 (5..N) report: no good point.  Controls: odd squares must have NO good point; 'wide' must break this.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
int main(int c,char**v){ ll N=atoll(v[1]); int wide=c>2; ll badn=0,sqs=0,sqgood=0;
 for(ll n=5;n<=N;n+=4){ int good=0; ll npts=0;
  for(ll x=1;x<=n+1;x++){ for(ll z=1;;z++){ ll a=x*z-1; if(a<=0){continue;} if(a>n+x) break; if((n+x)%a==0){ ll y=(n+x)/a; npts++;
      int X=x%4,Y=y%4,Z=z%4; if(Z==0||X==0||Y==0||(X*Z)%4==1||(Y*Z)%4==1||(wide&&Z==2)) good=1; } } if(good) break; }
  ll s=(ll)sqrt((double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; int sq=(s*s==n);
  if(sq){sqs++; sqgood+=good;}
  if(!good && !sq) { printf("S-bad non-square n=%lld (points scanned=%lld)\n",n,npts); badn++; } }
 printf("%s N=%lld: odd squares=%lld with a good point=%lld | S-bad non-squares=%lld\n",wide?"WIDE(control)":"MAIN",N,sqs,sqgood,badn); return 0; }

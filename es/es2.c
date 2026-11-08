// Erdos-Straus for all n<=N (non-primes follow from prime factors, so test primes only).
// For x: a=4x-n, b=n*x; need d | b^2, d<=b, d == -b (mod a). Then y=(b+d)/a, z=(b+b*b/d)/a.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __int128 i128;
static u64 pr[64];static int ex[64],np;
static void fac(u64 m,u64 n){np=0;u64 t=m;for(u64 p=2;p*p<=t;p++)if(t%p==0){int e=0;while(t%p==0){t/=p;e++;}pr[np]=p;ex[np++]=e;}
 if(t>1){pr[np]=t;ex[np++]=1;}}
static u64 A,B;static int found;static u64 sy,sz;
static void rec(int i,u64 d){ if(found)return; if(i==np){ if(d<=B && (u64)((d+A-B%A)%A)==0%A+0 ){} 
  if(d<=B){ u64 r=B%A; if((d+r)%A==0){ u64 y=(B+d)/A; u64 z=(B+(u64)(((i128)B*B)/d))/A; found=1;sy=y;sz=z;} } return;}
 u64 q=1; for(int e=0;e<=2*ex[i];e++){ rec(i+1,d*q); q*=pr[i]; if(d*q>B&&0)break; } }
int main(int c,char**v){u64 N=atoll(v[1]);u64 maxk=0,argk=0,fail=0,cnt=0;
 char*s=calloc(N+1,1);
 for(u64 n=2;n<=N;n++){ if(s[n])continue; for(u64 m=n*n;m<=N;m+=n)s[m]=1; cnt++;
  found=0; u64 x0=n/4+1;
  for(u64 x=x0;x<=3*n/4+1&&!found;x++){ A=4*x-n; B=n*x; // combine factorisation of n (prime) and x
    fac(x,n); int k=np; // add n
    int hit=0; for(int j=0;j<np;j++)if(pr[j]==n){ex[j]++;hit=1;} if(!hit){pr[np]=n;ex[np++]=1;}
    for(int j=0;j<np;j++)ex[j]=ex[j]; rec(0,1);
    if(found){ u64 k2=x-x0; if(k2>maxk){maxk=k2;argk=n;} }
  }
  if(!found){printf("FAIL %llu\n",n);fail++;}
 }
 printf("primes<=%llu: %llu tested, fails=%llu, max x-offset=%llu at n=%llu\n",N,cnt,fail,maxk,argk);}

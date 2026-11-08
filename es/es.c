// Erdos-Straus: for each n in [2,N], find x<=y<=z with 4/n=1/x+1/y+1/z by direct search.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __int128 i128;
int main(int c,char**v){u64 N=atoll(v[1]);u64 maxk=0,argk=0,fail=0;
 // hard-class count: n mod 840 in Mordell's 6 classes
 for(u64 n=2;n<=N;n++){int ok=0;
  u64 x0=n/4+1;
  for(u64 x=x0;x<=n/2+1&&!ok;x++){ // 1/x<4/n and x<=3n/4
   u64 a=4*x-n; if((i128)4*x<=n)continue; u64 b=n*x; // a/b = 1/y+1/z
   u64 ylo=b/a+1, yhi=(2*b)/a;
   for(u64 y=ylo;y<=yhi;y++){ i128 num=(i128)a*y-b; if(num<=0)continue;
     i128 den=(i128)b*y; if(den%num==0){ok=1;u64 k=x-x0;if(k>maxk){maxk=k;argk=n;}break;}}
  }
  if(!ok){printf("FAIL %llu\n",n);fail++;}
 }
 printf("N=%llu fails=%llu max x-offset=%llu at n=%llu\n",N,fail,maxk,argk);}

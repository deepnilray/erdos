// Longest convex chain of primes <= N (nondecreasing gaps). L[j][g]: best length ending at prime j with last gap g.
// For each prime p (increasing), for each earlier prime r with p-r=g<=G: L(p,g)=1+max_{g'<=g} L(r,g') (or 2).
// Store for each prime the prefix-max array over gaps (even gaps, index g/2) up to G.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); int G=atoi(argv[2]); int H=G/2+1;
  char*c=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!c[i]) for(long j=i*i;j<=N;j+=i)c[j]=1;
  long np=0; long*pr=malloc(sizeof(long)*(N/2+10)); for(long i=3;i<=N;i++) if(!c[i]) pr[np++]=i;
  unsigned short*PM=calloc((size_t)np*H,sizeof(unsigned short)); // prefix max of L over gap index
  int best=0; long bestp=0; 
  long checkpoints[64]; int nc=0; for(long x=1000;x<=N;x*=2) checkpoints[nc++]=x; int ci=0;
  long lo=0;
  for(long j=0;j<np;j++){
    long p=pr[j];
    unsigned short*row=PM+(size_t)j*H;
    while(pr[lo] < p-G) lo++;
    for(long i=j-1;i>=lo;i--){
      int g=p-pr[i]; int h=g/2;
      unsigned short v=PM[(size_t)i*H+h]; // max over gaps <= g ending at pr[i]
      unsigned short Lv = v? v+1 : 2;
      if(Lv>row[h]) row[h]=Lv;
    }
    for(int h=1;h<H;h++) if(row[h-1]>row[h]) row[h]=row[h-1];
    if(row[H-1]>best){best=row[H-1];bestp=p;}
    while(ci<nc && p>checkpoints[ci]){ printf("N=%ld maxlen=%d ratio len/sqrt(N)=%.4f  N/len^2=%.4f\n",checkpoints[ci],best,best/sqrt((double)checkpoints[ci]),(double)checkpoints[ci]/((double)best*best)); fflush(stdout); ci++;}
  }
  printf("N=%ld maxlen=%d N/len^2=%.4f\n",N,best,(double)N/((double)best*best));
}

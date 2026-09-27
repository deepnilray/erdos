// Longest convex chain of primes q_1<...<q_n (any start prime, q_1 may be 2) with q_k <= C k^2 for all k.
// DP over (prime, last gap): L = max valid length; extension to p valid iff p <= C*(L+1)^2.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  double C=atof(argv[1]); long N=atol(argv[2]); int G=atoi(argv[3]); int H=G+1;
  char*c=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!c[i]) for(long j=i*i;j<=N;j+=i)c[j]=1;
  long np=0; long*pr=malloc(sizeof(long)*(N/2+10)); for(long i=2;i<=N;i++) if(!c[i]) pr[np++]=i;
  unsigned short*PM=calloc((size_t)np*H,2); // prefix max over gap (all gaps, not only even, since 2->3 gap 1)
  int best=0; long bestp=0; long lo=0;
  for(long j=0;j<np;j++){
    long p=pr[j]; unsigned short*row=PM+(size_t)j*H;
    if(p<=C*1.0) row[0]=1; // chain of length 1 starting at p needs p<=C*1
    // encode length-1 chains as gap-0 entry
    while(pr[lo]<p-G) lo++;
    for(long i=j-1;i>=lo;i--){ int g=p-pr[i]; unsigned short v=PM[(size_t)i*H+g];
      if(v && p <= C*(double)(v+1)*(v+1)) { if(v+1>row[g]) row[g]=v+1; } }
    for(int g=1;g<H;g++) if(row[g-1]>row[g]) row[g]=row[g-1];
    if(row[H-1]>best){best=row[H-1];bestp=p;}
  }
  printf("C=%.2f N=%ld G=%d longest=%d (ends at %ld)  C*len^2=%.0f\n",C,N,G,best,bestp,C*best*(double)best);
}

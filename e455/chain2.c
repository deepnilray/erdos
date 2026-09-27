// Exact longest convex chain of odd primes <= N (nondecreasing gaps), with backtracking.
// L[j][h] = best length of chain ending at prime j whose last gap is exactly 2h (0 if none); PM = prefix max.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); int G=atoi(argv[2]); int H=G/2+1;
  char*c=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!c[i]) for(long j=i*i;j<=N;j+=i)c[j]=1;
  long np=0; long*pr=malloc(sizeof(long)*(N/2+10)); for(long i=3;i<=N;i++) if(!c[i]) pr[np++]=i;
  long*idx=malloc(sizeof(long)*(N+1)); for(long j=0;j<np;j++) idx[pr[j]]=j;
  unsigned short*PM=calloc((size_t)np*H,2);
  int best=0; long bj=0; int bh=0; long lo=0;
  for(long j=0;j<np;j++){
    long p=pr[j]; unsigned short*row=PM+(size_t)j*H;
    while(pr[lo]<p-G) lo++;
    for(long i=j-1;i>=lo;i--){ int h=(p-pr[i])/2; unsigned short v=PM[(size_t)i*H+h]; unsigned short Lv=v?v+1:2; if(Lv>row[h])row[h]=Lv; }
    // record exact before prefix max: store exact in separate pass? use trick: exact value = row[h] now
    for(int h=1;h<H;h++){ if(row[h]>best){best=row[h];bj=j;bh=h;} }
    for(int h=1;h<H;h++) if(row[h-1]>row[h]) row[h]=row[h-1];
  }
  // backtrack: at prime j with last gap 2h and length Lcur, previous prime r=p-2h must have PM[r][h] == Lcur-1 (or Lcur==2)
  long *ch=malloc(sizeof(long)*(best+2)); int n=0; long j=bj; int h=bh; int Lc=best;
  ch[n++]=pr[j];
  while(Lc>=2){ long r=pr[j]-2*h; ch[n++]=r; long i=idx[r]; if(Lc==2)break;
     // find largest h'<=h with exact value Lc-1: PM prefix max, so find minimal h' with PM[i][h']>=Lc-1
     int hh=1; while(PM[(size_t)i*H+hh]<Lc-1) hh++; j=i; h=hh; Lc--; }
  printf("N=%ld G=%d maxlen=%d N/len^2=%.4f\n",N,G,best,(double)N/((double)best*best));
  FILE*f=fopen(argv[3],"w"); for(int k=n-1;k>=0;k--) fprintf(f,"%ld\n",ch[k]); fclose(f);
}

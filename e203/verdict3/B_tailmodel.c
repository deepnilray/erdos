// Far-tail test of the Cramer/Bateman-Horn model against the exhaustive search (verdict3 step 4).
// For m sampled uniformly (coprime to 6) in [LO,HI], build the cells (k>=1,l>=1) with s=2^k3^l < 2^BMAX,
// sieve them EXACTLY by the primes 5..Z (cell killed iff p | s*m+1, i.e. s == -1/m mod p), and give each
// survivor the sieve-corrected probability of being prime  P = prod_{p<=Z}(1-1/p)^{-1} / ln(s*m+1).
// Output for each b: Pmodel(b) = mean_m prod_{cells s<2^b}(1-P_cell)  = model P(first prime has s >= 2^b),
// with the batch standard error.   usage: tailmodel LO HI NSAMP Z seed
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#define BMAX 33
typedef unsigned long long u64;
static u64 rs; static u64 rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){
  u64 LO=strtoull(argv[1],0,10), HI=strtoull(argv[2],0,10); long NS=atol(argv[3]); int Z=atoi(argv[4]); rs=strtoull(argv[5],0,10)*2654435761ULL+88172645463325252ULL;
  // cells
  static u64 S[4000]; int nc=0;
  for(int k=1;k<BMAX;k++){ u64 v=(1ULL<<k)*3; for(int l=1;;l++){ if(v>=(1ULL<<BMAX)) break; S[nc++]=v; v*=3; } }
  for(int i=0;i<nc;i++) for(int j=i+1;j<nc;j++) if(S[j]<S[i]){u64 t=S[i];S[i]=S[j];S[j]=t;}
  int NP=0; static int P[2000]; for(int p=5;p<=Z;p++){int ok=1; for(int q=2;q*q<=p;q++) if(p%q==0){ok=0;break;} if(ok) P[NP++]=p;}
  static unsigned short *RES[2000], *INV[2000];
  for(int j=0;j<NP;j++){ int p=P[j]; RES[j]=malloc(nc*2); INV[j]=malloc(p*2);
    for(int i=0;i<nc;i++) RES[j][i]=S[i]%p;
    for(int r=1;r<p;r++){ for(int x=1;x<p;x++) if((x*r)%p==1){INV[j][r]=x;break;} } }
  double lnS=log(3.0); for(int j=0;j<NP;j++) lnS-=log(1.0-1.0/P[j]);   // log prod_{p<=Z}(1-1/p)^{-1} incl p=2,3
  double SS=exp(lnS);
  int nb=30; // batches for standard error
  double acc[BMAX+1]={0}, bacc[30][BMAX+1]; for(int b=0;b<nb;b++) for(int i=0;i<=BMAX;i++) bacc[b][i]=0;
  long done=0; static char kill[4000];
  while(done<NS){
    u64 m=LO+rnd()%(HI-LO+1); if(m%2==0||m%3==0) continue;
    for(int i=0;i<nc;i++) kill[i]=0;
    for(int j=0;j<NP;j++){ int p=P[j]; int r=m%p; if(!r) continue; int t=(p-INV[j][r])%p; unsigned short*R=RES[j]; for(int i=0;i<nc;i++) kill[i]|=(R[i]==t); }
    double lm=log((double)m); double ls=0; int ci=0; double res[BMAX+1];
    for(int b=1;b<=BMAX;b++){
      while(ci<nc && S[ci]<(1ULL<<b)){ if(!kill[ci]){ double Pc=SS/(log((double)S[ci])+lm); if(Pc>=1) Pc=0.999999; ls+=log1p(-Pc);} ci++; }
      res[b]=exp(ls);
    }
    int bi=done%nb; for(int b=1;b<=BMAX;b++){ acc[b]+=res[b]; bacc[bi][b]+=res[b]; }
    done++;
  }
  printf("# LO=%llu HI=%llu NSAMP=%ld Z=%d cells=%d primes=%d prod=%.4f\n",LO,HI,NS,Z,nc,NP,SS);
  for(int b=1;b<=BMAX;b++){ double mean=acc[b]/NS; double var=0; for(int i=0;i<nb;i++){ double x=bacc[i][b]/(NS/(double)nb); var+=(x-mean)*(x-mean);} double se=sqrt(var/(nb*(nb-1.0)));
    printf("b=%d Pmodel=%.6e se=%.2e\n",b,mean,se); }
  return 0; }

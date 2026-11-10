// Exhaustive search for valid n-sets in Z_N up to affine equivalence (x -> ux+v).
// Normal form: for a divisor d of N (d<N): A contains 0 and d, and gcd(x-y,N) >= d for all pairs x,y in A.
// Every valid set is affinely equivalent to at least one such set (take a pair whose difference has minimal gcd with N).
// Validity is hereditary, so every prefix must be valid (prefix sets checked as k-sets).
// usage: enum2 n N [print]      (N <= 256)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef struct { uint64_t w[4]; } bs;
static int n,N,prt,W; static uint64_t lastmask;
static int gcdtab[257];
static int gcd(int a,int b){ while(b){int t=a%b;a=b;b=t;} return a; }
static inline int getbit(const bs*x,int i){ return (x->w[i>>6]>>(i&63))&1; }
static inline void rot(bs*r,const bs*x,int b){ // r = x rotated left by b (mod N)
  // (x<<b) | (x>>(N-b)), masked to N bits
  bs lo,hi; int s=b; int ws=s>>6, bsft=s&63;
  for(int i=3;i>=0;i--){ uint64_t v=0; int j=i-ws; if(j>=0){ v=x->w[j]<<bsft; if(bsft&&j-1>=0) v|=x->w[j-1]>>(64-bsft); } lo.w[i]=v; }
  s=N-b; ws=s>>6; bsft=s&63;
  for(int i=0;i<4;i++){ uint64_t v=0; int j=i+ws; if(j<4){ v=x->w[j]>>bsft; if(bsft&&j+1<4) v|=x->w[j+1]<<(64-bsft); } hi.w[i]=v; }
  for(int i=0;i<4;i++) r->w[i]=lo.w[i]|hi.w[i];
  r->w[W-1]&=lastmask; for(int i=W;i<4;i++) r->w[i]=0; }
static int B[32]; static long long cnt=0,nodes=0,checks=0;
static int valid(int d){ // set {0} U B[0..d-1] as (d+1)-set
  int nn=d+1; static bs g1[40],g2[40]; checks++;
  for(int j=0;j<=nn;j++){ memset(&g1[j],0,sizeof(bs)); memset(&g2[j],0,sizeof(bs)); } g1[0].w[0]=1;
  for(int i=0;i<d;i++){ int b=B[i];
    for(int j=1;j<=nn;j++){ bs r1,r2; rot(&r1,&g1[j-1],b); rot(&r2,&g2[j-1],b);
      for(int t=0;t<W;t++){ g2[j].w[t]|= r2.w[t] | (g1[j].w[t]&r1.w[t]); g1[j].w[t]|=r1.w[t]; } } }
  int s=0; for(int i=0;i<d;i++) s=(s+B[i])%N;
  int c=0; for(int j=0;j<=nn;j++){ if(getbit(&g2[j],s)) return 0; if(getbit(&g1[j],s)) c++; }
  return c==1; }
static int dmin;
static void rec(int d,int start){
  nodes++;
  if(d==n-1){ cnt++; if(prt){ printf("%d: 0",N); for(int i=0;i<d;i++) printf(" %d",B[i]); printf("\n"); fflush(stdout);} return; }
  for(int b=start;b<N;b++){ if(b==dmin) continue;
    if(gcdtab[b]<dmin) continue; int ok=1;
    for(int i=0;i<d;i++){ int df=b-B[i]; if(df<0) df=-df; if(gcdtab[df]<dmin){ok=0;break;} }
    if(!ok) continue;
    B[d]=b; if(valid(d+1)) rec(d+1,b+1); } }
int main(int argc,char**argv){ n=atoi(argv[1]); N=atoi(argv[2]); prt=argc>3; W=(N+63)/64; lastmask=(N%64)?((1ULL<<(N%64))-1):~0ULL;
  for(int i=0;i<=256;i++) gcdtab[i]=gcd(i%N,N); gcdtab[0]=N;
  for(dmin=1;dmin<N;dmin++){ if(N%dmin) continue; B[0]=dmin; if(n==2){ if(valid(1)) {cnt++;} continue; } if(valid(1)) rec(1,1); }
  fprintf(stderr,"n=%d N=%d normal_form_valid_sets=%lld nodes=%lld checks=%lld\n",n,N,cnt,nodes,checks); return 0; }

// Enumerate valid n-sets in Z_N containing 0 (Fonollosa validity), hereditary pruning.
// usage: enum n N [print]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static int n,N,prt; static u128 MASK;
static inline u128 rot(u128 x,int b){ // rotate left by b within N bits
  b%=N; if(!b) return x; return ((x<<b)|(x>>(N-b)))&MASK; }
static int B[64]; static long long cnt=0, nodes=0;
// validity of set {0} U B[0..d-1] with size bound d+1
static int valid(int d){
  int nn=d+1; u128 g1[70],g2[70];
  for(int j=0;j<=nn;j++){g1[j]=0;g2[j]=0;} g1[0]=1;
  for(int i=0;i<d;i++){ int b=B[i];
    for(int j=1;j<=nn;j++){ u128 r1=rot(g1[j-1],b), r2=rot(g2[j-1],b);
      g2[j]|= r2 | (g1[j]&r1); g1[j]|=r1; } }
  int s=0; for(int i=0;i<d;i++) s=(s+B[i])%N;
  int c=0; for(int j=0;j<=nn;j++){ if((g2[j]>>s)&1) return 0; if((g1[j]>>s)&1) c++; }
  return c==1; }
static void rec(int d,int start){
  nodes++;
  if(d==n-1){ cnt++; if(prt){ printf("0"); for(int i=0;i<d;i++) printf(" %d",B[i]); printf("\n"); } return; }
  for(int b=start;b<N;b++){ B[d]=b; if(valid(d+1)) rec(d+1,b+1); } }
int main(int argc,char**argv){ n=atoi(argv[1]); N=atoi(argv[2]); prt=argc>3;
  MASK = (N==128)? ~(u128)0 : (((u128)1<<N)-1);
  rec(0,1); fprintf(stderr,"n=%d N=%d valid_sets_with_0=%lld nodes=%lld\n",n,N,cnt,nodes); return 0; }

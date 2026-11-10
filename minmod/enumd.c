// Enumerate n-sets in Z_N containing 0 that are dissociated at every anchor. usage: enumd n N [print]
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
static int n,N,prt; static u128 MASK;
static inline u128 rot(u128 x,int b){ b%=N; if(b<0)b+=N; if(!b) return x; return ((x<<b)|(x>>(N-b)))&MASK; }
static int A[64]; static long long cnt=0;
static int diss(int k){ // set A[0..k-1]; all anchors
  for(int c=0;c<k;c++){ u128 R=1; for(int i=0;i<k;i++){ if(i==c) continue; int b=((A[i]-A[c])%N+N)%N; u128 r=rot(R,b); if(r&R) return 0; R|=r; } }
  return 1; }
static void rec(int k,int start){
  if(k==n){ cnt++; if(prt){ for(int i=0;i<k;i++) printf("%d ",A[i]); printf("\n"); } return; }
  for(int b=start;b<N;b++){ A[k]=b; if(diss(k+1)) rec(k+1,b+1); } }
int main(int argc,char**argv){ n=atoi(argv[1]); N=atoi(argv[2]); prt=argc>3; MASK=(N==128)?~(u128)0:(((u128)1<<N)-1);
  A[0]=0; rec(1,1); fprintf(stderr,"n=%d N=%d count=%lld\n",n,N,cnt); return 0; }

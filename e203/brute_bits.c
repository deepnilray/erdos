/* Exact max coverage by one coset per prime, bitset brute force (first prime's offset fixed by
   translation symmetry).  Cells of G_S = Z^2/L_S enumerated via HNF [[A,0],[C,D]]. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include FAM
#define W ((A*D+63)/64)
static uint64_t *bits[NP];   /* bits[i][c*W + w] = cells with psi_i == c */
int main(void){
  long n=(long)A*D;
  for(int i=0;i<NP;i++){ bits[i]=calloc((size_t)E[i]*W,8);
    for(long k=0;k<A;k++)for(long l=0;l<D;l++){ long x=k*D+l; long c=(AL[i]*k+BE[i]*l)%E[i];
      bits[i][c*W+x/64] |= 1ULL<<(x%64);} }
  int ch[NP]={0}; long best=-1; uint64_t acc[NP][W];
  /* depth-first over offsets with prefix ORs */
  int depth=1; memcpy(acc[0],bits[0],8*W);
  for(;;){
    if(depth==NP){ long cnt=0; for(int w=0;w<W;w++) cnt+=__builtin_popcountll(acc[NP-1][w]);
      if(cnt>best)best=cnt; depth--; }
    else { for(int w=0;w<W;w++) acc[depth][w]=acc[depth-1][w]|bits[depth][ch[depth]*W+w]; depth++; continue; }
    /* advance */
    while(depth>0 && ++ch[depth]==E[depth]){ ch[depth]=0; depth--; }
    if(depth==0) break;
  }
  printf("cells=%ld best=%ld frac=%.9f\n",n,best,(double)best/n);
}

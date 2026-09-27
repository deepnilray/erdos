/* Brute force max coverage of G = Z^2/L (HNF [[A,0],[C,D]]) by one coset per prime.
   Cells (k,l), 0<=k<A, 0<=l<D.  Prime i kills cell iff (AL[i]k+BE[i]l) mod E[i] == choice[i].
   First prime's choice fixed to 0 (translation symmetry).  Independent check of CP-SAT. */
#include <stdio.h>
#include <stdlib.h>
#include "core6.h"
int main(void){
  int n=A*D; int *val=malloc(sizeof(int)*n*NP);
  for(int k=0;k<A;k++)for(int l=0;l<D;l++)for(int i=0;i<NP;i++)
    val[(k*D+l)*NP+i]=(int)(((long)AL[i]*k+(long)BE[i]*l)%E[i]);
  int ch[NP]={0}; long best=-1, combos=0;
  for(;;){
    long cov=0;
    for(int x=0;x<n;x++){int *v=val+x*NP; for(int i=0;i<NP;i++) if(v[i]==ch[i]){cov++;break;}}
    if(cov>best)best=cov; combos++;
    int i=1; while(i<NP && ++ch[i]==E[i]){ch[i]=0;i++;} if(i==NP)break;
  }
  printf("cells=%d combos=%ld best=%ld frac=%.6f\n",n,combos,best,(double)best/n);
}

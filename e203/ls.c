/* Coordinate-ascent local search with perturbation for max coverage of G_S.
   cnt[x] = number of chosen cosets containing cell x.  For prime i, the best coset is
   argmax_c #{x : psi_i(x)=c, cnt[x]-[psi_i(x)==ch_i]==0}.  Reports best coverage fraction. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include FAM
static unsigned char *cnt; static unsigned short *psi[NP]; static long n;
static long covered(void){long s=0; for(long x=0;x<n;x++) s+=cnt[x]>0; return s;}
int main(int argc,char**argv){
  int rounds=argc>1?atoi(argv[1]):30; srand(argc>2?atoi(argv[2]):1);
  n=(long)A*D; cnt=calloc(n,1);
  for(int i=0;i<NP;i++){psi[i]=malloc(sizeof(unsigned short)*n);
    for(long k=0;k<A;k++)for(long l=0;l<D;l++) psi[i][k*D+l]=(unsigned short)((AL[i]*k+BE[i]*l)%E[i]);}
  int ch[NP], bestch[NP]; long best=-1;
  for(int i=0;i<NP;i++){ch[i]=rand()%E[i]; for(long x=0;x<n;x++) if(psi[i][x]==ch[i]) cnt[x]++;}
  long *gain=malloc(sizeof(long)*100000);
  for(int r=0;r<rounds;r++){
    for(int pass=0;pass<4;pass++) for(int i=0;i<NP;i++){
      memset(gain,0,sizeof(long)*E[i]);
      for(long x=0;x<n;x++){int c=psi[i][x]; int own=(c==ch[i]); if(cnt[x]-own==0) gain[c]++;}
      int bc=ch[i]; for(int c=0;c<E[i];c++) if(gain[c]>gain[bc]) bc=c;
      if(bc!=ch[i]){ for(long x=0;x<n;x++){int c=psi[i][x]; if(c==ch[i])cnt[x]--; else if(c==bc)cnt[x]++;} ch[i]=bc; }
    }
    long cv=covered(); if(cv>best){best=cv; memcpy(bestch,ch,sizeof ch);}
    fprintf(stderr,"round %d coverage %.6f best %.6f\n",r,(double)cv/n,(double)best/n);
    /* perturb: re-randomise 3 primes */
    for(int t=0;t<3;t++){int i=rand()%NP,nc=rand()%E[i];
      for(long x=0;x<n;x++){int c=psi[i][x]; if(c==ch[i])cnt[x]--; else if(c==nc)cnt[x]++;} ch[i]=nc;}
  }
  printf("cells=%ld best_coverage=%.6f choice:",n,(double)best/n); for(int i=0;i<NP;i++) printf(" %ld:%d",P[i],bestch[i]); printf("\n");
}

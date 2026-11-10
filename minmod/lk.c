// L_k(n): min N s.t. exists D (|D|=k, 0 in D), A'' (|A''|=n-k) in Z_N with:
// every nonzero x in Lambda (sum 0, value 0 mod N) with |x_l|<=1 off D has max>=2 and min<=-2.
// usage: lk k n Nlo Nhi [all]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 600
#define MAXM 12
static int k,n,m,N,showall; static int D[8],App[MAXM];
static unsigned char forb[2*MAXM+3][MAXN]; // forb[sigma+MAXM+1][r]: exists x_D (>=-1 or <=1), sum sigma, value r
static unsigned char forb0nz[MAXN];        // sigma=0, x_D nonzero
static unsigned char reach[MAXM+1][2*MAXM+3][MAXN]; // level, s, residue : nonzero z
static long long nsol;
static int xs[8];
static void gen(int idx,int rem,int lo,int sign,int sigma,int val,int nz){ // entries >= lo summing rem (in y=sign*x coords)
  if(idx==k-1){ int y=rem; if(y<lo) return; int x=sign*y; int v=((val+x*D[idx])%N+N)%N; int z=nz||x!=0;
    forb[sigma+MAXM+1][v]=1; if(sigma==0&&z) forb0nz[v]=1; return; }
  for(int y=lo;y<=rem-(k-1-idx)*lo;y++){ int x=sign*y; gen(idx+1,rem-y,lo,sign,sigma,((val+x*D[idx])%N+N)%N,nz||x!=0); } }
static void build_forb(){ memset(forb,0,sizeof forb); memset(forb0nz,0,sizeof forb0nz);
  for(int sigma=-m-1;sigma<=m+1;sigma++){ gen(0,sigma,-1,1,sigma,0,0); gen(0,-sigma,-1,-1,sigma,0,0); } }
static int check(int lev){ // reach[lev] built; check
  for(int s=-lev;s<=lev;s++){ unsigned char*R=reach[lev][s+MAXM+1]; unsigned char*F=forb[-s+MAXM+1];
    for(int r=0;r<N;r++) if(R[r] && F[(N-r)%N]) return 0; }
  return 1; }
static void rec(int lev,int start){
  if(lev==m){ nsol++; if(nsol==1||showall){ printf("N=%d D=",N); for(int i=0;i<k;i++) printf("%d ",D[i]); printf("A''="); for(int i=0;i<m;i++) printf("%d ",App[i]); printf("\n"); } return; }
  for(int b=start;b<N;b++){ int inD=0; for(int i=0;i<k;i++) if(D[i]==b) inD=1; if(inD) continue;
    App[lev]=b; memset(reach[lev+1],0,sizeof reach[lev+1]);
    for(int s=-lev;s<=lev;s++){ unsigned char*R=reach[lev][s+MAXM+1]; 
      for(int r=0;r<N;r++) if(R[r]){ reach[lev+1][s+MAXM+1][r]=1; reach[lev+1][s+1+MAXM+1][(r+b)%N]=1; reach[lev+1][s-1+MAXM+1][(r-b+N)%N]=1; } }
    reach[lev+1][1+MAXM+1][b]=1; reach[lev+1][-1+MAXM+1][(N-b)%N]=1;
    if(check(lev+1)){ rec(lev+1,b+1); if(nsol&&!showall) return; } } }
static void recD(int idx,int start){
  if(idx==k){ build_forb(); if(forb0nz[0]) return; memset(reach[0],0,sizeof reach[0]); rec(0,1); return; }
  for(int d=start;d<N;d++){ D[idx]=d; recD(idx+1,d+1); if(nsol&&!showall) return; } }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]); m=n-k; int Nlo=atoi(argv[3]),Nhi=atoi(argv[4]); showall=argc>5;
  for(N=Nlo;N<=Nhi;N++){ nsol=0; D[0]=0; recD(1,1); if(nsol){ printf("k=%d n=%d N=%d #solutions(found)=%lld\n",k,n,N,nsol); if(!showall) break; } }
  if(!nsol) printf("k=%d n=%d none in [%d,%d]\n",k,n,Nlo,Nhi); return 0; }

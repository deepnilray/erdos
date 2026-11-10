// 1D single-pair structure: find min N with beta_1<..<beta_m in Z_N s.t. for S!=S', |S'|>=|S|:
// (beta(S')-beta(S)) mod N in [|S'|-|S|+2, N-2].   usage: oned m Nmax
#include <stdio.h>
#include <stdlib.h>
static int m,N; static int beta[16]; static int pos[1<<12], wt[1<<12]; static long long found;
static int ok(int k){ // check cube on first k generators: new elements = old + beta[k-1]
  int half=1<<(k-1), full=1<<k;
  for(int s=0;s<half;s++){ pos[half+s]=(pos[s]+beta[k-1])%N; wt[half+s]=wt[s]+1; }
  for(int s=half;s<full;s++) for(int t=0;t<full;t++){ if(t==s) continue; if(t>=half && t>s) continue;
      int a=s,b=t; // ensure wt[b]>=wt[a]
      if(wt[a]>wt[b]){int x=a;a=b;b=x;}
      int d=((pos[b]-pos[a])%N+N)%N; int dw=wt[b]-wt[a];
      if(d<dw+2||d>N-2) return 0;
      if(dw==0){ int d2=N-d; if(d2<2||d2>N-2) return 0; } }
  return 1; }
static void rec(int k,int start){ if(found) return; if(k==m){ found=1; printf("m=%d N=%d beta:",m,N); for(int i=0;i<m;i++) printf(" %d",beta[i]); printf("\n"); return; }
  for(int b=start;b<N;b++){ beta[k]=b; if(ok(k+1)) rec(k+1,b+1); if(found) return; } }
int main(int argc,char**argv){ m=atoi(argv[1]); int Nmax=atoi(argv[2]); pos[0]=0; wt[0]=0;
  for(N=4;N<=Nmax;N++){ found=0; rec(0,1); if(found) break; } if(!found) printf("m=%d none up to %d\n",m,Nmax); return 0; }

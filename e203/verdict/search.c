// Erdos #203 direct search: for each m in [M0,M1], gcd(m,6)=1, find the first (k,l)
// in order of increasing 2^k 3^l such that 2^k 3^l m + 1 is prime (deterministic for n < 2^64:
// Miller-Rabin with Sinclair's 7 bases is a proof of primality below 2^64).
// m with no prime below 2^64 are printed as SURVIVOR lines (to be handled by gmpy2).
// usage: search M0 M1 [control]
//   control=1: restrict to l=0 (1D Sierpinski family), to check the detector can fire.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
typedef unsigned __int128 u128;
typedef uint64_t u64;

#define MAXS 4000
static u64 S[MAXS]; static int SK[MAXS], SL[MAXS]; static int NS;

static inline u64 mmul(u64 a, u64 b, u64 n, u64 ninv){
  u128 t=(u128)a*b; u64 lo=(u64)t, hi=(u64)(t>>64);
  u64 q=lo*ninv; u64 mh=(u64)(((u128)q*n)>>64);
  return hi>=mh ? hi-mh : hi-mh+n;
}
static int sprp(u64 n, u64 a, u64 ninv, u64 one, u64 r2, u64 d, int s){
  a%=n; if(!a) return 1;
  u64 x=mmul(a,r2,n,ninv), res=one, mone=n-one;
  u64 e=d;
  while(e){ if(e&1) res=mmul(res,x,n,ninv); x=mmul(x,x,n,ninv); e>>=1; }
  if(res==one||res==mone) return 1;
  for(int i=1;i<s;i++){ res=mmul(res,res,n,ninv); if(res==mone) return 1; if(res==one) return 0; }
  return 0;
}
static long long nMR=0;
static int isprime64(u64 n){
  if(n<2) return 0;
  static const int sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n==(u64)sp[i]) return 1; if(n%sp[i]==0) return 0; }
  if(n<1369) return 1;
  nMR++;
  u64 ninv=n; for(int i=0;i<6;i++) ninv*=2-n*ninv; // n^{-1} mod 2^64
  ninv=-ninv; // we need q = lo * (-n^{-1})? see below
  // Using REDC variant hi(t)-hi(q n) with q = lo * n^{-1}: lo(t)-lo(qn)=0.
  ninv=-ninv;
  u64 one=(u64)(-n)%n; u64 r2=(u64)(((u128)one*one)%n);
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  static const u64 B[7]={2,325,9375,28178,450775,9780504,1795265022};
  for(int i=0;i<7;i++) if(!sprp(n,B[i],ninv,one,r2,d,s)) return 0;
  return 1;
}
static int cmpu(const void*a,const void*b){ u64 x=*(u64*)a,y=*(u64*)b; return x<y?-1:x>y; }

#define NP 62
#define NW 4
static int P[NP];
static uint16_t TGT[NP][2000];     // TGT[j][r] = -r^{-1} mod p
static u64 MASK[NP][2000][NW];    // indices i<256 with S[i] = t mod p
static u64 K0MASK[NW];

int main(int argc,char**argv){
  u64 M0=strtoull(argv[1],0,10), M1=strtoull(argv[2],0,10);
  int control = argc>3 ? atoi(argv[3]) : 0;
  // smooth numbers up to 2^63
  u64 tmp[MAXS]; int n=0;
  for(int k=0;k<63;k++){ u64 p2=1ULL<<k; u64 v=p2; for(int l=0;;l++){ if(control && l>0) break; tmp[n++]=v; if(v> (1ULL<<63)/3) break; v*=3; } }
  qsort(tmp,n,sizeof(u64),cmpu); NS=n;
  for(int i=0;i<n;i++){ S[i]=tmp[i]; u64 v=S[i]; int k=0,l=0; while(!(v&1)){v>>=1;k++;} while(v%3==0){v/=3;l++;} SK[i]=k; SL[i]=l; }
  // sieve primes 5..
  int c=0; for(int p=5;c<NP;p++){ int ok=1; for(int q=2;q*q<=p;q++) if(p%q==0){ok=0;break;} if(ok) P[c++]=p; }
  for(int j=0;j<NP;j++){ int p=P[j];
    for(int r=1;r<p;r++){ int inv=1; for(int x=1;x<p;x++) if((x*r)%p==1){inv=x;break;} TGT[j][r]=(uint16_t)((p-inv)%p); }
    for(int i=0;i<NS && i<64*NW;i++){ int t=(int)(S[i]%p); MASK[j][t][i>>6]|=1ULL<<(i&63); }
  }
  for(int i=0;i<NS && i<64*NW;i++) if(SK[i]==0) K0MASK[i>>6]|=1ULL<<(i&63);
  int pmax=P[NP-1];

  long long hist_rank[MAXS]={0}, hist_log2[70]={0}, cnt=0, nsurv=0;
  u64 rec_s=0, rec_rank=0; // records as m increases
  u64 best_m_s=0, best_s=0; int best_k=0,best_l=0, best_rank=0; u64 best_m_rank=0;
  double best_logn=0; u64 best_m_logn=0;
  clock_t t0=clock();
  for(u64 m=M0; m<=M1; m++){
    if(m%2==0 || m%3==0) continue;
    cnt++;
    u64 lim = (u64)(-2)/m; // s*m+1 <= 2^64-1
    int found=-1;
    int usesieve = (m > (u64)pmax);
    if(usesieve){
      u64 kill[NW]; for(int w=0;w<NW;w++) kill[w]=K0MASK[w];
      for(int j=0;j<NP;j++){ int r=(int)(m%P[j]); if(!r) continue; int t=TGT[j][r]; for(int w=0;w<NW;w++) kill[w]|=MASK[j][t][w]; }
      for(int w=0;w<NW && found<0;w++){ u64 live=~kill[w];
        while(live){ int b=__builtin_ctzll(live); live&=live-1; int i=w*64+b; if(i>=NS) break; if(S[i]>lim) {found=-2;break;}
          if(isprime64(S[i]*m+1)){found=i;break;} }
      }
    }
    if(found==-1){
      int start = usesieve ? 64*NW : 0;
      for(int i=start;i<NS;i++){ if(S[i]>lim) break; if(SK[i]==0 && !(m==1&&i==0)) continue;
        u64 nn=S[i]*m+1;
        if(usesieve){ int bad=0; for(int j=0;j<NP;j++) if(nn%P[j]==0){bad=1;break;} if(bad) continue; }
        if(isprime64(nn)){found=i;break;} }
    }
    if(found<0){ nsurv++; printf("SURVIVOR %llu (no prime with n<2^64%s)\n",(unsigned long long)m, control?", l=0":""); fflush(stdout); continue; }
    hist_rank[found]++; u64 s=S[found]; int lg=63-__builtin_clzll(s); hist_log2[lg]++;
    if(s>best_s){ best_s=s; best_m_s=m; best_k=SK[found]; best_l=SL[found]; }
    if(found>best_rank){ best_rank=found; best_m_rank=m; }
    double logn=log2((double)s)+log2((double)m);
    if(logn>best_logn){best_logn=logn;best_m_logn=m;}
    if(s>rec_s){ rec_s=s; printf("REC_S m=%llu k=%d l=%d s=%llu rank=%d log2n=%.2f\n",(unsigned long long)m,SK[found],SL[found],(unsigned long long)s,found,logn); fflush(stdout);}
    if((u64)found>rec_rank){ rec_rank=found; printf("REC_RANK m=%llu k=%d l=%d rank=%d\n",(unsigned long long)m,SK[found],SL[found],found); fflush(stdout);}
  }
  double el=(double)(clock()-t0)/CLOCKS_PER_SEC;
  printf("DONE M0=%llu M1=%llu count=%lld survivors=%lld MRcalls=%lld time=%.1fs\n",(unsigned long long)M0,(unsigned long long)M1,cnt,nsurv,nMR,el);
  printf("BEST_S m=%llu k=%d l=%d s=%llu\n",(unsigned long long)best_m_s,best_k,best_l,(unsigned long long)best_s);
  printf("BEST_RANK m=%llu rank=%d\n",(unsigned long long)best_m_rank,best_rank);
  printf("BEST_LOG2N m=%llu log2n=%.2f\n",(unsigned long long)best_m_logn,best_logn);
  printf("HIST_LOG2S"); for(int i=0;i<64;i++) if(hist_log2[i]) printf(" %d:%lld",i,hist_log2[i]); printf("\n");
  printf("HIST_RANK"); for(int i=0;i<NS;i++) if(hist_rank[i]) printf(" %d:%lld",i,hist_rank[i]); printf("\n");
  return 0;
}

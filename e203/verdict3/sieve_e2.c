// Independent sieve route: for every prime 5 <= p < N compute e_p = lcm(ord_p 2, ord_p 3) from scratch
// (factor p-1 by trial division, exact orders) and print "p e" for every p with e_p <= EMAX.
// usage: sieve_e2 N EMAX > out.txt      (p < 2^31 so products fit in unsigned 64 bit)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
static u64 pw(u64 b, u64 e, u64 m){ u64 r=1; b%=m; while(e){ if(e&1) r=r*b%m; b=b*b%m; e>>=1;} return r; }
static u64 gcd(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10), EMAX=strtoull(argv[2],0,10);
  u64 R=1; while(R*R<=N) R++;
  char *comp=calloc(N/2+1,1);  // odd numbers only: index i <-> 2i+1
  for(u64 i=3;i*i<N;i+=2) if(!comp[i/2]) for(u64 j=i*i;j<N;j+=2*i) comp[j/2]=1;
  u64 *sp=malloc(sizeof(u64)*(R+1)); int ns=0;
  for(u64 i=3;i<=R;i+=2) if(!comp[i/2]) sp[ns++]=i;     // odd primes <= sqrt(N)
  u64 cnt=0, hit=0;
  for(u64 p=5;p<N;p+=2){
    if(comp[p/2]) continue; cnt++;
    u64 n=p-1; u64 fac[16]; int nf=0; u64 t=n;
    while(t%2==0) t/=2; fac[nf++]=2;
    for(int i=0;i<ns && sp[i]*sp[i]<=t;i++) if(t%sp[i]==0){ fac[nf++]=sp[i]; while(t%sp[i]==0) t/=sp[i]; }
    if(t>1) fac[nf++]=t;
    u64 o[2]; u64 base[2]={2,3};
    for(int b=0;b<2;b++){
      u64 ord=n;
      for(int k=0;k<nf;k++){ while(ord%fac[k]==0 && pw(base[b],ord/fac[k],p)==1) ord/=fac[k]; }
      o[b]=ord;
    }
    u64 e=o[0]/gcd(o[0],o[1])*o[1];
    if(e<=EMAX){ printf("%llu %llu\n",(unsigned long long)p,(unsigned long long)e); hit++; }
  }
  fprintf(stderr,"primes scanned %llu (p>=5, p<%llu), with e_p<=%llu: %llu\n",(unsigned long long)cnt,(unsigned long long)N,(unsigned long long)EMAX,(unsigned long long)hit);
  return 0;
}

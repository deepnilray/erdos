// D_eprimes.c: for primes 5<=q<=Y output binary records {uint32 q, uint32 e_q, uint32 ord2, uint32 ord3, uint16 G, uint16 alpha, uint16 beta}
// e_q=|<2,3> mod q|=lcm(ord2,ord3); G=gcd(e_q,55440); alpha,beta = discrete logs of 2,3 in H_q/H_q^G ~ Z/G w.r.t. generator gamma=r^((q-1)/e) (r primitive root).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int nf; static u64 fp[64];
static void factor(u64 n,uint32_t*sp,int nsp){nf=0;for(int i=0;i<nsp&&(u64)sp[i]*sp[i]<=n;i++){u64 p=sp[i];if(n%p==0){fp[nf++]=p;while(n%p==0)n/=p;}}if(n>1)fp[nf++]=n;}
static u64 order(u64 a,u64 q){u64 o=q-1;for(int i=0;i<nf;i++){while(o%fp[i]==0&&pw(a,o/fp[i],q)==1)o/=fp[i];}return o;}
int main(int argc,char**argv){u64 Y=strtoull(argv[1],0,10);FILE*out=fopen(argv[2],"wb");
 char*c=calloc(Y+1,1);uint32_t*sp=malloc(sizeof(uint32_t)*200000);int nsp=0;
 for(u64 i=2;i*i<=Y;i++)if(!c[i])for(u64 j=i*i;j<=Y;j+=i)c[j]=1;
 for(u64 i=2;i*i<=Y&&nsp<200000;i++)if(!c[i])sp[nsp++]=i;
 const u64 E=55440; const int PP[5]={16,9,5,7,11}; const int PL[5]={2,3,5,7,11};
 for(u64 q=5;q<=Y;q++){if(c[q])continue;
  factor(q-1,sp,nsp);u64 o2=order(2,q),o3=order(3,q);u64 e=o2/gcdu(o2,o3)*o3;
  u64 G=gcdu(e,E); u64 r=2; for(;;r++){int ok=1;for(int i=0;i<nf;i++)if(pw(r,(q-1)/fp[i],q)==1){ok=0;break;}if(ok)break;}
  u64 gam=pw(r,(q-1)/e,q); u64 al=0,be=0,mod=1;
  for(int k=0;k<5;k++){u64 L=1;int pl=PL[k];while(G%(L*pl)==0)L*=pl;if(L==1)continue;
    u64 z=pw(gam,e/L,q),x2=pw(2,e/L,q),x3=pw(3,e/L,q),t2=999,t3=999,cur=1;
    for(u64 t=0;t<L;t++){if(cur==x2)t2=t;if(cur==x3)t3=t;cur=(u128)cur*z%q;}
    if(t2==999||t3==999){fprintf(stderr,"dlog fail q=%llu\n",q);return 1;}
    // CRT combine (al mod mod) with (t2 mod L)
    u64 a=al; while(a%L!=t2)a+=mod; u64 b=be; while(b%L!=t3)b+=mod; al=a;be=b;mod*=L;}
  uint32_t rec[4]={(uint32_t)q,(uint32_t)e,(uint32_t)o2,(uint32_t)o3};uint16_t r2[3]={(uint16_t)G,(uint16_t)al,(uint16_t)be};
  fwrite(rec,4,4,out);fwrite(r2,2,3,out);}
 fclose(out);return 0;}

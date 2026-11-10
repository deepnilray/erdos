// a5_eprimes_check.c (agent 5, run5): independent check of verdict3/D_data/ep_1e8.bin (written by D_eprimes.c).
// Independent method: smallest-prime-factor sieve (not trial division) to factor q-1; e_q certified directly as
// |<2,3> mod q| by: 2^e = 3^e = 1 and for every prime r | e NOT(2^{e/r} = 1 and 3^{e/r} = 1)  (cyclic group => this is the order).
// D's (G, alpha, beta) are checked WITHOUT using any generator: G = gcd(e,55440); gcd(alpha,beta,G) = 1; and the index-G lattice
// K = {(i,j): i*alpha + j*beta = 0 mod G}, basis (g1, j0), (0, G/g1), must lie in the kernel of Z^2 -> H_q/H_q^G, i.e.
// (2^i 3^j)^(e/G) = 1 mod q for both basis vectors. Index-G sublattice of an index-G lattice => equal, so the map is certified.
// Also checks the record set = all primes 5 <= q <= Y (count and order).
// Planted control: argv[3] = "plant" flips alpha -> alpha+1 for every 1000th record with G > 1 and must report failures.
// Output: own table q, e (uint32 pairs) to argv[2].
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static long long egcd_inv(long long b,long long m){ // inverse of b mod m (gcd(b,m)=1), extended Euclid
  long long A=((b%m)+m)%m,B=m,s0=1,s1=0; while(B){long long q=A/B,t=A-q*B;A=B;B=t;t=s0-q*s1;s0=s1;s1=t;}
  long long r=s0%m; if(r<0)r+=m; return r;}
int main(int argc,char**argv){
  u64 Y=100000000ULL; const char*fin=argv[1]; FILE*fo=fopen(argv[2],"wb"); int plant=(argc>3&&!strcmp(argv[3],"plant"));
  uint32_t*spf=calloc(Y+1,4); if(!spf){fprintf(stderr,"oom\n");return 1;}
  for(u64 i=2;i<=Y;i++) if(!spf[i]){ for(u64 j=i;j<=Y;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
  FILE*f=fopen(fin,"rb"); unsigned char rec[22]; u64 nrec=0,bad_e=0,bad_G=0,bad_lat=0,bad_gcd=0,bad_seq=0,nG1=0; u64 qexp=5;
  while(fread(rec,1,22,f)==22){
    uint32_t q,e,o2,o3; uint16_t G,al,be; memcpy(&q,rec,4);memcpy(&e,rec+4,4);memcpy(&o2,rec+8,4);memcpy(&o3,rec+12,4);
    memcpy(&G,rec+16,2);memcpy(&al,rec+18,2);memcpy(&be,rec+20,2);
    while(qexp<=Y && spf[qexp]!=qexp) qexp++;
    if(q!=qexp){bad_seq++; if(bad_seq<5)fprintf(stderr,"seq: got %u expected %llu\n",q,qexp);} qexp=q+1;
    // factor q-1 with spf
    u64 n=q-1, fp[40]; int nf=0; while(n>1){u64 p=spf[n]; fp[nf++]=p; while(n%p==0)n/=p;}
    // own order of 2 and 3
    u64 O[2]; u64 base[2]={2,3};
    for(int t=0;t<2;t++){u64 o=q-1; for(int i=0;i<nf;i++) while(o%fp[i]==0 && pw(base[t],o/fp[i],q)==1) o/=fp[i]; O[t]=o;}
    u64 ee=O[0]/gcdu(O[0],O[1])*O[1];
    // certify ee as group order directly
    int ok=(pw(2,ee,q)==1&&pw(3,ee,q)==1);
    for(int i=0;i<nf&&ok;i++) if(ee%fp[i]==0 && pw(2,ee/fp[i],q)==1 && pw(3,ee/fp[i],q)==1) ok=0;
    if(!ok || ee!=e || O[0]!=o2 || O[1]!=o3){bad_e++; if(bad_e<5)fprintf(stderr,"e mismatch q=%u D:%u own:%llu\n",q,e,ee);}
    u64 GG=gcdu(ee,55440); if(GG!=G){bad_G++;}
    u64 a=al, b=be; if(plant && G>1 && (nrec%1000)==0) a=(a+1)%G;
    if(G>1){ nG1++;
      if(gcdu(gcdu(a%G,b%G),G)!=1){bad_gcd++;}
      else { u64 g1=gcdu(b%G,G); // basis (g1, j0), (0, G/g1)
        u64 Gq=G/g1; long long j0=0;
        if(Gq>1){ long long bb=(long long)((b/g1)%Gq); long long inv=egcd_inv(bb,(long long)Gq); j0=(long long)((Gq-(a%Gq))%Gq)*inv%(long long)Gq; }
        u64 ex=ee/G;
        u64 v1=(u128)pw(2,g1,q)*pw(3,(u64)j0,q)%q; v1=pw(v1,ex,q);
        u64 v2=pw(pw(3,Gq,q),ex,q);
        // sanity: (g1,j0) must satisfy g1*a + j0*b = 0 mod G
        if(((u128)g1*a+(u128)j0*b)%G!=0) {bad_lat++; if(bad_lat<5)fprintf(stderr,"basis algebra fail q=%u\n",q);}
        else if(v1!=1||v2!=1){bad_lat++; if(bad_lat<5)fprintf(stderr,"lattice fail q=%u G=%u\n",q,G);}
      }
    }
    uint32_t outr[2]={q,(uint32_t)ee}; fwrite(outr,4,2,fo); nrec++;
  }
  while(qexp<=Y && spf[qexp]!=qexp) qexp++;
  printf("records=%llu  (G>1: %llu)  e_mismatch=%llu  G_mismatch=%llu  gcd(a,b,G)!=1: %llu  lattice_fail=%llu  sequence_errors=%llu  missing_after_last=%d\n",
    nrec,nG1,bad_e,bad_G,bad_gcd,bad_lat,bad_seq,(qexp<=Y));
  fclose(f);fclose(fo);return 0;}

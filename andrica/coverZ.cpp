// Certified admissible table for the ZETA case F = Z*B*C (c = 1/2), Z a zeta sum (x^{1/4} <= Z <= T_1 z_2).
// Variables (log_x): p[0]=z, p[1]=c, b=1-z-c; p[2]=vZ, p[3]=vB, p[4]=vC (|Y(it)| ~ x^{v_Y} on T_sigma).
// Domain: z in [1/4,1/2]; vY in [-1, 0.8 y] (J. Lemma 5.8); vZ <= z/2 + 1/12 (van der Corput, see notes).
// Target: log int_{T_sigma} |Z B C M| <= 1 + r - DEL.
// Routes: generalized Hoelder. Each factor gets a mode:
//   Z : pointwise (adds vZ) | L^p over [T1,2T1], weight 1/p, adds J_p/p   (J_2=z+1/2, J_4=1/2+2z [J. Lemma 5.8],
//        J_12=1+6z [HB 12th moment via Perron], J_6, J_8 by Hoelder interpolation) | absorbed into M-pairing
//   B,C: pointwise | L^{2k} (k=1,2,3), weight 1/2k, adds (max(1/2,ky)+ky)/2k  (MVT for Y^k) | absorbed into M-pairing
//   M : pointwise (adds r) | L^2 paired with X (weight 1/2, adds max(2x+2r, x+r+1/2)/2, HB MVT)
//       | L^4 paired with X (weight 1/4, adds (2r+max(4x+2r,2x+r+1/2))/4 : |M|^4<=R^2|M|^2, HB MVT for X^2 M)
//   remaining weight a=1-W multiplies tau.  Route: a*tau + L_k <= 1+r-DEL for all max-branches k.
// Bounds on tau: 1/2; Huxley & Guth-Maynard on Y^w (Y in {Z,B,C}, w<=WMAX); Z moments: tau<=1/2+2z-4vZ, tau<=1+6z-12vZ.
#include <bits/stdc++.h>
using namespace std;
static double R=0.058, TT=0.5, DEL=1e-6; static int WMAX=30, USEZ12=1, USEZHUX=1, USEZPW=1, ZHOLD=1;
struct Lin{ double k[5]; double c0; };
static Lin zero(){ Lin f; memset(&f,0,sizeof f); return f; }
static Lin cst(double c){ Lin f=zero(); f.c0=c; return f; }
static Lin lenL(int i){ Lin f=zero(); if(i==0) f.k[0]=1; else if(i==2) f.k[1]=1; else { f.c0=1; f.k[0]=-1; f.k[1]=-1; } return f; } // 0=Z,1=B,2=C
static Lin vL(int i){ Lin f=zero(); f.k[2+i]=1; return f; }
static Lin comb(double s1, Lin x, double s2, Lin y, double c){ Lin f=zero(); for(int t=0;t<5;t++) f.k[t]=s1*x.k[t]+s2*y.k[t]; f.c0=s1*x.c0+s2*y.c0+c; return f; }
static Lin add(Lin x, Lin y){ return comb(1,x,1,y,0);} static Lin sc(double s, Lin x){ return comb(s,x,0,zero(),0);}
static Lin sub(Lin x, Lin y){ return comb(1,x,-1,y,0); }
struct Box{ double lo[5], hi[5]; };
static double ub(const Lin& f,const Box& B){ double s=f.c0; for(int t=0;t<5;t++) s+= f.k[t]>0? f.k[t]*B.hi[t]: f.k[t]*B.lo[t]; return s; }
static double lb(const Lin& f,const Box& B){ double s=f.c0; for(int t=0;t<5;t++) s+= f.k[t]>0? f.k[t]*B.lo[t]: f.k[t]*B.hi[t]; return s; }
static double at(const Lin& f,const double* p){ double s=f.c0; for(int t=0;t<5;t++) s+=f.k[t]*p[t]; return s; }
struct Term{ vector<Lin> mins; }; struct Bound{ vector<Term> terms; string name; };
struct Route{ bool free; vector<Lin> forms; string name; }; // free: forms are L_k (need L_k<=1+r-DEL); else tau <= min forms
static vector<Bound> BOUNDS; static vector<Route> ROUTES; static double MAXK[5];
// a "sum of maxes" accumulator: list of alternative linear forms (all must satisfy)
typedef vector<Lin> Alt;
static Alt addMax(const Alt& A, vector<Lin> opts){ Alt out; for(auto& a:A) for(auto& o:opts) out.push_back(add(a,o)); return out; }
static void build(){
  BOUNDS.clear(); ROUTES.clear();
  { Bound b; Term t; t.mins.push_back(cst(TT)); b.terms.push_back(t); b.name="triv"; BOUNDS.push_back(b); }
  for(int i=0;i<3;i++){ if(i==0 && !USEZHUX) continue; for(int w=1;w<=WMAX;w++){
    Lin l=lenL(i), v=vL(i);
    Lin h1=comb(2*w,l,-2*w,v,0), h2=comb(w,l,-2*w,v,TT), h3=comb(4*w,l,-6*w,v,TT);
    { Bound b; Term t1; t1.mins.push_back(h1); Term t2; t2.mins={h2,h3}; b.terms={t1,t2}; b.name="Hux"+to_string(i)+"^"+to_string(w); BOUNDS.push_back(b); }
    { Bound b; Term t1,t2,t3; t1.mins.push_back(h1); t2.mins.push_back(comb(3.6*w,l,-4*w,v,0)); t3.mins.push_back(comb(2.4*w,l,-4*w,v,TT)); b.terms={t1,t2,t3}; b.name="GM"+to_string(i)+"^"+to_string(w); BOUNDS.push_back(b); }
  } }
  { Bound b; Term t; t.mins.push_back(comb(2,lenL(0),-4,vL(0),0.5)); b.terms={t}; b.name="Z4"; BOUNDS.push_back(b); }
  if(USEZ12){ Bound b; Term t; t.mins.push_back(comb(6,lenL(0),-12,vL(0),1.0)); b.terms={t}; b.name="Z12"; BOUNDS.push_back(b); }
  // ---- routes
  Lin z=lenL(0); Lin J2=comb(1,z,0,zero(),0.5), J4=comb(2,z,0,zero(),0.5), J12=comb(6,z,0,zero(),1.0);
  vector<pair<double,Lin>> Zmodes; // (weight, contribution) ; weight<0 => pointwise
  Zmodes.push_back({0,vL(0)});
  if(ZHOLD){ Zmodes.push_back({0.5, sc(0.5,J2)}); Zmodes.push_back({0.25, sc(0.25,J4)});
    if(USEZ12){ Lin J6=comb(0.75,J4,0.25,J12,0), J8=comb(0.5,J4,0.5,J12,0);
      Zmodes.push_back({1.0/6, sc(1.0/6,J6)}); Zmodes.push_back({1.0/8, sc(1.0/8,J8)}); Zmodes.push_back({1.0/12, sc(1.0/12,J12)}); } }
  for(int Xm=0; Xm<8; Xm++) for(int Mmode=0; Mmode<3; Mmode++){ // Xm: subset of {Z,B,C} paired with M (Mmode 1,2); Mmode0 => M pointwise, Xm must be 0
    if(Mmode==0 && Xm) continue; if(Xm==7) continue;
    Lin x=zero(); for(int i=0;i<3;i++) if(Xm>>i&1) x=add(x,lenL(i));
    Alt base{cst(0)}; double W=0;
    if(Mmode==0) base=addMax(base,{cst(R)});
    if(Mmode==1){ W+=0.5; base=addMax(base,{comb(1,x,0,zero(),R), comb(0.5,x,0,zero(),0.5*R+0.25)}); }
    if(Mmode==2){ W+=0.25; base=addMax(base,{comb(1,x,0,zero(),R), comb(0.5,x,0,zero(),0.25*R+0.5*R+0.125)}); }
    // Z mode
    vector<pair<double,Lin>> zm; if(Xm&1) zm.push_back({0,zero()}); else zm=Zmodes;
    for(auto& zz:zm){
      // B, C modes: 0 pw, k=1..3 L^{2k}
      for(int mb=0; mb<4; mb++) for(int mc=0; mc<4; mc++){
        if((Xm&2) && mb) continue; if((Xm&4) && mc) continue;
        double W2=W+zz.first; Alt A=addMax(base,{zz.second});
        int md[3]={0,mb,mc}; bool bad=false;
        for(int i=1;i<3;i++){ if(Xm>>i&1) continue; Lin y=lenL(i);
          if(md[i]==0) A=addMax(A,{vL(i)});
          else { int k=md[i]; W2+=1.0/(2*k); A=addMax(A,{comb(1.0,y,0,zero(),0.5/(2*k)), comb(1.0,y,0,zero(),0)}); /* (max(1/2,ky)+ky)/2k = max(1/(4k)+y/2, y) */
                 A.pop_back(); }
        }
        (void)bad;
        if(W2>1+1e-12) continue;
        Route rt; double a=1-W2;
        // recompute properly the L^{2k} contributions (above shortcut removed): rebuild A cleanly
        Alt B2=addMax(base,{zz.second});
        for(int i=1;i<3;i++){ if(Xm>>i&1) continue; Lin y=lenL(i);
          if(md[i]==0) B2=addMax(B2,{vL(i)});
          else { int k=md[i]; B2=addMax(B2,{comb(0.5,y,0,zero(),0.25/k), comb(1.0,y,0,zero(),0)}); } }
        char nm[64]; snprintf(nm,64,"X%d M%d Zw%.3f B%d C%d",Xm,Mmode,zz.first,mb,mc); rt.name=nm;
        if(a<1e-12){ rt.free=true; rt.forms=B2; }
        else { rt.free=false; for(auto& L:B2) rt.forms.push_back(comb(-1.0/a,L,0,zero(),(1+R)/a)); }
        ROUTES.push_back(rt);
      }
    }
  }
  for(int t=0;t<5;t++) MAXK[t]=1;
  for(auto& b:BOUNDS) for(auto& tm:b.terms) for(auto& f:tm.mins) for(int t=0;t<5;t++) MAXK[t]=max(MAXK[t],fabs(f.k[t]));
}
static Lin vmax(int i){ // upper limit of v_i as function: 0.8*len (and for Z also z/2+1/12)
  return comb(0.8,lenL(i),0,zero(),0); }
static bool outDom(const Box& B){
  if(ub(lenL(1),B) < 0) return true;
  for(int i=0;i<3;i++) if(lb(sub(vL(i),vmax(i)),B) > 0) return true;
  if(USEZPW && lb(sub(vL(0),comb(0.5,lenL(0),0,zero(),1.0/12)),B) > 0) return true;
  return false; }
static bool inDomPt(const double* p){ if(at(lenL(1),p)<0) return false; for(int i=0;i<3;i++) if(at(vL(i),p)>at(vmax(i),p)) return false;
  if(USEZPW && p[2] > 0.5*p[0]+1.0/12) return false; return true; }
static int LASTR=-1;
static bool pairOK(const Route& r,const Bound& b,const Box& B){
  for(auto& tm:b.terms){ for(auto& q:r.forms){ double best=1e18; for(auto& p:tm.mins) best=min(best, ub(sub(p,q),B)); if(best>-DEL) return false; } } return true; }
static int TOPR=8, TOPB=12;
static bool certBox(const Box& B){
  static vector<pair<double,int>> rv, bv; rv.clear(); bv.clear();
  for(int ri=0; ri<(int)ROUTES.size(); ri++){ auto& r=ROUTES[ri];
    if(r.free){ bool ok=true; for(auto& L:r.forms) if(ub(L,B) > 1+R-DEL){ok=false;break;} if(ok) return true; continue; }
    double rl=1e18; for(auto& q:r.forms) rl=min(rl,lb(q,B)); rv.push_back({-rl,ri}); }
  for(int bi=0; bi<(int)BOUNDS.size(); bi++){ auto& b=BOUNDS[bi]; double M=-1e18; for(auto& tm:b.terms){ double m=1e18; for(auto& p:tm.mins) m=min(m,ub(p,B)); M=max(M,m);} bv.push_back({M,bi}); }
  sort(rv.begin(),rv.end()); sort(bv.begin(),bv.end());
  if(bv[0].first <= -rv[0].first - DEL) return true;
  int nr=min((int)rv.size(),TOPR), nb=min((int)bv.size(),TOPB);
  for(int a=0;a<nr;a++) for(int c=0;c<nb;c++) if(pairOK(ROUTES[rv[a].second],BOUNDS[bv[c].second],B)) return true;
  return false; }
static bool certPoint(const double* x){
  double bestR=-1e18; for(auto& r:ROUTES){ if(r.free){ bool ok=true; for(auto& L:r.forms) if(at(L,x)>1+R-DEL) ok=false; if(ok) return true; continue; }
    double m=1e18; for(auto& q:r.forms) m=min(m,at(q,x)); bestR=max(bestR,m); }
  for(auto& b:BOUNDS){ double M=-1e18; for(auto& tm:b.terms){ double m=1e18; for(auto& p:tm.mins) m=min(m,at(p,x)); M=max(M,m);} if(M<=bestR-DEL) return true; }
  return false; }
static long long NODES, BUDGET=8000;
static int cover(Box B){
  if(++NODES>BUDGET) return -1;
  if(outDom(B)) return 1;
  if(certBox(B)) return 1;
  double mid[5]; for(int t=0;t<5;t++) mid[t]=0.5*(B.lo[t]+B.hi[t]);
  if(inDomPt(mid) && !certPoint(mid)){ if(getenv("DBG")) fprintf(stderr,"FAIL z=%g c=%g vZ=%g vB=%g vC=%g\n",mid[0],mid[1],mid[2],mid[3],mid[4]); return 0; }
  int sd=-1; double sw=-1; for(int t=0;t<5;t++){ double w=(B.hi[t]-B.lo[t])*MAXK[t]; if(w>sw){sw=w;sd=t;} }
  if(sw<1e-9) return -1;
  Box L=B,H=B; L.hi[sd]=mid[sd]; H.lo[sd]=mid[sd];
  int r1=cover(L); if(r1!=1) return r1; return cover(H); }
int main(int argc,char**argv){
  int N=atoi(argv[1]); R=atof(argv[2]); int i0=atoi(argv[3]), i1=atoi(argv[4]);
  if(getenv("BUDGET")) BUDGET=atoll(getenv("BUDGET")); if(getenv("WMAX")) WMAX=atoi(getenv("WMAX"));
  if(getenv("NOZ12")) USEZ12=0; if(getenv("NOZHUX")) USEZHUX=0; if(getenv("NOZPW")) USEZPW=0; if(getenv("NOZHOLD")) ZHOLD=0;
  build(); fprintf(stderr,"bounds=%zu routes=%zu\n",BOUNDS.size(),ROUTES.size());
  if(getenv("PT")){ double p[5]; sscanf(getenv("PT"),"%lf,%lf,%lf,%lf,%lf",p,p+1,p+2,p+3,p+4); printf("pt cert=%d dom=%d\n",certPoint(p),inDomPt(p)); return 0; }
  // rows: z index i in [i0,i1) (z=i/N), columns c index j in [0,N)
  for(int i=i0;i<i1;i++){ string row;
    int jj0=getenv("J0")?atoi(getenv("J0")):0, jj1=getenv("J1")?atoi(getenv("J1")):N; for(int j=0;j<N;j++){ if(j<jj0||j>=jj1){ row+='-'; continue; }
      double z0=(double)i/N,z1=(double)(i+1)/N,c0=(double)j/N,c1=(double)(j+1)/N;
      if(z0<0.25-1e-12 || z1>0.5+1e-12 || z0+c0>=1){ row+='-'; continue; }
      Box B; B.lo[0]=z0;B.hi[0]=z1;B.lo[1]=c0;B.hi[1]=c1; double lmax[3]={z1,1-z0-c0,c1};
      for(int k=0;k<3;k++){ B.lo[2+k]=-1; B.hi[2+k]=0.8*max(0.0,lmax[k]); }
      bool bad=false;
      for(int ia=0;ia<3&&!bad;ia++) for(int ic=0;ic<3&&!bad;ic++){ double p[5]; p[0]=z0+(z1-z0)*ia/2.0; p[1]=c0+(c1-c0)*ic/2.0; double l[3]={p[0],1-p[0]-p[1],p[1]}; if(l[1]<0) continue;
        double vzmax=min(0.8*l[0], USEZPW? 0.5*l[0]+1.0/12 : 1.0);
        for(int s0=0;s0<=8&&!bad;s0++) for(int s1=0;s1<=8&&!bad;s1++) for(int s2=0;s2<=8&&!bad;s2++){ p[2]=vzmax*s0/8.0; p[3]=0.1*s1*l[1]; p[4]=0.1*s2*l[2]; if(!certPoint(p)){ bad=true; if(getenv("DBG")) fprintf(stderr,"SFAIL %g %g %g %g %g\n",p[0],p[1],p[2],p[3],p[4]); } } }
      int r= bad?0:(NODES=0,cover(B)); row+=(r==1?'1':(r==0?'0':'?')); }
    printf("%d %s\n",i,row.c_str()); fflush(stdout); }
}

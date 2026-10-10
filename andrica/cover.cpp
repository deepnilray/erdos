// Rigorous coverage table for Jarviniemi's Claim 5.1 (c = 1/2), no zeta factors.
// Variables: a = log_x A, c = log_x C, b = 1 - a - c, v_i = l_i * sigma_i  (|P_i(it)| ~ x^{v_i}).
// Domain: v_i in [-1, 0.8 l_i]  (|P| >= x^{-1};  sigma <= 4/5 by Lemma 5.8).
// Certificate at a point: some route r and some bound j with bound_j <= RHS_r - DEL.
//  routes:  (5.7)  |T| <= sum_i (l_i - v_i)
//           (5.8)X |T| <= min( sum_{i!=X} (2 l_i - 2 v_i),  1/2 + R + sum_{i!=X} (l_i - 2 v_i) )
//  bounds:  trivial t = 1/2;  for P = P_i^w (length L = w l_i, value exponent w v_i):
//           Huxley:  max( w(2l-2v), t + min( w(l-2v), w(4l-6v) ) )
//           GM    :  max( w(2l-2v), w(3.6l-4v), t + w(2.4l-4v) )
// Everything is linear in (a, c, vA, vB, vC), so interval bounds of linear differences are exact on boxes.
#include <bits/stdc++.h>
using namespace std;
static double R = 0.065, TT = 0.5, DEL = 1e-6; static int USE_GM = 1, WMAX = 30;
struct Lin { double k[5]; double c0; };
static Lin zero(){ Lin f; memset(&f,0,sizeof f); return f; }
static Lin lenL(int i){ Lin f=zero(); if(i==0) f.k[0]=1; else if(i==2) f.k[1]=1; else { f.c0=1; f.k[0]=-1; f.k[1]=-1; } return f; }
static Lin vL(int i){ Lin f=zero(); f.k[2+i]=1; return f; }
static Lin comb(double s1, Lin x, double s2, Lin y, double c){ Lin f=zero(); for(int t=0;t<5;t++) f.k[t]=s1*x.k[t]+s2*y.k[t]; f.c0=s1*x.c0+s2*y.c0+c; return f; }
static Lin sub(Lin x, Lin y){ return comb(1,x,-1,y,0); }
struct Box { double lo[5], hi[5]; };
static double ub(const Lin& f, const Box& B){ double s=f.c0; for(int t=0;t<5;t++) s += f.k[t]>0 ? f.k[t]*B.hi[t] : f.k[t]*B.lo[t]; return s; }
static double lb(const Lin& f, const Box& B){ double s=f.c0; for(int t=0;t<5;t++) s += f.k[t]>0 ? f.k[t]*B.lo[t] : f.k[t]*B.hi[t]; return s; }
static double at(const Lin& f, const double* p){ double s=f.c0; for(int t=0;t<5;t++) s+=f.k[t]*p[t]; return s; }
// bound = max over terms, term = min over linear forms
struct Term { vector<Lin> mins; };
struct Bound { vector<Term> terms; };
struct Route { vector<Lin> mins; };   // RHS = min over linear forms
static vector<Bound> BOUNDS; static vector<Route> ROUTES; static double MAXK[5];
static void build(){
  BOUNDS.clear(); ROUTES.clear();
  { Bound b; Term t; t.mins.push_back(comb(0,zero(),0,zero(),TT)); b.terms.push_back(t); BOUNDS.push_back(b); }
  for(int i=0;i<3;i++) for(int w=1; w<=WMAX; w++){
    Lin l=lenL(i), v=vL(i);
    Lin h1=comb(2*w,l,-2*w,v,0), h2=comb(w,l,-2*w,v,TT), h3=comb(4*w,l,-6*w,v,TT);
    { Bound b; Term t1; t1.mins.push_back(h1); Term t2; t2.mins.push_back(h2); t2.mins.push_back(h3);
      b.terms.push_back(t1); b.terms.push_back(t2); BOUNDS.push_back(b); }
    if(USE_GM){ Bound b; Term t1,t2,t3; t1.mins.push_back(h1); t2.mins.push_back(comb(3.6*w,l,-4*w,v,0));
      t3.mins.push_back(comb(2.4*w,l,-4*w,v,TT)); b.terms={t1,t2,t3}; BOUNDS.push_back(b); }
  }
  { Route r; Lin s=zero(); for(int i=0;i<3;i++) s=comb(1,s,1,sub(lenL(i),vL(i)),0); r.mins.push_back(s); ROUTES.push_back(r); }
  for(int X=0;X<3;X++){ Route r; Lin s1=zero(), s2=comb(0,zero(),0,zero(),0.5+R);
    for(int i=0;i<3;i++) if(i!=X){ s1=comb(1,s1,1,comb(2,lenL(i),-2,vL(i),0),0); s2=comb(1,s2,1,comb(1,lenL(i),-2,vL(i),0),0); }
    r.mins.push_back(s1); r.mins.push_back(s2); ROUTES.push_back(r); }
  for(int t=0;t<5;t++) MAXK[t]=1;
  for(auto& b:BOUNDS) for(auto& tm:b.terms) for(auto& f:tm.mins) for(int t=0;t<5;t++) MAXK[t]=max(MAXK[t],fabs(f.k[t]));
}
// certificate over a whole box: exists bound j, route r with for every term m of j and every rhs form q of r:
//   min_{p in m} UB(p - q) <= -DEL
static bool certBox(const Box& B){
  for(auto& r:ROUTES) for(auto& b:BOUNDS){
    if(b.terms.size()>1 && lb(b.terms[0].mins[0],B) > TT) continue; // dominated by trivial bound
    bool ok=true;
    for(auto& tm:b.terms){ for(auto& q:r.mins){ double best=1e18; for(auto& p:tm.mins) best=min(best, ub(sub(p,q),B)); if(best>-DEL){ok=false;break;} } if(!ok) break; }
    if(ok) return true;
  }
  return false;
}
static bool certPoint(const double* x){ // exact, no margin
  double bestR=-1e18; for(auto& r:ROUTES){ double m=1e18; for(auto& q:r.mins) m=min(m,at(q,x)); bestR=max(bestR,m); }
  for(auto& b:BOUNDS){ double M=-1e18; for(auto& tm:b.terms){ double m=1e18; for(auto& p:tm.mins) m=min(m,at(p,x)); M=max(M,m);} if(M<=bestR-DEL) return true; }
  return false;
}
static long long NODES;
// returns 1 covered, 0 definitely uncovered point found, -1 undecided (budget)
static int cover(Box B, int depth){
  if(++NODES > 8000) return -1;
  Lin bl=lenL(1); if(ub(bl,B) < 0) return 1;                       // b < 0 everywhere: infeasible
  for(int i=0;i<3;i++){ if(lb(sub(vL(i),comb(0.8,lenL(i),0,zero(),0)),B) > 0) return 1; } // sigma > 0.8 everywhere
  if(certBox(B)) return 1;
  double mid[5]; for(int t=0;t<5;t++) mid[t]=0.5*(B.lo[t]+B.hi[t]);
  bool inDom = at(bl,mid) >= 0; for(int i=0;i<3;i++) if(at(vL(i),mid) > 0.8*at(lenL(i),mid)) inDom=false;
  if(inDom && !certPoint(mid)){ if(getenv("DBG")) fprintf(stderr,"FAIL a=%g c=%g vA=%g vB=%g vC=%g  sig=(%g,%g,%g)\n",mid[0],mid[1],mid[2],mid[3],mid[4],mid[2]/mid[0],mid[3]/(1-mid[0]-mid[1]),mid[4]/mid[1]); return 0;}
  int sd=-1; double sw=-1; for(int t=0;t<5;t++){ double w=(B.hi[t]-B.lo[t])*MAXK[t]; if(w>sw){sw=w;sd=t;} }
  if(sw < 1e-9) return -1;
  Box L=B, H=B; L.hi[sd]=mid[sd]; H.lo[sd]=mid[sd];
  int r1=cover(L,depth+1); if(r1!=1) return r1;
  return cover(H,depth+1);
}
int main(int argc, char** argv){
  int N = atoi(argv[1]); R = atof(argv[2]); USE_GM = atoi(argv[3]);
  int i0 = argc>4 ? atoi(argv[4]) : 0, i1 = argc>5 ? atoi(argv[5]) : N;
  build();
  if(argc>6){ // single point query: a c
    double a=atof(argv[7]), c=atof(argv[8]); Box B; B.lo[0]=B.hi[0]=a; B.lo[1]=B.hi[1]=c;
    for(int i=0;i<3;i++){ double l=at(lenL(i),B.lo); B.lo[2+i]=-1; B.hi[2+i]=0.8*l; }
    NODES=0; int r=cover(B,0); printf("point (%g,%g,%g): %d nodes=%lld\n",a,1-a-c,c,r,NODES); return 0; }
  for(int i=i0;i<i1;i++){
    string row;
    for(int j=0;j<N;j++){
      double a0=(double)i/N,a1=(double)(i+1)/N,c0=(double)j/N,c1=(double)(j+1)/N;
      if(a0+c0>=1){ row+='1'; continue; }
      Box B; B.lo[0]=a0; B.hi[0]=a1; B.lo[1]=c0; B.hi[1]=c1;
      double lmax[3]={a1, 1-a0-c0, c1};
      for(int k=0;k<3;k++){ B.lo[2+k]=-1; B.hi[2+k]=0.8*max(0.0,lmax[k]); }
      bool bad=false;
      for(int ia=0; ia<3 && !bad; ia++) for(int ic=0; ic<3 && !bad; ic++){
        double p[5]; p[0]=a0+(a1-a0)*ia/2.0; p[1]=c0+(c1-c0)*ic/2.0; double l[3]={p[0],1-p[0]-p[1],p[1]};
        if(l[1]<0) continue;
        for(int s0=0;s0<=8&&!bad;s0++) for(int s1=0;s1<=8&&!bad;s1++) for(int s2=0;s2<=8&&!bad;s2++){
          p[2]=0.1*s0*l[0]; p[3]=0.1*s1*l[1]; p[4]=0.1*s2*l[2]; if(!certPoint(p)) bad=true; }
      }
      int r = bad ? 0 : (NODES=0, cover(B,0));
      row += (r==1?'1':(r==0?'0':'?'));
    }
    printf("%d %s\n", i, row.c_str()); fflush(stdout);
  }
}

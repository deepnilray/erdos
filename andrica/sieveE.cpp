/*
Author: Olli Järviniemi
Paper: "On large differences between consecutive prime numbers"
Code for bounding the loss, case c = 0.5.

Takes approximately 15 minutes.
Remember to use the -O2 optimization flag!
*/

//Libraries
#include <iostream>
#include <iomanip>
#include <vector>
#include <math.h>
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

//Macros for convenience
typedef double d;
typedef pair<d, d> pd;
#define F first
#define S second

//Important constants
d R = 0.07;
int USE_TAB = 0, DIRECT = 0; int TN=0; std::vector<std::string> TAB;
bool tabCell(int i,int j){ if(i<0) i=0; if(j<0) j=0; if(i>=TN||j>=TN) return true; if(i+j>=TN) return true; return TAB[i][j]=='1'; }
bool tabBox(double a0,double a1,double c0,double c1){ int i0=(int)floor((a0-1e-6)*TN), i1=(int)floor((a1+1e-6)*TN), j0=(int)floor((c0-1e-6)*TN), j1=(int)floor((c1+1e-6)*TN);
  for(int i=i0;i<=i1;i++) for(int j=j0;j<=j1;j++) if(!tabCell(i,j)) return false; return true; }
const d EPS = 1e-9;

/*
Evaluate the Buchstab function at u.
Returns an upper bound.
*/

d buch(d u) {
	if(u < 1) return 0;
	if(u <= 2) {
		return 1.0/u;
	}
	if(u <= 3) {
		return (1 + log(u-1))/u;
	}
	return 0.565;
}

/*
Return an upper bound for sup_{a <= u <= b} buch(u).
*/
d getUpperBuch(d a, d b) {
	if(b < 1 || a > b) return 0;

	d ans = 0;
	if(a <= 2) {
		//Buchstab is 1/u in [1, 2], thus decreasing
		ans = max(ans, buch(max(a, 1.0)));
	}
	if(a <= 2.75 && b >= 2) {
		//Buchstab is (1 + log(u-1))/u in [2, 3], and
		//hence increasing in [2, 2.75]
		ans = max(ans, buch(min(b, 2.75)));
	}
	if(b >= 2.75) {
		//Buchstab is bounded by 0.568 in [2.75, \infty)
		ans = max(ans, 0.568);
	}
	return ans;
}

/*
Return true if (P, Q) is in the region B_1.
*/

bool inB1(d P, d Q) {
	if(P <= Q + EPS) return false;

	if(Q         <= 0.25  + EPS) return false;
	if(P + Q     >= 0.5+R - EPS) return false;
	if(P + Q     <= 1-8*R + EPS) return false;
	if(P + 0.7*Q <= 0.5-R + EPS) return false;
	if(P - 3*Q   <= -8*R + EPS) return false;

	return true;
}
/*
Return true if (P, Q) is in the region B_2
*/
bool inB2(d P, d Q) {
	return inB1(1-P-Q, Q);
}

/*
Return true if the the set of (P, Q) defined by v lies completely
in either B_1 or in B_2.

The set of such (P, Q) is a square, and since B_1 and B_2 are convex,
it suffices to check whether the vertices of the square all lie in B_1
or B_2.
*/
bool inB(vector<pd> v) {
	d P1 = v[0].F;
	d P2 = v[0].S;
	d Q1 = v[1].F;
	d Q2 = v[1].S;
	if(inB1(P1, Q1) && inB1(P1, Q2) && inB1(P2, Q1) && inB1(P2, Q2)) return true;
	if(inB2(P1, Q1) && inB2(P1, Q2) && inB2(P2, Q1) && inB2(P2, Q2)) return true;
	return false;
}

/*
Give an upper bound for the loss arising from discarding the
region defined by v.
*/
d fullLoss(vector<pd> v) {
	d miSum = 0;
	d maSum = 0;
	int n = v.size();
	for(int i = 0; i < n; ++i) {
		miSum += v[i].F;
		maSum += v[i].S;
	}

	d a = (1 - maSum)/v[n-1].S;
	d b = (1 - miSum)/v[n-1].F;

	d bu = getUpperBuch(a, b);
	d ans = bu/v[n-1].F;
	for(int i = 0; i < n; ++i) {
		ans *= (v[i].S - v[i].F)/v[i].F;
	}
	return ans;
}

/*
Return a vector storing the maximal lengths of polynomials in v.
*/
vector<d> getMax(vector<pd> v) {
	vector<d> w;
	for(int i = 0; i < v.size(); ++i) {
		w.push_back(v[i].S);
	}
	return w;
}

/*
Given a set S defined by v, return z such that
SUM_{(p_1, ... p_n) \in S} S(A_{p_1 ... p_n}, z)
may be evaluated asymptotically via Lemma 6.1.

Takes as an input an upper bound for p_i in the set S.

Returns -1 if no such z may be found.
*/

d getZ(vector<d> v) {
	d sum = 0;
	int n = v.size();
	for(int i = 0; i < n; ++i) {
		sum += v[i];
	}

	if(sum > 0.75 - EPS) return -1;
	d maxZ = -1;


	//Consider partitions to (M, N).
	for(int i = 0; i < (1<<n); ++i) {
		d M = 0;
		int I = i;
		for(int j = 0; j < n; ++j) {
			if(I%2 == 0) M += v[j];
			I /= 2;
		}
		if(M < 0.5-EPS) {
			d N = sum - M;
			if(N > 0.25 + R-EPS) continue;
			if(N < 0.25) {
				return R - EPS;
			}
			maxZ = max(maxZ, 0.25 + R - N - EPS);
		}
	}
	return maxZ;
}


/*
Determine whether we can apply the Buchstab identity twice more
in the set defined by v.
*/
bool twoMore(vector<pd> v) {
	int n = v.size();
	if(n == 0) return true;
	vector<d> u = getMax(v);
	u.push_back(u[n-1]);
	if(getZ(u) > EPS) {
		return true;
	} else {
		return false;
	}
}

/*
Given intervals A, B, return the sumset A+B.
*/
pd add(pd A, pd B) {
	return {A.F + B.F, A.S + B.S};
}

/*
Given polynomials P_1, ..., P_n, check whether the polynomial
F(s) = P_1(s)...P_n(s)R_1(s)...R_k(s)H(s)
is admissible, where R_i < P_n and H is a zeta sum
(i.e. H > x^{1/4}).

We combine the polynomials R_1(s)...R_k(s) into one polynomial,
and check whether we can apply Proposition 5.1(iii).
*/

bool okHZeta(vector<pd> v) {
	int n = v.size();
	d miSum = 0;
	d maSum = 0;
	for(int i = 0; i < n; ++i) {
		miSum += v[i].F;
		maSum += v[i].S;
	}
	if(miSum >= 0.75 + EPS) return true;
	vector<d> w = getMax(v);
	w.push_back(0.75 + EPS - miSum); //Upper bound for the length of R_1(s)...R_k(s)
	for(int i = 0; i < (1<<n); ++i) {
		int I = i;
		d B = 0;
		d C = 0;
		for(int j = 0; j < n; ++j) {
			if(I%2 == 0) {
				B += w[j];
			} else {
				C += w[j];
			}
			I /= 2;
		}
		if(B < 0.5 - EPS && C < 0.25 + R - EPS) {
			return true;
		}
	}
	return false;
}


/*
Given polynomials P_1, ..., P_n, check whether the polynomial
F(s) = P_1(s)...P_n(s)R_1(s)...R_k(s)H(s)
is necessarily good, where R_i < P_n and H is not a zeta sum
(i.e. H < x^{1/4}).

We combine the polynomials R_1(s)...R_k(s)H(s) into one polynomial,
and then check whether we can apply Proposition 5.1(i) or (ii)
to obtain a suitable decomposition.
*/

bool okHnotZeta(vector<pd> v) {
	int n = v.size();
	d miSum = 0;
	d maSum = 0;
	for(int i = 0; i < n; ++i) {
		miSum += v[i].F;
		maSum += v[i].S;
	}
	v.push_back({1 - maSum, 1 - miSum});


	//We choose C to be the shortest polynomial we have.
	int Cindex = 0;
	pd C = v[0];

	for(int i = 1; i <= n; ++i) {
		if(v[i].S < C.S) {
			Cindex = i;
			C = v[i];
		}
	}

	bool found = false;
	for(int i = 0; i < (1<<n); ++i) {
		int I = i;
		pd A = {0, 0};
		pd B = {0, 0};
		for(int j = 0; j <= n; ++j) {
			if(j == Cindex) continue;
			if(I%2 == 0) {
				A = add(A, v[j]);
			} else {
				B = add(B, v[j]);
			}
			I /= 2;
		}

		bool origOK = true;
		if(B.S > 0.5 - R - EPS && !(A.F > 0.5 - R + EPS)) origOK = false;
		if(origOK && B.F < 0.5 - R + EPS && !(A.S + 0.6*C.S < 0.5 + R - EPS && A.S < 8*R + min(0.0, 1 - 8*C.S) - EPS)) origOK = false;
		if(origOK) return true;
		if(USE_TAB && tabBox(A.F, A.S, C.F, C.S)) return true;
	}
	return false;
}





int FULLPART=0, DECOMP=0;
bool origABC(pd A, pd B, pd C){
	if(B.S > 0.5 - R - EPS && !(A.F > 0.5 - R + EPS)) return false;
	if(B.F < 0.5 - R + EPS && !(A.S + 0.6*C.S < 0.5 + R - EPS && A.S < 8*R + min(0.0, 1 - 8*C.S) - EPS)) return false;
	return true;
}
// all assignments of pieces to three nonempty groups A,B,C
bool tripleOK(const vector<pd>& p){
	int k=p.size(); int tot=1; for(int i=0;i<k;i++) tot*=3;
	for(int m=0;m<tot;m++){
		pd G[3]={{0,0},{0,0},{0,0}}; int cnt[3]={0,0,0}; int M=m;
		for(int i=0;i<k;i++){ int g=M%3; M/=3; G[g]=add(G[g],p[i]); cnt[g]++; }
		if(!cnt[0]||!cnt[1]||!cnt[2]) continue;
		if(origABC(G[0],G[1],G[2])) return true;
		if(USE_TAB && tabBox(G[0].F,G[0].S,G[2].F,G[2].S)) return true;
	}
	return false;
}
// Prop 6.1(iii): pieces split into B (< 1/2) and C (< 1/4 + R), groups may be empty
bool zetaSplitOK(const vector<pd>& p){
	int k=p.size();
	for(int m=0;m<(1<<k);m++){ d B=0,C=0; for(int i=0;i<k;i++){ if(m>>i&1) C+=p[i].S; else B+=p[i].S; }
		if(B < 0.5-EPS && C < 0.25+R-EPS) return true; }
	return false;
}
bool decompOK(const vector<pd>& v, int idx){
	int n=v.size(); d miSum=0, maSum=0; for(int i=0;i<n;i++){ miSum+=v[i].F; maSum+=v[i].S; }
	pd rest={1-maSum,1-miSum}; pd P=v[idx]; if(P.F < 0.25) return false;
	vector<pd> others; for(int i=0;i<n;i++) if(i!=idx) others.push_back(v[i]);
	d tk=(d)1/400;
	// zeta factor Z in [1/4, P]
	for(d Z=0.25; Z<P.S; Z+=tk){ pd Zi={Z,min(Z+tk,P.S)}; pd rem={max(0.0,P.F-Zi.S), max(0.0,P.S-Zi.F)};
		vector<pd> q=others; q.push_back(rem); q.push_back(rest); if(!zetaSplitOK(q)) return false; }
	// no zeta factor: P = Q1 Q2 with Q1 in [P/2, max(1/4, 2P/3)]
	d hi=max(0.25, 2*P.S/3);
	for(d q1=P.F/2; q1<hi; q1+=tk){ pd Q1={q1,q1+tk}; pd Q2={max(0.0,P.F-Q1.S), max(0.0,P.S-Q1.F)};
		vector<pd> q=others; q.push_back(Q1); q.push_back(Q2); q.push_back(rest); if(!tripleOK(q)) return false; }
	return true;
}
bool okHnotZeta(vector<pd> v);
int WSPLIT=0, WSPLIT2=0;
// (C): non-zeta case. W = R_1...R_k H with every factor shorter than m = max(P_n, 1/4).
// Lemma (as Lemma split, with 1/4 replaced by m): W = W1 W2 with log W1 in [w/2, max(m, 2w/3)].
bool wsplitOK(const vector<pd>& v){
	int n=v.size(); d miSum=0, maSum=0; for(int i=0;i<n;i++){ miSum+=v[i].F; maSum+=v[i].S; }
	pd rest={1-maSum,1-miSum}; d m=max(v[n-1].S,0.25); d tk=(d)1/400;
	if(rest.F <= m + 1e-9) return false; // W must have >= 2 factors, so W2 is nonconstant
	d hi=max(m, 2*rest.S/3); if(hi>rest.S) hi=rest.S;
	for(d q1=rest.F/2; q1<hi; q1+=tk){ pd W1={q1,min(q1+tk,hi)}; pd W2={max(0.0,rest.F-W1.S), max(0.0,rest.S-W1.F)};
		vector<pd> q=v; q.push_back(W1); q.push_back(W2); if(!tripleOK(q)) return false; }
	return true;
}
// (C2): casework on the largest factor R1 of W (all factors of W are < m). Given R1 (log length in a tick),
//  (a) split off R1: pieces v, R1, W/R1;  or (b) all factors <= lam=R1.S, so for any L <= w some subproduct W1 has
//  log length in [L-lam, L]: pieces v, W1, W/W1, casework over W1 in that window;  or (c) second-largest factor R2 <= R1.
bool winOK(const vector<pd>& v, pd rest, d lam){
	d tk=(d)1/400;
	for(d L=lam; L<=rest.F+1e-12; L+=tk){ bool all=true;
		for(d a=L-lam; a<L-1e-12; a+=tk){ pd W1={a,min(a+tk,L)}; pd W2={max(0.0,rest.F-W1.S),rest.S-W1.F};
			vector<pd> q=v; q.push_back(W1); q.push_back(W2); if(!tripleOK(q)){all=false;break;} }
		if(all) return true; }
	return false;
}
int WS2DEPTH=1;
bool wsplit2OK(const vector<pd>& v, pd rest, d mcap, int depth){
	d tk=(d)1/400;
	for(d r1=0; r1<min(mcap,rest.S)-1e-12; r1+=tk){ pd R1={r1,min(r1+tk,mcap)};
		pd W2={max(0.0,rest.F-R1.S),rest.S-R1.F};
		vector<pd> q=v; q.push_back(R1); q.push_back(W2);
		if(tripleOK(q)) continue;
		if(winOK(v,rest,R1.S)) continue;
		if(depth<WS2DEPTH){ vector<pd> q2=v; q2.push_back(R1); if(wsplit2OK(q2,W2,R1.S,depth+1)) continue; }
		return false; }
	return true;
}
bool nonZetaOK(vector<pd> v){
	int n=v.size();
	if(okHnotZeta(v)) return true;
	d miSum=0, maSum=0; for(int i=0;i<n;i++){ miSum+=v[i].F; maSum+=v[i].S; }
	if(FULLPART){ vector<pd> q=v; q.push_back({1-maSum,1-miSum}); if(tripleOK(q)) return true; }
	if(maSum < 0.75 - EPS){
		d tick=(d)1/400; bool all=true;
		for(d R1=0; R1<=v[n-1].S; R1+=tick){ vector<pd> w=v; w.push_back({R1,R1+tick});
			bool ok=okHnotZeta(w);
			if(!ok && FULLPART){ d a=0,b=0; for(auto&x:w){a+=x.F;b+=x.S;} vector<pd> q=w; q.push_back({1-b,1-a}); ok=tripleOK(q); }
			if(!ok){ all=false; break; } }
		if(all) return true;
	}
	if(DECOMP) for(int i=0;i<n;i++) if(decompOK(v,i)) return true;
	if(WSPLIT && wsplitOK(v)) return true;
	if(WSPLIT2){ d mi=0,ma=0; for(auto&x:v){mi+=x.F;ma+=x.S;} if(wsplit2OK(v,{1-ma,1-mi},max(v[n-1].S,0.25),0)) return true; }
	return false;
}

bool okHZeta(vector<pd> v);
bool directOK(vector<pd> v){
	int n=v.size();
	if(!okHZeta(v)) return false;
	return nonZetaOK(v);
}

/*
Calculate the loss arising from the region defined by the vector v.
*/
d calculateLoss(vector<pd> v) {

	int n = v.size();
	d tick = (d) 1/400;

	//If n = 2 and we are in B_1 or B_2, an asymptotic is found.
	if(n == 2 && inB(v)) return 0;
	if(DIRECT && directOK(v)) return 0;

	/*
	Check whether we can apply the Buchstab identity twice more.
	Assuming that we can and we have so far applied it at most 4 times,
	apply it twice more.
	*/
	if(n <= 4 && twoMore(v)) {

		/*
		Let z be the maximum value such that we may apply the Buchstab
		identity with this z-parameter.
		*/
		d z = getZ(getMax(v));
		d prev = v[n-1].F;

		d loss = 0;
		d full = fullLoss(v);



		for(d A = prev; A+tick >= z; A -= tick) {
			vector<d> w = getMax(v);
			w.push_back(A+tick);

			/*
			Now that we have applied the Buchstab identity once,
			recheck the value of z for which we can apply it the second
			time.
			*/
			d z2 = getZ(w);
			for(d B = A; B+tick >= z2; B -= tick) {
				vector<pd> u = v;
				u.push_back({A, A+tick});
				u.push_back({B, B+tick});
				loss += calculateLoss(u);
				if(loss > full) break;
			}
			if(loss > full) break;
		}

		return min(loss, full);
	}

	/*
	If n = 2 or if the case where H > x^{1/4} fails, discard the sum
	and return the corresponding loss.
	*/
	if((n == 2 && !DIRECT) || !okHZeta(v)) return fullLoss(v);

	/*
	If in the case H < x^{1/4} the first strategy works, we have
	an asymptotic.
	*/
	if(nonZetaOK(v)) return 0;
	return fullLoss(v);
}

int main(int argc,char**argv) {
	R=atof(argv[1]); DIRECT=atoi(argv[2]); if(getenv("FULLPART")) FULLPART=1; if(getenv("DECOMP")) DECOMP=1; if(getenv("WSPLIT")) WSPLIT=1; if(getenv("WSPLIT2")) WSPLIT2=1; if(getenv("WS2DEPTH")) WS2DEPTH=atoi(getenv("WS2DEPTH")); double P0=atof(argv[3]),P1=atof(argv[4]);
	if(argc>5){ USE_TAB=1; std::ifstream f(argv[5]); int idx; std::string row; while(f>>idx>>row) TAB.push_back(row); TN=TAB.size(); std::cerr<<"table rows "<<TN<<std::endl; }
	cout << setprecision(8);
	cout << fixed;

	/*
	Calculate the loss arising from SUM S(A_{pq}, q),
	when p, q sum over [x^{0.07}, x^{1/2 - epsilon}],
	and q < p, pq^2 < x^{1+EPS}
	*/

	d loss = 0;
	d tick = (d) 1/3000;

	/*
	Split the sum over
	x^P <= p < x^{P + tick},
	x^Q <= q < x^{Q + tick}
	*/

	for(d P = R; P < 0.5; P += tick) {
		if(P < P0-1e-12 || P >= P1-1e-12) continue;
		for(d Q = R; Q < 0.5; Q += tick) {
			if(Q > P + tick + EPS || P+2*Q > 1+EPS) {
				/*
				The sum over (p, q) is empty.
				*/
				continue;
			}
			vector<pd> v;
			v.push_back({P, P+tick});
			v.push_back({Q, Q+tick});
			//Add the loss arising from this case to the total
			{ d L=calculateLoss(v); loss += L; if(getenv("DUMP") && L>0) cerr<<"BOX "<<P<<" "<<Q<<" "<<L<<" full "<<fullLoss(v)<<" twoMore "<<twoMore(v)<<" zeta "<<okHZeta(v)<<" nonzeta "<<nonZetaOK(v)<<"\n"; }
		}
		//Print intermediate upper bound for loss for p < x^{P + TICK}.

	}

	/*
	The computation takes roughly 15 minutes on a usual consumer
	laptop (when using the -O2 optimization flag).
	*/
	cout << "Total loss: " << loss << "\n";
}



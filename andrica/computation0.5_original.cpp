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

using namespace std;

//Macros for convenience
typedef double d;
typedef pair<d, d> pd;
#define F first
#define S second

//Important constants
const d R = 0.07;
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
	if(P + Q     >= 0.57  - EPS) return false;
	if(P + 0.7*Q <= 0.43  + EPS) return false;
	if(P - 3*Q   <= -0.56 + EPS) return false;

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

		if(B.S > 0.5 - R - EPS && !(A.F > 0.5 - R + EPS)) continue;
		if(B.F < 0.5 - R + EPS && !(A.S + 0.6*C.S < 0.5 + R - EPS && A.S < 8*R + min(0.0, 1 - 8*C.S) - EPS)) continue;
		return true;
	}
	return false;
}



/*
Calculate the loss arising from the region defined by the vector v.
*/
d calculateLoss(vector<pd> v) {

	int n = v.size();
	d tick = (d) 1/400;

	//If n = 2 and we are in B_1 or B_2, an asymptotic is found.
	if(n == 2 && inB(v)) return 0;

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
	if(n == 2 || !okHZeta(v)) return fullLoss(v);

	/*
	If in the case H < x^{1/4} the first strategy works, we have
	an asymptotic.
	*/
	if(okHnotZeta(v)) return 0;



	/*
	Consider then the second strategy.
	This reguires the product of polynomials being shorter than x^{3/4}.
	*/
	d maSum = 0;
	for(int i = 0; i < n; ++i) {
		maSum += v[i].S;
	}

	if(maSum >= 0.75 - EPS) return fullLoss(v);

	/*
	Consider possible values of R1
	*/

	for(d R1 = 0; R1 <= v[n-1].S; R1 += tick) {
		vector<pd> w = v;
		w.push_back({R1, R1 + tick});
		if(!okHnotZeta(w)) return fullLoss(v); 
	}
	return 0;
}

int main() {
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
			loss += calculateLoss(v);
		}
		//Print intermediate upper bound for loss for p < x^{P + TICK}.
		cout << P << " " << loss << "\n";
	}

	/*
	The computation takes roughly 15 minutes on a usual consumer
	laptop (when using the -O2 optimization flag).
	*/
	cout << "Total loss: " << loss << "\n";
}



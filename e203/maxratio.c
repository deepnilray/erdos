/* Exact coupled worst case for the merged {2,3} stage:
     R(A) = max over heavy offsets c of  (1 - covA(c)) / (1 - covG(c) - lam),
   covA = fraction of the image of A in (Z/M)^2 covered by U_i {psi_i = c_i}, covG = same over all of (Z/M)^2.
   Branch and bound: along a branch covA and covG only grow; covG_final <= covG_partial + sum_{rest} 1/e_i.
   First heavy offset fixed to 0 only if A is all of (Z/M)^2 -- otherwise translation changes covA, so all
   offsets are enumerated.  stdin: M g1x g1y g2x g2y lam_num lam_den nH [a b e]*nH   stdout: num den (exact ratio pieces) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int nH, WA, WG; static long nA, nG, M; static int E[16];
static uint64_t **bA, **bG, *accA[17], *accG[17];
static int G0; static double lam, rem[17], best = 0; static long bestA = 0, bestG = 0;
static long pc(uint64_t *v, int W){ long c = 0; for (int w = 0; w < W; w++) c += __builtin_popcountll(v[w]); return c; }
static void dfs(int d){
  long ca = pc(accA[d], WA), cg = pc(accG[d], WG);
  double ub = (1.0 - (double)ca / nA) / (1.0 - ((double)cg / nG + rem[d]) - lam);
  if (1.0 - ((double)cg / nG + rem[d]) - lam <= 0) ub = 1e300;
  if (ub <= best) return;
  if (d == nH){ double r = (1.0 - (double)ca / nA) / (1.0 - (double)cg / nG - lam);
                if (r > best){ best = r; bestA = ca; bestG = cg; } return; }
  int cmax = (d == 0) ? G0 : E[d];      /* heavy set 0: one offset per orbit of translations by A */
  for (int c = 0; c < cmax; c++){
    for (int w = 0; w < WA; w++) accA[d+1][w] = accA[d][w] | bA[d][(long)c*WA + w];
    for (int w = 0; w < WG; w++) accG[d+1][w] = accG[d][w] | bG[d][(long)c*WG + w];
    dfs(d + 1);
  }
}
int main(void){
  long g1x, g1y, g2x, g2y, ln, ld;
  if (scanf("%ld %ld %ld %ld %ld %ld %ld %d", &M, &g1x, &g1y, &g2x, &g2y, &ln, &ld, &nH) != 8) return 1;
  lam = (double)ln / ld; long aH[16], bH[16];
  for (int i = 0; i < nH; i++){ long e; if (scanf("%ld %ld %ld", &aH[i], &bH[i], &e) != 3) return 1; E[i] = (int)e; }
  nG = M*M; char *inA = calloc(nG, 1); nA = 0;
  for (long x = 0; x < M; x++) for (long y = 0; y < M; y++){
    long k = ((x*g1x + y*g2x) % M + M) % M, l = ((x*g1y + y*g2y) % M + M) % M;
    if (!inA[k*M + l]){ inA[k*M + l] = 1; nA++; } }
  WA = (int)((nA + 63)/64); WG = (int)((nG + 63)/64);
  bA = malloc(sizeof(uint64_t*)*nH); bG = malloc(sizeof(uint64_t*)*nH);
  for (int i = 0; i < nH; i++){ bA[i] = calloc((size_t)E[i]*WA, 8); bG[i] = calloc((size_t)E[i]*WG, 8);
    long xa = 0;
    for (long k = 0; k < M; k++) for (long l = 0; l < M; l++){
      long x = k*M + l, c = (aH[i]*k + bH[i]*l) % E[i];
      bG[i][c*WG + x/64] |= 1ULL << (x % 64);
      if (inA[x]){ bA[i][c*WA + xa/64] |= 1ULL << (xa % 64); xa++; } } }
  for (int d = 0; d <= nH; d++){ accA[d] = calloc(WA, 8); accG[d] = calloc(WG, 8); }
  rem[nH] = 0; for (int d = nH - 1; d >= 0; d--) rem[d] = rem[d+1] + 1.0 / E[d];
  /* psi_0(image of A) = g Z / E[0]; translations by A act on set-0 offsets transitively within cosets of it */
  { long g = E[0];
    for (long x = 0; x < M; x++) for (long y = 0; y < M; y++){
      long k = ((x*g1x + y*g2x) % M + M) % M, l = ((x*g1y + y*g2y) % M + M) % M;
      long v = (aH[0]*k + bH[0]*l) % E[0]; long a = g, b = v; while (b){ long t = a % b; a = b; b = t; } g = a; }
    G0 = (int)g; }
  dfs(0);
  printf("%.12f %ld %ld %ld %ld\n", best, bestA, nA, bestG, nG);
  return 0;
}

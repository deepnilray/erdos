/* Independent completeness check: for every prime 5 <= p < B, compute e_p = lcm(ord_p 2, ord_p 3) by factoring
   p-1 (smallest-prime-factor sieve) and exact order reduction; print p e_p whenever e_p <= EMAX. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint64_t pw(uint64_t b, uint64_t e, uint64_t m){ uint64_t r = 1; b %= m; while (e){ if (e & 1) r = r*b % m; b = b*b % m; e >>= 1; } return r; }
static uint64_t ord(uint64_t a, uint64_t p, const uint32_t *qs, int nq){
  uint64_t n = p - 1;
  for (int i = 0; i < nq; i++){ uint64_t q = qs[i]; while (n % q == 0 && pw(a, n/q, p) == 1) n /= q; }
  return n; }
static uint64_t gcd(uint64_t a, uint64_t b){ while (b){ uint64_t t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv){
  uint64_t B = strtoull(argv[1], 0, 10), EMAX = strtoull(argv[2], 0, 10);
  uint32_t *spf = calloc(B, 4);
  for (uint64_t i = 2; i < B; i++) if (!spf[i]){ for (uint64_t j = i; j < B; j += i) if (!spf[j]) spf[j] = (uint32_t)i; }
  long cnt = 0;
  for (uint64_t p = 5; p < B; p++){
    if (spf[p] != p) continue;
    uint32_t qs[32]; int nq = 0; uint64_t n = p - 1;
    while (n > 1){ uint32_t q = spf[n]; qs[nq++] = q; while (n % q == 0) n /= q; }
    uint64_t o2 = ord(2, p, qs, nq), o3 = ord(3, p, qs, nq), e = o2 / gcd(o2, o3) * o3;
    if (e <= EMAX){ printf("%lu %lu\n", p, e); cnt++; }
  }
  fprintf(stderr, "primes below %lu with e_p <= %lu: %ld\n", B, EMAX, cnt);
}

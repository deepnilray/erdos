#!/bin/bash
# run3.sh R table tag : sieve3 with FULLPART+DECOMP, all chunks sequentially
R=$1; T=$2; G=$3
for c in "0.43 0.5" "0.39 0.43" "0.36 0.39" "0.3337 0.36" "0.3 0.3337" "0.26 0.3" "0.22 0.26" "0.16 0.22" "0.0 0.16"; do set -- $c; FULLPART=1 DECOMP=1 ./sieve3 $R 1 $1 $2 $T > s3_${G}_$1_$2.txt 2>&1; done

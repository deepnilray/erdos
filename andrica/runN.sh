#!/bin/bash
R=$1; T=$2; G=$3; H=$4
if [ "$H" = "1" ]; then L="0.43 0.5|0.3337 0.36|0.26 0.3|0.0 0.16"; else L="0.39 0.43|0.36 0.39|0.3 0.3337|0.22 0.26|0.16 0.22"; fi
mkdir -p out
IFS='|'; for c in $L; do IFS=' '; set -- $c; ZTAB=Z400_0575.txt ZNOZ=1 WSPLIT=1 FULLPART=1 DECOMP=1 ./sieveZ $R 1 $1 $2 $T > out/${G}_$1_$2.txt 2>&1; IFS='|'; done

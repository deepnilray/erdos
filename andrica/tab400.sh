#!/bin/bash
# tab400.sh R  -> T400_<R>.txt using two row ranges sequentially on one core (callers run two)
R=$1; P=$2
case $P in
 a) ./cover 400 $R 1 0 120 > t4_${R}_a.txt 2>/dev/null ;;
 b) ./cover 400 $R 1 120 400 > t4_${R}_b.txt 2>/dev/null ;;
esac

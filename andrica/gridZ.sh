#!/bin/bash
# usage: gridZ.sh N R OUT  (rows z in [N/4, N/2))
N=$1; R=$2; O=$3; a=$((N/4)); b=$((N/2))
for h in 0 1; do ( for ((s=a+h; s<b; s+=2)); do BUDGET=${BUDGET:-20000} ./coverZ $N $R $s $((s+1)) 2>/dev/null; done > $O.part$h ) & done
wait; cat $O.part0 $O.part1 | sort -n > $O; rm $O.part0 $O.part1; echo done > $O.done

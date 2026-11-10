#!/bin/bash
# usage: run8.sh parity  -- runs n=8 for N in 128..247 with N%2==parity, skipping finished ones
for N in $(seq 128 247); do
  if [ $((N%2)) -ne $1 ]; then continue; fi
  if grep -q "^n=8 N=$N " logs/n8.log 2>/dev/null; then continue; fi
  ./enum2 8 $N p > logs/n8_sets_$N.txt 2> logs/n8_tmp_$N.txt && cat logs/n8_tmp_$N.txt >> logs/n8.log
done

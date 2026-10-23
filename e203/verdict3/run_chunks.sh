#!/bin/bash
# sequential chunked certificate; resumable (a chunk is done when its log has a RESULT line)
cd /home/claude/e203wt/e203
LO=${1:-400000}; HI=${2:-800000}; STEP=${3:-20000}; shift 3
POOLS="$@"
a=$LO
while [ $a -lt $HI ]; do
  b=$((a+STEP)); f=verdict3/chunks/cert_${a}_${b}.log
  if ! grep -q "^RESULT" $f 2>/dev/null; then
    nice -n 10 python3 verdict3/certify_range.py $a $b $POOLS > $f 2>&1
  fi
  a=$b
done
echo ALLDONE > verdict3/chunks/ALLDONE_${LO}_${HI}

#!/bin/bash
# Theorem E at 8e5: run after verdict3/run_verify.sh has printed "EXACT FRACTION:" in verdict3/verify23_800k.log.
# Uses the SAME delta file as the exact verifier (the S term must use the measure that B was computed for).
cd /home/claude/e203wt/e203
FR=$(grep "^EXACT FRACTION:" verdict3/verify23_800k.log | awk '{print $3}')
[ -z "$FR" ] && { echo "no EXACT FRACTION yet"; exit 1; }
sha256sum delta23r_E800000.json > verdict3/mixed_800k.log
nice -n 10 python3 verify_mixed.py poolE800000.jsonl 800000 delta23r_E800000.json "$FR" >> verdict3/mixed_800k.log 2>&1
cat verdict3/mixed_800k.log

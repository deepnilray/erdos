#!/bin/bash
cd /home/claude/e203wt/e203
nice -n 10 python3 verdict3/run_bound.py poolE800000.jsonl 800000 0.578318 200000 > verdict3/run_bound_800k.log 2>&1
verdict3/run_chunks.sh 400000 800000 20000 poolE400000.jsonl poolE_400k_800k.jsonl > verdict3/chunks/driver.out 2>&1

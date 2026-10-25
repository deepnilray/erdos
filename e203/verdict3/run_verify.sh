#!/bin/bash
cd /home/claude/e203wt/e203
export VERIFY_CKPT=verdict3/verify_ckpt.txt VERIFY_WORKERS=2
nice -n 10 python3 verify_distortion23.py poolE800000.jsonl 800000 5,7,13,17,19,37,73,97,577 delta23r_E800000.json 5,7,13,17,19,37 2770/5184 types_E200000.json coupled_full_E200000.txt > verdict3/verify23_800k.log 2>&1

#!/bin/bash
# Exact-rational verification of B' for C's final Theorem-Z delta vector (copy of V_run_cap.sh, own checkpoint).  Launch from the head session.
cd /home/claude/e203wt/e203
export VERIFY_CKPT=verdict3/C_ckpt_final.txt VERIFY_WORKERS=2
nice -n 10 python3 verify_distortion23.py poolE800000.jsonl 800000 5,7,13,17,19,37,73,97,577 verdict3/C_delta_final.json 5,7,13,17,19,37 2770/5184 types_E200000.json coupled_full_E200000.txt > verdict3/C_verify_final.log 2>&1

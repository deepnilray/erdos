#!/bin/bash
# exact verifier at 8e5, resumable via VERIFY_CKPT; refuses to resume if delta23r_E800000.json changed since the checkpoint began
cd /home/claude/e203wt/e203
export VERIFY_CKPT=verdict3/verify_ckpt.txt VERIFY_WORKERS=1
H=verdict3/verify23_800k.delta.sha256
if [ -s "$VERIFY_CKPT" ] && [ -s $H ]; then sha256sum -c --quiet $H || { echo "delta changed: delete $VERIFY_CKPT"; exit 1; }; fi
[ -s "$VERIFY_CKPT" ] || sha256sum delta23r_E800000.json > $H
nice -n 10 python3 verify_distortion23.py poolE800000.jsonl 800000 5,7,13,17,19,37,73,97,577 delta23r_E800000.json 5,7,13,17,19,37 2770/5184 types_E200000.json coupled_full_E200000.txt > verdict3/verify23_800k.log 2>&1

#!/bin/bash
# runs D_W.py and D_comp.py for w<31 with Y=1e7 (logs in D_data/)
cd /home/claude/e203wt/e203/verdict3
for w in 29 23 19 17 13; do
  nice -n 19 python3 D_W.py $w 1e7 2>&1 | grep -v Warn > D_data/W_w${w}.log
  nice -n 19 python3 D_comp.py $w 3000 1e7 2>&1 | grep -v Warn > D_data/comp_w${w}.log
done
echo DONE > D_data/run_w.done

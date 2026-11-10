#!/bin/bash
cd /home/claude/e203wt/e203/verdict3
for r in "0 1000000000" "1000000001 2000000000" "2000000001 3000000000"; do
 set -- $r
 nice -n 10 /tmp/claude-0/-home-claude/89603433-4fa1-57e4-a8fc-4d2490c5f294/scratchpad/s1 $1 $2 0 1 > search_l1_$1_$2.log 2>&1
done

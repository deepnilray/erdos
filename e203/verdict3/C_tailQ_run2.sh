cd /home/claude/e203wt/e203
for a in "1.0 1.0" "1.0 1.2" "1.0 1.34" "1.2 1.34" "1.2 1.5" "1.5 1.5" "1.0 1.5"; do
 set -- $a
 echo "tailonly kappa_L=$1 KQ=$2: $(PYTHONPATH=. nice -n 10 python3 verdict3/C_tail.py $1 1000 x 0.0 $2 tailonly 2>&1 | grep 'min-per-stage' | cut -c1-90)"
done

cd /home/claude/e203wt/e203
for a in "1.0 1.0 0.0" "1.2 1.2 0.0" "1.5 1.5 0.0" "1.2 1.5 0.0" "1.3 1.3 0.25" "1.0 1.3 0.0" "1.0 1.2 0.25" "1.0 1.6 0.0"; do
 set -- $a
 echo "kappa_L=$1 KQ=$2 eps=$3: $(PYTHONPATH=. nice -n 10 python3 verdict3/C_tail.py $1 1000 x $3 $2 2>&1 | grep 'min-per-stage' | cut -c1-90)"
done

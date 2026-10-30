# delta-profile scan for Theorem C' (round 4).  Each line: knobs -> pieces file; then C_tailR at uniform kQ=1.34 and at the per-range empirical kappas.
cd /home/claude/e203wt/e203
run() { # L1 DBIG DSCALE DCAP tag
  POUT=verdict3/C_tp_$5.npz DBIG=$2 DSCALE=$3 DCAP=$4 PYTHONPATH=. nice -n 15 python3 verdict3/C_tail.py 1.0 $1 x 0.0 1.0 tailonly >/dev/null 2>&1
  a=$(nice -n 15 python3 verdict3/C_tailR.py verdict3/C_tp_$5.npz 1 1.34 0 1.34 | head -1 | cut -c1-80)
  b=$(KLR=1.26,1.26,1.19,1.10,1.01,0.97,0.96,0.90 KQ2R=1.83,1.83,1.53,1.35,1.15,1.13,1.77,5.25 nice -n 15 python3 verdict3/C_tailR.py verdict3/C_tp_$5.npz 1 1.34 0 1.34 | head -1 | cut -c40-80)
  echo "$5 L1=$1 DBIG=$2 DSCALE=$3 DCAP=$4 | uniform 1.34: $a | empirical: $b"
}
run 1000 0.5 1.0 1.0 base
run 1000 0.4 1.0 1.0 big04
run 1000 0.6 1.0 1.0 big06
run 300 0.5 1.0 1.0 L300
run 3000 0.5 1.0 1.0 L3000
run 1000 0.5 0.9 1.0 sc09
run 1000 0.5 1.1 1.0 sc11
run 1000 0.5 1.0 0.5 cap05

#!/bin/bash
# build_T400_0575M.sh : rebuild the main admissible grid for r = 0.0575 and check T400_0575M.txt against it.
#  1. plain grid (cover.cpp, Guth-Maynard on, default budget), rows split over two cores;
#  2. boundary cells: cells not '1' in the plain grid, with i+j <= N-2, having a '1' within
#     Chebyshev distance 2 (mk_cells.py);
#  3. coverM.cpp with the extended Cauchy-Schwarz routes (MCS=3) on those cells, BUDGET=20000;
#  4. cell-wise OR of the plain grid and the coverM output;
#  5. check that every certified cell of the shipped grid T400_0575M.txt is certified in the rebuilt
#     grid. (The shipped grid was assembled in stages, partly with the default budget 8000, so the
#     rebuilt grid certifies some further cells; these are not used in Table 1.)
set -e
R=0.0575
g++ -O2 -o cover cover.cpp
g++ -O2 -o coverM coverM.cpp
( ./cover 400 $R 1 0 120 > plain_a.txt 2>/dev/null ) &
( ./cover 400 $R 1 120 400 > plain_b.txt 2>/dev/null ) &
wait
cat plain_a.txt plain_b.txt | sort -n > plain_0575.txt
cmp plain_0575.txt T400_0575.txt && echo "plain grid matches T400_0575.txt"
python3 mk_cells.py cells plain_0575.txt cells_0575_rebuilt.txt
cmp cells_0575_rebuilt.txt cells_0575.txt && echo "boundary cells match cells_0575.txt"
( CELLS=cells_0575_rebuilt.txt MCS=3 BUDGET=20000 ./coverM 400 $R 1 0 140 > cm_a.txt 2>/dev/null ) &
( CELLS=cells_0575_rebuilt.txt MCS=3 BUDGET=20000 ./coverM 400 $R 1 140 400 > cm_b.txt 2>/dev/null ) &
wait
cat cm_a.txt cm_b.txt | sort -n > coverM_0575_rebuilt.txt
cmp coverM_0575_rebuilt.txt coverM_0575.txt && echo "coverM output matches coverM_0575.txt"
python3 mk_cells.py or plain_0575.txt coverM_0575_rebuilt.txt T400_0575M_rebuilt.txt
python3 mk_cells.py sub T400_0575M.txt T400_0575M_rebuilt.txt

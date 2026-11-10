#!/usr/bin/env bash
# Usage: ./run_small_orders.sh /path/to/nauty/geng
set -euo pipefail
cd -- "$(dirname -- "$0")"
geng_binary=${1:-geng}
work_dir=$(mktemp -d)
trap 'rm -rf -- "$work_dir"' EXIT

g++ -O3 -std=c++17 -Wall -Wextra exact_scan.cpp -lgmpxx -lgmp -o "$work_dir/exact_scan"
status=0
"$work_dir/exact_scan" --plant-wrong-inertia </dev/null >"$work_dir/control.log" 2>&1 || status=$?
if [[ $status != 3 ]] || ! rg -q 'K2 control detected an incorrect inertia classification' "$work_dir/control.log"; then
    cat "$work_dir/control.log" >&2
    printf 'Expected a fired inertia control (exit 3), got %s\n' "$status" >&2
    exit 1
fi
printf 'CONTROL FIRED: %s\n' "$(cat "$work_dir/control.log")"

expected=(0 0 1 2 6 21 112 853 11117 261080 11716571)
for n in {2..10}; do
    "$geng_binary" -cq "$n" | "$work_dir/exact_scan" >"$work_dir/scan.log"
    read -r unresolved interlacing integer_inertia rational_inertia <"$work_dir/scan.log"
    count=$(( ${unresolved#*=} + ${interlacing#*=} + ${integer_inertia#*=} + ${rational_inertia#*=} ))
    if [[ ${unresolved#*=} != 0 || $count != "${expected[n]}" ]]; then
        printf 'Order %d failed certification or enumeration count\n' "$n" >&2
        exit 1
    fi
    printf 'VERIFIED n=%d graphs=%d %s\n' "$n" "$count" "$(cat "$work_dir/scan.log")"
done

#!/usr/bin/env bash
# Usage: ./lean/verify.sh /path/to/mathlib4 (v4.28.0 with the cache installed)
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
mathlib_dir=$(cd -- "${1:?give the path to a Mathlib v4.28.0 checkout}" && pwd)
work_dir=$(mktemp -d)
trap 'rm -rf -- "$work_dir"' EXIT

cd -- "$mathlib_dir"
dependency_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work_dir:$dependency_path"

for module in Certificate SpectralBridge Counterexample; do
    lean --root="$source_dir" -o "$work_dir/$module.olean" "$source_dir/$module.lean" \
        | tee "$work_dir/$module.log"
done
rg -Fq "'Cazenave20829.counterexample' depends on axioms: [propext, Classical.choice, Quot.sound]" \
    "$work_dir/Counterexample.log"

sed 's/(37 \/ 2504)/(36 \/ 2504)/' "$source_dir/Certificate.lean" > "$work_dir/Planted.lean"
if lean --root="$work_dir" "$work_dir/Planted.lean" >"$work_dir/planted.log" 2>&1; then
    printf 'Silent Lean control\n' >&2
    exit 1
fi
if ! rg -q 'error: unsolved goals' "$work_dir/planted.log"; then
    cat "$work_dir/planted.log" >&2
    exit 1
fi
printf 'CONTROL FIRED: changing the rational square coefficient made Lean reject the identity\n'
lean --version
printf 'Mathlib commit %s\n' "$(git rev-parse HEAD)"

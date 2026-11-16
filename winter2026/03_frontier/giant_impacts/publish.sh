#!/bin/bash
# copy results/ to branch impacts-live-$SHARD (force push). Usage: publish.sh <repo> <token>
set +e
B="impacts-live-${SHARD:-0}"
rm -rf /tmp/pub_$B && mkdir -p /tmp/pub_$B && cp -r results/* /tmp/pub_$B/ 2>/dev/null; rm -f /tmp/pub_$B/pool.csv
cd /tmp/pub_$B && git init -q && git checkout -q -b $B
git config user.name "github-actions" && git config user.email "actions@github.com"
echo "run ${GITHUB_RUN_ID} of ${GITHUB_SHA} shard ${SHARD} at $(date -u)" > RUN_INFO.txt
git add -A && git commit -qm "$B ${GITHUB_RUN_ID} $(date -u +%H:%M)"
git push -q -f "https://x-access-token:$2@github.com/$1.git" $B

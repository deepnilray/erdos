#!/bin/bash
# copy results/ to branch impacts-live (force push). Usage: publish.sh <repo> <token>
set +e
rm -rf /tmp/pub && mkdir -p /tmp/pub && cp -r results/* /tmp/pub/ 2>/dev/null
cd /tmp/pub && git init -q && git checkout -q -b impacts-live
git config user.name "github-actions" && git config user.email "actions@github.com"
echo "run ${GITHUB_RUN_ID} of ${GITHUB_SHA} at $(date -u)" > RUN_INFO.txt
git add -A && git commit -qm "impacts live ${GITHUB_RUN_ID} $(date -u +%H:%M)"
git push -q -f "https://x-access-token:$2@github.com/$1.git" impacts-live

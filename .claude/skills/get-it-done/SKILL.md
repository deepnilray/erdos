---
name: get-it-done
description: Finish-the-whole-job mode. Use when the user hands over a task (any size, any number of steps) and expects all of it done end to end without having to repeat or re-ask. Trigger on "get it done", "do all of it", "upload/download/process everything", or any multi-step request where partial completion would not be acceptable.
---

# Get it done

The user gives an instruction and expects the **whole** thing finished, no matter how many steps it takes. Partial progress is not a result.

## How to work

1. **Scope it fully.** Work out everything the request covers (all 23 videos, not the first one). List the pieces, track them, and count at the end.
2. **Start immediately** on what is unambiguous. Do not wait for permission on safe, in-scope steps.
3. **Treat blockers as problems to solve, not reasons to stop.** When a route fails (size limit, auth, tool cap), find another legitimate route (a different API, a script, a background job, chunking, retries). Diagnose before giving up: check whether the fault is the token, the proxy, or the target.
4. **Ask only when it is truly the user's call**: an ambiguous goal that changes what gets built, a credential only they can create, a destructive or outward-facing action. Ask once, concisely, with a recommended default and the cost of each option. Never make the user repeat themselves.
5. **Respect limits while pushing through.** Do not bypass security controls, disable TLS checks, change network policy, or use credentials beyond what was given. If one route is off limits, say so and take another.
6. **Run long work in the background**, with retries and a log, and never let an output filter kill it (do not pipe a long job into `head`).
7. **Verify against the source, not against your own success messages.** Compare counts, names and byte sizes between what exists locally and what landed at the destination. Fix any gap (missing item, mismatch) before declaring done.
8. **Handle side effects.** Do not commit huge or irrelevant files to git (exclude them locally). Delete temporary secrets you wrote to disk. Tell the user what to revoke or clean up.
9. **Interruptions:** when the user adds or changes a requirement mid-task, fold it in and keep going.
10. **Report faithfully.** Say what was done, what was verified, what is uncertain (for example a possible duplicate), and where the results live. Keep it short.

## Done means

Every item in scope is finished and checked at the destination, or the one remaining blocker is named along with exactly what the user must do.

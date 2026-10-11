# AIClassDocuments: recovering ambiguous AIBridge result delivery

This project uses the shared AIBridge recovery contract:
https://github.com/nguyenletrian/AIBridge/blob/main/docs/AMBIGUOUS_DELIVERY_RECOVERY.md

## Current incident

At 2026-10-11, the original task
`aiclassdocuments-conversation-rollover-count-diagnostic-20261011`
completed local execution but ChatGPT provider delivery became ambiguous.
Bridge refused to resend and blocked FIFO. Pending behind it:

- `aiclassdocuments-test-script-bridge-diagnostics-20261011`
- `aiclassdocuments-on-demand-read-log-20261011-b`

One managed restart was requested to load AIBridge PR #17.

## Architect recovery and ACK steps

1. Fetch the **current** `bridgeTask.json` from main, not a stale chat copy.
2. Inspect only `delivery_recovery_review` on the exact metrics task.
   Confirm `schema=aibridge-ambiguous-delivery-review-v1`,
   `task_id`, `result_route=browser:conversation_metrics`,
   `review_status=requires_architect_review`,
   `delivery=uncertain_not_resent`.
3. Use `safe_result.messages` and related counts if present. If the
   probe failed, record that; never infer a message count or fake PASS.
   `delivery=uncertain_not_resent` does not prove ChatGPT received
   the earlier result.
4. Only **after** that review, mark precisely the metrics task
   `architect_ack:true`, `bridge_completed:true`,
   `status:completed` if `execution_success=true` or
   `status:failed` if `execution_success=false`, with concise
   non-sensitive review notes. Keep all other tasks and history.
5. Let the worker proceed in FIFO. Review and ACK the TestScript task
   only after its actual `task_result`; similarly for the later
   `runtime:read_log` task.
6. Keep Jetking source goal paused at `AWAITING_SOURCE`; do not
   reopen lessons or create duplicate diagnostic tasks as a fallback.
7. If the preview is absent after the restart, do not ACK or
   relaunch blindly. Diagnose the current runtime head, Git push,
   and `RETURN_RECOVERY_REVIEW_*` log evidence safely.

This runbook does not authorize exporting raw worker logs, URLs,
credentials or lesson content to Git; the fallback schema intentionally
excludes them.

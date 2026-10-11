# AIClassDocuments — uses shared AIBridge status reminders

The owner confirmed on 2026-10-11 that status request reminders are
**AIBridge infrastructure for all managed projects**, not settings to
maintain separately in each project's task file.

Canonical implementation and configuration:
https://github.com/nguyenletrian/AIBrigde/blob/main/docs/REQUEST_REMINDERS.md

Shared Bridge default in `~/.aibridge/config.json`:

```json
"runtime": {
  "request_reminders": {
    "enabled": true,
    "revision": "bridge-global-managed-workers-v1",
    "interval_seconds": 60,
    "stalled_after_seconds": 45,
    "max_per_episode": 4
  }
}
```

All managed workers inherit this when they load AIBridge PR #23 or later,
including AIClassDocuments and AIMayaTool. The legacy
`bridgeTask.json.request_reminders` field has been **removed**.
One worker's reminders cannot reset another worker's persisted ledger.

Reminders are informational `task_request` messages to review current
TaskSource/worker state, not a command to execute a task or restart a
paused goal. The Jetking instructional source goal remains
`goal_review.enabled=false`. They must not trigger a new ChatGPT chat,
auto-ACK an unseen task result, or replay an ambiguous Send.

## DOM-shape probe result recovery

A live 60-second reminder already confirmed that
`aiclassdocuments-live-conversation-dom-shape-20261011` executed
successfully, but the result was retained locally at `RESULT_PENDING`
with `recovery_publish_pending:true`. PR #23 adds a **content-free
Git review preview** for the already-saved selector counts, enabling
Architect to inspect/ACK the same task without re-execution or
blind duplicate Send. If the preview is not yet present, no ACK is
authorized.

A managed runtime restart was requested in TaskSource
`aiclassdocuments-global-bridge-reminders-pr23-20261011`;
do not confuse that request with proof of a completed worker restart.

Shared PR: https://github.com/nguyenletrian/AIBrigde/pull/23

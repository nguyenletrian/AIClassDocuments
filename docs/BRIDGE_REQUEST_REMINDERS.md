# AIClassDocuments — Owner-enabled Bridge status reminders

The owner explicitly restored proactive status `task_request` reminders
on 2026-10-11. Shared AIBridge implementation:
https://github.com/nguyenletrian/AIBrigde/blob/main/docs/REQUEST_REMINDERS.md

Current authoritative `bridgeTask.json` includes:

```json
"request_reminders": {
  "enabled": true,
  "revision": "owner-restored-status-20261011-v1",
  "interval_seconds": 180,
  "stalled_after_seconds": 45,
  "max_per_episode": 4
}
```

This sends an informational `task_request` through current Edge ChatGPT
composer when a task remains unchanged for 45 seconds, then no faster
than every 180 seconds, at most four messages per unchanged episode.
On an idle queue, it may report status promptly. Reservations persist
across worker restarts; ambiguous sends are not replayed blindly.

**Do not resume Jetking goal**: `goal_review.enabled=false` remains
authoritative and the lesson source is still unverified. A reminder
authorizes an Architect *status review*, not re-reading slides or
inventing lesson content. Never auto ACK the remaining live
`aiclassdocuments-live-conversation-dom-shape-20261011` task without
a verified exact `task_result` or an approved safe review channel.
The owner can disable reminders by setting
`request_reminders.enabled=false`; the worker-local cancellation
marker also overrides them.

AIBridge PR #21: https://github.com/nguyenletrian/AIBrigde/pull/21

CI PASS alone does not prove the worker has restarted or delivered a
reminder. Confirm the runtime HEAD and an actual `task_request` before
claiming live notifications work.

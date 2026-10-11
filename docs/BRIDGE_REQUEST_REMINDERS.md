# AIClassDocuments — Owner-enabled Bridge status reminders

The owner explicitly restored proactive status `task_request` reminders
on 2026-10-11. Shared AIBridge implementation:
https://github.com/nguyenletrian/AIBrigde/blob/main/docs/REQUEST_REMINDERS.md

Current authoritative `bridgeTask.json` includes:

```json
"request_reminders": {
  "enabled": true,
  "revision": "owner-sixty-second-status-20261011-v2",
  "interval_seconds": 60,
  "stalled_after_seconds": 45,
  "max_per_episode": 4
}
```

This sends an informational `task_request` through current Edge ChatGPT
composer when a task remains unchanged for 45 seconds, then no faster
than every 60 seconds, at most four messages per unchanged episode.
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

## One-minute cadence adjustment

Owner explicitly changed the reminder spacing from three minutes to **60 seconds**. AIBridge PR #22 ([merged](https://github.com/nguyenletrian/AIBrigde/pull/22)) also adds a content-free `blocked_task_state` field in stalled reminder messages: the local queue state, saved result yes/no, result success (if known), bounded return-attempt count, and recovery flags. This enables Architect to distinguish a task not yet run from one held at provider delivery or ACK. No original results, errors, URLs, DOM, or log text are sent through these fields.

The original DOM-shape task remains pending until real evidence is reviewed. The Jetking goal remains paused. Worker restart has been requested for PR #22; deployment and new-cadence live observations are not yet independently verified.

## Usage-Based Auto-Lock

Auto-lock revokes a user's access to a Resource if they haven't accessed it within a configurable inactivity window. Per-user, automatic, designed for least-privilege hygiene.

**Concept:**
- Users granted access to a Resource
- If a user doesn't access the Resource for N days, that user is locked out (other users in the same Group are unaffected -- it's per-user)
- Locked user can request re-access (manual approval) or unlock with a reason (auto approval)

**Available Durations (Admin Console):**
- 1, 7, 30, 60, 90 days
- Other durations possible via API

**Configuration Locations:**
- **Resource page**: applies to all Group assignments (default)
- **Group page**: per-Group on a specific Resource (overrides the Resource default)
- **Per-Group-on-Resource**: when adding a Group to a Resource, set duration + approval method inline

### Approval Modes (When Locked Out)

| Mode | Flow |
|---|---|
| **Manual Approval** | User submits a request with a reason -> admin/Resource Approver decides |
| **Auto Approval** | User provides a reason -> immediately unlocked; reason logged in analytics |

### Tracking & Audit

- Auto-lock duration changes appear in the **Access category of Audit Logs**
- Per-Resource / per-Group / per-User CSV export includes:
  - Groups with access + their Resource Policy
  - Expiration dates (if Ephemeral Access is also configured)
  - Auto-lock duration
  - Per-user current lock status + last unlock timestamp

### Notifications & Webhooks

Admins choose how to be notified of incoming unlock requests:
- **Email**: select which Admin roles receive (Admins, DevOps, Access Reviewers)
- **Webhook**: disable emails, integrate with Slack / PagerDuty / SIEM

**Webhook Payload Schema** (`type: ACCESS_REQUEST`):
```json
{
  "timestamp": "...",
  "tenant": "autoco.twingate.com",
  "version": "1",
  "type": "ACCESS_REQUEST",
  "request_id": "...",
  "request_url": "https://...",
  "user_name": "Alex Marshall",
  "user_url": "https://...",
  "resource_name": "Gitlab",
  "resource_url": "https://...",
  "requested_at": "...",
  "reason": "I need access after a long period of no usage.",
  "approval_mode": "MANUAL",
  "request_type": "AutoLock",
  "request_duration_seconds": 2592000
}
```

`request_type` distinguishes `AutoLock` (this doc) from JIT (`JITAccessRequest`).

### Decision Notes

- Use auto-lock as a **backstop** for over-provisioned access (vendors, contractors, team-rotation users)
- 30-90 day windows are typical -- shorter windows generate too many unlock requests
- Combine with **Ephemeral Access** for time-bound engagements: ephemeral sets the hard cutoff; auto-lock catches early inactivity
- For high-trust users + frequently-used Resources: don't enable auto-lock; the unlock friction isn't worth it

**Gotchas:**
- Auto-lock is **per-user**, not per-Group -- one user's access being locked doesn't affect Group members
- Resource Policy is unrelated to auto-lock duration -- a user can satisfy the Resource Policy and still be auto-locked for inactivity
- Manual approval mode requires admin attention -- if your team is small, default to auto approval with reason logging
- The reason field is free-text -- don't rely on it for structured workflows; use a webhook + ticketing for that

**Related Docs:**
- /docs/jit-access-requests -- Sibling: time-bounded access via explicit request
- /docs/ephemeral-access-to-resources -- Sibling: time-bounded Group access (no inactivity check)
- /docs/resources-reviewing-access-requests -- Approval workflow
- /docs/audit-logs -- Audit Logs reference

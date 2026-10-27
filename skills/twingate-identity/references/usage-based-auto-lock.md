---
source: https://www.twingate.com/docs/usage-based-auto-lock
type: docs
fetched: 2026-10-25
source_version: 7d24dea806e2417d11f72d986532913f684b78611e6b6c11b3d2d2e3b5d94b6f
trust: official
---

# Usage-based Auto-lock

## Page Title
Usage-based Auto-lock

## Summary
Auto-lock automatically revokes Resource access for users who haven't accessed it within a configured duration, enforcing least-privilege. Access can be restored via manual admin approval or automatic approval (user provides a reason). Configuration is available at both the Resource and Group level.

## Key Information
- Auto-lock is evaluated **per user**, even when configured at the Group level
- Locking triggers when a user hasn't accessed the Resource within the configured duration
- Audit log entries appear under the **Access** category in the Admin Console
- Access summary reports (CSV/download) are available from Resource, Group, or User pages
- Webhook payload `request_type` field will be `"AutoLock"` for auto-lock-triggered requests

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate
- Notification settings configured at **Settings > Notifications** if webhook/email alerts are needed

## Configuration Values

| Setting | Admin Console Options | API |
|---|---|---|
| Auto-lock duration | 1, 7, 30, 60, 90 days | Additional durations available |
| Approval method | Manual, Automatic | — |

**Webhook payload fields (relevant to auto-lock):**
- `type`: `"ACCESS_REQUEST"`
- `request_type`: `"AutoLock"`
- `approval_mode`: `"MANUAL"` or `"AUTOMATIC"`
- `request_duration_seconds`: duration in seconds (e.g., `2592000` = 30 days)

## Step-by-Step

**Configure from Resource page:**
1. Navigate to the Resource in Admin Console
2. Set auto-lock duration at the Resource level (applies to all users)
3. Optionally override per Group when adding or editing Group access (set duration + approval method via Group options button)

**Configure from Group page:**
1. Navigate to the Group detail page
2. Set auto-lock duration and approval method per Resource

**Unlock a locked user:**
1. Navigate to the user's detail page in Admin Console
2. Unlock the specific Resource

## Gotchas
- Group-level configuration **inherits** Resource-level settings by default; must be explicitly overridden per Group
- Manual approval requires admin action; automatic approval restores access immediately but still logs reason in analytics
- Only Admin Console exposes 5 duration options; use the API for other durations
- Notifications (email/webhook) must be configured per admin user under Settings > Notifications; roles eligible: Admin, Viewer, DevOps, Helpdesk, Access Reviewer

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/) (referenced inline)
- Settings > Notifications (Admin Console)
- Twingate API (for custom auto-lock durations)
# Usage-based Auto-lock

## Summary
Auto-lock automatically revokes Resource access for users who haven't accessed it within a configured duration, enforcing least-privilege. Access can be restored via manual admin approval or automatic approval (user provides a reason). Configuration is available per-Resource or per-Group.

## Key Information
- Auto-lock is evaluated **per user**, even when configured at the Group level
- Duration options in Admin Console: **1, 7, 30, 60, or 90 days** (additional durations available via API)
- Configuration scope: Resource-level (applies to all users) or Group-level (overrides Resource default for that Group)
- Changes logged in **Access category** of audit logs
- Access summaries (CSV/report) downloadable from Resource, Group, or User pages

## Configuration Values
| Setting | Options |
|---|---|
| Auto-lock duration (UI) | 1, 7, 30, 60, 90 days |
| Auto-lock duration (API) | Any duration |
| Approval method | `MANUAL` or automatic |

## Step-by-Step

**From Resource page:**
1. Open Resource in Admin Console
2. Set auto-lock duration at Resource level (applies to all users)
3. Optionally override per-Group when adding or editing a Group's access

**From Group page:**
1. Open Group detail page
2. Set auto-lock duration and approval method per Resource

**Unlocking a user:**
1. Navigate to user's detail page in Admin Console
2. Unlock the specific locked Resource

## Webhook Payload Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL" | "AUTOMATIC",
  "request_duration_seconds": 2592000,
  "reason": "<user-provided>",
  "timestamp": "<ISO8601>",
  "tenant": "<tenant>.twingate.com",
  "request_id": "...",
  "user_name": "...",
  "resource_name": "..."
}
```

## Access Request Flow
- **Manual approval**: Locked user submits reason via block page → admin approves → access restored
- **Automatic approval**: Locked user submits reason → access restored immediately; reason recorded in analytics

## Notifications
- Configure at **Settings > Notifications**
- Email notifications toggleable per admin user (roles: Admin, DevOps, Support, Access Reviewer)
- Webhooks supported for workflow integrations
- Users notified by email when request is approved or denied

## Gotchas
- Group-level auto-lock **overrides** Resource-level; Groups inherit Resource config by default unless explicitly set
- Locking is per-user — one user being locked doesn't affect others in the same Group
- API allows durations beyond the 5 UI options; use API for custom intervals
- Auto-lock duration and last-unlock info only visible in downloaded access summary report, not directly in UI

## Related Docs
- Reviewing Access Requests
- Settings > Notifications
- Twingate API (for custom durations)
# Usage-based Auto-lock

## Summary
Automatically locks Resource access for users who haven't accessed it within a configured duration. Supports per-Resource and per-Group configuration with manual or automatic re-approval workflows. Enforces least-privilege by removing stale access.

## Key Information
- Auto-lock durations via Admin Console: **1, 7, 30, 60, or 90 days**
- Additional durations available via **API only**
- Locking is evaluated **per user**, even when configured at the Group level
- Configuration changes appear in **Access category** of audit logs
- Access summary reports downloadable from Resource, Group, or User pages

## Configuration Locations
- **Resource page** → applies to all users with access; can override per Group
- **Group page** → set per-Resource duration and approval method
- **Per-Group override on Resource** → set when adding Group or via options button on existing Group

## Approval Methods
| Method | Behavior on Lock |
|--------|-----------------|
| Manual | Admin must unlock; user submits request with reason via block page |
| Automatic | User provides reason; access restored immediately; reason logged |

## Unlocking Access
- Admins unlock via **user's detail page** in Admin Console
- Manual approval: admin must approve request submitted from block page
- Automatic approval: user self-serves with reason

## Access Tracking
Download access summary report (Resource/Group/User page) containing:
- Groups with access and policy used
- Expiration dates (if configured)
- Auto-lock duration
- Per-user lock status and last admin-unlock timestamp

## Notifications & Webhooks
Configure at **Settings > Notifications**. Email notifications toggleable per admin/DevOps/Support/Access Reviewer user.

**Webhook payload fields:**
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL" | "AUTOMATIC",
  "request_duration_seconds": <number>,
  "reason": "<user-provided string>",
  "user_name", "user_url", "resource_name", "resource_url",
  "request_id", "request_url", "requested_at", "timestamp",
  "tenant", "version"
}
```

## Gotchas
- Group-level auto-lock inherits Resource-level config by default; must explicitly override per Group
- Non-standard durations (outside 1/7/30/60/90 days) require API — not available in Admin Console
- Automatic approval still logs reason and records in analytics/resolved requests page
- Users receive email notification when request is approved or denied

## Related Docs
- Reviewing Access Requests
- Settings > Notifications (webhook configuration)
- Twingate API (for custom durations)
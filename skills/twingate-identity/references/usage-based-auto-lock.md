# Usage-Based Auto-Lock

## Summary
Automatically locks Resource access for users who haven't accessed a Resource within a configured duration. Supports manual or automatic approval for regaining access. Enforces least-privilege by removing stale access without admin intervention.

## Key Information
- Auto-lock is evaluated **per user**, even when configured at the Group level
- Duration options via Admin Console: **1, 7, 30, 60, or 90 days**; additional durations available via API
- Audit log changes appear in the **Access category** of audit logs
- Configuration can be set at Resource level (applies to all users) or overridden per Group

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate

## Configuration

### Via Admin Console
1. Navigate to a **Resource** or **Group** page
2. Set auto-lock duration (1/7/30/60/90 days)
3. Set approval method: **Manual** or **Automatic**
4. For Groups on a Resource: click the options button for an existing Group to modify duration and approval method

### Approval Methods
| Method | Behavior |
|--------|----------|
| Manual | Admin must unlock user access manually |
| Automatic | User provides reason; access restored immediately |

## Unlocking Access
- Admins unlock per-user from the **user's detail page** in Admin Console
- Manual approval: admin must approve request from block page submission
- Automatic approval: user submits reason on block page → immediate restore

## Tracking Access
Download access summary report from Resource, Group, or User page. Report includes:
- Groups with access and policy used
- Expiration dates
- Auto-lock duration
- Per-user lock status and last admin unlock time

## Notifications
- Configure at **Settings > Notifications**
- Email notifications toggleable per user for roles: Admin, DevOps, Support, Access Reviewer
- Webhook support available

### Webhook Payload Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL",          // or "AUTOMATIC"
  "request_duration_seconds": 2592000,
  "reason": "<user-provided string>",
  "request_id": "<base64>",
  "request_url": "<admin console URL>",
  "user_name": "...",
  "resource_name": "...",
  "timestamp": "<ISO8601>",
  "tenant": "<tenant>.twingate.com",
  "version": "1"
}
```

## Gotchas
- Group-level auto-lock inherits Resource-level config by default; must explicitly override per Group
- Locking is evaluated per user—one user in a Group being locked does not affect others
- Non-standard durations (e.g., 14 days) require API configuration; not available in Admin Console
- Locked users on automatic approval still have their reason and access details recorded in analytics

## Related Docs
- Reviewing Access Requests
- Settings > Notifications (webhook configuration)
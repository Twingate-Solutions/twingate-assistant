# Usage-based Auto-lock

## Summary
Automatically locks Resource access for users who haven't accessed it within a configured duration. Enforces least-privilege by removing stale access. Locking is evaluated per-user even when configured at the Group level.

## Key Information
- Auto-lock durations via Admin Console: **1, 7, 30, 60, or 90 days**; additional durations available via API
- Configurable at **Resource level** (applies to all users) or **Group level** (per Resource on Group detail page)
- Group-level config overrides Resource-level default; locking still evaluated per individual user
- Changes logged in **Access category** of audit logs
- Access summary reports downloadable from Resource, Group, or User pages

## Prerequisites
- Admin Console access
- Resources and Groups already configured
- Approval method chosen: **Manual** or **Automatic**

## Configuration Locations

### Resource Page
1. Open Resource → set auto-lock duration (applies to all users with access)
2. When adding a Group to a Resource → optionally specify Group-specific duration + approval method
3. For existing Group access → click options button on the Group → set duration and approval method

### Group Page
1. Open Group detail page → set auto-lock duration and approval method per Resource

## Approval Methods
| Method | Locked User Experience | Admin Action Required |
|--------|----------------------|----------------------|
| Manual | Submits request + reason via block page | Admin must approve |
| Automatic | Provides reason → access restored immediately | None (logged only) |

## Unlocking Access
- Admin unlocks via **user's detail page** in Admin Console
- Report fields include: lock status, last admin unlock date, expiration dates, auto-lock duration, Groups/policies

## Notifications
- Configure at **Settings > Notifications**
- Email notifications toggleable per admin user (roles: Admin, DevOps, Support, Access Reviewer)
- Webhook supported for workflow integration

## Webhook Payload Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL" | "AUTOMATIC",
  "request_duration_seconds": 2592000,
  "reason": "...",
  "user_name": "...",
  "resource_name": "...",
  "requested_at": "ISO8601",
  "request_url": "...",
  "tenant": "tenant.twingate.com"
}
```

## Gotchas
- Group inherits Resource-level config by **default**; must explicitly override at Group level if needed
- Manual approval requires admin action even for automatic-approval policies when auto-lock triggers — check approval method is set correctly per use case
- Approved/denied requests trigger **email notifications to users**; ensure notification settings are configured before enabling

## Related Docs
- Reviewing Access Requests
- Settings > Notifications
- Twingate API (for custom auto-lock durations beyond Admin Console options)
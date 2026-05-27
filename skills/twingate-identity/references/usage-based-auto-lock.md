# Usage-Based Auto-Lock

## Summary
Auto-lock removes user access to a Resource if they haven't accessed it within a configured duration, supporting least-privilege access. Access recovery depends on the approval method configured (manual admin unlock or automatic with reason). Configuration is available via Admin Console or API.

## Key Information
- Auto-lock operates **per-user**, even when configured at the Group level
- Duration options in Admin Console: **1, 7, 30, 60, or 90 days**; arbitrary durations possible via API
- Configurable from **Resource page** (applies to all users) or **Group page** (per-resource granularity)
- Groups inherit Resource-level auto-lock by default; can be overridden per-group
- Changes logged in **Audit Logs > Access category**

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate

## Configuration Steps

### Via Resource Page
1. Navigate to the Resource page
2. When adding a Group, specify auto-lock duration and approval method
3. To modify existing Group access: click the options button for the Group → set duration and approval method

### Via Group Page
1. Navigate to the Group page
2. Set auto-lock duration and approval method for specific Resources the Group can access

## Configuration Values

| Parameter | Options | Notes |
|-----------|---------|-------|
| `auto_lock_duration` | 1, 7, 30, 60, 90 days (UI); any value (API) | Per resource-group access right |
| `approval_mode` | `MANUAL`, automatic | Manual = admin unlock required; automatic = user provides reason |

### Webhook Payload Fields (ACCESS_REQUEST event)
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL",
  "reason": "<user-provided string>",
  "request_duration_seconds": 2592000,
  "user_name", "user_url", "resource_name", "resource_url",
  "request_id", "request_url", "timestamp", "tenant", "version"
}
```

## Unlocking & Tracking Access
- **Unlock**: Admin navigates to specific user's detail page
- **Reports**: Downloadable from Resource, Group, or User page; includes group access, policy, expiration dates, auto-lock duration, lock status, last admin unlock date
- **Notifications**: Configure in Settings > Access Requests; target roles: Admins, DevOps, or Access Reviewers; can disable email and use webhook instead

## Gotchas
- Auto-lock is enforced **per-user**, not per-group — one user being locked does not affect others in the same group
- Automatic approval still requires a reason from the user and logs it in analytics
- Webhook must be configured manually if email notifications are disabled; no default fallback
- Modifying auto-lock duration affects all users under that configuration going forward

## Related Docs
- Reviewing Access Requests
- Audit Logs
- Access Requests notifications/webhooks settings
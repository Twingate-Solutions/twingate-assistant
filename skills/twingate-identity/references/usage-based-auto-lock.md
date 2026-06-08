# Usage-based Auto-lock

## Summary
Automatically locks Resource access for users who haven't accessed it within a configured duration, enforcing least-privilege. Locking is evaluated per user. Regaining access depends on whether the approval method is manual or automatic.

## Key Information
- Auto-lock durations via Admin Console: **1, 7, 30, 60, or 90 days**; additional durations available via API
- Locking is **per user**, even when configured at the Group level
- Configuration can be set at the **Resource level** (applies to all users) or overridden per **Group-Resource pairing**
- Audit log changes appear under the **Access** category
- Access summary reports (CSV) downloadable from Resource, Group, or User pages

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate

## Configuration Steps
1. **Resource-level**: Open Resource page → set auto-lock duration (applies to all users with access)
2. **Group override on Resource**: When adding a Group to a Resource, specify a custom duration; existing Groups can be modified via the options button
3. **From Group page**: Open Group detail page → set duration and approval method per Resource

## Approval Methods
| Method | Behavior on Lock |
|---|---|
| Manual | Admin must unlock user from user's detail page |
| Automatic | User submits reason → access restored immediately |

## Unlocking Access
- Admins unlock from **user's detail page** in Admin Console
- Manual approval: admin must approve access request submitted via block page
- Automatic approval: user provides reason on block page; access restored instantly; reason logged in analytics and resolved requests page

## Tracking / Reporting
Download access summary from Resource, Group, or User page. Report includes:
- Groups with access and policy type
- Expiration dates (if set)
- Auto-lock duration
- Per-user lock status and last admin unlock timestamp

## Notifications
- Configure at **Settings > Notifications**
- Email notifications toggleable per user for roles: Admin, DevOps, Support, Access Reviewer
- Webhook support available

### Webhook Payload Key Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL",
  "request_duration_seconds": 2592000,
  "reason": "...",
  "user_name": "...",
  "resource_name": "..."
}
```

## Gotchas
- Admin Console limits durations to 5 preset values; use the **API for custom durations**
- Auto-lock configured at Resource level is the default; Group-level settings **override** it per Group
- Automatic approval still logs the reason and request details — not invisible to admins
- Users receive email notification when request is approved or denied

## Related Docs
- Reviewing Access Requests
- Settings > Notifications
- Twingate API (for custom auto-lock durations)
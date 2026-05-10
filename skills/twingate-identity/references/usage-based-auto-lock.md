# Usage-based Auto-lock

## Summary
Usage-based auto-lock automatically removes Resource access for users who haven't accessed it within a configured time period. Access can be regained through manual admin approval or automatic approval with a user-provided reason. Changes are tracked in Audit Logs under the Access category.

## Key Information
- Auto-lock operates **per-user**, even when configured at Group level
- Duration options via Admin Console: **1, 7, 30, 60, or 90 days**
- Additional durations available via **API only**
- Groups inherit Resource-level auto-lock by default; can be overridden per Group
- Locked users appear on the user's detail page; admins unlock from there
- Access reports downloadable from Resource, Group, or User pages

## Configuration Locations
- **Resource page**: Sets default for all Groups/users on that Resource
- **Group page**: Override duration/approval for specific Resources per Group

## Approval Modes
| Mode | Locked User Experience | Admin Action Required |
|------|----------------------|----------------------|
| Manual | Submit request + reason via block page | Admin must unlock |
| Automatic | Submit reason, access granted immediately | None (reason logged) |

## Notifications Configuration
- Configured in **Settings → Access Requests**
- Choose which admin roles receive email: Admins, DevOps, or Access Reviewers
- Can disable emails and use **webhook** instead

### Webhook Payload Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL" | "AUTOMATIC",
  "request_duration_seconds": 2592000,
  "reason": "<user-provided string>",
  "resource_name": "...",
  "user_name": "...",
  "request_url": "...",
  "timestamp": "<ISO8601>",
  "tenant": "<tenant>.twingate.com"
}
```

## Access Reports Include
- Groups with access and their policy
- Expiration dates (if set)
- Auto-lock duration configured
- Per-user lock status and last admin-unlock date

## Gotchas
- Changing auto-lock duration affects **future** lock calculations; review existing access when modifying
- Automatic approval still logs the reason—not fully frictionless from an audit standpoint
- Per-user locking means users in the same Group may have different lock states
- Admin Console limits durations to 5 preset values; use API for custom durations

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- Audit Logs (Admin Console → Access category)
- Twingate API (for custom auto-lock durations)
# Usage-Based Auto-Lock

## Summary
Auto-lock removes user access to a Resource after a configured period of inactivity, supporting least-privilege access. Access can be restored via manual admin approval or automatic approval (with user-provided reason). Configuration is available via Admin Console or API.

## Key Information
- Auto-lock operates **per-user**, even when configured at the Group level
- Admin Console durations: **1, 7, 30, 60, or 90 days**; arbitrary durations available via API
- Changes logged in **Audit Logs > Access category**
- Unlocking: admins unlock via the specific user's detail page
- Reports downloadable from Resource, Group, or User pages

## Configuration Locations
| Location | Scope |
|---|---|
| Resource page | Applies to all users with access; Groups inherit Resource-level setting by default |
| Group page | Set per-Resource duration and approval method for that Group |

## Approval Modes
- **Manual**: Admin must explicitly unlock access; locked users can submit request with reason via block page
- **Automatic**: User submits reason, immediately regains access; reason captured in analytics and resolved requests page

## Notifications Configuration
- Configure in **Settings > Access Requests**
- Choose which admin roles receive email: Admins, DevOps, or Access Reviewers
- Option to disable emails and use webhook instead

## Webhook Payload Fields
```json
{
  "type": "ACCESS_REQUEST",
  "request_type": "AutoLock",
  "approval_mode": "MANUAL" | "AUTOMATIC",
  "request_duration_seconds": 2592000,
  "reason": "<user-provided string>",
  "user_name", "user_url",
  "resource_name", "resource_url",
  "request_id", "request_url",
  "timestamp", "tenant", "version"
}
```

## Tracking / Reports
Downloaded report includes:
- Groups with access and their policy
- Expiration dates (if set)
- Auto-lock duration
- Per-user lock status and last admin-unlock timestamp

## Gotchas
- Group-level auto-lock duration can be **overridden per Group** on the Resource page; new Groups inherit Resource default
- Duration changes only available beyond the 5 preset values via **API** (not Admin Console)
- Users notified by email on approval/denial; admins notified per role configuration
- Webhook and email notifications are mutually exclusive (disabling emails routes to webhook only)

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- Twingate API (for custom auto-lock durations)
- Audit Logs (Admin Console > Access category)
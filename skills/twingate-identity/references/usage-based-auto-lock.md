# Usage-Based Auto-Lock

## Summary
Auto-lock automatically revokes Resource access for users who haven't accessed it within a configured duration, enforcing least-privilege. Access can be restored via manual admin approval or automatic approval (user provides reason). Configuration is available per-Resource or per-Group.

## Key Information
- Auto-lock evaluated **per user**, even when configured at the Group level
- Durations via Admin Console: **1, 7, 30, 60, or 90 days**; additional durations available via API
- Two approval modes: **Manual** (admin unlocks) or **Automatic** (user provides reason, immediately restored)
- Audit log changes appear in the **Access** category
- Access summary reports downloadable from Resource, Group, or User pages

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate

## Configuration

### Resource-Level (applies to all users with access)
1. Navigate to the Resource page in Admin Console
2. Set auto-lock duration directly on the Resource
3. When adding a Group, optionally specify a Group-level override duration
4. To modify existing Group access: click options button → set duration and approval method

### Group-Level
1. Navigate to the Group detail page
2. Set auto-lock duration and approval method per Resource

## Unlocking Access
- Admins unlock via the **user's detail page** in Admin Console
- Manual approval: admin must approve locked user's request
- Automatic approval: user submits reason on block page → access restored immediately

## Tracking Access (Access Summary Report)
Download from Resource, Group, or User page. Report includes:
- Groups with access and policy used
- Expiration dates (if configured)
- Auto-lock duration
- Per-user lock status and last admin unlock timestamp

## Notifications
- Configure at **Settings → Notifications**
- Email notifications toggleable per user for roles: Admin, DevOps, Support, Access Reviewer
- Webhook support for workflow integration

### Webhook Payload Fields (`type: ACCESS_REQUEST`)
| Field | Description |
|---|---|
| `request_type` | `"AutoLock"` for auto-lock events |
| `approval_mode` | `"MANUAL"` or `"AUTOMATIC"` |
| `request_duration_seconds` | Requested access duration |
| `reason` | User-provided reason |
| `resource_name` / `resource_url` | Affected resource |
| `user_name` / `user_url` | Requesting user |

## Gotchas
- Group-level duration **inherits** Resource-level config by default; must explicitly override
- Automatic approval still logs reason and records in analytics/resolved requests page
- API supports durations beyond the 5 Admin Console options — use API for custom intervals
- Users see a **block page** when locked; manual approval requires admin action before access resumes

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- Settings → Notifications (webhook configuration)
- Audit Logs → Access category
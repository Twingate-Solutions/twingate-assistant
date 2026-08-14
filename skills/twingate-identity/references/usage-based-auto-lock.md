---
source: https://www.twingate.com/docs/usage-based-auto-lock
type: docs
fetched: 2026-08-14
source_version: 74ce6b345c16a3fbfa36a099fc87736c86fd230d16bcde0b6d0c4c1c287cacce
---

# Usage-based Auto-lock

## Summary
Automatically locks Resource access for users who haven't accessed a Resource within a configured duration. Supports manual or automatic approval workflows for regaining access. Helps enforce least-privilege by removing stale access without manual auditing.

## Key Information
- Auto-lock is evaluated **per user**, even when configured at the Group level
- Duration options via Admin Console: **1, 7, 30, 60, or 90 days**; additional durations available via API
- Configuration scopes: Resource-level (applies to all users), Group-level override (per Group on a Resource), or from Group detail page
- Audit log changes appear in the **Access** category
- Access summary reports downloadable from Resource, Group, or User pages

## Prerequisites
- Admin Console access
- Resources and Groups already configured in Twingate
- Admin, DevOps, Helpdesk, Support, or Access Reviewer role for notification management

## Configuration

### From Resource Page
1. Navigate to Resource → configure auto-lock duration (applies to all users)
2. When adding a Group: specify Group-level duration to override Resource default
3. For existing Group access: click options button → set duration and approval method

### From Group Page
1. Navigate to Group detail page
2. Set auto-lock duration and approval method per Resource

### Approval Methods
| Method | Behavior on Lock |
|---|---|
| Manual | Admin must unlock via user's detail page |
| Automatic | User provides reason → access restored immediately |

## Unlocking Access
- Admins unlock via **user's detail page** in Admin Console
- Manual approval: admin must approve access request from block page submission
- Automatic approval: user submits reason on block page → instant restoration

## Configuration Values

### Webhook Payload Fields (`type: ACCESS_REQUEST`)
| Field | Description |
|---|---|
| `request_type` | `"AutoLock"` for auto-lock triggered requests |
| `approval_mode` | `"MANUAL"` or `"AUTOMATIC"` |
| `request_duration_seconds` | Duration of requested access |
| `reason` | User-submitted reason string |
| `request_id` | Unique request identifier |
| `resource_url` / `user_url` | Deep links to Admin Console entities |

### Notification Settings
- Path: **Settings → Notifications**
- Toggle email per user per role (Admin, DevOps, Helpdesk, Support, Access Reviewer)
- Webhook integration supported

## Gotchas
- Group-level duration **overrides** Resource-level; default is to inherit Resource config
- Locking is per-user, not per-group — a group setting locks individual members independently
- Automatic approval still logs reason and access details to analytics and resolved requests page
- API supports durations beyond the 5 Admin Console options — use API for custom intervals
- Users receive email notification when request is approved **or denied**

## Access Summary Report Contents
- Groups with access + policy used
- Expiration dates (if configured)
- Auto-lock duration
- Per-user: current lock status, last admin unlock date

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/) — reviewing locked-out user requests
- Settings → Notifications — webhook and email configuration
- Audit Logs (Access category) — configuration change history
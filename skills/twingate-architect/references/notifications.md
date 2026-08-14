---
source: https://www.twingate.com/docs/notifications
type: docs
fetched: 2026-08-14
source_version: 2145ea13bc6d4e053528f451790a3a3d4e4fc27798d0f20dca87e3958298016b
---

# Twingate Notifications

## Summary
Twingate provides configurable notification channels (email and webhooks) for admin alerts. Some notifications are fixed (subscription updates, end-user notifications sent to all admins via email); others are customizable per recipient and delivery method.

## Key Information
- Fixed notifications always go to all admin emails; cannot be customized
- Customizable notifications support: specific email addresses, webhooks, or both
- Granular control: configure per-channel (which notifications a channel receives) or per-notification (which channels receive it)
- Webhook test payloads can be sent directly from Admin Console
- **Slack**: Use Workflow Builder, not Incoming Webhooks (Incoming Webhooks only supports plain text JSON)

## Prerequisites
- Admin access to Twingate Admin Console
- For webhooks: an endpoint that accepts HTTP POST requests with standard JSON payloads

## Step-by-Step: Configure Notifications
1. Navigate to **Settings** in the Admin Console
2. **Email**: Select an admin email address → choose which notifications it receives
3. **Webhook**: Provide webhook name + URL → select notifications to route to it
4. Use **Test Payload** button per notification to validate webhook delivery

## Webhook Configuration Requirements
- Must accept **POST** requests (GET-only endpoints will error)
- Must accept standard JSON payloads
- Endpoint must respond without error to Twingate's payload format

## Webhook Payload Fields

### Common Fields (all payloads)
| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 UTC timestamp |
| `tenant` | Twingate tenant URL |
| `version` | Payload version (currently `"1"`) |
| `type` | Notification type identifier |

### Notification Types & Key Fields
| `type` | Notable Fields |
|--------|---------------|
| `ACCESS_REQUEST` | `request_id`, `user_name`, `resource_name`, `approval_mode`, `request_type` (`AutoLock` or `AccessRequest`), `request_duration_seconds`, `reason` |
| `CLIENT_UPDATE_RECOMMENDED` | `platform`, `devices_list` (URL) |
| `CLIENT_UPDATE_REQUIRED` | `message`, `table` |
| `CONNECTOR_UPGRADE_AVAILABLE` | `message`, `table` |
| `CONNECTOR_STATUS_OFFLINE` | `message`, `table` |
| `CONNECTOR_STATUS_ONLINE` | `message`, `table` |
| `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` | `integration`, `days_remaining`, `manage_integration` |
| `EVENTS_SYNC_ERRORS` | `message`, `manage_sync` |
| `EVENTS_SYNC_ERROR_RESOLVED` | `sync_type`, `manage_sync` |
| `EVENTS_SYNC_REQUIRES_ATTENTION` | `sync_type`, `manage_sync` |
| `GOOGLE_WORKSPACE_SYNC_ERROR` | `message`, `message_integration` |
| `IDENTITY_PROVIDER_INTEGRATION_ERROR` | `integration`, `manage_integration` |
| `INTEGRATION_ERROR_RESOLVED` | `integration`, `manage_integration` |
| `INTEGRATION_ERRORS` | `integration`, `manage_integration` |
| `SERVICE_ACCOUNT_KEYS_EXPIRATION` | `table[]` with `service_account_name`, `service_key`, `link` |

## Gotchas
- Slack Incoming Webhooks will fail — use Slack Workflow Builder instead
- Webhook errors = your endpoint returned an error, not a Twingate-side issue
- `table` field is an empty array `[]` in test payloads for some notification types
- `ACCESS_REQUEST` type covers both JIT and Usage-based requests; differentiate via `request_type` field (`AccessRequest` vs `AutoLock`)

## Related Docs
- Access Requests (JIT and Usage-based)
- Device Integrations settings
- Connector management
- Service Accounts
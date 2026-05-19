# Twingate Notifications

## Summary
Twingate provides configurable notification channels for admin alerts, supporting both email and webhook delivery. Admins can assign specific notifications to specific recipients/webhooks. Some notifications (subscription updates, end-user notifications) are always sent to all admins via email and cannot be customized.

## Key Information
- Notification settings managed under **Settings > Admin Console**
- Two delivery methods: **email** (to specific addresses) or **webhook** (POST requests with JSON payloads)
- Configuration can be done by channel (select recipient, choose notifications) or by notification (select notification, choose recipients)
- Webhooks require: name, URL, and selected notification types
- Test payloads can be sent directly from Admin Console
- For Slack: use **Workflow Builder**, not Incoming Webhooks (Incoming Webhooks reject standard JSON)

## Webhook Requirements
- Endpoint must accept **POST** requests
- Endpoint must accept standard **JSON** payloads
- Slack Incoming Webhooks are incompatible; use Slack Workflow Builder instead

## Webhook Payload Types & Fields

| Type | Key Fields |
|------|-----------|
| `ACCESS_REQUEST` | `request_id`, `user_name`, `resource_name`, `approval_mode`, `request_type` (`AutoLock` or `AccessRequest`), `request_duration_seconds`, `reason` |
| `CLIENT_UPDATE_RECOMMENDED` | `platform`, `devices_list` |
| `CLIENT_UPDATE_REQUIRED` | `message`, `table` |
| `CONNECTOR_UPGRADE_AVAILABLE` | `message`, `table` |
| `CONNECTOR_STATUS_OFFLINE` | `message`, `table` |
| `CONNECTOR_STATUS_ONLINE` | `message`, `table` |
| `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` | `integration`, `days_remaining`, `manage_integration` |
| `EVENTS_SYNC_ERRORS` | `message`, `manage_sync` |
| `EVENTS_SYNC_ERROR_RESOLVED` | `sync_type`, `message`, `manage_sync` |
| `EVENTS_SYNC_REQUIRES_ATTENTION` | `sync_type`, `message`, `manage_sync` |
| `GOOGLE_WORKSPACE_SYNC_ERROR` | `message`, `message_integration` |
| `IDENTITY_PROVIDER_INTEGRATION_ERROR` | `integration`, `message`, `manage_integration` |
| `INTEGRATION_ERROR_RESOLVED` | `integration`, `message`, `manage_integration` |
| `INTEGRATION_ERRORS` | `integration`, `message`, `manage_integration` |
| `SERVICE_ACCOUNT_KEYS_EXPIRATION` | `table[]` with `service_account_name`, `service_key`, `link` |

All payloads include: `timestamp`, `tenant`, `version`, `type`

## Gotchas
- Slack Incoming Webhooks will reject Twingate's standard JSON — use Workflow Builder instead
- Webhook endpoint must support POST (GET-only endpoints will error)
- Subscription and end-user notifications cannot be customized; always go to all admins
- `CLIENT_UPDATE_REQUIRED` and `CONNECTOR_*` payloads include a `table` array field (may be empty in test payloads)

## Related Docs
- Access Requests (JIT/Usage-based)
- Device Integrations
- Events Sync configuration
- Service Accounts
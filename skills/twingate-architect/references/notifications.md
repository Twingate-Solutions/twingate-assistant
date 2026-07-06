# Twingate Notifications

## Summary
Twingate provides granular notification controls for admins, supporting both email and webhook delivery channels. Some notifications (subscription updates, end-user notifications) are always emailed to all admins; others can be routed to specific recipients or webhooks.

## Key Information
- Notifications managed in **Admin Console → Settings**
- Two delivery methods: email (specific addresses) or webhook (URL-based)
- Can configure by channel (which notifications go to a recipient) or by notification (which recipients get a specific notification)
- Webhook testing available via "Test Payload" button in Admin Console
- All webhooks receive **POST requests** with **JSON payloads**
- Use **Slack Workflow Builder** (not Incoming Webhooks) for Slack integration

## Prerequisites
- Admin access to Twingate Admin Console
- Webhook endpoint must accept HTTP POST with standard JSON

## Webhook Configuration
Required fields:
- Webhook name
- Webhook URL
- Selected notification types

## Webhook Payload Types & Key Fields

| Type | `type` value | Notable fields |
|------|-------------|----------------|
| Usage-based Access Request | `ACCESS_REQUEST` | `request_type: "AutoLock"`, `approval_mode`, `request_duration_seconds` |
| JIT Access Request | `ACCESS_REQUEST` | `request_type: "AccessRequest"`, `reason`, `user_url`, `resource_url` |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` | `platform`, `devices_list` |
| Client update required | `CLIENT_UPDATE_REQUIRED` | `table` |
| Connector upgrade available | `CONNECTOR_UPGRADE_AVAILABLE` | `table` |
| Connectors offline | `CONNECTOR_STATUS_OFFLINE` | `table` |
| Connectors online | `CONNECTOR_STATUS_ONLINE` | `table` |
| Device integration API token expiry | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` | `integration`, `days_remaining`, `manage_integration` |
| Events sync errors | `EVENTS_SYNC_ERRORS` | `message`, `manage_sync` |
| Events sync resolved | `EVENTS_SYNC_ERROR_RESOLVED` | `sync_type`, `manage_sync` |
| Events sync needs attention | `EVENTS_SYNC_REQUIRES_ATTENTION` | `sync_type`, `manage_sync` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` | `message_integration` |
| IdP integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` | `integration`, `manage_integration` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` | `integration`, `manage_integration` |
| Integration errors | `INTEGRATION_ERRORS` | `integration`, `manage_integration` |
| Service account key expiry | `SERVICE_ACCOUNT_KEYS_EXPIRATION` | `table[].service_account_name`, `table[].service_key`, `table[].link` |

## Common Payload Fields
All payloads include: `timestamp` (ISO 8601), `tenant`, `version: "1"`, `type`

## Gotchas
- Webhook endpoint **must accept POST** — GET-only endpoints will error
- Slack Incoming Webhooks reject standard JSON; use Slack Workflow Builder instead
- Fixed notifications (subscription/end-user) cannot be customized — always go to all admins
- `table` field appears as empty array `[]` in test payloads for some notification types

## Related Docs
- Access Requests (JIT/Usage-based)
- Connector management
- Device integrations
- Service accounts
- Events sync configuration
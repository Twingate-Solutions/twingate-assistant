# Twingate Notifications

## Summary
Twingate provides configurable notification channels for admins, supporting both email and webhook delivery. Some notifications (subscription updates, end-user notifications) are mandatory to all admins; others can be routed to specific recipients or webhooks.

## Key Information
- **Fixed notifications**: Subscription updates and end-user notifications always go to all admin emails
- **Configurable notifications**: Can be sent to specific email addresses or webhooks
- **Management location**: Settings section of Admin Console
- **Dual configuration modes**: By channel (email/webhook) or by notification type
- **Test capability**: "Test Payload" button sends sample payloads to configured webhook URL
- **Slack**: Use Workflow Builder, not Incoming Webhooks (Incoming Webhooks only supports plain text JSON)

## Prerequisites
- Admin access to Twingate Admin Console
- Webhook endpoint that accepts HTTP POST requests with standard JSON

## Webhook Configuration
Required fields:
- Webhook name
- Webhook URL
- Selected notification types

Endpoint requirements:
- Must accept **POST** requests
- Must accept standard JSON payloads

## Webhook Payload Types & Key Fields

| Type | `type` value | Notable Fields |
|------|-------------|----------------|
| Usage-based Access Request | `ACCESS_REQUEST` | `request_type: "AutoLock"`, `request_duration_seconds` |
| JIT Access Request | `ACCESS_REQUEST` | `request_type: "AccessRequest"`, `approval_mode` |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` | `platform`, `devices_list` |
| Client update required | `CLIENT_UPDATE_REQUIRED` | `table` |
| Connector upgrade available | `CONNECTOR_UPGRADE_AVAILABLE` | `table` |
| Connectors offline | `CONNECTOR_STATUS_OFFLINE` | `message` |
| Connectors online | `CONNECTOR_STATUS_ONLINE` | `message` |
| Device integration token expiration | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` | `integration`, `days_remaining` |
| Events sync errors | `EVENTS_SYNC_ERRORS` | `manage_sync` |
| Events sync resolved | `EVENTS_SYNC_ERROR_RESOLVED` | `sync_type` |
| Events sync attention | `EVENTS_SYNC_REQUIRES_ATTENTION` | `sync_type` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` | `message_integration` |
| IdP integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` | `integration` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` | `integration` |
| Integration errors | `INTEGRATION_ERRORS` | `integration` |
| Service account key expiration | `SERVICE_ACCOUNT_KEYS_EXPIRATION` | `table[].service_account_name`, `table[].service_key` |

## Common Payload Fields
All payloads include: `timestamp`, `tenant`, `version: "1"`, `type`

## Gotchas
- Slack Incoming Webhooks will **reject** Twingate payloads—use Slack Workflow Builder instead
- GET-only endpoints will error; endpoint **must** support POST
- Default behavior lists all admin emails; explicit selection required to restrict recipients
- `CLIENT_UPDATE_REQUIRED` and `CONNECTOR_UPGRADE_AVAILABLE` use a `table` array that may be empty in test payloads

## Related Docs
- Access Requests (JIT/Usage-based)
- Device Integrations
- Connector management
- Events sync (S3)
---
source: https://www.twingate.com/docs/notifications
type: docs
fetched: 2026-09-20
source_version: f1ebe6488ffc4e0db383775e29a88b0cfc4142f382f6d49e376d8535b2a6aeee
---

# Twingate Notifications

## Summary
Twingate provides granular notification controls for admins, supporting both email and webhook delivery. Some notifications (subscription updates, end-user notifications) are always emailed to all admins; others can be customized per recipient and channel. Webhooks enable integration with external workflows and automation platforms.

## Key Information
- **Always-email notifications**: Subscription updates, end-user notifications → sent to all admins automatically
- **Configurable notifications**: Can target specific email addresses or webhooks
- **Management location**: Admin Console → Settings
- **Test capability**: "Test Payload" button sends sample payload to configured webhook URL
- **Webhook method**: Must accept `POST` requests with standard JSON
- Notifications can be managed by channel (configure per email/webhook) OR by notification type (configure per event)

## Notification Types (Webhook-Supported)
| Type Field | Description |
|---|---|
| `ACCESS_REQUEST` | Usage-based (AutoLock) or JIT access requests |
| `CLIENT_UPDATE_RECOMMENDED` / `CLIENT_UPDATE_REQUIRED` | Client version alerts |
| `CONNECTOR_UPGRADE_AVAILABLE` | Connector version alerts |
| `CONNECTOR_STATUS_OFFLINE` / `CONNECTOR_STATUS_ONLINE` | Connector status changes |
| `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` | Device integration token expiry |
| `EVENTS_SYNC_ERRORS` / `EVENTS_SYNC_ERROR_RESOLVED` / `EVENTS_SYNC_REQUIRES_ATTENTION` | Event sync status |
| `GOOGLE_WORKSPACE_SYNC_ERROR` | Google Workspace sync issues |
| `IDENTITY_PROVIDER_INTEGRATION_ERROR` | IdP integration errors |
| `INTEGRATION_ERROR_RESOLVED` / `INTEGRATION_ERRORS` | General integration status |
| `SERVICE_ACCOUNT_KEYS_EXPIRATION` | Service account key expiry |

## Webhook Payload Common Fields
```json
{
  "timestamp": "ISO8601",
  "tenant": "yourco.twingate.com",
  "version": "1",
  "type": "NOTIFICATION_TYPE"
}
```
- `table` field (array of structured data) appears in: Service Account key expiration, Connector status, Client updates

## Configuration Values
- **Webhook configuration requires**: name, URL, selected notification types
- **HTTP method**: POST (required)
- **Content-Type**: Standard JSON

## Gotchas
- **Slack Incoming Webhooks**: Only support plain-text JSON → use Slack Workflow Builder instead
- **`table` field incompatibility**: Notifications containing `table` arrays cannot be ingested directly by Slack (either incoming webhooks or Workflow Builder) → requires middleware (serverless function, Zapier, Make) to transform before forwarding
- **Webhook errors**: Usually caused by wrong HTTP method (GET instead of POST) or service rejecting standard JSON format

## Prerequisites
- Admin role on Twingate account
- Webhook endpoint must: accept POST requests, handle standard JSON payloads

## Step-by-Step: Configure Webhook
1. Navigate to Admin Console → Settings → Notifications
2. Add webhook with name + URL
3. Select specific notification types to route to it
4. Click "Test Payload" to validate connectivity

## Related Docs
- Access Requests (JIT/Usage-based)
- Service Accounts
- Connector management
- Device integrations
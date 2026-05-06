# Twingate Notifications

## Summary
Twingate provides configurable notification channels for admins, supporting both email and webhook delivery. Some notifications (subscription updates, end-user notifications) are always sent to all admins via email. Other notifications support granular per-recipient and per-channel configuration.

## Key Information
- Notification settings managed in **Admin Console → Settings**
- Two delivery methods: **email** (specific addresses) or **webhook** (URL-based)
- Can configure by channel (which notifications a recipient gets) or by notification (which recipients get a specific notification)
- Webhook test payload button available in Admin Console
- All webhook payloads are POST requests with standard JSON

## Prerequisites
- Admin access to Twingate Admin Console
- For webhooks: an endpoint that accepts HTTP POST with standard JSON body

## Step-by-Step: Configure Webhook
1. Go to **Settings** in Admin Console
2. Add webhook with: name, URL, and selected notification types
3. Use **Test Payload** button to validate endpoint connectivity

## Webhook Payload Fields (Common)
| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 UTC timestamp |
| `tenant` | Account domain |
| `version` | Payload version (`"1"`) |
| `type` | Notification type identifier |

## Notification Types & `type` Values
| Notification | `type` Value |
|---|---|
| Usage-based Access Request | `ACCESS_REQUEST` (request_type: `AutoLock`) |
| JIT Access Request | `ACCESS_REQUEST` (request_type: `AccessRequest`) |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` |
| Client update required | `CLIENT_UPDATE_REQUIRED` |
| Connector update available | `CONNECTOR_UPGRADE_AVAILABLE` |
| Connectors offline | `CONNECTOR_STATUS_OFFLINE` |
| Connectors online | `CONNECTOR_STATUS_ONLINE` |
| Device integration token expiring | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` |
| Events sync errors | `EVENTS_SYNC_ERRORS` |
| Events sync resolved | `EVENTS_SYNC_ERROR_RESOLVED` |
| Events sync attention needed | `EVENTS_SYNC_REQUIRES_ATTENTION` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` |
| IdP integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` |
| Integration errors | `INTEGRATION_ERRORS` |
| Service account key expiration | `SERVICE_ACCOUNT_KEYS_EXPIRATION` |

## Gotchas
- **Slack Incoming Webhooks** do not work — use **Slack Workflow Builder** instead (Incoming Webhooks only accept plain text JSON, not standard payloads)
- Webhook endpoint must accept **POST** requests; GET-only endpoints will error
- Subscription and end-user notifications are **always** sent to all admins via email — not configurable

## Related Docs
- Access Requests (JIT/Usage-based)
- Device Integrations
- Connector Management
- Events Sync (S3)
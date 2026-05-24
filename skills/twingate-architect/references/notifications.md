# Twingate Notifications

## Summary
Twingate provides granular notification controls for admins, supporting both email and webhook delivery channels. Admins can configure which recipients (email addresses or webhooks) receive specific notification types via the Admin Console Settings.

## Key Information
- Some notifications (subscription updates, end-user notifications) are **always** sent via email to all admins — not configurable
- Configurable notifications support: specific email addresses, webhooks, or both
- Notifications can be managed by channel (who gets what) or by notification type (which channels receive it)
- Webhook test payloads can be sent directly from Admin Console
- **Use Slack Workflow Builder** instead of Slack Incoming Webhooks (incoming webhooks only support plain text JSON)

## Prerequisites
- Admin access to Twingate Admin Console
- For webhooks: an endpoint that accepts HTTP POST requests with standard JSON payloads

## Configuration Steps
1. Navigate to **Settings** in Admin Console
2. For email: select an email address → choose which notifications it receives
3. For webhook: provide webhook name, URL, and select target notifications
4. Use **Test Payload** button to validate webhook endpoint

## Webhook Payload Structure

All payloads share common fields:
| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 datetime |
| `tenant` | Account domain |
| `version` | Payload schema version (`"1"`) |
| `type` | Notification type identifier |

## Notification Types & `type` Values
| Notification | `type` Value |
|---|---|
| Usage-based Access Request | `ACCESS_REQUEST` (request_type: `AutoLock`) |
| JIT Access Request | `ACCESS_REQUEST` (request_type: `AccessRequest`) |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` |
| Client update required | `CLIENT_UPDATE_REQUIRED` |
| Connector update available | `CONNECTOR_UPGRADE_AVAILABLE` |
| Connector offline | `CONNECTOR_STATUS_OFFLINE` |
| Connector online | `CONNECTOR_STATUS_ONLINE` |
| Device integration token expiring | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` |
| Events sync errors | `EVENTS_SYNC_ERRORS` |
| Events sync error resolved | `EVENTS_SYNC_ERROR_RESOLVED` |
| Events sync requires attention | `EVENTS_SYNC_REQUIRES_ATTENTION` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` |
| IdP integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` |
| Integration errors | `INTEGRATION_ERRORS` |
| Service account key expiration | `SERVICE_ACCOUNT_KEYS_EXPIRATION` |

## Gotchas
- Webhook endpoints **must accept POST requests** — GET-only endpoints will error
- Webhook payload must be standard JSON — some services (e.g., Slack Incoming Webhooks) reject this format
- `ACCESS_REQUEST` type is reused for both JIT and usage-based requests; differentiate via `request_type` field (`AccessRequest` vs `AutoLock`)
- Default email list includes all admin addresses; can be scoped per notification

## Related Docs
- Access Requests (JIT/Usage-based)
- Device Integrations
- Connector management
- Events sync configuration
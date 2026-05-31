# Twingate Notifications

## Summary
Twingate provides granular notification controls for admins, supporting both email and webhook delivery channels. Admins can configure which recipients/webhooks receive specific notification types via the Admin Console Settings section.

## Key Information
- Some notifications (subscription updates, end-user notifications) are **always** sent via email to all admins — not configurable
- Configurable notifications support: specific email addresses or webhooks
- Notifications can be managed from two perspectives: by channel (who gets what) or by notification type (what goes where)
- Webhook testing available directly in Admin Console via "Test Payload" button
- All webhook payloads use `POST` method with standard JSON

## Prerequisites
- Admin access to Twingate Admin Console
- Webhook endpoint that accepts `POST` requests and standard JSON

## Step-by-Step: Configure Webhook
1. Navigate to **Settings** in the Admin Console
2. Add webhook: provide name, URL, and select notification types
3. Use "Test Payload" to validate the endpoint

## Webhook Payload Structure (Common Fields)
All payloads include:
- `timestamp` — ISO 8601 UTC
- `tenant` — your Twingate domain
- `version` — payload schema version (`"1"`)
- `type` — notification type identifier (see below)

## Notification Types & `type` Values
| Notification | `type` value |
|---|---|
| Usage-based Access Request | `ACCESS_REQUEST` (request_type: `AutoLock`) |
| JIT Access Request | `ACCESS_REQUEST` (request_type: `AccessRequest`) |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` |
| Client update required | `CLIENT_UPDATE_REQUIRED` |
| Connector upgrade available | `CONNECTOR_UPGRADE_AVAILABLE` |
| Connector offline | `CONNECTOR_STATUS_OFFLINE` |
| Connector online | `CONNECTOR_STATUS_ONLINE` |
| Device integration API token expiring | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` |
| Events sync errors | `EVENTS_SYNC_ERRORS` |
| Events sync error resolved | `EVENTS_SYNC_ERROR_RESOLVED` |
| Events sync requires attention | `EVENTS_SYNC_REQUIRES_ATTENTION` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` |
| Identity provider integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` |
| Integration errors | `INTEGRATION_ERRORS` |
| Service account key expiration | `SERVICE_ACCOUNT_KEYS_EXPIRATION` |

## Gotchas
- **Slack Incoming Webhooks**: not supported — only accepts plain text JSON, not standard JSON payloads. Use **Slack Workflow Builder** instead
- Webhook endpoint must accept `POST` — `GET`-only endpoints will error
- Access request payloads use the same `type` (`ACCESS_REQUEST`) for both JIT and usage-based; differentiate via `request_type` field (`AccessRequest` vs `AutoLock`)
- `approval_mode` in access requests can be `MANUAL` or presumably automatic variants

## Related Docs
- Access Requests (JIT / Usage-based Access)
- Device Integrations
- Connector management
- Events sync / S3 integration
- Service Accounts
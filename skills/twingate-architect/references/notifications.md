# Twingate Notifications

## Summary
Twingate provides configurable notification channels (email and webhooks) for admin alerts. Some notifications are mandatory email-only; others can be routed to specific recipients or webhook endpoints. Webhooks accept POST requests with JSON payloads.

## Key Information
- **Fixed notifications** (always email to all admins): subscription updates, end-user notifications
- **Configurable notifications**: can target specific email addresses or webhooks
- Manage via Admin Console → Settings
- Use **Slack Workflow Builder** (not Incoming Webhooks) for Slack integration — Incoming Webhooks only support plain text JSON
- Test payloads available directly in Admin Console per notification type

## Prerequisites
- Admin access to Twingate Admin Console
- Webhook endpoint that accepts HTTP **POST** requests with standard JSON

## Webhook Configuration
Required inputs:
- Webhook name
- Webhook URL
- Selected notification types

## Webhook Payload Fields (Common)
| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 datetime |
| `tenant` | Twingate tenant domain |
| `version` | Payload version (`"1"`) |
| `type` | Notification type constant (see below) |

## Notification Types & `type` Values
| Notification | `type` constant |
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
| Events sync errors resolved | `EVENTS_SYNC_ERROR_RESOLVED` |
| Events sync requires attention | `EVENTS_SYNC_REQUIRES_ATTENTION` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` |
| Identity provider integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` |
| Integration errors | `INTEGRATION_ERRORS` |
| Service account keys expiring | `SERVICE_ACCOUNT_KEYS_EXPIRATION` |

## Access Request Payload Notable Fields
- `request_id`, `request_url` — link to approve/deny in console
- `approval_mode` — `MANUAL` or automatic
- `request_type` — `AutoLock` (usage-based) vs `AccessRequest` (JIT)
- `request_duration_seconds` — requested access duration

## Gotchas
- Webhook endpoints **must accept POST**; GET-only endpoints will error
- Slack Incoming Webhooks reject standard JSON — use Workflow Builder instead
- `CLIENT_UPDATE_REQUIRED` and connector/status payloads include a `table` array (may be empty in test payloads)
- `SERVICE_ACCOUNT_KEYS_EXPIRATION` includes a `table` array with `service_account_name`, `service_key`, `link`

## Related Docs
- Access Requests (JIT/Usage-based)
- Device Integrations settings
- Connector management
- Events sync configuration
# Twingate Notifications

## Summary
Twingate provides configurable notification channels for admins, supporting both email and webhook delivery. Some notifications (subscription updates, end-user notifications) are always emailed to all admins; others can be routed to specific recipients or webhooks with granular per-notification control.

## Key Information
- Notification settings managed in **Admin Console → Settings**
- Two delivery methods: **email** (per admin address) or **webhook** (custom URL)
- Granular control: configure by channel (who gets what) or by notification type (where each goes)
- Webhook configuration requires: name, URL, and selected notification types
- Test payloads can be sent directly from Admin Console per notification type
- All webhook payloads are POST requests with standard JSON

## Supported Webhook Notification Types
| Type | `type` field |
|---|---|
| Usage-based Access Requests | `ACCESS_REQUEST` (AutoLock) |
| JIT Access Requests | `ACCESS_REQUEST` (AccessRequest) |
| Client update recommended | `CLIENT_UPDATE_RECOMMENDED` |
| Client update required | `CLIENT_UPDATE_REQUIRED` |
| Connector update available | `CONNECTOR_UPGRADE_AVAILABLE` |
| Connectors offline/online | `CONNECTOR_STATUS_OFFLINE/ONLINE` |
| Device integration API token expiration | `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` |
| Events sync errors/resolved/attention | `EVENTS_SYNC_ERRORS`, `EVENTS_SYNC_ERROR_RESOLVED`, `EVENTS_SYNC_REQUIRES_ATTENTION` |
| Google Workspace sync error | `GOOGLE_WORKSPACE_SYNC_ERROR` |
| Identity provider integration error | `IDENTITY_PROVIDER_INTEGRATION_ERROR` |
| Integration error resolved | `INTEGRATION_ERROR_RESOLVED` |
| Integration errors | `INTEGRATION_ERRORS` |
| Service account key expiration | `SERVICE_ACCOUNT_KEYS_EXPIRATION` |

## Webhook Payload Common Fields
All payloads include:
- `timestamp` — ISO 8601 UTC
- `tenant` — account domain
- `version` — payload schema version (`"1"`)
- `type` — notification type identifier

## Gotchas
- **Slack Incoming Webhooks are not supported** — use Slack Workflow Builder instead (incoming webhooks reject standard JSON)
- Webhook endpoints must accept **POST** requests; GET-only endpoints will error
- Payload format is standard JSON — services requiring custom formats will reject it
- Fixed notifications (subscription, end-user) cannot be customized; they always go to all admins via email

## Step-by-Step: Configure a Webhook
1. Go to **Admin Console → Settings → Notifications**
2. Click to add a new webhook channel
3. Provide webhook name and URL
4. Select specific notification types to route to this webhook
5. Use **Test Payload** button per notification to validate delivery

## Related Docs
- Access Requests (JIT/Usage-based)
- Connector management
- Device integrations
- Service accounts
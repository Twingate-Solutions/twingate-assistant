## Notifications

Configurable notification system for Twingate Admin Console events. Supports delivery to specific email addresses and/or webhooks.

**Always-sent Notifications (all admins, email only):**
- Subscription updates and end-user notifications

**Configurable Notifications (Settings → Notifications):**
- Per-channel: select email addresses or webhooks, then choose which notifications each receives
- Per-notification: select which emails/webhooks receive a specific notification
- Webhooks require a name, URL, and selected notification types; use "Test Payload" to validate

**Webhook Event Types and Payload Fields:**
- `ACCESS_REQUEST` -- usage-based auto-lock or JIT request; includes user, resource, reason, approval_mode, request_type, request_duration_seconds
- `CLIENT_UPDATE_RECOMMENDED` / `CLIENT_UPDATE_REQUIRED` -- platform + devices_list URL
- `CONNECTOR_UPGRADE_AVAILABLE` -- table of connectors with updates
- `CONNECTOR_STATUS_OFFLINE` / `CONNECTOR_STATUS_ONLINE` -- connector status change
- `DEVICE_INTEGRATION_API_TOKEN_EXPIRATION` -- integration name + days_remaining
- `EVENTS_SYNC_ERRORS` / `EVENTS_SYNC_ERROR_RESOLVED` / `EVENTS_SYNC_REQUIRES_ATTENTION` -- S3 sync status
- `GOOGLE_WORKSPACE_SYNC_ERROR` -- error message
- `IDENTITY_PROVIDER_INTEGRATION_ERROR` / `INTEGRATION_ERRORS` / `INTEGRATION_ERROR_RESOLVED` -- integration name + message
- `SERVICE_ACCOUNT_KEYS_EXPIRATION` -- table of service account names, keys, and console links

**All webhook payloads include:** `timestamp` (UTC ISO 8601), `tenant`, `version`, `type`

**Gotchas:**
- Webhooks must accept POST requests with standard JSON; Slack Incoming Webhooks do not work — use Slack Workflow Builder instead
- Webhook test errors indicate the endpoint returned an error (check HTTP method and payload format support)

**Related Docs:**
- /docs/jit-access-requests -- JIT access request configuration
- /docs/usage-based-auto-lock -- Auto-lock and access request triggers
- /docs/syncing-data-to-s3 -- S3 sync for events

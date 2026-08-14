---
source: https://www.twingate.com/docs/audit-logs-schema
type: docs
fetched: 2026-08-14
source_version: 900bdc4e2fe40848c6c0d3623949bd8ba295b92eebd289797e92ab776f6d4f82
---

# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly or via S3 sync with a wrapper object. Multiple target types are supported with their own schemas.

## Key Information
- Schema `version` is currently `"1"` at both root and target levels
- `time` is UTC ISO 8601 format representing start of network communication
- Actor types: `"User"`, `"API"`, `"Twingate Support"`
- Action types: `"create"`, `"edit"`, `"delete"`
- `targets` is an array (multiple objects can be impacted per event)
- S3-synced logs wrap events in `{"event_type": "audit_log", "event": {...}}`

## Root Event Schema
```json
{
  "version": "1",
  "time": "2021-08-15T14:30Z",
  "actor": {
    "type": "User|API|Twingate Support",
    "id": "unique-id",
    "info": { "email": "...", "name": "..." }
  },
  "action": "create|edit|delete",
  "targets": [{ ... }]
}
```

## Target Types & Key Fields

| Target Type | `type` Value | Notable Fields |
|---|---|---|
| Remote Network | `remoteNetwork` | `name`, `location`, `isActive` |
| Connector | `connector` | `name`, `remoteNetwork` |
| Resource | `resource` | `address`, `protocols`, `isActive` |
| API Key | `publicAPIKey` | `permission`, `allowedIpRange` |
| User | `user` | `email`, `isAdmin`, `isActive` |
| Group | `group` | `name` |
| Device | `device` | `platform`, `osName`, `serialNumber`, `isTrusted`, `clientVersion` |
| Service Account | `serviceAccount` | `name` |
| Service Account Key | `serviceAccountKey` | `state`, `serviceAccount` |

## Enum Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (shown in example)
- **`resource.protocols.tcp/udp.policy`**: `"ALLOW_ALL"` (shown in example)

## Actor Info by Type
- **User**: `{ "email": "...", "name": "..." }`
- **API**: `{ "name": "Terraform API key" }`
- **Twingate Support**: `null`

## Gotchas
- S3-synced logs have an extra wrapper layer (`event_type` + `event` keys) — parsers must handle both formats
- `targets` is always an array; handle multi-target events
- `actor.info` is `null` for Twingate Support actors — guard against null dereference
- Device `name` (internal) vs `displayName` (user-facing) are distinct fields
- Service Account Key embeds full `serviceAccount` object as nested target

## Related Docs
- Audit Logs configuration (sync to S3)
- Twingate API documentation
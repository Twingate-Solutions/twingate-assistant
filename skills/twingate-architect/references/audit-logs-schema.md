# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly or via S3 sync with a wrapper object. Eight target types are supported covering all major Twingate objects.

## Key Information
- Schema `version` is currently `"1"` at both root and target levels
- `time` is UTC ISO 8601 format representing start of network communication
- `targets` is an array — one event can impact multiple objects
- S3-synced logs wrap each event: `{"event_type": "audit_log", "event": {...}}`

## Event Schema Fields

| Field | Values |
|-------|--------|
| `actor.type` | `"User"`, `"API"`, `"Twingate Support"` |
| `action` | `"create"`, `"edit"`, `"delete"` |

**Actor info by type:**
- `User`: `email`, `name`
- `API`: `name` (key name)
- `Twingate Support`: `null`

## Target Schemas

| Target Type | Key Fields |
|-------------|------------|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork.{id,name}` |
| `resource` | `name`, `address.{type,value}`, `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount` |

## Enumerated Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (implied; other types may exist)
- **`resource.protocols.tcp|udp.policy`**: `"ALLOW_ALL"` (other values likely exist)

## Gotchas
- S3 sync adds an outer wrapper — parse `event` field, not root object directly
- `Twingate Support` actor has `null` info — handle null checks in parsers
- `targets` is always an array even for single-object events
- Device `name` vs `displayName` are distinct fields — `displayName` is user-friendly label
- `serviceAccountKey` embeds full `serviceAccount` object, not just an ID reference

## Related Docs
- Audit Logs configuration (setup/export)
- S3 integration for log syncing
- API key management
- Service Accounts documentation
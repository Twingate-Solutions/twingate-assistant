# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema that captures actor, action, and target information for administrative events. Logs can be consumed directly or via S3 sync with a wrapper envelope. Eight distinct target object types are supported.

## Key Information
- Schema `version`: currently `"1"`
- `time`: UTC ISO 8601 datetime (beginning of network communication)
- `action` values: `"create"`, `"edit"`, `"delete"`
- `actor.type` values: `"User"`, `"API"`, `"Twingate Support"`
- S3-synced logs wrap each event in `{"event_type": "audit_log", "event": {...}}`

## Root Event Schema
```json
{
  "version": "1",
  "time": "2021-08-15T14:30Z",
  "actor": { "type": "User|API|Twingate Support", "id": "...", "info": {} },
  "action": "create|edit|delete",
  "targets": [{ ... }]
}
```

## Target Object Types & Key Fields

| Target Type | Notable Fields |
|---|---|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork` |
| `resource` | `address`, `protocols` (tcp/udp/icmp), `isActive` |
| `publicAPIKey` | `permission`, `allowedIpRange` |
| `user` | `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `platform`, `osName`, `serialNumber`, `isTrusted`, `user`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `state`, `serviceAccount` (nested) |

## Enum Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`

## Actor Info Variants
- **User**: `{ "email": "...", "name": "..." }`
- **API**: `{ "name": "key-name" }`
- **Twingate Support**: `null`

## Gotchas
- S3 sync adds an outer wrapper object — parse `event` field before applying the standard schema
- `targets` is an array; a single action can impact multiple objects
- `serviceAccountKey` includes a nested `serviceAccount` object (not just an ID reference)
- `resource.protocols.tcp/udp.ports` may be an empty array when policy is `ALLOW_ALL`

## Related Docs
- Audit Logs setup/configuration
- S3 sync integration
- API key management
- Service accounts documentation
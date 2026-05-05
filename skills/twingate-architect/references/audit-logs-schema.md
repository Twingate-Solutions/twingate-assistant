# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly via API or synced to S3 with a wrapper object. Multiple target types are supported with distinct schemas.

## Key Information
- Schema `version`: currently `"1"`
- `time`: UTC ISO 8601 datetime (start of network communication)
- `action` values: `"create"`, `"edit"`, `"delete"`
- `actor.type` values: `"User"`, `"API"`, `"Twingate Support"`
- S3-synced logs wrap each event in `{"event_type": "audit_log", "event": {...}}`

## Root Event Schema
```json
{
  "version": "1",
  "time": "2021-08-15T14:30Z",
  "actor": { "type": "User|API|Twingate Support", "id": "...", "info": {...} },
  "action": "create|edit|delete",
  "targets": [...]
}
```

## Target Types & Key Fields

| Target Type | Key Fields |
|---|---|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork.id/name` |
| `resource` | `name`, `address.type/value`, `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount` |

## Enumerated Field Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (implied; others may exist)
- **`resource.protocols.tcp/udp.policy`**: `"ALLOW_ALL"` (others may exist)

## Gotchas
- S3-synced logs have an extra wrapper layer (`event_type` + `event` keys) — parsers must handle both formats
- `actor.info` is `null` for `"Twingate Support"` actor type
- `targets` is an array — a single event can impact multiple objects
- Each target has its own `version` field independent of the root event version
- `serviceAccountKey` embeds the full `serviceAccount` object, not just an ID reference

## Related Docs
- Audit Logs configuration (streaming/S3 setup)
- API Keys management
- Service Accounts documentation
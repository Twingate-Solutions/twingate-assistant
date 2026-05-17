# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly or via S3 sync with a wrapper envelope. Nine distinct target object types are defined with their own schemas.

## Key Information
- Schema version: `"1"` (root-level field)
- `time` field: UTC ISO 8601 datetime representing start of network communication
- Actor types: `"User"`, `"API"`, `"Twingate Support"`
- Action types: `"create"`, `"edit"`, `"delete"`
- `targets` is an array — multiple objects can be impacted per event
- S3-synced logs wrap each event in `{"event_type": "audit_log", "event": {...}}`

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
  "targets": [...]
}
```

## Target Object Types & Key Fields

| Target Type | Key Fields |
|---|---|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork` (id+name) |
| `resource` | `name`, `address` (type+value), `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount` |

## Enumerated Values

- **API key `permission`**: `"read only"`, `"read write"`, `"provision"`
- **Service account key `state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **Resource `address.type`**: `"DNS"` (implied; shown in example)
- **Resource protocol `policy`**: `"ALLOW_ALL"` (shown in example)

## Gotchas
- Actor `info` is `null` for `"Twingate Support"` actor type — handle null before accessing fields
- `targets` is always an array; parse accordingly even for single-object events
- S3 logs have an extra wrapper layer (`event_type` + `event` envelope) not present in direct log output
- Each target has its own `version` field independent of the root event version

## Related Docs
- Audit Logs configuration (S3 sync setup)
- API Key management
- Service Accounts
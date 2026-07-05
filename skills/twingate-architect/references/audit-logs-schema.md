# Audit Logs Schema

## Summary
Defines the JSON schema for Twingate audit log events, including the root event structure and all possible target object schemas. Events track create/edit/delete actions by users, API keys, or Twingate Support on network objects.

## Key Information
- Schema version is currently `"1"`
- `time` field is UTC ISO 8601 format representing start of network communication
- `actor.type` values: `"User"`, `"API"`, `"Twingate Support"`
- `action` values: `"create"`, `"edit"`, `"delete"`
- S3-synced logs wrap events in an outer object with `event_type: "audit_log"`

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
  "targets": [ { ... } ]
}
```

## Target Object Types

| Type | Key Fields |
|------|-----------|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork{id,name}` |
| `resource` | `name`, `address{type,value}`, `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount` |

## Configuration Values

- **`publicAPIKey.permission`** values: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`** values: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (shown in example)
- **`resource.protocols.tcp/udp.policy`**: `"ALLOW_ALL"` (shown in example)

## S3 Wrapper Schema
```json
{
  "event_type": "audit_log",
  "event": { /* standard event schema */ }
}
```

## Gotchas
- S3-synced logs have an extra wrapper layer — parsers must unwrap `event` field before processing standard schema
- `actor.info` is `null` for `"Twingate Support"` actor type
- `targets` is an array — a single action can impact multiple objects
- Each target has its own `version` field independent of the root event version

## Related Docs
- Audit Logs setup/configuration (see Twingate audit logs docs)
- S3 integration for log export
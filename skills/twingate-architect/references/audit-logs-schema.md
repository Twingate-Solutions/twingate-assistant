# Audit Logs Schema

## Summary
Twingate audit logs are structured JSON events capturing who made a change, what action was taken, and what objects were affected. Logs can be consumed directly or synced to S3 with a wrapper envelope. Each event contains actor, action, and targets fields.

## Key Information

- **Schema version**: Current version is `"1"`
- **Time format**: UTC ISO 8601 datetime string (e.g., `"2021-08-15T14:30Z"`)
- **Actor types**: `"User"`, `"API"`, `"Twingate Support"`
- **Action values**: `"create"`, `"edit"`, `"delete"`
- **Target types**: `remoteNetwork`, `connector`, `resource`, `publicAPIKey`, `user`, `group`, `device`, `serviceAccount`, `serviceAccountKey`

## Root Event Schema

```json
{
  "version": "1",
  "time": "<UTC ISO datetime>",
  "actor": {
    "type": "User|API|Twingate Support",
    "id": "<unique-id>",
    "info": { "email": "...", "name": "..." }
  },
  "action": "create|edit|delete",
  "targets": [ { ... } ]
}
```

## S3 Wrapper Schema

```json
{
  "event_type": "audit_log",
  "event": { /* standard event schema */ }
}
```

## Target Schemas Reference

| Target Type | Key Fields |
|---|---|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork{id,name}` |
| `resource` | `name`, `address{type,value}`, `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount` |

## Enum Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (implied from example)
- **`resource.protocols.tcp/udp.policy`**: `"ALLOW_ALL"` (implied from example)

## Gotchas

- `"Twingate Support"` actor has `null` info field — handle null checks when parsing
- S3-synced logs have an extra wrapper object; direct API logs do not — parsers need to handle both formats
- `targets` is an array; a single event can affect multiple objects
- `time` represents **beginning** of network communication, not event processing time
- `serviceAccountKey` includes nested `serviceAccount` object (not just an ID reference)

## Related Docs

- Audit Logs setup/configuration (Twingate admin docs)
- S3 integration for log syncing
- Twingate API reference
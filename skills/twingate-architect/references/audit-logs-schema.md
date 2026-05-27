# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly or via S3 sync with a wrapper envelope. Schema version is currently `"1"`.

## Key Information

- **Actor types**: `User`, `API`, `Twingate Support`
- **Action values**: `create`, `edit`, `delete`
- **`time` field**: UTC ISO 8601, represents beginning of network communication
- S3-synced logs wrap each event in `{"event_type": "audit_log", "event": {...}}`
- All target objects include `version` and `type` fields

## Root Event Schema

```json
{
  "version": "1",
  "time": "<UTC ISO 8601>",
  "actor": { "type": "User|API|Twingate Support", "id": "...", "info": {...} },
  "action": "create|edit|delete",
  "targets": [...]
}
```

## Target Object Schemas

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

## Enumerated Field Values

- **`publicAPIKey.permission`**: `read only`, `read write`, `provision`
- **`serviceAccountKey.state`**: `active`, `expired`, `revoked`, `deleted`
- **`resource.address.type`**: `DNS` (implied; other types possible)
- **`resource.protocols.tcp|udp.policy`**: `ALLOW_ALL` (others possible)

## Gotchas

- `actor.info` is `null` for `Twingate Support` actor type
- S3 sync adds an outer wrapper object — parse `event` field to get the standard schema
- `targets` is an array; a single action can impact multiple objects
- `device.name` vs `device.displayName` are distinct fields (internal name vs user-visible name)

## Related Docs
- Audit Logs setup/export configuration
- S3 integration for log streaming
- API key management
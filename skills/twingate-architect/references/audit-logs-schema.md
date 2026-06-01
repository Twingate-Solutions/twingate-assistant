# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly via API or synced to S3 with a wrapper object. Eight target object types are supported.

## Key Information

- **Schema version**: Currently `"1"` (root-level field)
- **Time format**: UTC ISO 8601 (e.g., `2021-08-15T14:30Z`) — represents beginning of network communication
- **Actor types**: `"User"`, `"API"`, `"Twingate Support"`
- **Action types**: `"create"`, `"edit"`, `"delete"`
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
  "targets": [{ ... }]
}
```

## S3 Wrapper Schema

```json
{
  "event_type": "audit_log",
  "event": { /* standard event schema */ }
}
```

## Target Object Reference

| Target | Key Fields |
|--------|-----------|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork{id,name}` |
| `resource` | `name`, `address{type,value}`, `protocols`, `isActive` |
| `publicAPIKey` | `name`, `permission`, `allowedIpRange` |
| `user` | `name`, `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `name`, `displayName`, `platform`, `osName`, `serialNumber`, `user`, `isTrusted`, `clientVersion` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `name`, `state`, `serviceAccount{}` |

## Enum Values

- **`publicAPIKey.permission`**: `"read only"`, `"read write"`, `"provision"`
- **`serviceAccountKey.state`**: `"active"`, `"expired"`, `"revoked"`, `"deleted"`
- **`resource.address.type`**: `"DNS"` (implied; others may exist)
- **`resource.protocols.tcp|udp.policy`**: `"ALLOW_ALL"` (others may exist)

## Gotchas

- `"Twingate Support"` actor has `null` info field — handle null checks when parsing
- S3-synced logs have an extra wrapper layer (`event_type` + `event`) not present in direct API logs — parsers must handle both formats
- `targets` is an array; a single action can impact multiple objects
- `serviceAccountKey` embeds the full `serviceAccount` object nested within it

## Related Docs

- Audit Logs configuration (export to S3)
- Twingate API reference
- Service Accounts documentation
# Audit Logs Schema

## Summary
Twingate audit logs use a versioned JSON schema capturing actor, action, and target information for all administrative events. Logs can be consumed directly via API or synced to S3 with a wrapper envelope. Multiple target object types are supported with type-specific fields.

## Key Information

- **Schema version**: Currently `"1"` (root-level field)
- **Time format**: UTC ISO 8601 (represents beginning of network communication)
- **Actor types**: `"User"`, `"API"`, `"Twingate Support"`
- **Action types**: `"create"`, `"edit"`, `"delete"`
- **Target types**: `remoteNetwork`, `connector`, `resource`, `publicAPIKey`, `user`, `group`, `device`, `serviceAccount`, `serviceAccountKey`
- **S3 sync**: Events wrapped in `{"event_type": "audit_log", "event": {...}}`

## Base Event Schema

```json
{
  "version": "1",
  "time": "2021-08-15T14:30Z",
  "actor": { "type": "User", "id": "...", "info": { "email": "...", "name": "..." } },
  "action": "edit",
  "targets": [{ ... }]
}
```

## Target Schemas — Key Fields

| Target | Notable Fields |
|--------|---------------|
| `remoteNetwork` | `name`, `location`, `isActive` |
| `connector` | `name`, `remoteNetwork{id,name}` |
| `resource` | `address{type,value}`, `protocols{allowIcmp,tcp,udp}`, `isActive` |
| `publicAPIKey` | `permission` (`read only`/`read write`/`provision`), `allowedIpRange` |
| `user` | `email`, `isAdmin`, `isActive` |
| `group` | `name` |
| `device` | `platform`, `osName`, `serialNumber`, `isTrusted`, `clientVersion`, `user{}` |
| `serviceAccount` | `name` |
| `serviceAccountKey` | `state` (`active`/`expired`/`revoked`/`deleted`), `serviceAccount{}` |

## Gotchas

- `"Twingate Support"` actor has `null` info — handle null checks when parsing
- `targets` is an array — events can impact multiple objects simultaneously
- S3-synced logs have an extra wrapper layer (`event_type` + `event` keys) vs. direct API logs
- `resource.protocols.tcp/udp.ports` can be an empty array when policy is `ALLOW_ALL`
- `serviceAccountKey` includes nested `serviceAccount` object — potential for deeply nested parsing

## Related Docs
- Audit Logs setup/export configuration
- S3 integration for audit log syncing
- API key permissions reference
## Audit Logs Schema

JSON schema reference for Twingate audit log events. Each event has a root-level structure with version, time, actor, action, and a targets array. Targets represent specific Twingate objects impacted by the event.

**Root Event Schema:**
- `version`: schema version (currently "1")
- `time`: UTC ISO 8601 timestamp
- `actor.type`: `User`, `API`, or `Twingate Support`
- `action`: `create`, `edit`, or `delete`
- `targets`: array of impacted objects

**S3 Sync Wrapper:**
All S3-synced events are wrapped: `{ "event_type": "audit_log", "event": { ... } }`

**Target Object Types and Key Fields:**
- `remoteNetwork` -- id, name, location, isActive
- `connector` -- id, name, remoteNetwork (id + name)
- `resource` -- id, name, address (type + value), protocols (allowIcmp, tcp, udp policies), isActive
- `publicAPIKey` -- id, name, permission (`read only` / `read write` / `provision`), allowedIpRange
- `user` -- id, name, email, isAdmin, isActive
- `group` -- id, name
- `device` -- id, name, displayName, platform, osName, serialNumber, user (id/email/name), isTrusted, clientVersion
- `serviceAccount` -- id, name
- `serviceAccountKey` -- id, name, state (`active` / `expired` / `revoked` / `deleted`), serviceAccount reference

**Related Docs:**
- /docs/audit-logs -- Audit log overview and export options
- /docs/admin-console-export -- Exporting audit logs from Admin Console
- /docs/syncing-data-to-s3 -- S3 sync configuration

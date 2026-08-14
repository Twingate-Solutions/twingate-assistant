---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-14
source_version: b892d5f49e74ee908d20f4e3b3e08f677131096ce464a8037be6d1e3ab09b5c9
---

# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate JavaScript CLI (`tg`)

## Summary
Open-source JavaScript CLI tool wrapping Twingate GraphQL APIs for managing users, groups, resources, connectors, networks, devices, service accounts, and policies. Provides pre-built binaries for Windows/Mac/Linux plus export/import functionality. Community-maintained project (not Twingate product engineering).

## Key Information
- Binary download from GitHub releases page
- Wraps Twingate GraphQL API
- Prompts for account name and API key on first run; optionally saves credentials to file
- Accepts names **or** IDs for most entity references
- Returns Base64-encoded entity IDs (e.g., `VXNlcjoxMzY3Ng==`)

## Prerequisites
- Twingate account name (subdomain)
- Twingate API key
- GraphViz (only for `png`/`svg` export formats)

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | TRACE/DEBUG/INFO/WARN/ERROR/SEVERE/FATAL/QUIET/SILENT | INFO |

## Commands & Usage

### user
```
tg user list
```

### group
```
tg group list
tg group create <name> [UserIds...]
tg group remove <id>
tg group remove_bulk [groupIds...]
tg group add_user <groupNameOrId> [userIds...]
tg group remove_user <groupNameOrId> [userIds...]
tg group add_resource <groupNameOrId> [resourceNamesOrIds...]
tg group remove_resource <groupNameOrId> [resourceNamesOrIds...]
tg group set_policy <groupNameOrId> <securityPolicyNameOrId>
tg group copy <source> <destination>
```

### network
```
tg network list
tg network create <name>
```

### connector
```
tg connector list
tg connector create <remoteNetworkNameOrId> [name]   # outputs ACCESS_TOKEN + REFRESH_TOKEN
```

### resource
```
tg resource list
tg resource create <remoteNetworkNameOrId> <name> <address> [groupNamesOrIds...]
tg resource remove <id>
tg resource remove_bulk [resourceIds...]
tg resource add_group <resourceNameOrId> [groupNamesOrIds...]
```

### device
```
tg device list
```

### service
```
tg service list
tg service create <name> [resourceNamesOrIds...]
tg service remove <id>
tg service add_resource <serviceAccountId> [resourceNamesOrIds...]
tg service key_create <serviceAccountId> <keyName> <expirationTimeInDays>
```

### policy
```
tg policy list
tg policy add_group <securityPolicyNameOrId> [groupNamesOrIds...]
```

### export
```
tg export [-f xlsx|json|dot|png|svg] [-o outputFile] [-n] [-r] [-g] [-u] [-d]
```

### import
```
tg import -f <excelFile> [-n] [-r] [-g] [-d] [-s] [-y]
```

## Gotchas
- `group add_user` / `group create` with users requires **User IDs**, not email addresses
- `service remove` fails if service account has active keys
- `policy add_group` **replaces** existing policy assignment on groups
- `png`/`svg` export requires GraphViz installed and on PATH
- `group copy` copies all users from source to a **new** destination group
- Support via GitHub Issues only (not official Twingate support)

## Related Docs
- [Twingate Python CLI](https://www.twingate.com/docs/python-cli)
- Twingate GraphQL API docs
- [GitHub Issues](https://github.com/Twingate/twingate-js-cli/issues) for support
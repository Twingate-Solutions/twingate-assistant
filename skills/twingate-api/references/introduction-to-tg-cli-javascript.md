---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-10-04
source_version: e9307d3ab4bea40afae54d3550c1c748761ee7e61ed19cf3c9e6dd7a2dc0fe19
trust: official
---

# Twingate JavaScript CLI Reference

## Page Title
Introduction to the Twingate Javascript CLI

## Summary
An open-source JavaScript CLI tool wrapping Twingate's GraphQL APIs. Provides commands for managing users, groups, networks, connectors, resources, devices, policies, and service accounts. Available as pre-built binaries for Windows, Mac, and Linux; source is extensible for Node/Deno developers.

## Key Information
- Backed by `TwingateApiClient` library; open-source, community-maintained (not official product engineering)
- Prompts interactively for account name and API key on first run; optionally saves credentials to file
- Supports export (xlsx, json, dot, png, svg) and import (xlsx) for bulk account data
- PNG/SVG export requires GraphViz installed and on `PATH`
- Removing a service account requires 0 active keys first
- `policy add_group` **replaces** existing security policy on affected groups

## Prerequisites
- Twingate account name and API key
- Pre-built binary from [GitHub releases](https://github.com/Twingate/tg-cli) (download and unzip; no pipe-to-shell install)
- GraphViz (optional, for png/svg export only)

## CLI Flags (Global)
| Flag | Description | Default |
|------|-------------|---------|
| `-a, --account-name` | Twingate account name | — |
| `-l, --log-level` | `TRACE` `DEBUG` `INFO` `WARN` `ERROR` `SEVERE` `FATAL` `QUIET` `SILENT` | `INFO` |
| `-h, --help` | Show help | — |
| `-V, --version` | Show version | — |

## Command Reference

| Command | Subcommands |
|---------|-------------|
| `user` | `list` |
| `group` | `list`, `create <name> [userIds...]`, `remove <id>`, `remove_bulk`, `add_user`, `remove_user`, `add_resource`, `remove_resource`, `set_policy`, `copy` |
| `network` | `list`, `create <name>` |
| `connector` | `list`, `create <remoteNetworkNameOrId> [name]` |
| `resource` | `list`, `create <network> <name> <address> [groups...]`, `remove <id>`, `remove_bulk`, `add_group` |
| `device` | `list` |
| `policy` | `list`, `add_group <policyNameOrId> [groupNamesOrIds...]` |
| `service` | `list`, `create <name> [resources...]`, `remove <id>`, `add_resource`, `key_create <serviceId> <keyName> <expirationDays>` |
| `export` | `-f xlsx\|json\|dot\|png\|svg`, `-o <file>`, `-n` `-r` `-g` `-u` `-d` flags |
| `import` | `-f <xlsxFile>`, `-n` `-r` `-g` `-d` flags, `-s` (sync), `-y` (assume yes) |

## Gotchas
- User IDs (base64) required for user operations — not email addresses
- Referenced entities (groups, resources, networks) must exist before being referenced in create commands
- `group set_policy` / `policy add_group` overwrites existing policy assignments
- `connector create` returns `ACCESS_TOKEN` and `REFRESH_TOKEN` — capture output immediately

## Related Docs
- [Twingate Python CLI](https://www.twingate.com/docs/python-cli)
- [Twingate GraphQL API](https://www.twingate.com/docs/api)
- [GitHub Issues (support)](https://github.com/Twingate/tg-cli/issues)
---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-11-13
source_version: e3ad30eaa5dafaa8987dcebd544721b2d7ea1f1a5b5b284baaacee1c3212260f
trust: official
---

# Introduction to the Twingate JavaScript CLI (`tg`)

## Summary
The `tg` CLI is an open-source JavaScript (Node/Deno) command-line tool built on the Twingate GraphQL APIs. It manages users, groups, resources, networks, connectors, devices, policies, and service accounts, and supports export and import of account data. Pre-built binaries are available for Windows, macOS, and Linux. Support goes through GitHub issues, not Twingate engineering.

## Key Information
- Binaries come from the project's GitHub release page. Unzip and run `./tg --help`.
- Global options: `-h/--help`, `-V/--version`, `-a/--account-name <string>`, `-l/--log-level` (default `INFO`; values TRACE, DEBUG, INFO, WARN, ERROR, SEVERE, FATAL, QUIET, SILENT).
- Commands: `export`, `import`, `resource`, `group`, `user`, `network`, `connector`, `device`, `service`, `policy`.
- On first use, `tg` prompts for the Twingate account name and API key and offers to save them to a config file.
- A Python CLI alternative exists.

## Prerequisites
- A Twingate account name and API key.
- Entities referenced by commands must already exist (users, resources, groups, remote networks).
- Graphviz on your PATH for `png`/`svg` export.

## Command Reference
- **user**: `list`
- **group**: `list`, `create <name> [userIds...]`, `remove <id>`, `remove_bulk [groupIds...]`, `add_user`, `remove_user`, `add_resource`, `remove_resource`, `set_policy <group> <policy>`, `copy <source> <destination>`
- **network**: `list`, `create <name>`
- **connector**: `list`, `create <remoteNetworkNameOrId> [name]` (outputs ACCESS_TOKEN and REFRESH_TOKEN)
- **resource**: `list`, `create <network> <name> <address> [groups...]`, `remove <id>`, `remove_bulk`, `add_group <resource> [groups...]`. The `remove_group` command appears in the examples but not in the help output.
- **device**: `list`
- **policy**: `list`, `add_group <policy> [groups...]`
- **service**: `list`, `create <name> [resources...]`, `remove <id>`, `add_resource <serviceAccountId> [resources...]`, `key_create <serviceAccountId> <keyName> <expirationTimeInDays>`

## Configuration Values (export/import flags)
- **export**:
  - `-f/--format`: xlsx (default), json, dot, png, svg
  - `-o/--output-file`
  - Include flags: `-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices
  - Example: `./tg export -r -f json`
- **import**:
  - `-f/--file <path>` (required, Excel file)
  - `-n`, `-r`, `-g`, `-d` include flags
  - `-s/--sync`: synchronize entities with the same natural identifier
  - `-y/--assume-yes`: auto-answer yes to prompts

## Gotchas
- Users are added to groups by **user ID**, not email.
- `policy add_group` **replaces** any security policy already assigned to those groups.
- A service account cannot be removed until it has 0 active keys.
- `service key_create` outputs a token object containing a private key. Store it securely, since it is shown in terminal output.
- Connector creation prints tokens to the terminal.
- Saved API keys are written to a local config file, so protect it.
- The tool is community-maintained. Use GitHub issues for support.

## Related Docs
- Twingate Python CLI documentation
- Twingate GraphQL API documentation
- `tg` GitHub releases and issues page
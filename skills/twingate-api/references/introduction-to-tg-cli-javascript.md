---
source: https://www.twingate.com/docs/introduction-to-tg-cli-javascript
type: docs
fetched: 2026-08-14
source_version: 0e2ec905e35c5dbf62df3a1c935f08451f414938e78647bb77e47ef2d65e97f0
---

# Introduction to the Twingate JavaScript CLI

## Summary
The Twingate JavaScript CLI (`tg`) is an open-source, community-maintained tool built on the Twingate GraphQL API for managing Twingate account resources from the terminal. It ships as pre-built binaries for Windows, Mac, and Linux, and can be extended in Node or Deno. A Python CLI alternative exists for those who prefer it.

## Key Information
- **Community-maintained** — developed outside Twingate product engineering; support via the GitHub issues page, not Twingate support.
- Authenticates per-invocation with a **Twingate account name + API Key**, with an option to save both to a local config file.
- Command groups: `export`, `import`, `resource`, `group`, `user`, `network`, `connector`, `device`, `service`, `policy`.
- Entity references accept **name or ID** in most commands; users must be referenced by **ID only** when adding to groups.
- All entity IDs are base64-encoded GraphQL node IDs (e.g. `VXNlcjoxMzY3Ng==`).

## Prerequisites
- Download and unzip the binary from the GitHub release page.
- A Twingate API key (generate in the Admin Console).
- GraphViz installed and on PATH — **only** for `png`/`svg` export formats.

## Step-by-Step (Getting Started)
1. Download the platform binary from GitHub releases; unzip.
2. Run `./tg --help` to confirm.
3. Run any command (e.g. `./tg export`); enter account name and API key when prompted, optionally saving to config.

## Configuration Values
**Global options:** `-a/--account-name <string>`, `-l/--log-level` (`TRACE`,`DEBUG`,`INFO`,`WARN`,`ERROR`,`SEVERE`,`FATAL`,`QUIET`,`SILENT`; default `INFO`), `-h/--help`, `-V/--version`.

**Export** (`tg export`): `-f/--format` (`xlsx` default, `json`, `dot`, `png`, `svg`), `-o/--output-file`, and include-flags `-n` networks, `-r` resources, `-g` groups, `-u` users, `-d` devices.

**Import** (`tg import`): `-f/--file <path>` (required Excel file), `-n/-r/-g/-d` include-flags, `-s/--sync` (match entities by natural identifier), `-y/--assume-yes`.

**Service:** `key_create <serviceAccountId> <keyName> <expirationTimeInDays>`.

## Gotchas
- **Users must be added to groups by ID, not email address.** Same for other reference-by-ID operations noted in the docs.
- `group add_user`/`add_resource`, `resource create`, `service add_resource` require the referenced entities to **already exist**.
- A **service account cannot be removed until it has 0 active keys**.
- `policy add_group` **replaces** any security policy already assigned to those groups.
- `png`/`svg` exports silently depend on GraphViz being installed and on PATH.
- `connector create` and `service key_create` output secret tokens/private keys to the terminal — handle output securely.
- Tool is unsupported by Twingate product teams; treat as community tooling for automation, not a supported production integration.

## Related Docs
- Twingate Python CLI (alternative implementation)
- Twingate GraphQL API reference
- GitHub release/issues page for `tg`

---
This is formatted as a reference summary. Want me to write it to a `references/` file under `twingate-api` (the skill that owns CLI tooling), or is this a one-off?
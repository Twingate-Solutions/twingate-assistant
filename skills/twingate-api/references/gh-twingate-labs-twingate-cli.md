---
source: https://github.com/Twingate-Labs/Twingate-CLI
type: github
fetched: 2026-10-11
source_version: 1e55a8b63a9d5e654c6c98909828e7ed71cae834
trust: official
---

# Twingate Admin CLI

## Summary
A Python command-line tool for the Twingate Admin GraphQL API. Covers CRUD operations on remote networks, resources, connectors, groups, users, service accounts, policies, access requests, gateways, certificate authorities, and DNS security settings. Supports multiple tenant sessions, three output formats, and bulk operations like synced-group migration.

## Key Information
- MIT licensed; Python 3.9+
- Built with Typer; uses `keyring` for credential storage
- Output formats: JSON (default), CSV, Pandas DataFrame
- Auto-retries on HTTP 429 with `Retry-After` respect (3 retries max)
- Multi-tenant support via named sessions
- Bulk operations: group migration (Synced → Manual), device trust updates, serial-number allowlists

## Prerequisites
- Python 3.9 or later
- Twingate account with an Admin API token
- **Headless/CI Linux only:** `pip install keyrings.alt` + `export PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring`

## Installation
```bash
git clone https://github.com/Twingate-Labs/Twingate-CLI.git
cd Twingate-CLI
python3 -m venv .venv && source .venv/bin/activate
pip install .
```

## Usage / Step-by-Step
```bash
# Authenticate (stored in OS keychain)
tgcli auth login -a <api-token> -t <tenant-subdomain>

# Basic usage
tgcli resource list
tgcli -f CSV device list
tgcli -s staging group list

# Multi-tenant
tgcli auth login -a tgp_xxx -t acme -s prod
tgcli auth login -a tgp_yyy -t acme-staging -s staging
tgcli -s prod resource list

# Group migration (dry run by default)
tgcli group migrate
tgcli group migrate --execute --name-suffix " (Manual)" --report out.csv
```

## Configuration Values

### Global Flags (before command name)
| Flag | Short | Values | Default |
|------|-------|--------|---------|
| `--session` | `-s` | Any string | `default` |
| `--format` | `-f` | `JSON`, `CSV`, `DF` | `JSON` |
| `--log` | `-l` | `DEBUG`, `INFO`, `WARNING`, `ERROR` | `ERROR` |
| `--version` | `-v` | — | — |

### Auth
- `-a` API token
- `-t` Tenant subdomain (e.g. `acme` from `acme.twingate.com`)
- `-s` Session name

### Resource Create Key Flags
| Flag | Description | Default |
|------|-------------|---------|
| `-t` | TCP policy: `ALLOW_ALL`/`RESTRICTED` | `ALLOW_ALL` |
| `-c` | TCP port ranges JSON `[[22,22]]` | `[]` |
| `-m` | Routing: `THROUGH_TWINGATE`/`BYPASS_TWINGATE` | `THROUGH_TWINGATE` |

### Environment Variable
- `PYTHON_KEYRING_BACKEND` — override keyring backend (headless Linux)

## Command Reference

### device
- `list` — supports server-side filters: `--untrusted`, `--trusted`, `--state ACTIVE|ARCHIVED|BLOCKED` (repeatable), `--serial-number`, `--user-id` (repeatable)
- `list --idsonly` / `list --fileofids <file>` — ID-only output or diff against a saved list of IDs
- `show`, `updateTrust`, `block`, `unblock`, `archive`, `unarchive`
- Serial-number allowlist: `snumber list/add/remove`

### resource
- `list` — basic listing; add `-d`/`--detail` for access policy, approval mode, approver groups, and gateway-specific columns (slightly slower on large tenants)
- `show` — always includes the detail columns
- Both commands include a `type` column: `NETWORK`, `SSH`, `WEB
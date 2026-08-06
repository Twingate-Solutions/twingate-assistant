---
source: https://github.com/Twingate-Labs/Twingate-CLI
type: github
fetched: 2026-08-06
source_version: b61e7235a9a34d1bddd522391a1cfc748d741758
---

<!-- triage: unassigned -->

# Twingate Admin CLI

## Summary
A Python command-line tool for the Twingate Admin GraphQL API. Covers CRUD operations on remote networks, resources, connectors, groups, users, service accounts, policies, and DNS security settings. Supports multiple tenant sessions, three output formats, and bulk operations like synced-group migration.

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

## Gotchas
- All entity IDs are base64-encoded GraphQL node IDs (e.g. `UmVzb3VyY2U6MQ==`), not human-readable names
- `resource access_set` is **destructive** — replaces all existing group/service-account access
- `group migrate` skips inactive Synced Groups; reuses existing Manual Groups with matching names
- Rate limits vary by account (typically 60 reads/min, 20 writes/min); the CLI handles retries automatically but long bulk operations may be slow
- `mappings resource-connectivity` joins resources and connectors client-side — no direct API link exists between them
- `key create` with `-e 0` creates a non-expiring key

## Related Docs
- [Twingate Admin API overview](https://docs.twingate.com/docs/api-overview)
- [Internet Security Client Configuration](https://www.twingate.
---
source: https://github.com/Twingate-Labs/Twingate-CLI
type: github
fetched: 2026-10-25
source_version: e839a354e81e3c9a03ee2ca2dcb0e0373f50a4d0
trust: official
---

# Twingate Admin CLI

## Summary
A Python command-line tool for the Twingate Admin GraphQL API. Covers CRUD operations on remote networks, resources, connectors, groups, users, service accounts, policies, access requests, gateways, certificate authorities, and DNS security settings. Supports multiple tenant sessions, three output formats, and bulk operations like synced-group migration, backup, and import.

## Key Information
- MIT licensed; Python 3.9+
- Built with Typer; uses `keyring` for credential storage
- Output formats: JSON (default), CSV, Pandas DataFrame
- Auto-retries on HTTP 429 with `Retry-After` respect (3 retries max)
- Multi-tenant support via named sessions (**`-s <session>` is required for every command that contacts Twingate; there is no default session**)
- Bulk operations: group migration (Synced → Manual), device trust updates, serial-number allowlists, tenant backup, import from backup or custom CSV/JSON files
- Shell completion via `tgcli --install-completion` (zsh, bash 4.4+, fish, PowerShell); `-s`/`--session` and `group migrate --group` complete their values

## Prerequisites
- Python 3.9 or later
- Twingate account with an Admin API token
- **Headless/CI Linux only:** `pip install keyrings.alt` + `export PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring`

## Installation

**macOS / Linux:**
```bash
git clone https://github.com/Twingate-Labs/Twingate-CLI.git
cd Twingate-CLI
python3 -m venv .venv && source .venv/bin/activate
pip install .
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/Twingate-Labs/Twingate-CLI.git
cd Twingate-CLI
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
pip install .
```
Windows notes: credentials go to Windows Credential Manager; if `Activate.ps1` is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` first; set `$env:PYTHONUTF8 = "1"` before piping/redirecting to avoid `UnicodeEncodeError`; Windows PowerShell 5.1 `>` redirection writes UTF-16 (use PowerShell 7 or `| Out-File -Encoding utf8`). Developed and tested on macOS; Windows support is best-effort.

## Usage / Step-by-Step
```bash
# Authenticate (stored in OS keychain) — always name the session with -s
tgcli auth login -a <api-token> -t <tenant-subdomain> -s <session-name>

# Basic usage (-s is required)
tgcli -s acme resource list
tgcli -s acme -f CSV device list

# Multi-tenant
tgcli auth login -a tgp_xxx -t acme -s prod
tgcli auth login -a tgp_yyy -t acme-staging -s staging
tgcli -s prod resource list
tgcli -s staging resource list

# Group migration (dry run by default)
tgcli -s prod group migrate
tgcli -s prod group migrate --group "Engineering" --execute --name-suffix " (Manual)" --report out.csv

# Backup
tgcli -s prod backup
tgcli -s prod backup -o ./backups/acme-weekly

# Import (dry run by default)
tgcli -s staging import ./twingate-backup-acme-20261023T101500Z
tgcli -s staging import ./twingate-backup-acme-20261023T101500Z --execute
```

## Configuration Values

### Global Flags (before command name)
| Flag | Short | Values | Default |
|------|-------|--------|---------|
| `--session` | `-s` | Any string | **none** (required for API calls) |
| `--format` | `-f` | `JSON`, `
---
source: https://github.com/Twingate-Labs/Twingate-CLI
type: github
fetched: 2026-11-01
source_version: 1f7753aea120815497e53b9dba9972b1e06cf825
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
- Standard output carries only results; progress and advice go to standard error. Exit code `0` = success; `1` = API refused a change (printed in full on stdout, reason repeated on stderr) or any failure in a multi-item operation
- Current release: **v3.0.0**

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

To install a specific tagged release instead of latest `main`:
```
pip install "git+https://github.com/Twingate-Labs/Twingate-CLI.git@v3.0.0"
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/Twingate-Labs/Twingate-CLI.git
cd Twingate-CLI
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
pip install .
```
Windows notes: credentials go to Windows Credential Manager; if `Activate.ps1` is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` first; output is always UTF-8 (no `UnicodeEncodeError` for non-English characters); Windows PowerShell 5.1 re-encodes received output using the console code page and saves `>` redirection as UTF-16 — for clean UTF-8 files use PowerShell 7 (`pwsh`), or in 5.1 run `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` first and use `| Out-File -Encoding utf8 file.csv`; input files given to `tgcli` (e.g. `device list --fileofids`, `ca create --file`, files read by `import`) may be UTF-8 (with or without BOM) or UTF-16. Windows PowerShell 5.1 `>` redirection writes UTF-16 (use PowerShell 7 or `| Out-File -Encoding utf8`). Developed and tested on macOS; Windows support is best-effort.

## Breaking Changes in v3.0.0
- **Delete commands ask for confirmation and refuse without a terminal.** `account`, `connector`, `group`, `gateway`, `network`, `resource`, `user`, `ca`, and `dns-profile` `delete`, and `key delete` / `key revoke`, ask `[y/N]` before acting. **`--yes` (`-y`) skips the question.** Scripts that call delete commands must add `--yes` or they will exit 1.
- **A write the API refuses now exits
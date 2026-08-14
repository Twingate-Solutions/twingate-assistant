---
source: https://www.twingate.com/docs/introduction-to-the-python-cli
type: docs
fetched: 2026-08-14
source_version: 4197b82f9e3e4f2f208c4765831427d2ba6a3f695171fbb505ec083fd5a350cd
---

# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source CLI tool that wraps Twingate's GraphQL APIs to automate administrative functions available in the Admin Panel. It uses session-based authentication against a Twingate tenant and API key. Maintained outside of Twingate's core engineering team via GitHub.

## Key Information
- Supports CRUD operations on: Resources, Devices, Groups, Connectors, Users, Service Accounts, Service Account Keys, Remote Networks, Policies
- Returns JSON by default; supports CSV and DF (dataframe/table) output formats
- Session-based auth — authenticate once, reuse session name across commands
- Use `-h` at any command level for contextual help
- Available on GitHub (open source)

## Prerequisites
- Python 3
- `pandas` Python library
- Twingate API Key
- Twingate tenant name
- Clone the CLI repository locally

## Step-by-Step

### Initial Setup
```bash
git clone <repo>
cd <repo>
python3 ./tgcli.py auth list  # Returns [''] if setup is correct
```

### Authentication
```bash
python3 ./tgcli.py auth login -t <tenant> -a <apikey>
# Optional: specify session name
python3 ./tgcli.py auth login -t <tenant> -a <apikey> -s <sessionname>
```

### General Usage Pattern
```bash
python3 ./tgcli.py -s <sessionname> [-f FORMAT] <object> <operation> [params]
```

## Configuration Values

| Flag | Description | Required |
|------|-------------|----------|
| `-s SESSIONNAME` | Session name (reuse after login) | Yes (after auth) |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` | No (default: JSON) |
| `-a APIKEY` | Twingate API key | Yes (at login) |
| `-t TENANT` | Twingate tenant name | Yes (at login) |
| `-v` | Show version | No |
| `-h` | Context-sensitive help | No |

**Object types:** `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

**Auth operations:** `login`, `logout`, `list`

## Gotchas
- Missing `pandas` library causes errors on first run — install it manually if needed
- Every command requires `-s <sessionname>` after initial auth; omitting it returns `error: no session name passed`
- Session names are auto-generated (e.g., `OrangeElk`) unless `-s` is specified at login
- This is a community/open-source tool — support is via GitHub Issues, not Twingate support

## Related Docs
- Twingate GraphQL APIs
- GitHub repository (linked from docs page)
- GitHub Issues (for bug reports and feature requests)
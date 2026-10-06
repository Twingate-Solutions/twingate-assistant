---
source: https://www.twingate.com/docs/introduction-to-the-python-cli
type: docs
fetched: 2026-10-04
source_version: 223df0363bddbeed82f5b20e2d3be60c1de93e5503d254a7cc3af7abf238fb8d
trust: official
---

# Introduction to the Twingate Python CLI

## Summary
The Twingate Python CLI is an open-source tool wrapping the Twingate GraphQL APIs to automate administrative tasks available in the Admin Panel. It supports CRUD operations on Resources, Devices, Groups, Connectors, Users, Service Accounts, and Remote Networks. It is community-maintained, not officially supported by Twingate product engineering.

## Key Information
- Open-source project; support via GitHub Issues only
- Wraps Twingate GraphQL APIs
- Supports: Resources, Devices, Groups, Connectors, Users, Service Accounts, Service Account Keys, Remote Networks, Policies
- Output formats: JSON (default), CSV, DF (dataframe/table)
- Sessions persist auth credentials so you don't re-authenticate per command

## Prerequisites
- Python 3
- `pandas` library (`pip install pandas`)
- Twingate API Key
- Twingate tenant name

## Step-by-Step

### Install & Verify
1. Clone the GitHub repository
2. Navigate into the cloned folder
3. Run `python3 ./tgcli.py auth list` — empty list means ready; error means missing dependency

### Authenticate
```bash
python3 ./tgcli.py auth login -t <tenant> -a <api_key>
# Returns a random session name, e.g. "OrangeElk"

# Optional: specify your own session name
python3 ./tgcli.py auth login -t <tenant> -a <api_key> -s <session_name>
```

### Use CLI with Session
```bash
python3 ./tgcli.py -s OrangeElk resource list
python3 ./tgcli.py -s OrangeElk -f CSV resource list
python3 ./tgcli.py -s OrangeElk -f DF resource list
```

### Manage Sessions
```bash
python3 ./tgcli.py auth list    # list sessions
python3 ./tgcli.py auth logout  # remove session
```

## Configuration Values / CLI Flags

| Flag | Description |
|------|-------------|
| `-s SESSIONNAME` | Session name (required for all non-auth commands) |
| `-f OUTPUTFORMAT` | Output format: `JSON`, `CSV`, `DF` |
| `-a APIKEY` | API key for login |
| `-t TENANT` | Twingate tenant name for login |
| `-v` | Show version |
| `-h` | Contextual help at any level |

**Object types:** `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`

**Operations vary by object** — always use `-h` to discover available operations:
```bash
python3 ./tgcli.py <object> -h
python3 ./tgcli.py <object> <operation> -h
```

## Gotchas
- All commands (except `auth`) require `-s <session_name>` — omitting it causes `error: no session name passed`
- Missing `pandas` is the most common install error; install it before first use
- Session names are auto-generated (random words) unless `-s` is specified at login
- Pull updates from the repo periodically — features are actively added

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/api)
- [GitHub Repository](https://github.com/Twingate) (check for latest CLI link)
- GitHub Issues page for support
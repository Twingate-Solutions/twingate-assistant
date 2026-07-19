# Twingate Python CLI - Introduction

## Page Title
Introduction to the Twingate Python CLI

## Summary
An open-source CLI tool wrapping Twingate's GraphQL APIs to automate admin tasks available in the Admin Panel. Maintained outside core product engineering; support via GitHub Issues. Requires Python 3 and the `pandas` library.

## Key Information
- **GitHub**: Clone from the official Twingate Python CLI repository
- **Supported object types**: `auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`
- **Operations vary by object** (e.g., resource: `list`, `show`, `create`, `delete`)
- **Sessions**: Authentication is stored as named sessions; session name required for all non-auth commands
- **Output formats**: `JSON` (default), `CSV`, `DF` (dataframe/table)

## Prerequisites
- Python 3
- `pandas` library (`pip install pandas`)
- Twingate API Key
- Twingate tenant name

## Step-by-Step

### Initial Setup
```bash
git clone <repo>
cd <cli-folder>
python3 ./tgcli.py auth list   # Verify install; empty list = success
```

### Authenticate
```bash
python3 ./tgcli.py auth login -t <tenant> -a <apikey> [-s <session_name>]
# Returns auto-generated session name (e.g., "OrangeElk") if -s not specified
```

### Run Commands
```bash
python3 ./tgcli.py -s <session_name> [-f FORMAT] <object> <operation>
# Example:
python3 ./tgcli.py -s OrangeElk -f CSV resource list
```

## Configuration Values

| Flag | Description | Required |
|------|-------------|----------|
| `-s SESSIONNAME` | Session name | Yes (for most commands) |
| `-f OUTPUTFORMAT` | `JSON`, `CSV`, or `DF` | No (default: JSON) |
| `-a APIKEY` | API key for login | Yes (auth login) |
| `-t TENANT` | Tenant name for login | Yes (auth login) |
| `-v` | Show version | No |
| `-h` | Contextual help at any level | No |

## Gotchas
- All commands except `auth` require `-s <session_name>`; omitting it returns `error: no session name passed`
- Missing `pandas` is the most common install error — install and retry
- Open-source project: **not supported by Twingate product engineering**; file issues on GitHub
- Pull latest version periodically — features added incrementally

## Related Docs
- [Twingate GraphQL APIs](https://www.twingate.com/docs/)
- GitHub Issues page (for support)
---
source: https://www.twingate.com/docs/introduction-to-the-python-cli
type: docs
fetched: 2026-11-13
source_version: eafcd9d7ad058ec0346503a60ed6f463ed01de418605fb5b1867106188e17237
trust: official
---

# Introduction to the Twingate Python CLI

## Summary
The Twingate Python CLI (`tgcli.py`) wraps the Twingate GraphQL APIs to automate administrative tasks otherwise done in the Admin Console. It is an open source project maintained outside Twingate's product engineering teams; support goes through its GitHub issues page. It supports JSON, CSV, and DF output and uses named sessions to store the tenant and API token.

## Key Information
- Manageable objects: resources, devices, connectors, users, groups, service accounts (and their keys), remote networks, policies.
- Top-level object types shown in help: `auth, device, connector, user, group, resource, network, account`.
- Operations vary by object (e.g., resource: `list, show, create, delete`). Append `-h` at any level for contextual help.
- Default output is JSON. CSV suits Bash/PowerShell scripting. DF (dataframe) is a human-readable table.
- Sessions avoid re-authenticating on every command.

## Prerequisites
- Python 3
- `pandas` Python library (a missing library is the likely cause of errors on first run)
- Cloned GitHub repository for the CLI
- Twingate API token and tenant name (your network's subdomain)

## Step-by-Step
1. Clone the CLI's GitHub repository.
2. In a terminal, go to the repo folder and run `python3 ./tgcli.py auth list`. An empty list means setup is OK. If you get an error, install the missing library (likely pandas) and retry.
3. Log in: `python3 ./tgcli.py auth login -t mytenant -a mytoken`. This prints a session name (e.g., `OrangeElk`).
4. Run commands with the session: `python3 ./tgcli.py -s OrangeElk resource list`.
5. Change output format: `python3 ./tgcli.py -s OrangeElk -f CSV resource list`.

## Configuration Values (CLI flags)
- Global: `-h/--help`, `-v/--version`, `-s/--session SESSIONNAME`, `-f/--format OUTPUTFORMAT` (JSON, CSV, DF)
- `auth` operations: `login` (create session), `logout` (remove session), `list` (list sessions)
- `auth login`:
  - `-a/--apikey` API key (required)
  - `-t/--tenant` Twingate network tenant (required)
  - `-s/--session` session name (optional; random name generated if omitted)

## Gotchas
- Global flags (`-s`, `-f`) go before the object type: `tgcli.py -s NAME -f CSV resource list`.
- Running a command without a session gives the error `no session name passed`; log in first.
- Support is community-based via GitHub issues, not Twingate support.
- Pull the latest version of the repo periodically, since features are added over time.
- JSON output is hard to process in shell scripts; use CSV for that.

## Related Docs
- Twingate GraphQL API documentation
- Python CLI GitHub repository (releases and issues)
- Twingate Admin Console docs (equivalent manual functions)
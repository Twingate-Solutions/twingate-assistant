## Twingate Python CLI (`tgcli`)

Open-source Python CLI wrapping the Twingate GraphQL Admin API. **Community-maintained** -- not part of Twingate product engineering. Good fit for Python-shop teams or users who already have `pandas` available.

**Repo**: github (clone and run; no published binaries)

**Requirements**: Python 3 + `pandas` library

### Discovery Pattern

The CLI is built around **`-h` for everything** -- no need to memorize commands:

```
python3 ./tgcli.py -h                    # top-level: lists object types
python3 ./tgcli.py resource -h           # per-object: lists operations
python3 ./tgcli.py resource list -h      # per-operation: lists flags
```

### Object Types

`auth`, `device`, `connector`, `user`, `group`, `resource`, `network`, `account`, plus `policy` and `service`.

### Authentication Flow

The CLI uses **named sessions** so you don't re-enter API key + tenant on every call.

**Login:**
```
python3 ./tgcli.py auth login -t <tenant> -a <api-token>
# Token Stored in session: OrangeElk
```

The CLI generates a random session name (e.g., `OrangeElk`) -- save it. Optionally specify with `-s <session-name>` for predictable naming.

**List sessions:**
```
python3 ./tgcli.py auth list
```

**Use a session for queries:**
```
python3 ./tgcli.py -s OrangeElk resource list
```

### Output Formats

| Format | Flag | Use Case |
|---|---|---|
| **JSON** (default) | `-f JSON` | Programmatic parsing |
| **CSV** | `-f CSV` | Bash/PowerShell scripting |
| **DF** | `-f DF` | Human-readable table (pandas dataframe) |

```
python3 ./tgcli.py -s OrangeElk -f DF resource list   # readable table
python3 ./tgcli.py -s OrangeElk -f CSV resource list  # pipe to | grep, awk, etc.
```

### Capabilities (per object)

- **Resources**: list / show / add / remove / update
- **Devices**: list / show / update trust
- **Groups**: list / show / add users / remove users / add resources / remove resources / create / delete / assign policy
- **Connectors**: list / show / rename / generate tokens
- **Users**: list / show
- **Service Accounts**: list / show / create / delete / add resources / remove resources
- **Service Account Keys**: show / create / revoke / delete / rename
- **Remote Networks**: list / show
- **Policies**: list / show / assign groups

### Decision Notes

- **Use the Python CLI** when Python is your shell scripting default; functionally equivalent to the JS CLI
- For one-off automation: CLI is faster than writing custom GraphQL
- For IaC / drift management: prefer the **Terraform provider**
- Session-based auth makes scripting clean -- one login, many commands

### Gotchas

- Community-maintained -- file issues at the GitHub repo, not Twingate Support
- `pandas` is a heavy dependency for a CLI tool -- consider `pip install pandas` ahead of time, especially in containers
- Session storage is filesystem-based -- be aware on shared hosts (rotate sessions, use specific session names per user)
- The CLI output schemas may differ slightly between releases -- pin a known-good version for production scripts

### Related Docs

- /docs/introduction-to-tg-cli-javascript -- JS CLI sibling
- /docs/getting-started-with-the-api -- API token generation
- /docs/exploring-the-apis -- GraphQL exploration
- /docs/api-overview -- API reference
- /docs/terraform-getting-started -- IaC alternative

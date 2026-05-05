## Twingate JavaScript CLI (`tg`)

Open-source JavaScript CLI wrapping the Twingate GraphQL Admin API. **Community-maintained** -- not part of Twingate product engineering.

**Repo**: github (released binaries for Windows, macOS, Linux)

**Best fit for**: Node/Deno developers; users who prefer a TypeScript ecosystem; teams already standardized on JS tooling.

### Quick Reference

```
tg --help                # top-level help
tg <object> --help       # per-object commands
tg <object> <op> --help  # per-operation flags
```

**Object types**:
- `resource` (list/create/remove/add_group/remove_group)
- `group` (list/create/remove/add_user/remove_user/add_resource/remove_resource/set_policy/copy)
- `user` (list)
- `network` (list/create) -- Remote Networks
- `connector` (list/create)
- `device` (list)
- `service` (list/create/remove/add_resource/key_create) -- Service Accounts
- `policy` (list/add_group)
- `export` / `import` -- bulk operations

### First Run

```
./tg --help
./tg user list
```

On first command, the CLI prompts for **Twingate Account** (tenant subdomain) and **API Key**. Optionally save them for subsequent runs.

### Common Operations

**Create Resource:**
```
./tg resource create "<remote-network>" "<resource-name>" "<address>" [groupNames...]
```

**Create Connector:**
```
./tg connector create "<remote-network>" "<connector-name>"
```
(Returns `ACCESS_TOKEN` and `REFRESH_TOKEN` -- pipe these into Connector deployment)

**Service Account + Key:**
```
./tg service create "myService" "myResource1" "myResource2"
./tg service key_create "<service-account-id>" "keyName" "365"  # 365-day expiry
```
Output includes the JSON service key (private key, key_id) -- save it; the private key cannot be retrieved later.

### Export / Import (Bulk Operations)

**Export to xlsx (default):**
```
./tg export
```

**Export specific objects:**
```
./tg export -r -f json   # resources only, JSON format
./tg export -f svg       # graph visualization (requires GraphViz installed)
```

Available formats: `xlsx`, `json`, `dot`, `png`, `svg`. PNG/SVG require GraphViz on PATH.

**Import** uses the same xlsx format as export -- enables backup/restore or bulk seeding.

### Decision Notes

- Use the JS CLI when JS/TS is your default language; otherwise the **Python CLI** (/docs/introduction-to-the-python-cli) is functionally equivalent
- For IaC use cases: prefer the **Terraform provider** -- declarative, drift-aware, properly maintained
- For one-off ops or scripts: CLIs are quicker than crafting GraphQL queries directly

### Gotchas

- The CLI is community-maintained -- file issues at the GitHub repo, not Twingate Support
- Service Account key creation outputs the private key once -- if you lose it, you must rotate
- Bulk delete operations (`remove_bulk`) are dangerous -- always run `list` first to verify the IDs
- PNG/SVG export silently fails without GraphViz -- pre-install on CI runners

### Related Docs

- /docs/introduction-to-the-python-cli -- Python CLI sibling
- /docs/getting-started-with-the-api -- API token + GraphQL setup
- /docs/exploring-the-apis -- GraphQL exploration via Postman
- /docs/api-overview -- API reference
- /docs/terraform-getting-started -- IaC alternative

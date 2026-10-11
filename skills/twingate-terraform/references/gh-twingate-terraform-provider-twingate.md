---
source: https://github.com/Twingate/terraform-provider-twingate
type: github
fetched: 2026-10-11
source_version: 6c532028b7b93e01a36ae9204f8198877715dc6e
trust: official
---

# Twingate Terraform Provider

## Summary
Terraform provider for managing Twingate resources (networks, connectors, remote networks, resources, groups, users, service accounts). Enables infrastructure-as-code workflows for Twingate access policy and network configuration via the Twingate API.

## Key Information
- Written in Go; built on the Terraform Plugin Framework
- Supports resources and data sources for groups, remote networks, connectors, resources, users, and service accounts
- Documentation in `docs/` is auto-generated from `templates/`; edit only the templates
- Acceptance tests require a live Twingate network and API token

## Prerequisites
- Bash
- Go 1.26+
- Terraform 1.14.x
- Twingate account with an API token (Read, Write & Provision permissions) for acceptance tests

## Usage / Step-by-Step

**Build**
```shell
make build
```

**Install locally**
```shell
make install
```

**Run unit tests**
```shell
make test
```

**Run acceptance tests**
```shell
export TWINGATE_URL=twingate.com
export TWINGATE_NETWORK=<slug>
export TWINGATE_API_TOKEN=<token>
make testacc
```

**Regenerate docs**
```shell
make docs
```

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_URL` | Base Twingate URL (e.g., `twingate.com`) |
| `TWINGATE_NETWORK` | Network slug (`<slug>.twingate.com`) |
| `TWINGATE_API_TOKEN` | API token with Read, Write & Provision permissions |

## Gotchas
- Files under `docs/` are auto-generated; manual edits will be overwritten by `make docs`
- Acceptance tests (`make testacc`) run against a real Twingate network and will create/modify live resources
- The repo description references a Kubernetes controller/CRD pattern, but the actual repo is a standard Terraform provider
- `twingate_kubernetes_resource`, `twingate_ssh_resource`, and `twingate_web_app_resource` each expose a read-only `tags_all` attribute (Map of String) that includes both resource-level tags and default tags from the provider configuration

## Provider Caching and Datasource Filter Scoping

The provider can cache Resources and Groups to reduce API calls. When a cache filter (`resources_filter` / `groups_filter`) is configured, it also scopes what the corresponding datasources (`twingate_resources`, `twingate_groups`) can return:

- If at least one cached object matches a datasource lookup, the result is answered entirely from the cache — objects outside the cache filter are not returned.
- If nothing in the cache matches, the provider falls back to querying the API and returns the full result.
- To have datasources always search all objects, omit the cache filter or disable caching for that type (`resource_enabled = false` / `groups_enabled = false`).

```hcl
provider "twingate" {
  cache = {
    resource_enabled = true
    resources_filter = {
      remote_network_name = "production"
    }
  }
}
```

The `twingate_groups` and `twingate_resources` datasource docs note this scoping behavior inline.

## `name_in` / `email_in` Filters on List Datasources

All list datasources now support an `_in` filter (Set of String) that returns only objects whose name (or email, for users) exactly matches one of the values in the list:

| Datasource | Filter attribute |
|---|---|
| `twingate_connectors` | `name_in` |
| `twingate_remote_networks` | `name_in` |
| `twingate_resources` | `name_in` |
| `twingate_security_policies` | `name_in` |
| `twingate_service_accounts` | `name_in` |
| `twingate_groups` | `name_in` |
| `twingate_users` | `email_in` |

## `twingate_ssh_resource` – Downstream and Upstream Ports

The `twingate_ssh_resource` resource now
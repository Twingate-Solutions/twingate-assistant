<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Twingate Terraform Provider Overview

## Summary
The Twingate Terraform provider allows infrastructure teams to manage all Twingate resources — remote networks, connectors, resources, groups, and service accounts — as code using the official `twingate/twingate` provider from the Terraform Registry. It supports full lifecycle management including import of existing resources.

## Key Information
- **Provider source:** `twingate/twingate` on the public Terraform Registry (`registry.terraform.io/providers/twingate/twingate`)
- **Authentication:** Requires `TWINGATE_API_TOKEN` (API key from Twingate Admin Console) and `TWINGATE_NETWORK` (your tenant name, e.g. `acme` for `acme.twingate.com`); both can be set as environment variables or in the provider block
- **Core resource set:** `twingate_remote_network`, `twingate_connector`, `twingate_connector_tokens`, `twingate_resource`, `twingate_group`, `twingate_service_account`, `twingate_service_account_key`
- **Key data sources:** `data.twingate_connector`, `data.twingate_group`, `data.twingate_resource`, `data.twingate_remote_network` — used to reference existing objects not managed by the current module
- **Import support:** All managed resources support `terraform import`, enabling adoption of pre-existing Twingate configuration without recreation
- **Provider version pinning:** Always pin the provider version in `required_providers` to avoid unintended upgrades; the provider follows semantic versioning

## Prerequisites
- A Twingate account with Admin or Owner role
- An API key generated in the Twingate Admin Console under Settings → API
- Terraform 1.0 or later (the provider uses the Terraform Plugin Framework)
- `TWINGATE_API_TOKEN` and `TWINGATE_NETWORK` available as environment variables or supplied in the provider block (never hard-code tokens in `.tf` files)

## Step-by-Step
1. Declare the provider in `required_providers`:
   ```hcl
   terraform {
     required_providers {
       twingate = {
         source  = "twingate/twingate"
         version = "~> 3.0"
       }
     }
   }
   ```
2. Configure the provider (prefer env vars for secrets; only set `network` in the block if not using `TWINGATE_NETWORK`):
   ```hcl
   provider "twingate" {
     api_token = var.twingate_api_token   # or set TWINGATE_API_TOKEN
     network   = var.twingate_network     # or set TWINGATE_NETWORK
   }
   ```
3. Create a remote network (logical grouping for connectors in one location):
   ```hcl
   resource "twingate_remote_network" "aws_prod" {
     name = "AWS Production"
   }
   ```
4. Create a connector and generate its tokens:
   ```hcl
   resource "twingate_connector" "aws_prod_1" {
     remote_network_id = twingate_remote_network.aws_prod.id
     name              = "aws-prod-connector-1"
   }

   resource "twingate_connector_tokens" "aws_prod_1" {
     connector_id = twingate_connector.aws_prod_1.id
   }
   ```
5. Define a protected resource with access rules:
   ```hcl
   resource "twingate_resource" "internal_api" {
     name               = "Internal API"
     address            = "api.internal.example.com"
     remote_network_id  = twingate_remote_network.aws_prod.id

     protocols {
       allow_icmp = false
       tcp {
         policy = "RESTRICTED"
         ports  = ["443", "8443"]
       }
       udp {
         policy = "DENY_ALL"
       }
     }

     access {
       group_ids           = [twingate_group.devs.id]
       security_policy_id  = var.default_policy_id
     }
   }
   ```
6. Use `terraform import` to bring existing resources under Terraform management:
   ```bash
   terraform import twingate_remote_network.aws_prod <remote_network_id>
   terraform import twingate_connector.aws_prod_1 <connector_id>
   ```

## Configuration Values
- `api_token`: Twingate API key (32-character string); source from a secret manager or env var
- `network`: Tenant subdomain only, not the full URL — `acme` not `acme.twingate.com`
- `twingate_resource.protocols.tcp.policy`: `"ALLOW_ALL"` | `"RESTRICTED"` | `"DENY_ALL"`
- `twingate_resource.protocols.udp.policy`: `"ALLOW_ALL"` | `"RESTRICTED"` | `"DENY_ALL"`
- `twingate_resource.access.security_policy_id`: UUID of a Twingate Security Policy; omit to use the tenant default
- `twingate_connector_tokens` outputs: `access_token` and `refresh_token` — both are sensitive; used to configure the connector at deploy time

## Gotchas
- **`twingate_connector_tokens` is write-once:** Destroying and recreating `twingate_connector_tokens` generates new credentials and invalidates the old ones; the running connector will lose connectivity until restarted with the new tokens
- **`principal_id` vs `group_ids`:** Older provider versions used an `access` block with `principal_id` referencing users, groups, or service accounts individually; newer versions use `group_ids`, `service_account_ids` directly — check the provider version changelog before copying older examples
- **Network name uniqueness:** `twingate_remote_network` names must be unique within a tenant; Terraform will error on apply if a duplicate name exists outside its state
- **Data sources require exact matches:** `data.twingate_group` looks up by name — if the group name changes outside Terraform, the data source will fail on next plan
- **Sensitive outputs:** `twingate_connector_tokens.access_token` and `.refresh_token` are marked sensitive; use `nonsensitive()` carefully and never output them to logs
- **Import IDs:** All resource import IDs are the Twingate object UUID, available from the Admin Console URL or via the Twingate GraphQL API — not the human-readable name

## Related Docs
- `/docs/guides/terraform` — Official Twingate Terraform provider guide
- `/docs/api-reference` — Twingate GraphQL API (underlying API the provider uses)
- `/docs/connectors/connector-deployment` — Manual connector deployment reference
- `/docs/access-control/resource-access` — Access rules, security policies, and group assignments
- `/docs/service-accounts` — Service accounts and key management for non-human access

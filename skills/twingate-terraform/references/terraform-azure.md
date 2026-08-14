---
source: https://www.twingate.com/docs/terraform-azure
type: docs
fetched: 2026-08-14
source_version: 7d253c79382582e85a66024fcfb2124fdf9f1d67ab49931cfa42c80346b7b9de
---

# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure vNet using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance running the Connector, and a test VM). The Connector runs as an Azure Container Instance on a delegated subnet. Access is validated via SSH to the private VM through Twingate.

## Key Information
- Providers required: `twingate/twingate`, `hashicorp/azurerm` (v3.0.0), `hashicorp/random` (v3.3.2)
- Connector runs as `azurerm_container_group` using image `twingate/connector:1`
- Two subnets needed: container subnet (delegated to `Microsoft.ContainerInstance/containerGroups`) and general VM subnet
- Connector tokens (`access_token`, `refresh_token`) are passed as env vars to the container
- Twingate API token requires **Read, Write & Provision** permissions

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate account with API token generated at **Settings → API → Generate Token**
- Twingate tenant name (e.g., `mycorp` from `https://mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads providers
5. `terraform plan` — validate (non-destructive)
6. `terraform apply` — deploys ~14 resources
7. Add a Twingate user to the created group in Admin Console
8. Test: `ssh testadmin@<private_ip>`; retrieve password with `terraform output password`
9. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
tg_api_key       = "<api_token>"
tg_network       = "<tenant_name>"
subscription_id  = "<azure_subscription_id>"
tenant_id        = "<azure_tenant_id>"
client_id        = ""
client_secret    = ""
```

**Container env vars:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | `twingate_connector_tokens.*.access_token` |
| `TWINGATE_REFRESH_TOKEN` | `twingate_connector_tokens.*.refresh_token` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**Container specs:** CPU=1, Memory=1.5GB, UDP port 9999

**Twingate Resource ports:** TCP 80, 22 (RESTRICTED); UDP ALLOW_ALL; ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- Passwords stored in Terraform state file; use Azure Key Vault for production
- Container subnet must have delegation to `Microsoft.ContainerInstance/containerGroups` with specific actions
- VM private IP is dynamic; retrieve actual IP from Azure portal or state after apply
- `azurerm` pinned to `=3.0.0`; may not be latest — check for updates
- Must manually add user to Twingate group after apply for access to work

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Azure Provider Authentication Options](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- Twingate Connector deployment docs
- Terraform code structure guides (HashiCorp)
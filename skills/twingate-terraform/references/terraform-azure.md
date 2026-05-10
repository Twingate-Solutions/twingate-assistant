# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance for the connector, and a test VM). The connector runs as an Azure Container Instance with private networking.

## Key Information
- Providers required: `twingate/twingate`, `hashicorp/azurerm` (3.0.0), `hashicorp/random` (3.3.2)
- Connector deployed as Azure Container Instance (`twingate/connector:1`) on a delegated subnet
- Two subnets needed: container subnet (`10.0.2.0/24`) and general subnet (`10.0.1.0/24`) within `10.0.0.0/16` vNet
- Container subnet requires `Microsoft.ContainerInstance/containerGroups` delegation
- Twingate resource restricts TCP to ports 80 and 22; UDP allows all; ICMP enabled

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads providers
5. `terraform plan` — validate (expect 14 resources)
6. `terraform apply` — confirm with `yes`
7. Add Twingate user to the created group in Admin Console
8. Test: `ssh testadmin@<private_ip>`; retrieve password with `terraform output password`
9. Teardown: `terraform destroy`

## Configuration Values

### terraform.tfvars
| Variable | Description |
|---|---|
| `tg_api_key` | Twingate API token |
| `tg_network` | Twingate tenant name (e.g., `mycorp`) |
| `subscription_id` | Azure subscription ID |
| `tenant_id` | Azure tenant ID |
| `client_id` | Azure service principal client ID |
| `client_secret` | Azure service principal secret |

### Container Environment Variables
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | From `twingate_connector_tokens` resource |
| `TWINGATE_REFRESH_TOKEN` | From `twingate_connector_tokens` resource |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext secrets
- Passwords stored in Terraform state file in plaintext; use Azure Key Vault for production
- `azurerm` version pinned to `=3.0.0` — newer versions may have breaking changes
- Container subnet must have explicit delegation to `Microsoft.ContainerInstance/containerGroups` or deployment fails
- User must be manually added to the Twingate group after `terraform apply` before access works
- Software versions in guide may not be latest — verify against official docs

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/Twingate/twingate/latest
- Azure provider authentication options: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- Terraform code structure best practices (linked in doc)
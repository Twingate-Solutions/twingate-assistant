# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates deployment of a complete Twingate-secured Azure environment using Terraform. Creates a Twingate Remote Network, Connector (as Azure Container Instance), and Resource alongside Azure vNet, subnets, and a test VM. Enables full infrastructure lifecycle management via `terraform apply` / `terraform destroy`.

## Key Information
- Deploys Twingate Connector as an Azure Container Instance (`twingate/connector:1`) on a dedicated delegated subnet
- Creates two subnets: container subnet (`10.0.2.0/24`) and general/VM subnet (`10.0.1.0/24`) within a `/16` vNet
- Twingate Resource restricts TCP to ports 80 and 22; UDP allows all; ICMP enabled
- VM uses password auth (random 16-char password); password stored in Terraform state file
- Total resources created: 14 (across both Azure and Twingate)

## Prerequisites
- Terraform installed
- Azure credentials: `subscription_id`, `tenant_id`, `client_id`, `client_secret`
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with providers (azurerm `3.0.0`, twingate latest, random `3.3.2`)
3. Create `terraform.tfvars` with credentials (see Configuration Values below)
4. `terraform init` — downloads providers
5. `terraform plan` — validate config (non-destructive)
6. `terraform apply` — confirm with `yes`
7. Add Twingate user to the created group in Admin Console
8. Connect: `ssh testadmin@<vm_private_ip>` via Twingate client
9. Retrieve VM password: `terraform output password`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
tg_api_key        = "<twingate_api_token>"
tg_network        = "<tenant_name>"
subscription_id   = "<azure_subscription_id>"
tenant_id         = "<azure_tenant_id>"
client_id         = "<azure_client_id>"
client_secret     = "<azure_client_secret>"
```

**Container environment variables:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_REFRESH_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**Container:** `twingate/connector:1`, 1 CPU, 1.5GB RAM, UDP port 9999

## Gotchas
- **Never commit `terraform.tfvars` to source control** — contains plaintext credentials
- Terraform state file stores the VM password in plaintext; use Azure Key Vault for production
- Container subnet requires delegation to `Microsoft.ContainerInstance/containerGroups`
- `azurerm` pinned to `=3.0.0` — newer versions may have breaking changes
- Image tags (`twingate/connector:1`) may not be latest; check official docs
- Must manually add a Twingate user to the created group before the resource is accessible

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Azure Provider Authentication Options](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- Twingate: Settings → API for token generation
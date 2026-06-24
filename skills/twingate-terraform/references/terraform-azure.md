# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Terraform, creating a Remote Network, Connector, and Resource alongside Azure infrastructure (vNet, container instance running the Connector, and a test VM). All resources are defined in a single `main.tf` with credentials in `terraform.tfvars`.

## Key Information
- Providers required: `hashicorp/azurerm` (3.0.0), `twingate/twingate`, `hashicorp/random` (3.3.2)
- Connector runs as an Azure Container Instance (`twingate/connector:1`) in a delegated subnet
- Two subnets created: container subnet (`10.0.2.0/24`) and VM subnet (`10.0.1.0/24`)
- Twingate resource restricts TCP to ports 80 and 22; UDP allows all; ICMP allowed

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads providers
5. `terraform plan` — validate (non-destructive)
6. `terraform apply` — confirm with `yes`; creates 14 resources
7. Add Twingate user to the created group via Admin Console
8. `terraform output password` — retrieve VM password
9. `ssh testadmin@<private_ip>` to verify connectivity
10. `terraform destroy` — tear down all resources

## Configuration Values

### terraform.tfvars
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"          # e.g., "mycorp" from mycorp.twingate.com
subscription_id="<azure_sub_id>"
tenant_id="<azure_tenant_id>"
client_id="<service_principal_id>"
client_secret="<service_principal_secret>"
```

### Container Environment Variables
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_REFRESH_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

### Container Resources
- CPU: `1`, Memory: `1.5` GB, Port: `9999/UDP`

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext secrets
- Passwords stored in Terraform state file in plaintext; use Azure Key Vault for production
- `azurerm` version pinned to `3.0.0` — check for updates before production use
- Container subnet requires delegation to `Microsoft.ContainerInstance/containerGroups`
- Must manually add users to the Twingate group after `apply`; Terraform doesn't manage user membership here
- Software/image versions in guide may be outdated

## Related Docs
- [Twingate Terraform Provider (Terraform Registry)](https://registry.terraform.io/providers/Twingate/twingate)
- [Azure provider authentication options](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- Twingate Terraform GCP guide, AWS guide
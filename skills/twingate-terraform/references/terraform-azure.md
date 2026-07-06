# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure vNet using Terraform, creating all required components: Remote Network, Connector, Connector Tokens, Group, and Resource. The connector runs as an Azure Container Instance (ACI) on a private subnet. A test Ubuntu VM is provisioned to validate connectivity.

## Key Information
- Providers required: `twingate/twingate`, `hashicorp/azurerm` (3.0.0), `hashicorp/random` (3.3.2)
- Connector deployed as `azurerm_container_group` using image `twingate/connector:1`
- Two subnets: container subnet (`10.0.2.0/24`) and VM subnet (`10.0.1.0/24`)
- Container subnet requires delegation to `Microsoft.ContainerInstance/containerGroups`
- Twingate resource restricts TCP to ports 80 and 22; UDP allows all

## Prerequisites
- Terraform installed
- Azure service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate API key with Read, Write & Provision permissions (Settings → API → Generate Token)
- Twingate tenant name

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with providers, variables, and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads providers
5. `terraform plan` — validates config (non-destructive)
6. `terraform apply` — deploys ~14 resources
7. Add Twingate user to the created group in Admin Console
8. Connect: `ssh testadmin@<vm_private_ip>` via Twingate client
9. Retrieve password: `terraform output password`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
tg_api_key        = "<api_token>"
tg_network        = "<tenant_name>"   # e.g., "mycorp" from mycorp.twingate.com
subscription_id   = "<azure_sub_id>"
tenant_id         = "<azure_tenant_id>"
client_id         = ""
client_secret     = ""
```

**Container environment variables:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_REFRESH_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

## Gotchas
- **Never commit `terraform.tfvars`** to source control — contains plaintext credentials
- Terraform state file stores the VM password in plaintext; use Azure Key Vault for production
- `azurerm` version pinned to `=3.0.0` — may not be latest; check for updates
- Container image `twingate/connector:1` may not be latest version
- VM private IP (`10.0.1.4`) may vary; check Azure portal after apply
- Must manually add users to the Twingate group after deployment for access

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/Twingate/twingate/latest
- Azure provider authentication options: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- Terraform code structure guides (linked in source)
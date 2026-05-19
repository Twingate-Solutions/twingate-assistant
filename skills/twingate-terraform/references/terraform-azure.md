# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance running the Connector, test VM). The Connector runs as an Azure Container Instance with private networking.

## Key Information
- Single `main.tf` file approach; variables stored in `terraform.tfvars`
- Connector deployed as `azurerm_container_group` with `ip_address_type = "Private"`
- Two subnets required: one for container instance (`10.0.2.0/24`), one for VMs (`10.0.1.0/24`)
- Container subnet requires delegation to `Microsoft.ContainerInstance/containerGroups`
- Twingate API token needs **Read, Write & Provision** permissions
- `twingate_connector_tokens` resource generates `access_token` and `refresh_token` for the connector

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate account with API token (Read/Write/Provision)
- Twingate tenant name (subdomain portion of `https://<tenant>.twingate.com`)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with providers (azurerm 3.0.0, twingate, random 3.3.2)
3. Create `terraform.tfvars` with credentials
4. `terraform init`
5. `terraform plan` (verify 14 resources to add)
6. `terraform apply` → confirm with `yes`
7. Add Twingate user to the created group via Admin Console
8. Test: `ssh testadmin@<private_ip>`; retrieve password via `terraform output password`
9. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
tg_api_key        = "<api_token>"
tg_network        = "<tenant_name>"
subscription_id   = "<azure_subscription_id>"
tenant_id         = "<azure_tenant_id>"
client_id         = ""
client_secret     = ""
```

**Container env vars:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | `twingate_connector_tokens.access_token` |
| `TWINGATE_REFRESH_TOKEN` | `twingate_connector_tokens.refresh_token` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**Container:** image `twingate/connector:1`, CPU `1`, memory `1.5`, UDP port `9999`

**VM:** `Standard_B1ls`, Ubuntu 22.04 LTS, admin user `testadmin`

**Twingate Resource ports:** TCP 80, 22 (RESTRICTED); UDP ALLOW_ALL; ICMP allowed

## Gotchas
- **`terraform.tfvars` must be excluded from source control** — contains plaintext credentials
- Passwords stored in Terraform state file in plaintext; use Azure Key Vault for production
- `azurerm` pinned to `=3.0.0` — newer versions may have API changes
- Container subnet requires explicit delegation block or deployment fails
- Must manually add users to the Twingate group after `terraform apply` — not automated in this config
- `network_profile_id` on `azurerm_container_group` is deprecated in newer azurerm versions

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Azure Provider Authentication](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret)
- Twingate API: Settings → API → Generate Token
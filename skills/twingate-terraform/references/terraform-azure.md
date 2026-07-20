# Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance running the connector, and a test VM). The connector runs as an Azure Container Instance within a dedicated subnet with private IP only.

## Key Information
- Connector deployed as Azure Container Instance (`twingate/connector:1`) with private IP
- Two subnets required: one for container instance (`10.0.2.0/24`), one for VMs (`10.0.1.0/24`)
- Container subnet requires `Microsoft.ContainerInstance/containerGroups` delegation
- Connector communicates via UDP port 9999
- VM password stored in Terraform state file — use Azure Key Vault in production

## Prerequisites
- Terraform installed
- Azure subscription with service principal (subscription_id, tenant_id, client_id, client_secret)
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with providers (azurerm `3.0.0`, twingate, random `3.3.2`)
3. Create `terraform.tfvars` with credentials
4. `terraform init`
5. `terraform plan` — verify 14 resources to add
6. `terraform apply` — confirm with `yes`
7. Add Twingate user to the created group in Admin Console
8. Test: `ssh testadmin@<private_ip>` (retrieve password via `terraform output password`)
9. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
tg_api_key        = "<Twingate API token>"
tg_network        = "<tenant name>"  # 'mycorp' from mycorp.twingate.com
subscription_id   = "<Azure subscription ID>"
tenant_id         = "<Azure tenant ID>"
client_id         = "<service principal client ID>"
client_secret     = "<service principal secret>"
```

**Container env vars:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_REFRESH_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**Resource protocol config:** TCP ports 80, 22 (RESTRICTED); UDP ALLOW_ALL; ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains secrets in plaintext
- Passwords are stored in Terraform state file; use Azure Key Vault for production
- `terraform plan` is non-destructive and safe to run anytime for validation
- Provider versions are pinned examples; check for latest versions before use
- Azure region hardcoded to `West Europe` — adjust to match your environment
- IP ranges (`10.0.0.0/16`) are demo values — adjust for production

## Related Docs
- [Twingate Terraform Provider (Registry)](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Azure Authentication methods](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs#authenticating-to-azure)
- Twingate Terraform on GCP/AWS guides (parallel docs)
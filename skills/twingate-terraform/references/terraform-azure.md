# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure vNet using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance running the connector, and a test VM). The connector runs as an Azure Container Instance with private networking.

## Key Information
- Uses three providers: `twingate/twingate`, `hashicorp/azurerm` (3.0.0), `hashicorp/random` (3.3.2)
- Connector deployed as Azure Container Instance (`twingate/connector:1`) on a delegated subnet
- Two subnets required: container subnet (`10.0.2.0/24`) and general/VM subnet (`10.0.1.0/24`)
- Container subnet must be delegated to `Microsoft.ContainerInstance/containerGroups`
- Twingate Resource restricts TCP to ports 80 and 22; UDP allows all; ICMP enabled

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads providers
5. `terraform plan` — validate config
6. `terraform apply` — deploy (~14 resources created)
7. Add user to the Twingate group in Admin Console
8. `terraform output password` — retrieve VM password
9. `terraform destroy` — teardown

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"
subscription_id="<azure_sub_id>"
tenant_id="<azure_tenant_id>"
client_id=""
client_secret=""
```

**Container env vars:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_REFRESH_TOKEN` | from `twingate_connector_tokens` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**Container specs:** CPU: 1, Memory: 1.5GB, Port: 9999/UDP

## Gotchas
- **Never commit `terraform.tfvars`** — contains plaintext API keys and credentials
- Passwords stored in Terraform state file — use Azure Key Vault for production
- `azurerm` version pinned to `=3.0.0`; check compatibility before upgrading
- Container subnet delegation actions must include both `join/action` and `prepareNetworkPolicies/action`
- User must be manually added to the Twingate group after deployment for access to work
- `twingate_connector_tokens` is a separate resource from `twingate_connector` — both required

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twingate)
- [Azure Authentication methods](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs#authenticating-to-azure)
- Twingate Terraform GCP guide (parallel guide for GCP deployments)
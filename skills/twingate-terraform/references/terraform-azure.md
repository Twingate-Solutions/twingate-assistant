# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates deployment of Twingate on Azure vNet using Terraform, creating all required Twingate components (Remote Network, Connector, Resource, Group) alongside Azure infrastructure (vNet, subnets, container instance running the Connector, test VM). The Connector runs as an Azure Container Instance (ACI) on a delegated subnet.

## Key Information
- Providers required: `twingate/twingate`, `hashicorp/azurerm` (3.0.0), `hashicorp/random` (3.3.2)
- Connector deployed as Azure Container Instance using image `twingate/connector:1`
- Two subnets needed: container subnet (10.0.2.0/24) with ACI delegation, general subnet (10.0.1.0/24) for VM
- ACI subnet requires `Microsoft.ContainerInstance/containerGroups` service delegation
- Connector tokens (`access_token`, `refresh_token`) passed as container environment variables

## Prerequisites
- Terraform installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks
3. `terraform init`
4. Create `terraform.tfvars` with credentials
5. `terraform plan` — validate config
6. `terraform apply` — confirm with `yes`
7. Add Twingate user to the created group in Admin Console
8. Connect via Twingate client; SSH to VM using `terraform output password`
9. `terraform destroy` to tear down

## Configuration Values

**terraform.tfvars:**
```
tg_api_key=""
tg_network=""          # tenant subdomain only (e.g. "mycorp")
subscription_id=""
tenant_id=""
client_id=""
client_secret=""
```

**Container environment variables:**
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `var.tg_network` |
| `TWINGATE_ACCESS_TOKEN` | `twingate_connector_tokens.*.access_token` |
| `TWINGATE_REFRESH_TOKEN` | `twingate_connector_tokens.*.refresh_token` |
| `TWINGATE_TIMESTAMP_FORMAT` | `"2"` |

**ACI specs:** CPU: 1, Memory: 1.5GB, Port: 9999/UDP

**Twingate Resource ports:** TCP 80, 22 (RESTRICTED); UDP ALLOW_ALL; ICMP allowed

## Gotchas
- `terraform.tfvars` contains secrets — **exclude from source control**
- Passwords stored in Terraform state file; use Azure Key Vault for production
- `tg_network` is the subdomain only, not the full URL
- ACI subnet must have delegation block or deployment fails
- VM uses password auth (`disable_password_authentication = false`) — consider SSH keys for production
- Container image tag `twingate/connector:1` may not be latest

## Related Docs
- Twingate Terraform Provider: registry.terraform.io/providers/twingate/twingate
- Azure authentication options: registry.terraform.io/providers/hashicorp/azurerm
- Terraform code structure guides (linked in source)
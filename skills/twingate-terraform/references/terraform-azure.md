# Terraform with Azure and Twingate

## Page Title
How to Use Terraform with Azure and Twingate

## Summary
Automates Twingate deployment on Azure using Terraform, creating a Remote Network, Connector, Group, and Resource alongside Azure infrastructure (vNet, subnets, container instance running the Connector, and a test VM). The Connector runs as an Azure Container Instance (ACI) on a dedicated subnet with delegation to `Microsoft.ContainerInstance/containerGroups`.

## Key Information
- Providers required: `twingate/twingate`, `hashicorp/azurerm` (3.0.0), `hashicorp/random` (3.3.2)
- Connector deployed as ACI (`twingate/connector:1`) on private subnet `10.0.2.0/24`
- Test VM deployed on subnet `10.0.1.0/24` (Ubuntu 22.04, `Standard_B1ls`)
- ACI subnet requires delegation to `Microsoft.ContainerInstance/containerGroups`
- Twingate API key needs Read, Write & Provision permissions

## Prerequisites
- Terraform CLI installed
- Azure subscription with service principal credentials (subscription_id, tenant_id, client_id, client_secret)
- Twingate account with API token (Settings → API → Generate Token with Read/Write/Provision)

## Step-by-Step
1. `mkdir twingate_azure_demo && cd twingate_azure_demo`
2. Create `main.tf` with provider blocks for azurerm, twingate, random
3. `terraform init`
4. Create `terraform.tfvars` with credentials
5. Add Twingate resources: `twingate_remote_network` → `twingate_connector` → `twingate_connector_tokens`
6. Add Azure resources: resource group → vNet → subnets (container + general) → network profile → ACI (connector) → NIC → VM
7. Add Twingate `twingate_group` and `twingate_resource` pointing to VM's private IP
8. `terraform plan` to validate
9. `terraform apply` to deploy
10. Add user to Twingate group; SSH to VM via Twingate client
11. `terraform destroy` to tear down

## Configuration Values

**terraform.tfvars:**
```
tg_api_key=""         # Twingate API token
tg_network=""         # Twingate tenant name (e.g., "mycorp")
subscription_id=""
tenant_id=""
client_id=""
client_secret=""
```

**Container env vars:**
```
TWINGATE_NETWORK          = var.tg_network
TWINGATE_ACCESS_TOKEN     = twingate_connector_tokens...access_token
TWINGATE_REFRESH_TOKEN    = twingate_connector_tokens...refresh_token
TWINGATE_TIMESTAMP_FORMAT = "2"
```

**ACI port:** UDP 9999

**Twingate Resource protocols:** TCP ports 80, 22 (RESTRICTED); UDP ALLOW_ALL; ICMP allowed

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- Passwords stored in Terraform state file; use Azure Key Vault for production
- Container subnet must have `Microsoft.ContainerInstance/containerGroups` delegation with specific actions
- `azurerm` pinned to `=3.0.0`; newer versions may have breaking changes
- VM IP (`10.0.1.4`) is dynamically assigned; actual address may differ
- Retrieve VM password with `terraform output password`

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Azure provider authentication options](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- Twingate docs: Terraform with GCP, Terraform with AWS
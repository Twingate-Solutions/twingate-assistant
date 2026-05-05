## Terraform: Twingate on Azure

End-to-end Terraform recipe deploying Twingate alongside an Azure resource group: VNet, two subnets (one delegated to ACI), Twingate Connector running as an Azure Container Instance, test VM, and full Twingate config.

**Required Providers:**
- `hashicorp/azurerm` `=3.0.0`
- `twingate/twingate`
- `hashicorp/random` `3.3.2` (generates VM password)

**terraform.tfvars (do not commit):**
- `tg_api_key`, `tg_network` -- Twingate token + tenant
- `subscription_id`, `tenant_id`, `client_id`, `client_secret` -- Azure service principal (or use other auth)

**Connector Deployment: Azure Container Instance (ACI)**

Unlike the AWS guide (VM + AMI), Azure uses a Container Instance for the Connector:
- Image: `twingate/connector:1`
- CPU: 1, Memory: 1.5 GB
- `os_type = "Linux"`, `ip_address_type = "Private"`
- Port 9999/UDP exposed (P2P)
- Environment variables:
  - `TWINGATE_NETWORK` = tenant
  - `TWINGATE_ACCESS_TOKEN` = `twingate_connector_tokens.X.access_token`
  - `TWINGATE_REFRESH_TOKEN` = `twingate_connector_tokens.X.refresh_token`
  - `TWINGATE_TIMESTAMP_FORMAT` = `2`

**Subnet Delegation (Required for ACI):**
The container subnet needs a delegation block delegating to `Microsoft.ContainerInstance/containerGroups` with actions `Microsoft.Network/virtualNetworks/subnets/join/action` and `Microsoft.Network/virtualNetworks/subnets/prepareNetworkPolicies/action`.

`azurerm_network_profile` ties the ACI to the delegated subnet -- required for private IP.

**Twingate Resource Pattern:**
```
resource "twingate_resource" "demo" {
  name              = "azure demo web server"
  address           = azurerm_network_interface.test_vm_nic.private_ip_address
  remote_network_id = twingate_remote_network.demo.id
  group_ids         = [twingate_group.demo.id]
  protocols {
    allow_icmp = true
    tcp { policy = "RESTRICTED"; ports = ["80","22"] }
    udp { policy = "ALLOW_ALL" }
  }
}
```

**Random Password Output:**
- `random_password` resource generates the VM admin password
- Outputted with `sensitive = true`; retrieve via `terraform output password`
- **Note:** Passwords persist in Terraform state -- use Azure Key Vault for production

**Workflow:**
1. `terraform init`, `terraform plan`, `terraform apply` (creates ~14 resources)
2. Add a Twingate user to the new Group
3. SSH to the VM private IP via Twingate Client (e.g., `ssh testadmin@10.0.1.4`)
4. `terraform destroy` to tear down

**Gotchas:**
- `azurerm` provider version `=3.0.0` is pinned in the doc -- check Registry for newer compatible versions before using in production
- ACI requires subnet delegation; without it, the container group fails to start
- `azurerm_virtual_machine` is the legacy resource -- newer code should use `azurerm_linux_virtual_machine` / `azurerm_windows_virtual_machine`
- Sensitive values (passwords, tokens) live in state -- protect the state file (remote backend with encryption + access control)

**Related Docs:**
- /docs/terraform-getting-started -- Provider overview
- /docs/terraform-aws, /docs/terraform-gcp -- Other clouds
- /docs/azure -- Manual Azure Connector deployment

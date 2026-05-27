# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployment on GCP using Terraform. Creates a complete setup including Remote Network, Connector, Twingate Resource, and Group alongside GCP VPC, subnet, firewall, and two VMs (webserver + connector).

## Key Information
- Uses two Terraform providers: `twingate/twingate` (v0.1.10) and `hashicorp/google`
- Connector tokens are injected into the connector VM via a startup script template
- Total resources created: 10 (3 Twingate + 7 GCP)
- Connector VM installs Twingate via `setup.sh` using `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` env vars

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (the `mycorp` portion of `https://mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with `tg_api_key` and `tg_network` values
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (non-destructive)
7. `terraform apply` — deploy all 10 resources
8. Manually add users to the created Twingate group via Admin Console (Team → Groups)

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<API_TOKEN>"
tg_network="<tenant_name>"
```

**Provider config:**
```hcl
provider "twingate" {
  api_token = var.tg_api_key
  network   = var.tg_network
}
provider "google" {
  project = "<gcp-project-id>"
  region  = "europe-west2"
  zone    = "europe-west2-c"
}
```

**Connector install template (`twingate_client.tftpl`):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**GCP subnet CIDR:** `172.16.0.0/24`  
**VM type:** `e2-micro`  
**Image:** `ubuntu-2204-lts`  
**Firewall:** TCP port 80, source restricted to subnet CIDR

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- Provider version `0.1.10` referenced in guide may be outdated; check [Terraform Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- VM provisioning takes several minutes; wait ~5 min before testing connection
- User-to-group assignment is manual (not covered in Terraform code) due to IdP integrations (e.g., Entra ID)
- `resource` in Terraform context ≠ Twingate Resource object

## Related Docs
- [Twingate Terraform Provider (Registry)](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Terraform Code Structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP Terraform Credentials](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
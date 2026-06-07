# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for deploying Twingate on GCP using Terraform. Creates a complete setup including Remote Network, Connector, connector tokens, VPC networking, two VMs (webserver + connector), a Twingate Group, and a Twingate Resource. Uses Twingate provider v0.1.10 and Hashicorp Google provider.

## Key Information
- Two Terraform providers required: `twingate/twingate` and `hashicorp/google`
- Connector tokens are injected into the connector VM via a template file (`twingate_client.tftpl`)
- Total resources created: 10 (3 Twingate + 7 GCP)
- Connector installed via curl script using `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` env vars
- User-to-group assignment must be done manually via Admin Console or identity provider

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with `tg_api_key` and `tg_network` values
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect: 10 to add)
7. `terraform apply` — deploy all resources
8. Manually add users to the created group in Admin Console (Team → Groups)

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"
```

**Provider config:**
```hcl
provider "twingate" {
  api_token = var.tg_api_key
  network   = var.tg_network
}
provider "google" {
  project = "<project_id>"
  region  = "europe-west2"
  zone    = "europe-west2-c"
}
```

**Connector install template env vars:**
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_URL` = `https://${tgnetwork}.twingate.com`

**GCP resources:**
- Machine type: `e2-micro`
- Image: `ubuntu-2204-lts`
- Subnet CIDR: `172.16.0.0/24`
- Firewall: TCP port 80, source restricted to subnet

## Gotchas
- **Never commit `terraform.tfvars`** to source control — contains plaintext API token
- VM provisioning takes several minutes; wait ~5 min before testing connection
- Twingate provider version in guide (`0.1.10`) may be outdated — check [Terraform Registry](https://registry.terraform.io/providers/twingate/twingate/latest)
- `resource` in Terraform HCL is not the same as a Twingate Resource (different concepts)
- `access_config {}` block on network interfaces assigns public IPs to VMs — review for production security

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twingate/latest)
- Twingate Connector setup: `https://binaries.twingate.com/connector/setup.sh`
- GCP Terraform authentication guide
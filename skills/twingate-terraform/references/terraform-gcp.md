# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for deploying Twingate on a GCP VPC using Terraform, creating all required components: Remote Network, Connector, Connector Tokens, GCP networking, VMs, Twingate Group, and Resource. All infrastructure is defined in a single `main.tf` with a supporting template file for connector installation.

## Key Information
- Deploys 10 total resources: 3 Twingate objects + 7 GCP objects
- Connector is installed via startup script using curl setup.sh with token injection
- Twingate Terraform provider: `twingate/twingate` (example uses v0.1.10)
- GCP provider: `hashicorp/google` (auto-latest)
- Subnet CIDR: `172.16.0.0/24`; firewall allows TCP port 80 from within subnet only
- VMs use `e2-micro`, `ubuntu-2204-lts` image

## Prerequisites
- Terraform CLI installed
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources (see Configuration Values)
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 10 to add)
7. `terraform apply` — deploy all resources
8. Manually add user to the created group: Team → Groups

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api-token>"
tg_network="<tenant-name>"
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

**Connector install template** (`template/twingate_client.tftpl`):
```bash
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**Key Twingate resource types:**
- `twingate_remote_network`
- `twingate_connector` (requires `remote_network_id`)
- `twingate_connector_tokens` (requires `connector_id`)
- `twingate_group`
- `twingate_resource` (with `protocols` block)

## Gotchas
- **Never commit `terraform.tfvars`** to source control — contains plaintext API token
- Provider version `0.1.10` shown in example may not be latest — check [Terraform Registry](https://registry.terraform.io/providers/twingate/twingate/latest)
- VM startup scripts (Nginx + Connector install) take ~5 minutes after `apply` completes
- `resource` in Terraform HCL ≠ Twingate Resource concept
- User-to-group assignment is manual (not in this Terraform example) due to typical IdP integrations
- `twingate_connector_tokens` outputs are marked **sensitive** — won't display in plan output

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twin
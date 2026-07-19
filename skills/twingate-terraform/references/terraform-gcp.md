# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Deploys a complete Twingate setup on GCP using Terraform, including a Remote Network, Connector, Group, and Resource. Creates two GCP VMs (one Nginx webserver, one Twingate Connector) within a custom VPC. Uses Twingate and Google Terraform providers together.

## Key Information
- Creates 10 total resources: 3 Twingate objects + 7 GCP objects
- Connector installed via startup script using `setup.sh` with injected access/refresh tokens
- Resource access restricted to TCP port 80; uses a template file for connector setup script
- Twingate provider version used: `0.1.10` (check registry for latest)

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference))
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with both providers configured
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 10 resources)
7. `terraform apply` — deploy all resources
8. Manually add users to the created Twingate group via Admin Console

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
  project = "<gcp-project-id>"
  region  = "europe-west2"
  zone    = "europe-west2-c"
}
```

**Connector template (`template/twingate_client.tftpl`):**
```bash
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**Key resource parameters:**
- Subnet CIDR: `172.16.0.0/24`
- VM type: `e2-micro`
- Image: `ubuntu-2204-lts`
- Firewall: TCP port 80, source restricted to subnet range

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- VM provisioning takes ~5 minutes after `terraform apply` completes; wait before testing
- User-to-group assignment must be done manually in the Admin Console (not in this Terraform config)
- `twingate_connector_tokens` outputs are marked sensitive; won't appear in plan output
- The `resource` keyword in Terraform HCL ≠ Twingate Resource concept

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Terraform code structure guides](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP provider authentication](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference)
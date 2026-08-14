---
source: https://www.twingate.com/docs/terraform-gcp
type: docs
fetched: 2026-08-14
source_version: e3915f1de3ed367aec3ce87203e32c403a39242b4aa8f59594a089090b03d2fb
---

# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on GCP using Terraform. Creates a complete demo environment including a Twingate Remote Network, Connector, Group, and Resource alongside GCP VPC, subnet, firewall, and two VMs (webserver + connector).

## Key Information
- Uses two Terraform providers: `twingate/twingate` and `hashicorp/google`
- Connector tokens are generated via Terraform and injected into VM startup scripts via a template file
- Creates 10 total resources (3 Twingate, 7 GCP)
- Twingate Resource is scoped to port 80 TCP, ALLOW_ALL UDP, ICMP enabled

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect "10 to add")
7. `terraform apply` — deploy all resources
8. Manually add users to the GCP Demo group in Twingate UI (Team → Groups)

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<your-api-token>"
tg_network="<your-tenant-name>"
```

**Provider versions:**
```
twingate: 0.1.10
hashicorp/google: ~4.30.0
```

**GCP defaults (adjust for your environment):**
```
project = "twingate-projects"
region  = "europe-west2"
zone    = "europe-west2-c"
subnet  = "172.16.0.0/24"
machine_type = "e2-micro"
image = "projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts"
```

**Connector install template (`twingate_client.tftpl`):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- Provider version `0.1.10` referenced in guide may not be latest; check [Terraform Registry](https://registry.terraform.io/providers/twingate/twingate)
- VM provisioning takes ~5 minutes after `apply` completes before connector shows as active
- User-to-group assignment is manual via UI (not in Terraform config shown)
- `twingate_resource` in Terraform is not the same as Terraform's generic `resource` keyword

## Related Docs
- [Twingate Terraform Provider (Registry)](https://registry.terraform.io/providers/twingate/twingate)
- [Terraform Code Structure Guide](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP Provider Auth](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
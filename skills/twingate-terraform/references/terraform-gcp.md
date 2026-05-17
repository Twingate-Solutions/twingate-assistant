# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for deploying Twingate on a GCP VPC using Terraform. Creates a complete setup including Remote Network, Connector, Connector tokens, VPC/subnet/firewall, webserver VM, connector VM, Twingate Group, and Twingate Resource. Uses Twingate Terraform provider alongside the Google provider.

## Key Information
- Deploys 10 total resources (3 Twingate, 7 GCP)
- Connector installed on GCP VM via startup script using `setup.sh` from Twingate binaries
- Connector tokens passed to VM via Terraform template file (`.tftpl`)
- Group membership must be managed manually (or via identity provider integration)

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([Terraform GCP auth docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with both `twingate` and `google` providers
3. Create `terraform.tfvars` with `tg_api_key` and `tg_network`
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 10 resources)
7. `terraform apply` — deploy all resources
8. Manually add users to the created Twingate group in Admin Console

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api-token>"
tg_network="<tenant-name>"
```

**Provider versions (guide uses):**
- `twingate/twingate`: `0.1.10` (check registry for latest)
- `hashicorp/google`: `4.30.0` (auto-resolved)

**GCP defaults in guide:**
- Region: `europe-west2`, Zone: `europe-west2-c`
- Subnet CIDR: `172.16.0.0/24`
- Machine type: `e2-micro`
- Image: `ubuntu-2204-lts`

**Connector install template (`twingate_client.tftpl`):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**Twingate Resource protocol config:**
- TCP: `RESTRICTED`, ports `["80"]`
- UDP: `ALLOW_ALL`
- ICMP: allowed

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API key
- VM provisioning takes ~5 minutes before connector shows as active in Twingate UI
- Provider version `0.1.10` referenced in guide may be outdated — check [Terraform Registry](https://registry.terraform.io/providers/twingate/twingate/latest)
- `resource` in Terraform HCL ≠ Twingate Resource concept
- Firewall only allows port 80 intra-subnet; adjust for other applications
- GCP project name (`twingate-projects`) must be changed to your actual project

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twingate/latest)
- [Terraform Code Structure Guide](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP Terraform Authentication](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide to deploying Twingate on GCP using Terraform, creating a Remote Network, Connector, and Resource alongside GCP VPC infrastructure. Uses both the Twingate and Google Terraform providers to fully automate the setup. Results in a private web server accessible only through Twingate.

## Key Information
- Deploys 10 total resources: 3 Twingate objects + 7 GCP infrastructure objects
- Connector installed via bash script using `setup.sh` from Twingate binaries
- Connector tokens passed to GCP VM via `templatefile()` and a `.tftpl` startup script
- Group assignment to users must be done manually via Admin Console (or separate IDP integration)

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with both providers configured
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (non-destructive)
7. `terraform apply` — deploy all 10 resources
8. Manually add users to the created Twingate group in Admin Console

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"
```

**Provider versions (in guide; check registry for latest):**
- `twingate/twingate`: `0.1.10`
- `hashicorp/google`: `4.30.0`

**GCP defaults in guide:**
- `project`: `twingate-projects`
- `region`: `europe-west2` / `zone`: `europe-west2-c`
- `machine_type`: `e2-micro`
- `subnet`: `172.16.0.0/24`
- OS image: `ubuntu-2204-lts`

**Connector install template (`twingate_client.tftpl`):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**Twingate Resource protocol config:**
- TCP: `RESTRICTED`, port `80`
- UDP: `ALLOW_ALL`
- ICMP: allowed

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- Provider version in guide (`0.1.10`) may be outdated; check [Terraform Registry](https://registry.terraform.io/providers/twingate/twingate)
- VM provisioning takes ~5 minutes after `apply` before connector is active
- `resource` in Terraform HCL ≠ Twingate Resource (different concepts)
- Firewall rule only allows port 80 within subnet — adjust for other applications
- User-to-group assignment not automated in this guide

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twingate)
- [Terraform code structure guides](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP provider authentication](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
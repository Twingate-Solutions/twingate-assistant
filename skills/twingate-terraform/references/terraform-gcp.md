# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide for deploying Twingate on a GCP VPC using Terraform, creating all required components (Remote Network, Connector, Connector Tokens) and GCP infrastructure (VPC, subnet, firewall, VMs). Uses a template file to inject Connector tokens into the GCP VM startup script.

## Key Information
- Requires two Terraform providers: `twingate/twingate` and `hashicorp/google`
- Connector tokens are passed to the GCP VM via `metadata_startup_script` using a `.tftpl` template file
- Total resources created: 10 (3 Twingate + 7 GCP)
- Template file path: `./template/twingate_client.tftpl`

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference))
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, Twingate resources, and GCP resources
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 10 to add)
7. `terraform apply` — deploy all resources
8. Manually add users to the created Twingate group via Admin Console

## Configuration Values

**terraform.tfvars:**
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"
```

**Provider versions (guide uses):**
- `twingate/twingate`: `0.1.10` (check for latest)
- `hashicorp/google`: `4.30.0` (latest resolved)

**GCP config (adjust per environment):**
- `project`: `twingate-projects`
- `region`: `europe-west2`
- `zone`: `europe-west2-c`
- Subnet CIDR: `172.16.0.0/24`
- Machine type: `e2-micro`
- Image: `ubuntu-2204-lts`

**Template file (`twingate_client.tftpl`) variables:**
- `${accessToken}` — from `twingate_connector_tokens`
- `${refreshToken}` — from `twingate_connector_tokens`
- `${tgnetwork}` — from `var.tg_network`

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- Provider version `0.1.10` is outdated; check [Terraform Registry](https://registry.terraform.io/providers/Twingate/twingate/latest) for current version
- VM provisioning takes ~5 minutes after `terraform apply` completes before Connector is online
- User-to-group assignment must be done manually in the Admin Console (not in this Terraform config)
- Firewall only opens port 80 within the subnet — adjust `ports` for other applications

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Terraform Code Structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
- [GCP Provider Authentication](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference)
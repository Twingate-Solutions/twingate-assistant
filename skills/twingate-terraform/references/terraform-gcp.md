# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Automates deployment of Twingate infrastructure (Remote Network, Connector, Resource, Group) on GCP using Terraform. Creates a demo environment with a VPC, subnet, firewall, webserver VM (nginx), and Connector VM. Uses two providers: `twingate/twingate` and `hashicorp/google`.

## Key Information
- Single `main.tf` file approach with separate `terraform.tfvars` for secrets
- Connector installed via startup script using `twingate_connector_tokens` output
- Template file (`template/twingate_client.tftpl`) injects connector tokens into bash installer
- Total resources created: 10 (3 Twingate + 7 GCP)
- Twingate provider version used: `0.1.10` (check registry for latest)

## Prerequisites
- Terraform CLI installed
- GCP credentials configured (see Terraform GCP auth docs)
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with `tg_api_key` and `tg_network`
4. Create `template/twingate_client.tftpl` with connector setup script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect "10 to add")
7. `terraform apply` — deploy all resources
8. Manually add users to the created Twingate group via Admin Console (Team → Groups)

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

**Connector install template (`twingate_client.tftpl`):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**GCP resources:** subnet `172.16.0.0/24`, machine type `e2-micro`, image `ubuntu-2204-lts`, firewall allows TCP port 80 from subnet only.

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API key
- VM startup scripts take ~5 minutes; connector won't appear online immediately
- `resource` in Terraform HCL ≠ Twingate Resource (different concepts)
- `twingate_connector_tokens` outputs are marked **sensitive** — won't display in plan output
- User-to-group assignment not covered by this Terraform config; must be done manually or via IdP integration
- GCP credentials must be pre-configured separately before `terraform init`

## Related Docs
- Twingate Terraform Provider Registry (latest version)
- Terraform code structure guides
- GCP authentication for Terraform (Hashicorp docs)
- Twingate Connector setup documentation
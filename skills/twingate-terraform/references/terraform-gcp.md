# Terraform with GCP and Twingate

## Page Title
How to Use Terraform with GCP and Twingate

## Summary
Step-by-step guide to automating Twingate deployment on GCP using Terraform. Creates a complete stack including Remote Network, Connector, GCP VPC, subnets, firewall rules, VMs, Twingate Group, and Resource. Uses two Terraform providers: `twingate/twingate` and `hashicorp/google`.

## Key Information
- Creates 10 total resources: 3 Twingate objects + 7 GCP infrastructure objects
- Connector installation uses a `.tftpl` template file to inject access/refresh tokens at VM startup
- All code lives in `main.tf` plus `terraform.tfvars` and `template/twingate_client.tftpl`
- Group-to-user assignment must be done manually via Admin Console (not shown in Terraform code)

## Prerequisites
- Terraform installed locally
- GCP credentials configured ([GCP auth setup](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started))
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- Twingate tenant name (the `mycorp` portion of `https://mycorp.twingate.com`)

## Step-by-Step

1. `mkdir twingate_gcp_demo && cd twingate_gcp_demo`
2. Create `main.tf` with provider blocks, variables, and all resources (see Configuration Values)
3. Create `terraform.tfvars` with API key and network name
4. Create `template/twingate_client.tftpl` with connector install script
5. `terraform init` — downloads providers
6. `terraform plan` — validate (non-destructive)
7. `terraform apply` — deploy all 10 resources
8. Manually add users to the created group in Admin Console (Team → Groups)

## Configuration Values

**terraform.tfvars**
```
tg_api_key="<api_token>"
tg_network="<tenant_name>"
```

**Provider versions**
- `twingate/twingate`: `0.1.10`
- `hashicorp/google`: `4.30.0` (latest at time of writing)

**GCP defaults used**
- Region: `europe-west2`, Zone: `europe-west2-c`
- Subnet CIDR: `172.16.0.0/24`
- Machine type: `e2-micro`
- Image: `ubuntu-2204-lts`

**Connector template** (`template/twingate_client.tftpl`)
```bash
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```

**Twingate Resource protocol config**
```hcl
protocols {
  allow_icmp = true
  tcp  { policy = "RESTRICTED"; ports = ["80"] }
  udp  { policy = "ALLOW_ALL" }
}
```

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API token
- Connector and webserver VMs may take **several minutes** to fully provision after `terraform apply` completes
- Provider version `0.1.10` is referenced in this doc — check [Terraform Registry](https://registry.terraform.io/providers/Twingate/twingate/latest) for latest
- `access_config {}` block in `network_interface` assigns a public IP to VMs — review for production
- Firewall rule only allows TCP port 80 within the subnet CIDR; adjust for other applications
- `twingate_resource` (Terraform) ≠ Terraform `resource` keyword — don't confuse the two

## Related Docs
- [Twingate Terraform Provider (Registry)](https://registry.terraform.io/providers/Twingate/twingate/latest)
- [Terraform Code Structure Guide](
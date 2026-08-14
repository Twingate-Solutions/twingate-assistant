---
source: https://www.twingate.com/docs/terraform-aws
type: docs
fetched: 2026-08-14
source_version: 520e15dbe2dc9f194f8e6d8d384a58fa23857f96d34adfc3e6f7a1f21aac4fec
---

# Terraform with AWS and Twingate

## Page Title
How to Use Terraform with AWS and Twingate

## Summary
Automates deployment of a Twingate-secured AWS VPC using Terraform, creating a Remote Network, Connector, Group, and Resource alongside AWS infrastructure (VPC, subnets, EC2 instances). The setup provisions two EC2 instances: a private test VM (no public IP) and a Twingate Connector VM (public IP, outbound-only). Result is SSH access to a private VM via Twingate without exposing it to the internet.

## Key Information
- Two Terraform providers required: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Twingate Connector uses official AMI (owner: `617935088040`)
- Ubuntu test VM uses Canonical AMI (owner: `099720109477`, ubuntu-jammy-22.04)
- Connector configured via `user_data` script writing to `/etc/twingate/connector.conf`
- Resource allows TCP port 22 only (RESTRICTED), UDP ALLOW_ALL, ICMP enabled
- Total resources created: 13 (`terraform plan` output)

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate account with API token (Read, Write & Provision permissions)
- SSH keypair generated locally (`ssh-keygen`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH keypair: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and all resources
4. Create `terraform.tfvars` with credentials (see Configuration Values)
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 13 resources to add)
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. Connect: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<twingate_api_token>"
tg_network="<tenant_name>"  # 'mycorp' from mycorp.twingate.com
```

**Connector user_data env vars (written to /etc/twingate/connector.conf):**
```
TWINGATE_URL="https://<network>.twingate.com"
TWINGATE_ACCESS_TOKEN="<access_token>"
TWINGATE_REFRESH_TOKEN="<refresh_token>"
```

**Key resource parameters:**
- VPC CIDR: `10.0.0.0/16`
- Subnet CIDR: `10.0.1.0/24`
- Region: `eu-west-1`
- Instance type: `t3.micro` (both VMs)

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API tokens and AWS credentials
- Connector VM needs `associate_public_ip_address = true` for outbound internet access; test VM must NOT have public IP
- API token requires Read, Write & Provision permissions; restrict by IP if possible
- Must manually add a Twingate user to the created group before the resource appears in the client
- AMI filters use wildcards — versions may change; verify current AMIs if builds fail
- `terraform destroy` removes all Twingate config AND AWS infrastructure — verify plan before confirming

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/Twingate/twingate/latest
- AWS provider authentication options: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- Terraform code structure best practices (referenced but not linked in source)
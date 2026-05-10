# Terraform with AWS and Twingate

## Page Title
How to Use Terraform with AWS and Twingate

## Summary
Step-by-step guide to deploying Twingate on AWS using Terraform, creating a Remote Network, Connector, Group, and Resource alongside AWS VPC infrastructure. The setup provisions two EC2 instances: a private test VM and a Twingate Connector with outbound internet access.

## Key Information
- Deploys 13 total resources (4 Twingate + 9 AWS)
- Uses Twingate AMI from AWS Marketplace (owner: `617935088040`)
- Connector configured via `user_data` bootstrap script writing to `/etc/twingate/connector.conf`
- Single `main.tf` file structure; variables in `terraform.tfvars`
- AWS region hardcoded to `eu-west-1` in example — change as needed

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- SSH key pair generated locally (`ssh-keygen`)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Create `main.tf` with provider blocks, variables, and all resources
3. Create `terraform.tfvars` with credentials
4. `terraform init` — downloads AWS and Twingate providers
5. `terraform plan` — validate before applying
6. `terraform apply` — confirm with `yes`
7. Add Twingate user to the created group in Admin Console
8. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
9. Cleanup: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<token>"
tg_network="<tenant>"
```

**Connector user_data env vars** (written to `/etc/twingate/connector.conf`):
```
TWINGATE_URL="https://<network>.twingate.com"
TWINGATE_ACCESS_TOKEN="<access_token>"
TWINGATE_REFRESH_TOKEN="<refresh_token>"
```

**Key resource parameters:**
- VPC CIDR: `10.0.0.0/16`
- Subnet CIDR: `10.0.1.0/24`
- Instance type: `t3.micro`
- Ubuntu AMI owner: `099720109477` (Canonical)
- Twingate AMI owner: `617935088040`
- Resource protocol: TCP port 22 restricted, UDP allow all, ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- Connector requires outbound internet access (`associate_public_ip_address = true`) but no inbound
- Test VM has no public IP — only accessible via Twingate
- Must manually assign a Twingate user to the created group before the resource appears in the client
- AWS provider pinned to `~> 4.0`; Twingate provider unpinned (gets latest)
- Image versions in guide may not be current — verify AMI filters against latest available

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/twingate/twingate
- Terraform code structure best practices
- AWS authentication methods for Terraform
- Twingate Connector documentation
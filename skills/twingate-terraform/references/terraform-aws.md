# Terraform with AWS and Twingate

## Summary
Step-by-step guide to deploying Twingate on AWS using Terraform, creating a Remote Network, Connector, Group, and Resource alongside AWS VPC infrastructure. The setup provisions two EC2 instances: a private test VM and a Twingate Connector with outbound internet access.

## Key Information
- Uses two Terraform providers: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Connector VM uses official Twingate AMI (owner: `617935088040`)
- Connector configured via `user_data` bash script writing to `/etc/twingate/connector.conf`
- Connector requires outbound internet only; no inbound public access needed
- Total resources created: 13 (4 Twingate + 9 AWS)

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API key with **Read, Write & Provision** permissions
- SSH key pair generated (`ssh-keygen`)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with providers, variables, and all resources
4. Create `terraform.tfvars` with credentials
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 13 resources)
7. `terraform apply` — deploy
8. Add Twingate user to the created group in Admin Console
9. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<api_token>"
tg_network="<tenant_name>"
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
- AWS region: `eu-west-1`
- Instance type: `t3.micro`
- Ubuntu AMI owner: `099720109477` (Canonical), filter: `ubuntu-jammy-22.04-amd64`
- Twingate AMI owner: `617935088040`, filter: `twingate-amd64-*`
- Resource protocol: TCP port 22 restricted, UDP allow all, ICMP allowed

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- Test VM has no public IP; access only via Twingate after user is added to the group
- Connector VM needs `associate_public_ip_address = true` for outbound connectivity
- `twingate_connector_tokens` outputs are marked sensitive in plan output
- Image versions in the guide may be outdated; verify AMI filters against current releases

## Related Docs
- [Twingate Terraform Provider (Terraform Registry)](https://registry.terraform.io/providers/Twingate/twingate/latest)
- Twingate Admin Console: Settings → API → Generate Token
- AWS authentication methods documentation
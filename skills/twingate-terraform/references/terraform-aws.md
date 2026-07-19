# Terraform with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate on AWS using Terraform. Creates a complete setup including VPC, two EC2 instances (Connector + test VM), Remote Network, Connector, Group, and Resource. Connector uses Twingate AMI with cloud-init configuration.

## Key Information
- Creates 13 Terraform resources total across AWS and Twingate
- Two EC2 VMs: Twingate Connector (public IP, outbound internet) and test VM (private only)
- Connector bootstrapped via `user_data` script writing to `/etc/twingate/connector.conf`
- Twingate API key requires **Read, Write & Provision** permissions
- AWS region hardcoded to `eu-west-1` in example — change as needed

## Prerequisites
- Terraform installed
- AWS account with Access Key ID + Secret Access Key
- Twingate account with API token (Read/Write/Provision)
- SSH key pair generated (`ssh-keygen`)
- Twingate client installed for testing

## Step-by-Step

1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and resources
4. Create `terraform.tfvars` with credentials
5. `terraform init` — downloads AWS and Twingate providers
6. `terraform plan` — validate (expect "13 to add")
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID="..."
AWS_SECRET_ACCESS_KEY="..."
tg_api_key="..."
tg_network="mycorp"  # subdomain only, not full URL
```

**Connector user_data env vars** (written to `/etc/twingate/connector.conf`):
```
TWINGATE_URL="https://<network>.twingate.com"
TWINGATE_ACCESS_TOKEN="..."
TWINGATE_REFRESH_TOKEN="..."
```

**Key AWS/Twingate values:**
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`
- Instance type: `t3.micro`
- Ubuntu AMI owner: `099720109477` (Canonical)
- Twingate AMI owner: `617935088040`
- Twingate AMI filter: `twingate/images/hvm-ssd/twingate-amd64-*`
- Resource protocol: TCP port 22 RESTRICTED, UDP ALLOW_ALL, ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- Connector requires outbound internet access but no inbound — no security group for SSH on connector VM in this example
- AMI references may not be latest versions — verify before production use
- `tg_network` is the subdomain only (e.g., `mycorp` not `mycorp.twingate.com`)
- Must manually add a user to the Twingate group after apply to enable access

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate/latest)
- Twingate Connector documentation
- AWS authentication methods (alternative to access key/secret)
- Terraform code structure best practices
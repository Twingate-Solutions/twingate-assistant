# Terraform with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate on AWS using Terraform. Creates a complete setup including VPC, two EC2 instances (Connector + test VM), Twingate Remote Network, Connector, Group, and Resource. All infrastructure is managed as code and can be created/destroyed with single commands.

## Key Information
- Uses two Terraform providers: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Deploys two VMs: private test VM (Ubuntu) + public-facing Twingate Connector (Twingate AMI)
- Connector only requires outbound internet access; test VM has no public IP
- Twingate AMI owner ID: `617935088040`; Ubuntu AMI owner ID: `099720109477`
- Connector config written via `user_data` to `/etc/twingate/connector.conf`

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate account with API token (Read, Write & Provision permissions)
- SSH key pair generated (`ssh-keygen`)
- Twingate tenant name (subdomain portion of `https://mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH keys: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with providers, variables, and all resources
4. Create `terraform.tfvars` with credentials
5. `terraform init` — downloads providers
6. `terraform plan` — validate configuration
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<token>"
tg_network="<tenant-name>"
```

**Connector user_data env vars** (written to `/etc/twingate/connector.conf`):
- `TWINGATE_URL` — `https://<network>.twingate.com`
- `TWINGATE_ACCESS_TOKEN` — from `twingate_connector_tokens`
- `TWINGATE_REFRESH_TOKEN` — from `twingate_connector_tokens`

**Key resource settings:**
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`, Region: `eu-west-1`
- Instance type: `t3.micro` for both VMs
- Resource protocol: TCP port 22 (RESTRICTED), UDP ALLOW_ALL, ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext credentials
- `twingate_connector_tokens` are marked sensitive in Terraform state
- Connector VM needs `associate_public_ip_address = true` for outbound connectivity
- Must manually add a Twingate user to the created group before the resource is accessible
- Code references specific AWS provider version `~> 4.0` — check for updates
- `terraform plan` is non-destructive; always review before `apply` or `destroy`

## Related Docs
- [Twingate Terraform Provider (Terraform Registry)](https://registry.terraform.io/providers/Twingate/twingate)
- Twingate API token: Settings → API → Generate Token
- AWS authentication alternatives: AWS provider auth docs
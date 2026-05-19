# Terraform with AWS and Twingate

## Page Title
How to Use Terraform with AWS and Twingate

## Summary
Step-by-step guide to deploying Twingate on AWS using Terraform. Creates a complete setup including VPC, two EC2 instances (Connector + test VM), and Twingate Remote Network/Connector/Group/Resource configuration. All infrastructure managed as code in a single `main.tf` file.

## Key Information
- Requires two Terraform providers: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Deploys two VMs: Twingate Connector (public IP) and private test VM (no public access)
- Connector configured via `user_data` script writing to `/etc/twingate/connector.conf`
- Twingate AMI owner ID: `617935088040`; Ubuntu AMI owner: `099720109477`
- Default region in example: `eu-west-1`; VPC CIDR: `10.0.0.0/16`; Subnet: `10.0.1.0/24`

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API token with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- SSH key pair generated (`ssh-keygen` → `~/.ssh/aws_id_rsa`)
- Twingate tenant name (e.g., `mycorp` from `mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and all resources
4. Create `terraform.tfvars` with credentials
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 13 resources to add)
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. SSH test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<token>"
tg_network="<tenant_name>"
```

**Connector user_data env vars:**
```
TWINGATE_URL="https://${var.tg_network}.twingate.com"
TWINGATE_ACCESS_TOKEN="<from twingate_connector_tokens>"
TWINGATE_REFRESH_TOKEN="<from twingate_connector_tokens>"
```

**Key Terraform resources:**
- `twingate_remote_network` — requires `name`
- `twingate_connector` — requires `remote_network_id`
- `twingate_connector_tokens` — requires `connector_id`
- `twingate_resource` — requires `name`, `address`, `remote_network_id`, `group_ids`, `protocols`
- Instance type: `t3.micro` for both VMs

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext secrets
- Connector VM needs `associate_public_ip_address = true` for outbound internet access
- Test VM has **no public IP**; access only via Twingate
- Resource protocol example restricts TCP to port 22 only — adjust for real workloads
- Software versions in guide may not be current — verify AMI filters and provider versions

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/Twingate/twingate/latest
- AWS provider authentication options: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- Terraform code structure best practices
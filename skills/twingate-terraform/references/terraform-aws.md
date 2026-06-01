# Terraform with AWS and Twingate

## Page Title
How to Use Terraform with AWS and Twingate

## Summary
Automates deployment of a Twingate-secured AWS environment using Terraform. Creates a VPC with two EC2 instances (a private test VM and a Twingate Connector), plus all Twingate configuration (Remote Network, Connector, Group, Resource). The Connector uses a Twingate AMI and is configured via `user_data` at boot.

## Key Information
- Uses two Terraform providers: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Twingate AMI owner ID: `617935088040`; Ubuntu AMI owner ID: `099720109477`
- Connector requires only outbound internet access; test VM has no public IP
- Connector tokens (`access_token`, `refresh_token`) are sensitive values passed via `user_data`
- Config written to `/etc/twingate/connector.conf` on the connector VM
- Service started with: `sudo systemctl enable --now twingate-connector`

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API key with **Read, Write & Provision** permissions
- SSH key pair generated (`ssh-keygen` → `~/.ssh/aws_id_rsa`)
- Twingate tenant name (subdomain from `https://<tenant>.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH keys: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and all resources
4. Create `terraform.tfvars` with credentials (exclude from source control)
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 13 resources to add)
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. Connect via Twingate client, then SSH: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. `terraform destroy` — tear down everything

## Configuration Values

**terraform.tfvars**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key=""
tg_network=""        # subdomain only, e.g. "mycorp"
```

**Connector user_data env vars**
```
TWINGATE_URL="https://${var.tg_network}.twingate.com"
TWINGATE_ACCESS_TOKEN="<from twingate_connector_tokens>"
TWINGATE_REFRESH_TOKEN="<from twingate_connector_tokens>"
```

**Key resource parameters**
- VPC CIDR: `10.0.0.0/16`; Subnet: `10.0.1.0/24`; Region: `eu-west-1`
- Instance type: `t3.micro` for both VMs
- Resource protocol: TCP port 22 restricted, UDP allow-all, ICMP allowed

## Gotchas
- **Never commit `terraform.tfvars`** to source control — contains plaintext secrets
- Connector VM needs `associate_public_ip_address = true` for outbound internet; test VM should not have this
- AMI filters use wildcards — versions may change; verify filters return valid AMIs
- Code samples may reference outdated provider versions; check Terraform Registry for latest
- Must manually add a Twingate user to the created group before the resource appears in the client

## Related Docs
- [Twingate Terraform Provider (Registry)](https://registry.terraform.io/providers/Twingate/twingate/latest)
- Twingate Admin Console: Settings → API → Generate Token
- AWS credentials documentation (IAM Access Keys)
- Terraform code structure best practices
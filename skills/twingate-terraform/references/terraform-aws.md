# Terraform with AWS and Twingate

## Page Title
How to Use Terraform with AWS and Twingate

## Summary
Automates deployment of a Twingate-secured AWS VPC using Terraform. Creates a Remote Network, Connector, Group, and Resource in Twingate alongside AWS VPC infrastructure (subnet, gateway, routing, two EC2 instances). The Connector VM bridges Twingate to a private test VM with no public IP.

## Key Information
- Two providers required: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Two EC2 instances: Twingate Connector (public IP, Twingate AMI) and private test VM (Ubuntu AMI)
- Connector configured via `user_data` script writing to `/etc/twingate/connector.conf`
- Connector only needs outbound internet access; test VM has no public interface
- Twingate AMI owner ID: `617935088040`; Ubuntu AMI owner ID: `099720109477`

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API key with **Read, Write & Provision** permissions (Settings → API → Generate Token)
- SSH key pair generated locally (`ssh-keygen`)
- Twingate tenant name (e.g., `mycorp` from `https://mycorp.twingate.com`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH keypair: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and all resources
4. Create `terraform.tfvars` with credentials (exclude from source control)
5. `terraform init` — downloads providers
6. `terraform plan` — validate before applying
7. `terraform apply` — creates 13 resources total
8. Add Twingate user to the created group via Admin Console
9. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<twingate_api_key>"
tg_network="<tenant_name>"
```

**Connector user_data env vars written to `/etc/twingate/connector.conf`:**
```
TWINGATE_URL="https://<network>.twingate.com"
TWINGATE_ACCESS_TOKEN="<access_token>"
TWINGATE_REFRESH_TOKEN="<refresh_token>"
```

**Key resource parameters:**
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`
- Instance type: `t3.micro` for both VMs
- AWS region: `eu-west-1` (hardcoded in example)
- Resource protocol: TCP port 22 restricted, UDP allow all, ICMP enabled

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API keys and AWS credentials
- AWS region (`eu-west-1`) is hardcoded in provider block — change for your environment
- `twingate_connector_tokens` creates sensitive `access_token` and `refresh_token` — marked as sensitive values in plan output
- Software/AMI versions in guide may not be latest — verify current Twingate AMI name pattern
- Must manually add users to the Terraform-created group after deployment for access to work

## Related Docs
- Twingate Terraform Provider: https://registry.terraform.io/providers/Twingate/twingate/latest
- AWS authentication methods: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- Terraform code structure guides (linked in doc)
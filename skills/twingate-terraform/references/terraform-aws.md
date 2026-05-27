# Terraform with AWS and Twingate

## Summary
Deploys a complete Twingate-secured AWS environment using Terraform, including a Remote Network, Connector, Resource, and Group alongside AWS VPC infrastructure. The setup creates two EC2 instances: a private test VM and a Twingate Connector with outbound internet access. All resources are managed in a single `main.tf` file.

## Key Information
- Uses official `twingate/twingate` and `hashicorp/aws ~> 4.0` Terraform providers
- Twingate Connector uses the official Twingate AMI (owner: `617935088040`)
- Connector configured via `user_data` script writing to `/etc/twingate/connector.conf`
- Connector only needs outbound internet access (no inbound rules required)
- Resource restricted to TCP port 22; UDP allows all; ICMP enabled

## Prerequisites
- Terraform installed
- AWS account with Access Key ID and Secret Access Key
- Twingate API token with **Read, Write & Provision** permissions
- SSH key pair generated locally (`~/.ssh/aws_id_rsa`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with providers, variables, and all resources
4. Create `terraform.tfvars` with credentials (exclude from source control)
5. `terraform init` — downloads providers
6. `terraform plan` — validate 13 resources to add
7. `terraform apply` — deploy infrastructure
8. Add Twingate user to the created group in Admin Console
9. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<twingate_api_token>"
tg_network="<tenant_name>"   # 'mycorp' from mycorp.twingate.com
```

**Connector user_data env vars written to `/etc/twingate/connector.conf`:**
```
TWINGATE_URL="https://<network>.twingate.com"
TWINGATE_ACCESS_TOKEN="<access_token>"
TWINGATE_REFRESH_TOKEN="<refresh_token>"
```

**Key resource parameters:**
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`, Region: `eu-west-1`
- Instance type: `t3.micro` for both VMs
- Ubuntu AMI owner: `099720109477` (Canonical), filter: `ubuntu-jammy-22.04-amd64`
- Twingate AMI owner: `617935088040`, filter: `twingate-amd64-*`

## Gotchas
- **Exclude `terraform.tfvars` from source control** — contains plaintext API tokens and AWS credentials
- Connector VM requires `associate_public_ip_address = true` for outbound connectivity
- Test VM has no public IP — access only via Twingate after setup
- `twingate_connector_tokens` are marked sensitive; won't display in plan output
- Image versions in the guide may not be current — verify AMI filters against latest available

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/twingate/twingate)
- [AWS Provider Authentication](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Code Structure Guide](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
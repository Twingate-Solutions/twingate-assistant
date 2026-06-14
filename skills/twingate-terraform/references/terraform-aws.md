# Terraform with AWS and Twingate

## Summary
Step-by-step guide to deploying Twingate on AWS using Terraform. Creates a complete setup including VPC, two EC2 instances (Connector + test VM), and all Twingate configuration (Remote Network, Connector, Group, Resource). Connector uses Twingate's official AMI with cloud-init configuration.

## Key Information
- Two providers required: `hashicorp/aws` (~> 4.0) and `twingate/twingate`
- Twingate AMI owner ID: `617935088040`; Ubuntu AMI owner: `099720109477`
- Connector needs outbound internet access only (no inbound); test VM is fully private
- Connector configured via `/etc/twingate/connector.conf` using `user_data`
- Demo restricts Resource to TCP port 22 only; ICMP allowed

## Prerequisites
- Terraform installed
- AWS account with Access Key ID + Secret Access Key
- Twingate API token with **Read, Write & Provision** permissions
- SSH key pair generated locally (`~/.ssh/aws_id_rsa`)

## Step-by-Step
1. `mkdir twingate_aws_demo && cd twingate_aws_demo`
2. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
3. Create `main.tf` with provider blocks, variables, and all resources
4. Create `terraform.tfvars` with credentials (exclude from source control)
5. `terraform init` — downloads providers
6. `terraform plan` — validate (expect 13 resources)
7. `terraform apply` — deploy
8. Add Twingate user to the created group in Admin Console
9. Connect: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private_ip>`
10. Teardown: `terraform destroy`

## Configuration Values

**terraform.tfvars:**
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
tg_api_key="<twingate_api_token>"
tg_network="<tenant_name>"  # e.g. "mycorp" from mycorp.twingate.com
```

**Connector user_data environment variables:**
```
TWINGATE_URL="https://${var.tg_network}.twingate.com"
TWINGATE_ACCESS_TOKEN="<from twingate_connector_tokens>"
TWINGATE_REFRESH_TOKEN="<from twingate_connector_tokens>"
```

**Key Terraform resources:**
| Resource | Type |
|---|---|
| `twingate_remote_network` | Remote Network |
| `twingate_connector` | Connector (requires `remote_network_id`) |
| `twingate_connector_tokens` | Auth tokens (requires `connector_id`) |
| `twingate_group` | User Group |
| `twingate_resource` | Protected Resource |

**AWS defaults in demo:**
- Region: `eu-west-1`
- VPC CIDR: `10.0.0.0/16`
- Subnet: `10.0.1.0/24`
- Instance type: `t3.micro` for both VMs

## Gotchas
- `terraform.tfvars` contains secrets — add to `.gitignore`
- Connector instance needs `associate_public_ip_address = true`; test VM should not
- `twingate_connector_tokens` outputs are marked sensitive; reference via `access_token`/`refresh_token` attributes
- AMI filters use wildcards — versions may change; verify latest available
- Must manually assign users to the Twingate group post-deploy for access to work
- Demo uses single `main.tf` — not recommended for production (split into modules)

## Related Docs
- [Twingate Terraform Provider Registry](https://registry.terraform.io/providers/Twingate/twingate)
- [AWS Provider Authentication](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- Twingate Connector configuration reference
- Terraform code structure best practices
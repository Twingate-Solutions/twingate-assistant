## Terraform: Twingate on AWS

End-to-end Terraform recipe deploying Twingate alongside an AWS VPC: VPC, subnet, internet gateway, two EC2 instances (Connector + test VM), and full Twingate config (Remote Network, Connector, tokens, Resource, Group).

**Required Providers:**
- `hashicorp/aws` `~> 4.0`
- `twingate/twingate`

**terraform.tfvars (do not commit):**
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` -- AWS credentials (or use other auth methods)
- `tg_api_key` -- Twingate API token with Read/Write/Provision permissions
- `tg_network` -- Twingate tenant subdomain (e.g., `mycorp`)

**Twingate Resource Pattern:**
```
resource "twingate_remote_network" "demo" {
  name = "aws demo remote network"
}
resource "twingate_connector" "demo" {
  remote_network_id = twingate_remote_network.demo.id
}
resource "twingate_connector_tokens" "demo" {
  connector_id = twingate_connector.demo.id
}
resource "twingate_group" "demo" { name = "aws demo group" }
resource "twingate_resource" "demo" {
  name              = "aws demo web server"
  address           = aws_instance.test.private_ip
  remote_network_id = twingate_remote_network.demo.id
  group_ids         = [twingate_group.demo.id]
  protocols {
    allow_icmp = true
    tcp { policy = "RESTRICTED"; ports = ["22"] }
    udp { policy = "ALLOW_ALL" }
  }
}
```

**Connector AMI:**
- Twingate publishes a hardened AMI: filter `name = "twingate/images/hvm-ssd/twingate-amd64-*"`, owner `617935088040`
- Pre-installed Connector service; configure via cloud-init `user_data` writing `/etc/twingate/connector.conf` with `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, then `systemctl enable --now twingate-connector`

**Connector Networking:**
- Connector EC2 needs **outbound internet** only (via internet gateway / NAT)
- Use `associate_public_ip_address = true` if no NAT gateway exists
- Connector does **not** need inbound security group rules

**Resource VM:**
- Test VM has no public IP -- accessible only via Twingate
- `address` in `twingate_resource` uses the **private IP**: `aws_instance.test.private_ip`

**Workflow:**
1. `terraform init` -- install providers
2. `terraform plan` -- non-destructive preview (always run before apply)
3. `terraform apply` -- creates ~13 resources
4. Add a Twingate user to the new Group (Admin Console) to grant access
5. Verify: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private-ip>` works through Twingate Client
6. `terraform destroy` -- tear down

**Gotchas:**
- API token: token type must include **Provision** scope to create Connectors
- terraform.tfvars must be in `.gitignore` (contains secrets)
- `aws_route_table` route order: 0.0.0.0/0 + ::/0 both go to internet gateway
- TCP `policy = "RESTRICTED"` requires explicit `ports`; `policy = "ALLOW_ALL"` ignores ports

**Related Docs:**
- /docs/terraform-getting-started -- Provider overview
- /docs/terraform-azure, /docs/terraform-gcp -- Other clouds
- /docs/aws -- Manual AWS Connector deployment

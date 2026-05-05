## Terraform: Twingate on GCP

End-to-end Terraform recipe deploying Twingate alongside a GCP project: VPC, subnet, firewall rules, two Compute Engine instances (Connector + Nginx test webserver), and full Twingate config.

**Required Providers:**
- `twingate/twingate` (e.g. `0.1.10` -- check Registry for current)
- `hashicorp/google` (no version pin in this guide -- use a constraint in production)

**Provider Configuration:**
```
provider "google" {
  project = "twingate-projects"
  region  = "europe-west2"
  zone    = "europe-west2-c"
}
```

GCP credentials: use `gcloud auth application-default login` or other GCP-supported auth methods (service account JSON, env vars).

**terraform.tfvars (do not commit):**
- `tg_api_key` -- Twingate API token (Read/Write/Provision)
- `tg_network` -- tenant subdomain (e.g. `mycorp`)

**Connector Bootstrap via Template File:**
Unlike the AWS guide (custom AMI), the GCP guide uses an Ubuntu image and runs the Twingate setup script via `metadata_startup_script`:
```
# template/twingate_client.tftpl
#!/bin/bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="${accessToken}" \
  TWINGATE_REFRESH_TOKEN="${refreshToken}" \
  TWINGATE_URL="https://${tgnetwork}.twingate.com" bash
```
Inject via `templatefile()` with values from `twingate_connector_tokens` and `var.tg_network`.

**Twingate Resource Pattern:**
```
resource "twingate_resource" "demo" {
  name              = "gcp demo web server resource"
  address           = google_compute_instance.webserver.network_interface.0.network_ip
  remote_network_id = twingate_remote_network.demo.id
  group_ids         = [twingate_group.demo.id]
  protocols {
    allow_icmp = true
    tcp { policy = "RESTRICTED"; ports = ["80"] }
    udp { policy = "ALLOW_ALL" }
  }
}
```

**Networking Specifics:**
- VPC: `auto_create_subnetworks = false` -- create subnets explicitly
- Firewall: scope `source_ranges` to the subnet CIDR for internal-only traffic
- `access_config {}` (empty block) on Compute Instance NIC = ephemeral public IP -- needed on the Connector VM for outbound to Twingate
- Connector address used in `twingate_resource`: `network_interface.0.network_ip` (private IP)

**Workflow:**
1. `terraform init`, `terraform plan`, `terraform apply` (creates ~10 resources)
2. Manually add a Twingate user to the new Group (Admin Console; usually managed via IdP for production)
3. After ~5 min for VM provisioning, the Connector should appear connected in the Twingate UI
4. Restart Twingate Client -> see new Resource -> open in browser
5. `terraform destroy` to tear down

**Gotchas:**
- Provider version `0.1.10` is very old -- use the latest from the Registry for new work
- Connector VM needs outbound internet (ephemeral or NAT IP) -- a private-only subnet without Cloud NAT will leave the Connector unable to reach Twingate
- Subnet CIDR `172.16.0.0/24` may conflict with on-prem ranges -- pick non-overlapping ranges for production
- Manual user-to-group assignment is intentional in the doc; in production, drive group membership via IdP/SCIM

**Related Docs:**
- /docs/terraform-getting-started -- Provider overview
- /docs/terraform-aws, /docs/terraform-azure -- Other clouds
- /docs/gcp -- Manual GCP Connector deployment

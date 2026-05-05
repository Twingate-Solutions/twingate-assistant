## Getting Started with Terraform and Twingate

Entry point for the Twingate Terraform provider -- a HashiCorp-style IaC integration that provisions Twingate Remote Networks, Connectors, Resources, Groups, and tokens alongside cloud infrastructure.

**Provider:**
- Source: `twingate/twingate` (Terraform Registry)
- Authenticates with a Twingate API token (Read, Write & Provision permissions)
- Use the `network` argument to set the tenant subdomain (e.g., `acme` for `acme.twingate.com`)

**What the Cloud Guides Build:**
Each cloud-specific guide (AWS, Azure, GCP) deploys an end-to-end demo:

**Twingate side:**
- Remote Network (`twingate_remote_network`)
- Connector (`twingate_connector`)
- Connector tokens (`twingate_connector_tokens`) -- sensitive; passed to the Connector VM at boot
- Resource (`twingate_resource`)
- Group (`twingate_group`)

**Cloud side:**
- VPC/VNet + subnet + firewall/NSG rules
- Connector VM/container with Twingate Connector running
- Test VM behind Twingate (private IP only)

**Required Tools:**
- Terraform (CLI installed locally)
- Twingate Client (to verify access after deployment)
- Text editor/IDE (VS Code recommended)

**Provider Versioning:**
- The Twingate provider is actively maintained -- check the Terraform Registry for the latest version
- Use a version constraint (e.g., `version = "~> 1.0"`) in `required_providers` to avoid breaking changes
- Twingate Connector image (when used in cloud-init/user-data) is `twingate/connector:1` or `twingate/connector:latest`

**P2P Considerations:**
- Properly configured Connectors enable peer-to-peer connections -- better user experience and lower bandwidth on the Twingate Relay
- See /docs/peer-to-peer-communication-in-twingate for firewall/NAT requirements

**Related Docs:**
- /docs/terraform-aws -- Full AWS walkthrough
- /docs/terraform-azure -- Full Azure walkthrough
- /docs/terraform-gcp -- Full GCP walkthrough
- /docs/api-overview -- Underlying GraphQL API the provider uses
- /docs/peer-to-peer-communication-in-twingate -- P2P requirements

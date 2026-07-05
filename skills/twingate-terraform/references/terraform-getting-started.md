# Getting Started with Terraform and Twingate

## Summary
Overview page for deploying Twingate infrastructure using Terraform (IaC) across major cloud providers. Links to provider-specific guides for GCP, AWS, and Azure. Covers automated deployment of both Twingate configuration and cloud infrastructure components.

## Key Information
- Terraform provider available for full Twingate environment automation
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys a complete end-to-end setup including connector VMs and test resources
- Peer-to-peer connections are recommended to improve user experience and comply with Fair Use Policy bandwidth limits

## Prerequisites
- VSCode or any text editor installed
- Terraform CLI installed
- Twingate client installed
- Twingate API access (API key required for Terraform provider)

## What Each Guide Deploys

**Twingate Resources:**
- Remote Network (new)
- Connector (attached to Remote Network)
- Access and refresh tokens for the connector
- Resource (pointing to Nginx VM)
- Group (with access to network and resource)

**Cloud Provider Resources (GCP/AWS/Azure):**
- VPC
- Subnet within VPC
- Firewall rules
- VM with Twingate connector installed and configured
- VM with Nginx installed and running

## Related Docs
- [GCP Guide](https://www.twingate.com/docs/) — GCP-specific Terraform deployment
- [AWS Guide](https://www.twingate.com/docs/) — AWS-specific Terraform deployment
- [Azure Guide](https://www.twingate.com/docs/) — Azure-specific Terraform deployment
- Peer-to-peer connections support documentation
- Fair Use Policy (bandwidth)

## Gotchas
- Page is an index/overview only — actual step-by-step instructions are in the provider-specific sub-guides
- Connector tokens (access + refresh) are managed as Terraform resources, meaning they will be stored in Terraform state — use secure state backends (e.g., Terraform Cloud, encrypted S3)
# Getting Started with Terraform and Twingate

## Summary
Overview page for using Terraform (IaC) to automate Twingate environment deployment across major cloud providers. Links to provider-specific guides for GCP, AWS, and Azure. Covers full stack deployment including networking, VMs, and Twingate configuration.

## Key Information
- Terraform provider available for automating Twingate environments
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys a complete, consistent reference architecture
- Peer-to-peer connections are covered to support Fair Use Policy compliance

## Prerequisites
- VS Code or any text editor
- Terraform CLI installed
- Twingate client installed
- Twingate account with API access

## What Gets Deployed (per guide)

**Twingate Resources:**
- Remote Network (new)
- Connector (attached to Remote Network)
- Connector access + refresh tokens
- Resource (pointing to Nginx VM)
- Group (with access to network and resource)

**Cloud Provider Resources:**
- VPC
- Subnet within VPC
- Firewall rules
- VM with Twingate connector installed and configured
- VM with Nginx installed and running

## Step-by-Step
This page is an index — follow provider-specific guides:
1. [GCP Guide](https://www.twingate.com/docs/terraform-gcp)
2. [AWS Guide](https://www.twingate.com/docs/terraform-aws)
3. [Azure Guide](https://www.twingate.com/docs/terraform-azure)

## Configuration Values
- Twingate API used for provider authentication (API key required)
- Connector tokens: access token + refresh token generated via Terraform

## Gotchas
- Peer-to-peer connections should be configured to avoid Fair Use Policy bandwidth violations
- Connector tokens are generated as part of the Terraform plan — handle state file securely (contains secrets)

## Related Docs
- [Twingate Terraform Provider](https://registry.terraform.io/providers/Twingate/twingate/latest)
- GCP Terraform Guide
- AWS Terraform Guide
- Azure Terraform Guide
- Peer-to-peer connections support doc
- Fair Use Policy
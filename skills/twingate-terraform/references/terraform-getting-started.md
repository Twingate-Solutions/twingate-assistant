# Getting Started with Terraform and Twingate

## Summary
Overview page for using Terraform (HashiCorp IaC) to automate Twingate environment deployment across major cloud providers. Links to provider-specific guides for GCP, AWS, and Azure deployments. Covers full stack deployment including Twingate configuration and cloud networking infrastructure.

## Key Information
- Terraform provider available for Twingate to manage resources declaratively
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys both Twingate objects and cloud infrastructure components

## Prerequisites
- VS Code or any text editor installed
- Terraform CLI installed
- Twingate client installed
- Twingate account with API access

## What Gets Deployed (All Guides)

**Twingate Resources:**
- New Remote Network
- New Connector (attached to Remote Network)
- Access and refresh tokens for the Connector
- New Resource (pointing to Nginx VM)
- New Group with access to network and resource

**Cloud Provider Resources (GCP/AWS/Azure):**
- New VPC
- New subnet within the VPC
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Related Docs
- [GCP Deployment Guide](https://www.twingate.com/docs/gcp)
- [AWS Deployment Guide](https://www.twingate.com/docs/aws)
- [Azure Deployment Guide](https://www.twingate.com/docs/azure)
- Peer-to-peer connections support
- Twingate Fair Use Policy

## Gotchas
- Peer-to-peer connections are recommended to avoid Fair Use Policy bandwidth limits — the guides include P2P configuration
- Connector tokens (access + refresh) are created via Terraform, meaning they will be stored in Terraform state — treat state files as sensitive
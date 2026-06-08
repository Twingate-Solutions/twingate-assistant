# Getting Started with Terraform and Twingate

## Summary
Introductory page for using Terraform (IaC) to automate Twingate environment deployments across major cloud providers. Links to cloud-specific guides for GCP, AWS, and Azure. Covers deploying a complete Twingate + cloud networking stack via declarative code.

## Key Information
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys a full Twingate + cloud infrastructure stack
- Uses Twingate's official Terraform Provider with the Twingate API

## Prerequisites
- VS Code or any text editor installed
- Terraform CLI installed
- Twingate client installed
- Twingate account with API access

## What Each Guide Deploys

**Twingate Resources:**
- New Remote Network
- New Connector (attached to Remote Network)
- Access and refresh tokens for the Connector
- New Resource (pointing to Nginx VM)
- New Group with access to network and resource

**Cloud Provider Resources (GCP/AWS/Azure):**
- New VPC
- New subnet in the VPC
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Configuration Values
- Twingate API credentials required (access/refresh tokens generated via Terraform)
- Cloud provider credentials required (GCP, AWS, or Azure service account/credentials)

## Gotchas
- Peer-to-peer connections are recommended to improve user experience and stay within the Fair Use Policy for bandwidth consumption — enable this when deploying Connectors

## Related Docs
- [GCP Terraform Guide](https://www.twingate.com/docs/terraform-gcp)
- [AWS Terraform Guide](https://www.twingate.com/docs/terraform-aws)
- [Azure Terraform Guide](https://www.twingate.com/docs/terraform-azure)
- Twingate Terraform Provider (HashiCorp Registry)
- Peer-to-peer connections support guide
- Twingate Fair Use Policy
# Getting Started with Terraform and Twingate

## Summary
Overview page for deploying Twingate infrastructure using Terraform (IaC) across GCP, AWS, and Azure. Guides cover full stack deployment including Twingate components and cloud provider networking. Serves as an index/prerequisites page pointing to provider-specific guides.

## Key Information
- Twingate provides a Terraform Provider for automating Twingate environments
- Three cloud providers supported: GCP, AWS, Azure (separate guides for each)
- Each guide deploys both Twingate components and cloud infrastructure together

## Prerequisites
- VS Code or any text editor installed
- Terraform CLI installed
- Twingate Client installed
- Twingate account with API access

## What Each Guide Deploys

**Twingate Components:**
- New Remote Network
- New Connector (attached to Remote Network)
- Access and refresh tokens for the connector
- New Resource (pointing to Nginx VM)
- New Group with access to network and resource

**Cloud Provider Components (GCP/AWS/Azure):**
- New VPC
- New subnet
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Step-by-Step
1. Install prerequisites (VS Code, Terraform, Twingate Client)
2. Select cloud provider guide (GCP, AWS, or Azure)
3. Follow provider-specific deployment steps

## Gotchas
- Peer-to-peer connections are recommended to improve user experience and stay within Fair Use Policy for bandwidth consumption — configure these when deploying connectors
- This page is an index only; actual configuration values and Terraform code are in the provider-specific linked guides

## Related Docs
- [GCP Guide](https://www.twingate.com/docs/gcp)
- [AWS Guide](https://www.twingate.com/docs/aws)
- [Azure Guide](https://www.twingate.com/docs/azure)
- [Peer-to-peer connections support](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
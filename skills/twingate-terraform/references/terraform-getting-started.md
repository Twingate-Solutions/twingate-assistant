# Getting Started with Terraform and Twingate

## Summary
Overview page for deploying Twingate infrastructure using Terraform (IaC) across major cloud providers. Guides cover full-stack deployment including Twingate configuration and cloud provider networking. Links out to provider-specific guides for GCP, AWS, and Azure.

## Key Information
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys both Twingate objects and cloud infrastructure via Terraform
- Uses Twingate Terraform Provider alongside the Twingate API

## Prerequisites
- VS Code (or any text editor)
- Terraform installed locally
- Twingate client installed
- Twingate API access (for Terraform Provider)

## What Each Guide Deploys

**Twingate Objects:**
- New Remote Network
- New Connector (attached to Remote Network)
- Connector access and refresh tokens
- New Resource (pointing to Nginx VM)
- New Group (with access to network and resource)

**Cloud Provider Infrastructure (GCP/AWS/Azure):**
- New VPC
- New subnet
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Gotchas
- Peer-to-peer connections are recommended to avoid hitting the Fair Use Policy for bandwidth consumption — guides cover enabling this
- No Terraform code is shown on this page; it's an index/intro page only

## Related Docs
- [GCP Guide](https://www.twingate.com/docs/gcp)
- [AWS Guide](https://www.twingate.com/docs/aws)
- [Azure Guide](https://www.twingate.com/docs/azure)
- Peer-to-peer connections support doc
- Twingate Fair Use Policy
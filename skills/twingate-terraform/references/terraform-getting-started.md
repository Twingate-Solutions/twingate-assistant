# Getting Started with Terraform and Twingate

## Summary
Overview page for using Terraform (IaC) to automate Twingate environment deployments across major cloud providers. Links to cloud-specific guides for GCP, AWS, and Azure. Covers full stack deployment including Twingate configuration and cloud networking infrastructure.

## Key Information
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys both Twingate components and cloud infrastructure
- Uses Twingate Terraform Provider alongside cloud provider Terraform providers

## Prerequisites
- VS Code or any text editor
- Terraform installed
- Twingate client installed
- Twingate API access (for Terraform Provider)

## What Gets Deployed

**Twingate Components:**
- New Remote Network
- New Connector (attached to Remote Network)
- Connector access and refresh tokens
- New Resource (for Nginx VM)
- New Group (for network/resource access)

**Cloud Infrastructure (GCP/AWS/Azure):**
- New VPC
- New subnet within VPC
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Related Docs
- GCP deployment guide
- AWS deployment guide
- Azure deployment guide
- Twingate peer-to-peer connections support
- Twingate Fair Use Policy

## Gotchas
- Peer-to-peer connections are recommended for better user experience and to stay within Fair Use Policy bandwidth limits — configure this in addition to basic connector setup
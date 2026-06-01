# Getting Started with Terraform and Twingate

## Summary
Twingate provides Terraform (IaC) integration to automate deployment of full Twingate environments across major cloud providers. Guides cover end-to-end infrastructure setup including Twingate configuration and cloud provider resources. Three cloud provider guides are available: GCP, AWS, and Azure.

## Key Information
- Uses Twingate's official Terraform Provider
- Deploys both Twingate objects and cloud infrastructure in a single workflow
- Peer-to-peer connections are recommended for better UX and Fair Use Policy compliance

## Prerequisites
- [ ] VS Code or text editor installed
- [ ] Terraform CLI installed
- [ ] Twingate client installed
- [ ] Twingate account with API access

## What Gets Deployed

**Twingate Objects:**
- Remote Network (new)
- Connector (attached to Remote Network)
- Connector access + refresh tokens
- Resource (pointing to Nginx VM)
- Group (with access to network and resource)

**Cloud Provider Infrastructure (GCP/AWS/Azure):**
- VPC
- Subnet within VPC
- Firewall rules
- VM with Twingate connector installed and configured
- VM with Nginx installed and running

## Cloud Provider Guides
- [GCP](https://www.twingate.com/docs/gcp)
- [AWS](https://www.twingate.com/docs/aws)
- [Azure](https://www.twingate.com/docs/azure)

## Configuration Values
- Twingate API key required for Terraform provider authentication
- Connector tokens (access + refresh) generated via Terraform and injected into connector VM

## Gotchas
- Peer-to-peer connections must be explicitly supported; review Fair Use Policy for bandwidth limits
- Connector tokens are sensitive outputs — handle Terraform state securely (use remote state with encryption)

## Related Docs
- Twingate Terraform Provider (HashiCorp Registry)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- GCP, AWS, Azure deployment guides (linked above)
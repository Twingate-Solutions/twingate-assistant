# Getting Started with Terraform and Twingate

## Summary
Overview page for deploying Twingate infrastructure using Terraform (IaC) across major cloud providers. Guides cover automated deployment of Twingate Remote Networks, Connectors, Resources, and Groups alongside cloud networking infrastructure.

## Key Information
- Terraform provider available for automating complete Twingate environments
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys both Twingate objects and cloud infrastructure components

## Prerequisites
- [ ] VS Code or text editor installed
- [ ] Terraform CLI installed
- [ ] Twingate Client installed
- [ ] Twingate account with API access

## What Each Guide Deploys

**Twingate Objects:**
- Remote Network (new)
- Connector (attached to Remote Network)
- Connector access + refresh tokens
- Resource (pointing to Nginx VM)
- Group (with access to network and resource)

**Cloud Infrastructure (per provider):**
- New VPC
- Subnet within VPC
- Firewall rules
- VM with Twingate Connector installed and configured
- VM with Nginx installed and running

## Cloud Provider Guides
- [GCP](https://www.twingate.com/docs/gcp)
- [AWS](https://www.twingate.com/docs/aws)
- [Azure](https://www.twingate.com/docs/azure)

## Gotchas
- Peer-to-peer connections should be supported to improve user experience and stay within the Fair Use Policy for bandwidth consumption

## Related Docs
- Twingate Terraform Provider documentation
- Peer-to-peer connections support guide
- Fair Use Policy
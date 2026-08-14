---
source: https://www.twingate.com/docs/terraform-getting-started
type: docs
fetched: 2026-08-14
source_version: 2dbd37160319fa310e02a8e9aea4bb27dfd1c81c40eeb7551db81d0ae7329e2a
---

# Getting Started with Terraform and Twingate

## Summary
Overview page for deploying Twingate infrastructure using Terraform (IaC) across the three major cloud providers (GCP, AWS, Azure). Guides cover automated deployment of Twingate Remote Networks, Connectors, Resources, and Groups alongside cloud networking infrastructure.

## Key Information
- Twingate provides a Terraform Provider for full environment automation
- Three cloud provider guides available: GCP, AWS, Azure
- Each guide deploys identical Twingate components with cloud-specific infrastructure

## Prerequisites
- VS Code (or any text editor)
- Terraform installed locally
- Twingate Client installed
- Twingate account with API access

## What Each Guide Deploys

**Twingate Components:**
- Remote Network (new)
- Connector (attached to Remote Network)
- Connector access + refresh tokens
- Resource (pointing to Nginx VM)
- Group (with access to network and resource)

**Cloud Provider Components:**
- VPC
- Subnet within VPC
- Firewall rules
- VM with Twingate Connector installed/configured
- VM with Nginx installed and running

## Related Docs
- GCP deployment guide
- AWS deployment guide
- Azure deployment guide
- Peer-to-peer connections support
- Twingate Fair Use Policy

## Gotchas
- Peer-to-peer connections are recommended to improve user experience and stay within Fair Use Policy bandwidth limits — configure these alongside standard deployment
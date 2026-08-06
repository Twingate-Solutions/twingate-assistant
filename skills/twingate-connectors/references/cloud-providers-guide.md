---
source: https://www.twingate.com/docs/cloud-providers-guide
type: docs
fetched: 2026-08-05
source_version: 957efad7465a09a35a5648526420f760f94b5347ddf8d12b0d132de83b6698e0
---

# Cloud Providers Guide

## Page Title
Twingate Cloud Providers Guide

## Summary
Covers deploying and configuring Twingate Connectors across AWS, GCP, Azure, and DigitalOcean. The setup pattern is identical across all providers: create a Remote Network, deploy a Connector, then define Resources using private IPs or internal DNS names. No inbound firewall rules are required on the Connector host.

## Key Information
- **Universal setup pattern**: Remote Network → Connector → Resources
- Connectors make **outbound-only connections** — no inbound ports needed
- Resources are defined by private IP (e.g., `10.0.1.15`) or internal DNS (e.g., `app.internal.example.com`)
- **Production requirement**: Deploy ≥2 Connectors per Remote Network for high availability

## Prerequisites
- Twingate Admin Console access
- Cloud VM/instance to host the Connector (EC2, Compute Engine, Azure VM, or Droplet)
- Twingate Client installed on end-user devices

## Provider-Specific Guides
| Provider | Topics Covered |
|---|---|
| **AWS** | EC2 deployment, VPN migration, Workspaces, reference architecture, RDS/Aurora access |
| **GCP** | Compute Engine VM, Cloud SQL + Auth Proxy |
| **Azure** | Azure VM, VNet resource access, Azure SQL/SQL Managed Instance |
| **DigitalOcean** | Droplet deployment, VPC access |

## Configuration Values
| Requirement | Value |
|---|---|
| Outbound HTTPS | Port `443` |
| Outbound Relay | TCP `30000–31000` |
| Inbound rules | None required |

## Troubleshooting

**Connector won't connect:**
- Verify outbound access on port `443` and TCP `30000-31000`
- Confirm Connector tokens are valid and not expired

**Resources unreachable:**
- Security group/firewall must allow outbound traffic from Connector to Resource's private IP and port
- Connector needs network-level path to the Resource (same as any host in the VPC)

**DNS resolution failures:**
- Connector VM must be able to resolve internal DNS names
- Check VPC DNS settings and hosted zone VPC association

**Slow connections:**
- Check Connector health in Admin Console
- Deploy Connector closer to the Resource region
- Enable peer-to-peer connections

## Gotchas
- DNS: If using internal DNS names for Resources, the Connector's VM must have DNS resolution configured for those names — this is a common misconfiguration
- Security groups must allow Connector → Resource traffic (not just internet → Connector)
- Expired or incorrect Connector tokens are a frequent cause of connection failures

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Remote Network Best Practices](https://www.twingate.com/docs/remote-network-best-practices)
- [Database Access Guide](https://www.twingate.com/docs/database-access)
- [Terraform Getting Started](https://www.twingate.com/docs/terraform)
- [Pulumi Getting Started](https://www.twingate.com/docs/pulumi)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
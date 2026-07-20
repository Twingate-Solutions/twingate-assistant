# Cloud Providers Guide

## Page Title
Twingate Cloud Providers Guide

## Summary
Covers deploying and configuring Twingate Connectors across AWS, GCP, Azure, and DigitalOcean. The setup pattern is identical across all providers: create a Remote Network, deploy a Connector, then define Resources using private IPs or internal DNS names.

## Key Information
- Connectors make **outbound-only connections** — no inbound firewall rules or public ports required
- Deploy **minimum 2 Connectors per Remote Network** for production high availability
- Resources are defined by private IP addresses or internal DNS names

## Prerequisites
- Twingate Admin Console access
- Cloud VM/instance with outbound internet access
- Twingate Client installed on end-user devices

## Setup Pattern (All Providers)
1. Create a **Remote Network** in Admin Console (represents VPC/VNet/project)
2. Deploy a **Connector** into that network
3. Create **Resources** with private IPs or internal DNS names
4. Assign user permissions to Resources

## Provider-Specific Guides

| Provider | Topics Covered |
|----------|---------------|
| **AWS** | EC2 deployment, VPN migration, Workspaces, reference architecture, RDS/Aurora access |
| **GCP** | Compute Engine VM, Cloud SQL + Auth Proxy |
| **Azure** | Azure VM deployment, private VNet resources, Azure SQL/Managed Instance |
| **DigitalOcean** | Droplet deployment, VPC access |

## Configuration Values / Network Requirements

| Protocol | Port | Direction | Purpose |
|----------|------|-----------|---------|
| HTTPS | 443 | Outbound | Connector control plane |
| TCP | 30000–31000 | Outbound | Relay infrastructure |

No inbound ports required.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Connector won't connect | Verify outbound 443 + TCP 30000–31000; check Connector tokens not expired |
| Resources unreachable | Security group must allow outbound from Connector to Resource's private IP/port |
| DNS resolution failures | Confirm Connector VM can resolve internal DNS; check VPC DNS settings and hosted zone associations |
| Slow connections | Check Connector health in Admin Console; deploy Connector closer to Resource or enable peer-to-peer |

## Gotchas
- Connector must have a **network path to the Resource** (treated like any host in the VPC)
- Internal DNS names require the Connector's VM DNS to resolve them — check VPC DNS and hosted zone config
- Connector tokens must be valid and not expired

## Related Docs
- Connector Best Practices
- Remote Network Best Practices
- Best Practices for Connector Placement
- Database Access Guide
- Terraform Getting Started
- Pulumi Getting Started
- Twingate Troubleshooting Guide
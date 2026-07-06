# Cloud Providers Guide

## Page Title
Twingate Cloud Providers Guide

## Summary
Covers deploying and configuring Twingate Connectors across AWS, GCP, Azure, and DigitalOcean. The setup pattern is identical across all providers: create a Remote Network, deploy a Connector, then define Resources. Connectors use outbound-only connections, eliminating inbound firewall requirements.

## Key Information
- Supported providers: AWS, Google Cloud (GCP), Azure, DigitalOcean
- Universal pattern: Remote Network → Connector → Resources
- Connectors require **no inbound firewall rules** — outbound only
- High availability: deploy **minimum 2 Connectors** per Remote Network in production
- Resources addressed by private IP (e.g., `10.0.1.15`) or internal DNS (e.g., `app.internal.example.com`)

## Prerequisites
- Twingate Admin Console access
- VM/instance in target cloud VPC/VNet
- Outbound internet access from Connector VM
- Valid Connector tokens (generated in Admin Console)

## Step-by-Step (Universal Pattern)
1. Create a **Remote Network** in Admin Console representing your VPC/VNet/project
2. Deploy a **Connector** into that network (cloud-specific guides below)
3. Create **Resources** using private IPs or internal DNS names
4. Assign user permissions to Resources

## Provider-Specific Guides
| Provider | Topics Covered |
|----------|---------------|
| AWS EC2 | Instance sizing, security groups, IAM |
| AWS | Replace Client VPN / Site-to-Site VPN migration |
| AWS | WorkSpaces client install, RDS/Aurora database access |
| GCP Compute Engine | Machine type, VPC firewall, service accounts, Cloud SQL |
| Azure VM | VM sizing, NSG rules, resource groups, SQL Database/Managed Instance |
| DigitalOcean | Droplet deployment, VPC private resource access |

## Configuration Values
| Requirement | Value |
|-------------|-------|
| Outbound port (HTTPS) | `443` |
| Outbound port (Relay) | `30000–31000` TCP |
| Inbound ports required | None |

## Troubleshooting

| Issue | Check |
|-------|-------|
| Connector won't connect | Outbound access on 443 + 30000-31000; valid/unexpired tokens |
| Resources unreachable | Security group allows outbound from Connector to Resource IP/port |
| DNS resolution failures | Connector VM can resolve internal DNS; VPC DNS settings; hosted zone association |
| Slow connections | Connector health in Admin Console; deploy Connector closer to Resource; enable peer-to-peer |

## Gotchas
- Connector must have **network path to Resource** — treat it like any other host in the VPC needing access
- DNS failures often caused by hosted zone not associated with correct VPC
- Tokens must not be expired; regenerate in Admin Console if needed
- Single Connector = single point of failure; always use 2+ for production

## Related Docs
- Connector Best Practices
- Remote Network Best Practices
- Best Practices for Connector Placement
- Database Access Guide
- Terraform Getting Started
- Pulumi Getting Started
- Twingate Troubleshooting Guide
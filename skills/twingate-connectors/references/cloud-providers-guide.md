---
source: https://www.twingate.com/docs/cloud-providers-guide
type: docs
fetched: 2026-08-14
source_version: 8c73b5f80a17fa3a3ff64e9285e8947fa590d14ff1020414bca828b4a689ef25
---

# Cloud Providers Guide

## Page Title
Twingate Cloud Providers Guide

## Summary
Covers deploying and configuring Twingate Connectors across AWS, GCP, Azure, and DigitalOcean. Setup pattern is identical across providers: create a Remote Network, deploy a Connector, then define Resources using private IPs or internal DNS names.

## Key Information
- Connectors make **outbound-only connections** — no inbound firewall rules or public port exposure required
- Deploy **minimum 2 Connectors per Remote Network** for production high availability
- Users need Twingate Client installed + permissions to access Resources

## Prerequisites
- Twingate Admin Console access
- Cloud provider VM/compute access
- Outbound internet access from Connector VM

## Provider-Specific Deployment Notes

### AWS
- Deploy Connector on EC2 instance (see EC2 deployment guide for sizing, security groups, IAM)
- Migration path available from AWS Client VPN / Site-to-Site VPN
- Supports AWS Workspaces client installation
- Reference architecture covers multi-AZ Connector placement

### Google Cloud (GCP)
- Deploy Connector on Compute Engine VM
- Requires VPC firewall rules and service account setup
- Cloud SQL access requires authorized network config + Cloud SQL Auth Proxy consideration

### Azure
- Deploy Connector as Azure Virtual Machine
- Configure Network Security Group (NSG) rules
- Supports Azure SQL Database and SQL Managed Instance

### DigitalOcean
- Deploy Connector on a Droplet within DigitalOcean VPC

## Configuration Values

| Purpose | Value |
|---|---|
| Required outbound port (HTTPS) | `443` |
| Required outbound port (Relay) | TCP `30000–31000` |
| Inbound rules required | None |

## Troubleshooting

| Issue | Fix |
|---|---|
| Connector won't connect | Verify outbound `443` and TCP `30000-31000`; check Connector tokens valid |
| Resources unreachable | Confirm Connector security group allows outbound to Resource's private IP/port |
| DNS resolution failures | Verify Connector VM can resolve internal DNS; check VPC DNS settings and hosted zone association |
| Slow connections | Check Connector health in Admin Console; deploy Connector closer to Resource; enable peer-to-peer |

## Gotchas
- Connector VM must have a **network path to the Resource** (treat it like any other VPC host)
- Connector tokens can expire — verify they are current when troubleshooting connectivity
- Internal DNS names require the Connector's VM to use the VPC's DNS resolver with correct hosted zone association

## Related Docs
- Connector Best Practices
- Remote Network Best Practices
- Best Practices for Connector Placement
- Database Access Guide
- Terraform Getting Started
- Pulumi Getting Started
- Twingate Troubleshooting Guide
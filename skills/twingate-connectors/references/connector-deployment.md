# Connector Deployment

## Page Title
Deploying Connectors - Method Selection Guide

## Summary
Twingate Connectors deploy via Linux systemd packages or OCI (Docker) containers. A single Connector provides access to all reachable resources in its network segment; multiple Connectors enable load-balancing and failover. Deployment method selection depends on environment type (cloud, on-prem, serverless, home).

## Key Information
- Connectors do **not** need to be on every host — one Connector covers all reachable resources in its network
- Multiple Connectors on separate hosts = automatic load-balancing + failover
- No inbound firewall rules required — only outbound internet access needed
- Each location/cloud requires its own Remote Network in Twingate
- Peer-to-peer connections improve UX and reduce bandwidth (Fair Use Policy compliance)

## Supported Platforms

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|-------------|---------|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| On-prem/Office | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology, Linux, Home Assistant, Proxmox, Unraid, CasaOS, Mac VM |

## Gotchas
- Serverless/PaaS deployments offer less control over CPU, memory, and network resources allocated to Connectors
- Home networks with dynamic IPs, CGNATs (e.g., Starlink) cannot accept inbound connections — Twingate's outbound-only model solves this
- Cloud VMs recommended over serverless when compute resources already exist in cloud — better sizing control

## Prerequisites
- Outbound internet access from deployment host
- Linux-based host (systemd or Docker/OCI runtime)
- Remote Network configured in Twingate Admin Console for each location

## Recommendations
- **Cloud:** VM deployment preferred over serverless for performance consistency and resource control
- **On-prem:** Deploy second Connector on separate physical machine for redundancy
- **Multi-location:** Create separate Remote Network per location; enable peer-to-peer connections

## Related Docs
- Peer-to-peer connections support
- Fair Use Policy
- Individual deployment guides: AWS EC2, GCP, Azure, Kubernetes, Docker Compose, Terraform, Pulumi, Raspberry Pi, Home Assistant
- Best Practices for Secure Infrastructure-as-Code (webinar)
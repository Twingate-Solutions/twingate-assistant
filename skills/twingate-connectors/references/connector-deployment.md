# Connector Deployment Guide

## Page Title
Deploying Connectors

## Summary
Twingate Connectors are deployed via Linux systemd packages or OCI (Docker) containers. A single connector provides access to all reachable resources in its network; multiple connectors enable load-balancing and failover. Supports deployment across cloud VMs, on-premises, serverless, IaC, and home networks.

## Key Information
- Connectors do **not** need to be on every host — one connector serves all reachable resources in its network
- Multiple connectors on separate hosts = automatic load-balancing + failover
- No inbound firewall rules required — only outbound internet access needed
- Multiple locations require separate Remote Networks per location
- Peer-to-peer connections improve UX and help stay within Fair Use Policy bandwidth limits

## Supported Linux Distributions

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Options by Environment

| Environment | Methods |
|-------------|---------|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| On-Premises/Office | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology NAS, Linux, Home Assistant, Unraid, CasaOS, Mac VM |

## Recommendations by Use Case

- **Best performance:** Cloud VMs (consistent resources, sizing control, static IP support)
- **On-premises redundancy:** Deploy second connector on separate physical machine
- **Home/dynamic IP/CGNAT (Starlink):** Home network deployment avoids need for inbound rules or static IP
- **Multi-environment rollout:** IaC (Terraform/Pulumi) for consistency and change control

## Gotchas
- Serverless/PaaS deployments offer less control over CPU, memory, and network resources allocated to connectors
- CGNAT environments (e.g., Starlink) have no inbound IP — connector deployment is the only viable remote access method
- Sizing connectors on cloud VMs should account for expected end-user usage patterns

## Related Docs
- Peer-to-peer connections support
- Fair Use Policy (bandwidth)
- Remote Networks configuration
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Platform-specific guides: AWS EC2, GCP Compute, Azure Compute, Kubernetes, Docker Compose, Terraform, Pulumi, Raspberry Pi, Home Assistant, Synology
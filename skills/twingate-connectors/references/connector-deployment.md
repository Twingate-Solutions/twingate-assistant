# Connector Deployment Guide

## Page Title
Deploying Connectors

## Summary
Twingate Connectors are deployed via Linux systemd packages or OCI (Docker) containers. A single Connector provides access to all reachable resources in its network; additional Connectors add load-balancing and failover. This guide helps select the appropriate deployment method based on target environment.

## Key Information
- Connectors do **not** need to be on every host — one Connector covers all reachable resources in its network
- Multiple Connectors on separate hosts = automatic load-balancing + failover
- No inbound firewall rules required — only outbound internet access needed
- Multiple locations require separate Remote Networks per location
- Peer-to-peer connections improve user experience and help stay within Fair Use Policy bandwidth limits

## Supported Platforms

**Linux (x86/AMD64 and ARM64):**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**Linux (x86/AMD64 only):**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|---|---|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| Office/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology NAS, Linux, Home Assistant, Proxmox, Unraid, CasaOS, Mac (VM) |

## Recommendations by Use Case
- **Best performance**: Cloud VMs — allows sizing based on expected usage
- **Fixed Static IP for users**: Cloud VM deployment
- **On-premises (offices/data centers)**: Deploy second Connector on separate physical machine for redundancy
- **No server management**: Serverless/PaaS options
- **Repeatable multi-environment rollout**: IaC (Terraform/Pulumi)
- **Home with dynamic IP or CGNAT (e.g., Starlink)**: Home network deployment avoids need for inbound rules

## Gotchas
- Serverless/PaaS deployments offer less control over CPU, memory, and network resources allocated to Connector instances
- Home networks with CGNAT have no inbound IP available — Twingate's outbound-only model is specifically designed for this case
- Peer-to-peer must be explicitly configured; not automatic

## Prerequisites
- Outbound internet access from the host running the Connector
- Linux environment (systemd or Docker/OCI container support)
- Remote Network configured in Twingate admin console for each location

## Related Docs
- Supporting peer-to-peer connections
- Fair Use Policy
- Specific platform guides (AWS EC2, GCP, Azure, Kubernetes, Terraform, Pulumi, Raspberry Pi, Home Assistant, etc.)
- Best Practices for Secure Infrastructure-as-Code Initiatives (webinar)
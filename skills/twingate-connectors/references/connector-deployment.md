---
source: https://www.twingate.com/docs/connector-deployment
type: docs
fetched: 2026-08-05
source_version: ad8bb9eef29a9dc617ddbfdf5034f9f3194b81ccf5811468c2dd69a168c04e8c
---

# Connector Deployment

## Summary
Twingate Connectors run as either a Linux systemd package or OCI (Docker) container. A single Connector provides access to all reachable resources in its network; additional Connectors enable load-balancing and failover. No inbound firewall rules are required—only outbound internet access.

## Key Information
- Connectors do **not** need to be on every host; one Connector can serve an entire network segment
- Multiple Connectors on separate hosts = automatic load-balancing + failover
- Use separate Remote Networks per location for multi-site deployments
- Peer-to-peer connections improve user experience and reduce bandwidth under Fair Use Policy
- Cloud VMs are the recommended deployment method when available

## Supported Platforms

### Linux (x86/AMD64 and ARM64)
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

### Linux (x86/AMD64 only)
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|---|---|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute |
| Kubernetes | K8s |
| Office/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology NAS, Linux, Home Assistant, Proxmox, Unraid, CasaOS, Mac VM |

## Gotchas
- Serverless/PaaS deployments offer less control over CPU, memory, and network resources allocated to Connectors
- Home networks with dynamic IPs or CGNATs (e.g., Starlink) cannot accept inbound connections—Connector deployment resolves this without opening firewall ports
- For office/data center deployments, a **second Connector on a separate physical machine** is explicitly recommended for redundancy

## Prerequisites
- Outbound internet access from the host running the Connector
- No inbound firewall rules needed
- Target environment must support Linux systemd or Docker/OCI containers

## Related Docs
- Peer-to-peer connections support guide
- Fair Use Policy (bandwidth)
- AWS EC2, GCP Compute, Azure Compute deployment guides
- Terraform, Pulumi integration guides
- Specific home network guides (Plex, Home Assistant, Windows File Shares)
- Best Practices for Secure Infrastructure-as-Code webinar
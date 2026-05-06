# Connector Deployment

## Summary
Twingate Connectors run as either a Linux systemd package or OCI (Docker) container. A single Connector can provide access to all reachable resources in its network segment; multiple Connectors enable load-balancing and failover. No inbound firewall rules are required—only outbound internet access.

## Key Information
- Connectors do **not** need to be on every host—one Connector covers all reachable resources in its network
- Multiple Connectors on separate hosts = automatic load-balancing + failover
- Each distinct location/cloud requires its own **Remote Network** in Twingate
- Peer-to-peer connections reduce bandwidth and improve UX; required for Fair Use Policy compliance
- Two deployment formats: **Linux systemd package** or **OCI/Docker container**

## Supported Platforms

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|---|---|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| Office/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Mac VM, Synology NAS, Raspberry Pi, Linux, Home Assistant, Proxmox, Unraid |

## Prerequisites
- Outbound internet access from Connector host
- No inbound firewall rules needed

## Gotchas
- **Cloud VMs are the recommended default**—most consistent performance and resource sizing control
- **Serverless/PaaS** environments offer easier deployment but less control over CPU/memory/network allocation
- Home networks with **dynamic IPs or CGNAT** (e.g., Starlink) cannot receive inbound connections—Connector deployment is the only viable option
- For redundancy in offices/data centers, deploy second Connector on a **separate physical machine**
- Multi-location setups require a separate Remote Network per location (not just per Connector)

## Related Docs
- Peer-to-peer connections support
- Fair Use Policy
- Remote Networks configuration
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Individual deployment guides: AWS EC2, GCP Compute, Azure Compute, Kubernetes, Docker Compose, Terraform, Pulumi, Raspberry Pi, Home Assistant
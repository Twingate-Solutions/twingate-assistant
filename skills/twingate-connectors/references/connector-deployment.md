# Connector Deployment

## Page Title
Deploying Connectors

## Summary
Twingate Connectors are deployed via Linux systemd packages or OCI (Docker) containers. A single Connector can serve an entire network segment; multiple Connectors enable load-balancing and failover. Deployment method depends on target environment (cloud VM, on-prem, serverless, IaC, or home network).

## Key Information
- Connectors do **not** need to be on every host — one Connector covers all reachable resources in its network
- Multiple Connectors on separate hosts = automatic load-balancing + failover
- No inbound firewall rules required — only outbound internet access needed
- Use separate Remote Networks per location for multi-site deployments
- Peer-to-peer connections recommended for better UX and Fair Use Policy compliance

## Supported Platforms

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|---|---|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| On-Prem/Office | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Mac VM, Synology NAS, Raspberry Pi, Linux, Home Assistant, Proxmox, Unraid, CasaOS |

## Prerequisites
- Outbound internet access from the Connector host
- Linux-based host (systemd or Docker/OCI runtime)

## Gotchas
- **Cloud VMs are recommended** over serverless when available — better resource control and sizing
- Serverless/PaaS deployments offer less control over CPU/memory/network allocated to Connectors
- Home networks with dynamic IPs, CGNATs (e.g., Starlink), or no inbound access require Connector deployment (cannot rely on port forwarding)
- Deploy second Connector on a **separate physical machine** for on-prem redundancy — same host defeats the purpose

## Related Docs
- Peer-to-peer connection support
- Fair Use Policy
- Remote Networks configuration
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Platform-specific guides: Terraform, Pulumi, AWS EC2, Kubernetes, Docker Compose, Raspberry Pi, Home Assistant
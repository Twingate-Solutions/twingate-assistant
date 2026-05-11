# Connector Deployment

## Summary
Twingate Connectors run as either Linux systemd packages or OCI (Docker) containers. A single Connector provides access to all reachable resources in its network; multiple Connectors enable load-balancing and failover. No inbound firewall rules are required—only outbound internet access.

## Key Information
- Single Connector covers all reachable resources in its deployed network
- Multiple Connectors (separate hosts) = automatic load-balancing + failover
- Deployment types: Linux systemd package or OCI/Docker container
- Each distinct location/cloud should have its own Remote Network configured
- Peer-to-peer connections improve UX and reduce bandwidth under Fair Use Policy

## Supported Platforms

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Method Selection

| Environment | Recommended Methods |
|---|---|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute |
| Kubernetes | K8s deployment |
| Office/Data Center | Docker Compose, Proxmox, Synology, QNAP, Firewalla, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| Infrastructure-as-Code | Terraform, Pulumi |
| Home Network | Raspberry Pi, Linux, Synology DSM 7.x, Home Assistant, Proxmox, Unraid, CasaOS, Mac VM |

## Prerequisites
- Outbound internet access from the host
- No inbound firewall rules needed
- For Cloud VMs: size compute based on expected user load

## Gotchas
- Connectors do **not** need to be on every host—one per network segment is sufficient
- Serverless/PaaS deployments offer less control over CPU/memory/network resources allocated to Connectors
- Home networks with dynamic IPs, CGNATs (e.g., Starlink), or no inbound capability are fully supported—Connector handles this without port forwarding
- Static IP use case: Cloud VM Connectors are appropriate when users need a fixed egress IP

## Related Docs
- Peer-to-peer connections support
- Fair Use Policy (bandwidth)
- Remote Networks configuration
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Platform-specific guides: AWS EC2, GCP Compute, Azure Compute, K8s, Docker Compose, Terraform, Pulumi, Home Assistant, Raspberry Pi, Synology
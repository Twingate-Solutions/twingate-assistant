# Connector Deployment

## Summary
Twingate Connectors run as either a Linux systemd package or OCI (Docker) container. A single connector provides access to all reachable resources in its network; multiple connectors enable load-balancing and failover. No inbound firewall rules are required—only outbound internet access.

## Key Information
- Connectors do **not** need to be deployed on every host—one connector covers all reachable resources in its network
- Multiple connectors on separate hosts = automatic load-balancing + failover
- Supports x86/AMD64 and ARM64 architectures
- No inbound firewall rules needed; outbound internet access only
- Each deployment location should be its own Remote Network in Twingate

## Supported Linux Distributions

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|-------------|---------|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| On-prem/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology, Linux, Home Assistant, Proxmox, Unraid, CasaOS, Mac VM |

## Recommendations
- **Cloud VMs** preferred when available—most consistent performance, allows right-sizing
- **Minimum two connectors** on separate physical machines recommended for on-prem (redundancy)
- Cloud VMs appropriate when users need a **fixed static IP**
- Enable **peer-to-peer connections** to improve user experience and stay within Fair Use Policy bandwidth limits

## Gotchas
- Serverless/PaaS deployments offer less control over CPU/memory/network resources allocated to connectors
- Home networks with dynamic IPs or CGNAT (e.g., Starlink) have no inbound IP—connector deployment is the required solution
- Multiple locations require separate Remote Networks, not additional connectors in the same network

## Related Docs
- Peer-to-peer connections support
- Fair Use Policy
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Individual deployment guides: Terraform, Pulumi, AWS EC2, GCP, Azure, Kubernetes, Docker Compose, AWS ECS, Raspberry Pi, Home Assistant
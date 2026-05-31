# Connector Deployment

## Page Title
Deploying Connectors

## Summary
Twingate Connectors are deployed via Linux systemd packages or OCI (Docker) containers and do not need to be installed on every host—one connector per network location provides access to all reachable resources. Multiple connectors on separate hosts enable load-balancing and failover. Each distinct location or cloud should have its own Remote Network configured.

## Key Information
- Connectors require **outbound internet access only**—no inbound firewall rules needed
- Two deployment methods: **Linux systemd package** or **OCI/Docker container**
- Single connector serves all reachable resources in its network segment
- Multiple connectors on separate hosts = automatic load-balancing + failover
- Peer-to-peer connections reduce relay bandwidth and help stay within Fair Use Policy

## Supported Architectures & Distributions
**x86/AMD64 and ARM64:**
- Ubuntu 22.04, 24.04, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Methods by Environment

| Environment | Options |
|-------------|---------|
| Cloud VMs (recommended) | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| Office/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Raspberry Pi, Synology, Linux, Home Assistant, Proxmox, Unraid, CasaOS, Mac VM |

## Prerequisites
- Outbound internet access from the deployment host
- Linux-based environment (systemd or container runtime)
- Remote Network configured in Twingate admin console for each location

## Gotchas
- **Serverless/PaaS**: Less control over CPU/memory/network allocation compared to VMs
- **Dynamic IPs / CGNATs** (e.g., Starlink): Connector deployment is essential since inbound connections are impossible—connectors initiate outbound only
- **Multi-location**: Each separate location requires its own Remote Network—don't reuse a single Remote Network across locations
- Cloud VMs preferred over serverless when you need **static IP** for users or predictable resource sizing

## Configuration Values
None specified on this page—see individual deployment guides for environment-specific parameters.

## Related Docs
- Peer-to-peer connections setup
- Fair Use Policy
- AWS EC2 deployment
- Kubernetes deployment
- Terraform integration
- Pulumi integration
- Best Practices for Secure Infrastructure-as-Code (webinar)
# Connector Deployment - Twingate

## Summary
Twingate Connectors run as either a Linux systemd package or OCI (Docker) container. A single connector provides access to all reachable resources in its network; multiple connectors add load-balancing and failover. No inbound firewall rules are required—only outbound internet access.

## Key Information
- **Deployment formats**: Linux systemd package OR OCI/Docker container
- **Single connector** covers all reachable resources in its deployed network
- **Multiple connectors** (separate hosts) = automatic load-balancing + failover + added capacity
- **Multiple locations**: Add a separate Remote Network per location
- **Peer-to-peer connections** improve UX and help stay within Fair Use Policy bandwidth limits
- No inbound firewall rules required; only outbound internet access needed

## Supported Linux Distributions

**x86/AMD64 and ARM64:**
- Ubuntu 22.04 LTS, 24.04 LTS, 26.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+

**x86/AMD64 only:**
- Arch Linux, HP ThinPro, NixOS, Gentoo

## Deployment Options by Environment

| Environment | Options |
|-------------|---------|
| Cloud VMs | AWS EC2, GCP Compute, Azure Compute, Kubernetes |
| Office/Data Center | Docker Compose, Firewalla, Synology, QNAP, Proxmox, TrueNAS SCALE |
| Serverless/PaaS | AWS ECS (Fargate), Azure ACS, Aptible |
| IaC | Terraform, Pulumi |
| Home Network | Mac VM, Synology NAS, Raspberry Pi, Linux, Home Assistant, Proxmox, Unraid, CasaOS |

## Recommendations by Use Case

- **Best performance**: Cloud VMs (consistent resources, can be sized per usage)
- **Fixed static IP for users**: Cloud VM deployment
- **On-premises redundancy**: Deploy second connector on separate physical machine
- **No server management**: Serverless/PaaS environments
- **Repeatable multi-cloud**: IaC (Terraform/Pulumi)
- **Home with dynamic IP/CGNAT (e.g., Starlink)**: Home network connector (no inbound rules needed)

## Gotchas
- Connectors do **not** need to be installed on every host—only on a host that can route to target resources
- Serverless deployments offer easier management but less control over CPU/memory/network allocation
- Home network users with CGNAT (e.g., Starlink) have no inbound IP—connector solves this without port forwarding
- Peer-to-peer connections are important for bandwidth Fair Use Policy compliance

## Prerequisites
- Outbound internet access from the host running the connector
- Linux host matching supported distributions (for systemd installs)
- Docker/OCI runtime (for container installs)
- Remote Network configured in Twingate admin console

## Related Docs
- Peer-to-peer connections support guide
- Fair Use Policy
- Best Practices for Secure Infrastructure-as-Code (webinar)
- Individual platform guides (AWS EC2, Terraform, Kubernetes, etc.)
---
source: https://www.twingate.com/docs/connector-deployment
type: docs
fetched: 2026-11-13
source_version: fc77bbd55b5b5354f948849d010628fe2c8f1f787c46f83003a47dfa34ca8c6b
trust: official
---

# Page Title
Deploying Connectors (Twingate Docs)

## Summary
This page helps you choose a Connector deployment method for a target environment. All Twingate Connectors run either as a Linux `systemd` package or as an OCI (Docker) container. The page groups deployment options by environment: cloud, office/data center, serverless, IaC, and home network.

## Key Information
- A single Connector can provide access to any resource it can reach on its network. It does not need to run on every host.
- Additional Connectors on separate hosts add automatic load-balancing, failover, and capacity.
- For multiple locations or clouds, add a **Remote Network** per location.
- Peer-to-peer connections improve user experience and help stay within the Fair Use Policy for bandwidth. The page links to a guide on supporting them.
- **Supported Linux distributions (x86/AMD64 and ARM64):** Ubuntu 22.04/24.04/26.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+.
- **Additional (x64/AMD64 only):** Arch Linux, HP ThinPro, NixOS, Gentoo.

## Deployment Options by Environment
- **Cloud (recommended for consistent performance):** AWS EC2, GCP Compute, Azure Compute, Kubernetes. Suited to sizing Connectors for expected usage and to cases needing a fixed static IP.
- **Offices/data centers:** Docker Compose, Firewalla Box, Synology, QNAP NAS, Proxmox Container, TrueNAS SCALE. Works behind any firewall or NAT gateway.
- **Serverless (PaaS):** AWS ECS (Fargate), Azure Container Instances, Aptible. Easier to manage, but you have less control over CPU, memory, and network.
- **IaC:** Terraform, Pulumi. Gives repeatable, change-controlled rollouts, including multi-cloud.
- **Home network:** Mac (VM), Synology NAS DSM 7.x, Raspberry Pi, Linux, Home Assistant, Proxmox, Unraid, CasaOS. Useful for dynamic IPs or CGNAT (e.g., Starlink) and for reaching Plex, Windows file shares, or Home Assistant.

## Prerequisites
- A supported Linux distro (for the systemd package) or a container runtime (for OCI/Docker).
- Outbound Internet access from the Connector host.
- A Twingate Remote Network to attach the Connector to.

## Step-by-Step
This is a selection guide, not an install procedure. Choose your environment, then follow the linked platform-specific guide.

## Configuration Values
None on this page. Environment variables and tokens are covered in the individual deployment guides.

## Gotchas
- No inbound firewall rules are required, only outbound access.
- In offices and data centers, deploy a second Connector on a **separate physical machine** for redundancy.
- Serverless platforms limit resource control, which can affect Connector performance.
- Arch, HP ThinPro, NixOS, and Gentoo are supported on x64/AMD64 only, not ARM64.

## Related Docs
- Peer-to-peer connections guide
- Fair Use Policy
- Remote Networks
- Platform-specific guides: AWS EC2, GCP, Azure, Kubernetes, Docker Compose, Terraform, Pulumi, and others
- Webinar: Best Practices for Secure Infrastructure-as-Code Initiatives
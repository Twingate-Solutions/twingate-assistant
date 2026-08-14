---
source: https://www.twingate.com/docs/homelab-personal-use-case
type: docs
fetched: 2026-08-14
source_version: b856d16cfcd594a8b6e0c39f9aa481120a8c82f220ab687ac905cabadbfc7958
---

# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without requiring port forwarding or a VPN server. A free Starter plan is available, with typical setup under 15 minutes via a single Connector deployed on a home network device.

## Key Information
- **Free tier**: Starter plan available for personal use
- **No open inbound ports required**: eliminates port forwarding security risks
- **No static IP or dynamic DNS needed**
- Connector deployment options: Docker container or VM systemd service
- Supported platforms: Raspberry Pi, Synology NAS, QNAP NAS, TrueNAS SCALE, Proxmox, Firewalla, Linux servers, Windows

## Prerequisites
- One device on home network to host the Connector (Raspberry Pi, NAS, Linux/Windows server)
- Twingate account (free Starter plan sufficient for personal use)
- Docker or systemd-compatible environment on host device

## Step-by-Step Guides Available
- General homelab protection setup
- Home Assistant on Raspberry Pi
- Synology NAS (DSM 6.x and DSM 7.x separate guides)
- Plex Media Server
- Firewalla Connector deployment
- Proxmox Container deployment
- QNAP NAS deployment
- TrueNAS SCALE deployment

## Configuration Values
- Connector deployment methods: Docker image or systemd service
- Granular access control: per-resource permissions (e.g., grant access to specific resources only)

## Gotchas
- Synology NAS has **separate guides for DSM 6.x and DSM 7.x** — use the correct one for your version
- Single Connector per home network is sufficient; no need to deploy multiple
- Access grants are per-resource, so plan resource grouping when adding family/friend users

## Related Docs
- [Deployment Recommendations](https://www.twingate.com/docs) — guidance on where to deploy Connector
- Admin API, JavaScript CLI, Python CLI, Terraform, Pulumi — developer automation options
- Connector platform-specific deployment guides (linked above)
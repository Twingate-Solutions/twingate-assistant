## Page Title
Homelab & Personal Use Cases

## Summary
Use case overview for running Twingate on a home network to enable secure remote access without port forwarding or dynamic DNS. Free Starter plan available. Connector runs on Raspberry Pi, NAS devices, or any Linux/Docker host.

## Key Information
- Free Starter plan available for personal use — no credit card required
- Connector deployment options: Docker container or systemd service
- Supported home hardware: Raspberry Pi, Synology NAS (DSM 6 and 7), QNAP NAS, Proxmox, TrueNAS SCALE, Firewalla, Unraid
- No open inbound ports or port forwarding required
- No static IP or dynamic DNS needed on the home network
- Granular per-resource access — share specific resources (e.g. photo library) without exposing others (e.g. cameras)
- Desktop and mobile clients for all platforms
- Advanced features available: Admin API, Python CLI, JavaScript CLI, Terraform, Pulumi

## Prerequisites
- A device on the home network capable of running Docker or systemd (Raspberry Pi, NAS, Linux server, or Windows PC)
- Free Twingate account

## Step-by-Step
Not applicable on this page — see linked device-specific guides.

## Configuration Values
None on this page.

## Gotchas
- Starter plan has user and resource limits — check current plan limits at twingate.com/pricing
- Connector must remain running on the home network for remote access to work; plan for uptime (NAS or always-on device preferred over a laptop)

## Related Docs
- `/docs/homelab-step-by-step` — end-to-end homelab setup guide
- `/docs/home-assistant-getting-started` — Home Assistant integration
- `/docs/proxmox-getting-started` — Proxmox deployment
- `/docs/how-to-set-up-twingate-on-a-synology-nas-dsm-7` — Synology DSM 7
- `/docs/deploy-connector-on-firewalla` — Firewalla deployment
- `/docs/unraid-getting-started` — Unraid deployment

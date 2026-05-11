# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without port forwarding or VPN server configuration. A free Starter plan is available, with setup typically completed in under 15 minutes by deploying a single Connector on a home network device.

## Key Information
- No open inbound ports or port forwarding required
- No static IP or dynamic DNS configuration needed
- Free Starter plan available for personal use
- Connectors available as Docker container or systemd service (VM)
- Supports granular per-resource access control (e.g., grant family access to photos but not cameras)
- Cross-platform client apps: desktop and mobile

## Prerequisites
- A Twingate account (free Starter plan sufficient)
- A device on the home network to host the Connector (Raspberry Pi, NAS, Linux server, or Windows machine)

## Supported Connector Deployment Platforms
- Raspberry Pi
- Synology NAS (DSM 6.x and DSM 7.x)
- QNAP NAS
- TrueNAS SCALE
- Proxmox (container)
- Firewalla
- Any Docker-capable or Linux systemd device

## Step-by-Step Guides Available
1. General home lab protection setup
2. Home Assistant on Raspberry Pi
3. Synology NAS secure access
4. Plex Media Server secure access
5. Connector deployment on: Firewalla, Proxmox, QNAP, Synology DSM 6.x, Synology DSM 7.x, TrueNAS SCALE

## Configuration Values
- Connector deployment methods: Docker image or systemd service
- Access control: per-resource (network resource level)

## Developer/Automation Options
- Admin API
- JavaScript CLI configuration tool
- Python CLI configuration tool
- Terraform provider
- Pulumi provider

## Gotchas
- Synology NAS has separate guides for DSM 6.x and DSM 7.x — use the correct one for your version
- Connector must be deployed on a device that remains on and connected to the home network for persistent access

## Related Docs
- Twingate Connectors overview
- Deployment recommendations
- Admin API documentation
- Terraform / Pulumi integration guides
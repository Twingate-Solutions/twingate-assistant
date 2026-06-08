# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without port forwarding or VPN server configuration. A free Starter plan is available, with typical setup under 15 minutes via a Connector deployed on a single home network device.

## Key Information
- No open inbound ports or port forwarding required
- No static IP or dynamic DNS needed
- Free Starter plan available for personal use
- Connector runs on Raspberry Pi, NAS devices, Linux/Windows servers
- Connector deployment options: Docker container or systemd service VM
- Granular access control: share specific resources (e.g., photos but not cameras) with family/friends
- Cross-platform client apps: desktop and mobile

## Prerequisites
- A Twingate account (free Starter plan sufficient)
- One device on the home network to host the Connector (Raspberry Pi, NAS, Linux server, or Windows PC)
- Docker or systemd-compatible environment on the host device

## Supported Connector Platforms
- Raspberry Pi
- Firewalla
- Proxmox (container)
- QNAP NAS
- Synology NAS (DSM 6.x and DSM 7.x separately documented)
- TrueNAS SCALE
- Generic Linux (systemd service)

## Step-by-Step Guides Available
- General homelab protection setup
- Home Assistant on Raspberry Pi
- Synology NAS remote access
- Plex Media Server remote access
- Platform-specific Connector deployment guides (see links in source)

## Configuration Values
- No specific env vars documented on this page
- Connector deployment via Docker image or VM systemd service (details in platform-specific guides)

## Developer Features
| Feature | Description |
|---|---|
| Admin API | Programmatic network management |
| JavaScript CLI | Configuration tooling |
| Python CLI | Configuration tooling |
| Terraform provider | Infrastructure-as-code automation |
| Pulumi provider | Infrastructure-as-code automation |

## Gotchas
- Synology NAS has **separate guides** for DSM 6.x and DSM 7.x — use the correct one
- Only one Connector needed for basic home use, but placement matters — see deployment recommendations if unsure where to host it

## Related Docs
- Deployment recommendations
- Admin API documentation
- Terraform integration
- Pulumi integration
- Platform-specific guides: Firewalla, Proxmox, QNAP, Synology DSM 6/7, TrueNAS SCALE
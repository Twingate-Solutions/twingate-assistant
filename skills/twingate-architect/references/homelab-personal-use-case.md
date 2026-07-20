# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without requiring port forwarding, static IPs, or VPN server management. A free Starter plan is available for personal use, with typical setup completing in under 15 minutes via a single Connector deployment on a home network device.

## Key Information
- **Free tier**: Starter plan available for personal/homelab use
- **Core component**: One Twingate Connector deployed on any single home network device
- **No inbound ports required**: Eliminates port forwarding security risks
- **No static IP or dynamic DNS needed**
- **Connector deployment options**: Docker container or systemd service (VM)
- **Granular access control**: Per-resource permissions (e.g., share photos but not camera feeds)

## Prerequisites
- Twingate account (free Starter plan sufficient)
- One device on home network to run the Connector (Raspberry Pi, NAS, Linux server, or Windows PC)
- Twingate client apps installed on devices needing remote access

## Supported Connector Platforms
- Raspberry Pi
- Synology NAS (DSM 6.x and DSM 7.x+)
- QNAP NAS
- TrueNAS SCALE
- Proxmox (container)
- Firewalla
- Any Linux server (Docker or systemd)
- Windows computer

## Step-by-Step (High Level)
1. Create Twingate account at twingate.com
2. Deploy Connector on one home network device (Docker or systemd)
3. Define network Resources (services/IPs to expose)
4. Install Twingate client apps on remote devices
5. Grant access to users/groups per resource as needed

## Configuration Values
- **Deployment methods**: Docker container image or VM systemd service
- **Automation tools**: Terraform, Pulumi, Admin API, JavaScript CLI, Python CLI

## Gotchas
- Consult deployment recommendations page if unsure which device to use as Connector host
- DSM 6.x and DSM 7.x Synology deployments have separate guides—use the correct one for your version

## Related Docs
- [Deployment recommendations](#) — where to run the Connector
- [How to Protect Your Home Lab](#)
- [Home Assistant on Raspberry Pi setup guide](#)
- [Synology NAS setup guide](#)
- [Plex Media Server setup guide](#)
- [Firewalla, Proxmox, QNAP, TrueNAS SCALE deployment guides](#)
- [Admin API docs](#)
- [Terraform / Pulumi automation](#)
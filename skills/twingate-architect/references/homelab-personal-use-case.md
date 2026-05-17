# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without requiring port forwarding or static IPs. A free Starter plan is available, with typical setup under 15 minutes via a single Connector deployment on a home device.

## Key Information
- No open inbound ports or port forwarding required
- No static IP or dynamic DNS needed
- Connector runs on Raspberry Pi, NAS devices, Linux/Windows servers
- Connector deployment options: Docker container or systemd service (VM)
- Granular per-resource access control (share specific resources with specific users)
- Cross-platform client apps: desktop and mobile

## Prerequisites
- Twingate account (free Starter plan available)
- One device on home network to host the Connector (Raspberry Pi, NAS, Linux server, or Windows machine)

## Step-by-Step (High Level)
1. Create a Twingate account
2. Deploy a Connector on one home network device
3. Configure network Resources in the Admin console
4. Install Twingate client app on devices needing access
5. Grant access to users with appropriate permissions

## Supported Connector Platforms
- Raspberry Pi
- Firewalla
- Proxmox (container)
- QNAP NAS
- Synology NAS (DSM 6.x and DSM 7.x — separate guides)
- TrueNAS SCALE

## Configuration Values
- Deployment methods: Docker image, systemd service
- Developer tools available: Admin API, JavaScript CLI, Python CLI, Terraform provider, Pulumi provider

## Gotchas
- Synology NAS has separate guides for DSM 6.x vs DSM 7.x — use the correct one
- Check deployment recommendations if unsure which device to use as Connector host

## Related Docs
- [Deployment recommendations](#)
- [Admin API](#)
- [Terraform integration](#)
- [Pulumi integration](#)
- Specific guides: Home Assistant on Raspberry Pi, Synology NAS, Plex Media Server, Proxmox, QNAP, TrueNAS SCALE, Firewalla
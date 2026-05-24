# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home network services (Home Assistant, Plex, NAS, cameras) without port forwarding or static IPs. A free Starter plan is available, with typical setup under 15 minutes via a single Connector deployment on a home device.

## Key Information
- No open inbound ports or port forwarding required
- No static IP or dynamic DNS needed
- Free Starter plan available for personal use
- Connector runs on Raspberry Pi, NAS devices, Linux servers, Windows machines
- Connector deployment options: Docker container or systemd service (VM)
- Granular access control per resource (e.g., share photos but not cameras)
- Cross-platform client apps (desktop + mobile)

## Prerequisites
- A Twingate account (free Starter plan available)
- One always-on device on the home network to run the Connector (Raspberry Pi, NAS, Linux/Windows server)

## Step-by-Step (High Level)
1. Create Twingate account
2. Deploy a Connector on one home network device
3. Define network Resources in Twingate admin console
4. Install Twingate client app on remote devices
5. Connect and access home resources remotely

## Platform-Specific Guides
- Firewalla box
- Proxmox Container
- QNAP NAS
- Synology NAS (DSM 6.x or earlier)
- Synology NAS (DSM 7.x or later)
- TrueNAS SCALE
- Raspberry Pi (Home Assistant guide)

## Configuration Values
- Connector deployment methods: Docker image, systemd service
- Developer tools available: Admin API, JavaScript CLI, Python CLI, Terraform provider, Pulumi provider

## Gotchas
- Only one Connector needed per home network; no need to install on every home device
- Connector must be on a device that stays powered on for persistent remote access
- DSM version matters for Synology deployments (separate guides for 6.x vs 7.x)

## Related Docs
- Connector deployment recommendations
- Admin API documentation
- Terraform / Pulumi integration docs
- JavaScript and Python CLI configuration tools
- Home Assistant on Raspberry Pi setup guide
- Synology NAS setup guide
- Plex Media Server setup guide
- Homelab protection guide
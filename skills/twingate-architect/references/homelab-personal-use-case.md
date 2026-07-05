# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without port forwarding or VPN server configuration. A free Starter plan is available, with setup typically completing in under 15 minutes by deploying a single Connector on a home network device.

## Key Information
- **Free tier**: Starter plan available for personal use
- **No open inbound ports required**: eliminates port forwarding security risks
- **No static IP or dynamic DNS needed**
- **Connector deployment options**: Docker container or VM systemd service
- **Supported platforms**: Raspberry Pi, Synology NAS, QNAP NAS, TrueNAS SCALE, Proxmox, Firewalla, Linux servers, Windows

## Prerequisites
- Twingate account (free Starter plan sufficient)
- One device on home network to run the Connector
- Twingate client apps installed on accessing devices (desktop/mobile)

## Supported Home Devices (Connector Deployment)
| Device | Guide Available |
|--------|----------------|
| Firewalla | Yes |
| Proxmox Container | Yes |
| QNAP NAS | Yes |
| Synology NAS DSM 6.x | Yes |
| Synology NAS DSM 7.x | Yes |
| TrueNAS SCALE | Yes |
| Raspberry Pi | Yes (via Home Assistant guide) |

## Common Use Case Guides
- Home Assistant on Raspberry Pi
- Synology NAS remote access
- Plex Media Server remote access
- General homelab protection

## Configuration Values
- Connector deployment methods: Docker image or systemd service
- Access control: per-resource granular permissions (e.g., restrict specific resources per user)

## Developer Features
- Admin API
- JavaScript CLI configuration tool
- Python CLI configuration tool
- Terraform provider
- Pulumi provider

## Gotchas
- Only one Connector needed per home network (deploy on a single device)
- Connector must remain running for remote access to function — choose a device that stays powered on
- DSM 6.x and DSM 7.x Synology have separate deployment guides; use the correct one

## Related Docs
- Connector deployment recommendations
- Admin API documentation
- Terraform/Pulumi automation guides
- Individual platform deployment guides (linked above)
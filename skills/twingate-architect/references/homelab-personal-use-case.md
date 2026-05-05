# Homelab & Personal Use Cases

## Page Title
Twingate Homelab & Personal Use Cases

## Summary
Twingate provides secure remote access to home networks and self-hosted services without port forwarding or VPN server configuration. A free Starter plan is available, with typical setup time under 15 minutes via a single Connector deployment on a home network device.

## Key Information
- **Free tier available**: Starter plan supports personal/homelab use
- **No open inbound ports required**: eliminates port forwarding security risks
- **No static IP or dynamic DNS needed**
- **Connector deployment options**: Docker container or systemd service (VM)
- **Supported platforms**: Raspberry Pi, Synology NAS, QNAP NAS, TrueNAS SCALE, Proxmox, Firewalla, Linux servers, Windows

## Prerequisites
- A Twingate account (free Starter plan available)
- One device on the home network to host the Connector (Raspberry Pi, NAS, Linux/Windows machine)
- Docker or systemd-compatible OS on the Connector host

## Step-by-Step (High Level)
1. Create a Twingate account
2. Choose a Connector host device on your home network
3. Deploy the Connector (Docker image or systemd service)
4. Define network Resources (e.g., Home Assistant URL, Plex server, camera IPs)
5. Install Twingate client app on remote devices
6. Configure access permissions per resource for users/groups

## Configuration Values
- No specific env vars documented on this page
- Refer to platform-specific guides for Connector deployment flags
- Automation supported via: Terraform, Pulumi, Admin API, JS CLI, Python CLI

## Platform-Specific Guides
| Service/Device | Guide Available |
|---|---|
| Synology NAS (DSM 6.x) | Yes |
| Synology NAS (DSM 7.x) | Yes |
| QNAP NAS | Yes |
| TrueNAS SCALE | Yes |
| Proxmox Container | Yes |
| Firewalla | Yes |
| Home Assistant (Raspberry Pi) | Yes |
| Plex Media Server | Yes |

## Gotchas
- Only one Connector needed per home network (single device deployment)
- DSM 6.x and DSM 7.x Synology deployments have separate guides—confirm version before following
- Access permissions are per-resource and per-user; plan resource segmentation before inviting family/friends

## Related Docs
- [Deployment recommendations](https://www.twingate.com/docs/deployment-recommendations)
- [Admin API](https://www.twingate.com/docs/api)
- [Terraform integration](https://www.twingate.com/docs/terraform)
- [Pulumi integration](https://www.twingate.com/docs/pulumi)
- [JavaScript CLI configuration tool](https://www.twingate.com/docs/javascript-cli)
- [Python CLI configuration tool](https://www.twingate.com/docs/python-cli)
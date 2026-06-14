# Deploy Connector on Firewalla Box

## Summary
Install a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes. Runs in host network mode to access all LANs/VLANs. Only tested with Router mode configuration.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (Docker-capable models only)
- **Router mode only** — not tested with other Firewalla modes
- Host network mode is **required** for LAN/VLAN access
- Docker containers do not auto-start after reboot by default

## Prerequisites
- Firewalla running latest firmware in Router mode with outbound internet access
- SSH access to the Firewalla box from local network
- Twingate Admin Console with Remote Network, Resources, Users, and Groups configured

## Step-by-Step

1. SSH into Firewalla: `ssh pi@<firewalla-ip>`
2. Verify Docker is running: `sudo systemctl status docker`
3. In Admin Console: **Remote Networks → [Network] → Select/Add Connector**
4. Select **Docker** as deployment method
5. Click **Generate Tokens** (re-authentication required)
6. Configure Docker command options:
   - **Make Connector available on local network** → **Enable** (required for LAN/VLAN access; enables `--network host`)
   - **Custom DNS Server** → optional, skip for first-time setup
   - **Local network connection logs** → optional, useful for troubleshooting/SIEM
7. Copy and run the generated Docker command in SSH session
8. Verify connector is active in Admin Console and via `sudo docker ps`

## Configuration Values
| Option | Requirement |
|--------|-------------|
| Network mode | `host` (mandatory for LAN access) |
| Docker image | `twingate/connector:1` |
| Container command | `/connectord` |

## Gotchas
- **Auto-start after reboot**: Docker and containers won't restart automatically — use [Firewalla's Customized Scripting](https://help.firewalla.com) to add a post-reboot startup script
- **Connectivity restrictions**: Don't apply outbound firewall restrictions until the connector successfully establishes initial connection
- **Peer-to-peer connections**: Should be enabled to improve performance and comply with Twingate Fair Use Policy

## Verify Deployment
```bash
sudo docker ps
# Healthy containers show: Up X days (healthy)
```

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Firewalla Customized Scripting](https://help.firewalla.com)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
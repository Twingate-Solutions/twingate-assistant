# Deploy Connector on Firewalla Box

## Summary
Deploys a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes. Requires Router mode configuration. Eliminates need for open inbound ports by running the Connector behind the firewall.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- **Router mode only** — not tested on other Firewalla modes
- Docker containers and Connector do **not** auto-start after reboot by default; requires custom scripting
- Two Connectors per Remote Network recommended (redundancy + peer-to-peer support)

## Prerequisites
- Firewalla box running latest firmware in **Router mode** with outbound internet access
- SSH access from local network to Firewalla box (`ssh pi@<firewalla-ip>`)
- Docker enabled and running on the Firewalla box
- Twingate Admin Console with Remote Network, Resources, Users, and Groups configured

## Step-by-Step

1. **SSH into Firewalla** from local network: `ssh pi@<firewalla-ip>`
2. **Verify Docker is running**: `sudo systemctl status docker`
3. **Open Admin Console**: Remote Networks → Select Network → Add/Select Connector
4. **Deployment Method**: Select `Docker`
5. **Generate Tokens**: Authenticate to generate connector tokens
6. **Customize Docker Command**:
   - Custom DNS: Optional (skip if first-time user)
   - **"Make Connector available on local network"**: **Enable** (required for LAN/VLAN access — runs in host network mode)
   - Local network connection logs: Optional (useful for SIEM/troubleshooting)
7. **Run generated Docker command** in SSH session
8. **Verify** Connector shows active in Admin Console

## Configuration Values

| Option | Value | Notes |
|--------|-------|-------|
| Host network mode | `--network host` | Required for LAN/VLAN access |
| Docker image | `twingate/connector:1` | |
| Default user | `pi` | SSH login |

## Verification Command
```bash
sudo docker ps
# Healthy containers show: STATUS: Up X days (healthy)
```

## Gotchas
- **Host network mode is required** — without it, the Connector cannot reach LANs/VLANs on the Firewalla box
- **No auto-start after reboot** — configure via [Firewalla Customized Scripting](https://help.firewalla.com/hc/en-us/articles/360052177953) to restart Docker containers on boot
- Verify outbound connectivity before adding firewall restrictions; consult Connector Best Practices if connection fails
- Configuration only tested in Router mode — other modes unsupported

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- [Firewalla Router Mode Setup](https://help.firewalla.com)
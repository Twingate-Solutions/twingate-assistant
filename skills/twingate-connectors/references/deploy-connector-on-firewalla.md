# Deploy Connector on Firewalla Box

## Summary
Deploy a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable remote network access without exposed inbound ports. Configuration is tested only in Router mode. Containers must run in host network mode to access LANs/VLANs.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested in other modes
- Host network mode is **required** for LAN/VLAN access
- Docker containers and Connector do **not** auto-start after reboot by default
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Firewalla running latest firmware in Router mode with outbound internet access
- SSH access from local network to Firewalla box
- Docker enabled on the Firewalla box
- Twingate Admin Console with Remote Network, Resources, Users, and Groups configured

## Step-by-Step

1. **SSH into Firewalla box** from local network:
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running**:
   ```bash
   sudo systemctl status docker
   ```

3. **Open Twingate Admin Console** → Remote Networks → Select network → Select/Add Connector

4. **Select Docker** as deployment method

5. **Generate Tokens** (re-authentication required)

6. **Configure Docker command options**:
   - Custom DNS Server: optional, skip if first-time user
   - **Make Connector available on local network: Enable** (sets host network mode — required)
   - Local network connection logs: optional, useful for SIEM/troubleshooting

7. **Run generated Docker command** in SSH session

8. **Verify Connector is active** in Admin Console, or check locally:
   ```bash
   sudo docker ps
   # Healthy containers show: twingate/connector:1 ... (healthy)
   ```

## Configuration Values
| Option | Value | Notes |
|--------|-------|-------|
| Docker image | `twingate/connector:1` | |
| Network mode | host | Required for LAN/VLAN access |
| Container command | `/connectord` | |

## Gotchas
- **Auto-start after reboot**: Docker and Connector containers won't restart automatically — use [Firewalla Customized Scripting](https://help.firewalla.com) to run startup scripts post-reboot
- **Connectivity restrictions**: Don't restrict outbound connectivity until Connector successfully connects first
- **Router mode only**: Other Firewalla modes are untested and unsupported

## Related Docs
- [Firewalla SSH Access](https://help.firewalla.com)
- [Firewalla Customized Scripting](https://help.firewalla.com)
- [Twingate Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
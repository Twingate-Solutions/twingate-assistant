# Deploy Connector on Firewalla Box

## Summary
Deploy a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable secure remote access without open inbound ports. Configuration is tested only in Router mode. Containers must run in host network mode to access LANs/VLANs.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested in other modes
- Host network mode is **required** for LAN/VLAN access
- Containers do not auto-start after reboot by default — requires custom scripting

## Prerequisites
- Firewalla running latest firmware in **Router mode**
- Outbound internet access confirmed
- Twingate Admin Console configured: Users, Groups, Remote Networks, Resources
- SSH access to Firewalla box from local network

## Step-by-Step

1. **SSH into Firewalla box**
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running**
   ```bash
   sudo systemctl status docker
   ```

3. **Navigate in Admin Console**: Remote Networks → Select Network → Select/Add Connector

4. **Deployment wizard steps**:
   - Step 1: Select **Docker** as deployment method
   - Step 2: Click **Generate Tokens** (re-authentication required)
   - Step 3: Customize Docker command:
     - Custom DNS Server: optional, skip for first-time use
     - **"Make Connector available on local network"**: **Enable** (sets host network mode — required)
     - Local network connection logs: optional, useful for troubleshooting/SIEM
   - Step 4: Paste generated Docker command into SSH session
   - Step 5: Wait for Connector status to show **active** in Admin Console

5. **Verify running containers**
   ```bash
   sudo docker ps
   ```

## Configuration Values
| Option | Value | Notes |
|--------|-------|-------|
| Deployment method | Docker | |
| Network mode | host | Required for LAN/VLAN access |
| Container image | `twingate/connector:1` | |
| Default command | `/connectord` | |

## Gotchas
- **No auto-start on reboot**: Docker and Connector containers won't restart automatically — configure via [Firewalla Customized Scripting](https://help.firewalla.com/hc/en-us/articles/360051625034)
- Host network mode is mandatory; skipping this breaks LAN/VLAN access
- Don't restrict outbound connectivity until initial connection is verified
- Peer-to-peer connections recommended to stay within Twingate Fair Use Policy bandwidth limits

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- [Firewalla Router Mode Setup](https://help.firewalla.com)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
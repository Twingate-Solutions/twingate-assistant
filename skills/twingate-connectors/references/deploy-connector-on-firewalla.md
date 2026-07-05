# Deploy Connector on Firewalla Box

## Summary
Deploys a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable remote network access without exposed inbound ports. Requires Router mode configuration. Host network mode is mandatory for LAN/VLAN access.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested in other modes
- Host network mode required for container to access LANs/VLANs
- Containers do not auto-start after reboot by default; requires custom scripting
- Eliminates need for open inbound ports

## Prerequisites
- Firewalla box running latest firmware in **Router mode**
- Outbound internet access confirmed
- SSH access from local network
- Twingate Admin Console configured: Users, Groups, Remote Networks, Resources
- Docker enabled on Firewalla box

## Step-by-Step

1. **SSH into Firewalla box** from local network:
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running**:
   ```bash
   sudo systemctl status docker
   ```

3. **Navigate in Admin Console**: Remote Networks → Select Remote Network → Select/Add Connector

4. **Deployment wizard steps**:
   - Step 1: Select **Docker** as deployment method
   - Step 2: Click **Generate Tokens**, re-authenticate
   - Step 3: Configure options (see Configuration Values below)
   - Step 4: Copy/paste generated Docker command into SSH session
   - Step 5: Wait for Connector status to show **active** in console

5. **Verify running containers**:
   ```bash
   sudo docker ps
   # Healthy containers show: Up X days (healthy)
   ```

6. **Configure auto-start** via Firewalla [Customized Scripting](https://help.firewalla.com) to restart Docker containers after reboot.

## Configuration Values

| Option | Setting | Notes |
|--------|---------|-------|
| Deployment Method | Docker | Required |
| Make Connector available on local network | **Enable** | Runs in host network mode — required for LAN/VLAN access |
| Custom DNS Server | Optional | Use if local DNS server needed for FQDN resolution |
| Local network connection logs | Optional | Enable for troubleshooting/SIEM ingestion |

## Gotchas
- **Host network mode is required** — must enable "Make Connector available on local network" or the container cannot reach LANs/VLANs
- **No auto-start after reboot** — Docker and Connector containers won't restart automatically; must configure via Firewalla scripting
- Router mode only — configuration untested in Simple/DHCP modes
- Don't restrict outbound connectivity until Connector successfully establishes first connection

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Firewalla Customized Scripting](https://help.firewalla.com)
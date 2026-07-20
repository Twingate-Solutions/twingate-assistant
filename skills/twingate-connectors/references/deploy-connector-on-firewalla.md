# Deploy Connector on Firewalla Box

## Summary
Deploys a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable remote network access without open inbound ports. Requires Router mode configuration. Docker containers must be manually configured to start after reboot.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested in other modes
- Connector runs in Docker host network mode (required for LAN/VLAN access)
- Containers do not auto-start after reboot by default
- Two connectors shown in example (recommended for redundancy)

## Prerequisites
- Firewalla box running latest firmware in **Router mode**
- Outbound internet access confirmed
- SSH access from local network to Firewalla box
- Twingate Admin Console configured: Users, Groups, Remote Networks, Resources
- Docker enabled on Firewalla (`sudo systemctl status docker`)

## Step-by-Step

1. **SSH into Firewalla** from local network:
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running:**
   ```bash
   sudo systemctl status docker
   ```

3. **In Twingate Admin Console:** Navigate to Remote Networks → Select/Add Connector

4. **Deployment wizard:**
   - Step 1: Select **Docker**
   - Step 2: Click **Generate Tokens** (re-authentication required)
   - Step 3: Configure options (see below)
   - Step 4: Paste generated Docker command into SSH session
   - Step 5: Wait for Connector status to show **active**

5. **Verify running containers:**
   ```bash
   sudo docker ps
   ```

## Configuration Values

| Option | Setting | Notes |
|--------|---------|-------|
| Deployment Method | Docker | |
| Make Connector available on local network | **Enable** | Required — runs in host network mode for LAN/VLAN access |
| Local network connection logs | Enable (optional) | For troubleshooting/SIEM |
| Custom DNS Server | Optional | Skip for first-time setup; use if local DNS needed for FQDN resolution |

## Gotchas
- **Host network mode is required** — must enable "Make Connector available on local network" or the container cannot reach LANs/VLANs
- **No auto-start after reboot** — configure via [Firewalla Customized Scripting](https://help.firewalla.com/hc/en-us/articles/360051625034) to restart Docker containers on boot
- Don't restrict outbound connectivity until Connector successfully connects — verify open access first
- Enable peer-to-peer connections to avoid Fair Use Policy bandwidth issues

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- [Firewalla Router Mode Setup](https://help.firewalla.com)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [SSH into Firewalla](https://help.firewalla.com/hc/en-us/articles/360008543113)
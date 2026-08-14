---
source: https://www.twingate.com/docs/deploy-connector-on-firewalla
type: docs
fetched: 2026-08-14
source_version: 1ab931e2e435906ba07db02b29139ac1a022f66809e8c8fc3af9fd8e50378fb9
---

# Deploy Connector on Firewalla Box

## Summary
Deploys a Twingate Connector via Docker on Firewalla boxes (Gold, Purple, Blue Plus) to enable remote access without open inbound ports. Requires Router mode configuration. Container must run in host network mode to access LANs/VLANs.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested on other modes
- Host network mode is **required** for LAN/VLAN access
- Docker and Connector container do **not** auto-start after reboot by default
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Firewalla box running latest firmware in **Router mode**
- Outbound internet access confirmed
- SSH access to Firewalla box from local network
- Twingate Admin Console configured (Users, Groups, Remote Networks, Resources)

## Step-by-Step

1. **SSH into Firewalla box**
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running**
   ```bash
   sudo systemctl status docker
   # Confirm: Active: active (running)
   ```

3. **In Twingate Admin Console**: Navigate to Remote Networks → Select/Add Connector

4. **Deployment wizard steps**:
   - Step 1: Select **Docker** as deployment method
   - Step 2: Click **Generate Tokens** (re-authentication required)
   - Step 3: Configure options:
     - Custom DNS Server — optional, skip if first-time user
     - **Make Connector available on local network** — **Enable** (required for LAN/VLAN access; runs in host network mode)
     - Local network connection logs — optional, useful for troubleshooting/SIEM
   - Step 4: Paste generated Docker command into SSH terminal
   - Step 5: Wait for connector status to show **active** in Admin Console

5. **Verify running containers**
   ```bash
   sudo docker ps
   # Expect STATUS: Up X days (healthy)
   ```

## Configuration Values

| Option | Value | Notes |
|--------|-------|-------|
| Deployment method | Docker | |
| Network mode | Host | Required for LAN/VLAN access |
| Docker image | `twingate/connector:1` | |
| Container command | `/connectord` | |

## Gotchas
- **Host network mode is mandatory** — without it, the connector cannot reach LANs/VLANs behind Firewalla
- **No auto-start on reboot** — must configure post-reboot scripting via [Firewalla Customized Scripting](https://help.firewalla.com) to auto-restart Docker containers
- If connector fails to connect, remove outbound restrictions first, verify connectivity, then re-add restrictions
- Configuration only tested on Router mode — other modes unsupported

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- Firewalla Router Mode configuration guides
- Firewalla Customized Scripting docs
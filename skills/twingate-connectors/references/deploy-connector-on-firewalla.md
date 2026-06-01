# Deploy Connector on Firewalla Box

## Summary
Deploys a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable remote access without open inbound ports. Requires Router mode configuration. Host network mode is mandatory for LAN/VLAN access.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- **Router mode only** — not tested on other Firewalla modes
- Eliminates need for open inbound ports (unlike traditional VPN)
- Docker containers do **not** auto-start after reboot by default — requires custom scripting

## Prerequisites
- Latest Firewalla firmware installed
- Firewalla configured in Router mode with outbound internet access
- Basic Twingate setup complete (Users, Groups, Remote Networks, Resources)
- SSH access from local network to Firewalla box

## Step-by-Step

1. **SSH into Firewalla box**
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. **Verify Docker is running**
   ```bash
   sudo systemctl status docker
   ```

3. **Open Twingate Admin Console** → Remote Networks → Select Network → Add Connector

4. **Select Docker** as deployment method

5. **Generate Tokens** (re-authentication required)

6. **Configure Docker command options:**
   - Custom DNS Server — optional, skip for first-time users
   - **Make Connector available on local network** — **Enable** (required for LAN/VLAN access; runs in host network mode)
   - Local network connection logs — optional, useful for troubleshooting/SIEM

7. **Paste and run** the generated Docker command in SSH session

8. **Verify connection** in Admin Console (Connector shows active)

9. **Verify running containers**
   ```bash
   sudo docker ps
   ```

## Configuration Values

| Option | Value | Notes |
|--------|-------|-------|
| Deployment method | Docker | — |
| Network mode | host | Required for LAN/VLAN access |
| Container image | `twingate/connector:1` | — |
| Container command | `/connectord` | — |

## Gotchas
- **Host network mode is required** — without enabling "Make Connector available on local network," the container cannot reach Firewalla LANs/VLANs
- **No auto-start on reboot** — configure via [Firewalla Customized Scripting](https://help.firewalla.com) to restart Docker containers post-reboot
- Do not restrict outbound connectivity until Connector is confirmed working
- Only tested in Router mode — other modes unsupported

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
- Firewalla Customized Scripting (Firewalla official docs)
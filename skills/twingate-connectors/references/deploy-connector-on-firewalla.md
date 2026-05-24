# Deploy Connector on Firewalla Box

## Summary
Deploy a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus boxes to enable secure remote access without open inbound ports. Configuration is tested only in Router mode. Enables access to LANs/VLANs managed by the Firewalla box.

## Key Information
- Supported hardware: Firewalla Gold, Purple, Blue Plus (native Docker support required)
- Router mode only — not tested in other modes
- Host network mode is **required** for container to access LANs/VLANs
- Docker and connector containers do **not** auto-start after reboot by default
- Peer-to-peer connections recommended for Fair Use Policy compliance

## Prerequisites
- Firewalla box running latest firmware in Router mode with outbound internet access
- SSH access from local network to Firewalla box
- Twingate account with Remote Network, Resources, Users, and Groups configured
- Docker enabled on the Firewalla box

## Step-by-Step

1. SSH into Firewalla box from local network:
   ```bash
   ssh pi@<firewalla-ip>
   ```

2. Verify Docker is running:
   ```bash
   sudo systemctl status docker
   ```

3. In Twingate Admin Console: **Remote Networks → [Your Network] → Add Connector**

4. Select **Docker** as deployment method

5. Click **Generate Tokens** (re-authentication required)

6. Configure Docker command options:
   - **Make Connector available on local network**: **Enable** (required — runs in host network mode)
   - **Custom DNS Server**: Optional, for local FQDN resolution
   - **Local network connection logs**: Optional, for troubleshooting/SIEM

7. Copy and run the generated Docker command in SSH session

8. Verify connector is active in Admin Console and via:
   ```bash
   sudo docker ps
   ```

## Configuration Values

| Option | Value | Notes |
|--------|-------|-------|
| Deployment method | Docker | |
| Network mode | Host (`--network=host`) | Required for LAN/VLAN access |
| Docker image | `twingate/connector:1` | |
| Container command | `/connectord` | |

## Gotchas
- **Auto-start on reboot**: Must configure manually via [Firewalla's Customized Scripting](https://help.firewalla.com/hc/en-us/articles/360052819853) — Docker and containers won't restart automatically
- **Host network mode is mandatory** — without it, the connector cannot reach LANs/VLANs
- Only tested in **Router mode** — other Firewalla modes are unsupported
- If connection fails, avoid setting outbound connectivity restrictions until basic connectivity is confirmed; check [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Site-to-Site with Twingate](https://www.twingate.com/docs/site-to-site)
- [Firewalla Router Mode Setup](https://help.firewalla.com)
- [Firewalla Customized Scripting](https://help.firewalla.com/hc/en-us/articles/360052819853)
- [Twingate Quick Start](https://www.twingate.com/docs/quick-start)
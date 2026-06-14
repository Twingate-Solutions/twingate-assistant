# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware (UDM Pro, UDM SE, UXG-Pro, UXG-Max). The container persists on `/data` partition across firmware upgrades. Setup is automated via a single curl/bash command.

## Key Information
- Supported devices: UDM Pro, UDM SE, UXG-Pro, UXG-Max running UniFi OS 3.x+
- Container stored at `/data/custom/machines/` (firmware-upgrade safe)
- Initial debootstrap takes 5–10 minutes — expected behavior
- Multiple connectors supported via `CONTAINER_NAME` variable

## Prerequisites
- Ubiquiti Gateway with UniFi OS 3.x or later
- Root SSH access to the Gateway
- Twingate Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens
2. **Copy**: Network name (subdomain only, e.g., `mycompany`), Access Token, Refresh Token
3. **Deploy via SSH**:
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-connector/main/setup.sh | \
  sudo TWINGATE_NETWORK="mycompany" \
  TWINGATE_ACCESS_TOKEN="<token>" \
  TWINGATE_REFRESH_TOKEN="<token>" bash
```
4. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show `connected`
5. **Add Resource**: Create a Resource with Gateway's private IP (e.g., `192.168.x.x`) for remote UI access

## Configuration Values

| Variable | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Subdomain only (not full URL) |
| `TWINGATE_ACCESS_TOKEN` | Yes | Per-connector access token |
| `TWINGATE_REFRESH_TOKEN` | Yes | Per-connector refresh token |
| `CONTAINER_NAME` | No | Default: `twingate-connector` |

## Container Management Commands

```bash
machinectl status twingate-connector    # View status
machinectl stop twingate-connector      # Stop
machinectl start twingate-connector     # Start
machinectl disable twingate-connector   # Disable autostart

# Shell access inside container:
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Uninstall:
sudo ./uninstall.sh  # from GitHub repo
```

## Gotchas
- **Tokens are single-use per connector** — never reuse; regenerate for redeployment
- After firmware upgrade, symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may be lost — re-run setup script to restore (detects existing container data)
- Network name is subdomain only, not the full URL
- Each connector requires its own unique token pair

## Troubleshooting
```bash
# Container logs:
journalctl -M twingate-connector -xe --no-pager

# Connector service logs:
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- journalctl -u twingate-connector -n 50 --no-pager

# DNS check inside container:
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- curl -s https://binaries.twingate.com
```

## Related Docs
- [Proxmox Setup Guide](https://www.twingate.com/docs/deploy-connector-on-proxmox)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/deploy-connector-on-home-assistant)
- [Unraid Setup Guide](https://www.twingate
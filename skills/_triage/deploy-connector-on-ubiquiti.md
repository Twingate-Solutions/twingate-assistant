<!-- triage: unassigned URL: https://www.twingate.com/docs/deploy-connector-on-ubiquiti -->

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector on Ubiquiti Gateway devices (UDM Pro, UDM SE, UXG-Pro, UXG-Max) using a systemd-nspawn Debian container. The setup script installs and configures the Connector to auto-start on boot. Container is stored on `/data` partition and survives firmware upgrades.

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x or later
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on the Gateway

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Subdomain of your Twingate URL (e.g., `mycompany`) |
| `TWINGATE_ACCESS_TOKEN` | Per-connector access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Per-connector refresh token from Admin Console |
| `CONTAINER_NAME` | Optional; overrides default `twingate-connector` name |

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens. Copy Network name, Access Token, Refresh Token.

2. **Deploy via SSH**:
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-connector/main/setup.sh | \
sudo TWINGATE_NETWORK="mycompany" \
TWINGATE_ACCESS_TOKEN="<token>" \
TWINGATE_REFRESH_TOKEN="<token>" bash
```

3. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show `connected`.

4. **Add Resource**: Create a Twingate Resource pointing to the Gateway's private IP (e.g., `192.168.x.x`) to enable remote access to UniFi dashboard.

## Container Management Commands

```bash
machinectl status twingate-connector    # View status
machinectl stop twingate-connector      # Stop
machinectl start twingate-connector     # Start
machinectl disable twingate-connector   # Disable auto-start

# Shell access inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Uninstall
sudo ./uninstall.sh
```

## Gotchas
- **Tokens are single-use per Connector** — never reuse token sets; generate new tokens if redeploying
- Initial debootstrap takes **5–10 minutes** — this is normal
- After firmware upgrade, symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation — re-run setup script to auto-fix (detects existing container)
- Use `CONTAINER_NAME` env var when deploying multiple Connectors on the same Gateway

## Troubleshooting Commands
```bash
# Container logs
journalctl -M twingate-connector -xe --no-pager

# Connector service logs
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- journalctl -u twingate-connector -n 50 --no-pager

# Test DNS/connectivity inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- curl -s https://binaries.twingate.com
```

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/Twingate-Community/ubiquiti-connector)
- Proxmox, Home Assistant, and Unraid setup guides available in Twingate docs
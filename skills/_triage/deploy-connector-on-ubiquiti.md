<!-- triage: unassigned URL: https://www.twingate.com/docs/deploy-connector-on-ubiquiti -->

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway devices. The container lives on `/data` partition, persisting through firmware upgrades. Setup is automated via a single curl/bash script.

## Key Information
- Supported devices: UDM Pro, UDM SE, UXG-Pro, UXG-Max, similar UniFi OS devices
- Container managed via `machinectl` commands
- Initial debootstrap takes 5–10 minutes (normal)
- Each Connector requires unique tokens — never reuse token sets
- Multiple Connectors on same Gateway supported via `CONTAINER_NAME` override

## Prerequisites
- Ubiquiti Gateway running **UniFi OS 3.x or later**
- SSH root access to Gateway
- Twingate account with Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → select/add Connector → Manual → Generate Tokens → copy Network name, Access Token, Refresh Token
2. **Deploy via SSH**:
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-connector/main/setup.sh | \
  sudo TWINGATE_NETWORK="mycompany" \
  TWINGATE_ACCESS_TOKEN="<token>" \
  TWINGATE_REFRESH_TOKEN="<token>" bash
```
3. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show `connected`
4. **Optional**: Add Gateway's private IP as a Twingate Resource for remote UI access

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Subdomain only (e.g., `mycompany` from `mycompany.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |
| `CONTAINER_NAME` | Optional; overrides default `twingate-connector` |

## Container Management Commands

```bash
machinectl status twingate-connector
machinectl start twingate-connector
machinectl stop twingate-connector
machinectl disable twingate-connector

# Shell inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- /bin/bash

# Uninstall
sudo ./uninstall.sh  # from GitHub repo
```

## Gotchas
- **Firmware upgrades**: Symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may not survive upgrades — re-run setup script to restore (detects existing container, won't overwrite data)
- **Token reuse**: Tokens are single-use per Connector; regenerate if redeploying
- **Network name**: Use subdomain only, not full URL
- **Bootstrap time**: 5–10 min is expected, not a hang

## Troubleshooting Commands
```bash
# Container logs
journalctl -M twingate-connector -xe --no-pager

# Connector service logs
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- \
  journalctl -u twingate-connector -n 50 --no-pager

# Test DNS/connectivity inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- \
  curl -s https://binaries.twingate.com
```

## Related Docs
- [Setting Up Resources](https://www.twingate.com/docs/resources)
- Proxmox, Home Assistant, Unraid setup guides
- [GitHub Repository](https://github.com/Twingate-Community/ubiquiti-connector)
- General Twingate troubleshooting docs
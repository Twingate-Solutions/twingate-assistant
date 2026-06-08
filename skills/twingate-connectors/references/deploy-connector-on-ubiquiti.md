# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware. The container lives on `/data` partition, surviving firmware upgrades. Setup is automated via a single curl/bash script.

## Key Information
- Supported devices: UDM Pro, UDM SE, UXG-Pro, UXG-Max, similar UniFi OS devices
- Container stored at `/data/custom/machines/` (persistent across firmware upgrades)
- Symlinks at `/var/lib/machines/` and configs at `/etc/systemd/nspawn/` may not survive upgrades—re-run setup script to recreate them
- Initial debootstrap takes 5–10 minutes on Gateway hardware
- Multiple Connectors on same device supported via `CONTAINER_NAME` override

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x or later
- SSH root access to Gateway
- Twingate account with Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → Manual → Generate Tokens → copy Network name, Access Token, Refresh Token
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
| `CONTAINER_NAME` | Optional; default `twingate-connector` |

## Container Management Commands

```bash
machinectl status twingate-connector
machinectl stop twingate-connector
machinectl start twingate-connector
machinectl disable twingate-connector

# Shell inside container:
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Uninstall:
sudo ./uninstall.sh  # from GitHub repo
```

## Gotchas
- **Tokens are single-use per Connector**—generate a new set if redeploying; never reuse token pairs
- After firmware upgrade, re-run setup script if container fails to start (symlinks/configs need recreation)
- `TWINGATE_NETWORK` is the subdomain only, not the full URL
- Troubleshoot with: `journalctl -M twingate-connector -xe --no-pager` or check DNS with `curl -s https://binaries.twingate.com` inside container

## Related Docs
- [General Troubleshooting](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/Twingate-Community/ubiquiti-connector)
- Proxmox, Home Assistant, Unraid setup guides (sibling docs)
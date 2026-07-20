# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware (UDM Pro, UDM SE, UXG-Pro, UXG-Max). The container lives on `/data` partition, surviving firmware upgrades. Connector auto-starts on boot via systemd.

## Key Information
- Container stored at `/data/custom/machines/` — persists across firmware upgrades
- Symlinks at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation after upgrades (re-run setup script)
- Bootstrap (debootstrap) takes **5–10 minutes** — expected behavior
- Default container name: `twingate-connector` (customizable via `CONTAINER_NAME`)
- Each Connector requires its own unique token pair — tokens are single-use

## Prerequisites
- Ubiquiti Gateway running **UniFi OS 3.x or later**
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → select/add Connector → choose Ubiquiti → Generate Tokens
2. **SSH into Gateway**, run the copied bash command (includes Network name, Access token, Refresh token)
3. **Verify**: Admin Console → Remote Network → Connector → confirm Controller and Relay show `connected`
4. **Add Resource** (optional): Create Resource with Gateway's private IP (e.g., `192.168.x.x`) to access UniFi dashboard remotely

## Container Management Commands

```bash
# Status / control
machinectl status twingate-connector
machinectl stop twingate-connector
machinectl start twingate-connector
machinectl disable twingate-connector

# Shell inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Uninstall
sudo ./uninstall.sh  # from GitHub repo
```

## Troubleshooting

| Issue | Command |
|-------|---------|
| Container status/logs | `machinectl status twingate-connector` |
| Detailed container logs | `journalctl -M twingate-connector -xe --no-pager` |
| DNS check inside container | `nsenter ... -- curl -s https://binaries.twingate.com` |
| Connector service logs | `nsenter ... -- journalctl -u twingate-connector -n 50 --no-pager` |

## Gotchas
- **Never reuse tokens** — generate a new set for each Connector deployment
- Token errors require regeneration from Admin Console; no token recovery
- After firmware upgrade, re-run setup script to recreate missing symlinks/nspawn config — existing container data is preserved
- Container name in all `machinectl`/`nsenter` commands must match `CONTAINER_NAME` set during install

## Related Docs
- [General Troubleshooting Docs](https://www.twingate.com/docs)
- Proxmox Setup Guide
- Home Assistant Setup Guide
- Unraid Setup Guide
- [GitHub Repository](https://github.com/twingate) (uninstall script source)
---
source: https://www.twingate.com/docs/deploy-connector-on-ubiquiti
type: docs
fetched: 2026-08-05
source_version: 9f1bb837fd8ca50cf4ac41554b291ae43c617563b61e582239528bcefe8f8989
---

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway devices. The container is stored on `/data` partition (persists across firmware upgrades) and configured to auto-start on boot. Setup takes 5–10 minutes due to debootstrap on Gateway hardware.

## Key Information
- Supported devices: UDM Pro, UDM SE, UXG-Pro, UXG-Max, similar UniFi OS devices
- Container stored at `/data/custom/machines/` — survives firmware upgrades
- Symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation after firmware upgrade (re-run setup script)
- Each Connector requires its own unique token set — tokens are single-use per Connector

## Prerequisites
- Ubiquiti Gateway running **UniFi OS 3.x or later**
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose **Ubiquiti** option → Step 2 → **Generate Tokens**
2. **Copy the bash command** (includes Network name, Access token, Refresh token)
3. **SSH into Gateway** and run the copied command
4. **Verify**: Admin Console → Remote Networks → select network → confirm Connector shows `Controller` and `Relay` as **connected**
5. **Add Resource** (optional): Create a Resource with Gateway's private IP (e.g., `192.168.x.x`) to access UniFi dashboard remotely

## Container Management Commands

| Command | Description |
|---|---|
| `machinectl status twingate-connector` | View status |
| `machinectl stop twingate-connector` | Stop container |
| `machinectl start twingate-connector` | Start container |
| `machinectl disable twingate-connector` | Disable auto-start |

**Shell into container:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash
```

**View Connector logs:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- journalctl -u twingate-connector -n 50 --no-pager
```

**Uninstall:**
```bash
sudo ./uninstall.sh  # from GitHub repo
```

## Configuration Values
- `CONTAINER_NAME`: Custom container name (default: `twingate-connector`) — replace in all commands if customized

## Gotchas
- Bootstrap (debootstrap) takes **5–10 minutes** — expected, not an error
- Do **not** reuse token sets across Connectors
- After firmware upgrade: `/var/lib/machines/` symlink and `/etc/systemd/nspawn/` config may be lost; re-run setup script to restore (container data preserved)
- DNS issues inside container will prevent Connector from connecting — test with `curl -s https://binaries.twingate.com` inside container

## Troubleshooting Commands
```bash
# Container status and logs
machinectl status twingate-connector
journalctl -M twingate-connector -xe --no-pager

# Test DNS/connectivity inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- curl -s https://binaries.twingate.com
```

## Related Docs
- [Twingate General Troubleshooting](https://www.twingate.com/docs/troubleshooting)
- Proxmox Setup Guide
- Home Assistant Setup Guide
- Unraid Setup Guide
- GitHub repository (uninstall script source)
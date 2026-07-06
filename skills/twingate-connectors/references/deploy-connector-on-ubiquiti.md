# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector on Ubiquiti Gateways (UDM Pro, UDM SE, UXG-Pro, UXG-Max) using a systemd-nspawn Debian container. The setup script installs the Connector inside the container and configures auto-start on boot. Container persists on `/data` partition across firmware upgrades.

## Key Information
- Uses `systemd-nspawn` container (not Docker)
- Container stored at `/data/custom/machines/` — survives firmware upgrades
- Symlinks at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may not survive upgrades (re-run setup script to restore)
- Initial bootstrap takes **5–10 minutes** (normal)
- Each Connector requires a **unique** token set — do not reuse tokens

## Prerequisites
- Ubiquiti Gateway running **UniFi OS 3.x or later**
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on the Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose Ubiquiti option → Step 2 → Generate Tokens
2. **Copy the bash command** (includes Network name, Access token, Refresh token)
3. **SSH into Gateway** and run the copied command
4. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show `connected`
5. **Optional**: Add Gateway's private IP as a Twingate Resource for remote UniFi dashboard access

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

**View logs:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- journalctl -u twingate-connector -n 50 --no-pager
```

**Uninstall:**
```bash
sudo ./uninstall.sh  # from GitHub repo
```

## Configuration Values
- Default container name: `twingate-connector` (customizable via `CONTAINER_NAME` during setup)
- Persistent data path: `/data/custom/machines/`

## Gotchas
- Tokens are **single-use per Connector** — generate new tokens if redeploying
- After firmware upgrade, symlinks/nspawn config may be lost; re-running setup script detects existing container and recreates them
- Custom `CONTAINER_NAME` must replace `twingate-connector` in all management commands
- DNS resolution inside container should be verified if Connector fails to connect (`curl -s https://binaries.twingate.com`)

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/twingate) (setup and uninstall scripts)
- Proxmox, Home Assistant, Unraid setup guides (linked in Admin Console)
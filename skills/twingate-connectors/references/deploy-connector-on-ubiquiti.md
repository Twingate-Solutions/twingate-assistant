---
source: https://www.twingate.com/docs/deploy-connector-on-ubiquiti
type: docs
fetched: 2026-08-14
source_version: fce91890559253b9941fa93ac52b9346f68095aa228cd029593fea534f6a221a
---

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware (UDM Pro, UDM SE, UXG-Pro, UXG-Max). The container persists on `/data` partition and survives firmware upgrades. Auto-starts on boot via systemd.

## Key Information
- Container stored at `/data/custom/machines/` (firmware-upgrade safe)
- Bootstrap (debootstrap) takes ~5-10 minutes on Gateway hardware
- Default container name: `twingate-connector`
- Each Connector requires its own unique token set — tokens cannot be reused
- Symlinks at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may not survive firmware upgrades; re-run setup script to recreate them

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x or later
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on the Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → select/add Connector → choose Ubiquiti → Step 2 → Generate Tokens
2. **Copy bash command** shown (contains Network name, Access token, Refresh token)
3. **SSH into Gateway** and run the copied command
4. **Verify**: Admin Console → Remote Networks → Connector → confirm Controller and Relay show `connected`
5. **Add Resource** (optional): Add Gateway's private IP (e.g., `192.168.x.x`) as a Twingate Resource for remote access to UniFi dashboard

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

**Uninstall:**
```bash
sudo ./uninstall.sh  # from GitHub repo
```

## Troubleshooting

**Container fails to start:**
```bash
machinectl status twingate-connector
journalctl -M twingate-connector -xe --no-pager
```

**Connector not connecting (check DNS/connectivity):**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- \
  curl -s https://binaries.twingate.com
```

**View Connector logs:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- \
  journalctl -u twingate-connector -n 50 --no-pager
```

## Gotchas
- Token errors require generating a **new** token set — existing tokens cannot be reused after failed deploy
- `/var/lib/machines/` symlink may need recreation after firmware upgrade; re-running setup script handles this automatically
- Custom `CONTAINER_NAME` during setup requires substituting that name in all `machinectl` commands

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/twingate) (setup and uninstall scripts)
- Proxmox, Home Assistant, and Unraid setup guides (linked in Admin Console)
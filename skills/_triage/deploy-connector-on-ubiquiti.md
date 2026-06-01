<!-- triage: unassigned URL: https://www.twingate.com/docs/deploy-connector-on-ubiquiti -->

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateways (UDM Pro, UDM SE, UXG-Pro, UXG-Max). The container persists on `/data` partition and survives firmware upgrades. Setup is automated via a community script from GitHub.

## Key Information
- Container stored at `/data/custom/machines/` — survives firmware upgrades
- Symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation after firmware upgrade (re-run setup script)
- Initial debootstrap takes 5–10 minutes on Gateway hardware
- Each Connector requires its own unique token set — do not reuse tokens
- Supports multiple Connectors on same Gateway via `CONTAINER_NAME` variable

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x or later
- SSH root access to Gateway
- Twingate account with Admin Console access
- Internet connectivity on Gateway

## Step-by-Step

**1. Generate tokens:**
- Admin Console → Remote Networks → select network → select/add Connector → Manual → Generate Tokens
- Copy Network name (subdomain), Access Token, Refresh Token

**2. Deploy:**
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-connector/main/setup.sh | \
  sudo TWINGATE_NETWORK="mycompany" \
       TWINGATE_ACCESS_TOKEN="<token>" \
       TWINGATE_REFRESH_TOKEN="<token>" \
  bash
```

**3. Verify:** Admin Console → Remote Networks → Connector → confirm Controller and Relay show `connected`

**4. Add Resource:** Admin Console → Resources → `+ Resource` → assign Gateway private IP → grant group access

## Configuration Values

| Variable | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Subdomain (e.g., `mycompany` from `mycompany.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Yes | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Yes | Generated from Admin Console |
| `CONTAINER_NAME` | No | Override default `twingate-connector` (for multiple connectors) |

## Container Management Commands
```bash
machinectl status twingate-connector
machinectl start twingate-connector
machinectl stop twingate-connector
machinectl disable twingate-connector

# Shell access
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Logs
journalctl -M twingate-connector -xe --no-pager

# Uninstall
sudo ./uninstall.sh  # from GitHub repo
```

## Gotchas
- Tokens are single-use per Connector — regenerate new tokens if redeploying
- After firmware upgrade, re-run setup script to recreate symlink and nspawn config (container data preserved)
- DNS verification inside container: `curl -s https://binaries.twingate.com`
- Connector logs: `journalctl -u twingate-connector -n 50 --no-pager` (run inside container via `nsenter`)

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/Twingate-Community/ubiquiti-connector)
- Proxmox, Home Assistant, Unraid setup guides (linked in Admin Console docs)
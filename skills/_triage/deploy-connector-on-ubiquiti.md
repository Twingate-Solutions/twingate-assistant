<!-- triage: unassigned URL: https://www.twingate.com/docs/deploy-connector-on-ubiquiti -->

# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware. The container is stored on `/data` partition, persisting through firmware upgrades. Setup is fully automated via a community-maintained shell script.

## Key Information
- Supported devices: UDM Pro, UDM SE, UXG-Pro, UXG-Max, and similar
- Requires UniFi OS 3.x or later
- Container setup (debootstrap) takes 5–10 minutes
- Multiple Connectors on same Gateway supported via `CONTAINER_NAME`
- Script source: `https://github.com/Twingate-Community/ubiquiti-connector`

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x+
- Root SSH access to Gateway
- Twingate Admin Console access
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

| Variable | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Subdomain only (e.g., `mycompany` from `mycompany.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Yes | Generated per-Connector in Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Yes | Generated per-Connector in Admin Console |
| `CONTAINER_NAME` | No | Default: `twingate-connector`; set to deploy multiple Connectors |

## Container Management Commands

```bash
machinectl status twingate-connector   # View status
machinectl stop twingate-connector     # Stop
machinectl start twingate-connector    # Start
machinectl disable twingate-connector  # Disable autostart

# Shell inside container
nsenter -t $(machinectl show twingate-connector -p Leader --value) \
  -m -u -i -n -p -- /bin/bash

# Logs
journalctl -M twingate-connector -xe --no-pager

# Uninstall
sudo ./uninstall.sh
```

## Gotchas
- **Tokens are single-use per Connector** — do not reuse; generate new set for each deployment or redeployment
- After firmware upgrade, symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation — re-run setup script to fix
- Container data persists at `/data/custom/machines/` across upgrades
- `TWINGATE_NETWORK` is the subdomain only, not the full URL

## Related Docs
- [Twingate Troubleshooting Docs](https://www.twingate.com/docs/troubleshooting)
- [GitHub Repository](https://github.com/Twingate-Community/ubiquiti-connector)
- Setting Up Resources (Admin Console)
- Proxmox, Home Assistant, Unraid setup guides
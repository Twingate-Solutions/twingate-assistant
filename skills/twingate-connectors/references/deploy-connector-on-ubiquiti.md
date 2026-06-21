# Deploy Twingate Connector on Ubiquiti Gateways

## Summary
Deploys a Twingate Connector inside a systemd-nspawn Debian container on Ubiquiti Gateway hardware (UDM Pro, UDM SE, UXG-Pro, UXG-Max). The container lives on `/data` partition, persisting through firmware upgrades. Setup is automated via a bash script from the Admin Console.

## Key Information
- Container uses `systemd-nspawn` (not Docker)
- Stored at `/data/custom/machines/` — survives firmware upgrades
- Symlink at `/var/lib/machines/` and nspawn config at `/etc/systemd/nspawn/` may need recreation after firmware upgrade (re-run setup script)
- Initial `debootstrap` takes **5–10 minutes** — expected behavior
- Each Connector requires its own unique token set (tokens are single-use per Connector)

## Prerequisites
- Ubiquiti Gateway running **UniFi OS 3.x or later**
- SSH root access to the Gateway
- Twingate account with Admin Console access
- Internet connectivity on the Gateway

## Step-by-Step

1. **Generate tokens**: Admin Console → Remote Networks → select network → add/select Connector → choose Ubiquiti option → Step 2 → Generate Tokens
2. **Copy bash command** (includes Network name, Access token, Refresh token)
3. **SSH into Gateway**, run the copied command
4. **Verify**: Admin Console → Remote Networks → select Connector → confirm Controller and Relay show `connected`
5. **Optional**: Add Gateway's private IP (`192.168.x.x`) as a Twingate Resource for remote UniFi dashboard access

## Container Management Commands

| Command | Description |
|---------|-------------|
| `machinectl status twingate-connector` | View status |
| `machinectl stop twingate-connector` | Stop container |
| `machinectl start twingate-connector` | Start container |
| `machinectl disable twingate-connector` | Disable auto-start |

**Shell access inside container:**
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
journalctl -M twingate-connector -xe --no-pager
```

**Connector not connecting — check DNS/connectivity:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- curl -s https://binaries.twingate.com
```

**Check Connector logs:**
```bash
nsenter -t $(machinectl show twingate-connector -p Leader --value) -m -u -i -n -p -- journalctl -u twingate-connector -n 50 --no-pager
```

## Gotchas
- Custom `CONTAINER_NAME` during setup: replace `twingate-connector` in all commands
- After firmware upgrade, re-run setup script to recreate symlink and nspawn config (container data preserved)
- Do not reuse token sets across Connectors — regenerate if redeploying

## Related Docs
- [Twingate General Troubleshooting](#)
- [Proxmox Setup Guide](https://www.twingate.com/docs/deploy-connector-on-proxmox)
- [Home Assistant Setup Guide](https://www.twingate.com/docs/deploy-connector-on-home-assistant)
- [GitHub Repository](https://github.com/twingate) (uninstall script, issue tracking)
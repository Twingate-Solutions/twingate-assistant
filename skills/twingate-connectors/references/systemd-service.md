# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connectors running as native Linux systemd services using package managers (apt/dnf). Includes manual upgrade steps and automation options via cron jobs to minimize user downtime.

## Key Information
- Check current version: `twingate-connector -V`
- Restart required after package upgrade via `systemctl restart twingate-connector`
- Two distro families supported: Debian/Ubuntu (apt) and Fedora/CentOS (dnf)

## Prerequisites
- Connector deployed as Linux systemd service
- `sudo` access
- Package manager configured with Twingate repository (see Linux systemd deployment docs)
- Deploy **2+ Connectors per Remote Network** to enable zero-downtime upgrades

## Step-by-Step

### Ubuntu/Debian (apt)
```bash
sudo apt update
sudo apt install -yq twingate-connector
sudo systemctl restart twingate-connector
```

### Fedora/CentOS (dnf)
```bash
sudo dnf update
sudo dnf --best install twingate-connector
sudo systemctl restart twingate-connector
```

### Simple Weekly Cron (Ubuntu)
```bash
sudo tee -a /etc/cron.weekly/update-twingate-connector > /dev/null <<EOF
#!/bin/bash
sudo -- sh -c 'apt update && apt install -yq twingate-connector && systemctl restart twingate-connector'
EOF
sudo chmod +x /etc/cron.weekly/update-twingate-connector
```

### Advanced: Stay One Version Behind (apt)
```bash
sudo sh -c '
curl -fsSL "https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/refs/heads/main/bash-scripts/keep-one-behind.sh" \
  -o /usr/local/sbin/keep-one-behind.sh &&
chmod +x /usr/local/sbin/keep-one-behind.sh &&
echo "0 2 * * 0 root /usr/local/sbin/keep-one-behind.sh twingate-connector --apply --allow-downgrades >> /var/log/keep-one-behind.log 2>&1" \
  > /etc/cron.d/twingate-connector-one-behind
'
```
- Runs every Sunday at 2 AM
- Logs to `/var/log/keep-one-behind.log`
- Script flags: `--apply` (execute changes), `--allow-downgrades` (permit version rollback)

## Configuration Values
| Item | Value |
|------|-------|
| Script install path | `/usr/local/sbin/keep-one-behind.sh` |
| Cron file path | `/etc/cron.d/twingate-connector-one-behind` |
| Log file | `/var/log/keep-one-behind.log` |
| Cron schedule (advanced) | `0 2 * * 0` (Sunday 2 AM) |

## Gotchas
- **Never update multiple Connectors in the same Remote Network simultaneously** — stagger schedules to prevent downtime
- Simple cron example is Ubuntu-only; adapt `apt` commands for other distros
- `keep-one-behind.sh` is designed for Ubuntu/Debian only
- Monitor `/var/log/keep-one-behind.log` and adjust maintenance windows as needed
- `--allow-downgrades` flag enables version rollback if latest is skipped

## Related Docs
- Linux systemd deployment guide
- Upgrading Connectors (best practices)
- Connector Release Notes
# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Instructions for upgrading Twingate Connector running as a Linux systemd service using package managers (apt/dnf). Covers manual upgrades, simple cron automation, and an advanced "stay one version behind" update strategy.

## Key Information
- Check current version: `twingate-connector -V`
- Restart required after package upgrade via `systemctl restart twingate-connector`
- Deploy 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules across Connectors in the same Remote Network

## Prerequisites
- Twingate Connector installed as a Linux systemd service
- `apt` (Ubuntu/Debian) or `dnf` (Fedora/CentOS)
- sudo access

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

### Advanced: Stay One Version Behind (Ubuntu/Debian)
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
- Installs second-latest version (not latest)
- Logs to `/var/log/keep-one-behind.log`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Script path | `/usr/local/sbin/keep-one-behind.sh` |
| Cron job path | `/etc/cron.d/twingate-connector-one-behind` |
| Log file | `/var/log/keep-one-behind.log` |
| Cron schedule | `0 2 * * 0` (Sundays 2 AM) |
| Script flags | `--apply`, `--allow-downgrades` |

## Gotchas
- Never update multiple Connectors in the same Remote Network simultaneously — causes user downtime
- Advanced script is Ubuntu/Debian only (APT-based)
- Monitor `/var/log/keep-one-behind.log` and adjust schedule to match maintenance windows
- `--allow-downgrades` flag required for the "one behind" script since it installs an older version than what may be cached

## Related Docs
- [Linux systemd deployment](https://www.twingate.com/docs/connector-linux-systemd)
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
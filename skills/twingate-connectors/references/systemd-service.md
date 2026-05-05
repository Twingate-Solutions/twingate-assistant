# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connectors running as native Linux systemd services using package managers. Includes manual upgrade steps for Ubuntu/Fedora/CentOS and automated update options via cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Restart required after package upgrade via `systemctl restart twingate-connector`
- Deploy 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules when multiple Connectors exist in the same Remote Network

## Prerequisites
- Twingate Connector installed as a systemd service on Linux
- Package manager access (apt or dnf)
- sudo privileges

## Step-by-Step

### Ubuntu (apt)
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
- Logs to `/var/log/keep-one-behind.log`
- Script location: `/usr/local/sbin/keep-one-behind.sh`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Script flags | `--apply`, `--allow-downgrades` |
| Cron schedule | `0 2 * * 0` (Sunday 2 AM) |
| Log file | `/var/log/keep-one-behind.log` |
| Script install path | `/usr/local/sbin/keep-one-behind.sh` |
| Cron job file | `/etc/cron.d/twingate-connector-one-behind` |

## Gotchas
- Never update multiple Connectors in the same Remote Network simultaneously — causes user downtime
- Advanced script is Ubuntu/Debian only; dnf-based distros need a different approach
- Monitor `/var/log/keep-one-behind.log` to verify automated updates are running correctly
- Schedule updates during off-peak hours

## Related Docs
- Linux systemd deployment documentation
- Upgrading Connectors (best practices)
- Connector Release Notes
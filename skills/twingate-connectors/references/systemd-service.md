# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Instructions for upgrading Twingate Connector running as a native Linux systemd service. Covers manual upgrades via package managers and automated update strategies using cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Supports Ubuntu/Debian (apt) and Fedora/CentOS (dnf)
- Always deploy 2+ Connectors per Remote Network to avoid downtime during upgrades

## Prerequisites
- Twingate Connector installed as a systemd service
- Package manager access (apt or dnf)
- sudo privileges

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
- Logs to `/var/log/keep-one-behind.log`
- Installs second-latest version (not latest)

## Configuration Values
| Item | Value |
|------|-------|
| Script install path | `/usr/local/sbin/keep-one-behind.sh` |
| Cron job path | `/etc/cron.d/twingate-connector-one-behind` |
| Log file | `/var/log/keep-one-behind.log` |
| Script flags | `--apply`, `--allow-downgrades` |

## Gotchas
- **Never update multiple Connectors in the same Remote Network simultaneously** — stagger schedules to prevent user downtime
- Schedule updates during off-peak hours
- The "one version behind" script supports dry-run (omit `--apply`) for testing before applying
- Monitor `/var/log/keep-one-behind.log` after deploying automated updates

## Related Docs
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Linux systemd deployment](https://www.twingate.com/docs/systemd-service)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Automated update template script](https://github.com/Twingate-Solutions/general-scripts/blob/main/bash-scripts/keep-one-behind.sh)
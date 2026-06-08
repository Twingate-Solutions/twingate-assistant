# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connector packages running as native Linux systemd services using `apt` (Ubuntu/Debian) or `dnf` (Fedora/CentOS). Includes manual upgrade steps and automation options via cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Restart via systemd after every upgrade
- Deploy 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules when multiple Connectors exist in same Remote Network

## Prerequisites
- Twingate Connector installed as systemd service
- `apt` or `dnf` package manager
- `sudo` access

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

### Advanced: Stay One Version Behind (runs Sundays at 2 AM)
```bash
sudo sh -c '
curl -fsSL "https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/refs/heads/main/bash-scripts/keep-one-behind.sh" \
  -o /usr/local/sbin/keep-one-behind.sh &&
chmod +x /usr/local/sbin/keep-one-behind.sh &&
echo "0 2 * * 0 root /usr/local/sbin/keep-one-behind.sh twingate-connector --apply --allow-downgrades >> /var/log/keep-one-behind.log 2>&1" \
  > /etc/cron.d/twingate-connector-one-behind
'
```

## Configuration Values
| Value | Detail |
|---|---|
| Script location | `/usr/local/sbin/keep-one-behind.sh` |
| Cron job file | `/etc/cron.d/twingate-connector-one-behind` |
| Log file | `/var/log/keep-one-behind.log` |
| Cron schedule | `0 2 * * 0` (Sundays 2 AM) |
| Script flags | `--apply`, `--allow-downgrades` |

## Gotchas
- Never update multiple Connectors in the same Remote Network simultaneously — causes user downtime
- The "one version behind" script supports downgrades; useful if latest version has issues
- Monitor `/var/log/keep-one-behind.log` after enabling advanced automation
- Adjust cron schedule to match actual maintenance windows

## Related Docs
- Upgrading Connectors (best practices)
- Linux systemd deployment
- Connector Release Notes
- [Automated update template script](https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/refs/heads/main/bash-scripts/keep-one-behind.sh)
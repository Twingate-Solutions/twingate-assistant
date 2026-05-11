# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Instructions for upgrading Twingate Connectors running as native Linux systemd services. Covers manual upgrades via package managers and automated update strategies using cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Supports Ubuntu/Debian (apt) and Fedora/CentOS (dnf)
- Always deploy 2+ Connectors per Remote Network to avoid downtime during upgrades

## Prerequisites
- Connector deployed as Linux systemd service
- Package manager access (apt or dnf)
- sudo privileges

## Step-by-Step

### Manual Upgrade — Ubuntu (apt)
```bash
sudo apt update
sudo apt install -yq twingate-connector
sudo systemctl restart twingate-connector
```

### Manual Upgrade — Fedora/CentOS (dnf)
```bash
sudo dnf update
sudo dnf --best install twingate-connector
sudo systemctl restart twingate-connector
```

### Simple Automated Update (Ubuntu, weekly cron)
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

| Flag | Description |
|------|-------------|
| `--apply` | Actually install the update (vs dry run) |
| `--allow-downgrades` | Permits version downgrades |
| First argument | Package name (e.g., `twingate-connector`) |

## Gotchas
- **Never update multiple Connectors in the same Remote Network simultaneously** — stagger schedules to prevent downtime
- Advanced script is Ubuntu/Debian only; not compatible with dnf-based systems
- Monitor `/var/log/keep-one-behind.log` and adjust cron schedule to match maintenance windows
- Simple weekly cron updates to latest; use advanced script if pinning to second-latest is required

## Related Docs
- [Linux systemd deployment](https://www.twingate.com/docs/systemd-service)
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Automated update template script](https://github.com/Twingate-Solutions/general-scripts/blob/main/bash-scripts/keep-one-behind.sh)
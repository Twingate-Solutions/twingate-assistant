# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Instructions for upgrading Twingate Connectors running as native Linux systemd services. Covers manual upgrades via package managers and automated update strategies using cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Supports Ubuntu/Debian (apt) and Fedora/CentOS (dnf)
- Always deploy 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules across Connectors in the same Remote Network

## Prerequisites
- Twingate Connector installed as systemd service
- Root/sudo access
- See [Linux systemd deployment docs](https://www.twingate.com/docs/linux-systemd) for initial setup

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

## Configuration Values

| Item | Value |
|------|-------|
| Script install path | `/usr/local/sbin/keep-one-behind.sh` |
| Cron job file | `/etc/cron.d/twingate-connector-one-behind` |
| Log file | `/var/log/keep-one-behind.log` |
| Default cron schedule | Sundays at 2 AM (`0 2 * * 0`) |
| Script flags | `--apply`, `--allow-downgrades` |

## Gotchas
- Restarting a Connector drops active sessions — always maintain 2+ Connectors per Remote Network
- Never update multiple Connectors in the same Remote Network simultaneously
- The `keep-one-behind.sh` script is Ubuntu/Debian only (apt-based)
- Monitor `/var/log/keep-one-behind.log` regularly when using automated updates
- Adjust cron schedules to match your maintenance windows and off-peak hours

## Related Docs
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Linux systemd deployment](https://www.twingate.com/docs/linux-systemd)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Automated update template script](https://github.com/Twingate-Solutions/general-scripts/blob/main/bash-scripts/keep-one-behind.sh)
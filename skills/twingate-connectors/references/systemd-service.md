# Upgrade Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connectors running as native Linux systemd services on Ubuntu/Fedora/CentOS. Includes manual upgrade commands and automated update patterns using cron jobs.

## Key Information
- Check current version: `twingate-connector -V`
- Restart required after package upgrade via `systemctl restart twingate-connector`
- Always run 2+ Connectors per Remote Network to avoid upgrade downtime
- Never update multiple Connectors in the same Remote Network simultaneously

## Prerequisites
- Twingate Connector installed as systemd service
- `sudo` access on host
- Package manager: `apt` (Ubuntu/Debian) or `dnf` (Fedora/CentOS)

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

## Advanced Script Flags
| Flag | Behavior |
|------|----------|
| `--apply` | Actually installs the target version (vs dry run) |
| `--allow-downgrades` | Permits installing older versions |

## Gotchas
- Stagger cron schedules when multiple Connectors exist in the same Remote Network — simultaneous updates cause downtime
- Advanced "one-behind" script is Ubuntu/Debian only (uses APT)
- Monitor `/var/log/keep-one-behind.log` and adjust cron schedule to match maintenance windows
- `systemctl restart` is required after package install; the package upgrade alone does not restart the service

## Related Docs
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Linux systemd deployment](https://www.twingate.com/docs/systemd-service)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Automated update template script](https://github.com/Twingate-Solutions/general-scripts/blob/main/bash-scripts/keep-one-behind.sh)
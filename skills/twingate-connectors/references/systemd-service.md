# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connector packages running as native Linux systemd services on Ubuntu/Fedora/CentOS. Includes manual upgrade commands, simple cron automation, and an advanced script to stay one version behind latest.

## Key Information
- Check current version: `twingate-connector -V`
- Always deploy 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules so multiple Connectors in the same Remote Network don't update simultaneously

## Prerequisites
- Twingate Connector installed as a systemd service
- Root/sudo access
- `apt` (Ubuntu/Debian) or `dnf` (Fedora/CentOS)

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
| Cron schedule | Every Sunday at 2 AM (`0 2 * * 0`) |
| Script flags | `--apply`, `--allow-downgrades` |

## Gotchas
- The advanced `keep-one-behind.sh` script is Ubuntu/Debian only (uses APT)
- Restarting the Connector service causes brief disconnection — always maintain 2+ Connectors per Remote Network
- Multiple Connectors in the same Remote Network updated simultaneously = user downtime
- Monitor `/var/log/keep-one-behind.log` to confirm updates are applying correctly
- Adjust cron schedule to match actual maintenance windows

## Related Docs
- [Upgrading Connectors (best practices)](https://www.twingate.com/docs/upgrading-connectors)
- [Linux systemd deployment](https://www.twingate.com/docs/systemd-service)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [keep-one-behind.sh script](https://github.com/Twingate-Solutions/general-scripts/blob/main/bash-scripts/keep-one-behind.sh)
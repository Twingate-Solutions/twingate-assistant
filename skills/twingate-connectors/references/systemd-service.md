# Upgrading Twingate Connectors on Linux (systemd)

## Summary
Covers upgrading Twingate Connectors running as native Linux systemd services on Ubuntu/Fedora/CentOS. Includes manual upgrade commands and automated update strategies using cron jobs to minimize user downtime.

## Key Information
- Check current version: `twingate-connector -V`
- Always run 2+ Connectors per Remote Network to avoid downtime during upgrades
- Stagger update schedules across Connectors in the same Remote Network

## Prerequisites
- Twingate Connector deployed as Linux systemd service
- `apt` (Ubuntu/Debian) or `dnf` (Fedora/CentOS) package manager
- sudo access

## Step-by-Step: Manual Upgrade

**Ubuntu (apt):**
```bash
sudo apt update
sudo apt install -yq twingate-connector
sudo systemctl restart twingate-connector
```

**Fedora/CentOS (dnf):**
```bash
sudo dnf update
sudo dnf --best install twingate-connector
sudo systemctl restart twingate-connector
```

## Automated Update Options

**Simple weekly cron (Ubuntu):**
```bash
sudo tee -a /etc/cron.weekly/update-twingate-connector > /dev/null <<EOF
#!/bin/bash
sudo -- sh -c 'apt update && apt install -yq twingate-connector && systemctl restart twingate-connector'
EOF
sudo chmod +x /etc/cron.weekly/update-twingate-connector
```

**Advanced "stay one version behind" script (Ubuntu/Debian):**
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
- Installs second-latest version (not bleeding edge)

**Script flags:**
| Flag | Behavior |
|------|----------|
| `--apply` | Actually install (without: dry run) |
| `--allow-downgrades` | Permits version downgrade if needed |

## Gotchas
- Do **not** update multiple Connectors in the same Remote Network simultaneously — stagger schedules
- The advanced script is Ubuntu/Debian only (uses APT)
- Monitor `/var/log/keep-one-behind.log` to confirm updates are applying correctly
- Adjust cron schedule to match your maintenance windows

## Related Docs
- [Upgrading Connectors best practices](https://www.twingate.com/docs/upgrading-connectors)
- [Linux systemd deployment](https://www.twingate.com/docs/systemd-service)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
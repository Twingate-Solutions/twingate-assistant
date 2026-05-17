# Twingate Linux Client

## Summary
Installs and configures the Twingate network client on Linux via CLI. Supports major distributions on x86/AMD64 and ARM64. No GUI; operated entirely through terminal commands.

## Key Information
- Requires `systemd` and `glibc`; also needs `systemd-resolved` or `NetworkManager` for DNS
- Headless/non-interactive mode available for servers and containers
- Two release channels: `twingate` (stable) and `twingate-latest` (early release); mutually exclusive
- APT packages are GPG-signed; RPM packages currently disable gpgcheck

## Prerequisites
- Supported distro (Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+, Arch, HP ThinPro, NixOS, Gentoo)
- `systemd-resolved` or `NetworkManager` running
- Notification service for interactive auth (or use console fallback)

## Installation

### Quick Install (any supported distro)
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
```

### Manual: APT (Ubuntu/Debian)
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
```

### Manual: RPM (Fedora/CentOS/Oracle)
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Initial interactive configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Show status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config setting |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostic ZIP |

## Configuration Values
- Settings via `sudo twingate config`: `network`, `autostart`, `save-auth-data`, `log-level`
- Log levels: `error`, `warn`, `info`, `debug`, `trace`

## Logging
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback log path (containers): /var/log/twingated.log
sudo twingate config log-level debug  # set for troubleshooting
```

## Gotchas
- **Do not use `sudo twingate start`** — running with elevated permissions hides desktop auth notifications from the logged-in user
- `twingate` and `twingate-latest` conflict; only one can be installed at a time
- Without a notification service, authenticate via `/usr/bin/twingate-notifier console` and paste the returned URL into a browser

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
# Twingate Linux Client

## Summary
Twingate Linux Client is a CLI-based VPN client supporting major Linux distributions on x86/AMD64 and ARM64. It requires systemd and glibc, operates as a systemd service, and supports both interactive desktop and headless/server modes.

## Key Information
- No graphical interface; CLI-only operation
- Runs as a systemd service
- Supports headless/non-interactive mode for servers and containers
- Two release channels: `twingate` (stable) and `twingate-latest` (early release, mutually exclusive)
- GPG signing available for apt-based systems

## Supported Distributions
**x86/AMD64 + ARM64:** Ubuntu (22.04, 24.04, 26.04 LTS), Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+  
**x86/AMD64 only:** Arch Linux, HP ThinPro, NixOS, Gentoo

## Prerequisites
- `systemd-resolved` enabled/running **OR** `NetworkManager` configured as DNS service
- `systemd` and `glibc` packages required
- Notification service for interactive auth (optional; console fallback available)

## Installation

```bash
# Quick install (all supported distros)
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash

# Configure after install
sudo twingate setup
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Initial configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List available resources |
| `sudo twingate config [setting] [value]` | Change config settings |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Headless auth via console URL |
| `sudo twingate report` | Export diagnostic ZIP |

## Configuration Values
Settings via `sudo twingate config [setting] [value]`:
- `network` — network/tenant setting
- `autostart` — enable autostart
- `save-auth-data` — persist auth data
- `log-level` — `error`, `warn`, `info`, `debug`, `trace`

## Logs
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback (containers without journalctl):
/var/log/twingated.log
# Set debug logging for support:
sudo twingate config log-level debug
sudo twingate report  # exports ZIP
```

## Manual Installation

**APT (Ubuntu/Debian):**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
```

**RPM (Fedora/CentOS):**
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
```

## Gotchas
- **Do NOT use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate` and `twingate-latest` conflict; only one can be installed at a time
- RHEL 10 works (upstream of Fedora 41) but is not officially tested

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
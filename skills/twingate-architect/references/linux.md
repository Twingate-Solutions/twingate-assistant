# Twingate Linux Client

## Summary
Installs and manages the Twingate Client on Linux via CLI. Supports major distributions using systemd and glibc. A headless/non-interactive mode is available for servers and containers.

## Key Information
- **Architectures**: x86/AMD64 and ARM64 (some distros x86/AMD64 only)
- **Supported distros**: Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+, Arch, HP ThinPro, NixOS, Gentoo (Arch/ThinPro/NixOS/Gentoo: x86/AMD64 only)
- Requires `systemd` and `glibc`
- DNS requires either `systemd-resolved` or `NetworkManager` running

## Prerequisites
- `systemd-resolved` or `NetworkManager` enabled
- Notification service for interactive auth (or use console fallback)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Step-by-Step: Quick Install
```bash
# 1. Install
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash

# 2. Configure
sudo twingate setup

# 3. Start (without sudo to receive desktop notifications)
twingate start
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Interactive configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config setting |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostic ZIP |

## Configuration Values
- `sudo twingate config network [value]`
- `sudo twingate config autostart [value]`
- `sudo twingate config save-auth-data [value]`
- `sudo twingate config log-level [error|warn|info|debug|trace]`

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

## Logs
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback log path (containers): /var/log/twingated.log
```
Set to `debug` when troubleshooting: `sudo twingate config log-level debug`

## Gotchas
- **Do NOT use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate-latest` (early release) conflicts with `twingate`; only one can be installed at a time
- In containers without `journalctl`, logs go to `/var/log/twingated.log`
- Console auth (`/usr/bin/twingate-notifier console`) returns a URL to paste in browser

## Related Docs
- [Headless/Non-interactive mode](#)
- [Manual installation instructions](#)
- [Advanced CLI commands](#
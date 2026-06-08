# Twingate Linux Client

## Summary
Installs and manages the Twingate client on Linux via CLI. Supports major distributions with systemd and glibc. Headless/non-interactive mode available for servers and containers.

## Key Information
- Supported (x86/AMD64 + ARM64): Ubuntu 22.04/24.04/26.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- Supported (x86/AMD64 only): Arch Linux, HP ThinPro, NixOS, Gentoo
- Requires `systemd` and `glibc`; DNS requires `systemd-resolved` OR `NetworkManager`
- Two release channels: `twingate` (stable) and `twingate-latest` (early release) — mutually exclusive

## Prerequisites
- `systemd-resolved` or `NetworkManager` enabled and running
- Notification service for interactive auth (console fallback available)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Installation

**One-liner (all supported distros):**
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
```

**APT (Ubuntu/Debian):**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
```

**RPM (Fedora/CentOS/Oracle):**
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Initial configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List available resources |
| `sudo twingate config [setting] [value]` | Change config setting |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostics ZIP |

## Configuration Values
- `sudo twingate config network <value>`
- `sudo twingate config autostart <value>`
- `sudo twingate config save-auth-data <value>`
- `sudo twingate config log-level [error|warn|info|debug|trace]`

## Logs
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback (containers): /var/log/twingated.log
```

## Gotchas
- **Do not use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate` and `twingate-latest` conflict; only one can be installed at a time
- For headless auth, copy URL from `/usr/bin/twingate-notifier console` output and open in browser
- Set log level to `debug` before contacting support

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
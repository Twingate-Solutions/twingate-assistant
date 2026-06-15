# Twingate Linux Client

## Summary
Installs and manages the Twingate Client on Linux via CLI. Supports major distributions with systemd and glibc dependencies. A headless/non-interactive mode is available for servers and containers.

## Key Information
- Supported (x86/AMD64 + ARM64): Ubuntu 22.04/24.04/26.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- Supported (x86/AMD64 only): Arch Linux, HP ThinPro, NixOS, Gentoo
- Requires `systemd` and `glibc`; upstream distros (e.g., RHEL 10) likely work but untested
- Two release channels: `twingate` (stable) and `twingate-latest` (early release); mutually exclusive

## Prerequisites
- `systemd-resolved` OR `NetworkManager` configured as DNS service
- Notification service for interactive auth (console fallback available)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Installation

**Quick install (all supported distros):**
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
| `twingate status` | Show status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config (e.g., `network`, `autostart`, `save-auth-data`, `log-level`) |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (no desktop) |
| `sudo twingate report` | Export diagnostic ZIP |

## Logging
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback log path (containers): /var/log/twingated.log
sudo twingate config log-level debug   # Set for troubleshooting
```
Log levels: `error`, `warn`, `info`, `debug`, `trace`

## Gotchas
- **Do not use `sudo twingate start`** — runs as root, hides desktop auth notifications from logged-in user
- `twingate` and `twingate-latest` packages conflict; only one can be installed
- GPG signing only applies to APT-based systems; RPM repos have GPG check disabled
- In containers without `journalctl`, logs fall back to `/var/log/twingated.log`

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
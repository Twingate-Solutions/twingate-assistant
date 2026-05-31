# Twingate Linux Client

## Summary
Installs and manages the Twingate network client on Linux via CLI. Supports major distributions using systemd and glibc. A headless/non-interactive mode is available for servers and containers.

## Key Information
- Supports x86/AMD64 and ARM64: Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- x86/AMD64 only: Arch Linux, HP ThinPro, NixOS, Gentoo
- Requires `systemd` and `glibc`; compatible with upstreams of supported distros (e.g., RHEL 10)
- Two release channels: `twingate` (stable) and `twingate-latest` (early release); mutually exclusive

## Prerequisites
- `systemd-resolved` enabled/running **or** `NetworkManager` configured and running
- Notification service required for interactive auth; fallback: console-based URL notification
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Step-by-Step

**Quick Install (all supported distros):**
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
twingate start  # Do NOT use sudo — breaks desktop notifications
```

**Manual APT (Ubuntu/Debian):**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
```

**Manual RPM (Fedora/CentOS):**
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Interactive configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List available resources |
| `sudo twingate config [setting] [value]` | Change config (e.g., `network`, `autostart`, `save-auth-data`, `log-level`) |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Headless auth via URL |
| `sudo twingate report` | Export diagnostic ZIP |

## Logging
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback log path (containers): /var/log/twingated.log
sudo twingate config log-level debug  # Set for troubleshooting
```
Log levels: `error`, `warn`, `info`, `debug`, `trace`

## Gotchas
- **Never run `sudo twingate start`** — hides desktop auth notifications from the logged-in user
- `twingate` and `twingate-latest` packages conflict; only one can be installed at a time
- Containers without `journalctl` use `/var/log/twingated.log` instead
- ARM64 not supported on Arch Linux, HP ThinPro, NixOS, Gentoo

## Related Docs
- [Headless/non-interactive mode](https://www.twingate.com/docs/linux-headless)
- [Manual installation instructions](https://www.twingate.com/docs/linux)
- [Advanced CLI commands](https://www.twingate.com/docs/linux)
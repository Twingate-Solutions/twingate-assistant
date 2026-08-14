---
source: https://www.twingate.com/docs/linux
type: docs
fetched: 2026-08-14
source_version: 28c8f794a7787b9897100a76d3138d015bf76db7847eeb1609c77fb4954c6ca7
---

# Twingate Linux Client

## Summary
Twingate Linux Client is a CLI-based network client supporting major Linux distributions on x86/AMD64 and ARM64. It runs as a systemd service and requires either systemd-resolved or NetworkManager for DNS. No graphical interface is provided.

## Key Information
- Supported architectures: x86/AMD64 and ARM64 (ARM64 excludes Arch, HP ThinPro, NixOS, Gentoo)
- Relies on `systemd` and `glibc` — other distros with these packages may work
- Headless/non-interactive mode available for servers/containers
- Two release channels: `twingate` (stable) and `twingate-latest` (early release, mutually exclusive)

## Prerequisites
- DNS: `systemd-resolved` enabled OR `NetworkManager` configured and running
- Notification service required for interactive auth (console fallback available via `/usr/bin/twingate-notifier console`)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Step-by-Step Installation

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
sudo twingate setup
```

**RPM (Fedora/CentOS/Oracle):**
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
sudo twingate setup
```

## CLI Commands

| Command | Description |
|---|---|
| `sudo twingate setup` | Interactive configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Show status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config setting |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostic ZIP |

**Config settings:** `network`, `autostart`, `save-auth-data`, `log-level`

## Configuration Values
- **Log levels:** `error`, `warn`, `info`, `debug`, `trace`
- **View log level:** `sudo twingate config log-level`
- **Set log level:** `sudo twingate config log-level debug`
- **Log file fallback** (no journalctl): `/var/log/twingated.log`
- **journalctl:** `sudo journalctl -u twingate --since "1 hour ago"`

## Gotchas
- **Do NOT use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user; use `twingate start` without elevated permissions
- `twingate` and `twingate-latest` conflict — only one can be installed at a time
- ARM64 does not support Arch Linux, HP ThinPro, NixOS, or Gentoo
- Set log level to `debug` before contacting support

## Related Docs
- Headless/non-interactive mode documentation
- Manual installation instructions
- Advanced CLI commands reference
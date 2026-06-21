# Twingate Linux Client

## Summary
Installs and runs the Twingate Client on Linux via CLI. Supports major distributions on x86/AMD64 and ARM64. No GUI; operated entirely via terminal commands.

## Key Information
- Requires `systemd` and `glibc`; distributions with these are most compatible
- DNS requires either `systemd-resolved` or `NetworkManager` enabled
- Headless/non-interactive mode available for servers/containers
- Two release channels: `twingate` (stable) and `twingate-latest` (early release, mutually exclusive)
- Logs via `journalctl` or `/var/log/twingated.log` (containers)

## Prerequisites
- Supported distro (Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+; x64-only: Arch, HP ThinPro, NixOS, Gentoo)
- `systemd-resolved` or `NetworkManager` running
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Installation

**Quick install (any supported distro):**
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
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
| `sudo twingate setup` | Initial configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Show status |
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

## Gotchas
- **Do not use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate` and `twingate-latest` packages conflict; only one can be installed
- If no notification service is available, use `/usr/bin/twingate-notifier console` and paste the returned URL into a browser
- Set log level to `debug` before contacting support

## Logging
```bash
sudo journalctl -u twingate --since "1 hour ago"
sudo twingate config log-level debug
sudo twingate report  # generates diagnostic ZIP
```

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
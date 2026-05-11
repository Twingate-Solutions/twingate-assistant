# Twingate Linux Client

## Summary
Twingate Linux Client is a CLI-based VPN client supporting major Linux distributions on x86/AMD64 and ARM64. It runs as a systemd service and requires configuration after installation. A headless/non-interactive mode is available for servers and containers.

## Key Information
- No graphical interface; operated entirely via CLI
- Runs as a systemd service
- GPG-signed packages for apt-based systems
- Two release channels: `twingate` (stable) and `twingate-latest` (early release, mutually exclusive)
- Fallback log path if journalctl unavailable: `/var/log/twingated.log`

## Prerequisites
- **DNS**: Either `systemd-resolved` or `NetworkManager` must be enabled
- **Notifications**: Desktop notification service required for interactive auth (console fallback available)
- **Architecture**: x86/AMD64 or ARM64 (some distros AMD64-only)
- **Dependencies**: `systemd` and `glibc`

## Supported Distributions
**x86/AMD64 + ARM64**: Ubuntu 22.04/24.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+  
**AMD64 only**: Arch Linux, HP ThinPro, NixOS, Gentoo

## Step-by-Step Installation

### Quick Install (All Distros)
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
```

### Manual: APT (Ubuntu/Debian)
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
sudo twingate setup
```

### Manual: RPM (Fedora/CentOS/Oracle)
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
| `sudo twingate setup` | Initial configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config setting |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostic ZIP |

## Configuration Values
- **Settings**: `network`, `autostart`, `save-auth-data`, `log-level`
- **Log levels**: `error`, `warn`, `info`, `debug`, `trace`
- View log level: `sudo twingate config log-level`
- Set log level: `sudo twingate config log-level debug`

## Logs
```bash
sudo journalctl -u twingate --since "1 hour ago"
```

## Gotchas
- **Do NOT use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate` and `twingate-latest` conflict; only one can be installed at a time
- Must run `twingate start` (without sudo) from a desktop terminal to receive auth notifications

## Related Docs
- Non-interactive/headless mode
- Manual installation instructions
- Advanced CLI commands
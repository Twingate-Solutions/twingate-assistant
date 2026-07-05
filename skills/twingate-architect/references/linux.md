# Twingate Linux Client

## Summary
Twingate Linux Client is a CLI-based VPN client supporting major Linux distributions on x86/AMD64 and ARM64. It runs as a systemd service and requires either systemd-resolved or NetworkManager for DNS. No graphical interface; operated entirely via terminal commands.

## Key Information
- Supported distros (x86/AMD64 + ARM64): Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- AMD64-only additions: Arch Linux, HP ThinPro, NixOS, Gentoo
- Requires `systemd` and `glibc`; RHEL 10 works (upstream of Fedora 41) but untested
- Headless/non-interactive mode available for servers/containers
- Early release channel via `twingate-latest` package (conflicts with `twingate`)

## Prerequisites
- `systemd-resolved` enabled/running **OR** `NetworkManager` configured and running
- Notification service required for interactive auth (console fallback available)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Step-by-Step Installation

**Quick install (any supported distro):**
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
```

**APT manual:**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
```

**RPM manual:**
```bash
dnf install -y 'dnf-command(config-manager)'
dnf config-manager addrepo --set=baseurl="https://packages.twingate.com/rpm/"
dnf config-manager setopt "packages.twingate.com_rpm_.gpgcheck=0"
dnf install -y twingate
```

## CLI Commands

| Command | Purpose |
|---|---|
| `sudo twingate setup` | Initial configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Check status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config (network, autostart, save-auth-data, log-level) |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Console-based auth (headless) |
| `sudo twingate report` | Export diagnostic ZIP |

## Configuration Values
- Log levels: `error`, `warn`, `info`, `debug`, `trace`
- Config settings: `network`, `autostart`, `save-auth-data`, `log-level`
- Logs path (fallback): `/var/log/twingated.log`
- Journal: `sudo journalctl -u twingate --since "1 hour ago"`

## Gotchas
- **Do NOT use `sudo twingate start`** — desktop auth notifications will be hidden from the logged-in user
- `twingate-latest` and `twingate` packages conflict; only one can be installed
- Without a notification service, manually copy auth URL from console output to browser
- `journalctl` may be unavailable in containers; use `/var/log/twingated.log`
- Set log level to `debug` before contacting support

## Related Docs
- Headless/non-interactive mode
- Manual installation instructions
- Advanced CLI commands
# Twingate Linux Client

## Summary
Installs and configures the Twingate network access client on Linux via CLI. Supports major distributions using systemd and glibc. A headless/non-interactive mode is available for server and container deployments.

## Key Information
- Supported x86/AMD64 and ARM64: Ubuntu 22.04/24.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- x86/AMD64 only: Arch Linux, HP ThinPro, NixOS, Gentoo
- No GUI — operated entirely via CLI
- APT packages are GPG-signed; RPM packages require disabling gpgcheck manually
- Early release channel available via `twingate-latest` package (conflicts with `twingate`)

## Prerequisites
- `systemd-resolved` or `NetworkManager` must be enabled/running for DNS
- Notification service required for interactive auth (fallback: console-based URL)
- `curl`, `gpg`, `ca-certificates` for manual APT install

## Step-by-Step

**Quick Install (any supported distro):**
```bash
curl -s https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup
twingate start   # NOTE: no sudo — required for desktop notifications
```

**Manual APT:**
```bash
curl -fsSL https://packages.twingate.com/apt/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/twingate-client-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/twingate-client-keyring.gpg] https://packages.twingate.com/apt/ * *" | sudo tee /etc/apt/sources.list.d/twingate.list
apt update -yq && apt install -yq twingate
sudo twingate setup
```

**Manual RPM:**
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
| `sudo twingate setup` | Initial interactive configuration |
| `twingate start` | Start client (no sudo) |
| `twingate stop` | Stop client |
| `twingate status` | Show status |
| `twingate resources` | List accessible resources |
| `sudo twingate config [setting] [value]` | Change config (e.g., `network`, `autostart`, `save-auth-data`, `log-level`) |
| `twingate desktop-start` | Start desktop notifications |
| `/usr/bin/twingate-notifier console` | Headless auth via browser URL |
| `sudo twingate report` | Export diagnostic ZIP for support |

## Logging
```bash
sudo journalctl -u twingate --since "1 hour ago"
# Fallback log path (containers): /var/log/twingated.log
sudo twingate config log-level debug   # recommended for troubleshooting
```
Log levels: `error`, `warn`, `info`, `debug`, `trace`

## Gotchas
- **Do not run `sudo twingate start`** — elevating privileges hides desktop auth notifications from the logged-in user
- RPM repos have GPG check disabled (`gpgcheck=0`) — no signing verification for RPM installs
- `twingate-latest` and `twingate` conflict; only one can be installed at a time
- Distributions without `systemd` or `glibc` are unlikely to work

## Related Docs
- [Headless/non-interactive mode](https://www.twingate.com/docs/headless-linux)
- [Manual installation instructions](https://www.twingate.com/docs/linux)
- [Advanced CLI commands](https://www.twingate.com/docs/linux)
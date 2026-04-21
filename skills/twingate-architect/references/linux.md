## Linux Client

Full reference for installing and operating the Twingate Linux Client in interactive mode. Supports major distros via install script or manual package management; headless mode available for server/container use.

**Key Information:**
- Requires `systemd-resolved` or `NetworkManager` as DNS service
- Interactive mode requires a notification service for authentication prompts
- Start with `twingate start` (NOT `sudo twingate start`) to receive desktop auth notifications
- Logs via `journalctl -u twingate`; fallback log file at `/var/log/twingated.log` (containers)
- Support log export: `sudo twingate report` (generates ZIP)
- Early release channel: `twingate-latest` package (may be less stable)

**Supported Distros (x86/AMD64 + ARM64):** Ubuntu 22.04/24.04 LTS, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
**AMD64 only:** Arch Linux, HP ThinPro, NixOS, Gentoo

**One-Line Install:**
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

**CLI Commands:**
- `sudo twingate setup` -- configure Client
- `twingate start` / `twingate stop` / `twingate status`
- `twingate resources` -- list accessible Resources
- `sudo twingate config log-level debug` -- set log level

**Gotchas:**
- Running `sudo twingate start` hides desktop auth notifications -- always use `twingate start` without sudo
- `twingate-latest` conflicts with `twingate`; only one release channel can be installed at a time

**Related Docs:**
- /docs/linux-headless -- Non-interactive headless/service mode
- /docs/linux-userspace-networking -- HTTP proxy mode (no root required)

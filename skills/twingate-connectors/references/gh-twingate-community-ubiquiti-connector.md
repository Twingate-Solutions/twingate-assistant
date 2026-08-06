---
source: https://github.com/Twingate-Community/ubiquiti-connector
type: github
fetched: 2026-08-06
source_version: 11cc1546a1db1a9a3976f3af888289f1a0a66d19
---

<!-- triage: unassigned -->

# Twingate Ubiquiti Connector

## Summary
Deploys a Twingate Connector on Ubiquiti gateway devices (UDM Pro, UDM SE, UXG-Pro, UXG-Max) using a systemd-nspawn Debian container. The container persists across firmware upgrades via a boot hook and the unifi-common service. A single setup script handles container creation, Connector installation, and boot persistence configuration.

## Key Information
- Container filesystem stored at `/data/custom/machines/` (survives firmware upgrades)
- Uses systemd-nspawn with host networking (no NAT)
- Boot hook at `/data/on_boot.d/` restores container after firmware wipes `/var/` and `/etc/`
- Debian Bookworm base; bootstrapping takes ~5–10 minutes on gateway hardware
- User namespaces disabled (`PrivateUsers=off`) for kernel compatibility
- Opt-in automatic updates via unattended-upgrades inside the container
- Retrofit mode available for containers deployed with older script versions

## Prerequisites
- Ubiquiti Gateway running UniFi OS 3.x or later
- Root SSH access to the gateway
- Twingate account with a Connector created in the Admin Console (Network → Connectors → Deploy Connector → Manual → Generate New Tokens)
- Internet connectivity on the gateway

## Usage

**Interactive:**
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-gateway-connector/main/setup.sh | sudo bash
```

**Non-interactive:**
```bash
curl -sSf ... | sudo TWINGATE_NETWORK="mycompany" TWINGATE_ACCESS_TOKEN="..." TWINGATE_REFRESH_TOKEN="..." bash
```

**Manual update:**
```bash
curl -sSf .../update.sh | sudo bash
```

**Uninstall:**
```bash
curl -sSf .../uninstall.sh | sudo bash
```

## Configuration Values

| Variable | Required | Default | Description |
|---|---|---|---|
| `TWINGATE_NETWORK` | Yes (non-interactive) | — | Network subdomain (e.g., `mycompany`) |
| `TWINGATE_ACCESS_TOKEN` | Yes (non-interactive) | — | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Yes (non-interactive) | — | Connector refresh token |
| `CONTAINER_NAME` | No | `twingate-connector` | Name for the nspawn container |
| `AUTO_UPDATE` | No | `0` | Set to `1` to enable unattended-upgrades |

## Key Paths

| Path | Description |
|---|---|
| `/data/custom/machines/<name>` | Container root filesystem |
| `/data/custom/nspawn/<name>.nspawn` | Persistent nspawn config |
| `/data/custom/dpkg/` | Cached host packages for offline recovery |
| `/data/on_boot.d/05-nspawn-<name>.sh` | Boot hook script |
| `/data/custom/twingate/boot.log` | Boot hook log (rotated at 1MB) |

## Gotchas
- Container runs with **all capabilities** and host networking — required for Connector functionality but elevated privilege level
- Default container root password is `twingate`; change if needed via `machinectl shell`
- Firmware updates wipe `/var/` and `/etc/`; boot persistence depends on unifi-common being installed and the boot hook being present
- `debootstrap` step is slow (~10 min); this is expected on gateway hardware
- Uninstall does **not** remove the unifi-common boot service (other tools may depend on it)

## Related Docs
- [Twingate Connector Documentation](https://docs.twingate.com/)
- [unifi-common](https://github.com/unifi-utilities/unifi-common)
- [Twingate Community (Reddit)](https://www.reddit.com/r/twingate/)
- [Issue Tracker](https://github.com/Twingate-Community/ubiquiti-gateway-connector/issues)
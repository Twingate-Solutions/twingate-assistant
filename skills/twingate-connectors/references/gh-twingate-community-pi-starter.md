---
source: https://github.com/Twingate-Community/pi-starter
type: github
fetched: 2026-08-06
source_version: 214cadc4073ea679df13c1b180b0486bb619b867
---

<!-- triage: unassigned -->

# Twingate-Community/pi-starter

## Summary
Raspberry Pi image builder that produces ready-to-deploy Twingate Connector images. On first boot, the image auto-provisions a Connector via the Twingate API using credentials supplied in a config file on the boot partition. Includes optional auto-updates scoped to Twingate packages only.

## Key Information
- Base OS: Raspberry Pi OS 64-bit (Full or Lite)
- Provisioning runs once at first boot via a systemd service (`twingate-firstboot`)
- API key is removed from the config file after successful provisioning
- CI/CD workflow checks daily for new Connector and Raspberry Pi OS versions and auto-releases updated images
- Connector tokens stored at `/etc/twingate/connector.conf` with 600 permissions

## Prerequisites
- Twingate account with Admin Console access
- API token with `Read, Write, Provision` permissions
- Remote Network ID from the Admin Console
- For building locally: Docker with 8 GB+ free disk space, or a Linux system with `sudo`

## Usage / Step-by-Step
1. Download the latest image from GitHub Releases (or build it yourself)
2. Flash to SD card using Raspberry Pi Imager, Balena Etcher, or `dd`
3. Mount the boot partition; rename `twingate-config.txt.example` to `twingate-config.txt` and populate required values
4. Insert SD card, connect ethernet and power; wait up to ~10 minutes for provisioning to complete
5. Verify the Connector appears in the Twingate Admin Console
6. SSH in and change the default password immediately

**Build from source (Docker):**
```bash
git clone https://github.com/Twingate-Community/pi-starter.git
cd pi-starter
bash scripts/build-with-docker.sh
```

## Configuration Values (`twingate-config.txt`)

| Key | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Twingate network subdomain (e.g., `yourcompany`) |
| `TWINGATE_API_KEY` | Yes | API token with Read/Write/Provision permissions |
| `TWINGATE_REMOTE_NETWORK_ID` | Yes | ID from the Remote Network URL in Admin Console |
| `CONNECTOR_NAME` | No | Defaults to `twingate-pi-<hostname>` if blank |
| `AUTO_UPDATE_ENABLED` | No | `true` (default) or `false` |
| `AUTO_UPDATE_TIME` | No | 24-hour time, default `03:00` |

## Gotchas
- **Default credentials are `pi` / `raspberry` with SSH enabled** — change immediately after first boot
- API key is deleted from the boot partition after provisioning; store it securely before flashing
- The boot partition is readable without root access; do not leave the API key in the config file after setup
- To re-provision, delete `/etc/twingate/.provisioned` and reboot
- Provisioning log is at `/boot/firmware/twingate-provision.log` — check here first if the Connector does not appear within 10 minutes

## Troubleshooting Commands
```bash
cat /boot/firmware/twingate-provision.log
sudo systemctl status twingate-firstboot
sudo journalctl -u twingate-connector -f
```

## Related Docs
- [Twingate Connector Documentation](https://www.twingate.com/docs/connectors)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Linux Connector Deployment](https://www.twingate.com/docs/connectors-on-linux)
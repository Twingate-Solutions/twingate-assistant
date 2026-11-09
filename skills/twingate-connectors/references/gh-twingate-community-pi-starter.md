---
source: https://github.com/Twingate-Community/pi-starter
type: github
fetched: 2026-11-08
source_version: 27216ee7649b16dfea44ed02f301c1e25dc8db91
trust: community
---

# Twingate Connector for Raspberry Pi (`pi-starter`)

Automated Raspberry Pi image builder that creates ready-to-deploy Twingate Connectors. On first boot, the Pi self-provisions a Connector via the Twingate API, starts the Connector service, and optionally configures unattended auto-updates.

## Key Information

- Base: Raspberry Pi OS 64-bit (Full or Lite)
- Provisioning runs as a systemd first-boot service (`twingate-firstboot`)
- API key is removed from the config file after provisioning completes
- Connector tokens stored at `/etc/twingate/connector.conf` (permissions: 600)
- Auto-updates target only Twingate packages; no reboot required
- CI/CD workflow checks daily for new Connector or OS versions and auto-publishes releases

## Prerequisites

- Raspberry Pi with ethernet connection
- Twingate API key with **Read, Write, Provision** permissions
- Remote Network ID from the Twingate Admin Console
- For building: Docker + 8 GB free disk space (or a Linux host with `sudo`)

## Usage / Step-by-Step

1. Download the latest image from the repository's Releases page.
2. Flash to SD card using Raspberry Pi Imager, Balena Etcher, or `dd`.
3. Mount the boot partition; rename `twingate-config.txt.example` to `twingate-config.txt` and populate required fields.
4. Insert SD card, connect ethernet and power. Wait up to 10 minutes for provisioning.
5. Verify the Connector appears in the Twingate Admin Console.
6. SSH in and change the default password immediately: `passwd`

**Build your own image (Docker):**
Clone the repo, then run `bash scripts/build-with-docker.sh` from the repo root.

**Re-provision if needed:**
```bash
sudo rm /etc/twingate/.provisioned && sudo reboot
```

## Configuration Values (`twingate-config.txt`)

| Key | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Network subdomain (e.g., `yourcompany`) |
| `TWINGATE_API_KEY` | Yes | Admin Console API token |
| `TWINGATE_REMOTE_NETWORK_ID` | Yes | Remote Network ID from Console URL |
| `CONNECTOR_NAME` | No | Defaults to `twingate-pi-<hostname>` |
| `AUTO_UPDATE_ENABLED` | No | `true` (default) or `false` |
| `AUTO_UPDATE_TIME` | No | 24-hour time, default `03:00` |

**Default SSH credentials:** `pi` / `raspberry` — change immediately after first login.

## Gotchas

- The API key is removed from the boot partition after first provisioning; save it elsewhere before booting.
- The boot partition is readable without root access — do not leave a valid API key in `twingate-config.txt` after setup.
- SSH is enabled by default; disable it by deleting the `ssh` file from the boot partition before first boot if not needed.
- Provisioning log is at `/boot/firmware/twingate-provision.log`; check here first if the Connector does not appear in the Admin Console.

## Related Docs

- [Twingate Connector Documentation](https://www.twingate.com/docs/connectors)
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Linux Connector Deployment](https://www.twingate.com/docs/connectors-on-linux)
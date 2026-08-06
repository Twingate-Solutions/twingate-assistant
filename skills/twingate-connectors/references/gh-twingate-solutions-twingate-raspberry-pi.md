---
source: https://github.com/Twingate-Solutions/twingate-raspberry-pi
type: github
fetched: 2026-08-06
source_version: bd4822effca83354875145deb4bf7fdedddaa406
---

<!-- triage: unassigned -->

# twingate-raspberry-pi

## Summary
A utility repository providing scripts and tooling to install and run the Twingate client on Raspberry Pi devices. It targets the constraints of ARM-based Raspberry Pi hardware running Raspberry Pi OS (Debian-based).

## Key Information
- Maintained by Twingate-Solutions (official Twingate GitHub org)
- Targets Raspberry Pi hardware (ARM architecture)
- Raspberry Pi OS (Debian/apt-based) assumed
- Minimal README — implementation details live in scripts/files within the repo

## Prerequisites
- Raspberry Pi device (ARM32/ARM64)
- Raspberry Pi OS or compatible Debian-based OS
- Active Twingate account with a network configured
- A valid Twingate service key or user authentication token
- `curl` or `wget` available on the device

## Usage / Step-by-Step
1. Clone or download the repository to the Raspberry Pi:
   ```bash
   git clone https://github.com/Twingate-Solutions/twingate-raspberry-pi.git
   ```
2. Review available scripts in the repo for install/setup steps.
3. Run the relevant installation script (typically requires `sudo`):
   ```bash
   sudo bash <install-script>.sh
   ```
4. Provide your Twingate network name and service key when prompted or via environment variables.
5. Verify the Twingate client service is running:
   ```bash
   sudo systemctl status twingate
   ```

## Configuration Values
| Parameter | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name (e.g., `mycompany`) |
| `TWINGATE_SERVICE_KEY` | Service account key from the Twingate Admin Console |

*Exact variable names may differ — check individual scripts for accepted inputs.*

## Gotchas
- Standard Twingate Linux packages may not support ARM32; these scripts likely address architecture compatibility specifically for Pi
- Requires `sudo`/root access for installation and service management
- The README is sparse — inspect scripts directly before running
- Service key authentication is for headless/automated use; interactive user auth behaves differently
- Raspberry Pi OS versions (Buster vs. Bullseye vs. Bookworm) may affect package availability

## Related Docs
- [Twingate Linux Client Docs](https://www.twingate.com/docs/linux)
- [Twingate Service Accounts](https://www.twingate.com/docs/services)
- [Twingate Admin Console](https://auth.twingate.com/)
- [Main Twingate-Solutions GitHub Org](https://github.com/Twingate-Solutions)
---
source: https://help.twingate.com/articles/8503680533-linux-client-unable-to-authenticate-on-ubuntu-24-04
type: help
fetched: 2026-08-06
source_version: 0259e503e15f339b6a5126a1ce9a8b3a856b652c233bc9575e3a7c67191d0cc8
---

# [Linux Client] Unable to Authenticate on Ubuntu 24.04

## Summary
Twingate Linux Client fails to authenticate on Ubuntu 24.04 due to NetworkManager failing D-Bus network deletion calls, preventing network path creation. This manifests as `auth.sock` errors in the notifier logs and blocks all Resource connections. Occurs primarily after upgrades to 24.04, but also on fresh installs and after sleep/wake network changes.

## Key Information
- **Error symptom**: `twingate-notifier status` shows `[ERROR] Error: auth.sock socket is not found`
- **Root cause**: NetworkManager fails D-Bus network deletion calls → cannot create network path for Client
- **Trigger scenarios**: Ubuntu upgrade to 24.04, fresh installs (rare), sleep on network1 / wake on network2
- **Fix**: Switch netplan renderer from `NetworkManager` to `networkd`

## Prerequisites
- Ubuntu 24.04
- Twingate Linux Client installed
- `sudo` access

## Step-by-Step Fix

1. Navigate to netplan config directory:
   ```bash
   ls /etc/netplan
   ```

2. Edit the appropriate file (or create `01-network-manager-all.yaml` if neither exists):
   - `01-network-manager-all.yaml` → `sudo nano /etc/netplan/01-network-manager-all.yaml`
   - `50-cloud-init.yaml` → `sudo nano /etc/netplan/50-cloud-init.yaml`

3. Set contents to:
   ```yaml
   network:
     version: 2
     # renderer: NetworkManager
     renderer: networkd
   ```

4. Apply the change:
   ```bash
   sudo netplan apply
   ```
   *(Warnings from this command are safe to ignore)*

5. If auth prompt doesn't appear automatically:
   ```bash
   twingate stop && twingate start
   ```

6. If still no auth prompt, reboot and verify changes persisted.

## Configuration Values
| File | Location |
|------|----------|
| Primary config | `/etc/netplan/01-network-manager-all.yaml` |
| Cloud-init config | `/etc/netplan/50-cloud-init.yaml` |

| Setting | Old Value | New Value |
|---------|-----------|-----------|
| `renderer` | `NetworkManager` | `networkd` |

## Gotchas
- `sudo netplan apply` may produce warnings — these are non-fatal and can be ignored
- Sleep/wake cycle on different networks can re-trigger the issue even after initial setup
- Fresh Ubuntu 24.04 installs are affected, not only upgrades
- If no netplan file exists, you must **create** `01-network-manager-all.yaml` manually

## Related Docs
- Twingate Linux Client documentation
- Ubuntu Netplan documentation: `man netplan`
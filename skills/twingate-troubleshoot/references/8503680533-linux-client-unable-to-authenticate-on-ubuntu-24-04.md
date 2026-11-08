---
source: https://help.twingate.com/articles/8503680533-linux-client-unable-to-authenticate-on-ubuntu-24-04
type: help
fetched: 2026-11-08
source_version: 250c0a601ba1c8fd1f7e7d2cf81135e5b32f55fcce218a1eec9f8aa3f6a503a1
trust: official
---

# [Linux Client] Unable to Authenticate on Ubuntu 24.04

## Summary
Twingate Linux Client fails to authenticate on Ubuntu 24.04 due to NetworkManager failing to create a network path via D-Bus, causing `auth.sock` errors in the notifier service. This occurs most commonly after upgrading from older Ubuntu versions, but also on fresh installs and during sleep/wake network transitions.

## Key Information
- **Symptom**: `twingate-notifier status` shows `[ERROR] Error: auth.sock socket is not found`
- **Root cause**: NetworkManager fails D-Bus network deletion calls, blocking Client network path creation
- **Trigger scenarios**: Ubuntu upgrade to 24.04, fresh installs (rare), sleep on network1 / wake on network2
- **Fix**: Switch netplan renderer from `NetworkManager` to `networkd`

## Prerequisites
- Ubuntu 24.04
- Twingate Linux Client installed
- `sudo` access

## Step-by-Step

1. **Identify your netplan config file:**
   ```bash
   ls /etc/netplan
   ```

2. **Edit the appropriate file** (`01-network-manager-all.yaml` or `50-cloud-init.yaml`):
   ```bash
   sudo nano /etc/netplan/<filename>.yaml
   ```

3. **Update the renderer** in the file:
   ```yaml
   network:
     version: 2
     # renderer: NetworkManager
     renderer: networkd
   ```

4. **If neither file exists**, create `/etc/netplan/01-network-manager-all.yaml` with the above contents.

5. **Apply the change:**
   ```bash
   sudo netplan apply
   ```
   *(Warnings from this command are safe to ignore.)*

6. **If auth prompt does not appear automatically:**
   ```bash
   twingate stop
   twingate start
   ```

7. **If still no auth prompt**: reboot and verify the netplan change persisted.

## Configuration Values

| File | Key | Old Value | New Value |
|------|-----|-----------|-----------|
| `/etc/netplan/*.yaml` | `renderer` | `NetworkManager` | `networkd` |

## Gotchas
- This issue affects both upgraded and (rarely) fresh Ubuntu 24.04 installs — don't assume it only applies to upgrades
- Sleep/wake cycles across different networks can re-trigger the error even after initial setup
- `sudo netplan apply` may emit warnings; these are non-fatal and can be ignored
- Must restart Twingate client (`twingate stop && twingate start`) if the browser auth prompt doesn't appear automatically after applying netplan changes

## Related Docs
- Twingate Linux Client documentation
- Ubuntu Netplan documentation: https://netplan.io/
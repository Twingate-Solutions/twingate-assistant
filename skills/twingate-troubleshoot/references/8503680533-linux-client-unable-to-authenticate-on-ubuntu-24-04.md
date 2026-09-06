---
source: https://help.twingate.com/articles/8503680533-linux-client-unable-to-authenticate-on-ubuntu-24-04
type: help
fetched: 2026-09-06
source_version: d8483270dfc3ee26550aaa754d5658106c3c623a981c9a05431fe2299a73963b
---

# [Linux Client] Unable to Authenticate on Ubuntu 24.04

## Summary
Twingate Linux Client fails to authenticate on Ubuntu 24.04 due to NetworkManager failing D-Bus network deletion calls, which prevents network path creation for the client. This surfaces as `auth.sock` errors in the notifier logs and occurs primarily after upgrading to Ubuntu 24.04, but also on fresh installs and during sleep/wake network changes.

## Key Information
- **Symptom**: `twingate-notifier status` shows `[ERROR] Error: auth.sock socket is not found`
- **Root cause**: NetworkManager fails D-Bus network deletions → cannot create network path for Twingate client
- **Fix**: Switch netplan renderer from `NetworkManager` to `networkd`
- **Triggers**: Ubuntu upgrade to 24.04, fresh installs (rare), sleep/wake cycle across different networks

## Prerequisites
- Ubuntu 24.04
- Twingate Linux Client installed
- `sudo` access

## Step-by-Step Fix

1. Navigate to `/etc/netplan` and list files: `ls /etc/netplan`

2. **Edit the appropriate file** (or create `01-network-manager-all.yaml` if neither exists):
   - `01-network-manager-all.yaml`, OR
   - `50-cloud-init.yaml`

3. Set file contents:
   ```yaml
   network:
     version: 2
     # renderer: NetworkManager
     renderer: networkd
   ```

4. Apply the netplan change:
   ```bash
   sudo netplan apply
   ```
   *(Warnings from this command are safe to ignore)*

5. If browser auth prompt does not appear automatically:
   ```bash
   twingate stop && twingate start
   ```

6. If still no auth prompt — reboot and verify changes persisted.

## Configuration Values

| Setting | Old Value | New Value |
|---|---|---|
| `renderer` (netplan) | `NetworkManager` | `networkd` |

**Affected files:**
- `/etc/netplan/01-network-manager-all.yaml`
- `/etc/netplan/50-cloud-init.yaml`

## Gotchas
- `sudo netplan apply` may produce warnings — these are **safe to ignore**
- The issue recurs on sleep/wake if switching networks — workaround must be applied persistently
- Fresh Ubuntu 24.04 installs can also exhibit this issue, not only upgrades
- If neither netplan file exists, manually create `01-network-manager-all.yaml`

## Related Docs
- Twingate Linux Client documentation
- Ubuntu netplan renderer configuration
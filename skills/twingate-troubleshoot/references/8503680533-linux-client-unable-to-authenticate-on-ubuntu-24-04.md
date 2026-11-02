---
source: https://help.twingate.com/articles/8503680533-linux-client-unable-to-authenticate-on-ubuntu-24-04
type: help
fetched: 2026-11-01
source_version: 7937c48e83d6e8a0c2ead5e6e7262891d83bbde6aa50b868bf6d78be86eb49a7
trust: official
---

# [Linux Client] Unable to Authenticate on Ubuntu 24.04

## Summary
Twingate Linux Client fails to authenticate on Ubuntu 24.04 due to NetworkManager failing D-Bus network deletion calls, preventing network path creation for the Client. This manifests as `auth.sock` errors in the notifier logs and blocks all Resource connections. Occurs primarily after upgrades to 24.04, but also on fresh installs and after sleep/wake network changes.

## Key Information
- **Error symptom**: `twingate-notifier status` shows `[ERROR] Error: auth.sock socket is not found`
- **Root cause**: NetworkManager fails D-Bus network deletion calls → cannot create network path for Client
- **Trigger scenarios**: Upgrade to Ubuntu 24.04, fresh installs (rare), sleep on network A / wake on network B
- **Fix**: Switch netplan renderer from `NetworkManager` to `networkd`

## Prerequisites
- Ubuntu 24.04
- Twingate Linux Client installed
- `sudo` access

## Step-by-Step Fix

1. **Check existing netplan config:**
   ```bash
   ls /etc/netplan
   ```

2. **Edit the appropriate file** (use whichever exists):

   - `/etc/netplan/01-network-manager-all.yaml`, **or**
   - `/etc/netplan/50-cloud-init.yaml`

   If neither exists, create `/etc/netplan/01-network-manager-all.yaml`.

3. **Set file contents:**
   ```yaml
   network:
     version: 2
     # renderer: NetworkManager
     renderer: networkd
   ```

4. **Apply the change:**
   ```bash
   sudo netplan apply
   ```
   *(Warnings from this command are safe to ignore.)*

5. **If auth prompt does not appear automatically:**
   ```bash
   twingate stop && twingate start
   ```

6. **If still no prompt:** Reboot and verify the netplan change persisted.

## Configuration Values

| Setting | Old Value | New Value |
|---|---|---|
| `renderer` (in netplan YAML) | `NetworkManager` | `networkd` |

## Gotchas
- `sudo netplan apply` may emit warnings — these are expected and non-fatal in this context
- Sleep/wake network transitions can re-trigger the issue even on otherwise working systems; the renderer switch resolves this too
- Fresh Ubuntu 24.04 installs can exhibit this issue, not only upgrade scenarios

## Related Docs
- `twingate-notifier status` — primary diagnostic command for auth errors
- Netplan documentation: `/etc/netplan/` configuration reference
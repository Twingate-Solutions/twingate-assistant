---
source: https://help.twingate.com/articles/8503680533-linux-client-unable-to-authenticate-on-ubuntu-24-04
type: help
fetched: 2026-10-04
source_version: 13d3cd6bcaf740936b4e8b3ac671bce58fa59f78b8807b8f5180cc998bacb6ce
trust: official
---

# [Linux Client] Unable to Authenticate on Ubuntu 24.04

## Summary
Twingate Linux Client fails to authenticate on Ubuntu 24.04 due to NetworkManager failing D-Bus network deletion calls, blocking network path creation for the client. This manifests as `auth.sock` errors in notifier logs and affects upgrades, fresh installs, and sleep/wake network transitions.

## Key Information
- **Affected component:** Twingate Linux Client (notifier service)
- **Platform:** Linux / Ubuntu 24.04
- **Primary trigger:** Upgrade from older Ubuntu versions; also seen on fresh installs and sleep/wake across different networks
- **Root cause:** NetworkManager fails D-Bus calls → cannot create network path → notifier reports `auth.sock` failures

## Error Signature
```
twingate-notifier status
17:43:07 [ERROR] Error: auth.sock socket is not found
```

## Fix: Switch Netplan Renderer from NetworkManager to networkd

### Step-by-Step

1. Check which netplan config file exists:
   ```bash
   ls /etc/netplan
   ```

2. Edit the existing file (`01-network-manager-all.yaml` **or** `50-cloud-init.yaml`), or create `01-network-manager-all.yaml` if neither exists:
   ```bash
   sudo nano /etc/netplan/<filename>.yaml
   ```

3. Update file contents:
   ```yaml
   network:
     version: 2
     # renderer: NetworkManager
     renderer: networkd
   ```

4. Apply the changes:
   ```bash
   sudo netplan apply
   ```
   *(Warnings from this command are safe to ignore.)*

5. If auth prompt does not appear automatically:
   ```bash
   twingate stop && twingate start
   ```

6. If still no auth prompt, **reboot** and verify changes persisted.

## Configuration Values
| File path | Key setting |
|---|---|
| `/etc/netplan/01-network-manager-all.yaml` | `renderer: networkd` |
| `/etc/netplan/50-cloud-init.yaml` | `renderer: networkd` |

## Gotchas
- This is a **workaround**, not an upstream fix — switching renderers may affect other NetworkManager-dependent tooling on the system
- Sleep/wake cycle across different networks can re-trigger the issue even after initial setup
- `sudo netplan apply` may emit warnings; these do not indicate failure
- If neither standard netplan file exists, you must **create** `01-network-manager-all.yaml` manually

## Prerequisites
- Ubuntu 24.04 with Twingate Linux Client installed
- `sudo` access to edit netplan configuration

## Related Docs
- Twingate Linux Client documentation
- Ubuntu netplan documentation: `man netplan`
---
source: https://help.twingate.com/articles/4908519978-connector-offline-gone-code-410-in-logs
type: help
fetched: 2026-08-06
source_version: ff80c22519b1ed87b70d38d5086b5ec003916c5ea01ed2d481e40ae2e1b905e3
---

# Connector Offline—"Gone, code 410" in Logs

## Summary
A Connector shows as "Offline" when launched with expired or deleted tokens, generating a 410 error. This commonly occurs after incomplete or unsuccessful update attempts. Resolution requires purging the Connector service and re-deploying with fresh tokens.

## Key Information
- Error code 410 ("Gone") indicates the Connector's authentication tokens are expired or deleted server-side
- Connector state will show as `Error` in logs, not a network issue
- The error is unrecoverable without re-provisioning—the Connector cannot self-heal

## Symptoms
- Connector status: Offline in Admin Console
- Log indicators:
  - `Authentication [INFO] [libsdwan] sdwan_state: Offline User`
  - `Gone, code 410`
  - `[INFO] [connector] State: Error`
  - `[DEBUG] [libsdwan] [controller] run_state_machine: Pre-unrecoverable error`
  - `[DEBUG] [libsdwan] resetting configuration`
  - `[WARN] [libsdwan] [controller] operator(): failed to get SD: Gone, code 410`

## Resolution Steps

1. **Purge the existing Connector service** (choose based on distro):
   ```bash
   # Debian/Ubuntu
   sudo apt purge twingate-connector

   # RHEL/Fedora/CentOS
   dnf rm twingate-connector
   ```

2. **Generate a new deployment script** from the Twingate Admin Console

3. **Re-deploy** the Connector using the newly generated script

## Gotchas
- Simply restarting the Connector service will not resolve this—the stale token state persists until purged
- Must use `purge` (not just `remove`/`apt remove`) on Debian-based systems to clear configuration files
- A new token/script must be generated from the Admin Console; the old script cannot be reused
- If reusing the same host/VM, ensure full purge before re-installation to avoid stale config

## Related Docs
- Twingate Connector installation documentation
- Admin Console: Connector deployment script generation
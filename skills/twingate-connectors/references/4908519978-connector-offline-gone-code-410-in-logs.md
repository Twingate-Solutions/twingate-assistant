---
source: https://help.twingate.com/articles/4908519978-connector-offline-gone-code-410-in-logs
type: help
fetched: 2026-10-04
source_version: 6b3001ef07374c8848f7d2b34d2c61dd028a2c1c985afb756b49fa29b7564291
trust: official
---

# Connector Offline—"Gone, code 410" in Logs

## Summary
A Connector showing "Offline" with HTTP 410 errors indicates it was launched with expired or deleted tokens. This typically occurs after an incomplete or failed update attempt. The fix requires purging the Connector service and re-deploying with fresh credentials.

## Key Information
- HTTP 410 ("Gone") means the Connector's authentication tokens are invalid or have been deleted server-side
- The Connector enters an unrecoverable error state and cannot self-heal
- Affects any OS/package manager where Twingate Connector is installed

## Symptoms
Log lines indicating this issue:
```
[INFO] [connector] State: Error
[DEBUG] [libsdwan] [controller] run_state_machine: Pre-unrecoverable error
[DEBUG] [libsdwan] resetting configuration
[WARN] [libsdwan] [controller] operator(): failed to get SD: Gone, code 410
[INFO] [libsdwan] sdwan_state: Offline User
```

## Resolution (Step-by-Step)

1. **Purge the existing Connector installation** (removes stale tokens/config):
   - Debian/Ubuntu:
     ```bash
     sudo apt purge twingate-connector
     ```
   - RHEL/Fedora/CentOS:
     ```bash
     dnf rm twingate-connector
     ```

2. **Generate a new install script** from the Twingate Admin Console for the target Remote Network/Connector.

3. **Re-deploy** using the newly generated script from the Admin Console (do not reuse the old script).

## Gotchas
- Simply stopping/restarting the service will **not** resolve the 410 error — a full purge is required to clear stale token state
- Reusing the same install script from a previous deployment will reproduce the problem if those tokens have been invalidated
- `apt remove` (without `purge`) may leave behind config files containing the bad tokens; use `purge` to ensure full cleanup

## Related Docs
- Twingate Connector deployment documentation (Admin Console → Remote Networks → Connectors)
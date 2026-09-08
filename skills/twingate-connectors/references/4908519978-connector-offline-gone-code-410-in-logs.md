---
source: https://help.twingate.com/articles/4908519978-connector-offline-gone-code-410-in-logs
type: help
fetched: 2026-09-06
source_version: c372eec1c371cfccc80f3b59b537f306f1f523911617c64c801c46c293875626
---

# Connector Offline—"Gone, code 410" in Logs

## Summary
When a Connector starts with expired or deleted authentication tokens, it goes offline and logs a `Gone, code 410` error. This typically occurs after a failed or incomplete Connector update. Resolution requires purging the Connector service and re-deploying with fresh tokens.

## Key Information
- Error indicates Connector is using **invalid, expired, or deleted tokens**
- Connector appears **Offline** in the Admin Console
- Common trigger: incomplete/failed update attempts

## Symptoms
Log output indicating this issue:
```
[INFO] [connector] State: Error
[DEBUG] [libsdwan] [controller] run_state_machine: Pre-unrecoverable error
[DEBUG] [libsdwan] resetting configuration
[WARN] [libsdwan] [controller] operator(): failed to get SD: Gone, code 410
```
Also appears as:
- `Authentication [INFO] [libsdwan] sdwan_state: Offline User`

## Resolution (Step-by-Step)

1. **Purge the existing Connector service** from the host:

   - Debian/Ubuntu:
     ```bash
     sudo apt purge twingate-connector
     ```
   - RHEL/Fedora/CentOS:
     ```bash
     dnf rm twingate-connector
     ```

2. **Generate a new deployment script** from the Twingate Admin Console (creates fresh tokens).

3. **Re-run the new script** on the system to redeploy the Connector.

## Gotchas
- Simply restarting the Connector service will **not** resolve this—tokens are invalid and must be regenerated
- Use `purge` (not just `remove`/`uninstall`) on Debian systems to ensure configuration files with old tokens are cleared
- Re-using the same machine requires full purge before redeployment

## Related Docs
- Twingate Connector deployment (Admin Console)
- Connector update procedures
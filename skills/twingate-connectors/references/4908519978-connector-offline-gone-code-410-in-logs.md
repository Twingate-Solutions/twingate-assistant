---
source: https://help.twingate.com/articles/4908519978-connector-offline-gone-code-410-in-logs
type: help
fetched: 2026-11-01
source_version: 701f7ef3391220b43ace0868fde1f017d66b21458bc8fc2ee5710a40feb1c7f1
trust: official
---

# Connector Offline—"Gone, code 410" in Logs

## Summary
A Connector showing as Offline with a 410 error indicates it was launched with expired or deleted tokens. This commonly occurs after an incomplete or failed update attempt. Resolution requires purging the Connector service and re-provisioning with fresh credentials.

## Key Information
- Error code 410 ("Gone") means the Connector's tokens are no longer valid on the Twingate backend
- Connector will appear **Offline** in the Admin Console
- Root cause: expired tokens, deleted tokens, or failed update leaving stale state

## Symptoms
Log lines to look for:
```
[INFO] [connector] State: Error
[DEBUG] [libsdwan] [controller] run_state_machine: Pre-unrecoverable error
[DEBUG] [libsdwan] resetting configuration
[WARN] [libsdwan] [controller] operator(): failed to get SD: Gone, code 410
[INFO] [libsdwan] sdwan_state: Offline User
```

## Resolution Steps

1. **Purge the existing Connector installation** (choose based on distro):

   - Debian/Ubuntu:
     ```bash
     sudo apt purge twingate-connector
     ```
   - RHEL/Fedora/CentOS:
     ```bash
     dnf rm twingate-connector
     ```

2. **Generate a new install script** from the Twingate Admin Console for the target Remote Network/Connector.

3. **Re-deploy** using the newly generated script from the Admin Console (do not reuse old tokens or scripts).

## Gotchas
- Do not attempt to restart or reconfigure the existing Connector—the tokens are server-side invalidated and cannot be recovered
- Reusing the same machine requires a full purge (`purge`/`rm`), not just a stop/start or reinstall, to clear stale token state
- A simple `apt remove` may not clear configuration files; use `apt purge` to ensure full cleanup on Debian-based systems

## Related Docs
- Twingate Connector installation (Admin Console deploy scripts)
- Connector update procedures
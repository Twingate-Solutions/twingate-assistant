---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-08-06
source_version: b9f0ddadc7958d509cdb117b56a0398808e16268ca5629f8e00e1b6d14430000
---

# Access Denied to macOS Users Due to Screen Lock Posture Check

## Page Title
Access being denied to macOS users due to Screen Lock posture check

## Summary
A bug in the Twingate macOS client upgrade to version 1.0.27 causes false failures on Screen Lock posture checks. Users are denied resource access despite Screen Lock being properly configured. Logging out and restarting the client resolves the issue.

## Key Information
- **Affected component:** Twingate Client
- **Affected platform:** macOS
- **Affected version:** 1.0.27
- **Trigger:** Upgrade process to v1.0.27 causes incorrect posture check evaluation
- **Symptom:** Access denied with message stating device does not meet Screen Lock requirements, even when Screen Lock is properly enabled
- **Impact:** Any resource with Screen Lock posture check requirement becomes inaccessible

## Prerequisites
- Twingate macOS client version 1.0.27
- Resources configured with Screen Lock posture check requirements

## Step-by-Step Fix
1. Log out from Twingate client
2. Disconnect from Twingate
3. Restart the Twingate application
4. Reconnect — posture check should now pass correctly

## Gotchas
- Screen Lock being correctly configured on the device does **not** prevent this issue from occurring
- The fix is client-side only; no admin/network changes are required
- Issue is specific to the **upgrade process** to 1.0.27, not a clean install behavior

## Related Docs
- Twingate Posture Checks documentation
- macOS Client release notes
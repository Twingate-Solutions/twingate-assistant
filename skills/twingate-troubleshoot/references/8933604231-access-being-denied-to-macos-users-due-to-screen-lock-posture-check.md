---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-09-06
source_version: 7fdb62c792ad058f46f97606644d09247c7fa1ddf8935f768bec724979f2d80c
---

# Access Denied to macOS Users Due to Screen Lock Posture Check

## Page Title
Access being denied to macOS users due to Screen Lock posture check

## Summary
A bug in the Twingate macOS client upgrade to version 1.0.27 causes false posture check failures for Screen Lock requirements. Users are incorrectly denied access to resources even when Screen Lock is properly configured on their device.

## Key Information
- **Affected component:** Twingate Client
- **Affected platform:** macOS
- **Affected version:** 1.0.27
- **Symptom:** Access denied with message stating device does not meet Screen Lock posture check requirements, despite Screen Lock being correctly configured

## Prerequisites
- Twingate macOS client version 1.0.27
- Resources with Screen Lock posture check requirements enabled

## Fix / Resolution Steps
1. Log out of Twingate client
2. Disconnect from Twingate
3. Restart the Twingate application

## Gotchas
- This is an upgrade process bug — the device configuration itself is correct; the client fails to properly detect it post-upgrade
- Simply reconnecting without a full logout may not resolve the issue; a complete logout and restart is required
- No configuration changes to Screen Lock settings are needed on the device

## Related Docs
- Twingate Client documentation
- Screen Lock posture check configuration
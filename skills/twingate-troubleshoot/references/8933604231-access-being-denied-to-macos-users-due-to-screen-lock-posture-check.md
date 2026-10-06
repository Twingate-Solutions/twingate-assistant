---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-10-04
source_version: 3411b9f71b4c3c49470473efb84b63a5995b1a94d6c9ee06db36808d8bcb8cbd
trust: official
---

# Access Denied to macOS Users Due to Screen Lock Posture Check

## Summary
A bug in the upgrade process to macOS client version 1.0.27 causes false Screen Lock posture check failures. Users are denied access to Twingate resources even when Screen Lock is properly configured on their device.

## Key Information
- **Affected component:** Twingate Client
- **Affected platform:** macOS
- **Affected version:** 1.0.27
- **Symptom:** Access denied with message indicating device does not meet Screen Lock requirements, despite Screen Lock being correctly configured

## Prerequisites
- User must have Twingate client v1.0.27 installed on macOS
- Resource must have Screen Lock posture check requirement enabled

## Fix (Step-by-Step)
1. Log out of Twingate client
2. Disconnect from Twingate
3. Restart the Twingate application

## Gotchas
- The Screen Lock setting itself does not need to be changed — the issue is not a misconfiguration, it is an artifact of the upgrade process
- Simply reconnecting without a full logout may not resolve the issue; a full logout and restart is required

## Related Docs
- Twingate Posture Checks documentation
- macOS Client release notes for v1.0.27
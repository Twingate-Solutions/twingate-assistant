---
source: https://help.twingate.com/articles/6848754023-login-to-chromebook-fails-with-device-security-not-met
type: help
fetched: 2026-10-04
source_version: 982b083c0405ff6fbb44578eb17dd3e69923bc40f730e4b34f31d9bbb083eb76
trust: official
---

# Login to Chromebook Fails with "Device Security not met"

## Summary
When Biometric configuration is included as a criterion in Device Security Posture Checks, ChromeOS devices will always fail with "Device Security not met." This is a platform limitation with no workaround.

## Key Information
- **Affected component:** Twingate Client
- **Affected platform:** Google Chromebook (all models), ChromeOS (all versions)
- **Root cause:** ChromeOS APIs do not reliably expose biometric configuration data to third-party applications
- Twingate cannot validate biometrics posture on ChromeOS regardless of the device's actual biometric settings

## Gotchas
- There is **no supported workaround** — biometric posture checks simply cannot function on ChromeOS
- The failure message "Device Security not met" may be misleading; the device isn't necessarily insecure, it's a reporting limitation
- This affects all ChromeOS versions and all Chromebook hardware models

## Resolution
- **Remove biometric configuration** as a criterion from Device Security Posture Checks for any policies that apply to ChromeOS/Chromebook users
- If biometric enforcement is required for other platforms, create a **separate posture check policy** that excludes ChromeOS devices

## Related Docs
- Twingate Device Security Posture Checks (general configuration)
- Twingate Client documentation
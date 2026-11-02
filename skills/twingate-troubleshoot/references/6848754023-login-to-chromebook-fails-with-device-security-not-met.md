---
source: https://help.twingate.com/articles/6848754023-login-to-chromebook-fails-with-device-security-not-met
type: help
fetched: 2026-11-01
source_version: 1281dd2bda36246ea1a5f85195fa309e9c7bd0697d12c8bd3608d68089ba2db3
trust: official
---

# Login to Chromebook Fails with "Device Security not met"

## Summary
Chromebook devices fail Twingate Device Security Posture Checks when biometric configuration is set as a criteria. This is a platform-level limitation with ChromeOS APIs, not a Twingate bug. No workaround exists.

## Key Information
- **Affected component:** Twingate Client
- **Affected platform:** Google Chromebook, all models and all ChromeOS versions
- **Root cause:** ChromeOS APIs do not reliably report biometric configuration data to Twingate
- **Status:** No supported workaround; no fix timeline indicated

## Gotchas
- Adding biometric posture check criteria will block **all** ChromeOS users from connecting — avoid this configuration if your org uses Chromebooks
- Other device posture check criteria are unaffected; only **biometric configuration** is broken on ChromeOS
- Error message ("Device Security not met") is generic and does not indicate ChromeOS-specific cause — requires manual investigation to identify biometric check as the culprit

## Resolution
Remove or exclude biometric configuration from Device Security Posture Check policies that apply to ChromeOS devices. Use non-biometric posture criteria for Chromebook users.

## Related Docs
- Twingate Device Security Posture Checks (general configuration)
- Twingate Client troubleshooting
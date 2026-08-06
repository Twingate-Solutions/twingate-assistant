---
source: https://help.twingate.com/articles/6848754023-login-to-chromebook-fails-with-device-security-not-met
type: help
fetched: 2026-08-06
source_version: c3565387800e1c648c54ea40f33870fe8c8ea3a9d33a1ef98e3b6368e1a237b1
---

# Login to Chromebook Fails with "Device Security Not Met"

## Summary
Twingate Device Security Posture Checks fail on ChromeOS when Biometric configuration is included as a criteria. This is a platform limitation—ChromeOS APIs do not reliably report biometric data, so Twingate cannot validate biometric settings on these devices.

## Key Information
- **Affected component:** Twingate Client
- **Affected hardware:** All Google Chromebook models
- **Affected OS:** ChromeOS (all versions)
- **Trigger:** Biometric configuration criteria in Device Security Posture Checks
- **Error message:** "Device Security not met"

## Cause
ChromeOS APIs have a limitation in biometric reporting. Twingate cannot reliably read or validate biometric configuration state on ChromeOS devices, causing posture checks that include biometric criteria to always fail.

## Gotchas
- **No workaround exists.** There is no supported method to use biometric configuration posture checks on ChromeOS.
- Other posture check criteria (non-biometric) may still work on ChromeOS—the limitation is specific to biometric configuration.
- This affects **all** ChromeOS versions; there is no minimum version that resolves the issue.

## Resolution
- Remove biometric configuration as a criteria from Device Security Posture Checks if ChromeOS/Chromebook users need access.
- Use alternative posture check criteria that are supported on ChromeOS for those users or device groups.

## Related Docs
- Twingate Device Security Posture Checks configuration
- Twingate Client documentation
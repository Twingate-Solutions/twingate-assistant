---
source: https://help.twingate.com/articles/6848754023-login-to-chromebook-fails-with-device-security-not-met
type: help
fetched: 2026-09-06
source_version: 9109bc44dc315952bb6ec3524ed8e2be54e9d739d28ddf01135a12b6209ec686
---

# Login to Chromebook Fails with "Device Security not met"

## Page Title
Login to Chromebook Fails with "Device Security not met"

## Summary
When Biometric configuration is included as a criteria in Device Security Posture Checks, ChromeOS devices will always fail with "Device Security not met." This is a platform limitation with ChromeOS APIs, not a Twingate bug.

## Key Information
- **Affected component:** Twingate Client on Google Chromebook (all models, all ChromeOS versions)
- **Root cause:** ChromeOS APIs do not reliably report biometric configuration data to Twingate
- **Result:** Biometric posture checks always fail on ChromeOS regardless of actual device configuration
- **No workaround exists** for using biometric configuration posture checks on ChromeOS

## Prerequisites
- N/A (informational/diagnostic page)

## Step-by-Step Resolution
1. Identify if affected policies include **Biometric configuration** as a Device Security Posture Check criterion
2. Remove or exclude the Biometric configuration criterion from posture check policies applied to ChromeOS devices
3. Use alternative posture check criteria that are supported on ChromeOS

## Configuration Values
- No specific env vars, CLI flags, or API params applicable

## Gotchas
- This limitation applies to **all ChromeOS versions and all Chromebook models** — no OS update will resolve it
- There is **no supported workaround** — biometric posture checks cannot be made to work on ChromeOS
- Admins creating Device Security Posture policies must explicitly account for ChromeOS exclusions when using biometric criteria; applying a universal policy including biometrics will block all ChromeOS users

## Related Docs
- Twingate Device Security Posture Checks (general configuration)
- Twingate Client documentation
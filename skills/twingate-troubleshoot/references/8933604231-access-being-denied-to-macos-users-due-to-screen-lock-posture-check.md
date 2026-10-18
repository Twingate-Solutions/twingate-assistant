---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-10-18
source_version: 76f77d15125272df2042fce52a45b8c77e8d66417c0793e00d1a9787bd348d7f
trust: official
---

# [MacOS Client] Biometric Posture Check Fails in Clamshell Mode

## Summary
When a Device Security policy requires biometric configuration, MacBooks in clamshell mode (lid closed) fail the posture check because macOS disables Touch ID when the lid is closed. The Twingate Client caches the last successful biometric result while running, but this cache clears on quit or restart, causing failures when Twingate starts while already in clamshell mode.

## Key Information
- **Affected component:** Twingate Client / Device Security posture checks
- **Platform:** macOS only
- **Trigger condition:** Twingate starts (fresh launch or post-restart) while MacBook lid is closed
- **Cache behavior:** Successful biometric check result is retained in memory while Client runs; closing the lid after a successful check does not break the session
- **Cache invalidation:** Result is cleared on Twingate quit or system restart

## Symptoms
- Error messages: `"Device security not met"` or `"Device requirements not met"` on sign-in or Resource access
- Touch ID is correctly configured on the device
- Client logs contain: `Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value`

## Prerequisites
- Device Security policy with biometric configuration requirement enabled
- MacBook used with external display in clamshell mode

## Resolution Options

1. **Open the lid before starting Twingate**
   - After restart or reopening the Client, open the MacBook lid, sign in and connect, then close the lid to resume clamshell mode

2. **Use an Apple Magic Keyboard with Touch ID**
   - Pair with the Mac; keeps biometrics available while lid is closed, permanently resolving the issue

## Gotchas
- Simply having Touch ID configured is insufficient—macOS must be able to *evaluate* it at the time Twingate starts
- The cached result does not persist across Client restarts or system reboots
- If the check still fails **with the lid open**, the issue is something other than clamshell mode—collect Client logs and contact Twingate Support

## Related Docs
- Twingate Device Security policies
- Twingate Client logs collection (for support escalation)
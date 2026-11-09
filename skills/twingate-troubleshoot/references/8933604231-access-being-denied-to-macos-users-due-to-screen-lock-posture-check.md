---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-11-08
source_version: 6596899c537e255b522040764405fd7a53770ea1759fc9169d438fbed0368365
trust: official
---

# [MacOS Client] Biometric Posture Check Fails in Clamshell Mode

## Summary
When a Device Security policy requires biometric configuration, MacBooks running Twingate in clamshell mode (lid closed) may fail posture checks because macOS disables Touch ID when the lid is closed. The Twingate client caches a successful biometric check during a session, but this cache clears on quit or restart, causing failures if Twingate starts while already in clamshell mode.

## Key Information
- **Affected component:** Twingate Client, Device Security posture checks
- **Platform:** macOS only
- **Trigger condition:** Twingate starts (fresh launch or after restart) while MacBook lid is already closed
- **Cache behavior:** Successful biometric result is remembered during an active session but is wiped on client quit or system restart
- **macOS limitation:** Touch ID is unavailable in clamshell mode unless a Touch ID-capable external keyboard is connected

## Prerequisites
- Device Security policy with biometric configuration requirement enabled
- macOS MacBook used with external display in clamshell mode

## Symptoms
- Login or Resource access fails with `"Device security not met"` or `"Device requirements not met"`
- Touch ID is confirmed configured on the device
- Failure occurs after restart or Twingate relaunch while lid is closed
- Client logs contain: `Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value`

## Resolution Options

1. **Open the lid at startup** — After restart or reopening Twingate, open the MacBook lid before connecting. Once Twingate connects successfully, the lid can be closed and clamshell mode resumes normally.

2. **Use a Touch ID keyboard** — An Apple Magic Keyboard with Touch ID, paired to the Mac, keeps biometrics available regardless of lid state.

3. **Escalate if issue persists with lid open** — If posture check still fails with lid open, contact Twingate Support with Client logs attached.

## Gotchas
- The biometric result cache is **session-scoped only** — it does not persist across restarts or client relaunches
- Closing the lid *after* a successful connection does **not** trigger a failure; only startup-while-closed is problematic
- Third-party external keyboards with fingerprint sensors are not mentioned as a workaround — only Apple Magic Keyboard with Touch ID is confirmed

## Related Docs
- Twingate Device Security policies
- Twingate Client logs (for Support escalation)
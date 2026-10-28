---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-10-28
source_version: 2b2112c6497de467e4e214b95fdcc59891c3d808683ce97cf53555848876e176
trust: official
---

# [MacOS Client] Biometric Posture Check Fails in Clamshell Mode

## Summary
When a Device Security policy requires biometric configuration, MacBooks in clamshell mode (lid closed) may fail posture checks because macOS disables Touch ID when the lid is closed. The Twingate Client caches the last successful biometric check during a session, but this cache clears on quit or restart, causing failures when Twingate starts while already in clamshell mode.

## Key Information
- **Affected component:** Twingate Client / Device Security posture checks
- **Platform:** macOS only
- **Trigger condition:** Twingate starts (fresh launch or after restart) while MacBook lid is already closed
- **Cache behavior:** Successful biometric result is retained in-session (lid can be closed after connecting), but is cleared on Twingate quit or system restart

## Prerequisites
- Device Security policy configured with biometric requirement
- MacBook used in clamshell mode (external display, lid closed)

## Symptoms
- Sign-in or Resource access fails with `"Device security not met"` or `"Device requirements not met"`
- Touch ID is properly configured on the device
- Failure occurs after restart or Twingate relaunch while lid is closed
- Client logs contain: `Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value`

## Resolution Options

1. **Open lid before starting Twingate**
   - After restart or relaunch, open the MacBook lid, connect to Twingate, then close lid — clamshell use continues without issue for that session.

2. **Use a Touch ID keyboard**
   - Pair an Apple Magic Keyboard with Touch ID to the Mac; biometrics remain available regardless of lid state.

3. **If check fails with lid open:** Contact Twingate Support with Client logs.

## Gotchas
- The cached biometric result is **session-scoped only** — closing/reopening the app or rebooting clears it
- macOS behavior is the root cause; Twingate cannot override the OS-level Touch ID restriction in clamshell mode
- A non-Apple external keyboard will **not** resolve this; Touch ID requires Apple's Magic Keyboard with Touch ID specifically

## Configuration Values
- No specific env vars or CLI flags apply; behavior is governed by the Device Security policy biometric requirement setting in the Twingate admin console

## Related Docs
- Twingate Device Security policies
- Twingate Client logs (for Support escalation)
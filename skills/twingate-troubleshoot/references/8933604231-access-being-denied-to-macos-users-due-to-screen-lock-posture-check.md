---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-11-01
source_version: 60f9cf52e5e09adaeb15349af9ebf0c3bb74066208c67bdc507c8b49a83c1225
trust: official
---

# macOS Biometric Posture Check Fails in Clamshell Mode

## Summary
When a Device Security policy requires biometric configuration, MacBooks running Twingate in clamshell mode (lid closed) can fail posture checks because macOS disables Touch ID when the lid is closed. The Twingate client caches a successful biometric check during a session, but this cache clears on quit or restart.

## Key Information
- **Affected component:** Twingate Client / Device Security posture checks
- **Platform:** macOS only
- **Trigger:** Twingate starts or restarts while MacBook lid is already closed (clamshell mode)
- **Cache behavior:** Client remembers last successful biometric check while running — closing the lid *after* a successful check does not trigger failure; only startup-in-clamshell does

## Symptoms
- Error: `"Device security not met"` or `"Device requirements not met"` on sign-in or Resource access
- Occurs after Mac restart or Twingate quit/reopen with lid closed
- Client log entry:
  ```
  Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value
  ```

## Prerequisites
- Device Security policy with biometric configuration required
- MacBook used in clamshell mode (external display, lid closed)
- No Touch ID keyboard connected

## Resolution Options

1. **Open the lid before starting Twingate**
   - After a restart or reopen, open the MacBook lid, connect to Twingate, then close the lid to resume clamshell mode

2. **Use an Apple Magic Keyboard with Touch ID**
   - Pair a Touch ID-capable Apple Magic Keyboard to keep biometrics available regardless of lid state

3. **If check fails with lid open** — collect Client logs and contact Twingate Support

## Gotchas
- The biometric check cache is **session-scoped** — cleared on quit or system restart; there is no persistent cache across restarts
- macOS fully disables Touch ID in clamshell mode unless a compatible external Touch ID keyboard is connected — this is an OS-level restriction, not a Twingate bug
- Simply having Touch ID configured on the device is not sufficient; it must be *evaluable* at the time Twingate initializes

## Related Docs
- Twingate Device Security policies
- Twingate Client logs (for Support escalation)
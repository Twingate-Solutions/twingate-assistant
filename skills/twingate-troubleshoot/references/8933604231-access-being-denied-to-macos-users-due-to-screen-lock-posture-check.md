---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-10-25
source_version: 8688362227ae6d0995435c861e0c3994edec4ecfe191f65013faea0c464cfc6b
trust: official
---

# [MacOS Client] Biometric Posture Check Fails in Clamshell Mode

## Summary
When a Device Security policy requires biometric configuration, MacBooks in clamshell mode (lid closed) fail the posture check because macOS disables Touch ID when the lid is closed. The Twingate Client caches the last successful biometric check while running, but this cache is cleared on quit or restart.

## Key Information
- **Affected component:** Twingate Client, Device Security posture checks
- **Platform:** macOS only
- **Trigger condition:** Twingate starts (fresh launch or post-restart) while MacBook lid is already closed
- **Cache behavior:** Successful biometric check is remembered *during* a session; closing lid after a successful check does not break the session
- **Cache clears on:** Twingate quit, macOS restart

## Symptoms
- Login or Resource access fails with `"Device security not met"` or `"Device requirements not met"`
- Touch ID is confirmed configured on the device
- Failure occurs specifically after restart or relaunch while lid is closed
- Client logs contain: `Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value`

## Prerequisites
- Device Security policy with biometric configuration requirement enabled
- MacBook used in clamshell mode (external display, lid closed)

## Resolution Options

1. **Open the lid before starting Twingate**
   - After restart or relaunch, open the MacBook lid, connect to Twingate, then close the lid

2. **Use a Touch ID-capable external keyboard**
   - Apple Magic Keyboard with Touch ID keeps biometrics available while lid is closed
   - Keyboard must be paired with the Mac

3. **If check fails with lid open**
   - Collect Client logs and contact Twingate Support

## Gotchas
- The cached biometric result does **not** persist across Twingate restarts or macOS reboots — users must re-confirm biometrics each session start
- Simply having Touch ID configured is insufficient if Twingate initializes in clamshell mode; macOS-level availability is the constraint, not Twingate configuration
- Non-Apple keyboards with fingerprint readers do not resolve this issue — only Apple Magic Keyboard with Touch ID is confirmed to maintain biometric availability in clamshell mode

## Related Docs
- Twingate Device Security policies
- Twingate Client logs collection (for Support escalation)
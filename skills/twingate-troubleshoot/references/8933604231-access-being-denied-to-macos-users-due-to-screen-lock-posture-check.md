---
source: https://help.twingate.com/articles/8933604231-access-being-denied-to-macos-users-due-to-screen-lock-posture-check
type: help
fetched: 2026-11-13
source_version: 6bb025dc038d02f07af73ebe72ad4c0568865a7601bc1f404f058d4dc2b9d6a4
trust: official
---

# Page Title
[MacOS Client] Biometric posture check fails when Twingate starts in clamshell mode

# Summary
When a Device Security policy requires biometric configuration, a MacBook in clamshell mode (lid closed, external display) can fail the posture check because macOS disables Touch ID while the lid is closed. The Twingate Client caches the last successful biometric result, but the cache is cleared on quit or restart, so starting Twingate with the lid closed causes a failure.

# Key Information
- **Applies to:** Twingate Client and Device Security on macOS.
- **Error messages shown to the user:** "Device security not met" or "Device requirements not met", even though Touch ID is set up.
- **Typical trigger:** the Mac is restarted, or Twingate is quit and reopened, while the lid is closed.
- **Log signature:** `Unable to evaluate DeviceOwnerAuthenticationWithBiometrics policy, error - systemCancel, will return cached value`
- **Cause:**
  - macOS disables Touch ID in clamshell mode unless a Touch ID keyboard is connected.
  - The Client remembers the last successful biometric check only while it is running.
  - If the Client confirmed biometrics with the lid open, closing the lid afterward does not fail the check.
  - Quitting Twingate or restarting the Mac clears the cached result. If Twingate then starts in clamshell mode, there is no prior result and biometrics are reported as unavailable.

# Prerequisites
- A Device Security policy that requires biometric configuration.
- A MacBook with Touch ID configured.

# Step-by-Step (Resolution)
Use one of the following options:
1. **Open the lid when starting Twingate**
   - After a restart or reopening Twingate, open the lid and connect.
   - Once connected, you can close the lid and continue in clamshell mode.
2. **Use a keyboard with Touch ID**
   - Pair an Apple Magic Keyboard with Touch ID with the Mac.
   - Biometrics stay available while the lid is closed.

# Configuration Values
- None. This is a behavior and hardware limitation, with no env vars, CLI flags, or API parameters.
- Relevant policy setting: the biometric configuration requirement in a Device Security policy.

# Gotchas
- Users with Touch ID properly set up can still be denied, so the failure can be mistaken for a misconfiguration.
- The failure recurs after every restart or Twingate relaunch in clamshell mode, because the cached result is not persisted.
- Closing the lid after a successful connection is fine, as long as Twingate keeps running.
- If the check still fails with the lid open, contact Support and include the Client logs.

# Related Docs
- Twingate Device Security (posture check) policy documentation
- Twingate macOS Client documentation
- Twingate Support (for log submission)
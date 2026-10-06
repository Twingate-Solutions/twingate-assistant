---
source: https://help.twingate.com/articles/5666924507-device-security-windows-screen-lock-is-activated-but-not-detected-by-the-posture-check
type: help
fetched: 2026-10-04
source_version: 4152fb8f77f0dc68fbae79dd56849bdf7b73184eff746337b853fb921be2d6f5
trust: official
---

# Device Security: Windows Screen Lock Not Detected by Posture Check

## Summary
When Windows screen lock is enabled but not detected by Twingate's posture check, users are blocked from accessing resources that require screen lock. The issue stems from a specific registry value that Twingate reads to verify screen lock status.

## Key Information
- Twingate uses `user32.dll` (`SystemParametersInfo` function) to verify screen lock status
- The check reads the `ScreenSaverIsSecure` registry value
- A value of `1` = passes posture check; `0` or missing = fails

## Symptoms
- Cannot access resources requiring screen lock despite screen lock being active on the device
- Client log contains: `[INFO][client]Client posture data collected. {"IsScreenSaverSecure":false}`

## Prerequisites
- Back up the registry before making changes
- Windows admin access to modify registry keys

## Resolution Steps

1. Open Registry Editor (`regedit.exe`)
2. Navigate to:
   ```
   HKEY_CURRENT_USER\Control Panel\Desktop
   ```
3. Locate the value `ScreenSaverIsSecure`
4. Set the value to `1`
5. Verify posture check passes in the Twingate client

## Configuration Values

| Registry Path | Value Name | Required Value |
|---|---|---|
| `HKEY_CURRENT_USER\Control Panel\Desktop` | `ScreenSaverIsSecure` | `1` |

## Gotchas
- This is a **per-user** registry key (`HKEY_CURRENT_USER`), not machine-wide — must be set for each affected user profile
- Screen lock appearing active in Windows UI does not guarantee `ScreenSaverIsSecure` is set to `1`
- Always back up the registry before editing

## Related Docs
- Twingate Client posture checks documentation
- Twingate Device Security policies
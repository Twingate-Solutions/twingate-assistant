---
source: https://help.twingate.com/articles/5666924507-device-security-windows-screen-lock-is-activated-but-not-detected-by-the-posture-check
type: help
fetched: 2026-08-06
source_version: 930457303b8cde9a5407151a6ba276e094e61a2cf854f91f31d5d4fdf53866ee
---

# Device Security: Windows Screen Lock Not Detected by Posture Check

## Summary
Twingate's Windows client posture check may fail to detect screen lock as active even when it's enabled on the device. The issue stems from a specific registry value that must be set to `1` for Twingate to recognize screen lock as secure.

## Key Information
- **Component**: Twingate Client
- **Platform**: Windows (all current releases)
- **Detection method**: Twingate uses `user32.dll` → `SystemParametersInfo` function to verify screen lock
- **Log indicator**: `[INFO][client]Client posture data collected. {"IsScreenSaverSecure":false}`

## Prerequisites
- Registry backup recommended before making any changes
- User must have permission to modify `HKEY_CURRENT_USER` registry keys

## Configuration Values

| Setting | Details |
|---|---|
| Registry key | `HKEY_CURRENT_USER\Control Panel\Desktop` |
| Registry value name | `ScreenSaverIsSecure` |
| Required value | `1` |

## Step-by-Step Resolution

1. **Back up the registry** before proceeding
2. Open **Registry Editor** (`regedit`)
3. Navigate to `HKEY_CURRENT_USER\Control Panel\Desktop`
4. Locate the `ScreenSaverIsSecure` value
5. Set the value to `1`
6. Verify the posture check passes by attempting to connect to the restricted resource

## Gotchas
- Screen lock appearing active in Windows UI does not guarantee `ScreenSaverIsSecure` is set to `1`
- The registry value must be explicitly `1`; missing or `0` values will cause posture check failure
- This is a per-user registry key (`HKEY_CURRENT_USER`), so the fix applies per user profile, not system-wide

## Related Docs
- Twingate Device Security / Posture Checks documentation
- Windows `SystemParametersInfo` function (Microsoft docs)
- Twingate Client logging reference
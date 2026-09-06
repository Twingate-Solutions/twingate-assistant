---
source: https://help.twingate.com/articles/5666924507-device-security-windows-screen-lock-is-activated-but-not-detected-by-the-posture-check
type: help
fetched: 2026-09-06
source_version: adce2aaadcae7cb1fa3eee9e35e0a54d27e48847cf84385264fe9c62dffcbeeb
---

# Device Security: Windows Screen Lock Not Detected by Posture Check

## Summary
When Screen Lock is configured as a Twingate resource access requirement on Windows, the posture check may fail to detect it as active even when screen lock is enabled. The issue relates to a specific registry value that Twingate reads to verify screen lock status.

## Key Information
- Twingate verifies screen lock via `user32.dll` using the `SystemParametersInfo` function
- The specific registry value checked is `ScreenSaverIsSecure` under `HKEY_CURRENT_USER\Control Panel\Desktop`
- Value must be set to `1` to pass the posture check
- Affects all current Windows releases

## Symptoms
- Users cannot access resources requiring screen lock, despite screen lock being enabled on the device
- Client logs show: `[INFO][client]Client posture data collected. {"IsScreenSaverSecure":false}`

## Prerequisites
- Back up the Windows registry before making any changes

## Resolution Steps

1. Open Registry Editor (`regedit`)
2. Navigate to:
   ```
   HKEY_CURRENT_USER\Control Panel\Desktop
   ```
3. Locate the value `ScreenSaverIsSecure`
4. Set the value to `1`
5. Verify posture check passes by attempting to connect to the restricted resource

## Configuration Values

| Registry Path | Value Name | Required Value |
|---|---|---|
| `HKEY_CURRENT_USER\Control Panel\Desktop` | `ScreenSaverIsSecure` | `1` |

## Gotchas
- Windows screen lock settings in the UI do not always automatically set `ScreenSaverIsSecure=1` — manual registry verification may be required
- This is a per-user registry key (`HKEY_CURRENT_USER`), so the fix must be applied for each affected user profile on shared machines
- Always back up the registry before editing, even for minor changes

## Related Docs
- Twingate Client posture checks documentation
- Twingate Screen Lock security policy configuration
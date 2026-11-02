---
source: https://help.twingate.com/articles/5666924507-device-security-windows-screen-lock-is-activated-but-not-detected-by-the-posture-check
type: help
fetched: 2026-11-01
source_version: 98d7af9cbd9d99b771cb750d5e939d2aed36e61aac07cc93519a3a24bb38fc14
trust: official
---

# Device Security: Windows Screen Lock Not Detected by Posture Check

## Summary
When Screen Lock is required for resource access, Twingate's posture check may fail to detect it as active on Windows, blocking resource access. Twingate uses `user32.dll`'s `SystemParametersInfo` function to verify screen lock status via a specific registry value.

## Key Information
- **Component:** Twingate Client
- **Platform:** Windows (all current releases)
- **Root cause:** Registry value `ScreenSaverIsSecure` is not set to `1`
- Twingate checks screen lock via `user32.dll` → `SystemParametersInfo`

## Symptoms
- Cannot access resources requiring screen lock despite screen lock being enabled on device
- Client log entry: `[INFO][client]Client posture data collected. {"IsScreenSaverSecure":false}`

## Registry Fix

**Key:** `HKEY_CURRENT_USER\Control Panel\Desktop`  
**Value name:** `ScreenSaverIsSecure`  
**Required value:** `1`

### Steps
1. Back up the registry before making changes
2. Open Registry Editor (`regedit`)
3. Navigate to `HKEY_CURRENT_USER\Control Panel\Desktop`
4. Locate `ScreenSaverIsSecure`
5. Set value to `1`
6. Re-test resource access via Twingate client

## Configuration Values

| Registry Path | Value Name | Required Data |
|---|---|---|
| `HKCU\Control Panel\Desktop` | `ScreenSaverIsSecure` | `1` |

## Gotchas
- Screen lock being visually active on Windows does **not** guarantee this registry key is set correctly
- **Always back up the registry before editing** — even minor changes carry risk
- This is a per-user registry key (`HKEY_CURRENT_USER`), not machine-wide; fix must be applied per user account

## Related Docs
- Twingate Device Security / Posture Checks documentation
- Microsoft docs: [`SystemParametersInfo`](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
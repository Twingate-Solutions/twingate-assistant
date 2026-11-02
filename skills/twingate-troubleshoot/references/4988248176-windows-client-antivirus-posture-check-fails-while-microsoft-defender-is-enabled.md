---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-01
source_version: 0507e8009cb7ffd59c7fef516d4cdb171588f227ab4860577a9c538efbe22392
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
The Twingate Antivirus device posture check reports antivirus as disabled even when Microsoft Defender is running normally. This is a confirmed Microsoft bug in Defender platform versions 4.18.26070.9–4.18.26080.3, where Windows Security Center (WSC) misreports antivirus state. The fix is included in Defender platform version 4.18.26080.4 (released September 17, 2026).

## Key Information
- **Root cause**: WSC misreports antivirus status at service start; Twingate reads from WSC, not from `Get-MpComputerStatus` or `root\SecurityCenter2` WMI
- **Affected Defender versions**: 4.18.26070.9 through below 4.18.26080.4
- **Fix version**: 4.18.26080.4 or later
- **Twingate Client version is irrelevant** — updating the Client does not fix this
- Affected device set can change daily (intermittent per reboot); Defender continues to protect the device throughout

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users blocked with `Device security not met` or `Block reason: Verified device` in Resource access events
- Failure persists through sign-outs and Client reinstalls
- `Get-MpComputerStatus` and Windows Security app show Defender as healthy (expected disagreement — not a Twingate bug)

## Resolution

### Step 1: Check current Defender platform version
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion
```
Compare `AMProductVersion` against `4.18.26080.4`. Below that version = potentially affected.

### Step 2: Update Microsoft Defender
- Devices receive the update through their normal Defender update channel
- No Twingate changes or Client upgrade required
- Reference: [Microsoft Defender for Endpoint release notes](https://learn.microsoft.com/en-us/defender-endpoint/msda-updates-previous-versions-technical-upgrade-support)

## Temporary Workarounds (per-device only, not persistent)

**Toggle Real-time protection** (clears until next WSC service restart):
1. Open **Windows Security > Virus & threat protection > Manage settings**
2. Toggle **Real-time protection** off, then back on
- ⚠️ Briefly disables protection; does not survive reboot

**Fleet last resort**: Remove the Antivirus requirement from the Device Security Policy to restore access immediately — re-enable once devices reach 4.18.26080.4+.

## Gotchas
- `Get-MpComputerStatus`, WMI (`root\SecurityCenter2`), and the Windows Security app read a **different source** than the posture check — disagreement between these tools and Twingate is expected and normal on affected devices
- The toggle workaround does not scale and is not persistent across reboots
- Problem appears intermittent because WSC samples state only at service start

## Configuration Values
| Item | Value |
|------|-------|
| Fixed Defender platform version | `4.18.26080.4` |
| PowerShell property to check | `AMProductVersion` |

## Related Docs
- Microsoft advisory: *Incorrect notifications that "Microsoft Defender Antivirus is turned off"*
- [Twingate Device Posture Checks documentation](https://help.twingate.com)
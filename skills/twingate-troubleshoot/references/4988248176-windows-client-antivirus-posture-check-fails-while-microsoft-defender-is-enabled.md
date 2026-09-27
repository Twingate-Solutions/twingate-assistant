---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-09-27
source_version: 582b887ae31d1ce6ca977cba4219eb4374346ba427f5936806143d670a655318
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
A confirmed Microsoft bug causes Windows Security Center (WSC) to misreport antivirus status, causing Twingate's Antivirus posture check to fail even when Microsoft Defender is fully enabled. The Twingate Client reads from WSC (not from WMI/Get-MpComputerStatus), so the check fails until WSC re-evaluates. No Microsoft fix date has been published (issue active as of August–September 2026).

## Key Information
- **Root cause**: WSC misreports antivirus state at service startup and caches the incorrect value indefinitely
- **Twingate reads WSC**; other tools (`Get-MpComputerStatus`, `root\SecurityCenter2` WMI, Windows Security app) read different sources — disagreement between them and Twingate is expected and normal on affected devices
- Defender continues protecting the device throughout; only WSC's reported value is wrong
- Issue is not tied to a specific Windows build, Client version, or Windows security update
- Failure persists across sign-outs, Client reinstalls, and Twingate Client updates

## Affected Platforms
- Windows 10 (all supported versions)
- Windows 11
- Windows Server

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users blocked with **"Device security not met"**
- Resource access events show **"Block reason: Verified device"**
- Failure does not self-clear

## Workaround (Per-Device)

**Toggle Real-Time Protection:**
1. Open **Windows Security → Virus & threat protection → Manage settings**
2. Turn **Real-time protection** OFF, then back ON
3. This forces WSC to re-evaluate immediately

**Limitations:**
- Real-time protection is briefly disabled during the toggle
- Fix does not survive reboot — WSC service restart may re-apply incorrect value
- Repeat after each reboot if needed

## Fleet-Scale Workaround
For large numbers of affected devices (per-device toggle does not scale):
1. Temporarily **remove the Antivirus requirement** from the affected Device Security Policy in Admin Console
2. Re-enable the requirement after Microsoft ships the Defender fix

## Configuration Values
| Location | Setting |
|---|---|
| Admin Console | Device Security Policy → Antivirus requirement |
| Windows Security | Virus & threat protection → Manage settings → Real-time protection |

## Gotchas
- **Reboots are not reliable**: May clear or re-apply the incorrect WSC value
- **Updating Defender does not fix it**: Microsoft's advisory indicates the behavior appears *after* latest Defender updates install
- Do not use `Get-MpComputerStatus` or WMI queries to validate — they will show healthy even on affected devices, creating a false impression the posture check should pass
- The WSC incorrect value persists until the Security Center service restarts or state is manually toggled

## Related Docs
- Microsoft Windows release health: *"Incorrect notifications that Microsoft Defender Antivirus is turned off"*
- Twingate Device Security Policy configuration (Admin Console)
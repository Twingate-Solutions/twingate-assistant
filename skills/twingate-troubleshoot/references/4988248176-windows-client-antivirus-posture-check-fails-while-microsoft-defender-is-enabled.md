---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-10-04
source_version: af09bd3c88efbe8507eb279f10a1c45361f9c6f73ba801ac2d453724b86be958
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
Twingate's Antivirus device posture check falsely reports antivirus as disabled on Windows devices where Microsoft Defender is running normally. The root cause is a confirmed Microsoft bug where Windows Security Center (WSC) misreports antivirus state at service startup. No Microsoft fix date has been published (issue active as of August–September 2026).

## Key Information
- Twingate reads antivirus state from WSC, not from `Get-MpComputerStatus`, `root\SecurityCenter2` WMI, or the Windows Security app — those sources may show Defender as healthy while Twingate still fails the check
- The incorrect WSC value persists across sign-outs and Client reinstalls; updating the Twingate Client does not help
- Microsoft Defender continues protecting the device throughout; this is purely a reporting/state issue
- The discrepancy between WMI/PowerShell tools and Twingate is expected on affected devices — not a Client bug

## Affected Platforms
- Windows 10 (all supported versions), Windows 11, Windows Server
- Not tied to a specific Windows build; triggered by Defender antivirus definition updates

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users blocked with `Device security not met`
- Resource access events show `Block reason: Verified device`
- Windows may display "Microsoft Defender Antivirus is turned off" notifications
- Failure persists after reboot (may or may not clear)

## Per-Device Workaround
1. Open **Windows Security → Virus & threat protection → Manage settings**
2. Toggle **Real-time protection** OFF, then back ON
3. This forces WSC to re-evaluate its reported state immediately

**Caveat:** The fix does not survive a reboot. A Security Center service restart (e.g., on reboot) may reapply the incorrect value. Repeat the toggle as needed.

## Fleet-Scale Mitigation
Per-device toggling does not scale. For large numbers of affected devices:
- Temporarily **remove the Antivirus requirement** from the affected Device Security Policy in the Admin Console
- Re-enable the requirement once Microsoft ships a Defender fix

## Gotchas
- Rebooting is **not** a reliable fix — it restarts the Security Center service but may re-apply the bad state
- Updating Microsoft Defender does **not** resolve the issue; Microsoft's advisory notes the behavior appears *after* recent Defender updates
- `Get-MpComputerStatus` showing healthy does **not** confirm the posture check will pass

## Related Docs
- Microsoft Windows release health advisory: *"Incorrect notifications that Microsoft Defender Antivirus is turned off"*
- Twingate Device Security Policy configuration (Admin Console)
---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-10-25
source_version: 77f1bdec6946d8f2fd43e91cec01c015cd58a06b4fa5cb47f6344442aa10c29c
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
A confirmed Microsoft bug causes Windows Security Center (WSC) to misreport antivirus status, causing Twingate's Antivirus posture check to fail even when Microsoft Defender is fully operational. The Twingate Client reads WSC's published value, not Defender's actual state, so the failure persists until WSC re-evaluates. No Microsoft fix date has been published (issue active as of August–September 2026).

## Key Information
- **Root cause**: WSC misreports antivirus state at service startup and retains the incorrect value indefinitely until restarted or manually triggered
- **Twingate behavior is correct**: The Client reads exactly what WSC publishes; the bug is entirely in WSC/Defender
- **Tools that show Defender as healthy** (`Get-MpComputerStatus`, `root\SecurityCenter2` WMI, Windows Security app) read a **different source** than WSC — disagreement between these and Twingate is expected on affected devices
- **Not related to**: Twingate Client version, Windows build version, or any Windows security update
- **Updating the Twingate Client does not help**

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users see `Device security not met` or `Block reason: Verified device` in Resource access events
- Defender is enabled with real-time protection on and signatures current
- Failure persists across sign-outs and Client reinstalls
- Windows may show its own false notifications that Defender is turned off

## Workaround (Per-Device)

### Toggle Real-Time Protection
1. Open **Windows Security → Virus & threat protection → Manage settings**
2. Switch **Real-time protection** off, then immediately back on
3. This forces WSC to re-evaluate and publish the correct state

**Caveats:**
- Real-time protection is briefly disabled during the toggle
- Fix does **not survive a reboot** — WSC service restart may re-apply the incorrect value
- Repeat toggle after each reboot if needed

## Fleet-Scale Recommendation
The per-device toggle does not scale. For environments with many affected devices:
- **Temporarily remove the Antivirus requirement** from the affected Device Security Policy in the Admin Console
- Re-enable the requirement once Microsoft ships the Defender fix
- This restores access without modifying endpoints

## Gotchas
- Rebooting is **not a reliable fix** — it restarts WSC but may re-apply the wrong value immediately
- Updating Microsoft Defender does **not** resolve this; Microsoft's advisory notes the issue appears *after* recent Defender updates install
- The posture check will not self-correct without manual intervention or a Microsoft fix

## Prerequisites
- Affected platforms: Windows 10 (all supported versions), Windows 11, Windows Server
- Twingate component: Client (any version)

## Related Docs
- Microsoft Windows release health advisory: *"Incorrect notifications that Microsoft Defender Antivirus is turned off"*
- Twingate Device Security Policy configuration (Admin Console)
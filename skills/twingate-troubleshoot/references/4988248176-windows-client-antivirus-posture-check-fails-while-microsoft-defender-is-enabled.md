---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-13
source_version: ffeafeee665307b185622aa23bfa4192545b8c7ac5e5ab5b38f397985d3155ed
trust: official
---

# Page Title
[Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
The Twingate Antivirus device posture check can report antivirus as not enabled even though Microsoft Defender is running normally. The cause was a Microsoft Defender platform bug that made Windows Security Center (WSC) misreport antivirus status. Microsoft fixed it in Defender platform 4.18.26080.4, so updating Defender is the resolution.

## Key Information
- **Applies to:** Twingate Client on Windows 10, Windows 11 (all supported versions), and Windows Server.
- **Affected Defender versions:** platform 4.18.26070.9 (released Aug 5, 2026) up to, but not including, 4.18.26080.4.
- **Fixed in:** 4.18.26080.4 (released Sep 17, 2026). Microsoft marked the advisory Resolved on Sep 30, 2026.
- **Not caused by:** a Windows security update, a specific Windows build, or the Twingate Client version.
- **Root cause:** WSC misreports AV status when the Security Center service starts and keeps the wrong value until the service restarts or the state is changed. The Twingate Client reads the value WSC publishes.
- **Symptoms:**
  - Users see "Device security not met", or "Block reason: Verified device" in Resource access events.
  - Defender shows real-time protection on and signatures current.
  - Windows may show false "Defender Antivirus is turned off" notifications.
  - The failure persists across sign-outs and Client reinstalls.
  - The set of affected devices can change day to day, because the bad value is sampled at service start.
- `Get-MpComputerStatus`, the `root\SecurityCenter2` WMI class, and the Windows Security app read a different source, so they often show healthy on an affected device. This disagreement is expected.

## Prerequisites
- Access to the affected devices or to your Defender/endpoint management update channel.
- Admin Console access if you need to change a Device Security Policy.

## Step-by-Step
1. Check the Defender version in PowerShell:
   `Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion`
2. Compare `AMProductVersion` to `4.18.26080.4`. Below that version, the device can still be affected.
3. Update Defender through the normal update channel. No Twingate change or Client upgrade is needed.
4. **Stopgap for a blocked device that can't update yet:**
   - Go to Windows Security > Virus & threat protection > Manage settings.
   - Turn Real-time protection off, then on again.
   - Real-time protection is briefly disabled during this. The fix may not hold after a reboot, and results have been mixed.
5. **For many devices:** roll out the Defender platform update fleet-wide through your existing management tooling instead of toggling per device.

## Configuration Values
- Target Defender platform version: `>= 4.18.26080.4`
- PowerShell fields: `AMProductVersion`, `AMEngineVersion`

## Gotchas
- Updating the Twingate Client does not help.
- The real-time protection toggle does not survive a reboot and does not scale.
- Removing the Antivirus requirement from a Device Security Policy restores access immediately but drops the check for every device on that policy. Use it only as a last resort and re-enable it once devices are on 4.18.26080.4 or later.
- Earlier guidance said updating Defender was not a fix. That is outdated, and updating is now the correct action.

## Related Docs
- Microsoft Windows release health: "Incorrect notifications that 'Microsoft Defender Antivirus is turned off'"
- Microsoft Defender for Endpoint release notes (current platform versions)
- Twingate Device Security Policy and device posture check documentation
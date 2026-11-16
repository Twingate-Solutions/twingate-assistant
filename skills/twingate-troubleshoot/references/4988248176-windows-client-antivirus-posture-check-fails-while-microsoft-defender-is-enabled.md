---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-15
source_version: 6cc229838bcfc97eb635850657ec034eb4b53b5ff67c5f6fa76f392c12bf8642
trust: official
---

# Page Title
[Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
The Twingate Antivirus device posture check can report antivirus as not enabled even though Microsoft Defender is running normally. The cause is a Microsoft issue in Defender platform 4.18.26070.9, which makes Windows Security Center (WSC) misreport status. Microsoft fixed it in platform 4.18.26080.4, so updating Defender is the resolution.

## Key Information
- Applies to the Twingate Client on Windows 10, Windows 11 (all supported versions), and Windows Server.
- Affected Defender platform versions: 4.18.26070.9 (released Aug 5, 2026) up to, but not including, 4.18.26080.4.
- Fix: 4.18.26080.4 or later (released Sept 17, 2026). Microsoft marked the advisory Resolved on Sept 30, 2026.
- Not tied to a Windows security update or a specific Windows build.
- Cause: WSC misreports AV status at service start and keeps the wrong value until the service restarts or the state is changed. The Twingate Client reads the WSC-published value.
- Symptoms:
  - Posture check fails.
  - Users see "Device security not met" or "Block reason: Verified device" in Resource access events.
  - Windows may show false "Defender is turned off" notifications.
  - The failure persists across sign-outs and Client reinstalls.
  - The set of affected devices can change day to day, because the value is sampled at each service start.
- `Get-MpComputerStatus`, the `root\SecurityCenter2` WMI class, and the Windows Security app read a different source and often show healthy. A disagreement with Twingate is expected and is not a Client bug.
- No Twingate change or Client upgrade is required.

## Prerequisites
- Access to the affected Windows device (PowerShell).
- Ability to push Defender platform updates (for fleets), or admin rights on the device.

## Step-by-Step
1. Check the platform version in PowerShell:
   `Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion`
2. Compare `AMProductVersion` to `4.18.26080.4`. Below it, the device can still be affected.
3. Update Defender through the normal update channel (see Microsoft Defender for Endpoint release notes for current platform releases).
4. Stopgap if the device can't update yet:
   - Open Windows Security > Virus & threat protection > Manage settings.
   - Switch Real-time protection off, then on.
5. For fleets, roll out the platform update through your Defender or endpoint management channel instead of toggling per device.

## Configuration Values
- Minimum fixed Defender platform: `4.18.26080.4`
- Affected range starts at: `4.18.26070.9`
- PowerShell fields: `AMProductVersion`, `AMEngineVersion`

## Gotchas
- The Real-time protection toggle is only a stopgap. Results are mixed, protection is briefly disabled, and the fix does not survive a reboot.
- Updating the Twingate Client or reinstalling it does not help.
- Removing the Antivirus requirement from the Device Security Policy restores access immediately, but it drops the check for every device on that policy. Use it as a last resort and re-enable it once devices are on 4.18.26080.4 or later.
- Earlier guidance said updating Defender was not a fix. That is outdated, and updating is now correct.

## Related Docs
- Microsoft Windows release health: "Incorrect notifications that 'Microsoft Defender Antivirus is turned off'"
- Microsoft Defender for Endpoint release notes
- Twingate Device Security Policy and posture check documentation
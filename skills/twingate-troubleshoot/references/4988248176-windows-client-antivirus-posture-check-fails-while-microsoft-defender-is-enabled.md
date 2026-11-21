---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-19
source_version: f4f012324f8d3dbd50d516baac0edef5198ad7e2146a3d7e19c3c546ee168ffd
trust: official
---

# Windows Client: Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
The Twingate Antivirus device posture check can report antivirus as not enabled even though Microsoft Defender is running normally. The cause is a Microsoft issue in which Windows Security Center (WSC) misreports antivirus status. Microsoft fixed it in Defender platform version 4.18.26080.4, so updating Defender resolves it. No Twingate change is needed.

## Key Information
- **Applies to:** Twingate Client on Windows 10, Windows 11 (all supported versions), and Windows Server.
- **Affected Defender versions:** Platform 4.18.26070.9 (released Aug 5, 2026) up to, but not including, 4.18.26080.4. The issue is not tied to a Windows build or security update.
- **Fix:** Defender platform 4.18.26080.4 or later (released Sep 17, 2026). Microsoft marked the advisory Resolved on Sep 30, 2026.
- **Symptoms:**
  - Posture check fails in the Client or Admin Console.
  - Users see "Device security not met", or "Block reason: Verified device" in Resource access events.
  - Windows may show false "Defender Antivirus is turned off" notifications.
  - The failure survives sign-outs and Client reinstalls.
  - The set of affected devices can change day to day.
- **Cause:** WSC reads the wrong antivirus state at service start and keeps it until the service restarts or the state is changed manually. Because the state is sampled at each start, the problem looks intermittent.
- **Why other tools look healthy:** `Get-MpComputerStatus`, the `root\SecurityCenter2` WMI class, and the Windows Security app read a different source than the posture check. A disagreement between them and Twingate is expected on an affected device and does not mean the Client is faulty.
- Updating the Twingate Client does not help, because the behavior is independent of Client version.

## Prerequisites
- Ability to run PowerShell on the device.
- Access to the Defender or endpoint management update channel for fleet-wide rollout.

## Resolution Steps
1. Check the Defender version:
   `Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion`
2. Compare `AMProductVersion` with `4.18.26080.4`. Anything below it can still be affected.
3. Update Defender through the normal update channel. Microsoft lists current platform releases on its Defender for Endpoint release notes page.

## Workarounds (if the device can't be updated yet)
- **Per device:** Open Windows Security > Virus & threat protection > Manage settings. Turn Real-time protection off, then on again.
  - Protection is briefly disabled while you do this.
  - Results are mixed, and the fix may be lost at the next Security Center service start, such as a reboot.
- **Fleet-wide:** Push the Defender platform update through your management tooling instead of toggling devices one by one.
- **Last resort:** Remove the Antivirus requirement from the affected Device Security Policy. This restores access immediately but drops the check for every device on the policy. Re-enable it once devices are on 4.18.26080.4 or later.

## Configuration Values
- `AMProductVersion` target: `>= 4.18.26080.4`
- Affected range: `4.18.26070.9` to just below `4.18.26080.4`
- No Twingate environment variables, CLI flags, or API parameters are involved.

## Gotchas
- Earlier guidance said updating Defender was not a fix. That guidance is outdated, and updating is now the correct action.
- Reinstalling or upgrading the Twingate Client does nothing for this issue.
- Toggling Real-time protection does not survive a reboot and does not scale.
- Healthy results from other Defender status tools do not rule out this issue.

## Related Docs
- Microsoft Windows release health: "Incorrect notifications that 'Microsoft Defender Antivirus is turned off'"
- Microsoft Defender for Endpoint release notes
- Twingate Device Security Policy and device posture check documentation
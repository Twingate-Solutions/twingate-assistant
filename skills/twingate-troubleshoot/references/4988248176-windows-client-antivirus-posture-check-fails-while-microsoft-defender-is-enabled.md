---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-22
source_version: 67fd356f83cd43f61a1d8d6d28ed6bd5b38a8a242fe431eaf238169772d798bd
trust: official
---

# Page Title
[Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

# Summary
The Twingate Antivirus device posture check can report antivirus as not enabled even though Microsoft Defender is running normally. This was a Microsoft Windows Security Center (WSC) issue, fixed in Defender platform version 4.18.26080.4. The resolution is to update Defender; no Twingate change or Client upgrade is needed.

# Key Information
- Applies to: Twingate Client on Windows 10, Windows 11 (all supported versions), and Windows Server.
- Affected Defender platform versions: between 4.18.26070.9 (released Aug 5, 2026) and 4.18.26080.4.
- Fix: platform 4.18.26080.4 or later (released Sept 17, 2026). Microsoft marked the advisory Resolved Sept 30, 2026.
- Not caused by a Windows security update or a specific Windows build.
- Cause: WSC misreports AV status when the Security Center service starts and keeps the wrong value until the service restarts or the state is changed. Twingate reads the value WSC publishes.
- Symptoms:
  - Posture check fails.
  - Users see "Device security not met" or "Block reason: Verified device" in Resource access events.
  - Defender is enabled with real-time protection on and signatures current.
  - Windows may show "Defender Antivirus is turned off" notifications.
  - Failure survives sign-out and Client reinstall.
  - Affected devices can vary day to day, so the problem looks intermittent.
- `Get-MpComputerStatus`, the `root\SecurityCenter2` WMI class, and the Windows Security app read a different source and often show healthy. This disagreement is expected and does not indicate a Client problem.

# Prerequisites
- Ability to update Microsoft Defender through the normal update channel or endpoint management.
- PowerShell access to check the version.

# Step-by-Step
1. Check the version:
   `Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion`
2. Compare `AMProductVersion` to 4.18.26080.4. Below it, the device can still be affected.
3. Update Defender to 4.18.26080.4 or later.

**Stopgap if the device can't be updated yet:**
1. Open Windows Security > Virus & threat protection > Manage settings.
2. Turn Real-time protection off, then on. Protection is briefly disabled.

**Fleet-wide:** roll out the Defender platform update through your Defender or endpoint management channel instead of toggling per device.

# Configuration Values
- Target `AMProductVersion`: ≥ 4.18.26080.4
- Known problematic version: 4.18.26070.9 up to, but not including, 4.18.26080.4

# Gotchas
- Updating the Twingate Client does not help.
- The Real-time protection toggle is per-device, gives mixed results, and may not survive a reboot (the check can fail again once the Security Center service restarts).
- Removing the Antivirus requirement from a Device Security Policy restores access immediately but drops the check for all devices on that policy. Use it only as a last resort and re-enable it once devices are on the fixed version.
- Earlier guidance said updating Defender was not a fix. That is outdated; updating is now correct.

# Related Docs
- Windows release health: Incorrect notifications that "Microsoft Defender Antivirus is turned off" (https://learn.microsoft.com/en-us/windows/release-health/status-windows-11-25H2#4956msgdesc)
- Microsoft Defender for Endpoint release notes (https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint-releases)
---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-10-11
source_version: c9fcf805db657a855b831b1a44918fbdf456928309655022c265fcdb3898c11a
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
A confirmed Microsoft bug causes Windows Security Center (WSC) to misreport Microsoft Defender's antivirus status, causing Twingate's Antivirus posture check to fail even when Defender is fully operational. The issue originated from Defender antivirus updates in August–September 2026 and persists until WSC re-evaluates. No Microsoft fix date has been published.

## Key Information
- **Root cause**: WSC misreports antivirus state at service start and retains the incorrect value until restarted or manually forced to re-evaluate
- **Twingate behavior**: Client reads WSC's published value — if WSC is wrong, the check fails regardless of actual Defender state
- **Scope**: Windows 10, Windows 11 (all supported versions), Windows Server; not tied to a specific Windows build
- **Not caused by**: Twingate Client version, Windows security updates, or actual Defender configuration issues
- **Misleading tools**: `Get-MpComputerStatus`, `root\SecurityCenter2` WMI, and the Windows Security app read a *different* source than the posture check — they may show Defender healthy while the posture check still fails; this discrepancy is expected

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users see `Device security not met` or `Block reason: Verified device` in Resource access events
- Defender is enabled with real-time protection on and signatures current
- Failure persists across sign-outs, Client reinstalls, and Client version updates

## Per-Device Workaround
1. Open **Windows Security → Virus & threat protection → Manage settings**
2. Toggle **Real-time protection** off, then back on
3. WSC re-evaluates immediately; posture check should pass

**Caveat**: The fix does not survive a reboot. The Security Center service restart on reboot may reapply the incorrect value — repeat the toggle if the check fails again after rebooting.

## Fleet-Scale Mitigation
- Per-device toggle does not scale
- If many devices are blocked: **temporarily remove the Antivirus requirement from the affected Device Security Policy** until Microsoft ships the fix, then re-enable it
- This restores access without modifying endpoints

## Gotchas
- Updating Microsoft Defender does **not** resolve the issue; Microsoft's advisory indicates the behavior appears *after* the latest Defender updates are installed
- A reboot is **not** a reliable fix — it may or may not clear the incorrect value
- Reinstalling the Twingate Client has no effect
- A disagreement between `Get-MpComputerStatus`/WMI and Twingate's posture check is **expected** on affected devices

## Related Docs
- Microsoft Windows release health: *"Incorrect notifications that Microsoft Defender Antivirus is turned off"*
- Twingate Device Security Policy configuration (Admin Console)
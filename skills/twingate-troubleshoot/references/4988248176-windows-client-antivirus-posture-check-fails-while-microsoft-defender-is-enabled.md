---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-10-18
source_version: 16edd904146f91b8224fc9bd9e799580100662a72103d2ee686b138fff429ab5
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
A confirmed Microsoft bug causes Windows Security Center (WSC) to misreport Microsoft Defender's antivirus status, causing Twingate's Antivirus posture check to fail even when Defender is fully operational. The Twingate Client reads WSC's published value, not Defender directly, so the check fails until WSC re-evaluates. No Microsoft fix date has been published (as of mid-2026).

## Key Information
- Affects Windows 10, Windows 11, and Windows Server (all supported versions)
- Triggered by Microsoft Defender antivirus updates, not Windows OS updates; not tied to a specific build
- WSC caches the incorrect status until the Security Center service restarts or state is manually toggled
- Defender continues protecting the device normally throughout
- Twingate Client updates do **not** resolve this; behavior is version-independent

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users see `Device security not met` or `Block reason: Verified device` in Resource access events
- Failure persists across sign-outs and Client reinstalls
- Windows may display spurious "Microsoft Defender Antivirus is turned off" notifications

## Why Diagnostic Tools Show Defender as Healthy
These tools read a **different source** than the posture check and will disagree on affected devices — this is expected:
- `Get-MpComputerStatus`
- `root\SecurityCenter2` WMI class
- Windows Security app

## Workaround (Per-Device)

**Toggle Real-Time Protection to force WSC re-evaluation:**

1. Open **Windows Security → Virus & threat protection → Manage settings**
2. Turn **Real-time protection** OFF
3. Turn **Real-time protection** back ON

> **Note:** Real-time protection is briefly disabled during the toggle. The fix does not survive a reboot — the incorrect state may reapply when the Security Center service restarts. Repeat the toggle if posture check fails again after reboot.

## Fleet-Scale Mitigation
The per-device toggle does not scale. If many devices are blocked:
- Temporarily **remove the Antivirus requirement** from the affected Device Security Policy in the Admin Console
- Re-enable the requirement once Microsoft ships the Defender fix

## Gotchas
- Updating Microsoft Defender may **re-trigger** the issue, not fix it
- Rebooting is **not a reliable fix** — it restarts WSC but may reapply the incorrect value
- Disagreement between `Get-MpComputerStatus`/WMI and Twingate is **expected** on affected devices; do not use those tools to validate the posture check result

## Related Docs
- Microsoft advisory: *"Incorrect notifications that Microsoft Defender Antivirus is turned off"* (Windows release health pages)
- Twingate Device Security Policy configuration (Admin Console)
---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-09-20
source_version: 0d74f2befeaac1706c79a4410f55df522a829b724d5ec4ffae7e4648ee98bf81
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
A confirmed Microsoft bug causes Windows Security Center (WSC) to misreport antivirus status, making Twingate's Antivirus posture check fail even when Microsoft Defender is running normally. The Twingate Client reads WSC's published value, not Defender directly, so the check fails until WSC re-evaluates. No Microsoft fix date has been published (issue active as of August–September 2026).

## Key Information
- **Affected components**: Twingate Client (all versions), Windows 10/11, Windows Server
- **Root cause**: WSC misreports antivirus state at service startup and retains incorrect value until service restarts or state is manually changed
- **Not caused by**: Windows security updates, specific Windows build, or Twingate Client version
- **Diagnostic confusion**: `Get-MpComputerStatus`, `root\SecurityCenter2` WMI, and Windows Security app read different sources than WSC — they may show Defender healthy while posture check fails. This discrepancy is expected.

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users blocked with "Device security not met" or `Block reason: Verified device` in Resource access events
- Microsoft Defender enabled with real-time protection on and signatures current
- Failure persists across sign-outs and Client reinstalls
- Windows may also show "Microsoft Defender Antivirus is turned off" notifications

## Workaround (Per-Device)

**Toggle Real-time Protection:**
1. Open **Windows Security > Virus & threat protection > Manage settings**
2. Turn **Real-time protection** Off
3. Turn **Real-time protection** back On

**Behavior**: Forces WSC to re-evaluate immediately. Fix persists until Security Center service next starts — may recur after reboot.

## Fleet-Scale Mitigation
If many devices are affected:
- Temporarily **remove the Antivirus requirement from the affected Device Security Policy** in the Admin Console
- Re-enable once Microsoft ships the Defender fix
- This restores access without per-device intervention

## Gotchas
- Reboot is **not a reliable fix** — restarts the Security Center service but may re-apply the incorrect value
- Updating Microsoft Defender does **not** resolve the issue; Microsoft's advisory indicates the bug appears *after* latest Defender updates install
- The per-device toggle workaround does **not survive reboots** — must be repeated if posture check fails again
- Updating the Twingate Client has no effect on this issue

## Configuration Values
- **Device Security Policy setting to modify (fleet workaround)**: Antivirus requirement toggle in Admin Console > Device Security Policy

## Related Docs
- Microsoft Windows release health: "Incorrect notifications that Microsoft Defender Antivirus is turned off"
- Twingate Device Security Policy configuration
- Twingate Resource access events (for `Block reason: Verified device` diagnosis)
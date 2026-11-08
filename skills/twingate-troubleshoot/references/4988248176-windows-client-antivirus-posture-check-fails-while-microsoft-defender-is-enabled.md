---
source: https://help.twingate.com/articles/4988248176-windows-client-antivirus-posture-check-fails-while-microsoft-defender-is-enabled
type: help
fetched: 2026-11-08
source_version: 6070a0f296dfccc7727656b858e7cebf2c1e3ab71decd3be0efffe61a8db13c4
trust: official
---

# [Windows Client] Antivirus Posture Check Fails While Microsoft Defender Is Enabled

## Summary
The Twingate Antivirus device posture check can falsely report antivirus as disabled on Windows devices even when Microsoft Defender is fully operational. This is a confirmed Microsoft bug in Defender platform versions 4.18.26070.9–4.18.26080.3, where Windows Security Center (WSC) misreports antivirus state. Microsoft shipped a fix in platform version 4.18.26080.4 (released September 17, 2026).

## Key Information
- **Root cause**: WSC samples and caches antivirus state at service startup; Twingate reads from WSC, not from `root\SecurityCenter2` WMI or `Get-MpComputerStatus`
- **Affected platform versions**: 4.18.26070.9 through below 4.18.26080.4
- **Fix version**: 4.18.26080.4 or later
- **Intermittent appearance**: Affected set of devices can change day-to-day depending on when Security Center service restarts
- **Twingate Client version is irrelevant**: Updating or reinstalling the Client does not fix this

## Symptoms
- Antivirus posture check fails in Client or Admin Console
- Users see `Device security not met` or `Block reason: Verified device` in Resource access events
- `Get-MpComputerStatus` and Windows Security app still show Defender as healthy (expected discrepancy on affected devices)
- Failure persists across sign-outs and Client reinstalls

## Prerequisites
- Windows 10/11 or Windows Server (all supported versions)
- Microsoft Defender as the active antivirus provider

## Resolution (Step-by-Step)

### 1. Check current Defender platform version
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion
```
Compare `AMProductVersion` against `4.18.26080.4`. Below that value = potentially affected.

### 2. Update Microsoft Defender
- Deploy platform update 4.18.26080.4+ through normal Defender/endpoint management update channel
- No Twingate changes required
- Reference: [Microsoft Defender for Endpoint release notes](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/release-notes)

### 3. Temporary per-device workaround (if update not yet available)
1. Open **Windows Security > Virus & threat protection > Manage settings**
2. Toggle **Real-time protection** off, then back on
- ⚠️ Stopgap only; does not survive reboot; real-time protection briefly disabled

### Fleet-scale temporary measure
- Remove the Antivirus requirement from the affected Device Security Policy to restore access immediately
- Re-enable once devices reach 4.18.26080.4+
- Do **not** use the Real-time protection toggle at scale — it is per-device and non-persistent

## Configuration Values
| Item | Value |
|---|---|
| Fixed Defender platform version | `4.18.26080.4` |
| Buggy version range | `4.18.26070.9` – `4.18.26080.3` |
| PowerShell field to check | `AMProductVersion` |

## Gotchas
- `Get-MpComputerStatus`, WMI `root\SecurityCenter2`, and Windows Security app read a **different source** than Twingate's posture check — disagreement between these tools and Twingate is expected and not a Client bug
- Toggling Real-time protection only holds until the next Security Center service restart
- Removing the Antivirus policy requirement affects **all devices** on that policy

## Related Docs
- Microsoft advisory: *Incorrect notifications that "Microsoft Defender Antivirus is turned off"* (marked Resolved September 30, 2026)
- [Microsoft Defender for Endpoint release notes](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/release-notes)
- Twingate Device Security Policy documentation
---
source: https://help.twingate.com/articles/1111227325-windows-troubleshooting-the-twingate-tap-adaptor
type: help
fetched: 2026-11-01
source_version: 9cff8952d0283c50789c9aa63864ef715c548b0c1c8258bf6673acd831a2312b
trust: official
---

# [Windows] Troubleshooting the Twingate TAP Adapter

## Summary
The Twingate TAP adapter is a required component for the Windows Client to function. If missing, misconfigured, or conflicted by third-party software, the Client will fail to start. This guide covers diagnosis and resolution steps.

## Key Information
- Affected component: Windows Twingate Client
- The TAP adapter must be present, enabled, uniquely named, and not conflicted by other VPN/tunnel software
- Log files are the primary diagnostic tool

## Prerequisites
- Windows system with Twingate Client installed
- Access to `%LOCALAPPDATA%\Twingate\logs\` log files
- Admin rights for registry edits (advanced fix only)
- Registry backup before any registry changes

## Symptoms
- Twingate Client fails to start
- `TapAdapterExistence details` + `PreconnectionFault` in `Twingate.log`
- `Twingate adapter is missing from the computer` in `Twingate.Service.log`

**Log paths:**
- `%LOCALAPPDATA%\Twingate\logs\Twingate.log`
- `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`

## Troubleshooting Checklist

1. Verify `Twingate TAP-Windows Adapter V9` network adapter is **enabled** in Windows Network Adapters
2. Confirm the adapter is **named exactly**: `Twingate TAP-Windows Adapter V9` (no variation)
3. Confirm **only one instance** of the adapter exists
4. Check for conflicting VPN/tunnel/DNS software using TAP adapters — see [Known Incompatibility Overview](https://help.twingate.com)

## Resolution Steps

1. **Uninstall incompatible software** (other VPNs or TAP-based tools)
2. **Reinstall Twingate Client:**
   - Uninstall the Twingate Client
   - Manually delete the Twingate TAP adapter
   - Reinstall the Twingate Client
3. **Registry fix (advanced):** If reinstall doesn't resolve the issue, check:
   - Path: `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000`
   - The `friendly name` value must be exactly: `Twingate TAP-Windows Adapter V9`
   - **Back up the registry before making any edits**
   - If unsure, submit a Support Request to Twingate

## Configuration Values

| Item | Expected Value |
|------|---------------|
| Adapter name | `Twingate TAP-Windows Adapter V9` |
| Registry path | `HKLM\SYSTEM\ControlSet001\Enum\ROOT\NET\0000` |
| Registry key | `friendly name` |

## Gotchas
- Registry edits are destructive if done incorrectly — always back up first
- Multiple TAP adapter instances will cause conflicts
- Third-party VPN software (e.g., OpenVPN, other TAP-based tools) can interfere even if not actively connected
- This issue is distinct from the "System Service Is Not Running" error — check that article first

## Related Docs
- [Windows Twingate Client: System Service Is Not Running](https://help.twingate.com)
- [Known Incompatibility Overview](https://help.twingate.com)
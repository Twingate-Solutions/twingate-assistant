---
source: https://help.twingate.com/articles/1111227325-windows-troubleshooting-the-twingate-tap-adaptor
type: help
fetched: 2026-09-06
source_version: 87f0c6320f012dc74517932afc622f56644461d1c95cf2479f523ab920b73296
---

# [Windows] Troubleshooting the Twingate TAP Adapter

## Summary
The Twingate TAP adapter is required for the Windows Client to function. When the adapter is missing, misconfigured, or conflicting with third-party software, the Client fails to start. This guide covers diagnosis and resolution steps.

## Key Information
- TAP adapter name must be exactly: `Twingate TAP-Windows Adapter V9`
- Log files to check:
  - `%LOCALAPPDATA%\Twingate\logs\Twingate.log`
  - `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
- Registry path involved: `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000`

## Prerequisites
- Windows Client installed
- Already attempted fix via "Windows Twingate Client: System Service Is Not Running" article
- Admin access for registry edits

## Symptoms / Diagnosis
- Client fails to start
- `Twingate.log` contains `TapAdapterExistence details` and `PreconnectionFault`
- `Twingate.Service.log` contains: `Twingate adapter is missing from the computer`

## Troubleshooting Checklist
1. Verify `Twingate TAP-Windows Adapter V9` network adapter is **enabled**
2. Verify the adapter is **named correctly** (exact string match required)
3. Verify **only one instance** of the adapter exists
4. Check for conflicting VPN, tunnel, or DNS software using a TAP adapter — see Known Incompatibility Overview

## Resolution Steps
1. Uninstall incompatible third-party software
2. Uninstall Twingate Client → manually delete the Twingate TAP adapter → reinstall Twingate Client
3. If issue persists, check registry `friendly name` at `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000`:
   - Value must be exactly: `Twingate TAP-Windows Adapter V9`
   - **Back up registry before editing**
   - Contact Twingate Support if assistance needed with registry edit

## Configuration Values
| Item | Required Value |
|------|---------------|
| Adapter name | `Twingate TAP-Windows Adapter V9` |
| Registry friendly name | `Twingate TAP-Windows Adapter V9` |

## Gotchas
- Registry edits are high-risk; always back up before modifying
- Multiple TAP adapter instances will cause failures — only one should exist
- Other VPN/tunnel software using TAP adapters can conflict; must be removed, not just disabled
- Adapter name must match exactly — spacing or capitalization differences will cause issues

## Related Docs
- Windows Twingate Client: System Service Is Not Running
- Known Incompatibility Overview
- Twingate Support Request (for registry assistance)
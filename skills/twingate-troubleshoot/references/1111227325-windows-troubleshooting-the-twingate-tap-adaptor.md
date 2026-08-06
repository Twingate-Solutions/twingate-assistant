---
source: https://help.twingate.com/articles/1111227325-windows-troubleshooting-the-twingate-tap-adaptor
type: help
fetched: 2026-08-06
source_version: 03d3e36a485b952e2cceb828a42acc5eeefe49857651d76f910076526419216f
---

# [Windows] Troubleshooting the Twingate TAP Adapter

## Summary
The Twingate TAP adapter is a required component for the Windows Client to function. This article covers diagnosis and resolution when the TAP adapter is missing, misconfigured, or conflicting with third-party software causing the Client to fail on startup.

## Key Information
- TAP adapter must be present, enabled, correctly named, and unique (only one instance)
- Issue manifests as Client startup failure after standard service troubleshooting fails
- Two log files are relevant for diagnosis

## Prerequisites
- Already attempted steps in "Windows Twingate Client: System Service Is Not Running" article
- Admin access to Windows registry (for advanced resolution)
- Registry backup completed before any regedit changes

## Diagnostic Log Locations
| Log File | Path |
|----------|------|
| Client log | `%LOCALAPPDATA%\Twingate\logs\Twingate.log` |
| Service log | `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log` |

**Error signatures to look for:**
- `Twingate.log`: `TapAdapterExistence details` + `PreconnectionFault`
- `Twingate.Service.log`: `Twingate adapter is missing from the computer`

## Troubleshooting Steps

1. **Verify adapter is enabled** — Check Network Adapters for `Twingate TAP-Windows Adapter V9` and ensure it is enabled
2. **Verify adapter name** — Must be named exactly `Twingate TAP-Windows Adapter V9`
3. **Check for duplicates** — Only one instance of `Twingate TAP-Windows Adapter V9` should exist
4. **Check for conflicts** — Remove any conflicting VPN, tunnel, or DNS software that uses a TAP adapter (see Known Incompatibility Overview)

## Resolution Steps

1. Uninstall incompatible third-party software
2. Uninstall Twingate Client → manually delete the TAP adapter → reinstall Twingate Client
3. **If still unresolved — Registry fix:**
   - Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000`
   - Verify `friendly name` value is exactly: `Twingate TAP-Windows Adapter V9`
   - Correct if mismatched
   - **Requires registry backup before editing**

## Configuration Values
- **Adapter name (exact):** `Twingate TAP-Windows Adapter V9`
- **Registry path:** `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000`
- **Registry key:** `friendly name`

## Gotchas
- Registry edits are destructive — always back up before modifying
- Name must match exactly; any variation will cause failure
- Multiple TAP adapter instances (e.g., from other VPN software) will cause conflicts
- Contact Twingate Support before attempting registry edits if unsure

## Related Docs
- Windows Twingate Client: System Service Is Not Running
- Known Incompatibility Overview
- Twingate Support Request
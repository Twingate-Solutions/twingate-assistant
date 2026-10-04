---
source: https://help.twingate.com/articles/1111227325-windows-troubleshooting-the-twingate-tap-adaptor
type: help
fetched: 2026-10-04
source_version: ed0a6bbf5ba1233ad062b021b886b8fdea4a7fcaa47050a52363999c5c4c0686
trust: official
---

# [Windows] Troubleshooting the Twingate TAP Adapter

## Summary
The Twingate TAP adapter is a required component for the Windows Client to function. If missing, misconfigured, or conflicting with third-party software, the Client will fail to start. This guide covers diagnosis and resolution steps.

## Key Information
- **Component:** Windows Client
- **Platform:** Windows only
- **TAP Adapter Name:** `Twingate TAP-Windows Adapter V9`
- **Log files to check:**
  - `%LOCALAPPDATA%\Twingate\logs\Twingate.log`
  - `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`

## Symptoms
- Twingate Client fails to start
- `TapAdapterExistence` + `PreconnectionFault` error in `Twingate.log`
- `Twingate adapter is missing from the computer` error in `Twingate.Service.log`
- Issue persists after following the "System Service Is Not Running" troubleshooting steps

## Diagnostic Checklist
1. Confirm `Twingate TAP-Windows Adapter V9` appears in Network Adapters and is **enabled**
2. Confirm the adapter name is **exactly** `Twingate TAP-Windows Adapter V9` (no typos/renaming)
3. Confirm **only one instance** of the adapter exists
4. Check for conflicting VPN, tunnel, or DNS software that also uses a TAP adapter (see [Known Incompatibility Overview](https://help.twingate.com))

## Resolution Steps

1. **Uninstall incompatible third-party software** that uses TAP adapters
2. **Reinstall Twingate Client:**
   - Uninstall the Twingate Client
   - Manually delete the Twingate TAP adapter
   - Reinstall the Twingate Client
3. **Registry fix (last resort):** If the above fails, check registry key:
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000
   ```
   - The `friendly name` value must be exactly: `Twingate TAP-Windows Adapter V9`
   - **Back up the registry before making any edits**
   - If unsure, open a Support Request with Twingate

## Gotchas
- Registry edits are high-risk; always back up before modifying
- Adapter renaming (even minor) breaks detection — name must match exactly
- Multiple TAP adapter instances cause conflicts
- Other VPN clients sharing TAP adapter infrastructure are a common root cause

## Related Docs
- Windows Twingate Client: System Service Is Not Running
- Known Incompatibility Overview
---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-09-27
source_version: e45d029d8eeef88c57b2a3f4f929531c73a06fa2c3e91dc7d6c7d48dcb0a4f4d
---

# [Windows Client] Joining Twingate Network Fails - "Unable to Join Network"

## Summary
Windows Twingate client fails to connect when it cannot locate a usable TAP adapter. The most common cause is a renamed TAP adapter `FriendlyName`, often introduced by OpenVPN or FortiClient installations (past or present).

## Key Information
- **Log locations:**
  - `%LOCALAPPDATA%\Twingate\logs\Twingate.log` (client)
  - `%PROGRAMDATA%\Twingate\logs\Twingate.Service.log` (service)
- Required adapter `FriendlyName`: `Twingate TAP-Windows Adapter V9` (exact string)
- OpenVPN adapter name (`TAP-Windows Adapter V9`) differs only by the `Twingate ` prefix — easy to miss
- Removing conflicting VPN software does **not** automatically restore the correct name

## Causes
- TAP adapter is disabled
- TAP adapter is absent/missing
- TAP adapter `FriendlyName` was renamed (commonly by OpenVPN or FortiClient)

## Step-by-Step Resolution

### 1. Verify adapter exists and is enabled
```powershell
Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' | Select-Object Name, InterfaceDescription, Status
```
- If greyed out in Network Connections UI: right-click → **Enable**

### 2. Check adapter FriendlyName in registry
```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' | Select-Object PSChildName, FriendlyName, DeviceDesc
```
- Note the `PSChildName` (key index) — **not always `0000`**
- Confirm `FriendlyName` reads exactly: `Twingate TAP-Windows Adapter V9`

### 3. Correct the FriendlyName
```cmd
# Backup first (substitute correct index)
reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg

# Then set FriendlyName via regedit or reg add
```
- Uninstall any conflicting VPN software cleanly before editing
- Reboot after correction

### 4. If still failing
- Reinstall the Twingate Client
- If unresolved, contact support with both log files

## Configuration Values
| Item | Value |
|------|-------|
| Required `FriendlyName` | `Twingate TAP-Windows Adapter V9` |
| Registry path | `HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\<index>` |

## Gotchas
- The index key (`PSChildName`) is **not always `0000`** — verify before editing registry
- Uninstalling OpenVPN/FortiClient does not restore the adapter name automatically
- The name difference between OpenVPN and Twingate adapters is a single prefix word — compare full strings
- A machine may show this error with **no VPN currently installed**

## Related Docs
- Twingate Windows Client logs: `%LOCALAPPDATA%\Twingate\logs`, `%PROGRAMDATA%\Twingate\logs`
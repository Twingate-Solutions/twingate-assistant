---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-10-18
source_version: d3c0b1c343d774c54b3a8242cfd9ac9ed96bf17aa7b971d9040aa805c345c28b
trust: official
---

# [Windows Client] Joining Twingate Network Fails with "Unable to join network"

## Summary
On Windows, Twingate fails to connect when it cannot locate a usable TAP adapter. The most common cause is the adapter's `FriendlyName` being renamed (often by OpenVPN or FortiClient), though the adapter may also be disabled or absent entirely.

## Key Information
- Error appears in two log files simultaneously
- Root cause: TAP adapter missing, disabled, or incorrectly named
- The name difference between OpenVPN and Twingate adapters is a single prefix: `Twingate TAP-Windows Adapter V9` vs `TAP-Windows Adapter V9`
- Removing conflicting VPN software does **not** automatically restore the correct adapter name

## Log File Locations
| Log File | Path |
|---|---|
| `Twingate.log` | `%LOCALAPPDATA%\Twingate\logs` |
| `Twingate.Service.log` | `%PROGRAMDATA%\Twingate\logs` |

## Diagnostic & Resolution Steps

**1. Verify adapter exists and is enabled**
```powershell
Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' | Select-Object Name, InterfaceDescription, Status
```
If greyed out in Network Connections UI: right-click → **Enable**, then retry.

**2. Check adapter FriendlyName in registry**
```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' | Select-Object PSChildName, FriendlyName, DeviceDesc
```
Expected value: `Twingate TAP-Windows Adapter V9` (exact match required). Note the `PSChildName` index (not always `0000`).

**3. Correct the FriendlyName if wrong**
- Uninstall conflicting VPN software first if present
- Back up the registry key (substitute actual index):
  ```
  reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg
  ```
- Set `FriendlyName` to `Twingate TAP-Windows Adapter V9` using the correct index from step 2
- Reboot

**4. If still failing**
Reinstall the Twingate Client. If unresolved, contact support with both log files attached.

## Gotchas
- `PSChildName` index is **not always `0000`** — confirm with step 2 before editing registry
- Machines with no VPN currently installed can still exhibit this issue if a prior VPN renamed the adapter
- Do a full string comparison — scanning for `TAP-Windows Adapter V9` will miss the `Twingate` prefix
- Always back up the registry key before editing

## Related Docs
- Twingate Windows Client installation
- Twingate support contact (attach both log files when escalating)
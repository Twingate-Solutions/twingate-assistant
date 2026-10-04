---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-10-04
source_version: ad2535b6480fee5505e7d3688d9c2567a74369ce5c32001f3c9526dad057da1c
trust: official
---

# [Windows Client] Joining Twingate Network Fails with "Unable to join network"

## Summary
On Windows, Twingate fails to connect when the TAP adapter is missing, disabled, or has an incorrect `FriendlyName`. The most common cause is a renamed TAP adapter resulting from other VPN software (e.g., OpenVPN, FortiClient) that altered or conflicts with the adapter name.

## Key Information
- Error appears in two log files simultaneously
- Root cause: Twingate service cannot locate a usable TAP adapter named exactly `Twingate TAP-Windows Adapter V9`
- OpenVPN's adapter is named `TAP-Windows Adapter V9` (missing "Twingate" prefix) — easy to confuse
- Uninstalling conflicting VPN software does **not** automatically restore the correct adapter name
- Registry key index is **not** always `0000` — must be verified

## Log File Locations
| Log File | Path |
|---|---|
| `Twingate.log` | `%LOCALAPPDATA%\Twingate\logs` |
| `Twingate.Service.log` | `%PROGRAMDATA%\Twingate\logs` |

## Prerequisites
- Administrator/elevated PowerShell for registry and adapter commands
- Back up registry key before editing

---

## Step-by-Step Resolution

### 1. Check adapter exists and is enabled
```powershell
Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' |
  Select-Object Name, InterfaceDescription, Status
```
If greyed out in Network Connections UI: right-click → **Enable**, then retry.

### 2. Check adapter FriendlyName in registry
```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' |
  Select-Object PSChildName, FriendlyName, DeviceDesc
```
- `FriendlyName` must be exactly: `Twingate TAP-Windows Adapter V9`
- Note the `PSChildName` value (the key index, e.g., `0000`, `0001`) — needed for step 3

### 3. Correct the FriendlyName (if wrong)
1. Uninstall any conflicting VPN software first
2. Back up the registry key (substitute correct index):
   ```
   reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg
   ```
3. Set `FriendlyName` to `Twingate TAP-Windows Adapter V9` using Registry Editor or `reg add`
4. Reboot

### 4. If still failing
Reinstall the Twingate Windows Client. If unresolved, contact support with both log files attached.

---

## Gotchas
- The adapter index in the registry path (`ROOT\NET\0000`) varies — do not assume `0000`
- Removing OpenVPN/FortiClient may leave the renamed adapter behind with no visible other VPN installed
- Name comparison must be exact — scanning for partial string `TAP-Windows Adapter V9` will miss the missing `Twingate` prefix

## Related Docs
- Twingate Windows Client installation
- Twingate support contact (include both log files when escalating)
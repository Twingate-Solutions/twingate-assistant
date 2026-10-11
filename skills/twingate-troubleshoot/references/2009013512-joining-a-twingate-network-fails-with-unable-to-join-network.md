---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-10-11
source_version: 6a6d5b2cdc5af770d18aece010a9af080599fa9efb87079f104994026ce5fdb8
trust: official
---

# [Windows Client] Joining Twingate Network Fails with "Unable to join network"

## Summary
On Windows, Twingate fails to connect when it cannot locate a usable TAP adapter. The most common cause is a renamed adapter `FriendlyName`, often caused by OpenVPN or FortiClient installations changing or conflicting with the adapter name.

## Key Information
- Error occurs during preconnection checks before the network join completes
- Twingate requires adapter `FriendlyName` to be exactly `Twingate TAP-Windows Adapter V9`
- OpenVPN's adapter is named `TAP-Windows Adapter V9` (no "Twingate" prefix) — easy to confuse
- Uninstalling conflicting VPN software does **not** automatically restore the correct name

## Log File Locations
| File | Path |
|------|------|
| `Twingate.log` | `%LOCALAPPDATA%\Twingate\logs` |
| `Twingate.Service.log` | `%PROGRAMDATA%\Twingate\logs` |

**Error signatures:**
- Client log: `Preconnection check failed. TapAdapterExistence details: Twingate`
- Service log: `Twingate adapter is missing from the computer`

## Step-by-Step Resolution

### 1. Verify adapter exists and is enabled
```powershell
Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' | Select-Object Name, InterfaceDescription, Status
```
If greyed out in Network Connections UI: right-click → **Enable**, then retry.

### 2. Check adapter FriendlyName in registry
```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' | Select-Object PSChildName, FriendlyName, DeviceDesc
```
- `FriendlyName` must be exactly `Twingate TAP-Windows Adapter V9`
- Note the `PSChildName` value (the key index — not always `0000`)

### 3. Correct the FriendlyName (registry edit)
```cmd
reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg
```
Replace `0000` with the actual index from Step 2. Then set `FriendlyName` to `Twingate TAP-Windows Adapter V9` and **reboot**.

### 4. If still failing
Reinstall the Twingate Client. If unresolved, contact support with both log files attached.

## Gotchas
- The index key in `ROOT\NET\` is **not always `0000`** — always verify with Step 2 before editing
- Conflicting software (OpenVPN, FortiClient) may leave behind a renamed adapter even after uninstall
- Always back up the registry key before editing
- Uninstall any no-longer-needed TAP-based VPN software cleanly before renaming

## Related Docs
- Twingate Windows Client installation
- Twingate support contact (include both log files when escalating)
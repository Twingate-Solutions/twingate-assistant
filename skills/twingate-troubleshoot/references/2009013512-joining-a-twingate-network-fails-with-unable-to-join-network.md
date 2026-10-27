---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-10-25
source_version: bc9e20e7a49f7019021b55a0db632adbb96f201ba622fffb37d0b2fad9b1a930
trust: official
---

# [Windows Client] Joining Twingate Network Fails: "Unable to join network"

## Summary
On Windows, Twingate fails to connect when it cannot locate a usable TAP adapter. The most common cause is the adapter's `FriendlyName` being incorrect, often due to interference from other TAP-based VPN software like OpenVPN or FortiClient.

## Key Information
- Error appears as "Unable to join network" in the client UI
- Root cause: missing, disabled, or misnamed TAP adapter
- Critical naming distinction: Twingate's adapter is **`Twingate TAP-Windows Adapter V9`**; OpenVPN's is **`TAP-Windows Adapter V9`** — differs only by the `Twingate ` prefix
- Uninstalling conflicting VPN software does **not** automatically restore the correct adapter name

## Log File Locations
| File | Path |
|---|---|
| `Twingate.log` | `%LOCALAPPDATA%\Twingate\logs` |
| `Twingate.Service.log` | `%PROGRAMDATA%\Twingate\logs` |

## Diagnostic Errors
- `Twingate.log`: `Preconnection check failed. TapAdapterExistence`
- `Twingate.Service.log`: `Twingate adapter is missing from the computer`

## Resolution Steps (in order)

**1. Verify adapter exists and is enabled**
```powershell
Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' | Select-Object Name, InterfaceDescription, Status
```
If greyed out in Network Connections UI: right-click → **Enable**, then retry.

**2. Check adapter FriendlyName in registry**
```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' | Select-Object PSChildName, FriendlyName, DeviceDesc
```
- `FriendlyName` must be exactly: `Twingate TAP-Windows Adapter V9`
- Note the `PSChildName` value (registry key index) — it is **not always `0000`**

**3. Correct the FriendlyName if wrong**
```powershell
# Backup first (substitute correct index for 0000)
reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg
```
Then set `FriendlyName` to `Twingate TAP-Windows Adapter V9` using the index from step 2, then **reboot**.

**4. If still failing**
Reinstall the Twingate Client. If unresolved, contact support with both log files attached.

## Gotchas
- The name difference between OpenVPN and Twingate adapters is a single word prefix — easy to miss on visual scan
- A machine may show no other VPN installed yet still have the renamed adapter persisting in the registry
- Always note the correct registry key index from step 2 before editing — do not assume `0000`
- Back up the registry key before making changes

## Related Docs
- Twingate Windows Client installation
- Twingate support contact (provide both log files)
---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-11-22
source_version: 48c1ed7484f03e7bb6e678acc294039c531f6df0436598936738c2b11d1d6d62
trust: official
---

# [Windows Client] Joining a Twingate network fails with "Unable to join network"

## Summary
On Windows, joining a Twingate network can fail because the Twingate service cannot find a usable TAP adapter. The adapter may be disabled, missing, or have a renamed `FriendlyName`, which is often caused by other TAP-based software such as OpenVPN or FortiClient.

## Key Information
- **Symptom logs**
  - `Twingate.log` (`%LOCALAPPDATA%\Twingate\logs`): `Preconnection check failed. TapAdapterExistence details`
  - `Twingate.Service.log` (`%PROGRAMDATA%\Twingate\logs`): `PreconnectionException: Twingate adapter is missing from the computer`
- **Causes** (any one triggers the error):
  - Adapter disabled
  - Adapter absent
  - Adapter `FriendlyName` changed from `Twingate TAP-Windows Adapter V9`
- The rename is commonly seen where OpenVPN, FortiClient, or other TAP software is or was installed.
- OpenVPN's adapter is `TAP-Windows Adapter V9`, and Twingate's is `Twingate TAP-Windows Adapter V9`. Compare the full string.
- Removing the other software does not necessarily restore the name. This can occur even with no other VPN installed and no other TAP adapter visible.

## Prerequisites
- Windows machine with the Twingate Client installed
- Administrator rights (needed for registry edits)
- Access to both log files

## Step-by-Step
Work in order. Use the registry step only if steps 1 and 2 don't resolve it.

1. **Check the adapter exists and is enabled**
   - Go to Control Panel > Network and Internet > Network and Sharing Center > Change adapter settings.
   - If the Twingate adapter is greyed out, right-click > Enable and retry.
   - Or run:
     ```powershell
     Get-NetAdapter | Where-Object InterfaceDescription -like '*Twingate*' |
       Select-Object Name, InterfaceDescription, Status
     ```
2. **Check the adapter's name**
   ```powershell
   Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Enum\ROOT\NET\*' |
     Select-Object PSChildName, FriendlyName, DeviceDesc
   ```
   - `FriendlyName` must read exactly `Twingate TAP-Windows Adapter V9`.
   - Note the `PSChildName` of that entry. It is the key index used below and is not always `0000`.
3. **Correct the name**
   - If another VPN is still installed and no longer needed, uninstall it as cleanly as possible first.
   - Back up the key:
     ```
     reg export "HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\0000" tap-backup.reg
     ```
   - Set `FriendlyName` to `Twingate TAP-Windows Adapter V9`, substituting the index from step 2.
   - Reboot.
4. **If it still fails**
   - Reinstall the Twingate Client.
   - If that doesn't help, contact support with both log files.

## Configuration Values
- Registry path: `HKLM\SYSTEM\CurrentControlSet\Enum\ROOT\NET\<index>`
- Registry value: `FriendlyName` = `Twingate TAP-Windows Adapter V9`
- Log locations: `%LOCALAPPDATA%\Twingate\logs`, `%PROGRAMDATA%\Twingate\logs`

## Gotchas
- The near-identical names are easy to confuse. Don't match on a substring.
- The registry key index varies. Don't assume `0000`, and substitute the correct index in the `reg export` command.
- Back up the key before editing.
- The name may stay wrong after other VPN software is removed.

## Related Docs
- None linked in the source.
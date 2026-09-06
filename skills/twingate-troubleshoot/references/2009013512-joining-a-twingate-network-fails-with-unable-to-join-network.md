---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-09-06
source_version: 1d1759cba54680b363ead10d6123f7c15b40f209664b1e98fa44d2ed2e46d072
---

# Joining Twingate Network Fails with "Unable to Join Network"

## Summary
On Windows, Twingate fails to connect when a TAP adapter exists but has an incorrect `FriendlyName` (set by another VPN application). The Twingate service cannot locate its TAP adapter despite it being present, and reinstalling Twingate does not resolve this.

## Key Information
- Affects Windows OS only
- Occurs when another VPN application (past or present) has claimed/renamed the TAP adapter
- Twingate requires its TAP adapter `FriendlyName` to be exactly `Twingate TAP-Windows Adapter V9`
- Registry edit + reboot resolves the issue; reinstall alone does not

## Symptoms
- Network join fails with "Unable to join network"
- No other VPN currently installed
- TAP adapter appears in interface list but with wrong description
- `Twingate.log` error: `PreconnectionFault` / `TapAdapterExistence`
- `Twingate.Service.log` error: `Twingate adapter is missing from the computer`

## Prerequisites
- Registry backup completed before making changes
- Administrative access to Windows Registry Editor
- Other VPN software fully uninstalled (if still present)

## Step-by-Step Resolution

1. **Uninstall conflicting VPN** (if still installed) as cleanly as possible
2. **Back up the Windows Registry** before proceeding
3. Open Registry Editor and navigate to:
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000
   ```
4. Locate the `FriendlyName` value and change it to:
   ```
   Twingate TAP-Windows Adapter V9
   ```
5. **Reboot** the computer

## Configuration Values

| Item | Value |
|------|-------|
| Registry path | `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000` |
| Registry key | `FriendlyName` |
| Required value | `Twingate TAP-Windows Adapter V9` |

## Gotchas
- The TAP adapter `\ROOT\NET\0000` key number (`0000`) may differ if multiple network adapters are present — verify you're editing the correct adapter entry
- Reinstalling Twingate or cleaning the registry of Twingate entries alone will **not** fix this issue
- Always back up the registry before editing; incorrect changes can break Windows networking
- Previous VPN software (even if uninstalled) can leave a renamed TAP adapter behind

## Related Docs
- Twingate Windows client troubleshooting
- Twingate TAP adapter installation requirements
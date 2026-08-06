---
source: https://help.twingate.com/articles/2009013512-joining-a-twingate-network-fails-with-unable-to-join-network
type: help
fetched: 2026-08-06
source_version: 19b1e8b0c32694b0af6511cd612a7393ac8e65eefbc5140b0e9f6315eb8beaf9
---

# Joining Twingate Network Fails: "Unable to join network"

## Summary
On Windows, joining the Twingate network fails when the TAP adapter exists but has an incorrect `FriendlyName` (caused by another VPN's TAP adapter overwriting the registry entry). Reinstalling Twingate or cleaning the registry does not resolve this issue.

## Key Information
- Affects Windows OS only
- TAP adapter is present in the interface list but has a wrong description
- Root cause: another VPN application (current or previously installed) has claimed/renamed the TAP adapter registry entry
- Twingate service identifies its adapter by `FriendlyName` = `Twingate TAP-Windows Adapter V9`

## Symptoms
- Network join fails with "Unable to join network"
- No other VPN currently installed (but may have been previously)
- `Twingate.log` shows: `PreconnectionFault` / `TapAdapterExistence` error
- `Twingate.Service.log` shows: `Twingate adapter is missing from the computer`

## Prerequisites
- Registry editor access (admin privileges)
- Registry backup completed before making changes

## Step-by-Step Resolution

1. **Uninstall conflicting VPN** (if still installed) as cleanly as possible
2. **Back up the Windows registry** before making changes
3. **Open Registry Editor** and navigate to:
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\ROOT\NET\0000
   ```
4. **Update `FriendlyName` value** to exactly:
   ```
   Twingate TAP-Windows Adapter V9
   ```
5. **Reboot** the computer

## Configuration Values

| Registry Path | Key | Required Value |
|---|---|---|
| `HKLM\SYSTEM\ControlSet001\Enum\ROOT\NET\0000` | `FriendlyName` | `Twingate TAP-Windows Adapter V9` |

## Gotchas
- The TAP adapter *appears* present in the interface list — this is misleading; the issue is the adapter name mismatch, not a missing adapter
- Reinstalling Twingate and registry cleanup **do not fix** this issue
- The `0000` key may vary if multiple NET adapters exist — verify it corresponds to the Twingate TAP adapter
- Always back up the registry before editing

## Related Docs
- Twingate Windows client troubleshooting
- TAP adapter installation issues
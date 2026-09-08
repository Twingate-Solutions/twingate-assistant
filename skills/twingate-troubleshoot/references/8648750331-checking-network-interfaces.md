---
source: https://help.twingate.com/articles/8648750331-checking-network-interfaces
type: help
fetched: 2026-09-06
source_version: 38351a0570d6ad147840c0f6f531a8b7128890d6f67f58e4d5c7cfc70ccdc28a
---

# Checking Network Interfaces

## Summary
The Twingate Client creates a dedicated network adapter during installation that is required for proper operation. This guide covers how to verify the Twingate network interface exists on macOS and Windows devices. If the interface is missing, reinstallation is required.

## Key Information
- Twingate installs its own network adapter on end-user devices during client installation
- The network interface is created automatically during installation
- Missing interface = client cannot function; reinstall to recreate it
- Two possible healthy states: connected or disconnected (both indicate adapter exists)

## Prerequisites
- Twingate Client installed on device
- Terminal (macOS) or CMD (Windows) access

## Step-by-Step

### macOS
1. Open Terminal
2. Run:
   ```bash
   networksetup -showpppoestatus "Twingate"
   ```
3. Interpret output:
   - `disconnected` → adapter exists, not connected ✓
   - `connected` → adapter exists and connected ✓
   - *(empty response)* → adapter missing, reinstall required ✗

### Windows
1. Open CMD
2. Run:
   ```cmd
   ipconfig | findstr "Twingate"
   ```
3. Interpret output:
   - `Unknown adapter Twingate:` → adapter exists ✓
   - *(empty response)* → adapter missing, reinstall required ✗

## Gotchas
- Empty/no output on either platform means the network interface was removed — reinstall the Twingate Client to recreate it
- On macOS, the command uses PPPoE status check; "disconnected" is a valid/healthy state
- Windows output shows "Unknown adapter" — this is expected and not an error

## Related Docs
- [Twingate Troubleshooting Guide](https://help.twingate.com/articles/8648750331-checking-network-interfaces) (parent guide linked at bottom of page)
- Twingate Client installation documentation
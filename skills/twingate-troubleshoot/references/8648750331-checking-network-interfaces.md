---
source: https://help.twingate.com/articles/8648750331-checking-network-interfaces
type: help
fetched: 2026-08-06
source_version: 49f8a2963d63c04acdc7d0211cc60b3c2552682d67ce7dca93be9a26a33667df
---

# Checking Network Interfaces

## Page Title
Checking Network Interfaces

## Summary
The Twingate Client installs its own network adapter on end-user devices during installation. If this adapter is missing or removed, the client cannot function. This guide provides commands to verify the network interface exists on macOS and Windows.

## Key Information
- Twingate creates a dedicated network adapter during client installation
- Missing network interface = client cannot function
- Fix for missing interface: reinstall the Twingate Client
- Two possible healthy states: `connected` or `disconnected`

## Prerequisites
- Twingate Client installed (or attempting to verify why it isn't working)
- Terminal access (macOS) or CMD access (Windows)

## Step-by-Step

### macOS
```bash
networksetup -showpppoestatus "Twingate"
```
**Expected outputs:**
- `disconnected` — adapter exists, not connected
- `connected` — adapter exists, connected
- *(empty response)* — adapter missing, reinstall required

### Windows
```cmd
ipconfig | findstr "Twingate"
```
**Expected output:**
- `Unknown adapter Twingate:` — adapter exists
- *(empty response)* — adapter missing, reinstall required

## Gotchas
- An empty response does **not** mean the command failed — it means the interface is missing
- Reinstalling the Twingate Client is the remediation for a missing interface; no manual adapter creation steps are provided
- macOS command uses PPPoE status check specifically for the `"Twingate"` named interface

## Related Docs
- Twingate Troubleshooting Guide (parent document linked as "Back to troubleshooting guide")
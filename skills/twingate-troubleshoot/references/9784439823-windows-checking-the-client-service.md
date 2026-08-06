---
source: https://help.twingate.com/articles/9784439823-windows-checking-the-client-service
type: help
fetched: 2026-08-06
source_version: c3ba7a9b9b04feb9cb160d892dcd323644d61f258a1b53bcf081805bc6385a5a
---

# [Windows] Checking the Client Service

## Summary
The Twingate Windows Client depends on a local Windows service ("Twingate Service") to function, including supporting Start Before Logon. If the service is not running, the client will not work and must be started or the client reinstalled.

## Key Information
- Windows Twingate Client runs a background service named **"Twingate Service"**
- Service must be in **Running** status for the client to function
- Service enables **Start Before Logon** capability on Windows

## Prerequisites
- Twingate Client installed on Windows
- Access to Windows Services manager or CMD prompt

## Step-by-Step

1. Open Services manager — run `services.msc` in a CMD window
2. Scroll the list to find **"Twingate Service"**
3. Check status column — confirm it shows **Running**
4. If not running, right-click and **Start** the service
5. If service is missing entirely, **reinstall the Twingate Client**

## Troubleshooting / Gotchas
- If "Twingate Service" cannot be located, reinstallation is required — the service entry is not separately repairable
- Check **Event Viewer** and **Twingate Client logs** for additional diagnostic information when service is missing or fails to start
- Missing service likely indicates a corrupted or incomplete installation

## Configuration Values
| Item | Value |
|------|-------|
| Service name (display) | `Twingate Service` |
| Services MMC command | `services.msc` |

## Related Docs
- Twingate Client logs (Windows)
- Start Before Logon documentation
- Twingate Windows Client installation guide
- Twingate troubleshooting guide
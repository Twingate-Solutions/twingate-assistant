---
source: https://help.twingate.com/articles/9784439823-windows-checking-the-client-service
type: help
fetched: 2026-09-06
source_version: 04a5c8556cc4fdcd355c2d0cd5d3c372169f2934c5ed2b74988264078cde5cc2
---

# [Windows] Checking the Client Service

## Summary
The Twingate Windows Client relies on a local Windows service ("Twingate Service") to function, including supporting Start Before Logon. If this service is not running, the client will not work and must be started or the client reinstalled.

## Key Information
- The Windows Twingate Client uses a background Windows service named **Twingate Service**
- Service must be in **Running** status for the client to function
- Service enables the **Start Before Logon** feature on Windows

## Prerequisites
- Windows OS with Twingate Client installed
- Access to Windows Services manager or CMD

## Step-by-Step

1. Open Services manager — run the following in a CMD window:
   ```
   services.msc
   ```
2. Scroll the list to find **Twingate Service**
3. Check the **Status** column — it must show **Running**
4. If not running, right-click the service and select **Start**
5. If **Twingate Service** is not listed at all → reinstall the Twingate Client

## Gotchas
- If the service is missing entirely, reinstallation is required — starting it is not an option
- Check **Event Viewer** and **Twingate Client logs** for root cause if service is missing or fails to start
- Simply restarting the visible client UI is insufficient if the underlying service is stopped

## Related Docs
- Twingate Windows Client installation guide
- Twingate Client logs (Windows)
- Windows Event Viewer troubleshooting
- Start Before Logon feature documentation
- Twingate Windows troubleshooting guide
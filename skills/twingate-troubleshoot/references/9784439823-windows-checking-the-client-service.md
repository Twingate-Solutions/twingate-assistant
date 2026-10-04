---
source: https://help.twingate.com/articles/9784439823-windows-checking-the-client-service
type: help
fetched: 2026-10-04
source_version: dadb01b0687d392bed1a666acb0c08b1e57d86b835394d125b7b85735efef86e
trust: official
---

# [Windows] Checking the Client Service

## Summary
The Twingate Windows Client relies on a local Windows service ("Twingate Service") to function, enabling features like Start Before Logon. If the service is not running, the client will not work. This guide covers how to verify and start the service.

## Key Information
- Windows Twingate Client uses a background Windows service
- Service enables **Start Before Logon** functionality
- Service must be in **Running** status for the client to operate

## Prerequisites
- Twingate Client installed on Windows
- Access to Windows Services manager or CMD

## Step-by-Step

1. Open Services manager — run the following in a CMD window:
   ```
   services.msc
   ```
2. Scroll the list to find **Twingate Service**
3. Check the **Status** column:
   - If **Running** → no action needed
   - If not running → right-click and select **Start**
4. If **Twingate Service** is not listed at all → reinstall the Twingate Client

## Troubleshooting If Service Is Missing

- Reinstall the Twingate Client
- Check **Event Viewer** for Windows-level errors
- Review **Twingate Client logs** for additional detail

## Gotchas
- Simply relaunching the client UI will not fix a stopped/missing service — the service must be started independently via `services.msc`
- A missing service entry (not just stopped) indicates a broken install; reinstallation is required rather than a simple restart

## Related Docs
- Twingate Windows Client installation guide
- Twingate Client logs (troubleshooting)
- Start Before Logon feature documentation
- Twingate Windows troubleshooting guide
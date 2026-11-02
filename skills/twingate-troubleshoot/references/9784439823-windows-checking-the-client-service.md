---
source: https://help.twingate.com/articles/9784439823-windows-checking-the-client-service
type: help
fetched: 2026-11-01
source_version: dbe7230bb71cbc671fd779646b6bfb4679b59bf613ae1877e25b130a928d592d
trust: official
---

# [Windows] Checking the Client Service

## Summary
The Twingate Windows Client relies on a local Windows service ("Twingate Service") to function, including for Start Before Logon support. If this service is not running, the client will not work. This page covers how to verify and start the service.

## Key Information
- The Twingate Windows Client requires a background Windows service named **Twingate Service**
- The service enables **Start Before Logon** functionality
- Service must be in **Running** status for the client to operate

## Prerequisites
- Twingate Client installed on Windows
- Access to Windows Services console or CMD

## Step-by-Step

1. Open the Services console — run the following in a CMD window:
   ```
   services.msc
   ```
2. Scroll the list to find **Twingate Service**
3. Check that its status is **Running**
4. If not running, right-click → **Start**
5. If **Twingate Service** is not listed at all, reinstall the Twingate Client

## Gotchas
- If the service is missing entirely (not just stopped), reinstallation is required — starting or restarting will not help
- After confirming service state, check **Event Viewer** and **Twingate Client logs** for deeper troubleshooting if issues persist
- A stopped service will silently prevent all Twingate connectivity without obvious UI errors

## Related Docs
- Twingate Windows Client installation guide
- Twingate Client logs (Windows)
- Windows Event Viewer
- Start Before Logon documentation
- [Twingate Windows troubleshooting guide](https://help.twingate.com)
---
source: https://help.twingate.com/articles/2020664128-windows-client-system-service-is-not-running
type: help
fetched: 2026-09-06
source_version: e069dea8a9bae2d9bf6164c8c5945a814d3f2ddbd6d5ca90251c61fc1850ce4b
---

# [Windows Client] System Service Is Not Running

## Summary
The Twingate Windows Client requires the "Twingate Service" Windows service to be running. If stopped or missing, the client cannot establish connectivity and displays an error. Resolution involves starting the service and setting it to automatic startup.

## Key Information
- Error message: *"The Twingate system service is not running. To connect, restart the Twingate system service or contact your admin."*
- Affected component: Windows Client
- Dependency: Twingate TAP network adapter must be present and enabled
- Service name in services.msc: **Twingate Service rc**

## Prerequisites
- Windows OS with Twingate Client installed
- Access to `services.msc` (may require admin rights)
- Twingate TAP network adapter installed and not disabled

## Troubleshooting Steps

1. Press **Win + R**, type `services.msc`, press Enter
2. Scroll to **Twingate Service** in the list
3. Check status:
   - **Not running** → proceed to Resolution
   - **Running + Automatic** → restart the service, restart the client app, retry connection
   - **Fails to start** → verify TAP adapter is present/enabled; collect detailed logs and contact Twingate Support

## Resolution Steps

1. Press **Win + R**, type `services.msc`, press Enter
2. Scroll to **Twingate Service rc**
3. Right-click → **Start**
4. Right-click → **Properties** → set **Startup Type** to **Automatic**

## Gotchas
- The service name shown during troubleshooting is "Twingate Service" but the actual entry in services.msc is **"Twingate Service rc"** — scroll carefully
- If the service fails to start even after manual attempt, check the TAP adapter first before opening a support ticket
- Setting startup type to Automatic prevents recurrence after reboots

## Related Docs
- Twingate detailed logs collection (referenced but not linked)
- Twingate Support ticket submission
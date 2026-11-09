---
source: https://help.twingate.com/articles/2020664128-windows-client-system-service-is-not-running
type: help
fetched: 2026-11-08
source_version: 963d9e0987e5b6c0e905222cd644cc8cd88ce484834d58a2784a25b9062230ce
trust: official
---

# [Windows Client] System Service Is Not Running

## Summary
The Twingate Windows Client requires the **Twingate Windows Service** to be running to establish connectivity. If the service is stopped or missing, the client will display an error and fail to connect. Resolution involves starting the service and setting it to automatic startup.

## Key Information
- Error message: *"The Twingate system service is not running. To connect, restart the Twingate system service or contact your admin."*
- Affects: Windows platform, Twingate Client component
- Root cause: `Twingate Service rc` Windows service is stopped or not set to automatic

## Prerequisites
- Windows OS with Twingate Client installed
- Access to `services.msc` (may require local admin privileges to start services)

## Step-by-Step

### Diagnose
1. Press `Win + R`, type `services.msc`, press Enter
2. Scroll to **Twingate Service**
3. Check status — if null/not running, proceed to resolution

### Resolve
1. Press `Win + R`, type `services.msc`, press Enter
2. Scroll to **Twingate Service rc**
3. Right-click → **Start**
4. Right-click → **Properties** → set **Startup Type** to `Automatic`
5. Restart the Twingate Client application and attempt reconnection

## Gotchas
- If the service is already running but connection still fails: restart the service, restart the client app, then retry
- If the service **fails to start**: check that the **Twingate TAP network adapter** is present and not disabled in Device Manager
- If TAP adapter check doesn't resolve the issue: collect detailed logs and open a support ticket — do not attempt further self-service

## Configuration Values
| Setting | Value |
|---|---|
| Service name | `Twingate Service rc` |
| Startup Type | `Automatic` |
| Services console | `services.msc` |

## Related Docs
- Twingate detailed logs collection (referenced in source, link not provided)
- Twingate Support ticket submission
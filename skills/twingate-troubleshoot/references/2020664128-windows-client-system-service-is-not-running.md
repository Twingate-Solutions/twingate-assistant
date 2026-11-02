---
source: https://help.twingate.com/articles/2020664128-windows-client-system-service-is-not-running
type: help
fetched: 2026-11-01
source_version: 7a98300f96210914b6b1d529b4d2f35954cfe1ac44d539500d79d9157c55a047
trust: official
---

# [Windows Client] System Service Is Not Running

## Summary
The Twingate Windows Client requires the **Twingate Windows Service** to be running to establish connectivity. If the service is stopped or missing, the client will display an error and fail to connect. This article covers diagnosis and resolution steps via Windows Services Manager.

## Key Information
- Affected component: Twingate Windows Client
- Platform: Windows only
- Root cause: Twingate Windows Service (`Twingate Service rc`) is not running or not set to automatic startup

## Symptoms
- Client fails to connect
- Popup error: *"The Twingate system service is not running. To connect, restart the Twingate system service or contact your admin."*

## Troubleshooting Steps

1. Open Run dialog: `Win + R` → type `services.msc` → press Enter
2. Scroll to **Twingate Service** in the list
3. Check status:
   - **If null/not running** → proceed to Resolution below
   - **If running + set to Automatic** → restart the service, restart the Twingate client app, then retry connection
   - **If service fails to start** → check TAP adapter (see Gotchas), collect detailed logs, contact Twingate Support

## Resolution (Start + Set to Automatic)

1. `Win + R` → `services.msc` → Enter
2. Scroll to **Twingate Service rc**
3. Right-click → **Start**
4. Right-click → **Properties** → set **Startup Type** to `Automatic`

## Gotchas
- The service name in the list is **Twingate Service rc** (not just "Twingate Service")
- If the service fails to start, check that the **Twingate TAP network adapter** is present and not disabled in Device Manager
- Service failing to start despite the TAP adapter being present requires log collection and a support ticket — not self-resolvable

## Configuration Values
| Setting | Required Value |
|---|---|
| Service Startup Type | `Automatic` |

## Related Docs
- Twingate detailed logs collection (linked in source as "detailed logs")
- Twingate Support ticket submission
---
source: https://help.twingate.com/articles/2020664128-windows-client-system-service-is-not-running
type: help
fetched: 2026-08-06
source_version: 5f193d508178ef371602dadc9596d509c1a61299a8e5b3b720bf66f724d4b0ca
---

# [Windows Client] System Service Is Not Running

## Summary
The Twingate Windows Client requires the "Twingate Service" Windows service to be running. If the service is stopped or missing, the client cannot establish connectivity. This article covers diagnosis and resolution steps.

## Key Information
- Error message: *"The Twingate system service is not running. To connect, restart the Twingate system service or contact your admin."*
- Component: Twingate Windows Service (`Twingate Service rc`)
- Service should be set to **Automatic** startup type
- Client depends on the Twingate TAP network adapter being present and enabled

## Prerequisites
- Windows OS with Twingate Client installed
- Access to `services.msc` (admin rights may be required to start services)

## Step-by-Step

### Troubleshooting
1. Press `Win + R`, type `services.msc`, press **Enter**
2. Scroll to **Twingate Service** in the list
3. Check status:
   - If not running → proceed to Resolution
   - If running and set to Automatic → restart the service, restart the client app, retry connection

### Resolution
1. Press `Win + R`, type `services.msc`, press **Enter**
2. Scroll to **Twingate Service rc**
3. Right-click → **Start**
4. Right-click → **Properties** → set **Startup Type** to `Automatic`

## Gotchas
- Service name in the list appears as **Twingate Service rc** (not just "Twingate Service")
- If the service fails to start after manual attempt, check that the **Twingate TAP network adapter** is present and not disabled in Device Manager
- If TAP adapter is missing or service still fails, collect detailed logs and open a support ticket — do not attempt further self-service

## Configuration Values
| Setting | Value |
|---|---|
| Service name | `Twingate Service rc` |
| Required startup type | `Automatic` |

## Related Docs
- Twingate detailed log collection (referenced but not linked)
- Twingate Support ticket submission
# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploys a Twingate Connector on Synology NAS devices running DSM 6.x/7.1 or earlier using DSM's built-in Task Scheduler. The Connector enables secure remote access to the NAS and other network devices without VPN or port forwarding. Uses Docker token generation and a scheduled task to run and auto-update the Connector.

## Key Information
- Applies to DSM 6.x and DSM 7.1 or earlier (separate guide exists for newer DSM versions)
- Deployment method: DSM Task Scheduler running a Docker-based deploy command
- Task runs on a schedule (default: daily midnight) — handles both initial deploy and upgrades
- Connector status verified via Twingate Admin Console Remote Network page

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network already configured in Twingate Admin Console
- Access to DSM web admin interface (`https://<NAS-IP>:5001`)
- Connected to the same local network as the NAS during setup
- Docker support on the NAS

## Step-by-Step

1. In Twingate Admin Console → **Networks** → select Remote Network
2. Open a Connector → click **Deploy Connector**
3. Select **Docker** → click **Generate Tokens** → authenticate
4. Configure optional settings (custom DNS, local connection logging)
5. Copy the generated deploy command
6. Log into DSM web interface (`https://X.X.X.X:5001`)
7. Open **Task Scheduler**
8. Create new task: **Scheduled Task → User-defined script**
9. **General tab**: set task name (e.g., `Twingate Connector`), set user to `root`
10. **Schedule tab**: adjust run frequency to suit environment (minimize disruption)
11. **Task Settings tab**: paste deploy command into **User-defined script** field
12. Save → select task → click **Run** → confirm prompt
13. Verify Connector shows **Connected** status in Admin Console

## Configuration Values
| Setting | Value |
|---|---|
| DSM admin URL | `https://<NAS-IP>:5001` |
| Task user | `root` |
| Deploy method | Docker (token-based) |
| Default schedule | Daily at midnight (adjust as needed) |

## Gotchas
- Must run task as `root` — other users will fail
- Default schedule (daily midnight) also runs the **upgrade** command — adjust timing to avoid disruption during active use
- After Connector is running, the NAS itself still requires a separate **Resource** entry in Admin Console using its local IP address
- This guide does not apply to DSM 7.2+; use the appropriate DSM 7.x guide for newer versions

## Related Docs
- [Add a Remote Network](https://www.twingate.com/docs/network)
- [Resources Guide](https://www.twingate.com/docs/resources)
- Twingate Client installation (required on end-user devices)
- DSM 7.2+ Connector deployment guide (separate)
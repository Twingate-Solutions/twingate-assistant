# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploys a Twingate Connector on Synology NAS running DSM 6.x or 7.1 and earlier using the built-in Task Scheduler. The Connector enables secure remote access to the NAS and other local network devices without VPN or port forwarding.

## Key Information
- Applies to DSM 6.x and DSM 7.1 or earlier (separate guide exists for DSM 7.2+)
- Deployment method: DSM native Task Scheduler running a Docker-based deploy command
- Connector runs as root user via scheduled task
- Task Scheduler also handles automatic Connector upgrades on the configured schedule

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network created in Twingate Admin Console
- Docker support on the Synology device
- Access to DSM web admin interface (default: `https://X.X.X.X:5001`)
- Must be on the same local network as the NAS during setup

## Step-by-Step

1. In Admin Console → **Networks** → select Remote Network → **Deploy Connector**
2. Select **Docker** → **Generate Tokens** → Authenticate
3. Configure optional settings (custom DNS, local connection logging)
4. Copy the generated deploy command
5. Log into DSM web UI at `https://<NAS-IP>:5001`
6. Open **Task Scheduler**
7. Create new task: **Scheduled Task → User-defined script**
8. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
9. **Schedule tab**: Adjust run frequency to minimize disruption (default: daily at midnight)
10. **Task Settings tab**: Paste the deploy command into **User-defined script**
11. Save → select task → click **Run** → confirm
12. Verify Connector shows **Connected** in Admin Console

## Configuration Values
- **Task user**: `root` (required)
- **Deploy command**: Generated from Admin Console Docker deployment flow (contains tokens and optional flags)
- **Optional flags available**: Custom DNS, local connection logging

## Gotchas
- Default schedule (daily midnight) may not suit all environments — adjust to reduce service disruption
- The scheduled task serves dual purpose: initial deployment AND recurring upgrades; schedule affects upgrade timing
- After Connector is running, the NAS itself still requires a separate **Resource** entry in Admin Console using its local IP address
- This guide does not apply to DSM 7.2+ (separate documentation exists)

## Related Docs
- [Add a Remote Network](https://www.twingate.com/docs/network)
- [Resources Guide](https://www.twingate.com/docs/resources)
- DSM 7.2+ Synology deployment guide (separate page)
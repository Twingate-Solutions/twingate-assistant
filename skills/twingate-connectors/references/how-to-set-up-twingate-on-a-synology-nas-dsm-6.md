# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploys a Twingate Connector on Synology NAS running DSM 6.x or 7.1 and earlier using DSM's built-in Task Scheduler. The Connector enables secure remote access to the NAS and other devices on the same network without VPN or port forwarding.

## Key Information
- Target OS: Synology DSM 6.x / 7.1 or earlier
- Deployment method: DSM Task Scheduler (User-defined script)
- Connector runs as `root` user
- Task Scheduler also handles connector upgrades on the configured schedule
- DSM web interface default: `https://X.X.X.X:5001`

## Prerequisites
- Active Twingate account with Admin Console access
- Remote Network created in Twingate Admin Console
- Connector created under that Remote Network
- Docker token generated for the Connector
- Browser access to DSM web interface from same local network

## Step-by-Step

1. In Twingate Admin Console → **Networks** → open Remote Network → select a Connector → click **Deploy Connector**
2. Click **Docker** → **Generate Tokens** → Authenticate
3. Configure optional settings (custom DNS, local connection logging), then **copy the deploy command**
4. Log into DSM web interface (`https://X.X.X.X:5001`)
5. Open **Task Scheduler**
6. Create new task: **Scheduled Task → User-defined script**
7. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
8. **Schedule tab**: Adjust run frequency to minimize disruption (default: daily at midnight)
9. **Task Settings tab**: Paste the copied deploy command into **User-defined script**
10. Save → select task → click **Run** → confirm
11. Verify in Admin Console: Remote Network → Connector status should show **Connected**

## Post-Deployment
- Add the NAS as a Resource in Admin Console using its local IP address
- Twingate Client must be installed and signed in on any device needing access
- See [Resources guide] for adding Resources

## Gotchas
- Task must run as `root` — other users will fail
- The same scheduled task handles both deployment and upgrades; adjust schedule to avoid disruption
- This guide is specifically for DSM 6.x / 7.1 and earlier — DSM 7.2+ has a separate guide
- Must be on the same local network as the NAS to access the DSM interface during setup

## Configuration Values
- Deploy command: generated in Admin Console (Docker token-based, includes any optional flags)
- Optional flags available at generation time: custom DNS, local connection logging

## Related Docs
- Twingate Resources guide
- Synology DSM 7.x deployment guide (separate)
- Add Remote Network (Admin Console)
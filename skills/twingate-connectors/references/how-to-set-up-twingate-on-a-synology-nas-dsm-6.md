# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploys a Twingate Connector on Synology NAS devices running DSM 6.x/7.1 or earlier using the built-in Task Scheduler. The Connector enables secure remote access to the NAS and other network devices without VPN server setup or port forwarding.

## Key Information
- Applies to DSM 6.x and 7.1 or earlier
- Uses DSM's native Task Scheduler to run the Docker-based Connector deploy command
- Connector auto-upgrades on the configured schedule
- After setup, add NAS as a Resource using its local IP address

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network created in Twingate Admin Console
- Docker selected as deployment method when generating Connector tokens
- Access to DSM web admin interface (`https://X.X.X.X:5001`)
- Must be on same local network as the NAS during setup

## Step-by-Step

1. In Twingate Admin Console → **Network** page → select Remote Network
2. Choose a pre-created Connector → click **Deploy Connector**
3. Select **Docker** → click **Generate Tokens** → authenticate
4. Configure options (custom DNS, local connection logging) → copy the deploy command
5. Log into DSM web interface at `https://<NAS-IP>:5001`
6. Open **Task Scheduler**
7. Create new task: **Scheduled Task → User-defined script**
8. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
9. **Schedule tab**: Adjust run frequency to minimize disruption (default: daily at midnight)
10. **Task Settings tab**: Paste the copied deploy command into **User-defined script**
11. Save → select task → click **Run** → confirm execution
12. Verify Connector shows **Connected** status in Admin Console
13. Add NAS as a Resource using its local IP address

## Configuration Values
- Deploy command: generated in Admin Console (Docker format, includes tokens and optional flags)
- Optional flags available: custom DNS, local connection logging
- Default schedule: daily at midnight (modify as needed)

## Gotchas
- Task must run as `root` user — other users will likely lack required permissions
- The scheduled task serves dual purpose: initial deployment **and** recurring upgrades — schedule timing affects upgrade disruption
- DSM 7.2+ users should use a different guide (this guide is for 6.x/7.1 and earlier only)
- NAS must be added separately as a Resource in Admin Console after Connector is running

## Related Docs
- [Add a Remote Network](https://www.twingate.com/docs/network)
- [Resources Guide](https://www.twingate.com/docs/resources)
- Synology DSM 7.2+ Connector deployment (separate guide)
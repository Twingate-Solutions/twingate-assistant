# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 6.x or 7.1 and earlier using DSM's native Task Scheduler. The Connector enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- DSM is Linux-based; Connector runs via Docker through Task Scheduler
- Task Scheduler handles both initial deployment and scheduled upgrades
- Connector status visible in Twingate Admin Console under the Remote Network page
- After deployment, NAS must be added separately as a Resource using its local IP

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network configured in Twingate Admin Console
- Access to DSM web admin interface (`https://X.X.X.X:5001`)
- Must be on the same local network as the NAS during setup
- Docker available on the NAS

## Step-by-Step

1. **Admin Console**: Navigate to Remote Network → select a pre-created Connector → click **Deploy Connector**
2. **Generate tokens**: Select **Docker** → **Generate Tokens** → Authenticate
3. **Copy deploy command**: Configure optional settings (custom DNS, local connection logging), then copy the deploy command from the bottom of the page
4. **Open DSM**: Sign into DSM web admin at `https://X.X.X.X:5001`
5. **Open Task Scheduler**: Control Panel → Task Scheduler
6. **Create task**: New → Scheduled Task → User-defined script
7. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
8. **Schedule tab**: Configure run frequency (default: daily at midnight — adjust to minimize disruption)
9. **Task Settings tab**: Paste the copied deploy command into **User-defined script**
10. **Run**: Save → select task → click **Run** → confirm prompt
11. **Verify**: Check Connector status in Admin Console — should show **Connected**
12. **Add Resource**: Add the NAS as a Resource in Admin Console using its local IP address

## Configuration Values
- **Deploy method**: Docker (selected during token generation)
- **DSM admin URL**: `https://X.X.X.X:5001`
- **Task user**: `root` (required)
- **Optional flags during token generation**: Custom DNS, local connection logging

## Gotchas
- Must be physically on the same network as the NAS when configuring via DSM
- Task Scheduler runs the deploy command on every scheduled execution — acts as auto-upgrade mechanism; set schedule carefully to avoid disruption
- The NAS itself is **not** automatically a Resource — must be added manually post-deployment
- This guide applies to DSM 6.x and 7.1 or earlier only (separate guide exists for DSM 7.2+)

## Related Docs
- [Add a Remote Network](https://www.twingate.com/docs/network)
- [Resources Guide](https://www.twingate.com/docs/resources)
- Synology NAS DSM 7.x deployment (separate documentation)
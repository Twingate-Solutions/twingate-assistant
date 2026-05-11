# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 6.x/7.1 or earlier using DSM's built-in Task Scheduler. The Connector enables secure remote access to the NAS and other network devices without VPN server setup or port forwarding.

## Key Information
- Applies to DSM 6.x and 7.1 or earlier
- Uses DSM Task Scheduler with a user-defined script (not Docker package directly)
- Connector runs as `root` user via scheduled task
- Task also handles connector upgrades on the configured schedule

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network created in Twingate Admin Console
- Connector token generated via Admin Console → Remote Network → Deploy Connector → Docker → Generate Tokens
- Browser access to DSM web interface (default: `https://<NAS-IP>:5001`)
- Must be on the same local network as the NAS during setup

## Step-by-Step

1. In Twingate Admin Console, create a Remote Network if not already done
2. Open Remote Network details → select a Connector → click **Deploy Connector**
3. Select **Docker** → **Generate Tokens** → authenticate when prompted
4. Configure optional settings (custom DNS, local connection logging), then copy the deploy command
5. Log into DSM web interface at `https://<NAS-IP>:5001`
6. Open **Task Scheduler**
7. Create new task: **Scheduled Task → User-defined script**
8. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
9. **Schedule tab**: Adjust run frequency to suit your environment (default: daily at midnight)
10. **Task Settings tab**: Paste the copied deploy command into **User-defined script**
11. Save → select task → click **Run** → confirm execution
12. Verify Connector shows **Connected** status in Admin Console

## Configuration Values
- Deploy command: obtained from Admin Console (Docker deploy flow)
- Optional flags available in console UI: custom DNS, local connection logging

## Gotchas
- Must select `root` as the task user — Connector will fail to deploy otherwise
- Schedule defaults to daily midnight; adjust to minimize service disruption
- The scheduled task serves dual purpose: initial deploy + recurring upgrades
- After Connector is running, the NAS itself still requires a separate **Resource** entry in Admin Console (use the local network IP address)
- This guide does **not** apply to DSM 7.2+; use the DSM 7.x-specific guide for newer versions

## Related Docs
- [Add a Remote Network](https://www.twingate.com/docs/network)
- [Resources Guide](https://www.twingate.com/docs/resources)
- Twingate Client installation (required on end-user devices for access)
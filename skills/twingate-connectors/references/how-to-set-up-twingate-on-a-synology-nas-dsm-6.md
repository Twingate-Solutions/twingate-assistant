## Deploy Connector on Synology NAS (DSM 6.x)

Deploys a Twingate Connector on Synology NAS running DSM 6.x (or DSM 7.1 and earlier) using the DSM Task Scheduler. The deploy command also handles upgrades on whatever schedule is set.

**Prerequisites:**
- Synology NAS running DSM 6.x or 7.1 and earlier
- Twingate Admin Console access with a configured Remote Network

**Step-by-Step:**
1. In Twingate Admin Console: Remote Network → Deploy Connector → Docker → Generate Tokens → copy the deploy command
2. Log into the DSM web admin interface (typically `https://<NAS-IP>:5001`)
3. Open Task Scheduler → Create → Scheduled Task → User-defined script
4. General tab: set a name (e.g., "Twingate Connector"), select user: `root`
5. Schedule tab: configure run frequency (adjust from default daily midnight to minimize disruption)
6. Task Settings tab: paste the Connector deploy command in "User-defined script"
7. Save, select the task, click Run → confirm
8. Verify in Admin Console: Connector status shows "Connected"

**Key Notes:**
- The same task handles both initial deployment and upgrades — running it again on schedule keeps the Connector updated
- For DSM 7.2+, use the DSM 7 guide instead (uses Docker Compose via Container Manager)

**Related Docs:**
- /docs/how-to-set-up-twingate-on-a-synology-nas-dsm-7 -- DSM 7.x guide
- /docs/upgrading-connectors -- Connector update process

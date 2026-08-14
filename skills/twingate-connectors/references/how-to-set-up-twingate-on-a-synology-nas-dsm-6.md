---
source: https://www.twingate.com/docs/how-to-set-up-twingate-on-a-synology-nas-dsm-6
type: docs
fetched: 2026-08-14
source_version: d3db719c8d9034cc42e1c573e00635ec391b3e6316aa5fa00dad563b6a0d5884
---

# Deploy Twingate Connector on Synology NAS (DSM 6.x)

## Summary
Deploys a Twingate Connector on Synology NAS running DSM 6.x/7.1 or earlier using DSM's built-in Task Scheduler. The Connector enables secure remote access to the NAS and other local network devices without VPN or port forwarding.

## Key Information
- DSM is Linux-based; Connector runs via Docker through Task Scheduler
- Task Scheduler both deploys the Connector and handles automatic upgrades on schedule
- Verify deployment by checking Connector status ("Connected") in Admin Console
- After deployment, add NAS as a Resource using its local IP address

## Prerequisites
- Synology NAS running DSM 6.x or 7.1 or earlier
- Remote Network created in Twingate Admin Console
- Docker package available on DSM
- Browser access to DSM web interface (default: `https://<NAS-IP>:5001`)
- Connector deploy command copied from Admin Console (Docker > Generate Tokens)

## Step-by-Step

1. In Admin Console → **Networks** page, select your Remote Network
2. Click **Deploy Connector** on one of the pre-created Connectors
3. Select **Docker** → **Generate Tokens** → Authenticate
4. Configure options (custom DNS, local connection logging), then **copy the deploy command**
5. Open DSM web interface at `https://<NAS-IP>:5001`
6. Open **Task Scheduler**
7. Create new task: **Scheduled Task → User-defined script**
8. **General tab**: Set task name (e.g., `Twingate Connector`), set user to `root`
9. **Schedule tab**: Adjust run frequency to minimize disruption (default: daily at midnight)
10. **Task Settings tab**: Paste the copied deploy command into **User-defined script**
11. Save, select the task, click **Run**, confirm execution
12. Verify status shows **Connected** in Admin Console Remote Network page

## Configuration Values
- **Deploy command**: Generated in Admin Console (Docker method); includes auth tokens
- **Optional flags** (toggled in Admin Console before copying command):
  - Custom DNS
  - Local connection logging
- **DSM task user**: Must be `root`

## Gotchas
- This guide applies only to DSM **6.x and 7.1 or earlier** — different process for DSM 7.2+
- Task schedule controls upgrade cadence — set carefully to avoid disrupting active connections
- NAS must be added separately as a **Resource** in Admin Console using its local IP; deployment alone does not make it accessible
- Must be on the same local network as the NAS when accessing DSM for setup

## Related Docs
- [Resources Guide](https://www.twingate.com/docs/resources) — adding the NAS as an accessible Resource
- Twingate Admin Console → Networks page — Remote Network and Connector management
- DSM 7.2+ deployment guide (separate process)
## Deploy Connector on Synology NAS (DSM 7.x)

Deploys a Twingate Connector on Synology NAS running DSM 7.2+ using Container Manager (Docker Compose project). Supports in-place image updates from the Container Manager UI.

**Prerequisites:**
- Synology NAS running DSM 7.2 or later
- Container Manager installed
- Twingate Admin Console access with a configured Remote Network

**Step-by-Step:**
1. In Twingate Admin Console: Remote Network → Deploy Connector → Docker → Generate Tokens → copy Access Token and Refresh Token
2. Create folder `twingate-connector` under your Docker config directory in File Station
3. Create a local `compose.yaml`:
   ```yaml
   services:
     twingate-connector:
       image: twingate/connector:latest
       environment:
         - TWINGATE_NETWORK=<TENANT NAME>
         - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
         - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
       network_mode: host
   ```
4. In Container Manager → Project → Create → name project "twingate-connector" → point Path to the folder → upload `compose.yaml`
5. Replace placeholders (tenant name, tokens) when prompted
6. Check "Start the project once it is created" → Done
7. Verify: Connector deploys with exit code 0; confirm connected in Admin Console

**Updates:**
- Container Manager → Image → if "Update Available" appears → click → Update → acknowledge warning
- Image downloads and applies automatically without manual intervention

**Gotchas:**
- `network_mode: host` is included in the example compose file — required for local P2P and LAN access
- For DSM 6.x or 7.1 and earlier, use the DSM 6 guide (Task Scheduler method)

**Related Docs:**
- /docs/how-to-set-up-twingate-on-a-synology-nas-dsm-6 -- DSM 6.x guide
- /docs/deploy-connector-with-docker-compose -- Docker Compose parameter reference

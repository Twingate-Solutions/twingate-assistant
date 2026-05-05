## Deploy Connector on QNAP NAS

Installs a Twingate Connector on a QNAP NAS using Container Station (Docker). Makes the NAS and other local network devices remotely accessible.

**Prerequisites:**
- QNAP device with Container Station installed and configured
- Twingate account and a configured Remote Network

**Step-by-Step:**
1. In Twingate Admin Console: create a Remote Network → Deploy Connector → select Docker → Generate Tokens (re-authenticate) → copy the `docker run` command to a text editor
2. On the QNAP: open Container Station → Create → search "twingate" → select `twingate/connector` image → Install → select `latest` tag
3. Set container name (use Connector name), set CPU and Memory limits
4. Click Advanced Settings → Environment section → add three variables:
   - `TWINGATE_NETWORK` = your network name
   - `TWINGATE_ACCESS_TOKEN` = access token
   - `TWINGATE_REFRESH_TOKEN` = refresh token
5. Configure Network (hostname can be the Connector name)
6. Continue → OK to start the container
7. Verify in Admin Console: Connector shows as connected

**After Setup:**
- Add the QNAP NAS as a Resource using its local IP address

**Related Docs:**
- /docs/resources -- Adding Resources after Connector is up
- /docs/connector-placement-best-practices -- Connector placement guidance

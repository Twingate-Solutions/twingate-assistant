## Deploy Connector on TrueNAS SCALE

Runs a Twingate Connector as a Docker application on TrueNAS SCALE (HCI platform with Linux container support).

**Prerequisites:**
- TrueNAS SCALE web UI access
- Twingate Admin Console access to generate tokens

**Step-by-Step:**
1. In Twingate Admin Console: Remote Network → Add Connector → select **Linux** deployment method → Generate New Tokens
   - Note which token is the Access token and which is the Refresh token
   - Note your Twingate network name (subdomain)
2. In TrueNAS SCALE web UI: Apps → Launch Docker Image
   - Application Name: e.g., `twingate-connector`
   - Image repository: `twingate/connector`, tag: `latest`
3. Add Container Environment Variables:
   - `TWINGATE_NETWORK` = your network name
   - `TWINGATE_ACCESS_TOKEN` = access token
   - `TWINGATE_REFRESH_TOKEN` = refresh token
   - `TWINGATE_LABEL_HOSTNAME` = descriptive name
4. Optional variables:
   - `TWINGATE_DNS` = custom DNS server IP
   - `TWINGATE_LOG_ANALYTICS=v2` for detailed SIEM-ready JSON logs
5. For local network visibility (Clients on same LAN): set Host Interface in the Networking section
6. Save — TrueNAS pulls the image and starts the container; verify green "Active" status

**ICMP/Ping Support:**
- System Settings → Advanced → Sysctl → Add: `net.ipv4.ping_group_range = 0 2147483647`, then reboot

**Gotchas:**
- Updates are not automatic; use the Upgrade option in the TrueNAS app UI to update
- Use Linux token generation method even though TrueNAS runs Docker (only tokens are needed)

**Related Docs:**
- /docs/connector-deployment -- General connector deployment guide
- /docs/upgrading-connectors -- Connector update process

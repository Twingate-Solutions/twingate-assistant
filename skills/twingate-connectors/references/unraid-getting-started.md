## Getting Started with Unraid and Twingate

Deploys a Twingate Connector on Unraid using the official Community Applications plugin. Quickest path for Unraid users.

**Prerequisites:**
- Unraid instance with the Community Applications plugin installed
- Twingate Admin Console access

**Step-by-Step:**
1. In Twingate Admin Console: Remote Networks → select network → Add Connector → Manual → Generate Tokens (re-authenticate) → copy Access Token and Refresh Token
2. In Unraid web UI: Apps tab → search "Twingate Connector" → select official entry → Install
3. Fill in the configuration form:
   - Network: your Twingate network name (subdomain)
   - Access Token: from Admin Console
   - Refresh Token: from Admin Console
4. Click Apply
5. Verify in Admin Console: Controller and Relay both show connected

**Gotchas:**
- Each Connector needs its own unique token set — do not reuse tokens
- Select the official Twingate entry in the Community Apps store

**Related Docs:**
- /docs/proxmox-getting-started -- Proxmox integration
- /docs/home-assistant-getting-started -- Home Assistant integration
- /docs/resources -- Configuring Resources after Connector is up

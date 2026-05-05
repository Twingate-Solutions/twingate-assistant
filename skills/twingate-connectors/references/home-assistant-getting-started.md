## Home Assistant + Twingate

Installs a Twingate Connector as a Home Assistant app to enable secure remote access to Home Assistant and connected smart home devices. Works on Home Assistant OS only (not containers).

**Prerequisites:**
- Home Assistant OS (not Home Assistant Container)
- Twingate Admin Console access
- Twingate account with a configured Remote Network

**Step-by-Step:**
1. Add the Twingate repository to Home Assistant via the repository dialog (URL from Twingate Community GitHub)
2. In the App Store, check for updates (ellipsis → Check for updates); search "Twingate"
3. Install the **Twingate Connector** app from the Twingate Connector app repository section
4. In Twingate Admin Console: Remote Networks → select network → Add Connector → Manual → Generate Tokens (authenticate when prompted); copy Access Token and Refresh Token
5. In Home Assistant: Twingate app → Configuration tab → enter Network domain, Access Token, Refresh Token
6. Navigate to the Info tab → click Start
7. Verify in Logs tab; confirm Connector shows Controller and Relay both **connected** in Admin Console

**Gotchas:**
- Each Connector must have its own unique token set — do not reuse tokens across Connectors
- Home Assistant Container (Docker) is not supported; only Home Assistant OS

**Related Docs:**
- /docs/proxmox-getting-started -- Proxmox integration guide
- /docs/unraid-getting-started -- Unraid integration guide
- /docs/resources -- Configuring Resources after Connector is up

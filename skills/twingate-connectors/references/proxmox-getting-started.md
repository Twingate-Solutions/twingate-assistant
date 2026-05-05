## Getting Started with Proxmox VE and Twingate

Quickest path to deploying a Twingate Connector on Proxmox VE using the community open-source Proxmox VE Helper Scripts. Creates an LXC container automatically.

**Prerequisites:**
- Proxmox VE running instance with SSH or web UI access
- Twingate Admin Console access

**Step-by-Step:**
1. In Twingate Admin Console: Remote Networks → select network → Add Connector → Manual → Generate Tokens (re-authenticate) → copy Access Token and Refresh Token
2. On the Proxmox VE head node, run:
   ```
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/twingate-connector.sh)"
   ```
3. When prompted by the script, enter: Network name, Access Token, Refresh Token
4. Script automatically deploys and starts the Connector in an LXC container
5. Verify in Admin Console: Controller and Relay statuses show connected

**Gotchas:**
- Each Connector must have its own unique token set — do not reuse tokens
- Uses the community-scripts/ProxmoxVE open-source repository (not an official Twingate package)

**Related Docs:**
- /docs/proxmox-container-deployment -- Manual LXC container deployment guide
- /docs/home-assistant-getting-started -- Home Assistant integration
- /docs/resources -- Configuring Resources after Connector is up

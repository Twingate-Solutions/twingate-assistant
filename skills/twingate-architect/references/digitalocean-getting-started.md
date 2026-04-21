## Getting Started with DigitalOcean and Twingate

Quick guide to deploying a Twingate Connector on DigitalOcean using the `doctl` CLI and a cloud-init script. The Twingate Admin Console generates a ready-to-run `doctl` command that creates a Droplet with the Connector pre-configured via cloud-init; the process takes three steps.

**Key Information**
- Deployment method: `doctl` CLI + cloud-init (Twingate Admin Console generates the full command)
- The Admin Console's DigitalOcean Connector option generates the complete `doctl` command including Access and Refresh tokens
- Each Connector requires its own unique token pair -- never reuse tokens across Connectors
- After deployment, verify in both DigitalOcean (Droplet running) and Twingate Admin Console (Controller and Relay status = connected)

**Prerequisites**
- DigitalOcean account with API access
- `doctl` CLI installed and authenticated with DigitalOcean credentials
- Twingate account with Admin Console access

**Step-by-Step**
1. In Twingate Admin Console -> Remote Networks -> select network -> add/select Connector -> See More -> DigitalOcean
2. Click "Generate Tokens" in Step 2 and authenticate; then copy the `doctl` command from Step 4
3. Paste and run the `doctl` command in your terminal; wait for it to complete
4. Verify in DigitalOcean Control Panel: Droplets -> confirm Droplet is running
5. Verify in Twingate Admin Console: Remote Networks -> select network -> select Connector -> confirm Controller and Relay = connected

**Gotchas**
- Do NOT reuse token sets -- each Connector must have its own unique Access and Refresh token pair
- Copy/paste errors can occur if your terminal reinterprets whitespace; paste into a script file first if needed
- `doctl not found`: install via DigitalOcean docs and authenticate with `doctl auth init`

**Related Docs**
- /docs/connector-management
- /docs/resources
- /docs/troubleshooting-guide

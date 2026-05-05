## Deploy Connector in a Proxmox LXC Container

Guide to running a Twingate Connector inside a Proxmox Linux Container (LXC). Targets homelab and corporate Proxmox users.

**Prerequisites:**
- Proxmox VE with a container template downloaded (Ubuntu 22.04 LTS recommended)
- Download template: `pveam update && pveam list && pveam download <storageLocation> <templateName>`

**Minimum Container Resources:**
- 1 vCPU, 512 MB RAM; increase based on traffic volume

**Container Configuration Notes:**
- Leave **Nesting** checked
- Uncheck **Unprivileged container** if you want to allow pings (ICMP) to Resources from this Connector
- Assign a static IP address (recommended) so Resources can allowlist the Connector's IP and logs remain consistent

**Installation Steps:**
1. Start the container and log in via Proxmox VNC console (user: root)
2. Run: `apt update && apt upgrade -y && apt install curl -y`
3. In Twingate Admin Console: navigate to the Remote Network → Add Connector → select Linux deployment → Generate Tokens
4. Copy and paste the generated deployment command into the container console
5. Verify Connector status updates to "connected" in the Admin Console

**Gotchas:**
- Connectors do not auto-update; stagger updates across multiple Connectors to avoid downtime; automate with a cron job if desired

**Related Docs:**
- /docs/connector-placement-best-practices -- Where to deploy Connectors
- /docs/proxmox-getting-started -- Full Proxmox getting-started guide
- /docs/upgrading-connectors -- Connector update process

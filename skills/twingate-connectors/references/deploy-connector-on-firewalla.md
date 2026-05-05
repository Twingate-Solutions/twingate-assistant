## Deploy Connector on a Firewalla Box

Deploys a Twingate Connector via Docker on Firewalla Gold, Purple, or Blue Plus (boxes with native Docker support). Tested in Router mode only.

**Prerequisites:**
- Firewalla box running the latest firmware in Router mode with outbound internet access
- Docker enabled on the Firewalla box (`sudo systemctl status docker`)
- Basic Twingate config (Users, Groups, Remote Networks, Resources) already in place

**Step-by-Step:**
1. SSH into the Firewalla box: `ssh pi@<firewalla-ip>`
2. Verify Docker is running
3. In Twingate Admin Console: Remote Networks → Remote Network → Add/Select Connector
4. Select Docker deployment method
5. Generate Tokens (re-authenticate when prompted)
6. Optional customizations:
   - Custom DNS Server: skip for first-time users
   - **Make Connector available on local network: Enable** (required for LAN/VLAN access — uses host network mode)
   - Local network connection logs: Enable for SIEM ingestion
7. Copy and run the Docker command in the SSH session
8. Verify Connector is active: `sudo docker ps`

**Gotchas:**
- Host network mode (`--network host`) is **required** for the Connector to access LANs/VLANs on the Firewalla box
- Docker and the Connector container may not start automatically after reboot — configure Firewalla's Customized Scripting to auto-start Docker containers on boot

**Related Docs:**
- /docs/deploy-connector-with-docker-compose -- General Docker Compose deployment
- /docs/site-2-site -- Site-to-site with multiple Firewalla boxes

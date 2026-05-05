## Deploy Connector on Linux

Complete guide to deploying Twingate Connectors on Linux via Docker container or systemd service.

**Docker Container (most flexible — any 64-bit Linux distro):**
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. Admin Console → Remote Network → Add Connector → Docker → Generate Tokens → configure options → copy and run the `docker run` command
- Use only Docker from the official distribution channel — other channels may have incompatible versions

**systemd Service (preferred for supported distros — lower overhead):**
- Supported distros: Ubuntu 22.04 LTS / 24.04 LTS, Fedora 39/40, CentOS Stream 9, Debian 11/12
- Admin Console → Connector → Linux → Generate Tokens → enable optional real-time logging → copy and run the install command
- Config file: `/etc/twingate/connector.conf`
  ```
  TWINGATE_NETWORK=https://autoco.twingate.com
  TWINGATE_ACCESS_TOKEN=<access_token>
  TWINGATE_REFRESH_TOKEN=<refresh_token>
  ```
- Key commands: `systemctl status/stop/start/restart/enable/disable twingate-connector`

**Gotchas:**
- Amazon Linux: use the AMI deployment method instead (systemd Connector pre-installed)
- Tokens are Connector-specific — cannot be shared between multiple Connectors
- Updates are not automatic: use Linux package manager manually or schedule with a cron job; stagger across Connectors

**Related Docs:**
- /docs/connector-best-practices -- Hardware and network requirements
- /docs/upgrading-connectors -- Systemd and Docker update guides
- /docs/advanced-connector-management -- Environment variable reference

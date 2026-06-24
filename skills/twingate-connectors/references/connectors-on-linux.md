# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers (any distro) or as a systemd service (select distros). Docker offers broader compatibility; systemd is more robust with lower overhead. Both methods require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens (access + refresh) are connector-specific and non-shareable
- Config file location (systemd): `/etc/twingate/connector.conf`
- Service name: `twingate-connector`

## Prerequisites
- **Docker**: Docker installed and running; use official channel only
- **systemd**: Supported distros only:
  - Ubuntu 22.04 LTS, 24.04 LTS
  - Fedora 39, 40
  - CentOS Stream 9
  - Debian 11 LTS, 12 LTS
- Access to Twingate Admin Console to generate tokens

## Step-by-Step

### Docker Deployment
1. Install Docker via official method or convenience script
2. In Admin Console → Remote Networks → select network → Add Connector
3. Click new connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run generated `docker run` command

### systemd Deployment
1. In Admin Console → Remote Networks → select network → Add Connector
2. Click new connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

### `/etc/twingate/connector.conf`
```
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

### systemd Management Commands
```bash
sudo systemctl status twingate-connector
sudo systemctl start twingate-connector
sudo systemctl stop twingate-connector
sudo systemctl restart twingate-connector   # also reloads config
sudo systemctl enable twingate-connector    # auto-start at boot
sudo systemctl disable twingate-connector
```

### Docker Install (convenience script)
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Gotchas
- **Do not use unofficial Docker channels** — may install outdated versions incompatible with Connector image
- **Amazon Linux**: Use pre-built AMI deployment instead of these instructions
- Tokens cannot be shared between connectors
- Restarting the service is required after editing `connector.conf`
- Stagger updates across multiple connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Provisioning/re-provisioning a Connector
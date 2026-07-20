# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can be deployed either as Docker containers (flexible, any distro) or as a systemd service (more robust, lower overhead, supported distros only). Both methods require tokens generated from the Twingate Admin Console. Docker is simpler but requires Docker runtime; systemd integrates natively with the OS.

## Key Information
- Two deployment methods: Docker container or systemd service
- Docker works on any Linux distribution
- systemd service is the recommended option where supported
- Tokens are per-Connector and cannot be shared between Connectors
- Config file location (systemd): `/etc/twingate/connector.conf`

## Prerequisites
- Access to Twingate Admin Console
- An existing Remote Network with a Connector created
- Docker installed (Docker method) OR supported Linux distro (systemd method)
- Generated Access Token and Refresh Token from Admin Console

## Supported Distros (systemd)
- Ubuntu 22.04 LTS, 24.04 LTS
- Fedora 39, 40
- CentOS Stream 9
- Debian 11 LTS, 12 LTS

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console: Remote Networks → Remote Network → Add Connector
3. Click connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated `docker run` command

### systemd Deployment
1. In Admin Console: Remote Networks → Remote Network → Add Connector
2. Click connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Enable optional real-time logging if needed
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file:** `/etc/twingate/connector.conf`

```ini
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

**systemd Management Commands:**
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector
```

## Gotchas
- Only install Docker via official channel (`get.docker.com`); other channels may have outdated versions incompatible with Connector image
- Amazon Linux: use pre-built AMI deployment instead of Docker or manual systemd install
- Configuration file changes require `systemctl restart twingate-connector` to take effect
- Stagger updates across multiple Connectors to avoid downtime
- Only Ubuntu LTS versions are officially supported (non-LTS not supported)

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Provisioning/re-provisioning a Connector
- Amazon Linux AMI deployment
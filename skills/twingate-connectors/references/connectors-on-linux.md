# Twingate Connector Deployment on Linux

## Summary
Twingate Connectors on Linux can be deployed via Docker container or as a native systemd service. Docker works on any Linux distro; systemd is more robust but limited to supported distributions. Both methods require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Docker supports any Linux distribution; systemd supports specific distros only
- Tokens are per-Connector and cannot be shared between Connectors
- Config file location (systemd): `/etc/twingate/connector.conf`

## Prerequisites
- Access to Twingate Admin Console
- Remote Network already created in Admin Console
- **Docker method**: Docker installed and running
- **Systemd method**: Supported Linux distribution

## Supported Distributions (systemd)
- Ubuntu 22.04 LTS, 24.04 LTS (LTS only)
- Fedora 39, 40
- CentOS Stream 9
- Debian 11 (Bullseye), 12 (Bookworm)

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console: Remote Networks → Select Network → Add Connector
3. Select connector → Choose **Docker** option → Generate tokens (requires re-auth)
4. Enable optional features, copy and run generated command

### Systemd Deployment
1. In Admin Console: Remote Networks → Select Network → Add Connector
2. Select connector → Choose **Linux** option → Generate tokens (requires re-auth)
3. Enable optional real-time logging if needed, copy and run generated install command
4. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file:** `/etc/twingate/connector.conf`

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Full URL, e.g. `https://autoco.twingate.com` |
| `TWINGATE_ACCESS_TOKEN` | Per-connector access token |
| `TWINGATE_REFRESH_TOKEN` | Per-connector refresh token |

## Management Commands
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector  # boot behavior
```

## Gotchas
- Install Docker only via official channel (`get.docker.com`); other channels may have outdated versions incompatible with Connector image
- Amazon Linux: use pre-built AMI deployment instead
- Access/refresh tokens are Connector-specific — cannot be reused across Connectors
- Restart required after editing config file: `sudo systemctl restart twingate-connector`
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Peer-to-peer connections setup
- Connector provisioning/re-provisioning
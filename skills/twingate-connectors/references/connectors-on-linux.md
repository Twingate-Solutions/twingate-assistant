# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers or as a systemd service. Docker supports any Linux distro; systemd is more robust but limited to specific distributions. Both require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens (access + refresh) are Connector-specific and cannot be shared
- Config file location (systemd): `/etc/twingate/connector.conf`
- Amazon Linux: use pre-built AMI instead

## Supported Distributions (systemd)
- Ubuntu 22.04 LTS, 24.04 LTS (LTS only)
- Fedora 39, 40
- CentOS Stream 9
- Debian 11 (Bullseye), 12 (Bookworm)

## Prerequisites
- Twingate Admin Console access
- Remote Network already created
- Docker installed (Docker method) or supported Linux distro (systemd method)

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. Admin Console → Remote Networks → Remote Network → Add Connector
3. Select **Docker** option on deployment page
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated command

### Systemd Deployment
1. Admin Console → Remote Networks → Remote Network → Add Connector
2. Select **Linux** option on deployment page
3. Generate tokens (requires re-authentication)
4. Enable optional real-time logging if needed
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**File:** `/etc/twingate/connector.conf`

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Full URL, e.g. `https://autoco.twingate.com` |
| `TWINGATE_ACCESS_TOKEN` | Generated per-Connector token |
| `TWINGATE_REFRESH_TOKEN` | Generated per-Connector token |

## systemd Management Commands
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector  # boot behavior
```

## Gotchas
- Install Docker via official channel only (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image
- Only Ubuntu LTS versions are supported for systemd
- Tokens cannot be reused across multiple Connectors
- After editing config file, restart service for changes to take effect
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Peer-to-peer connections
- Amazon Linux AMI deployment
- Provisioning/re-provisioning Connectors
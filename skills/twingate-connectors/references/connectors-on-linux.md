# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers or as a systemd service. Docker works on any Linux distro; systemd is more robust with lower overhead but supports specific distros only. Both methods require tokens generated from the Twingate Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Docker: flexible, any Linux distro, higher management overhead
- systemd: more robust, lower overhead, limited distro support
- Tokens (access + refresh) are connector-specific and cannot be shared

## Prerequisites
- Access to Twingate Admin Console
- A configured Remote Network with a Connector created
- **Docker method**: Docker installed and running
- **systemd method**: Supported Linux distribution

## Supported Distributions (systemd)
| Distro | Versions |
|--------|----------|
| Ubuntu | 22.04 LTS, 24.04 LTS (LTS only) |
| Fedora | 39, 40 |
| CentOS | Stream 9 |
| Debian | 11 LTS, 12 LTS |

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console: Remote Networks → Remote Network → Add Connector
3. Select **Docker** option on deployment page
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated `docker run` command

### systemd Deployment
1. In Admin Console: Remote Networks → Remote Network → Add Connector
2. Select **Linux** option on deployment page
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file location**: `/etc/twingate/connector.conf`

```ini
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

**systemd Management Commands**:
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector
```

## Gotchas
- **Docker**: Use only official Docker channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image
- **Amazon Linux**: Use pre-built AMI deployment instead; do not use this guide
- Tokens are per-connector — cannot reuse tokens across multiple connectors
- systemd Connector may run on unsupported distros but no support is provided
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Provisioning/re-provisioning a Connector
- Amazon Linux AMI deployment instructions
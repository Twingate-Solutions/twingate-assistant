# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers or as a systemd service. Docker works on any Linux distro; systemd is supported on specific distributions and is the recommended option for lower management overhead.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens (access + refresh) are connector-specific and cannot be shared
- Config file location (systemd): `/etc/twingate/connector.conf`
- Amazon Linux users should use the pre-built AMI instead

## Prerequisites
- Access to Twingate Admin Console
- Docker installed (for Docker method) or supported Linux distro (for systemd)
- Connector created in Admin Console with tokens generated

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
2. In Admin Console: Remote Networks → Select Network → Add Connector
3. Open connector → Select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run generated `docker run` command

### systemd Deployment
1. In Admin Console: Remote Networks → Select Network → Add Connector
2. Open connector → Select **Linux** option
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**File:** `/etc/twingate/connector.conf`

```ini
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

## systemd Management Commands
```bash
sudo systemctl status twingate-connector
sudo systemctl start twingate-connector
sudo systemctl stop twingate-connector
sudo systemctl restart twingate-connector   # required for config reload
sudo systemctl enable twingate-connector    # auto-start at boot
sudo systemctl disable twingate-connector
```

## Gotchas
- Install Docker only via official channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image requirements
- Tokens cannot be shared across multiple Connectors
- Connector service may run on unsupported distros but won't receive official support
- Stagger updates across multiple Connectors to avoid downtime
- Configuration file changes require `systemctl restart` to take effect

## Related Docs
- Connector Best Practices
- systemd Connector Update Guide
- Docker Connector Update Guide
- Peer-to-peer connections setup
- Amazon Linux AMI deployment
- Provisioning/re-provisioning Connectors
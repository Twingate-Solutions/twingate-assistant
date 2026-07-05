# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers or systemd services. Docker works on any Linux distribution; systemd is more robust but limited to specific distros. Both methods require tokens generated from the Twingate Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens are Connector-specific and cannot be shared between Connectors
- Config file location (systemd): `/etc/twingate/connector.conf`
- Verify service: `sudo systemctl status twingate-connector`

## Prerequisites
- Access to Twingate Admin Console
- Remote Network already created in Admin Console
- **Docker method**: Docker installed and running
- **Systemd method**: Supported Linux distro (see below)

### Supported Distros (systemd)
| Distro | Versions |
|--------|----------|
| Ubuntu | 22.04 LTS, 24.04 LTS only |
| Fedora | 39, 40 |
| CentOS | Stream 9 |
| Debian | 11 LTS, 12 LTS |

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console: Remote Networks → Remote Network → Add Connector
3. Click new Connector → Select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated command in terminal

### Systemd Deployment
1. In Admin Console: Remote Networks → Remote Network → Add Connector
2. Click new Connector → Select **Linux** option
3. Generate tokens (requires re-authentication)
4. Enable optional real-time logging if needed
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**File**: `/etc/twingate/connector.conf`

```
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

**systemd Management Commands:**
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector  # boot behavior
```

## Gotchas
- Install Docker only via official channel (`get.docker.com`) — other channels may have outdated versions incompatible with Connector image requirements
- Ubuntu: only LTS versions supported
- Amazon Linux: use pre-built AMI with systemd instead of standard Linux instructions
- Stagger updates across multiple Connectors to avoid downtime
- Tokens are per-Connector; cannot be reused across Connectors
- Config file changes require service restart to take effect

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Provisioning/re-provisioning a Connector
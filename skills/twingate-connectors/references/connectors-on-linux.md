# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run as Docker containers or as a systemd service. Docker works on any Linux distro; systemd is more robust but limited to supported distributions. Both methods require tokens generated from the Twingate Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Docker works on any Linux distribution
- systemd service is lower-overhead and more robust
- Amazon Linux: use pre-built AMI with systemd pre-installed (not Docker)
- Tokens are per-Connector and cannot be shared between Connectors

## Prerequisites
- Access to Twingate Admin Console
- A Remote Network configured in Admin Console
- **Docker method**: Docker installed and running
- **systemd method**: Supported Linux distribution (see below)

## Supported Distributions (systemd)
| Distro | Versions |
|--------|----------|
| Ubuntu | 22.04 LTS, 24.04 LTS (LTS only) |
| Fedora | 39, 40 |
| CentOS | Stream 9 |
| Debian | 11 LTS, 12 LTS |

## Step-by-Step

### Docker Deployment
1. Install Docker via official channel or convenience script:
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo docker run hello-world
   ```
2. In Admin Console: Remote Networks → Remote Network → Add Connector
3. Open new Connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated command in terminal

### systemd Deployment
1. In Admin Console: Remote Networks → Remote Network → Add Connector
2. Open new Connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run the generated command in terminal
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file location**: `/etc/twingate/connector.conf`

```bash
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

**systemd Management Commands**:
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector  # boot behavior
```

## Gotchas
- Do **not** install Docker from unofficial/third-party channels — outdated versions may be incompatible with Connector image requirements
- Access and refresh tokens are unique per Connector — cannot be reused across Connectors
- Configuration file changes require `systemctl restart` to take effect
- Ubuntu: only LTS versions officially supported
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Amazon Linux AMI deployment
- Provisioning/re-provisioning Connectors
# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can be deployed as Docker containers (any distro) or as a systemd service (select distros). Systemd is the more robust option with lower overhead; Docker offers broader compatibility. Both methods require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens (access + refresh) are connector-specific and non-shareable
- Config file location (systemd): `/etc/twingate/connector.conf`
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Access to Twingate Admin Console
- Remote Network already created
- **Docker method**: Docker installed and running
- **Systemd method**: Supported Linux distribution (see below)

### Supported Distros (systemd)
| Distro | Versions |
|--------|----------|
| Ubuntu | 22.04 LTS, 24.04 LTS |
| Fedora | 39, 40 |
| CentOS | Stream 9 |
| Debian | 11 LTS, 12 LTS |

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. Admin Console → Remote Networks → select network → Add Connector
3. Click new connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated `docker run` command

### Systemd Deployment
1. Admin Console → Remote Networks → select network → Add Connector
2. Click new connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**File:** `/etc/twingate/connector.conf`

```ini
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

### systemd Management Commands
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector
```

## Gotchas
- **Docker install source matters**: Use only official Docker channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image
- **Amazon Linux**: Use the pre-built AMI deployment path instead of standard Linux instructions
- **Token sharing**: Access/refresh tokens are per-connector — cannot reuse across multiple connectors
- **Ubuntu**: Only LTS versions supported; supported until end of standard support date
- **Updates**: Stagger updates across connectors to avoid downtime; systemd and Docker have separate update guides

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Support peer-to-peer connections
- Provisioning/re-provisioning a Connector
- Amazon Linux AMI deployment
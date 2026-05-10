# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can be deployed as Docker containers (any distro) or as a systemd service (select distros). Docker offers broader compatibility; systemd is more robust with lower overhead. Both methods require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens are per-Connector and cannot be shared between Connectors
- Config file location (systemd): `/etc/twingate/connector.conf`
- Peer-to-peer connections recommended to reduce bandwidth and stay within Fair Use Policy

## Prerequisites
- Access to Twingate Admin Console
- A Remote Network with a Connector created (generates access/refresh tokens)
- **Docker method**: Docker installed and running
- **systemd method**: Supported Linux distro (Ubuntu 22.04/24.04 LTS, Fedora 39/40, CentOS Stream 9, Debian 11/12)

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console: Remote Networks → Remote Network → Add Connector
3. Click the new Connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated deploy command

### systemd Deployment
1. In Admin Console: Remote Networks → Remote Network → Add Connector
2. Click the new Connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Optionally enable real-time logging
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file**: `/etc/twingate/connector.conf`

```
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
- Install Docker only via official channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector images
- Only Ubuntu LTS versions are officially supported (not interim releases)
- Amazon Linux: use pre-built AMI deployment instead of manual Linux steps
- Access/refresh tokens are Connector-specific — cannot be reused across Connectors
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Peer-to-peer connections setup
- Provisioning/re-provisioning Connectors
- Amazon Linux AMI deployment
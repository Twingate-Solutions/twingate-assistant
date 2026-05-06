# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can be deployed as Docker containers or as a systemd service. Docker works on any Linux distro; systemd is more robust but limited to specific supported distributions. Both methods require tokens generated from the Twingate Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Docker supports any Linux distribution
- systemd service supported on specific distros only (Ubuntu, Fedora, CentOS Stream, Debian)
- Tokens (access + refresh) are connector-specific and cannot be shared between connectors
- Amazon Linux: use pre-built AMI instead

## Prerequisites
- Access to Twingate Admin Console
- For Docker: Docker installed and running
- For systemd: Supported Linux distribution
- A Remote Network configured in Twingate

## Supported Distributions (systemd)
- Ubuntu 22.04 LTS, 24.04 LTS
- Fedora 39, 40
- CentOS Stream 9
- Debian 11 LTS, 12 LTS

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. In Admin Console → Remote Networks → select network → Add Connector
3. Select new connector → choose **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated command in terminal

### systemd Deployment
1. In Admin Console → Remote Networks → select network → Add Connector
2. Select new connector → choose **Linux** option
3. Generate tokens (requires re-authentication)
4. Enable optional real-time logging if desired
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**Config file location:** `/etc/twingate/connector.conf`

```
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<token>
TWINGATE_REFRESH_TOKEN=<token>
```

**systemd Management Commands:**
```bash
sudo systemctl status twingate-connector
sudo systemctl start|stop|restart twingate-connector
sudo systemctl enable|disable twingate-connector
```

## Gotchas
- Install Docker only via official channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image
- Only Ubuntu LTS versions are officially supported (not interim releases)
- Access/refresh tokens are per-connector — cannot reuse across multiple connectors
- Stagger updates across connectors to avoid downtime
- Amazon Linux: do not use standard Linux method; use AMI deployment instead

## Related Docs
- Connector Best Practices
- Peer-to-peer connections support
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Provisioning/re-provisioning Connectors
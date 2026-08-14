---
source: https://www.twingate.com/docs/connectors-on-linux
type: docs
fetched: 2026-08-14
source_version: 1d6dcf0839977e0c6b26220d4ae2ab28afb8e520fa448a91e8928a073d83d317
---

# Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can be deployed as Docker containers (any distro) or as a systemd service (select distros). Docker offers flexibility; systemd offers lower management overhead. Both require tokens generated from the Admin Console.

## Key Information
- Two deployment methods: Docker container or systemd service
- Tokens are per-Connector and cannot be shared between Connectors
- Config file location (systemd): `/etc/twingate/connector.conf`
- Verify service: `sudo systemctl status twingate-connector`

## Prerequisites
- **Docker method**: Docker installed and running
- **systemd method**: Supported distro (see below)
- Access to Twingate Admin Console to generate tokens
- Connector created under a Remote Network in Admin Console

## Supported Distros (systemd only)
| Distro | Versions |
|--------|----------|
| Ubuntu | 22.04 LTS, 24.04 LTS |
| Fedora | 39, 40 |
| CentOS | Stream 9 |
| Debian | 11 LTS, 12 LTS |

## Step-by-Step

### Docker Deployment
1. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`
2. Admin Console → Remote Networks → Remote Network → Add Connector
3. Click new Connector → select **Docker** option
4. Generate tokens (requires re-authentication)
5. Enable optional features
6. Copy and run the generated command in terminal

### systemd Deployment
1. Admin Console → Remote Networks → Remote Network → Add Connector
2. Click new Connector → select **Linux** option
3. Generate tokens (requires re-authentication)
4. Enable optional real-time logging if desired
5. Copy and run the generated install command
6. Verify: `sudo systemctl status twingate-connector`

## Configuration Values

**File**: `/etc/twingate/connector.conf`

```ini
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access_token>
TWINGATE_REFRESH_TOKEN=<refresh_token>
```

**systemd Management Commands**:
```bash
sudo systemctl status twingate-connector
sudo systemctl start twingate-connector
sudo systemctl stop twingate-connector
sudo systemctl restart twingate-connector   # also reloads config
sudo systemctl enable twingate-connector    # auto-start at boot
sudo systemctl disable twingate-connector
```

## Gotchas
- Install Docker only via official channel (`get.docker.com`); third-party channels may have outdated versions incompatible with Connector image
- Amazon Linux: use pre-built AMI deployment instead
- Tokens are Connector-specific — cannot reuse across multiple Connectors
- Stagger updates across Connectors to avoid downtime
- Only Ubuntu LTS versions are officially supported

## Related Docs
- Connector Best Practices
- Peer-to-peer connections setup
- systemd Connector Update Guide
- Docker Connector Update Guide
- Provisioning/re-provisioning a Connector
- Amazon Linux AMI deployment
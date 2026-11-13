---
source: https://www.twingate.com/docs/connectors-on-linux
type: docs
fetched: 2026-11-13
source_version: 20e631b675ee35405cb7d3335cdaf7d9ae815113b4ef7110fab32125c9f8a5f7
trust: official
---

# How to Deploy a Connector on Linux

## Summary
Twingate Connectors on Linux can run either as a Docker container or as a native systemd service. Docker works on any distribution but has more management overhead. The systemd service is the more robust option but is supported only on specific distributions.

## Key Information
- Two deployment options: Docker container or systemd service (`twingate-connector`).
- Both are provisioned from the Admin Console: Remote Networks → select network → Add Connector → choose Docker or Linux → generate tokens → copy the generated command and run it in the terminal.
- Step 3 in the console offers optional features (Docker) or optional real-time logging (Linux).
- Amazon Linux: use the pre-built AMI, which has the systemd Connector preinstalled (see the AMI deployment instructions).
- Peer-to-peer connections are recommended for better user experience and to stay within the Fair Use Policy.
- Supported systemd distributions (tested until EOL):
  - Ubuntu 22.04 LTS and 24.04 LTS (LTS only)
  - Fedora 39, 40
  - CentOS Stream 9
  - Debian 11 and 12
- Other distributions may work but are unsupported.

## Prerequisites
- Access to the Twingate Admin Console and an existing Remote Network.
- Docker path: Docker installed from the official source and running. Verify with `sudo docker run hello-world`.
- Systemd path: a supported distribution.

## Step-by-Step
**Docker**
1. Install Docker using the official instructions for your distro (Docker's convenience script is at get.docker.com; see the source page for details).
2. In the Admin Console, add a Connector and select the Docker option.
3. Generate tokens (you will re-authenticate).
4. Enable the optional features you want.
5. Copy the generated command and run it in the terminal.

**Systemd**
1. In the Admin Console, add a Connector and select the Linux option.
2. Generate tokens and optionally enable real-time logging.
3. Copy the generated single-command installer and run it.
4. Verify: `sudo systemctl status twingate-connector`

## Configuration Values
Config file: `/etc/twingate/connector.conf`. All three settings are required:
```
TWINGATE_NETWORK=https://<account>.twingate.com
TWINGATE_ACCESS_TOKEN=<access token>
TWINGATE_REFRESH_TOKEN=<refresh token>
```
Service management commands:
```
sudo systemctl status|stop|start|restart twingate-connector
sudo systemctl enable|disable twingate-connector   # boot behavior
```
Restart the service to reload configuration changes.

## Gotchas
- Install Docker only from the official channel. Other channels may ship outdated versions incompatible with the Connector image.
- Access and refresh tokens are unique per Connector and cannot be shared across Connectors. Generate or re-provision tokens for each one.
- Only Ubuntu LTS releases are supported.
- Stagger updates across multiple Connectors to avoid downtime.

## Related Docs
- Connector Best Practices (including hardware recommendations)
- Support for peer-to-peer connections
- Fair Use Policy
- AMI deployment instructions (Amazon Linux)
- Systemd Connector Update Guide
- Docker Connector Update Guide
- Provisioning or re-provisioning a Connector
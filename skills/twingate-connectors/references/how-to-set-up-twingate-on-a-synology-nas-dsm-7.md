# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 7.0+ using Docker Compose via the built-in Container Manager. The Connector enables secure remote access to the NAS and other local network devices without VPN servers or port forwarding.

## Key Information
- Requires DSM 7.0 or later (use separate DSM 6 guide for older versions)
- Uses Container Manager's Docker Compose (Project) feature
- Connector runs with `network_mode: host` for local network visibility
- DSM web admin interface accessible at `https://<NAS-IP>:5001`

## Prerequisites
- Synology NAS running DSM 7.x
- Twingate Remote Network created in Admin Console
- Connector created with Access Token and Refresh Token generated
- Access to DSM web interface from same local network

## Step-by-Step Deployment

1. In Twingate Admin Console → Remote Network → Deploy Connector → Docker → Generate Tokens
2. In DSM File Station, create folder: `docker/twingate-connector/`
3. On local machine, create `compose.yaml`:
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
    network_mode: host
```
4. Open Container Manager → Project → Create
5. Name project `twingate-connector`, set Path to created folder, upload `compose.yaml`
6. Replace token placeholders with values from Admin Console
7. Click Next → Next → Enable "Start the project once it is created" → Done
8. Verify Connector shows as live in Admin Console

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |

Optional parameters available via [Docker Compose examples](https://www.twingate.com/docs/docker-compose).

## Update Process
1. Container Manager → Image → click "Update Available"
2. Click Update → Acknowledge warning → Update
3. New image downloads and applies automatically; no reconfiguration needed

## Gotchas
- Must be on the **same local network** as the NAS when setting up via DSM web interface
- After deployment, the NAS itself must be added as a **Resource** in Admin Console using its local IP address before it's accessible remotely
- DSM 6.x requires a different guide entirely

## Related Docs
- [Synology NAS DSM 6 Guide](https://www.twingate.com/docs/synology-nas-dsm-6)
- [Docker Compose Examples](https://www.twingate.com/docs/docker-compose)
- [Resources Guide](https://www.twingate.com/docs/resources)
- [Add Remote Network](https://www.twingate.com/docs/remote-networks)
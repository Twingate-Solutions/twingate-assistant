# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS devices running DSM 7.0+ using Docker Compose via Container Manager. The Connector enables secure remote access to the NAS and other local network devices without VPN or port forwarding.

## Key Information
- Requires DSM 7.0 or later (use separate DSM 6 guide for older versions)
- Uses Container Manager's Docker Compose (Project) feature
- Connector runs in `host` network mode to access local network resources
- After deployment, add the NAS as a Resource using its local IP address

## Prerequisites
- Synology NAS running DSM 7.0+
- Twingate Remote Network configured in Admin Console
- Container Manager installed on the NAS
- Access to DSM web interface (typically `https://X.X.X.X:5001`)
- Twingate Access Token and Refresh Token generated from Admin Console

## Step-by-Step

1. In Twingate Admin Console, create/select a Remote Network → add a Connector → generate Access Token and Refresh Token
2. In DSM File Station, create folder: `docker/twingate-connector`
3. On your local computer, create `compose.yaml` (see below)
4. In DSM Container Manager → **Project** → **Create**
5. Name project `twingate-connector`, set Path to the folder, upload `compose.yaml`
6. Replace placeholder values with actual tenant name and tokens
7. Click Next → Next → check **"Start the project once it is created"** → Done
8. Verify Connector shows as live in Admin Console
9. Add NAS as a Resource in Admin Console using its local IP address

## Configuration Values

**compose.yaml:**
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

| Parameter | Value |
|---|---|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Generated in Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated in Admin Console |
| `network_mode` | Must be `host` |

## Update Process
1. Container Manager → **Image** → click **"Update Available"**
2. Click **Update** → confirm warning
3. New image downloads and applies automatically; no reconfiguration needed

## Gotchas
- DSM 7.x uses Container Manager with Docker Compose Projects — not the older Docker app from DSM 6
- `network_mode: host` is required; do not change this
- The NAS itself must be added as a separate Resource in Admin Console after Connector deployment
- Successful deployment shows exit code 0 in Container Manager

## Related Docs
- [Synology NAS DSM 6 Guide](https://www.twingate.com/docs/synology-nas-dsm-6)
- [Docker Compose Examples](https://www.twingate.com/docs/docker-compose)
- [Resources Guide](https://www.twingate.com/docs/resources)
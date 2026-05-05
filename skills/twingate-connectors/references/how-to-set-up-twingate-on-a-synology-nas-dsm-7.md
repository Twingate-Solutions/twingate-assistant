# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 7.0+ using Docker Compose via Container Manager. The Connector enables secure remote access to the NAS and other local network devices without VPN or port forwarding. DSM 6.x users must use a separate guide.

## Key Information
- Uses Synology Container Manager's built-in Docker Compose (Project feature)
- DSM 7.2+ required for Docker Compose support
- Connector runs with `network_mode: host` for local network access
- Updates are applied in-place via Container Manager without reconfiguration

## Prerequisites
- Synology NAS running DSM 7.0 or later
- Remote Network created in Twingate Admin Console
- Connector tokens generated (Access Token + Refresh Token) from Admin Console → Remote Network → Deploy Connector → Docker
- Container Manager installed on DSM
- Access to DSM web interface (default: `https://X.X.X.X:5001`)

## Step-by-Step Deployment

1. In Twingate Admin Console, create a Remote Network and generate connector tokens (Deploy Connector → Docker → Generate Tokens)
2. In DSM File Station, create folder: `docker/twingate-connector`
3. Create `compose.yaml` locally with config below
4. In Container Manager → Project → Create, name project `twingate-connector`
5. Set Path to the created folder, upload `compose.yaml`
6. Replace placeholder values with actual tokens and tenant name
7. Click Next → Next → enable "Start the project once it is created" → Done
8. Verify Connector appears as live in Admin Console

## Configuration Values (`compose.yaml`)

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
|-----------|-------|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Generated in Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated in Admin Console |
| `network_mode` | Must be `host` |

## Update Process
1. Container Manager → Image → check for "Update Available" badge
2. Click "Update available" → Update → confirm warning
3. New image downloads and applies automatically; no token regeneration needed

## Gotchas
- DSM 6.x requires a different installation guide
- Tenant name only (not full URL) goes in `TWINGATE_NETWORK`
- After deployment, the NAS itself must be added as a Resource in Admin Console using its local IP address — the Connector alone does not grant access
- Additional options (custom DNS, local connection logging) must be configured before copying the deploy command from Admin Console

## Related Docs
- Synology NAS DSM 6 guide
- Docker Compose examples (additional connector parameters)
- Resources guide (adding NAS/devices as accessible Resources)
- Twingate Admin Console: Remote Networks
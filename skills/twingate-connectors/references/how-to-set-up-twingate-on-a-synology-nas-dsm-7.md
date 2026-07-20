# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 7.0+ using Docker Compose via Container Manager. This enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- Applies to DSM 7.0 and later only (use DSM 6 guide for older versions)
- Uses Container Manager's built-in Docker Compose (Project feature)
- Connector runs with `network_mode: host` for local network access
- DSM web admin interface typically at `https://X.X.X.X:5001`

## Prerequisites
- Synology NAS running DSM 7.0+
- Twingate Remote Network created in Admin Console
- Connector tokens (Access Token + Refresh Token) generated from Admin Console
- Container Manager installed on DSM
- Device on same local network as NAS for initial setup

## Step-by-Step

1. In Twingate Admin Console → Network → Remote Network → Deploy Connector → Docker → Generate Tokens
2. In DSM File Station, create folder: `docker/twingate-connector`
3. On local computer, create `compose.yaml` with connector config (see below)
4. Open Container Manager → Project → Create
5. Name project `twingate-connector`, set Path to created folder, upload `compose.yaml`
6. Replace placeholder values with actual tenant name and tokens
7. Click Next → Next → check "Start the project once it is created" → Done
8. Verify connector shows as live in Admin Console
9. Add NAS as a Resource in Admin Console using its local IP address

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
|---|---|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Generated from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated from Admin Console |
| `network_mode` | Must be `host` |

## Update Process
1. Container Manager → Image → check for "Update Available" badge
2. Click "Update available" → Update → confirm warning
3. Image downloads and applies to running container automatically (no reconfiguration needed)

## Gotchas
- DSM 6.x users must use the separate DSM 6 guide — this guide is DSM 7.x only
- NAS must be added as a separate Resource in Admin Console after connector deployment; connector alone does not grant access
- Additional Docker Compose parameters (custom DNS, local connection logging) available via Docker Compose examples docs
- Successful deployment shows exit code 0 in Container Manager

## Related Docs
- [Synology NAS DSM 6 guide](#) — for DSM versions prior to 7.0
- [Docker Compose examples](#) — additional connector configuration parameters
- [Resources guide](#) — adding NAS/devices as accessible resources